# Plan 0224 — Mobile Touch Fix (Custodian interludes + buttons)

**Status:** COMPLETE (verified S63 audit)
**Priority:** High — interludes and key buttons completely broken on phone
**Scope:** `build/reader.js` only, touchend handler

## Bug

The `touchend` handler (line 1140) intercepts taps on ANY element with `data-hover` or `data-hover-id`. It calls `e.preventDefault()`, killing the synthetic `click` event. Three things break:

1. **Custodian menu items** — have `data-hover-id` + `data-hover-disabled="true"`. Line 1166 `preventDefault()` fires, `showPanel()` bails (disabled). Click handler at line 1280 never fires. Purple interlude links are visible but dead.

2. **Expand/Collapse All** — has `data-hover` + `hover-nav`. No `h2/h3` inside, so `shouldShow=true` (line 1151). Line 1154 `preventDefault()` shows tooltip instead of expanding. Click handler (line 214) never fires.

3. **"C" (Custodian-only) button** — same as Expand All. Tooltip shown, mode never activates.

## Root cause

Two paths in the touchend handler are too greedy:

**Path A (hover-nav, line 1148-1163):** `shouldShow` is true for ANY `hover-nav` element without an `h2/h3` — buttons, links, etc. This was designed for part-level `<summary>` elements (which have no heading). But it catches all `hover-nav` buttons too.

**Path B (non-hover-nav, line 1166):** Unconditional `preventDefault()` on everything with `data-hover-id`, including `.custodian-menu-item` elements that have `data-hover-disabled="true"`.

## Fix

### Change 1: Guard for `data-hover-disabled` (line 1142)

After line 1142 (`if (!term) return;`), add:

```js
if (term.hasAttribute('data-hover-disabled')) return;
```

Elements with `data-hover-disabled` don't show tooltips — they exist only for the click handler. Let the touch fall through to synthetic click.

### Change 2: Fix `hover-nav` button detection (line 1148-1163)

The `shouldShow` logic needs to distinguish between:
- **`<summary>` elements** (part labels) — SHOULD show tooltip on tap (correct behavior)
- **`<button>` elements** (Expand All, C, etc.) — should NOT show tooltip, should let click fire

Replace line 1151:
```js
var shouldShow = !headingInTerm || (tappedHeading && term.contains(tappedHeading));
```

With:
```js
var isButton = term.tagName === 'BUTTON' || term.tagName === 'A';
var shouldShow = !isButton && (!headingInTerm || (tappedHeading && term.contains(tappedHeading)));
```

When `isButton` is true, `shouldShow` is false → falls through to line 1162 "native action happens" → returns without `preventDefault()` → synthetic click fires → button's click handler runs.

### What this preserves

- Chapter `<summary>` elements still show tooltips on heading-text tap (they have `h2/h3` inside, aren't buttons)
- Part `<summary>` elements still show tooltips (no heading, but aren't buttons)
- Triangle/marker area still does native toggle (falls through at line 1162)
- Regular `data-hover` elements (term definitions, domain buttons) still show tooltips on touch
- Desktop hover behavior unchanged (touchend doesn't fire on desktop)

## Acceptance Tests

1. **Phone: tap Custodian menu item** → chapter expands, scrolls to purple interlude
2. **Phone: tap Expand All** → all sections expand (no tooltip)
3. **Phone: tap "C" button** → Custodian-only mode activates
4. **Phone: tap chapter title text** → tooltip shows (NOT expand)
5. **Phone: tap chapter triangle/marker** → chapter expands (NOT tooltip)
6. **Phone: tap a domain button** → tooltip with domain description
7. **Phone: tap a hover term** → tooltip shows
8. **Desktop: hover Expand All** → tooltip shows on hover, click expands
9. **Desktop: all existing hover behavior unchanged**
10. **Build succeeds:** `make html` exits 0

## Handoff Prompt

```
You are the Generator for Plan 0224 (mobile touch fix).

Read: ~/software/relinquishment/plans/0224-mobile-touch-fix.md

Two changes to `build/reader.js`, both in the touchend handler
starting at line 1140:

1. After line 1142 (`if (!term) return;`), add:
   `if (term.hasAttribute('data-hover-disabled')) return;`

2. At line 1151, replace the `shouldShow` assignment with:
   `var isButton = term.tagName === 'BUTTON' || term.tagName === 'A';`
   `var shouldShow = !isButton && (!headingInTerm || (tappedHeading && term.contains(tappedHeading)));`

After: `make dev`, test on phone (interludes, Expand All, C button),
commit as "Plan 0224: fix mobile touch — interludes, expand, C button",
push. Report ≤5 lines with deviations.
```
