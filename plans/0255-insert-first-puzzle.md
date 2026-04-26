# Plan 0255 — Insert First Puzzle into Book HTML

**Goal:** Insert pz-mc-t2-002 "The 2DEG in Your Pocket" into the main book HTML as an end-to-end proof of the puzzle-in-book pipeline. One puzzle, fully functional, gated on `approved: true` in puzzle-tracker.yaml.

**Why this puzzle:** MC type (simplest JS), p1 level, the-flat chapter (well-understood structure), already has a working egg reward page at `/eggs/the-flat/`. Minimal risk, maximum validation.

---

## Manifest-First Checklist

Before ANY code changes:

1. ✅ `deep-links.yaml` — pz-mc-t2-002 already registered (done in S65)
2. ✅ `puzzle-tracker.yaml` — entry exists, `approved: false`, `location.chapter: the-flat`
3. ✅ `puzzle-data.yaml` — full content exists (question, options, answer_key, hint, abstract, egg_url)
4. ✅ `easter-egg-manifest.yaml` — the-flat egg registered (done in Plan 0254)
5. **Action:** Set `approved: true` in puzzle-tracker.yaml for pz-mc-t2-002 FIRST, before generating HTML

---

## Architecture

### What changes

| File | Change |
|------|--------|
| `build/puzzle-tracker.yaml` | Set `approved: true` for pz-mc-t2-002 |
| `build/preprocess.py` | Add `inject_chapter_puzzles()` function + call in `--fix-html` pipeline |
| `build/puzzle-data.yaml` | No change (content authority stays here) |
| Relinquishment.html | Rebuilt via `make html` — puzzle appears at end of the-flat chapter |

### What does NOT change

- `build/build-puzzles.py` — standalone puzzle page is untouched
- `build/reader.js` — independent of puzzles, no coupling needed
- `docs/style.css` — puzzle CSS goes inline in preprocess.py injection (same pattern as SVG injections)

### Insertion point

The puzzle goes at the **end of the the-flat chapter content**, just before the `custodian:dance` interlude div. In the current HTML, this is after the paragraph ending "whatever lives there hears everything." and before `<div class="custodian-interlude" id="custodian:dance">`.

The marker text for `str.find()`: `<div class="custodian-interlude" id="custodian:dance">`

### Approved gating

`inject_chapter_puzzles()` reads `puzzle-tracker.yaml` and only injects puzzles where `approved: true`. This means:
- Setting approved=false removes the puzzle from next rebuild
- No puzzle appears until Bruce explicitly approves it
- The approval field is in puzzle-tracker.yaml (metadata authority)

---

## Phase 1: Approve + Inject Function

### Step 1.1 — Set approved: true

In `build/puzzle-tracker.yaml`, change `approved: false` → `approved: true` for pz-mc-t2-002.

### Step 1.2 — Add `inject_chapter_puzzles()` to preprocess.py

Add a new function in the injection section (after `inject_genesis_illustrations`, before `fix_html_glossary_names`). Pattern follows `inject_flat_diagram()`.

**Function signature:** `def inject_chapter_puzzles(html_path):`

**Logic:**
1. Read `puzzle-tracker.yaml` — filter for `approved: true`
2. Read `puzzle-data.yaml` — get content for approved puzzles
3. For each approved puzzle:
   a. Find chapter boundary using tracker's `location.chapter` field
   b. Build puzzle HTML container (same structure as `render_container()` in build-puzzles.py)
   c. Build inline `<style>` block with MC puzzle CSS (subset of build-puzzles.py CSS)
   d. Build inline `<script>` with MC puzzle engine (subset of JS_ENGINE)
   e. Insert before the next interlude or chapter boundary
4. Print count of injected puzzles

**Chapter boundary detection:**
- For the-flat chapter: find marker `<div class="custodian-interlude" id="custodian:dance">`
- Insert puzzle HTML block just before this marker
- Wrap in `<details class="puzzle-section">` for collapsibility

**Puzzle HTML structure (matching build-puzzles.py render_container):**
```html
<details class="puzzle-section" open>
  <summary>Puzzle</summary>
  <div class="puzzle-container" id="pz-mc-t2-002" data-puzzle-id="pz-mc-t2-002" data-puzzle-type="mc">
    <h3>The 2DEG in Your Pocket</h3>
    <p class="gateway-blurb">🧩 Every smartphone on Earth contains a two-dimensional electron gas. Why is it there?</p>
    <p class="question">Every modern smartphone contains a two-dimensional electron gas. Why?</p>
    <div class="interaction"></div>
    <p class="hint" id="hint-pz-mc-t2-002">[hint text]</p>
    <div class="result" id="result-pz-mc-t2-002">
      <div class="solved-badge">✓ Solved</div>
      <blockquote class="abstract">[abstract text]</blockquote>
      <p class="egg-reward"><a href="../eggs/the-flat/" target="_blank">🔓 Continue exploring →</a></p>
    </div>
    <noscript><p class="puzzle-fallback">Enable JavaScript to interact with this puzzle.</p></noscript>
  </div>
</details>
```

**Note on heading level:** Use `<h3>` not `<h2>` — puzzles are subordinate to the chapter heading.

**Note on egg_url:** The path `../eggs/the-flat/` is relative from `docs/downloads/Relinquishment.html` to `docs/downloads/eggs/the-flat/index.html`. Verify this resolves correctly.

### Step 1.3 — Inline JS and CSS

The JS engine for MC puzzles is small. Embed it as a `<script>` block inside the puzzle section. Required functions (extract from build-puzzles.py JS_ENGINE):
- `getSolved()`, `setSolved()` — localStorage persistence
- `revealPuzzle()` — show result, hide interaction
- `showHint()` — show hint on wrong answer
- `sha256()` — hash answer for checking
- `initMC()`, `checkMC()` — MC-specific init and check
- Initialization: `querySelectorAll(".puzzle-container")` loop

**Differences from standalone page:**
- No `PD` global object — use a single puzzle data object
- No bridge builder, KM, or other type code
- No `updateCounts()` — no progress counter in the book
- No `resetPuzzles()` — no reset button in the book
- Storage key: same `relinquishment-puzzles-solved` (shared state with standalone page)

**CSS subset needed for MC only:**
- `.puzzle-section` (new — collapsible wrapper, styled like `.tech-section`)
- `.puzzle-container`, `.puzzle-container.solved`
- `.question`, `.gateway-blurb`
- `.option-btn`, `.option-btn:hover`, `.option-btn.wrong`, `.option-btn.correct`
- `@keyframes shake`
- `.hint`, `.hint.visible`, `.result`, `.result.visible`
- `.solved-badge`, `.abstract`
- `.egg-reward` (already in build-puzzles.py CSS)
- `.puzzle-fallback`
- Dark mode variants for all above
- Mobile: `.option-btn { min-height: 44px; }` for touch targets

**Pre-hash the answer:** The standalone page uses `sha256(key)` and compares to stored hashes. For inline injection, pre-compute `sha256("b")` and embed as a constant. Value: compute at build time in Python using `hashlib.sha256(b"b").hexdigest()`.

### Step 1.4 — Wire into --fix-html pipeline

In the `elif sys.argv[1] == '--fix-html':` block, add `inject_chapter_puzzles(sys.argv[2])` after `inject_genesis_illustrations` and before `inject_questions_index`.

---

## Phase 2: Rebuild + Verify

### Step 2.1 — Rebuild HTML

```bash
make html
```

This runs the LaTeX→HTML pipeline including `preprocess.py --fix-html`, which now calls `inject_chapter_puzzles()`.

### Step 2.2 — Verify deep links

```bash
python3 build/verify-deep-links.py
```

Expected: still clean (pz-mc-t2-002 is category: puzzle, which is in SKIP_CATEGORIES).

### Step 2.3 — Verify puzzle appears in HTML

```bash
grep -c 'pz-mc-t2-002' docs/downloads/Relinquishment.html
# Expected: ≥3 (id, data-puzzle-id, hint-id, result-id)
```

### Step 2.4 — Verify egg link resolves

```bash
# From Relinquishment.html location, check relative path
ls docs/downloads/eggs/the-flat/index.html
# Expected: exists
```

### Step 2.5 — Browser test

Open `docs/downloads/Relinquishment.html` in browser:
1. Navigate to The Flat → Wormholes in the Flat
2. Scroll to end of chapter
3. Puzzle section should appear (collapsible, open by default)
4. Click wrong answer → shake animation + hint appears
5. Click correct answer (b) → solved badge + abstract + egg link
6. Click egg link → opens the-flat egg page
7. Reload page → puzzle remembers solved state (localStorage)
8. Check dark mode (if applicable)
9. Check mobile viewport (option buttons ≥44px)

---

## Phase 3: Commit

Single commit: `Plan 0255: insert first puzzle (pz-mc-t2-002) into book HTML`

Files committed:
- `build/preprocess.py` (inject_chapter_puzzles function)
- `build/puzzle-tracker.yaml` (approved: true for pz-mc-t2-002)
- `docs/downloads/Relinquishment.html` (rebuilt)
- `plans/0255-insert-first-puzzle.md`

---

## Acceptance Criteria

1. pz-mc-t2-002 appears at end of the-flat chapter in Relinquishment.html
2. Puzzle is interactive: wrong answer shakes + shows hint, correct answer reveals abstract
3. Egg reward link appears after solving and navigates to `/eggs/the-flat/`
4. `verify-deep-links.py` passes clean
5. Puzzle state persists across page reloads (localStorage)
6. No puzzle appears in PDF (injection is HTML-only via `--fix-html`)
7. `puzzle-tracker.yaml` shows `approved: true` for pz-mc-t2-002
8. Dark mode renders correctly
9. Mobile touch targets ≥44px

## Scope Boundary

This plan inserts ONE puzzle (MC type only). It does NOT:
- Add other puzzle types to the book
- Create a general-purpose puzzle injection system for all chapters
- Modify the standalone puzzles.html page
- Change any other puzzle's approval status
- Add progress tracking or reset functionality to the book

Future plans will generalize the injection function to handle all types and all chapters. This plan validates the pipeline.

---

## Risk Notes

- **CSS collision:** Puzzle CSS class names (.puzzle-container, .option-btn, etc.) must not collide with existing book CSS. Grep the HTML `<style>` block for conflicts before injecting. If collision, prefix with `pz-`.
- **JS scope:** Puzzle JS should be wrapped in an IIFE to avoid polluting global scope. The standalone page uses globals; the book injection should not.
- **localStorage key sharing:** Using the same `relinquishment-puzzles-solved` key means solving in the book and on the standalone page share state. This is intentional — a reader who solves on the puzzle page sees it solved in the book too.
