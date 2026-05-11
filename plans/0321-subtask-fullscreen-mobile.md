# Subtask: Fullscreen Button + Mobile Teaser

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fullscreen button, mobile shows teaser + play fullscreen`
**Read first:** The existing HTML file (focus on the outer HTML/CSS wrapper and controls).

## Context

This HTML file gets embedded into a book (responsive web reader). The book text
must remain readable on phones. The animation is an interruption in the text flow —
on desktop it plays inline, on phone it becomes a compact card that invites the
reader to go fullscreen. The surrounding book layout handles its own responsiveness;
this file just needs to not break it and to degrade cleanly.

## What to Build

### 1. Fullscreen Button (all viewports)

Add a small button in the top-right corner of the SVG container:
- Icon: ⛶ or a simple expand SVG icon (two diagonal arrows)
- Position: absolute, top 8px, right 8px, z-index above SVG
- Style: semi-transparent background (rgba(0,0,0,0.5)), white icon, 32x32px, rounded
- On click: call `requestFullscreen()` on the SVG container div, then attempt
  `screen.orientation.lock('landscape')` (wrap in try/catch — not all browsers support it)
- On fullscreen exit: unlock orientation if locked

```javascript
function goFullscreen(el) {
  var req = el.requestFullscreen || el.webkitRequestFullscreen || el.msRequestFullscreen;
  if (req) {
    req.call(el).then(function() {
      try { screen.orientation.lock('landscape'); } catch(e) {}
    }).catch(function() {});
  }
}
document.addEventListener('fullscreenchange', function() {
  if (!document.fullscreenElement) {
    try { screen.orientation.unlock(); } catch(e) {}
  }
});
```

### 2. Mobile Teaser (below 768px)

Add CSS + HTML so that below 768px width:

- The full SVG + controls are hidden (`display: none`)
- A teaser div is shown instead, containing:
  - A static inline SVG (same viewBox as main but scaled to fit container width)
    showing ONLY the Kuhn loop circle + 5 phase labels at full opacity. No animations,
    no JS. Just the clean diagram as a preview of what the animation covers.
  - Below the static SVG: a button "▶ Play Fullscreen" (large tap target, min 48px
    height, full container width, styled green #4caf50, white text, rounded corners)
  - Small caption below button: "Best experienced in landscape" (muted, 12px)
  - The button calls `goFullscreen()` on the FULL animation container

```css
.sr-teaser { display: none; }
@media (max-width: 767px) {
  .sr-full { display: none; }
  .sr-teaser { display: block; text-align: center; margin: 1em 0; }
}
```

When fullscreen is entered from teaser:
1. Un-hide `.sr-full` (so the real SVG renders in fullscreen)
2. Call `goFullscreen()` on `.sr-full`
3. On fullscreen exit: re-hide `.sr-full`, show teaser again

### 3. Fullscreen Styles

When in fullscreen, the SVG container should:
- Fill the screen (`width: 100vw; height: 100vh`)
- Black background
- SVG scales to fit (it already does via viewBox)
- The `display: none` from mobile media query must be overridden

```css
.sr-full:fullscreen, .sr-full:-webkit-full-screen {
  width: 100vw; height: 100vh;
  background: #000;
  display: block !important;
}
```

### 4. Inline Behavior on Desktop (≥768px)

On desktop/tablet the animation plays inline as it does now. The fullscreen button
is available but optional. The container should have `max-width: 100%` and
`aspect-ratio: 12/7` so it fits the book's text column without overflowing.

```css
.sr-full {
  position: relative;
  max-width: 100%;
  aspect-ratio: 12 / 7;
}
.sr-full svg { width: 100%; height: 100%; }
```

## Structure

Wrap the existing SVG + scrubber in a div with class `sr-full`. Add the teaser div
with class `sr-teaser` as a sibling AFTER it. Add the fullscreen button inside `sr-full`.

## Do NOT

- Change any animation logic or keyframes
- Modify the SVG viewBox or internal coordinates
- Break the existing scrubber or play/pause controls
- Add external dependencies or frameworks

## Report

State: file size, confirm fullscreen works, confirm teaser shows on narrow viewport,
confirm inline playback still works on wide viewport.
