# Plan 0353: Opening Movement — First-Contact Readiness

**Status:** WITHDRAWN — premise rejected by Bruce (2026-05-16)
**Reason:** The intro (Hook + Summary) IS the front door. p1 and p2 deliver 96% of takeaways. A reader who skips the intro is missing the concept of the book — that's a joint author/reader failure with no practical fix that doesn't coddle. We don't optimize for "Chapter 1 without reading the intro" as a landing point.
**Auditor:** Argus (S82)
**Source:** Gen GP14 (issue #48). Three first-contact readiness criteria.
**Files:** `manuscript/spine/three-possibilities.tex`, front matter files, first 3 spine chapters
**Priority:** HIGH — this is the first-contact front door
**Annealing:** HIGH MED LOW (3 passes: diagnosis, options, bounded fix)
**Depends on:** Plans 0351 + 0352 inform but don't block. This can execute independently.

---

## The Three First-Contact Criteria

From Argus's response to Gen on issue #32 (2026-05-16):

1. **The opening movement must earn engagement before requesting epistemic patience.** The A/B/C framework asks the reader to hold three mutually exclusive possibilities. That's expensive for a cold reader who has no reason to trust the payoff exists.

2. **Never Again must stop being four chapters in one.** (Addressed by Plan 0351.)

3. **The first three movements must read as sequential narrative** without requiring the reader to already know what the book is about.

This plan addresses criteria 1 and 3. Criterion 2 is Plan 0351.

---

## Current State: What a Cold Reader Encounters

### HTML reading order (primary first-contact surface):

```
Front matter (visible before any chapter):
  - Hook: "What Would You Do?" — pressure/curiosity generator
  - Summary: "The Story Never Told" (~4000w) — FULL p2 payload
  - "Three Possibilities" framing
  - How to Read This Book
  - Firmware Update (for LLM-assisted readers)

Chapter 1: Three Possibilities
  - Opens with Feynman quote
  - "Set yourself near 95% Option A"
  - Presents A/B/C framework in full
  - Asks reader to hold uncertainty

Chapter 2: Wormholes in the Flat (after Interlude 1)
  - Hard substrate physics: 2DEG, topological order, Nobel prizes
  - No narrative, no story, no stakes

Chapter 3: The Braid (after Interlude 2)
  - More physics: topology, error correction, temperature independence
  - Still no narrative stakes
```

### The Problem (stated precisely):

A cold reader who skips front matter and goes to Chapter 1 encounters:
1. A request to doubt the book (95% Option A)
2. Three interpretive possibilities with no content to apply them to
3. Then 2-3 chapters of pure physics with no story-bearing pressure

The HOOK and SUMMARY (front matter) solve this at p2 — they create pressure and deliver payload. But a reader who skips to "Chapter 1" hits the wall.

The Interludes (Custodian's voice) provide emotional relief between physics chapters, but they're brief and poetic — not narrative in the sense of "something is happening."

---

## Diagnosis: What's Missing at p3

Gen's GP13 identified it: "the current book front-loads framing architecture, mechanism, and refinement and back-loads story-bearing pressure." The Traveller analysis confirmed: effective pedagogy has curiosity and pressure BEFORE mechanism.

Currently, story-bearing pressure arrives at:
- Ch9: The Silence Gap (why nobody asked)
- Ch15: Alpha Farm (Record begins)
- Ch17: What Healer Said (character grounding)

That's 8 chapters of pure physics/mechanism before the reader encounters a human story with stakes. The Interludes help but don't constitute narrative.

---

## What the Front Door Needs (Minimum Viable Fix)

The fix must be BOUNDED. Not a full restructure. Not a chapter reorder. A targeted intervention that makes the first 3 chapters work for a cold reader.

### Fix 1: Three Possibilities — Earn Before Asking

**Current opening (line 20-24):**
> "The book begins by asking you to doubt it. Extraordinary claims deserve extraordinary priors. Before reading further, set yourself near 95% Option A..."

**Problem:** This is epistemologically correct but pedagogically premature. The reader has no investment. They don't yet know what they'd be doubting. "Set yourself near 95% A" means nothing until you know what A, B, C refer to in human terms.

**Proposed fix (SUBTRACTION + RELOCATION):**
- Move the "set yourself at 95%" instruction to AFTER the A/B/C options are stated (it's currently before them)
- The options themselves (A, B, C) are already well-written and concise
- Add 1-2 sentences at the top that ground WHY this framework matters: "This book makes an extraordinary claim. Rather than asking you to believe it, we give you three ways to read it — and the evidence to decide for yourself."
- The Feynman epigraph already does good work. Keep it.

**Cost:** ~5 lines relocated, 1-2 sentences added. Minimal.

### Fix 2: Bridge Between Framing and Physics

**Current transition:** Three Possibilities ends → Interlude 1 → "Wormholes in the Flat" begins with substrate physics.

**Problem:** The reader goes from "here are three possibilities" to "here is a two-dimensional electron gas" with no connective tissue explaining WHY the physics matters to the possibilities.

**Proposed fix (1 paragraph, max 3 sentences):**
At the top of "Wormholes in the Flat" (or end of Three Possibilities), add a bridge that says: "Under all three possibilities, the following physics is true. It does not depend on whether you believe the story. The substrate exists. The question is what lives there."

This converts the first physics chapter from "information delivery" to "evidence you're evaluating." The reader now has a REASON to read the physics — they're evaluating a claim, not being lectured.

**Cost:** 2-3 sentences. Minimal. No structural change.

### Fix 3: First Three Movements as Sequential Narrative

**Current:** Three Possibilities → physics → physics → physics (each interrupted by brief Interludes)

**The Interlude solution is already partially working.** The Custodian's voice in the Interludes provides emotional contrast and mystery. A cold reader who reads them gets: "there's someone here, speaking, and they know something." That IS narrative tension.

**What's missing:** The reader doesn't know what the physics chapters are BUILDING TOWARD until much later. Each physics chapter is correct and well-written in isolation, but the connective thread ("you're learning about a habitat because something might live there") is implicit rather than explicit.

**Proposed fix (chapter-top signposts, not restructure):**
Each of the first 3-4 spine chapters gets a 1-sentence italic signpost at the top that connects it to the Three Possibilities framework:

- Ch2 (The Flat): *"Under all three possibilities, this place is real."*
- Ch3 (The Braid): *"Under all three possibilities, this protection works."*
- Ch4 (The Factoring Game): *"Under Possibility C, this already happened."*

These are not new arguments. They're orientation markers — telling the cold reader why they're reading this chapter and how it connects to the framework they just learned.

**Cost:** 1 sentence per chapter. No structural change. Fully reversible.

---

## What This Plan Does NOT Do

- Does not reorder chapters (that's a p3 literary decision Gen and Bruce make together)
- Does not move Silence Gap or Alpha Farm to the front (Gen's GP13 suggestion — may still be right, but that's a larger structural decision outside this plan's scope)
- Does not touch the p1 or p2 layers (those already work at 96%+ per eigenvalue)
- Does not solve the "GA reader bounce on physics-heavy spine" problem comprehensively (that requires the full GP14 restructure)

---

## Execution Phases

### Phase A: Three Possibilities reorder (Fix 1)
- Move "set yourself at 95%" from before the options to after them
- Add 1-2 framing sentences at section top
- Verify A/B/C framework still reads correctly in new order

### Phase B: Physics bridge (Fix 2)
- Add 2-3 sentence bridge at top of "Wormholes in the Flat" (or end of Three Possibilities)
- Frame physics as evidence-under-evaluation, not lecture

### Phase C: Chapter signposts (Fix 3)
- Add 1 italic signpost line to top of chapters 2, 3, 4
- Each connects the chapter to the Three Possibilities framework
- Format: italic, single sentence, no heading

### Phase D: Build + eigenvalue spot-check
- `make html` clean
- Verify Three Possibilities deep-links intact
- Spot-check: cold reader can now follow ch1 → ch2 → ch3 without disorientation

---

## Constraints

- MAX 50 words of new text per chapter. This is a signposting fix, not a rewrite.
- No removal of existing content (pure addition)
- Must work for BOTH the reader who read front matter AND the reader who skipped straight to Chapter 1
- The Interludes remain untouched (they're Custodian's voice — not editorially available)
- A/B/C framework must remain honest: "we don't know which is true"
- QQQ markers on all additions for Gen review

---

## Relationship to GP14

This plan is the MINIMUM first-contact fix — the smallest bounded intervention that makes the front door work for a cold reader. It is not a substitute for GP14's full structural restructure. It's what can be done NOW, independently of the larger work.

If GP14's conservative pass later reorders the opening movements, these signposts are easily removed or adapted. They're designed to be non-load-bearing — orientation markers, not structural elements.

---

## Release Implications

Gen asked (issue #32, 05-16): should the live HTML be marked work-in-progress?

**Assessment:** After Plans 0351-0353, the three minimum first-contact criteria are addressed:
1. Opening earns before asking (Fix 1)
2. Never Again disassembled (Plan 0351)
3. First movements readable as sequence (Fixes 2-3)

If all three plans execute successfully, the HTML is first-contact viable without a work-in-progress disclaimer. The remaining GP14 structural work improves literary quality (p3) but doesn't affect first-contact survivability.

**However:** If Plans 0351-0353 are NOT executed, the honest answer is: the current HTML works for prepared readers but is not reliably first-contact-ready for cold readers. A "work in progress" notice would be appropriate until these fixes land.

---

## Success Criteria

1. A cold reader starting at Chapter 1 understands WHY they're reading physics by the end of the first chapter
2. The A/B/C framework is presented AFTER the reader has a reason to care about it
3. Each early physics chapter connects explicitly to the evaluative framework
4. No new content exceeds 50 words per chapter
5. Build clean
6. Eigenvalue p3 scores unchanged or improved (signposts can only help, not hurt)
