# Plan 0271: Codebase Refactoring and Size Reduction

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** Medium-High
**Scope:** `build/reader.js`, `build/preprocess.py`, `build/build-puzzles.py`, `build/utils.py` (new), repo hygiene
**Constraint:** Output must remain a single self-contained HTML file. No external dependencies.
**Annealing:** MED LOW LOW
**Note:** Phase 7 (Hover Data Architecture) is DEFERRED — skip it.

---

## Problem Statement

Relinquishment.html is 1.02 MB. A full codebase audit reveals:

- **67.6% is JavaScript** (690 KB) — unminified, with dead code and duplication
- **19.9% is hover JSON data** (203 KB) — unminified, contains 20 embedded SVGs
- **reader.js (80 KB)** has dead code, duplicated patterns, and two complete magnetosphere SVGs
- **Build scripts (340 KB Python)** scatter the same 5 colors across 187 locations in 4 files, reimplement escape() 3 times, and fragment the hover system across 3 scripts
- **Git tracks 572 KB of LaTeX build artifacts** and duplicates the 1 MB HTML file

Conservative estimate: **150-250 KB savings** (15-25%) from deduplication, dead code removal, and minification — without losing any functionality or self-containedness.

---

## Phase 1: Dead Code Removal (reader.js)

**Target savings: ~15 KB**

### 1a. Remove defunct popup navigation system

Lines 461-599 of reader.js define a complete popup navigation system (backdrop, container, list, buildPopupContents, navigateTo, openPopup, closePopup, event bindings) that is **never displayed**. Plan 0268 will implement this properly — this dead scaffolding must go before 0268 runs.

- Delete lines 461-599 (DOM creation, 4 functions, event bindings)
- Verify no other code references `navPopup`, `navBackdrop`, `buildPopupContents`, `navigateTo`, `openPopup`, `closePopup`

### 1b. Remove commented-out Science/Story filter buttons

Lines 413-417: commented-out `nav.appendChild(scienceBtn)` and `nav.appendChild(storyBtn)`. The filter buttons were disabled intentionally; the commented code is dead weight. Also remove the supporting functions if they're only reachable through these buttons:

- Check if `applyFilters()`, `updateFilterButtons()` are called from anywhere besides the commented-out buttons
- If orphaned, delete the functions AND the button creation code (scienceBtn, storyBtn DOM elements)

### 1c. Remove outdated clipboard fallback

`fallbackCopy()` (lines 20-28) uses `document.execCommand('copy')` for IE11 compatibility. IE11 is EOL since Jan 2023. All target browsers support `navigator.clipboard`. Remove the fallback and simplify `copyToClipboard()`.

---

## Phase 2: Deduplication (HTML output)

**Target savings: ~20 KB**

### 2a. Deduplicate puzzle utility functions

Currently getSolved(), setSolved(), escHtml(), sha256() are repeated in every puzzle's IIFE (3x in current book, will grow). Extract to a single shared block:

In `preprocess.py` `inject_chapter_puzzles()`:
- Inject a single `<script>` block before the first puzzle containing the 4 shared utilities
- Each puzzle IIFE references the shared functions instead of redefining them
- Savings: ~1.5 KB now, scales with puzzle count

### 2b. Deduplicate SVG animation @media rules

5 identical `@media(prefers-reduced-motion:reduce)` blocks inside SVG `<defs>`. Extract to a single `<style>` in the `<head>` or first SVG:
```css
@media(prefers-reduced-motion:reduce) {
  animate, animateMotion, animateTransform { display: none }
}
```
Savings: ~444 bytes (minor but free).

### 2c. Deduplicate kbtn-sh SVG filter

`<filter id="kbtn-sh">` defined 6 times inside individual SVGs. Move to a single shared `<svg>` hidden defs block at top of `<body>`:
```html
<svg style="display:none"><defs>
  <filter id="kbtn-sh"><feDropShadow dx="1" dy="1" stdDeviation="1.5" flood-opacity="0.15"/></filter>
</defs></svg>
```
Each SVG references `filter="url(#kbtn-sh)"` from the shared definition. Savings: ~400 bytes.

### ~~2d. Consolidate magnetosphere SVG~~ — SKIPPED

The dual magnetosphere SVGs (dark/light) are intentionally separate. Two complete copies is correct — CSS custom properties inside SVGs have cross-browser issues (print, older WebKit). Keep as-is.

---

## Phase 3: Build System Consolidation

**Target: maintainability, not HTML size**

### 3a. Extract shared color palette

Create `build/colors.py`:
```python
COLORS = {
    'primary': '#1a5276',
    'secondary': '#2471a3',
    'teal': '#2a9b9a',
    'purple': '#9b7db8',
    'gold': '#d4a847',
    'light_blue': '#5dade2',
    'accent_blue': '#6ba3f7',
}
```

All build scripts import from `colors.py`. A brand color change becomes a 1-line edit.

### 3b. Extract shared utilities

Create `build/utils.py`:
```python
import html as _html

def esc(s):
    """HTML-escape a string."""
    return _html.escape(str(s), quote=True)
```

Replace 3 independent `escape()` implementations in preprocess.py, build-puzzles.py, build-tooltips.py.

### 3c. Unify .hover-term CSS

Currently defined differently in 3 files (italic vs. non-italic, pointer vs. help cursor). Consolidate to a single canonical definition in `colors.py` or a new `build/styles.py`, imported by all consumers.

---

## Phase 4: JavaScript Minification

**Target savings: ~35-40 KB**

### 4a. Add JS minification to build pipeline

After reader.js is injected into the HTML, minify it. Options (in order of preference):

1. **Python-native minifier** (no new dependency): `rjsmin` or `jsmin` — pip install, ~70% size reduction on whitespace-heavy code
2. **Simple whitespace stripper** (zero dependency): a 20-line Python function that strips comments and collapses whitespace. Gets ~50% of the benefit.
3. **terser/uglify** (Node dependency): best compression but adds node_modules dependency

Recommendation: Option 2 (zero-dependency stripper) applied as a post-processing step in preprocess.py. reader.js stays human-readable in source; only the built HTML gets minified JS.

Implementation:
```python
def minify_js(text):
    """Strip JS comments and collapse whitespace. Preserves string literals."""
    # Remove single-line comments (not inside strings)
    # Remove multi-line comments
    # Collapse runs of whitespace to single space
    # Remove whitespace around operators
    return result
```

Add to `inject_reader_js()` in preprocess.py, applied before injection.

### 4b. Minify embedded CSS

Same approach for `<style>` blocks: strip comments, collapse whitespace. Less savings than JS but free to add.

### 4c. Minify hover JSON data

The hover-data JSON (203 KB) likely has formatting whitespace from `json.dumps(indent=...)`. Remove the indent:
```python
json.dumps(hover_dict, separators=(',', ':'))  # compact, no whitespace
```
This alone could save 20-40 KB depending on current indentation.

---

## Phase 5: SVG Optimization

**Target savings: ~10-20 KB**

### 5a. Audit embedded SVGs for optimization

20 SVGs are embedded in the hover JSON as escaped HTML strings. Check each for:
- Unnecessary `xmlns` declarations (only needed on root SVG)
- Redundant `fill="none"` or `stroke="none"` defaults
- Excessive decimal precision on coordinates (3+ decimals → 1)
- Empty `<g>` wrappers
- Unnecessary `id` attributes on elements not referenced

### 5b. Strip SVG metadata in build pipeline

Add a post-processing step in `generate-hover.py` or `preprocess.py` that strips:
- `<!-- comments -->`
- `<metadata>` blocks
- `data-name` attributes (Illustrator artifact)
- Excessive whitespace between attributes

---

## Phase 6: Repository Hygiene

**Target: git cleanliness, not HTML size**

### 6a. Remove tracked LaTeX artifacts

These are regenerated on every build:
```
Relinquishment.aux, .fdb_latexmk, .fls, .log, .bcf, .bbl, .blg
texput.pdf
```
```bash
git rm --cached Relinquishment.aux Relinquishment.fdb_latexmk \
  Relinquishment.fls Relinquishment.log Relinquishment.bcf \
  Relinquishment.bbl Relinquishment.blg texput.pdf
```
Update `.gitignore` to ensure they stay excluded. Savings: 572 KB from tracked files.

### 6b. Remove stale draft stub

`docs/downloads/Relinquishment-draft.html` is 272 bytes (near-empty stub). Either regenerate it properly or delete it.

### 6c. Verify .gitignore coverage

Several entries in `.gitignore` have comments saying files "belong in aurasys-memory" but are tracked anyway (plans/). This is intentional (plans are part of the project). Clean up the misleading comments.

---

## Phase 7: Hover Data Architecture (DEFERRED — largest single target)

**Potential savings: 50-100 KB. But high complexity, so deferred to post-release.**

The hover JSON (203 KB, 196 entries) is the single largest data structure. Opportunities:
- **Lazy loading**: inject only the terms that appear in the current page view (but breaks self-containedness — skip)
- **Dictionary compression**: many entries share phrasing ("The [X] is a..."). A small dictionary + substitution could compress significantly
- **SVG externalization**: move the 20 SVGs to `<template>` elements in HTML, reference by ID from JSON. Saves the HTML-escaping overhead (~20% per SVG)
- **Pruning**: audit whether all 196 entries are actually referenced by hover-term spans in the HTML

Mark as backlog. Evaluate post-release based on real reader feedback about load times.

---

## Anneal: Failure Mode Analysis

### MEDIUM

**M1. JS minifier breaks code.**
A naive regex-based minifier will mangle string literals or regex patterns.
**Mitigation:** Phase 4 option 2 (whitespace stripper) is conservative — only strips line comments NOT inside strings, collapses whitespace. No variable renaming. Test by diffing behavior in browser console. Add `make validate-js` with headless Playwright.

### LOW

**L2. Shared SVG filter breaks cross-browser.**
Moving `<filter id="kbtn-sh">` to a hidden `<svg>` defs block may not resolve `url(#id)` across SVG boundaries in older WebKit.
**Mitigation:** Test on modern browsers. If any fails, keep filters inline (skip Phase 2c — only 400 bytes).

**L3. Dead code removal breaks an undiscovered reference.**
**Mitigation:** `grep -r` across entire repo before deletion. Run Playwright suite after.

**L4. Color palette module creates import dependency.**
**Mitigation:** `sys.path.insert(0, Path(__file__).parent)` at top of each script.

**L5. JSON minification breaks hover panel.**
**Mitigation:** JSON is parsed as whole by `JSON.parse()`. No substring matching. Safe.

**L6. SVG optimization removes a visually important attribute.**
**Mitigation:** Visual diff with Playwright screenshots. Any visible change = revert that SVG.

---

## Execution Order

| Phase | Dependency | Effort | HTML Savings | Risk |
|-------|-----------|--------|-------------|------|
| 1 Dead code | None | 1 hr | ~15 KB | Low |
| 2 Dedup | None | 2 hr | ~14 KB | Low-Med |
| 3 Build consolidation | None | 2 hr | 0 (maintenance) | Low |
| 4 Minification | Phase 1+2 done | 3 hr | ~35-40 KB | Med |
| 5 SVG optimization | None | 2 hr | ~10-20 KB | Low |
| 6 Repo hygiene | None | 30 min | 0 (git only) | Low |
| 7 Hover architecture | DEFERRED | 6+ hr | ~50-100 KB | High |

**Phases 1-6 total: ~10 hours, ~74-89 KB savings (7-9% of file)**
**With Phase 7: ~124-189 KB savings (12-19%)**

Phases 1, 2, 3, 5, 6 are independent and can be parallelized across Generator shells. Phase 4 should run after 1+2 to avoid minifying dead code.

---

## Acceptance Criteria

1. Relinquishment.html ≤ 950 KB (currently 1,020 KB — 7% reduction minimum)
2. All puzzles functional (click, solve, localStorage persistence)
3. All hover tooltips display correctly
4. All SVGs render identically (visual diff)
5. Magnetosphere toggle works in light and dark mode
6. No JavaScript errors in browser console
7. `make` builds cleanly with no new warnings
8. `verify-deep-links.py` passes
9. Playwright test suite passes (if available)
10. Phone test: book loads, scrolls, and interacts normally on Bruce's phone
11. File remains fully self-contained (no external dependencies)

---

## Handoff Prompt (Phases 1-2)

```
You are the Generator. Read plan 0271 in ~/software/relinquishment/plans/.
Execute Phases 1 and 2 only. Remove dead code from reader.js (defunct popup,
commented-out filter buttons, clipboard fallback). Deduplicate puzzle utilities,
SVG filters, and @media rules in preprocess.py output. Consolidate magnetosphere
SVG in reader.js. Build, verify no JS errors, push.
```

## Handoff Prompt (Phase 3)

```
You are the Generator. Read plan 0271 in ~/software/relinquishment/plans/.
Execute Phase 3 only. Create build/colors.py and build/utils.py. Update
preprocess.py, build-puzzles.py, and build-tooltips.py to import shared
colors and escape function. Unify .hover-term CSS definition. Build, verify
output unchanged, push.
```

## Handoff Prompt (Phase 4)

```
You are the Generator. Read plan 0271 in ~/software/relinquishment/plans/.
Execute Phase 4 only. Add a JS minification step to preprocess.py that strips
comments and collapses whitespace from the reader.js injection. Also minify
CSS style blocks and compact the hover JSON. Build, verify no JS errors in
browser, push.
```
