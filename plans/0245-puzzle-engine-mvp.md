# Plan 0245 — Puzzle Engine MVP: Standalone Preview Page

**Status:** READY for Generator
**Author:** Auditor (Argus S64)
**Date:** 2026-04-24
**Parent:** Plan 0233 (Easter Egg Architecture), Phase 1
**Purpose:** Build a standalone puzzle preview page with 3 working puzzles. Deploy to website. Share deep link with Gen for review. Do NOT embed puzzles in the book yet.

---

## What This Plan Does

Builds a standalone HTML page at a known URL showing 3 working puzzles. Each puzzle has a deep link anchor. The page uses the book's styling but is separate from the main HTML — like the SVG sheet but deployed.

Gen opens the URL, plays with the puzzles, and tells us whether this feels like discovery or homework. If she approves, a future plan embeds them in chapters.

---

## Architecture

### Deployed page

`docs/downloads/puzzles.html` — standalone HTML page, pushed to website.

Deep links:
- `relinquishment.ai/downloads/puzzles.html#puzzle-flat`
- `relinquishment.ai/downloads/puzzles.html#puzzle-genesis`
- `relinquishment.ai/downloads/puzzles.html#puzzle-silence-gap`

### What it contains

- Book CSS (fonts, colors, spacing)
- Puzzle engine JS (inline or linked)
- 3 puzzle blocks with full interaction
- Brief framing text at top: what this page is, how it works
- Each puzzle shows: chapter name, question, interaction, and Spiral Abstract excerpt on solve
- localStorage persistence (solved puzzles stay solved on reload)
- Progress indicator: "0/3 → 1/3 → 2/3 → 3/3"

### What it does NOT contain

- Table of contents or navigation sidebar
- Any injection into the main Relinquishment.html
- Any modification to preprocess.py or the build pipeline
- Any link FROM the main HTML TO this page

### Make target

`make puzzles` → builds `docs/downloads/puzzles.html` from a template + puzzle-data.yaml.

Or: the page is a self-contained HTML file (all CSS/JS inline) built by a small script. Since it's standalone and not generated from LaTeX, it can be simpler than the egg pipeline — a Python script that reads puzzle-data.yaml and emits an HTML file.

---

## The 3 Puzzles

### Puzzle 1: Wormholes in the Flat (easy — multiple choice)

**Question:** The Flat exists in every device that processes radio-frequency signals — phones, satellites, WiFi routers. What makes a Flat different from ordinary electronics?

**Options:**
- (a) It uses faster processors
- (b) Physics works differently in two dimensions than in three
- (c) It requires cryogenic cooling

**Answer:** (b)
**Hint (after wrong):** "Think about what happens when you confine electrons to two dimensions. What new particles become possible?"

**Spiral Abstract excerpt (on solve):**

> *The Flat is substrate, not metaphor. Two-dimensional electron gases exhibit topological order — a property that protects quantum information from local disturbance. This protection is not engineered. It is a consequence of confining electrons to two dimensions under the right conditions. The Flat is everywhere there is a 2DEG: in every high-electron-mobility transistor, in magnetospheric current sheets, in the thin quantum worlds embedded inside ordinary three-dimensional matter.*

### Puzzle 2: Genesis (medium — free text)

**Question:** Kauffman's buttons-and-threads experiment shows that connection creates structure — not gradually, but all at once. What is the name for this kind of sudden shift?

**Answer:** "phase transition"
**Accept:** "phase transition", "a phase transition" (normalize: lowercase, trim, strip articles)
**Hint:** "The chapter describes the origin of life as exactly this kind of event — not gradual, not accidental."

**Spiral Abstract excerpt (on solve):**

> *Non-abelian anyonic quasiparticles in a fractional quantum Hall system, subjected to structured electromagnetic perturbation, can undergo autocatalytic self-organization at the edge of chaos, producing an emergent topological quantum neural network. Unlike conventional quantum computer design, which requires engineered gate sequences, the proposed system requires only the establishment of critical conditions in the substrate; computational architecture emerges spontaneously from the physics.*

### Puzzle 3: The Silence Gap (harder — multiple choice)

**Question:** The chapter argues that no one has published a paper saying life cannot arise in a 2DEG. Why not?

**Options:**
- (a) The evidence against it has been suppressed
- (b) The question has never been formally asked in the relevant journals
- (c) Several papers have argued against it, but they were retracted
- (d) The physics clearly forbids it, so no paper was needed

**Answer:** (b)
**Hint:** "The chapter distinguishes between rejection and absence. Which one describes the current literature?"

**Spiral Abstract excerpt (on solve):**

> *Five scientific disciplines — solid-state physics, topological quantum computation, neural networks, complexity science, and computational universality — each contain results that, taken together, point toward the possibility of life in two-dimensional quantum substrates. No discipline contains a refutation, because no discipline contains the proposition. The intersection is empty. The silence is not rejection. It is the absence of a question that no one's job description required them to ask.*

---

## Technical Specification

### puzzle-data.yaml

```yaml
puzzles:
  - id: "flat"
    chapter_title: "Wormholes in the Flat"
    type: "multiple-choice"
    question: "The Flat exists in every device that processes radio-frequency signals — phones, satellites, WiFi routers. What makes a Flat different from ordinary electronics?"
    options:
      - key: "a"
        text: "It uses faster processors"
      - key: "b"
        text: "Physics works differently in two dimensions than in three"
      - key: "c"
        text: "It requires cryogenic cooling"
    answer_hashes: []  # Generator computes SHA-256 of "b"
    hint: "Think about what happens when you confine electrons to two dimensions. What new particles become possible?"
    abstract: |
      The Flat is substrate, not metaphor...

  - id: "genesis"
    chapter_title: "Genesis: The Edge of Chaos"
    type: "text"
    question: "Kauffman's buttons-and-threads experiment shows that connection creates structure — not gradually, but all at once. What is the name for this kind of sudden shift?"
    answer_hashes: []  # Generator computes SHA-256 of normalized "phase transition" variants
    hint: "The chapter describes the origin of life as exactly this kind of event — not gradual, not accidental."
    abstract: |
      Non-abelian anyonic quasiparticles...

  - id: "silence-gap"
    chapter_title: "The Silence Gap"
    type: "multiple-choice"
    question: "The chapter argues that no one has published a paper saying life cannot arise in a 2DEG. Why not?"
    options:
      - key: "a"
        text: "The evidence against it has been suppressed"
      - key: "b"
        text: "The question has never been formally asked in the relevant journals"
      - key: "c"
        text: "Several papers have argued against it, but they were retracted"
      - key: "d"
        text: "The physics clearly forbids it, so no paper was needed"
    answer_hashes: []  # Generator computes SHA-256 of "b"
    hint: "The chapter distinguishes between rejection and absence. Which one describes the current literature?"
    abstract: |
      Five scientific disciplines...
```

### Puzzle engine JS (~150-200 lines, inline in page)

**Functions:**
- `initPuzzles()` — on load, check localStorage, reveal solved puzzles, update count
- `checkAnswer(puzzleId)` — normalize input, SHA-256 hash via SubtleCrypto, compare
- `revealAbstract(puzzleId)` — animate reveal, set localStorage, update count
- Progress counter at top of page

**Normalization (text input):** lowercase, trim, strip leading "a "/"an "/"the ", strip trailing punctuation.

**Graceful degradation:** If SubtleCrypto unavailable, show all puzzles unlocked with note.

### Page structure

```html
<!doctype html>
<html><head>
  <meta charset="utf-8">
  <title>Relinquishment — Puzzle Preview</title>
  <!-- Book CSS (subset: fonts, colors, spacing) -->
  <style>/* inline */</style>
</head>
<body>
  <h1>Puzzle Preview</h1>
  <p class="framing">Each chapter ends with a puzzle. Solve it to reveal
  the chapter's Spiral Abstract — the meta-view that connects the chapter
  to the book's larger argument. These are samples from three chapters.</p>
  <p class="progress">Progress: <span id="count">0</span>/3</p>

  <div class="puzzle-block" id="puzzle-flat">
    <h2>Wormholes in the Flat</h2>
    <!-- puzzle interaction -->
    <!-- hidden abstract -->
  </div>

  <div class="puzzle-block" id="puzzle-genesis">
    <h2>Genesis: The Edge of Chaos</h2>
    <!-- puzzle interaction -->
    <!-- hidden abstract -->
  </div>

  <div class="puzzle-block" id="puzzle-silence-gap">
    <h2>The Silence Gap</h2>
    <!-- puzzle interaction -->
    <!-- hidden abstract -->
  </div>

  <script>/* puzzle engine inline */</script>
</body></html>
```

---

## Generator Handoff Prompt

```
You are the Generator. Read plans/0245-puzzle-engine-mvp.md in full.

Build a standalone puzzle preview page:

1. Create build/puzzle-data.yaml with the 3 puzzles from the plan.
   Compute actual SHA-256 hashes for all answers:
   - "b" for flat and silence-gap (multiple choice)
   - Normalized variants of "phase transition" for genesis (text)

2. Create build/build-puzzles.py — reads puzzle-data.yaml, emits a
   self-contained HTML file at docs/downloads/puzzles.html. All CSS
   and JS inline. Book fonts/colors. No external dependencies.

3. The page must have:
   - Deep link anchors: #puzzle-flat, #puzzle-genesis, #puzzle-silence-gap
   - Working interaction: wrong → hint, correct → abstract reveals
   - localStorage persistence (solved puzzles stay on reload)
   - Progress counter: "0/3" → "3/3"
   - Graceful degradation without SubtleCrypto
   - Brief framing text at top explaining what this is
   - No link to or from the main Relinquishment.html

4. Add "make puzzles" target to Makefile:
   puzzles:
       python3 build/build-puzzles.py
       @echo "Open docs/downloads/puzzles.html or push to website."

5. Create build/review-artifacts.yaml tracking this preview page:
   review_artifacts:
     - slug: "puzzle-preview"
       path: "docs/downloads/puzzles.html"
       make_target: "puzzles"
       purpose: "Gen reviews puzzle UX before chapter embedding"
       created_by: "Plan 0245"
       status: "active"
       cleanup_plan: "Plan 0245 cleanup phase"

6. After: make puzzles, open in browser, test all 3 puzzles end-to-end.
   Verify deep link anchors work. Verify localStorage. Verify mobile.

Commit: "Plan 0245: standalone puzzle preview page with 3 sample puzzles"
Do NOT modify preprocess.py, reader.js, or Relinquishment.html.
Report ≤5 lines.
```

---

## Manifest Tracking

The puzzle preview page is a **temporary review artifact** — it exists for Gen's evaluation and will be removed once puzzles are embedded in chapters.

**Tracked in:** `build/review-artifacts.yaml`

```yaml
review_artifacts:
  - slug: "puzzle-preview"
    path: "docs/downloads/puzzles.html"
    make_target: "puzzles"
    purpose: "Gen reviews puzzle UX before chapter embedding"
    created_by: "Plan 0245"
    status: "active"
    cleanup_plan: "Plan 0245 cleanup phase"
```

**Referenced from:** `reference-landmarks.md` (manifest of manifests).

### Cleanup Procedure (when Gen approves and puzzles move into chapters)

1. Remove `docs/downloads/puzzles.html`
2. Remove `make puzzles` target from Makefile
3. Remove `build/build-puzzles.py` (or equivalent build script)
4. Set status to `"retired"` in `build/review-artifacts.yaml` (or remove entry)
5. Update `reference-landmarks.md` if review-artifacts.yaml becomes empty
6. Commit: "Clean up puzzle preview page (superseded by chapter embedding)"

---

## After Generator

1. `make puzzles` → verify locally
2. Push to website (standard deploy)
3. When Gen responds to issue #3, share the deep link in a reply on that same thread
4. Gen plays with puzzles, gives feedback
5. If approved: future plan embeds puzzles in chapters via preprocess.py

---

## Acceptance Tests

11. `build/review-artifacts.yaml` exists and tracks the preview page

1. `docs/downloads/puzzles.html` exists and is self-contained
2. All 3 deep link anchors work (`#puzzle-flat`, etc.)
3. Wrong answer → hint appears, no reveal
4. Correct answer → abstract reveals
5. localStorage persists across reload
6. Progress counter updates
7. Page uses book fonts and colors
8. Main HTML has no link to puzzles.html
9. Mobile renders correctly
10. `make puzzles` exits clean

---

## Estimate

~2-3 hours Generator time. Single session.
