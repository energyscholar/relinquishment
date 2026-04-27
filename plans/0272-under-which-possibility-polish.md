# Plan 0272: Polish "Under Which Possibility?" and Install in Three Possibilities

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** High
**Scope:** `build/puzzle-data.yaml`, `build/puzzle-tracker.yaml`, `build/build-puzzles.py`, `build/preprocess.py`
**Annealing:** MED LOW LOW

---

## Context

"Under Which Possibility?" (pz-log-t6-002) is a truth table where the reader marks 6 statements as true/false under Possibilities A, B, and C. The punchline: 3 of 6 rows hold under ALL three possibilities. This is the book's thesis — "preparation not disclosure" — made interactive.

Currently: approved, p2, located at `weigh-the-evidence` (end of book).

Bruce wants it: polished, prominent, installed in `three-possibilities` (early Flat), promoted to p1. The problem: at that early point, the reader doesn't yet know terms like "2DEG," "silence gap," or "the Custodian." Solution: selective tooltips on rows that need them.

---

## Dignity Net: Tooltip Design Principles

- Tooltips **inform**, not argue. They define the term so the reader can evaluate the claim themselves.
- Rows WITHOUT tooltips signal: "you already know enough to answer this."
- Tooltips never hint at the correct answer.
- The pattern: 3 tooltips, 3 absent. The gap IS the pedagogy — it teaches the reader which concepts are self-evident and which require context they haven't yet acquired.

---

## Phase 1: Add Row Tooltips to Puzzle Data

### 1a. Update `puzzle-data.yaml`

Change the `rows` for pz-log-t6-002 from flat strings to mixed string/object format:

```yaml
    rows:
      - text: "The Flat is real — 2DEGs exist in every phone"
        tooltip: "A two-dimensional electron gas (2DEG) forms at semiconductor interfaces. Every smartphone contains one in its radio-frequency transistors."
      - "The physics in this book is published, peer-reviewed science"
      - text: "The silence gap exists in the scientific literature"
        tooltip: "A documented absence: multiple scientific fields that could study this topic have published nothing on it."
      - "Something lives in the Flat"
      - "Healer guided Bruce through published science"
      - text: "The Custodian manages cryptographic infrastructure"
        tooltip: "A figure described later in this book who is said to hold cryptographic keys under ethical constraints derived from the UDHR."
```

**Tooltip rationale:**
| Row | Tooltip | Why |
|-----|---------|-----|
| 1. The Flat / 2DEGs | YES | Reader hasn't encountered 2DEGs yet |
| 2. Physics is published | NO | Self-evident — the book cites real papers |
| 3. Silence gap | YES | Concept not yet introduced at this chapter |
| 4. Something lives | NO | THE core distinguishing claim — obvious split |
| 5. Healer guided | NO | Reader just read Three Possibilities — this is the chapter's subject |
| 6. Custodian | YES | Not yet introduced at this point in the book |

### 1b. Update `build_json()` in `build-puzzles.py`

Currently line 265: `d['rows'] = puzzle['rows']` passes rows through as-is.

Change to normalize rows to objects (same pattern as columns at lines 267-272):
```python
elif t == 'log':
    rows = puzzle['rows']
    d['rows'] = []
    for r in rows:
        if isinstance(r, dict):
            d['rows'].append({'text': r['text'], 'tooltip': r.get('tooltip', '')})
        else:
            d['rows'].append({'text': r, 'tooltip': ''})
    # ... columns and correct unchanged
```

### 1c. Update `initLOG()` in `build-puzzles.py`

Currently line 1548-1549:
```javascript
html += "<tr><td>" + esc(d.rows[r]) + "</td>";
```

Change to handle object rows with tooltip (same pattern as columns at lines 1542-1545):
```javascript
var rowText = typeof d.rows[r] === "object" ? d.rows[r].text : d.rows[r];
var rowTip = typeof d.rows[r] === "object" && d.rows[r].tooltip ? d.rows[r].tooltip : "";
html += "<tr><td" + (rowTip ? ' title="' + esc(rowTip) + '" style="cursor:help;border-bottom:1px dotted #888"' : "") + ">" + esc(rowText) + "</td>";
```

---

## Phase 2: Relocate and Promote

### 2a. Update `puzzle-tracker.yaml`

Change pz-log-t6-002:
- `level: p2` → `level: p1`
- `location.chapter: weigh-the-evidence` → `location.chapter: three-possibilities`
- `installed: false` → `installed: true`
- Update rationale: `"A/B/C truth table — reader tests the framework they just learned"`

### 2b. Add chapter marker in `preprocess.py`

In `inject_chapter_puzzles()`, add to CHAPTER_MARKERS (currently line ~3317):
```python
CHAPTER_MARKERS = {
    'the-flat': '<div class="custodian-interlude" id="custodian:dance">',
    'three-possibilities': '<div class="custodian-interlude" id="custodian:flat">',
}
```

The puzzle will be inserted just before the Custodian interlude that follows Three Possibilities — placing it at the chapter's end, after the reader has absorbed A, B, and C.

---

## Phase 3: Enable LOG Type in Book Injection

Currently `inject_chapter_puzzles()` (preprocess.py ~line 3407) only handles `mc` and `gd`:
```python
if ptype not in ('mc', 'gd'):
    continue
```

Add `log` support. The LOG puzzle needs:

### 3a. Expand type filter

```python
if ptype not in ('mc', 'gd', 'log'):
    continue
```

### 3b. Add LOG rendering block

After the `elif ptype == 'gd':` block and before the `puzzle_html = f'''` assembly, add a `elif ptype == 'log':` block.

**HTML body** for LOG:
```python
if ptype == 'log':
    question = _esc(puzzle.get('question', ''))
    rows_data = puzzle.get('rows', [])
    cols_data = puzzle.get('columns', [])
    correct_data = puzzle.get('correct', [])

    body_html = f'''    <h3>{title}</h3>
    {blurb_html}
    <p class="pz-question">{question}</p>
    <div class="pz-interaction" id="pz-inter-{pid}"></div>
    <p class="pz-hint" id="pz-hint-{pid}">{_esc(puzzle.get("hint", ""))}</p>'''
```

**JS IIFE** for LOG — the truth table is rendered dynamically (same approach as build-puzzles.py initLOG):
```python
# Serialize rows as JSON (handle string or object format)
import json
rows_json = []
for r in rows_data:
    if isinstance(r, dict):
        rows_json.append({'text': r['text'], 'tooltip': r.get('tooltip', '')})
    else:
        rows_json.append({'text': r, 'tooltip': ''})

cols_json = []
for c in cols_data:
    if isinstance(c, dict):
        cols_json.append({'text': c['text'], 'tooltip': c.get('tooltip', '')})
    else:
        cols_json.append({'text': c, 'tooltip': ''})

puzzle_js = f'''
(function() {{
{PZ_JS_UTILS}
  var pid = "{pid}";
  var rows = {json.dumps(rows_json)};
  var cols = {json.dumps(cols_json)};
  var correct = {json.dumps(correct_data)};
  var grid = [];
  for (var r = 0; r < rows.length; r++) {{ grid[r] = []; for (var c = 0; c < cols.length; c++) grid[r][c] = null; }}

  function render() {{
    var inter = document.getElementById("pz-inter-" + pid);
    if (!inter) return;
    var html = '<table class="pz-log-table"><thead><tr><th></th>';
    cols.forEach(function(col) {{
      var text = typeof col === "object" ? col.text : col;
      var tip = typeof col === "object" && col.tooltip ? col.tooltip : "";
      html += tip ? '<th title="' + escHtml(tip) + '" style="cursor:help;text-decoration:underline dotted">' + escHtml(text) + '</th>' : '<th>' + escHtml(text) + '</th>';
    }});
    html += '</tr></thead><tbody>';
    for (var r = 0; r < rows.length; r++) {{
      var rowText = typeof rows[r] === "object" ? rows[r].text : rows[r];
      var rowTip = typeof rows[r] === "object" && rows[r].tooltip ? rows[r].tooltip : "";
      html += '<tr><td' + (rowTip ? ' title="' + escHtml(rowTip) + '" style="cursor:help;border-bottom:1px dotted #888"' : '') + '>' + escHtml(rowText) + '</td>';
      for (var c = 0; c < cols.length; c++) {{
        var v = grid[r][c] === true ? "\\u2713" : (grid[r][c] === false ? "\\u2717" : "");
        html += '<td class="pz-log-cell" data-r="' + r + '" data-c="' + c + '">' + v + '</td>';
      }}
      html += '</tr>';
    }}
    html += '</tbody></table><button class="pz-option-btn pz-log-check">Check</button>';
    inter.innerHTML = html;

    var cells = inter.querySelectorAll(".pz-log-cell");
    for (var j = 0; j < cells.length; j++) {{
      (function(td) {{ td.addEventListener("click", function() {{
        var r = parseInt(td.dataset.r), c = parseInt(td.dataset.c);
        if (grid[r][c] === null) grid[r][c] = true;
        else if (grid[r][c] === true) grid[r][c] = false;
        else grid[r][c] = null;
        render();
      }}); }})(cells[j]);
    }}

    inter.querySelector(".pz-log-check").addEventListener("click", function() {{
      var ok = true;
      for (var r = 0; r < rows.length; r++) for (var c = 0; c < cols.length; c++) {{
        if (grid[r][c] !== correct[r][c]) {{
          ok = false;
          var td = inter.querySelector('.pz-log-cell[data-r="' + r + '"][data-c="' + c + '"]');
          if (td) td.classList.add("pz-wrong");
        }}
      }}
      if (ok) {{ revealPuzzle(); }}
      else {{
        setTimeout(function() {{ var ws = inter.querySelectorAll(".pz-wrong"); for (var k = 0; k < ws.length; k++) ws[k].classList.remove("pz-wrong"); }}, 800);
        showHint();
      }}
    }});
  }}

  function revealPuzzle() {{
    var el = document.getElementById(pid);
    if (el) el.classList.add("pz-solved");
    var inter = document.getElementById("pz-inter-" + pid);
    if (inter) inter.style.display = "none";
    var hint = document.getElementById("pz-hint-" + pid);
    if (hint) hint.classList.remove("pz-visible");
    var result = document.getElementById("pz-result-" + pid);
    if (result) result.classList.add("pz-visible");
    setSolved(pid);
  }}

  function resetPuzzle() {{
    try {{ var s = getSolved(); delete s[pid]; localStorage.setItem(SKEY, JSON.stringify(s)); }} catch(e) {{}}
    var el = document.getElementById(pid);
    if (el) el.classList.remove("pz-solved");
    var inter = document.getElementById("pz-inter-" + pid);
    if (inter) {{ inter.style.display = ""; }}
    var hint = document.getElementById("pz-hint-" + pid);
    if (hint) hint.classList.remove("pz-visible");
    var result = document.getElementById("pz-result-" + pid);
    if (result) result.classList.remove("pz-visible");
    grid = [];
    for (var r = 0; r < rows.length; r++) {{ grid[r] = []; for (var c = 0; c < cols.length; c++) grid[r][c] = null; }}
    render();
  }}

  function showHint() {{
    var h = document.getElementById("pz-hint-" + pid);
    if (h) h.classList.add("pz-visible");
  }}

  function init() {{
    if (getSolved()[pid]) {{ revealPuzzle(); return; }}
    render();
  }}

  var resetBtn = document.getElementById("pz-reset-" + pid);
  if (resetBtn) {{
    resetBtn.addEventListener("click", function(e) {{ e.preventDefault(); resetPuzzle(); }});
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", init);
  }} else {{
    init();
  }}
}})();'''
```

### 3c. Add LOG-specific CSS to PZ_CSS

Append to the PZ_CSS string (before the closing `'''`):

```css
.pz-log-table { width: 100%; border-collapse: collapse; margin-bottom: 1em; font-size: 0.92em; }
.pz-log-table th { padding: 0.5em; text-align: center; border-bottom: 2px solid #1a5276; color: #1a5276; font-size: 0.9em; }
.pz-log-table td { padding: 0.5em; border-bottom: 1px solid #e0e0e0; }
.pz-log-table td:first-child { text-align: left; max-width: 55%; font-size: 0.9em; }
.pz-log-cell { text-align: center; cursor: pointer; font-size: 1.2em; min-width: 2.5em; user-select: none; transition: background 0.15s; }
.pz-log-cell:hover { background: #e8f0f8; }
.pz-log-cell.pz-wrong { background: #fdf2f2; color: #c0392b; }
.pz-log-check { margin-top: 0.5em; }
```

And dark mode:
```css
@media (prefers-color-scheme: dark) {
  .pz-log-table th { border-bottom-color: #6ba3f7; color: #6ba3f7; }
  .pz-log-table td { border-bottom-color: #333; }
  .pz-log-cell:hover { background: #2a3a4a; }
  .pz-log-cell.pz-wrong { background: #3a1a1a; }
}
```

---

## Phase 4: Build and Verify

1. `make` — build must succeed, verify-deep-links must pass
2. Open `http://localhost:8765/downloads/Relinquishment.html#spine:three-possibilities` — scroll to chapter end
3. Verify:
   - Puzzle appears collapsed at end of Three Possibilities, before Custodian interlude
   - Puzzle expands on click
   - Truth table renders with 6 rows × 3 columns
   - Cells cycle through ✓/✗/empty on click
   - Rows 1, 3, 6 show dotted underline and tooltip on hover
   - Rows 2, 4, 5 have NO tooltip (no underline, no cursor:help)
   - "Check" validates correctly (3 all-true rows, 3 mixed rows)
   - Wrong cells flash red briefly
   - Correct completion reveals abstract + Try again link
   - Try again resets the grid
   - Teal wash + braid border present (puzzle-section styling)
4. Open `http://localhost:8765/downloads/puzzles.html#pz-log-t6-002` — verify standalone version also shows tooltips
5. Commit, push

---

## Anneal: Failure Mode Analysis

### MEDIUM

**M1. LOG injection JS has a bug in the truth table rendering.**
This is the first LOG type injected into the book. The JS is complex (grid state, cell cycling, validation).
**Mitigation:** The JS is a direct port of the proven `initLOG()` from build-puzzles.py, adapted to the IIFE pattern already used by MC and GD injections. Test manually: fill all 18 cells correctly, verify solve; fill 1 wrong, verify red flash + hint; reset, verify grid clears.

### LOW

**L2. Chapter marker `custodian:flat` is fragile.**
If the Custodian interlude div changes (e.g., different id format), the injection point breaks silently.
**Mitigation:** `inject_chapter_puzzles()` already prints a count of injected puzzles. If "0 injected" for a puzzle that should inject, the marker is stale. The existing logging catches this.

**L3. Tooltips too long on mobile, overlap table cells.**
`title` attribute tooltips are rendered by the browser, not custom JS. On mobile, they appear as long-press popups.
**Mitigation:** All three tooltips are ≤ 130 characters — within comfortable display range. If mobile rendering is poor, a future plan could upgrade to the onHover system (which is already built). Not needed now.

---

## Acceptance Criteria

1. Puzzle appears at end of Three Possibilities chapter, before Custodian interlude
2. Promoted to p1 in tracker
3. 6 × 3 truth table renders correctly
4. Rows 1, 3, 6 have hover tooltips; rows 2, 4, 5 do not
5. Cell click cycles ✓ → ✗ → empty
6. Check button validates, wrong cells flash red
7. Correct solution reveals abstract
8. Try again resets grid to empty
9. Standalone puzzles.html also shows tooltips
10. Build + verify-deep-links passes

---

## Handoff Prompt

```
You are the Generator. Read plan 0272 in ~/software/relinquishment/plans/.
Implement all 4 phases. Add row tooltips to the Under Which Possibility
puzzle, promote to p1, relocate to three-possibilities, and add LOG type
support to inject_chapter_puzzles() in preprocess.py. All changes are in
build/puzzle-data.yaml, build/puzzle-tracker.yaml, build/build-puzzles.py,
and build/preprocess.py. Build, test in browser, push.
```
