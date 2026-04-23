# Plan 0173 — Hover Panel Dwell Fix (let the user actually read and copy)

**Type:** Small JS patch. One commit. No content changes, no YAML changes.

## Problem

Rich-panel hovertips (e.g., `wormholes`, `nonlocal`, `2DEG`) render SVG + paragraph content on hover. Bruce reports: *"I cant copy it, it runs away from my mouse click attempt."* Symptom: when the user moves the mouse off the triggering term toward the panel, the panel dismisses before the mouse reaches it — or dismisses during a click-and-drag text selection inside the panel.

## Root cause (pinpointed)

`build/reader.js` lines 1074–1086 (term `mouseleave` handler):

```js
term.addEventListener('mouseleave', function(e) {
  if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }
  setTimeout(function() {
    var panel = document.querySelector('.hover-panel');
    if (panel && !panel.matches(':hover')) {
      dismissPanel();
    }
  }, 100);
});
```

Three issues:
1. **No listeners on the panel itself.** Once `showPanel` runs (lines 929–1006), the panel is a static DOM node. Nothing cancels dismiss when mouse enters it; nothing re-schedules dismiss when mouse leaves it.
2. **One-shot `:hover` check.** 100ms grace, single evaluation. If the mouse is mid-traversal across the 6px gap (`positionPanel`, line 1014), the check fires while nothing is hovered → dismiss.
3. **Nested hover-terms inside rich panels** (e.g., a `<span class="hover-term">` inside the-flat-title's HTML) fire their own mouseleave events that race with the outer dismiss logic.

## Fix

Convert the term's one-shot 100ms check into a **shared dismiss timer** that both the term's mouseleave AND the panel's mouseleave feed, and that both the term's mouseenter AND the panel's mouseenter cancel.

### Patch (Phase 1)

**File:** `build/reader.js`

**Change 1 — add a shared dismiss timer module-level:**

Near line 907 (where `hoverTimer` and `panelIdCounter` are declared), add:

```js
var dismissTimer = null;
var dismissDelay = 300; // ms grace window to traverse term→panel gap
```

**Change 2 — inside `showPanel` (before `return panel;` near line 1005), add panel listeners:**

```js
// Keep panel alive while mouse is on it; schedule dismiss when mouse leaves.
panel.addEventListener('mouseenter', function() {
  if (dismissTimer) { clearTimeout(dismissTimer); dismissTimer = null; }
});
panel.addEventListener('mouseleave', function() {
  if (dismissTimer) clearTimeout(dismissTimer);
  dismissTimer = setTimeout(function() {
    dismissTimer = null;
    dismissPanel();
  }, dismissDelay);
});
```

**Change 3 — rewrite term mouseleave (lines 1074–1086) to use shared timer:**

```js
term.addEventListener('mouseleave', function(e) {
  if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }
  if (dismissTimer) clearTimeout(dismissTimer);
  dismissTimer = setTimeout(function() {
    dismissTimer = null;
    var panel = document.querySelector('.hover-panel');
    // Only dismiss if panel is not currently hovered (mouse reached it in time)
    if (panel && !panel.matches(':hover')) {
      dismissPanel();
    }
  }, dismissDelay);
});
```

**Change 4 — cancel dismissTimer on term mouseenter (lines 1062–1072):**

Add at top of the mouseenter callback, before the `Date.now() - lastTouchTime` check:

```js
if (dismissTimer) { clearTimeout(dismissTimer); dismissTimer = null; }
```

**Change 5 — cancel dismissTimer in `dismissPanel` itself (line 910):**

At the top of `dismissPanel()`:

```js
if (dismissTimer) { clearTimeout(dismissTimer); dismissTimer = null; }
```

### Why these changes together

- Mouse traversal term → gap → panel: term mouseleave schedules dismiss in 300ms; panel mouseenter cancels it. User reaches panel → panel keeps itself alive via its own mouseenter/mouseleave loop.
- Mouse leaves panel: panel mouseleave schedules dismiss; user returns → cancelled; user genuinely moves away → dismissed after 300ms.
- Click-and-drag inside panel to select text: no term mouseleave fires (still inside panel), no dismiss. Selection works.
- Existing touch/click paths unchanged — touch events don't write to dismissTimer, so mobile behavior preserved.
- Nav tooltips that use `pointer-events: none` (lines 994–997 in showPanel) still work because mouseenter/mouseleave aren't delivered to them anyway.

## Acceptance

1. `make` / HTML build clean.
2. On the live website (desktop, Chrome + Safari + Firefox):
   - Hover *Wormholes* on cover → SVG panel appears after 250ms.
   - Move mouse from trigger to panel across the 6px gap → panel stays.
   - Click+drag to select text inside panel → selection works, panel does not dismiss.
   - Move mouse off panel entirely → panel dismisses after 300ms.
   - Hover a different term → old panel replaced by new (single-panel rule preserved).
3. On mobile (phone, touch):
   - Tap *Wormholes* → panel appears.
   - Tap elsewhere → panel dismisses.
   - No regression in touch toggle behavior.
4. Nav tooltips (menu items) still pass mouse through (pointer-events: none honored).

## Commit

One commit: `Plan 0173: hover panel dwell fix — shared dismiss timer, panel mouseenter/mouseleave`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit. No other files change. Zero risk to content.

## Out of scope

- CSS changes (gap geometry, panel styling).
- SVG changes.
- Rich-panel content changes.
- Any YAML changes.
- Touch UX changes beyond verifying no regression.

## Handoff report (Generator, 4 lines)

1. Commit SHA + summary of changes.
2. Build + push result.
3. Browser test matrix: desktop + mobile, pass/fail per acceptance criteria 2.x and 3.x.
4. Any regressions observed (especially nav tooltips, touch toggle, keyboard Enter/Escape).
