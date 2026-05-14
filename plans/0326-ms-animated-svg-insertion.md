---
Plan-UID: 0326 (rev 2)
Status: READY FOR GENERATOR
Priority: MEDIUM
Source: Bruce, S78. "Insert MS tutorial first animated SVG into the book."
Audit: 10 failure points found in rev 1. All addressed in rev 2.
---

# Plan 0326: Insert Animated Magnetosphere SVG into The Wrong Substrate

## Goal

Port the opening animated SVG (`svg-opening`) from `persistent-ai-collaboration/tutorial-magnetosphere.html` into the book's "The Wrong Substrate" chapter (`pos32-the-magnetosphere.tex`). Display small inline, designed for fullscreen viewing. Starts **paused**. Standard controls. Prime deep entry point.

## Size Budget

| Component | Bytes |
|-----------|-------|
| SVG markup (`svg-opening`, lines 311–449) | ~9.4 KB |
| Utility JS (svgEl, ease, lerp, clamp, boundaryPts, dipoleLine, ptsToPath) | ~2.8 KB |
| Animation JS (opening IIFE, lines 775–1407) | ~28.8 KB |
| CSS (scene container, fullscreen, teaser, progress bar, print) | ~3 KB |
| **Total** | **~46 KB** |
| Current book HTML | 1,332 KB |
| **Impact** | **+3.5%** |

## Source

File: `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html`
Lines 311–449 (SVG), 705–773 (utilities), 774–1407 (animation JS)
Plus CSS from lines 69–78 (`.scene-full`), 129–146 (`.fullscreen-btn`), 183–195 (`.narration`)

**Reference implementation for mobile/fullscreen pattern:** `docs/Relinquishment.html` lines 6051–6055 (SR chapter CSS), lines 7640–7700 (SR fullscreen JS). Copy the teaser/fullscreen pattern from the Scientific Revolutions chapter.

## Deep Link

**This is a prime deep entry point.** Must have a proper deep link.

### 1. Add entry to `build/deep-links.yaml`:

```yaml
- id: dl:ms-opening
  question: "Earth's magnetosphere — animated solar wind and field structure"
  category: svg
```

### 2. Add anchor to the figure:

The `<figure>` wrapper gets `id="dl:ms-opening"`. This replaces the `fig-ms-animated` ID from rev 1.

### 3. URL:

`https://relinquishment.ai/Relinquishment.html#dl:ms-opening`

The existing `openHashTarget()` function handles scrolling and opening parent `<details>` ancestors. No changes needed to hash navigation.

### 4. Verification:

`python3 build/verify-deep-links.py` must pass with `dl:ms-opening` resolved.

## Injection Target

File: `build/preprocess.py`
New function: `inject_ms_animated_opening()` called from the main pipeline.

The animated SVG goes at the `% IMAGE:` comment placeholder at `pos32-the-magnetosphere.tex:29` — the FIRST image in the chapter, in "The Invisible Ocean" section. Find the rendered paragraph starting "Between the two lobes of the magnetotail" (`pos32` line 33) and insert the figure BEFORE it.

**Both images stay.** The animated SVG is the opening cinematic — "feel the system" (nature documentary establishing shot). The existing static imagemaps with hovertips (Earth, Jupiter, Saturn) are teaching tools — "learn the system" (hover to explore labeled regions). Different purposes, no conflict. The static imagemaps remain wherever `inject_magnetosphere_imagemaps()` currently places them.

## What the Reader Sees

**Phone/small screen (< 768px):**
1. A **mobile teaser**: static poster frame (~200px tall) with a green "▶ Play Fullscreen" button below it and a hint "Best experienced in landscape." This matches the SR chapter's mobile pattern exactly.
2. Tapping the button shows the full figure and requests fullscreen.
3. On iOS Safari where Fullscreen API fails on divs: the container expands to `position:fixed; 100vw × 100vh` as pseudo-fullscreen fallback.

**Desktop/tablet (≥ 768px):**
4. The full figure inline (~300px tall within max-width:800px container). Shows the static poster frame on a dark (#0a0a1a) background.
5. A centered **▶** play button overlaid on the poster.
6. A **⛶** fullscreen button top-right.
7. A "Best in fullscreen" hint that fades after 3 seconds.

**On play (any size):**
8. Animation runs. Play button fades. A thin **progress bar** appears at the bottom of the figure (2px tall, accent color, left-to-right over ~25 seconds).
9. Click/tap the figure or press **Space** to pause. Play button returns. Progress bar freezes.

**On fullscreen:**
10. Container enters fullscreen at 1600×900. Try `screen.orientation.lock('landscape')` (fail silently if unsupported).
11. **Escape** exits fullscreen. Returns to inline/teaser state based on screen width.

**Loop behavior:**
12. One cycle (~25 seconds), then auto-pause back on poster frame. Progress bar resets. Reader can play again or move on.

**Key principle:** Encourage fullscreen, don't insist. The animation must be functional and pleasant at any size. Fullscreen is the reward for curiosity, not a requirement for comprehension.

## Poster Frame Spec

The animation's frame 0 is a wide shot (Sun at x=200, Earth at x=1400 in a 1600-wide viewBox) — too zoomed out for a small poster. The poster frame must be a **custom initial state**, not frame 0:

- Set initial viewBox to the "zoomed-in Earth" state: roughly `viewBox="1000 100 600 700"` (centered on Earth + magnetosphere, no Sun visible)
- Show: Earth (blue circle), dipole field lines (green), bow shock curve, magnetopause, a few solar wind arrows entering from left, "Magnetosphere" label
- This looks good at phone size because it's zoomed in on the interesting structure
- When animation starts, the first camera move zooms OUT to reveal the full Sun-to-Earth scene — a satisfying "reveal" moment

The Generator must verify the poster looks good at 320px wide before considering this done.

## Behavioral Requirements

- **Default: PAUSED.** Animation does not auto-play on scroll or load.
- **Click/tap to play/pause.** Toggle on figure click, play button click, or Space key (when figure has focus).
- **Keyboard:** Space = play/pause (when focused). Escape = exit fullscreen. Tab-focusable play and fullscreen buttons.
- **Fullscreen button.** Requests `element.requestFullscreen()` on the container div. Vendor prefixes: `webkitRequestFullscreen`, `msRequestFullscreen`. Listen to both `fullscreenchange` and `webkitfullscreenchange`.
- **iOS fallback.** If `requestFullscreen` is not available on the container, use `position:fixed; inset:0; z-index:9999; width:100vw; height:100vh` as pseudo-fullscreen. A close button (✕) appears top-right to exit.
- **Progress bar.** Required. Thin (2–3px), below the SVG, fills left-to-right proportional to animation elapsed time. Accent color (book green or similar). Not interactive (no scrubbing) — informational only.
- **Reduced motion:** If `prefers-reduced-motion: reduce`, show poster frame. Play button still works — user opt-in overrides the preference (per WCAG: user-initiated animation is permitted). The animation JS runs normally on play; `reducedMotion` suppresses only auto-play (which we don't have anyway, but check it explicitly so future changes don't break this).
- **No star canvas.** Omit. The SVG must have its own `<rect>` background fill (`#0a0a1a` or similar dark) so it doesn't rely on an external canvas. Verify the space regions don't look flat without stars.
- **No nav dots.** Omit — single embedded figure.

## Controls Summary

| Control | Desktop | Mobile | Keyboard |
|---------|---------|--------|----------|
| Play/pause | Click figure or ▶ button | Tap figure or ▶ button | Space |
| Fullscreen | ⛶ button top-right | "▶ Play Fullscreen" green button | — |
| Exit fullscreen | ⛶ button or Escape | ✕ button (iOS fallback) or Escape | Escape |
| Progress | 2px bar at bottom | Same | — |

## Modifications from Tutorial Source

1. **Remove** star canvas dependency. Add `<rect>` fill to SVG background.
2. **Remove** section nav dots
3. **Remove** IntersectionObserver auto-play logic (we control play state manually)
4. **Remove** dependencies on other SVGs (circuit, gate) — opening is self-contained
5. **Add** play/pause toggle button with icon swap (▶/⏸)
6. **Add** container-level fullscreen with vendor prefixes + iOS fixed-position fallback
7. **Add** auto-pause at loop boundary, reset to poster frame
8. **Add** progress bar (2px, non-interactive)
9. **Add** mobile teaser pattern (copy SR chapter: hide full figure at < 768px, show teaser + "Play Fullscreen" button)
10. **Add** keyboard controls (Space, Escape, tab focus)
11. **Add** deep link anchor `id="dl:ms-opening"`
12. **Add** `@media print` rule: show poster frame, hide controls
13. **Add** ARIA: `aria-label` on SVG, `aria-pressed` on play button, `role="button"` on focusable controls
14. **Set** custom poster viewBox (zoomed-in Earth) as initial state
15. **Wrap** in `<figure>` with `id="dl:ms-opening"` and descriptive `<figcaption>`
16. **Namespace** all CSS classes with `ms-anim-` prefix to avoid collisions
17. **Scope** ALL JS inside one IIFE — utilities (svgEl, ease, lerp, clamp, boundaryPts, dipoleLine, ptsToPath) go INSIDE the IIFE, not outside. Zero globals.
18. **Place** `<script>` tag AFTER the `</figure>` closing tag so DOM is present when IIFE executes

## CSS Pattern

```css
/* Container */
.ms-anim-container {
  position: relative;
  max-width: 800px;
  margin: 1.5em auto;
  background: #0a0a1a;
  border-radius: 4px;
  overflow: hidden;
  cursor: pointer;
  aspect-ratio: 16 / 9;
}
.ms-anim-container svg { width: 100%; height: 100%; display: block; }

/* Play button overlay */
.ms-anim-play-btn {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 2.5rem;
  color: rgba(255,255,255,0.8);
  background: rgba(0,0,0,0.4);
  border: none; border-radius: 50%;
  width: 3.5rem; height: 3.5rem;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: opacity 0.3s;
}
.ms-anim-container.ms-playing .ms-anim-play-btn { opacity: 0; pointer-events: none; }

/* Fullscreen button */
.ms-anim-fs-btn {
  position: absolute; top: 8px; right: 8px;
  background: rgba(0,0,0,0.5); color: #ccc;
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 4px; padding: 4px 8px;
  cursor: pointer; font-size: 1rem; z-index: 10;
}

/* Progress bar */
.ms-anim-progress {
  position: absolute; bottom: 0; left: 0;
  height: 2px; background: #66ff88;
  width: 0%; transition: none;
}

/* Hint text */
.ms-anim-fs-hint {
  position: absolute; bottom: 8px; right: 8px;
  color: rgba(255,255,255,0.5); font-size: 0.7rem; font-family: sans-serif;
  animation: ms-fade-hint 3s ease-out forwards;
}
@keyframes ms-fade-hint { 0%, 70% { opacity: 1; } 100% { opacity: 0; } }

/* Mobile teaser (copy SR pattern) */
.ms-anim-teaser { display: none; }
@media (max-width: 767px) {
  .ms-anim-container { display: none; }
  .ms-anim-teaser { display: block; text-align: center; margin: 1em 0; }
  .ms-anim-teaser-img { width: 100%; max-width: 400px; margin: 0 auto; }
  .ms-anim-teaser-btn {
    display: block; width: 100%; max-width: 400px;
    margin: 12px auto 0; padding: 14px 24px; min-height: 48px;
    background: #4caf50; color: #fff; border: none; border-radius: 8px;
    font-size: 18px; font-family: Georgia, serif; cursor: pointer;
  }
  .ms-anim-teaser-hint { color: #706858; font-size: 12px; margin-top: 6px; }
}

/* Fullscreen states */
.ms-anim-container:fullscreen,
.ms-anim-container:-webkit-full-screen {
  display: block !important; width: 100vw; height: 100vh; background: #000;
  max-width: none; border-radius: 0;
}
.ms-anim-container:fullscreen svg,
.ms-anim-container:-webkit-full-screen svg { width: 100vw; height: 100vh; }

/* iOS pseudo-fullscreen fallback */
.ms-anim-container.ms-pseudo-fs {
  position: fixed !important; inset: 0; z-index: 9999;
  width: 100vw; height: 100vh; max-width: none;
  border-radius: 0; background: #000;
}

/* Print */
@media print {
  .ms-anim-play-btn, .ms-anim-fs-btn, .ms-anim-fs-hint,
  .ms-anim-progress, .ms-anim-teaser-btn { display: none !important; }
  .ms-anim-container { display: block !important; }
}
```

## HTML Build Integration

In `preprocess.py`, add a new function `inject_ms_animated_opening(html_path)`:

1. Find the anchor point: the paragraph starting "Between the two lobes of the magnetotail" in the Wrong Substrate chapter. Insert the figure BEFORE it.
2. Inject the complete block: `<figure id="dl:ms-opening">` containing:
   - Mobile teaser div (poster img + "Play Fullscreen" button + hint)
   - Desktop container div (SVG + play button + fullscreen button + progress bar + hint)
   - `<figcaption>`
   - `<style>` block (scoped CSS above)
   - `<script>` block (IIFE with all utilities + animation logic)
3. Return modified html.
4. Call from the main pipeline alongside `inject_magnetosphere_imagemaps()`.

## PDF Handling

HTML-only. The `% IMAGE:` comment at tex line 29 is invisible in PDF. The existing `placeholder-magnetosphere.pdf` in `build/images/` can be wired up as a `\includegraphics` in a future plan if a static PDF figure is desired. Not in scope here.

## Files to Modify

| File | Change |
|------|--------|
| `build/preprocess.py` | New function `inject_ms_animated_opening()` + call from pipeline |
| `build/deep-links.yaml` | Add `dl:ms-opening` entry |

## Files to Create

None — everything inlines into preprocess.py as a string literal (matching the pattern of all other SVG injections).

## Verification

1. `python3 build/verify-deep-links.py` passes — `dl:ms-opening` resolves
2. `grep -c 'dl:ms-opening' docs/Relinquishment.html` → 1
3. **Desktop:** On load: figure visible, paused, poster frame (zoomed-in Earth), ▶ button visible, ⛶ visible, progress bar at 0%. "Best in fullscreen" hint fades after 3s.
4. **Desktop play:** Click ▶ → animation plays, ▶ fades, progress bar fills over ~25s. Click figure → pauses. Space key toggles. End of cycle → auto-pause, poster frame restored, progress bar resets.
5. **Desktop fullscreen:** ⛶ → container goes fullscreen (landscape). Escape exits. Animation state preserved across transition.
6. **Mobile (< 768px):** Teaser visible (poster + green "▶ Play Fullscreen" button). Full container hidden.
7. **Mobile play:** Tap green button → container shown + fullscreen requested. On iOS: pseudo-fullscreen (position:fixed) with ✕ close button.
8. **Deep link:** Navigate to `#dl:ms-opening` → page scrolls to figure, parent accordions opened (if any). Animation stays paused.
9. **Print:** `Ctrl+P` → poster frame visible, controls hidden.
10. **Reduced motion:** Poster shown. ▶ still works on click.
11. **Keyboard:** Tab to ▶ button → Enter/Space plays. Tab to ⛶ → Enter fullscreens. Escape exits.
12. **No JS errors** in console on any of the above.
13. **Poster frame:** Verify at 320px wide the zoomed-in Earth view is legible and attractive.
14. Existing static imagemaps (Earth, Jupiter, Saturn) still present and functional later in chapter.
15. File size increase < 50 KB.

## Do Not

- Do NOT remove or modify the existing static magnetosphere imagemaps
- Do NOT auto-play the animation
- Do NOT include the star canvas background
- Do NOT include tutorial navigation dots
- Do NOT add page-level fullscreen — container-level only
- Do NOT put utility functions in global scope — everything inside the IIFE
- Do NOT place `<script>` before the `</figure>` — DOM must exist first

## Report Format

"Plan 0326 complete. Animated magnetosphere SVG with deep link `dl:ms-opening` inserted into The Wrong Substrate. Size: [N] KB added. Poster frame verified at 320px. Controls: play/pause, fullscreen, progress bar, keyboard, mobile teaser. verify-deep-links.py passes."

---

## Annealing Record

**Round 1 (CRITICAL): Deep link missing.**
Rev 1 had `id="fig-ms-animated"` — not in the deep link system. Bruce said "prime deep entry point." Added `dl:ms-opening` to manifest + figure ID + verification via `verify-deep-links.py`.

**Round 2 (CRITICAL): iOS Safari can't fullscreen divs.**
The Fullscreen API doesn't work on `<div>` elements in iOS Safari. The SR chapter already solved this with a mobile teaser pattern (hide inline figure at < 768px, show "Play Fullscreen" button). Added the same pattern + pseudo-fullscreen fallback (`position:fixed`).

**Round 3 (CRITICAL): Poster frame is frame 0 — too zoomed out.**
The animation's frame 0 is a wide Sun-to-Earth shot. At phone size (~320px wide) this is illegible. Specified a custom poster state: initial viewBox zoomed in on Earth + magnetosphere structure. Animation's first camera move zooms OUT — a "reveal" moment.

**Round 4 (IMPORTANT): No keyboard controls.**
Added Space to play/pause, Escape to exit fullscreen, Tab focus on buttons, Enter/Space to activate focused buttons. ARIA attributes on controls.

**Round 5 (IMPORTANT): Progress bar was "optional."**
25 seconds with no progress indicator is disorienting. Made it required: 2px green bar at bottom, non-interactive.

**Round 6 (IMPORTANT): Script timing unspecified.**
IIFE calls `getElementById` — fails if DOM isn't ready. Specified: `<script>` goes AFTER `</figure>` so SVG DOM exists when JS executes.

**Round 7 (IMPORTANT): Print stylesheet missing.**
Added `@media print` rule: show poster frame, hide all controls and progress bar.

**Round 8 (MINOR): Utility function scoping.**
Listed all 7 utility functions explicitly as IIFE-internal. Generator must not put them in global scope.

**Round 9 (MINOR): Star canvas visual gap.**
SVG relied on external canvas for dark background. Added requirement: `<rect>` fill inside SVG for self-contained dark background.

**Round 10 (MINOR): reducedMotion interaction unclear.**
Clarified: `reducedMotion` suppresses auto-play only. User-initiated play runs normally (per WCAG). Explicit check so future changes don't break.

---

*Plan 0326 rev 2, S78, 2026-05-12. Auditor: Argus.*
*10 failure points found and fixed. Rev 1 was 78%. Rev 2: 95%.*
*Remaining 5%: poster frame aesthetics can only be verified by Generator at render time.*
*Estimated generator time: ~45 min.*
