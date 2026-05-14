---
Plan-UID: 0326 (rev 3)
Status: READY FOR GENERATOR
Priority: HIGH
Source: Bruce, S79. "I want the whole thing in there, just as it is in the tutorial."
Supersedes: 0326 rev 2. Rev 2's port stripped the substorm cycle, narration, scale bar, and halved the duration. This rev re-ports faithfully from the tutorial source.
---

# Plan 0326 rev 3: Full Re-Port of Animated Magnetosphere SVG

## Goal

Replace the stripped-down magnetosphere animation in `build/preprocess.py` with a faithful port of the opening animation from the tutorial. The tutorial version includes the substorm cycle, narration overlays, scale bar, time readout, and full 48-second camera journey. The book version keeps the Plan 0326 UI chrome (teaser, fullscreen button, progress bar, click-to-play, deep link).

## Source of Truth

**File:** `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html`

| Component | Lines | Size |
|-----------|-------|------|
| SVG markup (`svg-opening`) | 311–415 | ~3.5 KB |
| Narration overlays + scale bar | 417–433 | ~1.5 KB |
| Utility functions | 705–771 | ~2.8 KB |
| Opening IIFE (camera + substorm) | 774–1405 | ~28 KB |
| **Total animation code** | | **~36 KB** |

## What to Replace

**In `build/preprocess.py`:** Replace the entire `MS_ANIM_OPENING` string constant (currently lines 3339–3611) and the `inject_ms_animated_opening()` function with the faithful port. The function signature and pipeline call remain the same.

## Porting Rules

### 1. SVG Markup — Port Faithfully, Rename IDs

Port all SVG elements from tutorial lines 311–415. Every element. Specifically including:

**Substorm group (tutorial lines 401–412):**
```
open-substorm (group)
  open-nenl (near-Earth neutral line ellipse, glowing)
  open-flow-particles (group, 10 particles built by JS)
  open-aurora-n (aurora north ellipse)
  open-aurora-s (aurora south ellipse)
  open-aurora-label ("Aurora" text)
  open-phase-label (Growth/Onset/Expansion/Recovery/Quiet)
  open-substorm-label ("Substorm" bold text)
  open-energy-note ("Energy accumulates in the plasma sheet...")
  open-discharge-note ("...until it discharges as a substorm")
```

**All IDs must be prefixed `mso-`** to avoid collision with book elements. Mapping: `open-sun-group` → `mso-sun-group`, `open-substorm` → `mso-substorm`, etc. The tutorial uses `open-` prefix; the book uses `mso-` prefix.

**Two extra sun streamers** the port dropped (tutorial lines 353–354, the outermost pair at opacity 0.15) — restore them.

**Initial viewBox:** `0 0 1600 900` (full scene, Sun left, Earth right) — NOT the zoomed-in poster frame from rev 2. The poster frame is handled by a custom initial state set in JS (see §5).

### 2. Narration Overlays — Port Faithfully

Port the 6 narration divs from tutorial lines 418–423:

```html
<div class="mso-narr" id="mso-narr-1" style="top:55%;left:6%;max-width:380px;">One hundred and fifty million kilometres away, the Sun exhales. A million tonnes of charged plasma per second.</div>
<div class="mso-narr" id="mso-narr-2" style="top:58%;right:6%;text-align:right;max-width:360px;">Racing outward at four hundred kilometres per second. It has been doing this for four and a half billion years.</div>
<div class="mso-narr" id="mso-narr-3" style="top:65%;left:50%;transform:translateX(-50%);text-align:center;max-width:300px;">Earth stands in the way.</div>
<div class="mso-narr" id="mso-narr-4" style="top:60%;right:6%;text-align:right;max-width:340px;">A magnetic shield &mdash; invisible, enormous &mdash; deflects the wind around the planet.</div>
<div class="mso-narr" id="mso-narr-5" style="top:65%;left:6%;max-width:360px;">This rhythm is four and a half billion years old&mdash;older than life on Earth. The magnetosphere has never stopped breathing.</div>
<div class="mso-narr" id="mso-narr-6" style="top:72%;right:6%;text-align:right;max-width:380px;">The Moon passes through the magnetotail once every orbit. Sixty Earth-radii out.</div>
```

CSS for narration (add to the `<style>` block):
```css
.mso-narr{position:absolute;color:rgba(255,255,255,0.9);font-family:Georgia,serif;font-size:14px;line-height:1.6;opacity:0;transition:opacity 0.3s;pointer-events:none;z-index:5;text-shadow:0 1px 4px rgba(0,0,0,0.8)}
```

Narration timing array in JS (tutorial lines 1071–1078):
```js
var narrations=[
  [0.02, 0.18, 'mso-narr-1'],
  [0.20, 0.32, 'mso-narr-2'],
  [0.34, 0.43, 'mso-narr-3'],
  [0.44, 0.57, 'mso-narr-4'],
  [0.59, 0.75, 'mso-narr-5'],
  [0.77, 0.94, 'mso-narr-6']
];
```

### 3. Scale Bar + Time Readout — Port Faithfully

Port the scale indicator from tutorial lines 425–431. Place inside the `mso-container` div:

```html
<div class="mso-key" id="mso-key">
  <div id="mso-time-text"></div>
  <div style="display:flex;align-items:center;gap:8px;">
    <div id="mso-scale-bar" style="width:80px;height:4px;background:#ffb347;border-radius:2px;"></div>
    <span id="mso-scale-text">150 million km</span>
  </div>
</div>
```

CSS:
```css
.mso-key{position:absolute;bottom:20px;left:24px;z-index:5;pointer-events:none;font-family:system-ui;color:#999;font-size:12px}
```

Port the full scale + time-rate computation from tutorial lines 1277–1318 (logarithmic interpolation between AU-scale and RE-scale based on zoom level, time compression readout).

### 4. Utilities — Port All

Port ALL utility functions from tutorial lines 705–771 **inside the IIFE**:

- `svgEl(tag, attrs, parent)` — already present, keep
- `ease(t)` — **MISSING, add:** `function ease(t){return t<0.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;}`
- `lerp(a, b, t)` — **MISSING, add:** `function lerp(a,b,t){return a+(b-a)*t;}`
- `clamp(v, lo, hi)` — already present, keep
- `boundaryPts(r0, alpha, nPts, tailLen)` — already present, keep
- `ptsToPath(pts, cx, cy, scale)` — already present, keep
- `dipoleLine(L, nPts)` — already present, keep
- `catmullRom(pts, t)` — **MISSING, add** (tutorial lines 757–771)
- `reducedMotion` check — **MISSING, add:** `var reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;`

### 5. Animation JS — Port the Full Opening IIFE

Port the IIFE from tutorial lines 775–1405. This is the heart of the animation. Key sections:

**Particle pools (port exact counts):**
- 80 wind particles (50 ions + 30 electrons) — rev 2 had 60
- 30 front-deflection particles — rev 2 had 20
- 6 hero particles — same
- 10 substorm flow particles — **MISSING entirely, add**

**Camera keyframes (tutorial lines 1030–1048):**
Use the tutorial's 17 keyframes exactly. These start wide (Sun visible) and pan Sun→Earth. Do NOT use rev 2's reversed camera (Earth-first).

```js
var KF=[
  [0.00,    0,     0,  1600,  900],
  [0.06,    0,     0,  1600,  900],
  [0.11,    0,    80,  1200,  675],
  [0.16,   50,   150,  1000,  563],
  [0.22,  200,   140,  1200,  675],
  [0.28,  400,   150,  1100,  619],
  [0.34,  650,   170,   950,  534],
  [0.39,  900,   190,   750,  422],
  [0.43, 1100,   200,   600,  338],
  [0.49, 1100,   200,   600,  338],
  [0.54, 1050,   180,   700,  394],
  [0.57, 1000,   160,   900,  506],
  [0.67, 1000,   160,   900,  506],
  [0.76,  700,    50,  1400,  788],
  [0.86,  700,    50,  1400,  788],
  [0.94, 1000,   160,   900,  506],
  [1.00, 1000,   160,   900,  506]
];
```

**Duration:** `var DURATION=48000;` (48 seconds, not 25)

**`updateOpen(ts)` function (tutorial lines 1084–1357):** Port in full:
- Camera interpolation
- Narration fade in/out (tutorial lines 1096–1105)
- Sun visibility + corona pulse
- Sun label with pulse (tutorial lines 1115–1118)
- Front-view MS opacity
- Front wind deflection (30 particles)
- Hero particle deflection (approach/arc/depart)
- Side-view MS with breathing
- Moon orbit + label (steady during reveal, pulse otherwise)
- MS labels
- Solar wind particles (80, with MP deflection)
- Scale bar computation (tutorial lines 1277–1318)
- Time rate computation with logarithmic interpolation
- Wind label (repositioned during substorm view at line 1328)
- Moon label (steady during reveal, tutorial lines 1331–1340)
- Completion handler: at t>=1.0, transition to substorm loop

**`substormLoop(ts2)` function (tutorial lines 894–1021):** Port in full. This is the critical missing piece. 22-second repeating cycle:

| Phase | t range | Visual |
|-------|---------|--------|
| Growth | 0–0.36 | Tail stretches (50→70 RE), plasma sheet thins (gap 1.5→0.7), flow particles accumulate tailward, plasma sheet glow intensifies, energy note fades in |
| Onset | 0.36–0.41 | NENL flash, tail at max extension |
| Expansion | 0.41–0.55 | Flow particles burst earthward (color shift orange→yellow), discharge note appears, "Substorm" label fades in, tail retracts |
| Recovery | 0.55–0.73 | Aurora brightens (N+S ellipses expand), "Substorm" label fades out |
| Quiet | 0.73–1.0 | Return to baseline, aurora fades, energy/discharge notes gone |

The substorm loop also:
- Updates magnetopause and bow shock paths every frame (breathing + tail extension)
- Updates plasma sheet gap (thinning during growth, expanding during expansion)
- Manages phase label text
- Repositions wind label into substorm view
- Continues moon orbit
- Continues wind particle movement with deflection

### 6. Book-Specific Adaptations

Keep these from rev 2 — they are correct for the book context:

- **Poster frame (paused initial state):** Set initial viewBox to `1000 160 900 506` (side view of MS) and show side-view elements. This is the static poster the reader sees before pressing play. When play starts, the animation resets to viewBox `0 0 1600 900` and runs the full 48s camera journey. The tutorial's `reducedMotion` static view (lines 1399–1403) is the right poster state.
- **Click-to-play:** Default paused. Click/tap or ▶ button to start. Space key toggles.
- **Fullscreen button:** ⛶ top-right, same as rev 2.
- **Progress bar:** 2px green bar, 48s fill time.
- **Mobile teaser:** Same pattern — static poster + "Play Fullscreen" button at <768px.
- **Deep link:** `id="dl:ms-opening"` on the figure.
- **IIFE wrapping:** All code inside `(function(){...})();`
- **`<script>` after `</figure>`**

**Adaptation: substorm loop ending.** The tutorial loops substormLoop forever. In the book, after ONE full substorm cycle (22s), auto-pause and return to poster frame. The reader can replay. Total animation: 48s camera + 22s substorm = ~70s, then done. This avoids an infinite loop that drains battery on a book page.

**Adaptation: play/pause/reset controls.** The tutorial uses `toggleOpen()` and `restartOpen()` as global functions. The book uses click-on-container + ▶ button. Keep the rev 2 event listeners but wire them to the tutorial's logic. When paused mid-camera-journey, resume from where paused. When paused during substorm, resume substorm. Reset = full restart from camera beginning.

**Adaptation: narration positioning.** Narration divs must be inside `.mso-container` (positioned relative) so they stay within the figure. The tutorial has them at page level. Add `position:relative` to the container and the narrations will position correctly within it.

### 7. ID Mapping Table

Every tutorial ID maps to a book ID. The Generator must use this mapping consistently in both SVG markup and JS:

| Tutorial ID | Book ID |
|-------------|---------|
| `svg-opening` | `mso-svg` |
| `open-sun-group` | `mso-sun-group` |
| `open-corona` | `mso-corona` |
| `open-sun` | (unnamed, same structure) |
| `open-streamers` | (unnamed, same structure) |
| `open-sun-label` | `mso-sun-label` |
| `open-wind-particles` | `mso-wind-particles` |
| `open-front-ms` | `mso-front-ms` |
| `open-front-shield` | `mso-front-shield` |
| `open-front-bowshock` | `mso-front-bowshock` |
| `open-side-ms` | `mso-side-ms` |
| `open-mp` | `mso-mp` |
| `open-bs` | `mso-bs` |
| `open-ps` | `mso-ps` |
| `open-fieldlines` | `mso-fieldlines` |
| `open-earth` | `mso-earth` |
| `open-moon-group` | `mso-moon-group` |
| `open-moon-orbit` | (unnamed circle) |
| `open-moon` | `mso-moon` |
| `open-moon-label` | `mso-moon-label` |
| `open-wind-label` | `mso-wind-label` |
| `open-ms-labels` | `mso-ms-labels` |
| `open-lbl-bs` | `mso-lbl-bs` |
| `open-lbl-mp` | `mso-lbl-mp` |
| `open-lbl-ps` | `mso-lbl-ps` |
| `open-lbl-cusp-n` | `mso-lbl-cusp-n` |
| `open-lbl-cusp-s` | `mso-lbl-cusp-s` |
| `open-lbl-orbit` | `mso-lbl-orbit` |
| `open-substorm` | `mso-substorm` |
| `open-nenl` | `mso-nenl` |
| `open-flow-particles` | `mso-flow-particles` |
| `open-aurora-n` | `mso-aurora-n` |
| `open-aurora-s` | `mso-aurora-s` |
| `open-aurora-label` | `mso-aurora-label` |
| `open-phase-label` | `mso-phase-label` |
| `open-substorm-label` | `mso-substorm-label` |
| `open-energy-note` | `mso-energy-note` |
| `open-discharge-note` | `mso-discharge-note` |
| `open-key` | `mso-key` |
| `open-time-text` | `mso-time-text` |
| `open-scale-bar` | `mso-scale-bar` |
| `open-scale-text` | `mso-scale-text` |
| `narr-1` through `narr-6` | `mso-narr-1` through `mso-narr-6` |
| `sun-core-grad` | `mso-sun-core` |
| `sun-corona-grad` | `mso-sun-corona` |
| `open-earth-grad` | `mso-earth-grad` |
| `ms-front-grad` | `mso-front-grad` |
| `open-glow` | `mso-glow` |
| `title-safe-clip` | `mso-clip` |

### 8. Gradient/Filter ID Mapping

The tutorial's `<defs>` use IDs like `sun-core-grad`, `open-glow`. These MUST be renamed to `mso-*` because the book has other SVGs with potential ID collisions. Update every `url(#...)` and `filter="url(#...)"` reference.

## Files to Modify

| File | Change |
|------|--------|
| `build/preprocess.py` | Replace `MS_ANIM_OPENING` constant + update `inject_ms_animated_opening()` if needed |

## Files to Read First

1. This plan (complete spec)
2. `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html` lines 311–415 (SVG), 417–433 (narration+scale), 705–771 (utilities), 774–1405 (animation JS)
3. `~/software/relinquishment/build/preprocess.py` lines 3339–3636 (current code to replace)

## Acceptance Criteria

- [ ] All SVG elements from tutorial lines 311–415 present (with mso- prefix)
- [ ] 6 narration overlays present and timed correctly
- [ ] Scale bar + time readout present and computed correctly
- [ ] 80 wind particles (50 ion + 30 electron)
- [ ] 30 front-deflection particles
- [ ] 6 hero particles with approach/arc/depart
- [ ] 10 substorm flow particles with growth accumulation + expansion burst
- [ ] Camera: 17 keyframes, 48s, Sun-first direction (tutorial's KF table)
- [ ] substormLoop: 22s cycle with Growth/Onset/Expansion/Recovery/Quiet
- [ ] NENL flash, aurora (N+S), phase label, substorm label, energy/discharge notes
- [ ] Magnetopause + bow shock update every frame during substorm (breathing + tail extension)
- [ ] Plasma sheet gap modulation (thinning during growth, expanding during expansion)
- [ ] Auto-pause after one substorm cycle (~70s total)
- [ ] Poster frame: side-view MS (viewBox 1000 160 900 506), paused on load
- [ ] Click-to-play, fullscreen, progress bar, mobile teaser — all working
- [ ] `reducedMotion`: show static side-view, play button works on click
- [ ] Deep link dl:ms-opening resolves
- [ ] verify-deep-links.py passes
- [ ] No JS console errors
- [ ] No CSS collisions with book styles (all classes mso-* prefixed)
- [ ] `make html` completes clean
- [ ] Existing static imagemaps (Earth, Jupiter, Saturn) still present and functional

## Do NOT

- Strip, simplify, or "optimize" the animation — port faithfully
- Change the camera direction (must be Sun-first, following the wind to Earth)
- Reduce particle counts
- Omit the substorm cycle
- Omit narrations
- Omit the scale bar
- Use the poster-frame-first camera from rev 2
- Put utility functions in global scope
- Change any other function in preprocess.py
- Modify the tutorial source file

## Handoff Prompt

```
You are the Generator. Plan 0326 rev 3 — full MS animation re-port.
Read ~/software/relinquishment/plans/0326-ms-animation-report.md

Replace the MS_ANIM_OPENING constant in build/preprocess.py (lines 3339–3611)
with a FAITHFUL port of the opening animation from:
~/software/persistent-ai-collaboration/tutorial-magnetosphere.html

READ THE TUTORIAL SOURCE FIRST (lines 311-415 SVG, 417-433 narration,
705-771 utilities, 774-1405 animation JS). Then read the plan for the
complete spec including ID mapping, adaptations, and acceptance criteria.

The current code is a stripped version missing the substorm cycle, narration,
scale bar, and half the particles. Port EVERYTHING. Do not simplify.

Key adaptations for book context (detailed in plan):
- IDs: open-* → mso-* (full mapping table in plan)
- Poster frame: start paused at side-view (1000 160 900 506)
- Click-to-play + fullscreen (keep rev 2 UI chrome)
- One substorm cycle then auto-pause (~70s total)
- Narration divs inside mso-container (not page level)
- Progress bar over full 70s

After replacing, rebuild:
cd ~/software/relinquishment && make html 2>&1 | tail -10

Open in browser:
garcon-url-handler "file:///media/fuse/crostini_9dd5bcbb8a024ec1145e1a9be84b9b2890959b90_termina_penguin/software/relinquishment/docs/Relinquishment.html#dl:ms-opening"

Verify: animation plays Sun-first, narration appears, substorm cycle runs
(Growth→Onset→Expansion→Recovery→Quiet with visible aurora, NENL flash,
phase labels, flow burst), scale bar updates, auto-pauses after one cycle.

Commit: "Plan 0326 rev 3: faithful MS animation re-port with substorm cycle"
Report: what's working, what might need tuning, total size added.
```

---

*Plan 0326 rev 3, S79, 2026-05-13. Auditor: Argus.*
*Rev 2 was a stripped-down port. Rev 3 re-ports faithfully from tutorial source.*
*Estimated generator time: ~60 min (large constant replacement + testing).*
