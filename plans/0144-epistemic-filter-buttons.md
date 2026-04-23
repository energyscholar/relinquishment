# Plan 0144: Epistemic Filter Buttons

**Status:** DONE (implemented prior to 2026-04-10; confirmed by Generator D)

## Context

The book has chapters tagged with filter-groups (A=science, B=bridge, C=testimony, G=Guardian, M=meta). Skeptical readers dismiss the book because B/C/G material ("crank territory") overshadows the published physics. The filter lets them read just the science (A) or just the story (B/C/G). Guardian is visible in ALL modes — she narrates both tracks. Data structure already exists in `menu-tooltips.yaml`; this plan propagates it to HTML and adds toggle buttons.

## Files to modify

- `build/preprocess.py` (~line 1215) — propagate `data-filter-group` attributes
- `build/reader.js` (lines 74-262) — filter buttons + toggle logic
- `build/menu-tooltips.yaml` — fix G comment (G visible in ALL modes, not just story)

## Phase 1: Data propagation (preprocess.py)

After the existing epistemic-class loop (~line 1215), add a second loop:
- Read `filter-group` from `menu-tooltips.yaml` chapter entries
- Apply `data-filter-group="A"` (or B/C/G/M) to each `<details class="chapter-section">`
- Same rfind approach as epistemic loop: find `id="anchor_id"`, walk back to nearest `<details class="chapter-section"`, inject attribute
- Chapters with no `data-filter-group` are treated as M (always visible) by JS

Expected output:
```html
<details class="chapter-section epistemic-a" data-filter-group="A">
<details class="chapter-section epistemic-c" data-filter-group="C">
<details class="chapter-section" data-filter-group="M">
```

## Phase 2: Filter buttons (reader.js)

Two toggle buttons between Expand All and AI Eval:

- **"Science"** (`id="filter-science"`) — shows A + M + G + untagged, hides B + C
- **"Story"** (`id="filter-story"`) — shows B + C + G + M + untagged, hides A

Button behavior:
- Outline style when inactive (transparent bg, `#1a5276` border)
- Filled style when active (`#1a5276` bg, white text)
- Click active button again → deactivate (show all)
- Hidden chapters get `display:none` and `open=false`

Filter logic:
```javascript
function applyFilter(mode) {
  // mode: null | 'science' | 'story'
  document.querySelectorAll('details.chapter-section').forEach(function(ch) {
    var fg = ch.getAttribute('data-filter-group') || 'M';
    var hide = false;
    if (mode === 'science') hide = (fg === 'B' || fg === 'C');
    else if (mode === 'story') hide = (fg === 'A');
    ch.style.display = hide ? 'none' : '';
    if (hide) ch.open = false;
  });
  // Auto-hide empty part-sections
  document.querySelectorAll('details.part-section').forEach(function(part) {
    var chs = part.querySelectorAll(':scope > details.chapter-section');
    if (!chs.length) return;
    var allHidden = Array.from(chs).every(function(c) { return c.style.display === 'none'; });
    part.style.display = allHidden ? 'none' : '';
  });
  updateFilterButtons();
  // localStorage persistence
  try { if (mode) localStorage.setItem('relinquishment-filter', mode);
        else localStorage.removeItem('relinquishment-filter'); } catch(e) {}
}
```

## Phase 3: Integration fixes

1. **Expand All** (reader.js ~line 209): skip hidden chapters
   ```javascript
   if (d.style.display === 'none') return;
   ```

2. **Deep links**: If hash target is inside a hidden chapter, clear filter first
   ```javascript
   var parentCh = target.closest('details.chapter-section');
   if (parentCh && parentCh.style.display === 'none') { activeFilter = null; applyFilter(null); }
   ```

3. **State restore on load**: After DOM construction, check localStorage and apply saved filter

4. **Dark mode**: Add button color overrides in dark mode section (~line 670)

## Phase 4: YAML comment fix

In `menu-tooltips.yaml` line 10, change:
```
G = Guardian interlude (visible in "just the story" mode)
```
to:
```
G = Guardian interlude (visible in ALL modes)
```

## NOT in this plan (deferred)

- T1-T5 tooltip variants per mode
- AI Eval button conditional visibility per mode
- DN 11-domain → 5-cluster mapping in book

## Verification

1. `make html` builds without errors
2. Open in browser — bottom bar shows Science and Story buttons
3. Click "Science": The Record part disappears, The Flat stays, Guardian interludes stay
4. Click "Story": The Flat disappears, The Record stays, Guardian interludes stay
5. Click active button: everything returns
6. Reload page: filter state persists
7. Navigate to `#record:alpha-farm` while in Science mode: filter clears, chapter opens
8. Expand All in filtered mode: only visible chapters expand
9. Hover tooltips still work on all visible elements
