# Plan 0221 — Disable Guardian Interlude Tooltips

**Status:** DONE  
**Author:** Auditor  
**Priority:** Low  
**EV:** Stable — no T degrades, F-scifi/F-crank slightly improved via reduced TOC busyness  
**Scope:** `build/preprocess.py`, `build/reader.js`  
**Rationale:** The full-text Custodian tooltips on guardian interlude menu items make the TOC feel too busy. The content is valuable but optional — readers who miss it still get the interludes in-body. Disable, don't remove: the tooltip data stays in `menu-tooltips.yaml` and the hover dictionary so Bruce can re-enable later with a one-line change.

## Approach

Add a `data-hover-disabled` attribute to guardian interlude menu items. Respect it in `showPanel()` as an early-exit condition, same pattern as the existing `data-hover-always` attribute but inverted.

## Changes

### 1. `build/preprocess.py` — Mark guardian menu items as hover-disabled

In the guardian menu item injection block (~line 1844–1852), add `data-hover-disabled="true"` to the generated `<div>`:

```python
# Current (line 1844-1852):
menu_item = (
    f'\n<div class="custodian-menu-item" id="menu-{iid}" '
    f'data-target="{iid}" '
    f'role="link" tabindex="0" '
    f'aria-label="Custodian interlude: {html_mod.escape(title)}" '
    f'data-filter-group="G" '
    f'data-hover-id="{hover_id}">'
    ...

# Changed — add data-hover-disabled="true" after data-hover-id:
menu_item = (
    f'\n<div class="custodian-menu-item" id="menu-{iid}" '
    f'data-target="{iid}" '
    f'role="link" tabindex="0" '
    f'aria-label="Custodian interlude: {html_mod.escape(title)}" '
    f'data-filter-group="G" '
    f'data-hover-id="{hover_id}" '
    f'data-hover-disabled="true">'
    ...
```

**Note:** The `_register_hover()` call (lines 1839–1842) stays untouched — tooltip content remains in the JSON dictionary. Only the menu item element is marked as disabled.

### 2. `build/reader.js` — Respect `data-hover-disabled` in `showPanel()`

At line 948 in `showPanel()`, add a check for `data-hover-disabled` alongside the existing `data-hover-always` gate:

```javascript
// Current (line 948):
if (!tooltipsEnabled() && !term.hasAttribute('data-hover-always')) return;

// Changed — add line BEFORE the existing gate:
if (term.hasAttribute('data-hover-disabled')) return;
if (!tooltipsEnabled() && !term.hasAttribute('data-hover-always')) return;
```

The `data-hover-disabled` check comes first and is unconditional — it suppresses the tooltip regardless of the global toggle state. This means even with tips:on, guardian interludes won't show tooltips.

## What is NOT changed

- `menu-tooltips.yaml` — all 7 Custodian interlude texts preserved
- `hover-definitions.yaml` — untouched
- The `_register_hover()` calls — tooltip data still enters the JSON dictionary
- The `custodian-menu-item` click behavior (scrolls to interlude) — unaffected
- The C filter button — unaffected
- All other tooltips — unaffected

## Re-enabling

To restore guardian tooltips later: remove `data-hover-disabled="true"` from the menu_item f-string in `preprocess.py` (one line). The `reader.js` check becomes inert (no elements carry the attribute). Or remove the JS check too for cleanliness.

## Acceptance Tests

After `make html`:

1. **Guardian tooltips suppressed:** Hover over each of the 7 Custodian menu items (◇ markers in TOC). No tooltip panel should appear.
2. **Guardian click navigation works:** Click each Custodian menu item. It should still open the containing chapter and scroll to the interlude.
3. **Other tooltips unaffected:** Hover over any chapter menu item (non-Custodian). Tooltip should appear normally when tips:on.
4. **Global toggle still works:** Click tips:off/tips:on. Non-guardian tooltips should respond. Guardian tooltips should stay suppressed in both states.
5. **C filter still works:** Click the purple C button. Guardian-only view should activate/deactivate normally.
6. **Grep validation:** `grep -c 'data-hover-disabled' output.html` should return 7 (one per interlude menu item).
7. **Content preserved:** `grep -c 'interlude-custodian:' output.html` in the hover-data JSON block should still show 7 entries (tooltip data present, just not displayed).
