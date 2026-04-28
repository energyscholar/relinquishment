# Plan 0274i: Puzzle Injection — Source of Truth Architecture

**Status:** READY FOR GENERATOR  
**Author:** Auditor (Argus S64)  
**Priority:** Critical — correctness of all 16 installed puzzles  
**Supersedes:** 0274f, 0274g, 0274h (all architecturally wrong)  
**Scope:** `build/preprocess.py`, `build/build-puzzles.py`  
**Annealing:** MED LOW LOW LOW  

---

## Problem Statement

Two independent rendering codepaths for puzzles:

1. **`build/build-puzzles.py`** → `docs/downloads/puzzles.html` (source of truth). All 10 types. Unprefixed CSS (`.option-btn`, `.hint`). Global `PD` data object + `initAllPuzzles()` dispatcher.

2. **`build/preprocess.py`** → `inject_chapter_puzzles()` (reimplemented). Only mc/gd/log. Prefixed CSS (`.pz-option-btn`, `.pz-hint`). Per-puzzle IIFEs. Lines 3534–4053.

The 16 installed puzzles may differ from their source-of-truth versions. 7 more types can't be installed at all. Plans 0274f/g/h proposed compounding the divergence by adding more reimplemented renderers.

**Fix:** `inject_chapter_puzzles()` extracts working puzzle HTML from the built `puzzles.html` instead of reimplementing.

---

## Phase 1: Rewrite inject_chapter_puzzles() (MED)

Replace the three reimplemented renderers with extraction from puzzles.html.

### JS Engine: Inject the Full Script Block

Inject the complete `<script>` block from puzzles.html (lines 1537–2671), PD blob and all. This includes ~1,100 lines of engine code plus a ~50-80KB JSON data object with all 33 puzzles.

Why this is safe:
- `initAllPuzzles()` (line 2555) iterates `.puzzle-container` **DOM elements**, not PD keys. Extra PD entries are inert.
- Every per-puzzle init is try-caught (line 2572). Failure → fallback text, other puzzles unaffected.
- `initBridge()` guards on `#bridge-svg` existence (line 2417-2418) and is try-caught (line 2581). No bridge DOM in book → silent no-op.
- `initReviewControls()` guards on missing buttons (line 2600). `updateCounts()` guards on missing elements. Both no-op in book.
- `window.addEventListener("load", ...)` is additive — no conflict with `reader.js` (which uses per-element handlers, no load listener).
- ~50-80KB of inert data in a 1-2MB+ book HTML. Acceptable.

**Do not filter PD or extract functions separately.** That creates a new divergence point.

### CSS: Rename Only

Auditor verified zero CSS collisions — the book HTML has no classes named `.hint`, `.option-btn`, `.result`, `.interaction`, `.question`, `.abstract`, `.solved`, or `.gateway-blurb` outside puzzle contexts.

Extract the `<style>` content from puzzles.html. Replace `.puzzle-collapse` → `.puzzle-section` throughout (the book's outer wrapper class). Inject as-is. No scoping needed.

### HTML Extraction and Summary Rewrite

Extract each puzzle's `<details>` block by matching `data-puzzle-wrap="{pid}"`. Transform:

1. Replace `<details class="puzzle-collapse" data-puzzle-wrap="...">` → `<details class="puzzle-section">`
2. Replace `<summary...>...</summary>` → `<summary>Puzzle &mdash; {summary_label}<span class="share-anchor" data-link-id="{pid}" aria-hidden="true"></span></summary>` where `summary_label` comes from deep-links.yaml (falling back to puzzle title), HTML-escaped.
3. Keep all inner HTML from `<div class="puzzle-container"` onward unchanged.
4. If tracker says `render: inline`, add `open` attribute to `<details>`.

### Extraction Functions

```python
def extract_puzzle_html(standalone_html, pid):
    """Extract a puzzle's <details> block by data-puzzle-wrap ID."""
    marker = f'data-puzzle-wrap="{pid}"'
    start = standalone_html.find(marker)
    if start == -1:
        return None
    tag_start = standalone_html.rfind('<details', 0, start)
    if tag_start == -1:
        return None
    depth = 0
    i = tag_start
    while i < len(standalone_html):
        if standalone_html[i:i+8] == '<details':
            depth += 1
        elif standalone_html[i:i+10] == '</details>':
            depth -= 1
            if depth == 0:
                return standalone_html[tag_start:i+10]
        i += 1
    return None

def extract_standalone_css(standalone_html):
    """Extract the first <style> block content."""
    m = re.search(r'<style>(.*?)</style>', standalone_html, re.DOTALL)
    return m.group(1) if m else ''

def extract_standalone_js(standalone_html):
    """Extract the JS engine (the <script> block containing initAllPuzzles)."""
    for m in re.finditer(r'<script>(.*?)</script>', standalone_html, re.DOTALL):
        if 'initAllPuzzles' in m.group(1):
            return m.group(1)
    return ''
```

### Delete from preprocess.py

- `PZ_CSS` block (lines 3534–3615) + `replace('{{','{')` call
- `PZ_JS_UTILS` block (lines 3618–3629) + `replace('{{','{')` call
- `_esc()` helper (lines 3530–3531)
- MC renderer (lines 3678–3775), GD renderer (lines 3777–3917), LOG renderer (lines 3919–4053)
- HTML assembly block (lines 4055–4107)
- Type filter `if ptype not in ('mc', 'gd', 'log')` (line 3659)
- `import hashlib as _hashlib` (line 3498)

### Keep

- `CHAPTER_INJECTION_TARGETS` + `CHAPTER_SECTION_IDS` dicts
- `find_injection_point()` + `find_chapter_end()`
- Tracker/data/deep-links loading
- Chapter grouping + level sorting
- Render mode + visibility handling

### Build Order

Add at top of function after loading tracker/data:

```python
standalone_path = REPO / 'docs' / 'downloads' / 'puzzles.html'
if not standalone_path.exists():
    print("  ERROR: puzzles.html not found — run build-puzzles.py first")
    return
standalone_html = standalone_path.read_text()
```

Verify Makefile runs `build-puzzles.py` before `preprocess.py --fix-html`.

### Graceful Failure

If extraction returns None for a puzzle, print warning and skip. Don't abort. Verification catches missing puzzles.

---

## Phase 2: Build, Verify, Browser Test (LOW)

1. `make dev` — zero errors, 16 injection confirmations
2. Open book in browser, test one MC, one GD, one LOG:
   - MC: wrong → shakes, correct → abstract + solved badge
   - GD: stages advance, progress dots, bridge text
   - LOG: grid renders, cells cycle, check validates
3. Solve one in book, check puzzles.html shows solved (shared localStorage)
4. Browser console: no JS errors

---

## Phase 3: Deep Link Visibility in puzzles.html (LOW)

In `build/build-puzzles.py` `wrap_collapsible()` (line 592-594), replace the `if inst:` block:

```python
if inst:
    book_url = f'Relinquishment.html#{pid}'
    full_url = f'relinquishment.ai/downloads/Relinquishment.html#{pid}'
    badge += f' <a href="{book_url}" class="collapse-badge installed-tag" title="View in book">INSTALLED</a>'
    badge += f' <span class="deep-link-url"><a href="{book_url}">{full_url}</a></span>'
```

Add CSS after `.installed-tag:hover` (~line 817):
```css
.deep-link-url { display: inline-block; margin-left: 0.5em; font-size: 0.75em; font-family: monospace; color: #888; word-break: break-all; }
.deep-link-url a { color: #888; text-decoration: none; border-bottom: 1px dotted #ccc; }
.deep-link-url a:hover { color: #1a5276; }
```

Dark-mode variant after `.installed-tag:hover` in dark section (~line 906):
```css
.deep-link-url a { color: #6ba3f7; border-bottom-color: #3a5a7a; }
```

Rebuild puzzles.html + book. Verify deep-link spans don't leak into book puzzles (Phase 1's summary rewrite replaces the entire `<summary>`, so they won't).

---

## Phase 4: Update verify_puzzle_injection() (LOW)

Line 4122 in preprocess.py, change:
```python
if ptype in ('mc', 'gd', 'log') and chapter in CHAPTER_INJECTION_TARGETS:
```
To:
```python
if chapter in CHAPTER_INJECTION_TARGETS:
```

Final full build. Verify 16 puzzles pass. Spot-check 3 in browser.

---

## Acceptance Criteria

1. All 16 installed puzzles render correctly — identical behavior to puzzles.html
2. No reimplemented renderers in preprocess.py — PZ_CSS, PZ_JS_UTILS, MC/GD/LOG renderers deleted
3. JS uses same engine as puzzles.html — full script block, `initAllPuzzles` dispatcher
4. All 10 types supported — type filter removed
5. Graceful failure — missing puzzle → warning + skip; JS try-catch on every init; missing DOM → no-op
6. Deep links visible in puzzles.html — copyable URL next to INSTALLED badge
7. Shared localStorage preserved — `relinquishment-puzzles-solved`
8. Build succeeds, verification OK, browser console clean

---

## Commit Plan

- Phase 1: `Plan 0274i phase 1: extract puzzles from source of truth instead of reimplementing`
- Phase 2: `Plan 0274i phase 2: verify all 16 installed puzzles in browser`
- Phase 3: `Plan 0274i phase 3: show deep link URLs in puzzles.html INSTALLED indicators`
- Phase 4: `Plan 0274i phase 4: update verification to expect all puzzle types`
