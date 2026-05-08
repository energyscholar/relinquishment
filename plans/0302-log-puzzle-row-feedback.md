# Plan 0302: LOG Puzzle Per-Row Green Feedback

**Status:** READY FOR GENERATOR
**Priority:** LOW — UX polish
**Source:** Bruce, S67 CW3

## Context

The LOG puzzle type (matrix grid — used by "UDHR Service Compatibility" and "Under Which Possibility?") currently only validates on "Check" button press, marking wrong cells red. There is no per-row feedback. Bruce wants: when a user correctly completes all cells in a row, that row's background turns green immediately — before pressing Check.

## Scope

**One file:** `build/build-puzzles.py`

**Two changes:**
1. CSS: add `.log-table tr.row-correct td` style (green background) + dark-mode variant
2. JS: in `initLOG`, after each cell toggle in `render()`, evaluate each row and apply/remove `row-correct` class

## Plan

### Phase 1: Add CSS

**Location:** After `.log-table td.wrong` (line 716), add:

```css
.log-table tr.row-correct td { background: #e8f5e9; }
.log-table tr.row-correct td:hover:not(:first-child) { background: #c8e6c9; }
```

**Dark-mode location:** After `.log-table td:hover:not(:first-child) { background: #1e3a50; }` (line 882), add:

```css
.log-table tr.row-correct td { background: #1a3a1a; }
.log-table tr.row-correct td:hover:not(:first-child) { background: #2a4a2a; }
```

**Idempotency:** If `row-correct` exists in build-puzzles.py — phase is applied.

### Phase 2: Add row validation to initLOG

**Location:** In the `render()` function inside `initLOG` (around line 1602), after the table HTML is built and cells have click handlers attached (after line 1630), add row-correctness evaluation:

```javascript
    // Per-row green feedback
    var trs = inter.querySelectorAll("tbody tr");
    for (var ri = 0; ri < d.rows.length; ri++) {
      var rowOk = true;
      for (var ci = 0; ci < d.columns.length; ci++) {
        if (grid[ri][ci] !== d.correct[ri][ci]) { rowOk = false; break; }
      }
      if (trs[ri]) { if (rowOk) trs[ri].classList.add("row-correct"); else trs[ri].classList.remove("row-correct"); }
    }
```

Insert this block after the cell click-handler loop (after line 1630, before the `.log-submit` handler at line 1632). This runs on every `render()` call — including initial render and after every cell toggle — so rows go green the moment the last cell in that row is toggled to the correct value.

**Idempotency:** If `row-correct` exists in the `initLOG` function — phase is applied.

### Phase 3: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

- [ ] Open UDHR Service Compatibility puzzle
- [ ] Toggle all cells in "Weather prediction" row to correct (✓, ✓, ✓) — row turns green immediately
- [ ] Toggle one cell wrong — green disappears
- [ ] Complete "Weapons targeting" row (✗, ✓, ✓) — row turns green
- [ ] Complete all 6 rows — all green, then Check button still reveals abstract
- [ ] Verify "Under Which Possibility?" puzzle also works (same LOG type)
- [ ] Check dark mode: green rows visible against dark background
- [ ] No regression in wrong-cell red feedback on Check button press
- [ ] No regression in puzzle reveal flow

## Acceptance Criteria

- [ ] Each correctly completed row turns green immediately (no Check button needed)
- [ ] Green disappears if any cell in the row changes to wrong
- [ ] Check button still works as before (reveals abstract when all correct, shows hints when wrong)
- [ ] Both light and dark mode green are visible and distinct from hover state
- [ ] All existing LOG puzzles behave correctly

---

*Plan 0302 v1, written S67, 2026-05-07. Auditor: Argus.*
