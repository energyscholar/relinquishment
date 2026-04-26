# Plan 0263 — Cover Magnetosphere SVG Injection

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Bruce's cover image request (S63)
**Annealing:** MED MED LOW (3 passes)
**Independent:** No dependency on GP plans.

---

## Problem

Bruce created SVG-034 (dark-mode magnetosphere) and SVG-035 (light-mode
twin) in the gallery. These need to be injected into the book page
(Relinquishment.html) via `build/reader.js`, positioned right-aligned
above the sticky nav bar, with automatic light/dark mode switching via
`prefers-color-scheme`. The 12-hour flip: nightside in dark mode,
dayside in light mode.

A toggle button in the nav bar lets the reader show/hide the image.
Default: ON. State persisted in localStorage.

---

## Architecture

### Injection point: `build/reader.js`

reader.js is included via `--include-after-body` in the Pandoc build
(Makefile line 73). It already:
- Detects dark mode at line 17: `var isDark = window.matchMedia(...)`
- Creates and appends the sticky nav bar at lines 83-431
- Sets body padding at line 434
- Uses innerHTML at lines 484, 979 (precedent for the SVG approach)

The magnetosphere SVG should be injected AFTER the nav bar creation
(after line 434), using the same DOM-creation pattern.

### Positioning

- `position: fixed` (stays in place while reader scrolls)
- `bottom:` dynamically set to `nav.offsetHeight + 'px'` (not hardcoded
  — nav bar height varies slightly with content/font)
- `right: 0`
- `max-width: calc((100vw - 50em) / 2 - 1em)` (fits in the right
  margin between the 50em body and the viewport edge)
- `pointer-events: none` — decorative, should not intercept clicks
- `z-index: 1` — below nav (z-index 100), below hover panels
- `opacity: 0.85` — slightly transparent to feel like ambient decoration
- `aria-hidden: "true"` — purely decorative, screen readers skip it

### Responsive behavior

Use CSS (not JS resize listener) for the viewport threshold:

```css
@media (max-width: 900px) {
  #cover-magnetosphere { display: none !important; }
}
```

This is cleaner than a JS resize handler and reacts instantly.

### Light/dark switching

Use CSS `prefers-color-scheme` media queries (Approach A). This reacts
to runtime OS changes — no JS listener needed. The existing reader.js
`isDark` variable is set once at load time and does NOT update when the
OS switches. The CSS approach is superior for the 12-hour flip.

```css
@media (prefers-color-scheme: dark) {
  #cover-ms-light { display: none !important; }
  #cover-ms-dark { display: block; }
}
@media (prefers-color-scheme: light), (prefers-color-scheme: no-preference) {
  #cover-ms-dark { display: none !important; }
  #cover-ms-light { display: block; }
}
@media print {
  #cover-magnetosphere { display: none !important; }
}
```

### Toggle button

A small button in the nav bar (alongside existing Expand, Evaluate,
Top, etc.) that toggles the cover image on/off.

- **Label:** A small icon or symbol. Suggestion: `◐` (half-moon,
  echoes the day/night flip) or `🌍` or just `⬡` (hexagonal, abstract).
  Use a character that renders across platforms.
- **Tooltip (data-hover):** "Toggle cover illustration"
- **Default state:** ON (image visible)
- **Persistence:** `localStorage.setItem('cover-ms-hidden', 'true')`
  on hide; remove the key on show. Check at load time.
- **Behavior:** Toggles `wrapper.style.display` between `''` and `'none'`
- **`pointer-events`:** The toggle button itself needs `pointer-events:
  auto` (it's outside the wrapper, in the nav, so this is natural).

---

## SVG Content

The Generator should extract the SVG markup from `docs/gallery.html`:

**Dark mode SVG:** Section `#SVG-034-cover-magnetosphere`
(viewBox `0 0 720 320`). All gradient/filter IDs prefixed `cv-`.

**Light mode SVG:** Section `#SVG-035-ms-light-mode`
(viewBox `0 0 720 320`). All gradient/filter IDs prefixed `lm-`.

ID prefixes are already distinct — no collisions with each other or
with existing SVGs in the book (which use `ms-`, `flat-`, `deg-`,
`tq-`, `kbtn-`, `dbtn-`).

### Preparing the SVGs:

1. Remove the background `<rect>` element from both (page background
   provides the correct color per mode)
2. Add `id="cover-ms-dark"` or `id="cover-ms-light"` to each `<svg>`
3. Set `width="100%"` and remove any fixed width (keep viewBox)
4. Build as JS string concatenation (ES5 — reader.js uses `var`
   throughout, no template literals, no const/let, no arrow functions)

---

## Implementation Steps

### Step 1: Add CSS style block

At the top of the magnetosphere section (after line 434), inject a
`<style>` element containing the media queries for light/dark swap,
responsive hiding, and print suppression.

### Step 2: Create wrapper and SVGs

Create a wrapper `<div id="cover-magnetosphere">` with fixed positioning.
Set `bottom` to `nav.offsetHeight + 'px'` (the `nav` variable is in
scope — it was created at line 83).

Inject both SVGs via `wrapper.innerHTML`. Use string concatenation.
The SVGs are ~4KB each; total ~8KB added to the ~975KB page (0.8%).

### Step 3: Add toggle button to nav bar

Create a button element:
```javascript
var msToggle = document.createElement('a');
msToggle.href = '#';
msToggle.id = 'nav-ms-toggle';
msToggle.textContent = '◐'; // ◐ half-circle
msToggle.setAttribute('data-hover', 'Toggle cover illustration');
msToggle.classList.add('hover-nav');
msToggle.style.cssText = 'text-decoration:none;color:' +
  (isDark ? '#aaa' : '#888') + ';font-size:1.1em;cursor:pointer;' +
  'margin-left:0.5em;';
```

Append to nav bar (before `topBtn`).

Wire click handler:
```javascript
msToggle.addEventListener('click', function(e) {
  e.preventDefault();
  var hidden = wrapper.style.display === 'none';
  wrapper.style.display = hidden ? '' : 'none';
  msToggle.style.opacity = hidden ? '1' : '0.4';
  try {
    if (hidden) localStorage.removeItem('cover-ms-hidden');
    else localStorage.setItem('cover-ms-hidden', 'true');
  } catch(e) {}
});
```

Check localStorage at load time:
```javascript
try {
  if (localStorage.getItem('cover-ms-hidden') === 'true') {
    wrapper.style.display = 'none';
    msToggle.style.opacity = '0.4';
  }
} catch(e) {}
```

### Step 4: Build and verify

- `make dev`
- Open `docs/downloads/Relinquishment.html` in browser (wide viewport)
- Verify: SVG appears in right margin, right-aligned, above nav bar
- Verify: SVG hidden on narrow viewport (<900px)
- Verify: dark/light mode swap (DevTools → Rendering → Emulate
  `prefers-color-scheme`)
- Verify: toggle button works (click hides/shows, opacity dims when off)
- Verify: toggle state persists across page reload
- Verify: SVG does not intercept mouse clicks
- Verify: print preview does not show the SVG
- Verify: no ID collisions with existing SVGs in the book
- Verify: existing functionality unaffected (hover panels, nav,
  copy buttons, expand/collapse, breadcrumb)

---

## What NOT to Change

- Do not modify gallery.html (the SVGs stay in the gallery too)
- Do not modify the Makefile or Pandoc template
- Do not add new files — all changes go in `build/reader.js`
- Do not change existing reader.js functionality
- Do not add the SVG to index.html (landing page stays as-is)
- Do not use ES6 features (const, let, arrow functions, template
  literals) — reader.js is ES5 throughout

---

## Annealing Log (MED MED LOW — 3 passes)

### Pass 1 (MED) — Structural review

**SVG string embedding in ES5:** Two SVGs at ~200 lines / ~4KB each
need to become JS string concatenation. This is verbose but matches
existing reader.js patterns (innerHTML used at lines 484, 979).
Alternative (DOM API element creation) would be far worse for this many
elements. String concat is the right approach.

**Nav bar bottom offset:** Original plan hardcoded `bottom: 2.8em`.
Problem: nav bar height varies with font size and content. Fix: use
`nav.offsetHeight + 'px'` — the `nav` variable is in scope at the
injection point. The Generator has access to it.

**Toggle button:** Bruce's suggestion. Eliminates the fixed-vs-scroll
debate. Default ON, localStorage persistence, dimmed icon when off.
Placed in nav bar using the same pattern as the existing share (§),
Expand, Evaluate, and Top buttons.

**Responsive via CSS not JS:** Original plan used a JS resize listener.
Better: a CSS `@media (max-width: 900px)` rule in the injected style
block. Cleaner, no event listener overhead, instant response. The
JS-only `window.innerWidth < 900` early-return is still useful for
skipping DOM creation on initial load of narrow viewports.

### Pass 2 (MED) — Edge cases

**Print suppression:** `@media print { #cover-magnetosphere { display:
none !important; } }` — without this, the fixed-position SVG prints
on every page. Added to the CSS block.

**Accessibility:** The wrapper must have `aria-hidden="true"`. It's
purely decorative. Screen readers should skip it entirely.

**localStorage try/catch:** reader.js already wraps localStorage in
try/catch at line 836. The Generator must follow this pattern — Safari
private browsing and some corporate environments throw on localStorage
access.

**ID collision deeper check:** `cv-` and `lm-` prefixes are unique to
these SVGs. Verified: existing book inline SVGs use `ms-`, `flat-`,
`deg-`, `tq-`, `kbtn-`, `dbtn-`, `filter-sh` prefixes. No collision.

**Body max-width edge case:** Body is `max-width: 50em` ≈ 800px. The
CSS calc formula `(100vw - 50em) / 2 - 1em` yields negative on screens
≤ 52em wide. Combined with `@media (max-width: 900px)` hiding, the
SVG never appears on screens where it would have negative width. Safe.

**Dark-mode `<rect>` removal:** Both SVGs have a `<rect width="720"
height="320" fill="url(#cv-bg)">` (dark) and `<rect ... fill=
"url(#lm-bg)">` (light) as their first visible element. The Generator
MUST remove these AND can also remove the `cv-bg`/`lm-bg` gradient
definitions to save bytes.

### Pass 3 (LOW) — Final check

**Performance:** 8KB of SVG strings added to a 975KB page (0.8%).
SVG filters (4x feGaussianBlur at stdDeviation 1.2–8) run on the GPU
but only on screens >900px where GPU capability is assumed. The fixed
positioning means no repaints during scroll.

**Interaction with hover panels:** Hover panels have z-index above 1.
The SVG at z-index 1 will be behind all hover panels. With
`pointer-events: none`, it can't interfere with panel triggers.
The toggle button in the nav bar has `pointer-events: auto` naturally
(it's a nav child, not inside the wrapper).

**`no-preference` fallback:** The `prefers-color-scheme: no-preference`
media query catches browsers/OSes that don't report a preference.
Default: show light mode (matches the book's default light styling).

**Tested against desired effect:** Reader opens book on wide screen →
sees magnetosphere in right margin (ambient, not distracting). Reader
scrolls → image stays fixed (decorative landmark). Reader switches to
dark mode → image flips to nightside. Reader finds it distracting →
clicks ◐ toggle → image hides, preference saved. Next visit → still
hidden. Reader clicks ◐ again → image returns.

**Rating: 8/10.** The 2-point gap: (1) the SVG string concatenation is
the main execution complexity — ~200 lines of carefully escaped JS
strings, easy to get a quote or angle bracket wrong; (2) the exact
`bottom` offset may need tuning once Bruce sees it in the actual book.
Both are solvable in one Generator pass.

---

## Acceptance Criteria

- [ ] Both SVGs injected via reader.js (no manual HTML edits)
- [ ] Background `<rect>` elements removed from both SVGs
- [ ] `prefers-color-scheme` swaps dark/light automatically at runtime
- [ ] SVG positioned in right margin, above nav bar (dynamic offset)
- [ ] Hidden on viewports <900px (CSS media query)
- [ ] Hidden in print (`@media print`)
- [ ] Toggle button in nav bar (◐ or similar)
- [ ] Toggle state persisted in localStorage
- [ ] `aria-hidden="true"` on wrapper
- [ ] No click interception (pointer-events: none on wrapper)
- [ ] No ID collisions (cv- and lm- prefixes verified)
- [ ] `make dev` clean build
- [ ] Existing reader.js functionality unaffected
- [ ] ES5 style throughout (var, string concat, no arrow functions)

---

## Generator Handoff

```
You are the Generator.

Read Plan 0263 at ~/software/relinquishment/plans/0263-cover-magnetosphere-injection.md

Execute: Add magnetosphere SVG injection to build/reader.js, after
the nav bar body-padding line (line 434). Extract SVG-034 (dark,
cv- prefix) and SVG-035 (light, lm- prefix) from docs/gallery.html.
Remove background <rect> elements and unused background gradients.
Inject both into a fixed-position wrapper with CSS media queries for
light/dark swap, responsive hiding (<900px), and print suppression.
Add a toggle button (◐) to the nav bar with localStorage persistence.
Set bottom offset from nav.offsetHeight. Add aria-hidden="true" to
wrapper. Use ES5 style (var, string concat, try/catch on localStorage).
Run `make dev`. Open the book HTML on a wide viewport and verify:
image appears in right margin, toggle works, dark/light swap works
(use DevTools emulation). Report completion.
```

---

*Plan 0263 written by Argus (Auditor), S63. Annealed 3 passes (MED MED LOW).*
