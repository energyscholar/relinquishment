# Plan 0264 — Cover Magnetosphere: Mobile Scroll Behavior

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Bruce's phone test of Plan 0263
**Annealing:** LOW (1 pass)
**Depends on:** Plan 0263 (already executed and committed)

---

## Problem

Plan 0263 hides the magnetosphere on viewports < 900px. But Bruce's
Android phone shows a usable right margin at the title screen (about
100-120px). The image should appear on mobile as a welcome element,
then hide when the reader scrolls into full-width content.

---

## Current Code (build/reader.js, lines 450-729)

The magnetosphere injection block has two barriers to mobile display:

1. **Line 452:** `if (window.innerWidth < 900) return;` — skips all
   injection on narrow viewports. Nothing is created.

2. **Line 456:** `@media (max-width: 900px) { #cover-magnetosphere
   { display: none !important; } }` — CSS backup hide.

Both must be removed. The scroll behavior replaces them.

---

## Changes

### Step 1: Remove the 900px barriers

1. **Delete line 452:** `if (window.innerWidth < 900) return;`

2. **Delete the max-width media query** from the style block (line 456).
   Keep the `prefers-color-scheme` and `@media print` rules.

### Step 2: Make width responsive

Replace the fixed `width:350px` (line 465-466) with responsive sizing:

```javascript
var isNarrow = window.innerWidth < 900;
wrapper.style.cssText = 'position:absolute;bottom:100%;right:0;' +
  'width:' + (isNarrow ? '100px' : '350px') + ';' +
  'max-width:50%;pointer-events:none;z-index:1;' +
  'opacity:0.85;transition:opacity 0.3s;';
```

Key: `transition:opacity 0.3s` — the scroll hide/show will fade
smoothly, not snap.

### Step 3: Add scroll-aware hide/show (all viewports)

After the localStorage check (line 723-728), before the closing
`})();`, add:

```javascript
var scrollHidden = false;
window.addEventListener('scroll', function() {
  var manuallyHidden = false;
  try { manuallyHidden = localStorage.getItem('cover-ms-hidden') === 'true'; } catch(e) {}
  if (manuallyHidden) return;

  if (window.scrollY > 20 && !scrollHidden) {
    wrapper.style.opacity = '0';
    scrollHidden = true;
  } else if (window.scrollY <= 20 && scrollHidden) {
    wrapper.style.opacity = '0.85';
    scrollHidden = false;
  }
});
```

**Design decisions:**
- `scrollY > 20` — catches the first scroll gesture without being
  hair-trigger
- Uses `opacity` not `display:none` — the CSS transition makes it
  fade rather than snap
- Applies to ALL viewports — the image is a welcome element on load,
  fades out once the reader starts reading, returns on scroll to top
- Respects the manual toggle — if user clicked ◐ to hide, scroll
  listener doesn't override
- Scroll back to top (`scrollY <= 20`) restores the image

### Step 4: Build and verify

- `make dev`
- Desktop (>900px):
  - On load: magnetosphere visible in right margin (350px)
  - Scroll down: image fades out over 0.3s
  - Scroll back to top: image fades back in
  - Toggle ◐: hides image, scroll doesn't bring it back
- Mobile emulation (DevTools → Toggle Device Toolbar → e.g. Pixel 7):
  - On load: small magnetosphere visible in right margin (100px)
  - Scroll down: image fades out over 0.3s
  - Scroll back to top: image fades back in
  - Toggle ◐: hides image, scroll doesn't bring it back
- Both: dark/light swap works

---

## What NOT to Change

- SVG content (no changes to the dark/light SVGs)
- Toggle button behavior on desktop
- Dark/light mode switching
- Print suppression
- Any other reader.js functionality

---

## Annealing Log (LOW — 1 pass)

**Scroll listener performance:** `scroll` events fire rapidly. The
handler is lightweight (one scrollY comparison, one opacity assignment).
No forced reflow, no DOM queries. The `scrollHidden` flag prevents
redundant style assignments on every scroll tick. Acceptable on all
viewports.

**`opacity:0` vs `display:none`:** Using opacity keeps the element in
the DOM (no layout shift) and enables the CSS transition. An invisible
element with `pointer-events:none` has zero interaction cost.

**Resize edge case:** If someone rotates a phone from portrait to
landscape (crossing the 900px threshold), `isNarrow` is set at load
time and won't update. This only affects the width (100px vs 350px),
not the scroll behavior. Page reload on rotation is common. Acceptable.

**Rating: 9/10.** Small, contained change. The 1-point gap: the 100px
mobile width is a guess from the screenshot — Bruce may want it
slightly larger or smaller once he sees it.

---

## Acceptance Criteria

- [ ] Magnetosphere visible on mobile at load (small, right margin)
- [ ] Fades out on scroll (threshold ~20px)
- [ ] Fades back in on scroll to top
- [ ] Toggle ◐ overrides scroll behavior
- [ ] Desktop: fades on scroll, returns on scroll-to-top (same as mobile)
- [ ] Dark/light swap works on mobile
- [ ] `make dev` clean build

---

## Generator Handoff

```
You are the Generator.

Read Plan 0264 at ~/software/relinquishment/plans/0264-cover-ms-mobile-scroll.md

Execute: Modify the cover magnetosphere section in build/reader.js
(lines 450-729). Remove the 900px early return (line 452) and the
@media max-width:900px CSS rule (line 456). Make wrapper width
responsive (100px on narrow, 350px on wide). Add opacity transition.
Add scroll listener for narrow viewports only: fade out on scrollY>20,
fade back in on scrollY<=20, respect manual toggle state. Do NOT
change SVG content or desktop behavior. Use ES5 style. Run `make dev`.
Test in browser with mobile emulation. Report completion.
```

---

*Plan 0264 written by Argus (Auditor), S63. Annealed 1 pass (LOW).*
