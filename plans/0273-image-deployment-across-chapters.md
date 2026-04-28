# Plan 0273 — Image Deployment Across Chapters

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** PHASE 5 DONE — Phases 1-4 ready for Generator
**Source:** Bruce request (S63): "plan additional images to fill the biggest gaps. Only do images where it really helps. Look for places we can eliminate words in place of an image."
**Annealing:** MED LOW LOW LOW + LOW + MED (S63 marker audit + chapter-scoped fix)

---

## Problem

Image distribution is heavily concentrated. Of 15 spine chapters:
- **genesis** has 11 SVGs (filmstrip + 4 illustrations)
- **the-wrong-substrate** has 3 SVGs (MS teaching imagemaps)
- **the-flat** has 2 SVGs (flat diagram + domain buttons)
- **12 chapters have zero inline illustrations**

Several existing hover SVGs (braiding, anyon, cellular automata,
phase transition) already teach the right concepts at tooltip scale
but aren't deployed as inline chapter illustrations. Two approved
SVGs (broken-bridges, guided-deduction) are designed but unbuilt.
Four grid-sequence SVGs exist as standalone files but are orphaned.

## Strategy

Promote existing assets first (hover SVGs → chapter inline).
Build approved designs second. New SVGs only where nothing
exists. Prioritized into tiers so Bruce can cherry-pick.

**Chapters deliberately NOT illustrated:**
- **The Strongest Objection** — literary register; images break tone
- **Weigh the Evidence** — too short (framing chapter)
- **Three Possibilities** — framing chapter, no visual concept
- **What to Do** — decision/ethics chapter, no visual concept

---

## Architecture

### Injection Pattern

**Chapter-scoped search** (not global `text.find`). The book is a
single-page HTML — markers that look unique in a .tex file may
appear 16 times in the full HTML. Every injection targets a
specific chapter-section by its `<h2 id="...">`.

```python
def _find_in_chapter(text, chapter_id, marker):
    """Find marker within a specific chapter-section. Returns index or -1."""
    ch_starts = [m.start() for m in re.finditer(
        r'<details class="chapter-section', text)]
    id_idx = text.find(f'id="{chapter_id}"')
    if id_idx == -1:
        print(f"  WARNING: chapter {chapter_id} not found")
        return -1
    import bisect
    ci = bisect.bisect_right(ch_starts, id_idx) - 1
    ch_start = ch_starts[ci]
    ch_end = ch_starts[ci + 1] if ci + 1 < len(ch_starts) else len(text)
    idx = text.find(marker, ch_start, ch_end)
    if idx == -1:
        print(f"  WARNING: marker '{marker[:50]}' not found in {chapter_id}")
        return -1
    return idx

# Then: find </p> after marker → insert figure after
idx = _find_in_chapter(text, chapter_id, marker)
close_p = text.find('</p>', idx)
insert_point = close_p + len('</p>')
text = text[:insert_point] + '\n' + figure_html + '\n' + text[insert_point:]
```

This is the same pattern used by hover dedup (Plan 0213), concept
symbols (Plan 0276), and puzzle injection (Plan 0274).

### Variable Naming

Chapter-promoted SVGs follow existing convention:
`ALL_CAPS_NAME` in preprocess.py (e.g., `BRAIDING_CHAPTER`,
`ANYON_CHAPTER`).

### SVG Sizing

Hover SVGs use `viewBox="0 0 380 200"` — too small for chapter
context. Each promotion must:
1. Keep the hover SVG's visual design
2. Scale viewBox to ≥400px width for chapter readability
3. Add `width="100%"` for responsive display
4. Wrap in `<figure class="inline-svg">` with figcaption

### Function Organization

New function `inject_promoted_illustrations(html)` handles all
Phases 1 and 3. Separate from genesis (different chapter targets).
Phase 2 approved SVGs added to same function. Phase 4 grid-sequence
gets its own injection call.

---

## Phase 1 — Promote Hover SVGs to Chapter Inline

**Priority: Tier 1 (high impact, low effort)**

These hover SVGs exist in `hover-definitions.yaml` and already
teach the concept. Each needs a chapter-scale version defined as
an ALL_CAPS variable in preprocess.py.

### 1A: Braiding → the-braid

| Field | Value |
|-------|-------|
| Source SVG | hover-definitions.yaml key: `braiding` |
| Variable | `BRAIDING_CHAPTER` |
| Chapter ID | `spine:the-braid` |
| Marker | `Take three strands` |
| Verified | 1 match in chapter, 1 global |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-braiding-inline` |
| Manifest | New entry SVG-042 |

**Why here:** The opening paragraph literally describes braiding
by text — "take three strands, cross the left over the middle,
cross the right over the new middle." The SVG replaces ~25 words
of spatial description with an instant visual. Reader sees the
braid before reading the physics.

**SVG spec:** Three-strand braid with crossings highlighted as
quantum gates. Scale hover's 380×200 to 420×220 viewBox.
`width="100%"`, max-width 420px centered.

### 1B: Anyon → the-braid

| Field | Value |
|-------|-------|
| Source SVG | hover-definitions.yaml key: `anyon` |
| Variable | `ANYON_CHAPTER` |
| Chapter ID | `spine:the-braid` |
| Marker | `The particles in question are non-abelian` |
| Verified | 1 match in chapter, 1 global |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-anyon-inline` |
| Manifest | New entry SVG-043 |

**Why here:** Anyons are the exotic quasiparticles that make
braiding computational. The hover SVG shows worldlines braiding
in 2+1D spacetime — exactly what the text describes but can't
convey in words alone.

**Old marker `Non-abelian anyons`:** 0 matches in the-braid body
(only in appendix predictions). Fixed to the introductory sentence.

**SVG spec:** Two anyons with worldlines braiding in 2+1D.
Scale hover's viewBox to 420×230. Centered.

### 1C: Cellular Automata (Rule 110) → growing-a-mind

| Field | Value |
|-------|-------|
| Source SVG | hover-definitions.yaml key: `cellular automata` |
| Variable | `CELLULAR_AUTOMATA_CHAPTER` |
| Chapter ID | `spine:growing-a-mind` |
| Marker | `Patterns on seashells run the` |
| Verified | 1 match in chapter, 1 global |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-rule110-inline` |
| Manifest | New entry SVG-044 |

**Why here:** The chapter has an explicit `%TODO: ILLUSTRATION
CANDIDATE` at line 25. The text discusses how natural patterns
match computational ones. Rule 110 triangular pattern is the
canonical visual. Addresses the existing TODO.

**Old marker `Patterns on seashells run the same algorithms`:**
0 matches — HTML line break after "the". Truncated to pre-break.

**SVG spec:** Rule 110 automaton — Turing-complete triangular
pattern. Scale to 420×240 viewBox. Centered.

### 1D: Phase Transition → growing-a-mind

| Field | Value |
|-------|-------|
| Source SVG | hover-definitions.yaml key: `phase transition` |
| Variable | `PHASE_TRANSITION_CHAPTER` |
| Chapter ID | `spine:growing-a-mind` |
| Marker | `described in the previous chapter` |
| Verified | 1 match in chapter, 1 global |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-phase-transition-inline` |
| Manifest | New entry SVG-045 |

**Why here:** The text references "the phase transition described
in the previous chapter" — Kauffman's threshold. The S-curve
diagram makes the concept immediate. Reinforces the genesis
chapter's filmstrip with a different visual language.

**Old marker `buttons and threads model`:** 0 matches — "buttons"
is wrapped in `<span class="hover-term">`, breaking plain-text
search. New marker targets the same sentence, after the span.

**SVG spec:** S-curve with control parameter vs order parameter,
red critical point marked. Scale to 400×220. Centered.

---

## Phase 2 — Build Approved SVGs

**Priority: Tier 2 (high impact, medium effort)**

These SVGs are designed in the manifest (description, targets,
display specs) but have `source: gallery` — no SVG exists yet.
Generator must build the SVG from the manifest description.

### 2A: Broken Bridges (SVG-029) → the-silence-gap

| Field | Value |
|-------|-------|
| Manifest entry | SVG-029 (status: approved) |
| Variable | `BROKEN_BRIDGES_SVG` |
| Chapter ID | `spine:silence-gap` |
| Marker | `There is no journal called` |
| Verified | 1 match in chapter, 1 global |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-broken-bridges` |
| Manifest update | Change status approved → live, source gallery → preprocess.py |

**Why here:** The chapter argues that nobody's job description
requires them to bridge five disciplines. The SVG IS the argument:
five tall silos standing apart, broken dashed bridges between each
pair, × at each break. Caption: "No journal. No career. No
funding. No one's job."

**SVG spec (from manifest):** Five tall silos (domains) standing
apart. Broken dashed bridges between each pair with × at break.
viewBox 500×280. Colors: silos in domain-badge colors from
domain-buttons (match the existing visual language). Bridges in
dashed #999 with red × at midpoint.

### 2B: Guided Deduction Two Paths (SVG-030) → why-relinquish

| Field | Value |
|-------|-------|
| Manifest entry | SVG-030 (status: approved) |
| Variable | `GUIDED_DEDUCTION_SVG` |
| Chapter ID | `spine:why-relinquish` |
| Marker | `The solution was` |
| Verified | 1 match in chapter, 3 global (safe when scoped) |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-guided-deduction` |
| Manifest update | Change status approved → live, source gallery → preprocess.py |

**Why here:** The text explains why guided deduction was the only
legal option. The SVG shows it as a fork: top path (red) = direct
disclosure → prosecution; bottom path (blue) = guided deduction →
five published domains → student deduces → clean record. Visual
makes the constraint viscerally clear.

**SVG spec (from manifest):** Two paths from "Classified knowledge"
node. Top: red arrow → "Direct disclosure" → "CRIME" → skull/gavel.
Bottom: blue arrow → "Guided deduction" → 5 domain nodes → "Student
deduces" → green checkmark. viewBox 520×240. Decision-tree layout,
left to right.

---

## Phase 3 — New SVG: CA vs Seashell

**Priority: Tier 3 (medium impact, medium effort)**

### 3A: CA-vs-Seashell Comparison → growing-a-mind

| Field | Value |
|-------|-------|
| Variable | `CA_SEASHELL_COMPARISON` |
| Chapter ID | `spine:growing-a-mind` |
| Marker | `Three results, one conclusion` |
| Verified | 1 match in chapter, 1 global |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-ca-seashell` |
| Manifest | New entry SVG-046 |

**Adjacency note:** 1C (Rule 110) and 3A (CA-vs-seashell) both
target growing-a-mind near the seashell paragraph. 1C goes
BEFORE the seashell sentence (after `Patterns on seashells run
the`). 3A goes AFTER `Three results, one conclusion` — roughly
15 lines later. Placement order matters: inject 3A first (later
in file), then 1C, so 3A's marker isn't shifted by 1C's
insertion. Or, use `_find_in_chapter()` offsets and adjust.

**Why here:** The %TODO at line 25 specifically requests this:
"an image showing a cellular automaton pattern alongside an
identical pattern on a natural sea shell." The visual proves
computation emerges in nature without a programmer.

**SVG spec:** Split panel. Left: stylized Rule 30 triangular
pattern (black/white cells). Right: stylized cone shell with
same triangular pigment pattern. Dividing line labeled "Same
algorithm." viewBox 480×240. No photographs (licensing); use
geometric stylization for the shell shape.

**Note:** The %TODO mentions licensing concerns about Wolfram's
NKS images. This SVG must be original artwork, not a copy.

---

## Phase 4 — Grid-Sequence Assembly → the-flat

**Priority: Tier 3 (medium impact, assembly effort)**

### 4A: Four-Panel Zoom-Out Sequence

| Field | Value |
|-------|-------|
| Source files | `build/images/grid-sequence-{1,2,3,4}-the-flat.svg` |
| Variable | `GRID_SEQUENCE_ASSEMBLY` |
| Chapter ID | `spine:the-flat` |
| Marker | `All your electricity are belong to us` |
| Verified | 1 match in chapter, 2 global (safe when scoped) |
| Insert | After `</p>` containing marker |
| Figure ID | `fig-grid-sequence` |
| Manifest | Update SVG-035 through SVG-038: status deferred → live |

**Why here:** The text just explained how every 2DEG in every chip
connects through classical infrastructure to form a planetary
network. The four-panel zoom shows this: regional grid → global
grid → magnetosphere → the Flat. The visual payoff of the
chapter's central claim.

**SVG spec:** 2×2 grid assembly. Each panel retains its existing
SVG content but is embedded in a composite:

```
┌─────────────┬─────────────┐
│  Regional   │   Global    │
│  (panel 1)  │  (panel 2)  │
├─────────────┼─────────────┤
│Magnetosphere│  The Flat   │
│  (panel 3)  │  (panel 4)  │
└─────────────┴─────────────┘
```

Composite viewBox: `0 0 820 620` (two 400×300 panels + 10px gaps).
Panels numbered 1-4 with small labels. Arrows between panels
showing zoom direction (1→2→3→4). The existing SVGs are dark
background (fill="#1a2a3a") so the composite should maintain
that. `width="100%"`, max-width 820px, centered.

**Manifest changes:** Update all four from `status: deferred` and
`notes: "Orphaned..."` to `status: live`, `source: preprocess.py`,
`chapter: the-flat`, `figure_id: fig-grid-sequence`,
`sequence_group: grid-zoom`, `sequence_order: 1-4`.

---

## Implementation Steps (Per Phase)

### Phase 1 Steps

1. **Extract hover SVGs.** For each of braiding, anyon,
   cellular automata, phase transition: extract the `<svg>` from
   hover-definitions.yaml's `html:` field.

2. **Create chapter-scale variables.** In preprocess.py, define
   `BRAIDING_CHAPTER`, `ANYON_CHAPTER`,
   `CELLULAR_AUTOMATA_CHAPTER`, `PHASE_TRANSITION_CHAPTER`.
   Each wraps the extracted SVG in a `<figure>` with:
   - `class="inline-svg"`
   - `style="text-align:center;margin:1.5em auto;"`
   - `<figcaption>` with brief label
   - Scaled viewBox (see SVG spec per entry)

3. **Add `_find_in_chapter()` helper and
   `inject_promoted_illustrations(html)`.** New functions in
   preprocess.py. For each entry: `_find_in_chapter(text,
   chapter_id, marker)` → find `</p>` after → insert figure
   after. Wire into pipeline after `inject_ms_diagrams`.
   Two growing-a-mind injections: insert in reverse file order
   (1D before 1C) to avoid offset shift.

4. **Add manifest entries.** SVG-042 through SVG-045 in
   `gallery-manifest.yaml`.

5. **Build + test.** `make dev`. Verify each illustration appears
   in correct chapter at correct location. Regenerate gallery.

### Phase 2 Steps

1. **Build SVG-029.** Create `BROKEN_BRIDGES_SVG` variable.
   Five silos, broken dashed bridges, × at breaks. Test hover
   tooltips not needed (static illustration).

2. **Build SVG-030.** Create `GUIDED_DEDUCTION_SVG` variable.
   Two-path decision tree. Static illustration.

3. **Add both to `inject_promoted_illustrations`.** Use
   `_find_in_chapter()` with chapter-scoped markers from tables.

4. **Update manifest.** SVG-029 and SVG-030: status → live,
   source → preprocess.py, add chapter/figure_id/marker fields.

5. **Build + test.**

### Phase 3 Steps

1. **Design CA-vs-seashell SVG.** Split panel, geometric
   stylization only (no photographic content). Original artwork.

2. **Create `CA_SEASHELL_COMPARISON` variable.**

3. **Add to injection function.** Use `_find_in_chapter(text,
   "spine:growing-a-mind", "Three results, one conclusion")`.
   Adjacency warning: 1C already injected nearby — check offset.

4. **Add SVG-046 to manifest.**

5. **Build + test. Remove %TODO from growing-a-mind.tex** once
   the illustration is live.

### Phase 4 Steps

1. **Read all four grid-sequence SVGs** from `build/images/`.

2. **Create `GRID_SEQUENCE_ASSEMBLY` variable.** Composite SVG
   embedding all four panels in 2×2 layout with gaps and arrows.

3. **Add injection.** Extend `inject_promoted_illustrations`.
   Use `_find_in_chapter(text, "spine:the-flat",
   "All your electricity are belong to us")`.

4. **Update manifest entries** SVG-035 through SVG-038.

5. **Build + test.**

---

## Manifest Changes Summary

### New Entries

```yaml
- id: SVG-042
  name: braiding-chapter
  status: live
  source: preprocess.py
  category: Physics Concepts
  chapter: the-braid
  figure_id: fig-braiding-inline
  marker: "Take three strands. Cross the left over"
  description: "Three-strand braid with quantum gate crossings — chapter inline version."

- id: SVG-043
  name: anyon-chapter
  status: live
  source: preprocess.py
  category: Physics Concepts
  chapter: the-braid
  figure_id: fig-anyon-inline
  marker: "The particles in question are non-abelian"
  description: "Two anyons with worldlines braiding in 2+1D — chapter inline version."

- id: SVG-044
  name: rule110-chapter
  status: live
  source: preprocess.py
  category: Physics Concepts
  chapter: growing-a-mind
  figure_id: fig-rule110-inline
  marker: "Patterns on seashells run the"
  description: "Rule 110 cellular automaton — chapter inline version."

- id: SVG-045
  name: phase-transition-chapter
  status: live
  source: preprocess.py
  category: Physics Concepts
  chapter: growing-a-mind
  figure_id: fig-phase-transition-inline
  marker: "described in the previous chapter"
  description: "S-curve phase transition diagram — chapter inline version."

- id: SVG-046
  name: ca-seashell-comparison
  status: live
  source: preprocess.py
  category: Genesis Illustrations
  chapter: growing-a-mind
  figure_id: fig-ca-seashell
  marker: "Three results, one conclusion"
  description: "Split panel: Rule 30 pattern alongside stylized cone shell with matching pigment pattern."
```

### Updated Entries

SVG-029: status approved → live, source gallery → preprocess.py,
add chapter: the-silence-gap, figure_id: fig-broken-bridges,
marker: "There is no journal called"

SVG-030: status approved → live, source gallery → preprocess.py,
add chapter: why-relinquish, figure_id: fig-guided-deduction,
marker: "The solution was"

SVG-035 through SVG-038: status deferred → live,
source → preprocess.py, chapter: the-flat,
figure_id: fig-grid-sequence, add sequence_group: grid-zoom

---

## What Does NOT Change

- hover-definitions.yaml — hover SVGs stay as-is (chapter versions
  are copies, not moves)
- reader.js — Phase 5 added step-through handler; no further changes
  needed for Phases 1-4
- Existing inject_* functions — unchanged
- Genesis illustrations — unchanged (Phase 5 refactored filmstrip
  from 6 stacked SVGs to 1 step-through SVG)
- MS teaching diagrams — unchanged
- Chapter prose — no text changes (images supplement, not replace)
- Exception: remove %TODO comment from growing-a-mind.tex once
  Phase 3 is live

---

## Priority Guidance

Bruce: "Maybe we won't implement."

| Phase | Tier | Impact | Effort | Do it? |
|-------|------|--------|--------|--------|
| 1A braiding | 1 | HIGH — replaces 25 words of spatial text | LOW — hover SVG exists | YES |
| 1C cellular automata | 1 | HIGH — addresses explicit %TODO | LOW — hover SVG exists | YES |
| 2A broken-bridges | 2 | HIGH — IS the chapter's argument | MED — build from spec | YES |
| 2B guided-deduction | 2 | HIGH — explains tradecraft visually | MED — build from spec | YES |
| 1B anyon | 2 | MED — deepens the-braid | LOW — hover SVG exists | LIKELY |
| 1D phase transition | 2 | MED — reinforces growing-a-mind | LOW — hover SVG exists | LIKELY |
| 4A grid-sequence | 3 | MED — payoff visual for the-flat | MED — assembly work | MAYBE |
| 3A ca-seashell | 3 | MED — original artwork needed | HIGH — new SVG design | MAYBE |
| 5 filmstrip step-through | 1 | HIGH — 6x scroll → 1x, puzzle link | MED — refactor existing code | **DONE** (S63, f091b41) |

**Recommended execution order:** Phase 1 (four promotions) →
Phase 2A (broken-bridges) → Phase 2B (guided-deduction) →
Phase 4 (grid-sequence) → Phase 3 (ca-seashell, if appetite
remains). Phase 5 complete.

---

## Acceptance Criteria

### Phase 1
- [ ] `_find_in_chapter()` helper in preprocess.py
- [ ] 4 new chapter-scale SVG variables in preprocess.py
- [ ] `inject_promoted_illustrations()` function using chapter-scoped lookups
- [ ] braiding visible in the-braid after "Take three strands"
- [ ] anyon visible in the-braid after "The particles in question are non-abelian"
- [ ] Rule 110 visible in growing-a-mind after "Patterns on seashells run the"
- [ ] Phase transition visible in growing-a-mind after "described in the previous chapter"
- [ ] All 4 centered, responsive, `<figcaption>` present
- [ ] SVG-042 through SVG-045 in manifest (with corrected markers)
- [ ] Gallery regenerated with new entries
- [ ] `make dev` clean

### Phase 2
- [ ] SVG-029 broken-bridges built and deployed in the-silence-gap
- [ ] SVG-030 guided-deduction built and deployed in why-relinquish
- [ ] Manifest entries updated (status: live)
- [ ] Visual matches manifest description
- [ ] `make dev` clean

### Phase 3
- [ ] CA-vs-seashell SVG is original artwork (no Wolfram copies)
- [ ] Split-panel design clearly shows pattern match
- [ ] %TODO removed from growing-a-mind.tex
- [ ] `make dev` clean

### Phase 4
- [ ] 2×2 composite assembles all four grid-sequence panels
- [ ] Zoom arrows visible between panels
- [ ] Dark background maintained
- [ ] SVG-035-038 manifest entries updated
- [ ] `make dev` clean

---

## Generator Handoff — Phase 1

```
You are the Generator.

Read Plan 0273 at ~/software/relinquishment/plans/0273-image-deployment-across-chapters.md
Read the Architecture section for _find_in_chapter() pattern.

Execute Phase 1 (Promote 4 hover SVGs to chapter inline):

(1) From hover-definitions.yaml, extract the <svg> content for keys:
braiding, anyon, cellular automata (or cellular automaton), phase transition.

(2) In preprocess.py, create 4 ALL_CAPS variables: BRAIDING_CHAPTER,
ANYON_CHAPTER, CELLULAR_AUTOMATA_CHAPTER, PHASE_TRANSITION_CHAPTER.
Each wraps its SVG in <figure class="inline-svg"
style="text-align:center;margin:1.5em auto;"> with a <figcaption>.
Scale viewBox width to ≥400px. Add width="100%".

(3) Add _find_in_chapter(text, chapter_id, marker) helper (see
Architecture section). Add inject_promoted_illustrations(html)
using chapter-scoped lookups — NOT global text.find(). Each entry
has a Chapter ID and verified Marker in its table. The two
growing-a-mind injections (1C, 1D) must be inserted in
reverse-file-order (1D first, then 1C) to avoid offset shift, OR
recalculate offsets after each insertion. Wire into pipeline after
inject_ms_diagrams.

(4) Add SVG-042 through SVG-045 to gallery-manifest.yaml (entries
in plan's Manifest Changes section — note markers are updated).

(5) Run make dev. Run python3 build/generate-gallery.py.

(6) Commit and push. Report: which chapters got illustrations,
byte delta, any markers not found.
```

## Generator Handoff — Phase 2

```
You are the Generator.

Read Plan 0273 at ~/software/relinquishment/plans/0273-image-deployment-across-chapters.md
Read the Architecture section for _find_in_chapter() pattern.

Execute Phase 2 (Build 2 approved SVGs):

(1) Build BROKEN_BRIDGES_SVG in preprocess.py: 5 tall silos
(domain colors from domain-buttons), broken dashed bridges between
each pair with red × at break. viewBox 500×280. Caption: "No
journal. No career. No funding. No one's job."

(2) Build GUIDED_DEDUCTION_SVG: two-path decision tree. Top (red):
Classified → Direct disclosure → CRIME → prosecution. Bottom
(blue): Classified → Guided deduction → 5 domains → Student
deduces → clean record. viewBox 520×240.

(3) Add both to inject_promoted_illustrations using
_find_in_chapter() — NOT global text.find(). Chapter-scoped
markers from the plan tables:
  2A: chapter_id="spine:silence-gap", marker="There is no journal called"
  2B: chapter_id="spine:why-relinquish", marker="The solution was"
After </p> pattern. If Phase 1 already created the function,
add entries to it.

(4) Update SVG-029 and SVG-030 in manifest: status→live,
source→preprocess.py, add chapter/figure_id/marker (use updated
markers from plan).

(5) make dev + generate gallery. Commit and push.
```

---

## Phase 5 — Filmstrip Step-Through + Puzzle Link

**Priority: Tier 1 (high impact, medium effort)**
**Source:** Bruce (S63): "We have 6 Kauffman filmstrip images. We have
a PUZZLE that does the same thing only better. Improve user experience
and learning."

### Problem

The Genesis chapter's Kauffman filmstrip is 6 stacked SVGs
(preprocess.py lines 2464-2673, SVG-008 through SVG-013). Each shows
one stage of the buttons-and-threads process: scatter → tie → clusters
→ net → almost → snap. Six panels × ~2KB = ~12KB, massive vertical
scroll on phone, and the reader passively observes.

Meanwhile, puzzle `pz-sim-t3-001` (build-puzzles.py, `sim_type:
threads`) is an interactive version of the SAME process. The reader
clicks "Pick Two" repeatedly, doesn't know when the phase transition
will hit, and gets the teaching moment: "You didn't design this
network. The structure organized itself." The puzzle teaches; the
filmstrip only illustrates.

### What Changes

**5A: Step-through replaces stack.** Replace 6 stacked SVGs with ONE
SVG containing 6 `<g>` layers (one per stage). Only one layer visible
at a time. Prev/next controls advance through stages. Caption and
counter ("0/30" → "24/30") change per step.

All 6 stages already share the same 30 button x-positions (`bx[]`
array, line 2469). Each stage differs only in: which threads exist,
and which buttons are lifted (y-position). The Python code already
computes these per stage — emit as layers, not separate SVGs.

**Implementation:**

```python
def _stage_group(stage_id, threads, lifted, label, counter, caption):
    """One <g> layer: threads + buttons at stage-specific positions."""
    parts = []
    for a, b in threads:
        ya = lifted.get(a, floor_y[a])
        yb = lifted.get(b, floor_y[b])
        parts.append(_thread(bx[a], ya, bx[b], yb))
    for i in range(30):
        y = lifted.get(i, floor_y[i])
        parts.append(_button(bx[i], y))
    parts.append(_label(label))
    parts.append(_counter(counter))
    parts.append(_caption(caption))
    vis = ' style="display:none"' if stage_id > 0 else ''
    return f'<g class="step-stage" data-stage="{stage_id}"{vis}>\n' + '\n'.join(parts) + '\n</g>'
```

Single SVG wraps all 6 groups + shared defs + floor + controls.
Uses `data-stepthrough` attribute so multiple instances coexist
on the single-page book:

```html
<svg viewBox="0 0 500 310" data-stepthrough="kauffman">
  <defs>...</defs>
  <line ... /> <!-- floor (always visible) -->
  <g class="step-stage" data-stage="0">...</g>  <!-- scatter -->
  <g class="step-stage" data-stage="1" style="display:none">...</g>
  ...
  <g class="step-stage" data-stage="5" style="display:none">...</g>
  <!-- step controls -->
  <text class="step-prev" x="20" y="295" ...>◀</text>
  <text class="step-next" x="480" y="295" ...>▶</text>
</svg>
```

**JS handler (reader.js, ~20 lines) — discovers all instances:**

```javascript
document.querySelectorAll('svg[data-stepthrough]').forEach(function(svg) {
  var stages = svg.querySelectorAll('.step-stage');
  var cur = 0;
  function show(n) {
    stages.forEach(function(g, i) { g.style.display = i === n ? '' : 'none'; });
    cur = n;
  }
  var prev = svg.querySelector('.step-prev');
  var next = svg.querySelector('.step-next');
  if (prev) prev.addEventListener('click', function() { if (cur > 0) show(cur - 1); });
  if (next) next.addEventListener('click', function() { if (cur < stages.length - 1) show(cur + 1); });
  if (prev) prev.style.cursor = 'pointer';
  if (next) next.style.cursor = 'pointer';
});
```

No global IDs. Any SVG with `data-stepthrough` gets step controls
automatically. Works for filmstrip, grid-sequence, or any future
step-through we add.

**5B: Deep link to puzzle.** Below the step-through, add a link:

```html
<p style="font-size:0.9em;text-align:center;margin-top:0.5em;">
  <a href="#pz-sim-t3-001" class="puzzle-link">Try it yourself →</a>
</p>
```

If the puzzle is on puzzles.html (not inline), use the full URL with
deep link. If the puzzle is embedded in the chapter (future Phase 5C),
use an in-page anchor.

### What Does NOT Change

- The puzzle itself — untouched
- The domain buttons diagram (SVG after filmstrip) — untouched
- The 30 button positions (`bx[]`) — reused exactly
- The stage data (thread lists, lifted positions) — reused exactly
- The marker and insertion point — same `connected web.</p>`

### Sizing

| Metric | Before (6 stacked) | After (step-through) |
|--------|--------------------|--------------------|
| Vertical space | ~6× panel height | 1× panel height |
| Bytes (est.) | ~12KB | ~5KB |
| Phone scrolling | Massive | Minimal |
| Reader engagement | Passive observation | Controlled stepping + puzzle link |

### Acceptance Criteria — DONE (S63, f091b41)

- [x] Single SVG with 6 `<g>` layers replaces 6 stacked SVGs
- [x] Prev/next controls work (click and touch)
- [x] Caption, label, and counter change per stage
- [x] Stage 0 visible by default; stage 5 shows red snap thread
- [x] "Try it yourself →" links to puzzle `pz-sim-t3-001`
- [x] `prefers-reduced-motion`: no animation (step-through is
      click-driven, so already compliant)
- [x] Dark mode: controls visible
- [x] `make dev` clean
- [x] Phone test: fits in viewport, controls tappable
- [ ] Gallery manifest: update SVG-008 through SVG-013 notes

### Future: Phase 5C (not in scope)

Embed the threads puzzle inline in the Genesis chapter, replacing the
step-through entirely. Requires extracting `initThreads()` and its
dependencies from build-puzzles.py into reader.js or a shared module.
Highest engagement, highest plumbing effort. Gate: puzzle engagement
data shows readers who reach the puzzle have meaningfully better
retention of T3 (life in the Flat).

### Generator Handoff — Phase 5

```
You are the Generator.

Read Plan 0273 at ~/software/relinquishment/plans/0273-image-deployment-across-chapters.md
— section "Phase 5 — Filmstrip Step-Through + Puzzle Link".

Execute Phase 5A+5B. Refactor inject_button_sequence() in preprocess.py:
emit 6 <g> layers in one SVG instead of 6 separate SVGs. Reuse existing
bx[], thread lists, and lifted positions — same data, different structure.
Add ~15-line step handler in reader.js. Add puzzle deep link below.
Run make dev. Commit, push. Report: byte delta, panel count confirmed.
```

---

*Plan 0273 written by Argus (Auditor), S63. Annealed MED LOW LOW LOW
+ LOW + MED (marker audit + chapter-scoped fix). Phase 5 DONE
(f091b41). Phases 1-4 ready for Generator. All 8 markers verified
against built HTML with chapter-scoped injection pattern.*
