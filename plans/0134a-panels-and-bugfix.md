# Plan 0134a: Hover Panels + Bug Fix (Phase A)

**Parent plan:** 0134 (onHover System Upgrade + Deep Link Navigation)
**Depends on:** None
**Followed by:** 0134b (Navigation + Responsive)
**Session:** S52

## Purpose

Replace browser-native `title` tooltips with custom hover panels on all 16
existing hover terms. Fix a critical deep-link crash. This is the foundation —
all subsequent phases build on working panels.

## Generator Context (REQUIRED)

Before executing this plan, the Generator MUST read:
1. This plan (0134a)
2. `build/reader.js` — the entire file (524 lines). Understand the IIFE structure,
   the existing utilities (copyToClipboard, autoExpand, isDark), and the bottom
   nav bar creation. Your code goes INSIDE this IIFE, after the existing code.
3. `build/preprocess.py` — search for "hover" and read the two hover systems:
   - `hover_replace()` (~line 851) — the `.hover-term` system. YOU CHANGE THIS.
   - `collapse_chapters()` (~line 242) — the `<summary title="...">` system.
     YOU DO NOT TOUCH THIS. These are chapter-hover-descriptions, a SEPARATE
     system that must remain as browser-native tooltips.
4. `build/hover-definitions.yaml` — 16 terms, plain text strings
5. `build/test-hover-panel.html` — the test suite. Run it after building.
   Focus on Groups 1-6, 9-11, 13-15 for this phase.

Do NOT read or modify any .tex files. This is infrastructure only.

## Critical Bug Fix (DO FIRST)

`autoExpand()` calls `document.querySelector(hash)` without try/catch. When
hash contains a colon (e.g., `#ch:firmware-update`), querySelector throws
`SyntaxError` (colon parsed as CSS pseudo-class). This crashes the ENTIRE
reader.js IIFE — killing all features (copy buttons, nav bar, heading links,
expand/collapse, everything).

Most chapter IDs contain colons. Any deep link to these chapters currently
destroys the page.

**Fix:** Wrap the querySelector call in try/catch:
```javascript
function autoExpand(hash) {
  if (!hash) return;
  var target;
  try { target = document.querySelector(hash); } catch(e) { /* colon-IDs */ }
  if (!target) {
    try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch(e) {}
  }
  if (!target) return;
  // ... rest unchanged
}
```

**Verification:** Run `node build/test-e2e-devices.js` — the 6 deep-link
failures should become passes.

## Attribute Change (preprocess.py)

In `hover_replace()` (~line 861), change:
```python
f'<span class="hover-term" title="{escaped_def}">{term}</span>'
```
to:
```python
f'<span class="hover-term" data-hover="{escaped_def}">{term}</span>'
```

**CRITICAL: Change ONLY this one line.** Do NOT modify `collapse_chapters()`.
The `title=` attributes on `<summary>` elements are a SEPARATE system —
chapter hover descriptions — and MUST remain as browser-native tooltips.

If you grep for `title=` in preprocess.py, you will find ~20 occurrences.
Change only the one inside `hover_replace()`.

## Panel Renderer (reader.js)

Add ~250-350 lines inside the existing IIFE in reader.js. After the existing
code (after the heading-link section, before the closing `})();`).

### Architecture Constraints

**Panels MUST be appended to `document.body`.**
NOT as children or siblings of the hover term. Hover terms live inside
`<details>` elements at up to 4 levels of nesting. `<details>` when closed
has `display: none` on content — any panel inserted as a child is invisible.
Even when open, ancestor elements may clip positioned children.

Panels are `position: fixed` or `position: absolute` relative to viewport.
Use `getBoundingClientRect()` on the trigger term to calculate position.
Append panel to `document.body`. This is the standard tooltip/popover pattern.

**Event handlers MUST call `stopPropagation()`.**
Hover terms can live inside `<summary>` elements (the title-line terms do).
Without stopPropagation, tapping "Wormholes" on phone opens a panel AND
collapses the entire book. The existing heading-link code at ~line 352 shows
the exact pattern:
```javascript
a.addEventListener('click', function(e) {
  e.preventDefault();
  e.stopPropagation();
  // ...
});
```
Apply the same pattern to ALL hover term event handlers (tap, click, Enter).

**Touch and mouse require SEPARATE handlers.**
- Desktop: `mouseenter` with 250ms delay → show panel. `mouseleave` → hide.
  The delay prevents flicker when the mouse crosses a term without stopping.
- Phone: `touchstart`/`touchend` → toggle panel immediately. No delay.
  Detect touch capability: `var hasTouch = 'ontouchstart' in window;`
  If hasTouch, bind touch handlers. If not, bind mouse handlers.
  Do NOT unify into one handler — the interaction models are fundamentally
  different (hover-to-preview vs tap-to-toggle).

**Use `textContent`, not `innerHTML`, for panel content.**
Phase A definitions are plain text, HTML-escaped by `html.escape()` in
preprocess.py. Using `innerHTML` would double-escape `&amp;` etc. Phase D
will add formatted content — `innerHTML` support comes then. For now,
`textContent` is correct and safe.

### Panel Features

- **Content:** Read from `data-hover` attribute via `getAttribute('data-hover')`
- **Size:** `max-width: 400px; max-height: 300px; overflow-y: auto;`
- **Style:** Background, border, subtle box-shadow, padding. Inherit font.
- **Dark mode:** Check `isDark` (already exists in reader.js scope) and apply
  appropriate colors. Also add `@media (prefers-color-scheme: dark)` CSS rule
  for `.hover-panel`.
- **Positioning:** Smart — check viewport bounds. If panel would overflow
  right edge, shift left. If it would overflow bottom, show above the term
  instead of below. Use `getBoundingClientRect()` on the term.
- **Dismiss:** mouseleave (desktop), tap outside (phone), click outside,
  Escape key. Remove panel from DOM on dismiss (don't just hide).
- **Single panel:** Only one panel visible at a time. Before showing a new
  panel, remove any existing `.hover-panel` from the DOM.
- **Anti-flicker (desktop only):** The 250ms mouseenter delay. If mouseleave
  fires before the delay completes, cancel the pending panel. Use
  `setTimeout`/`clearTimeout`.
- **Keyboard:** Add `tabindex="0"` to all `.hover-term` elements. On focus +
  Enter → show panel. On Escape → dismiss. Add `aria-describedby` linking
  term to panel (generate unique IDs).
- **No dependency on external libraries.** Vanilla JS only. No Tippy, no
  Popper, no framework.

### CSS

Add to `build/html.css` (preferred) or inject via preprocess.py:

```css
.hover-panel {
  position: fixed;
  z-index: 200;
  max-width: 400px;
  max-height: 300px;
  overflow-y: auto;
  padding: 0.8em 1em;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  font-size: 0.9em;
  line-height: 1.5;
  animation: panel-fade-in 0.15s ease-out;
}

@keyframes panel-fade-in {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.hover-term {
  font-style: italic;
  border-bottom: 1px dotted #888;
  cursor: pointer;  /* was cursor: help — panels are interactive now */
}
.hover-term:hover { border-bottom-color: #2471a3; }

@media (prefers-color-scheme: dark) {
  .hover-panel {
    background: #2a2a2a;
    border-color: #555;
    color: #e0e0e0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
  }
  .hover-term { border-bottom-color: #666; }
  .hover-term:hover { border-bottom-color: #5dade2; }
}
```

Update the existing `.hover-term` CSS in preprocess.py's injected styles:
change `cursor: help` to `cursor: pointer`.

## Test Verification

After building, run:

1. `make html` — must build without errors
2. Open `build/test-hover-panel.html` in browser — focus on:
   - Groups 1-5: panel rendering, dismissal, touch, keyboard, dark mode
   - Group 6: smart positioning
   - Group 9: title line three doors (and verify details state preserved)
   - Groups 10-11: no regressions, anti-flicker
   - Groups 13-15: graceful degradation, expand/collapse interaction, performance
3. `node build/test-e2e-devices.js` — the 6 deep-link failures should pass.
   Phone panel tests (Group 3) should activate and pass.

Groups 7-8, 16-22 test features built in later phases — they will skip.

## Acceptance Criteria (Phase A only)

1. autoExpand colon-ID crash fixed — deep links with colons work
2. All 16 hover terms use `data-hover`, not `title` attribute
3. Hover on term creates `.hover-panel` element on `document.body`
4. Panel content matches `data-hover` text (via `textContent`)
5. Panel max-width ≤ 400px, max-height ≤ 300px, scrollable overflow
6. Panel dismissed on: mouseleave, click-outside, Escape, tap-outside
7. Only one panel visible at a time
8. Touch: tap opens panel immediately (no delay)
9. Mouse: hover with 250ms delay opens panel (anti-flicker)
10. Keyboard: tabindex on terms, Enter opens, Escape closes
11. `aria-describedby` links term to panel
12. Dark mode: panel colors adapt to prefers-color-scheme
13. Smart positioning: panel stays within viewport bounds
14. Tapping title-line terms does NOT toggle book `<details>` (stopPropagation)
15. Chapter `<summary>` elements still have `title` attributes (no regression)
16. Copy Science Reference button still works
17. Expand All / Collapse All toggle still works
18. autoExpand still works for standard deep links
19. `make html` builds without errors
20. Build time increase < 5 seconds

## Files Modified

| File | Change |
|---|---|
| build/reader.js | autoExpand fix + panel renderer (~300 lines) |
| build/preprocess.py | `title=` → `data-hover=` (one line in hover_replace only) |
| build/html.css | .hover-panel styles + dark mode + cursor change |

## Files NOT Modified

| File | Why |
|---|---|
| build/generate-hover.py | PDF side unchanged |
| build/hover-definitions.yaml | Content unchanged in Phase A |
| build/chapter-hover-descriptions.yaml | Separate system |
| build/test-hover-panel.html | Auditor's test suite — do not modify |
| build/test-e2e-devices.js | Auditor's test suite — do not modify |
| Any .tex file | No content changes |
