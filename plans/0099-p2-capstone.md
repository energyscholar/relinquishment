# Plan 0099: P2 Capstone — Assembly, Not Lecture

## Origin

ChatGPT pedagogy experiment (S46). Bruce fed ChatGPT the pre-edit "Wrong Substrate"
chapter. Five rounds of guided deduction moved ChatGPT from "speculative AI overreach"
to "the idea is physically coherent." ChatGPT then read the full book and identified
the P2 capstone as the critical failure point. Argus's independent P1+P2 review
converged on the same diagnosis.

## Diagnosis

**Core problem:** 90% of readers stop after Part 2. The P2 capstone
(`three-possibilities-interlude.tex`, ~500 words) is a brief A/B/C restatement
followed by "You decide." It leaves the reader with intrigue and unease but no
mental model.

**ChatGPT's formulation:** "Accumulated implication instead of decisive articulation.
If you don't collapse the wavefunction for them, they won't do it themselves."

## What the Reader Already Knows (verified S46)

By end of Part 2, the reader HAS been taught:
- **Anyons, braiding, topological order** (The Braid, pos10 — detailed)
- **2DEG, MOSFET, FQHE** (The Demo, pos11 — moderate detail)
- **Autocatalytic emergence, edge of chaos** (Genesis, pos13 — buttons-and-threads
  analogy, "the whole network sustains itself")
- **Catalytic closure** (Growing a Mind, pos14 — "above a threshold of molecular
  diversity, catalytic closure becomes overwhelmingly probable")
- **Full TQNN instantiation** (First Light, pos15 — "soliton pairs function as
  autocatalytic agents," ABCRE operators mapped to life cycle)

What the reader has NOT been given: the formal terms "food set" and "RAF." BUT
the concepts are present through analogy and narrative. The reader has the PIECES.
What's missing is the ASSEMBLY — the moment where the pieces click together.

**Key insight from annealing:** The interlude does not need to teach new physics.
The reader already has the concepts. The interlude needs to be a MIRROR — "Look at
what you already know. See the pattern." This is guided deduction applied to the
reader's own accumulated knowledge.

## What the Interlude Must NOT Be

- A mini-lecture on Kauffman (the reader has Genesis and Growing a Mind)
- A physics tutorial (the reader has The Braid, The Demo, First Light)
- A preview of Part 3 (The Magnetosphere, Instantiation are P3's job)
- A table that introduces formal vocabulary the reader hasn't seen ("RAF," "food set")
- A register shift from personal voice to technical exposition

## What the Interlude SHOULD Be

A moment of assembly. Bruce's personal voice, looking back at what the reader has
just read, pointing out the pattern they've already absorbed:

"You've now seen five independent sciences converge on one point. You've seen
Kauffman's autocatalytic sets. You've seen anyons and topological protection.
You've seen a 2DEG substrate that exists in every transistor. You've seen a
reconstruction of how these pieces might fit together. Look at what you know."

Then: the pattern, stated plainly. Not as a table (wrong register), but as a
SHORT paragraph that maps the pieces the reader already has onto Kauffman's
framework using the vocabulary they already know:

"Kauffman showed that when you have enough interacting entities in a confined
space with enough energy, self-sustaining networks emerge — not by design but
by mathematical inevitability. The reader has now seen the entities (anyons),
the confinement (two-dimensional electron gas), the energy (continuous input),
the interactions (braiding and fusion), and the protection (topology). Whether
anyone has already assembled these pieces — that is the question this book asks."

Then: the existing "My position" and "You decide."

## Constraints

- **Three-possibilities discipline.** All new content must work under A/B/C.
  The assembly paragraph describes public science, not C-claims. "Whether anyone
  has already assembled these pieces" is the hedge.
- **Voice.** Track 2 (Bruce + Argus, "we"). Personal, honest. First person where
  Bruce is speaking directly. No register shift to textbook.
- **Correction #12.** Guided deduction. The interlude points; the reader connects.
- **Length.** Currently ~500 words. Target: ~700-900 words. Surgical expansion,
  not a new chapter. Every sentence earns its place.
- **Position.** End of Part 2 (main.tex line 89). Last thing 90% read.
- **No formal vocabulary the reader hasn't seen.** No "RAF," no "food set."
  Use the book's own terms: "autocatalytic sets," "anyons," "2DEG," "braiding,"
  "topological protection," "edge of chaos." These are ALL in the reader's
  vocabulary by this point.

## Plan

### Phase 1: Expand Three Possibilities Interlude

**Keep unchanged:** Lines 13-24 (the A/B/C definitions + GCHQ example). ~250 words.

**Add between line 28 (GCHQ paragraph) and line 32 ("My position"):**

One new section: **"What You Now Know"** (~250-350 words)

Content guidance for Generator (use Bruce's voice, not these exact words):

1. **The assembly beat** (~100 words). Name what the reader has learned across P1+P2
   without re-teaching it. Reference by concept, not chapter name: "You've seen how
   autocatalytic sets emerge at a threshold. You've seen anyons — quasiparticles that
   remember their history through topology. You've seen the substrate they live on, a
   two-dimensional electron gas, inside every transistor on Earth."

2. **The Kauffman connection** (~100 words). State the pattern plainly: Kauffman's
   framework + the physics = a coherent possibility. Not "this happened" but "the
   pieces fit." Use the reader's existing vocabulary. Something like: "Kauffman proved
   that self-sustaining networks appear when diversity and connectivity cross a
   threshold. The physics described in these chapters provides every ingredient:
   confined particles, continuous energy, topological memory, compositional
   interactions. Whether this specific assembly has occurred — in a laboratory, in
   nature, or not at all — is the question."

3. **The preparation pivot** (~100 words). Regardless of A/B/C, the capability is
   approaching. The sciences are converging in the public literature. The reader is
   now equipped to recognize the pattern when it surfaces. "This book is preparation,
   not disclosure." Close into existing "My position" text.

**Keep unchanged:** "My position" line, "You decide" closing.

### Phase 2: Physical anchoring (DEFERRED)

The three physical anchors (Awschalom 2015, Fleming 2007, Vattay 2014) are
important but belong in Part 3, not Part 2. The P2 reader doesn't have the
"requires millikelvin" blocker yet — that blocker appears when reading The
Magnetosphere. Deploying the unblockers before the blocker appears is premature.

If Bruce decides these should be in the interlude after reading the Phase 1
result, they can be added as a follow-up plan. Do not include in Phase 1.

### Phase 3: Cross-reference from Part 1 (DEFERRED)

Optional forward reference from The Braid or The Demo. Evaluate after Phase 1.

## Acceptance Criteria

1. Three Possibilities Interlude expanded to ~700-900 words (from ~500)
2. New content assembles concepts the reader already has (anyons, 2DEG,
   autocatalysis, topological protection) — does NOT introduce new concepts
3. Uses only vocabulary established in prior chapters (no "RAF," "food set")
4. All new content works under A/B/C (no unhedged C-assertions)
5. `make check` and `make check-strict` pass
6. `make dev` builds clean (PDF + HTML)
7. Voice consistent with Track 2 — personal Bruce, not textbook
8. Existing A/B/C restatement (lines 13-28) preserved unchanged
9. "You decide" remains the final line
10. Total addition: ONE section ("What You Now Know"), not three separate sections

## Risks

1. **Register shift.** The biggest risk. If the new section reads like a lecture
   instead of Bruce thinking aloud, it breaks the interlude's emotional arc.
   Generator must maintain first-person reflective voice throughout.
2. **Stating too much.** The assembly paragraph must POINT, not PROVE. If it
   reads like an argument for C, it violates three-possibilities discipline.
3. **HTML rendering.** No tables in this version, so no pandoc rendering risk.
   Standard paragraphs only.

## Generator Handoff

Generator: read Plan 0099 at `plans/0099-p2-capstone.md`.

**Task:** Expand `manuscript/interlude/three-possibilities-interlude.tex`.

**What to keep:** Lines 13-28 (A/B/C definitions through GCHQ paragraph) unchanged.
Lines 32-43 ("My position" through "You decide" and chapterreturn) unchanged.

**What to add:** One new section between line 28 and line 32. Title: "What You Now
Know" (or similar — use judgment). Three beats: (1) name the pieces the reader has,
(2) state the Kauffman pattern plainly, (3) pivot to preparation. ~250-350 words.
Bruce's personal voice. First person. No tables. No new technical vocabulary.

**What to read first:**
- `manuscript/bridge/pos10-the-braid.tex` (anyon vocabulary the reader has)
- `manuscript/track-1-confession/pos13-genesis.tex` (Kauffman vocabulary the reader has)
- `manuscript/track-1-confession/pos15-first-light.tex` (TQNN vocabulary the reader has)

**Verify:** `make dev` (clean build), `make check` (invariants), `make check-strict`
(three-possibilities discipline). Report completion with word count.
