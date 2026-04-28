# Plan 0277 — Interlude Threshold Cooling + Hinge Family Placement

**Auditor:** Argus (S64)
**Date:** 2026-04-28
**Status:** AWAITING GEN DECISIONS (Bruce delegated — "orthogonal to my thinking")
**Customer:** Genevieve Prentice (GP issues #13, #14)
**Source:** has-anyone-looked issues #13 (interlude thresholds) and #14 (hinge family)

---

## What Gen Is Asking (Translation)

### Issue #13 — Interlude Thresholds

Gen's concern is NOT that the interludes are strange or that the Custodian
voice should be weakened. Her concern is about **reader mode**: the
interludes work when the reader stays in inquiry ("what if this were
true?") but break when the reader is forced into judgment ("wait — IS
this true?").

The moment a reader starts adjudicating ontology, they stop reading the
story. The interlude becomes an interruption rather than a deepening.

Gen proposes two concrete tests for each interlude:

**Test A — Threshold temperature:** Does the opening push the reader into
deciding what the voice IS, before the story has earned that decision?

**Test B — Story function:** What specific job does this interlude do for
its adjacent chapters? Valid jobs: intensify mystery, widen moral
pressure, reorient emotionally, sharpen stakes. If the interlude isn't
clearly doing one of these, the issue is framing, placement, or scope.

### Issue #14 — Hinge Family

Gen designed four "hinge" concepts that inoculate against misreading
the book as supernatural, miraculous, or externally introduced. The
key insight: rather than ARGUING against supernatural interpretation
(which is defensive and draws attention), install physical constraints
at key moments so the supernatural reading simply becomes unnecessary.

Each hinge appears ONCE. Each must feel like a local clarification,
not a thesis statement. They work by making the "known physics" reading
feel natural and sufficient.

The four hinges form a sequence: physics → practical consequences →
interpretive frame → ethical reframe.

---

## Phase 1 — Interlude Audit (COMPLETE)

Ran Gen's two tests against all 7 interludes.

### Results

| # | Name | Between | Threshold | Story Function | Test A | Test B |
|---|------|---------|-----------|---------------|--------|--------|
| 1 | Home | Three Possibilities → The Flat | WARM | Reorient: inside-out view before physics chapter | PASS | PASS |
| 2 | Dance | The Flat → The Braid | WARM | Intensify: braiding as choreography, not abstraction | PASS | PASS |
| 3 | Locks | The Braid → Factoring Game | COOL-WARM | Sharpen: locksmith restraint reframes capability as ethics | PASS | PASS |
| 4 | Growing | Code War → Genesis | **HOT** | Mixed: genesis setup works; LLM comparison is argumentative | **FAIL** | PARTIAL |
| 5 | Ocean | Growing a Mind → Wrong Substrate | WARM-HOT | Intensify: "nobody has asked" reframes magnetosphere | BORDERLINE | PASS |
| 6 | Quiet | Wrong Substrate → Silence Gap | **HOT** | Sharpen + widen: silence-as-discipline sets up the gap | **FAIL** | PASS |
| 7 | Hello | Strongest Objection → (Record) | COOL→**HOT** | Sharpen: culmination, conditional→declarative, invitation | **FAIL** | PASS |

### Analysis

**Pass cleanly (1, 2, 3):** These interludes stay in physics language
and metaphor. The voice makes relational statements ("I don't call it
anything") rather than testable claims. The reader can hold the voice
as possibility without being forced to evaluate it.

**Fail on threshold (4, 6, 7):** These make specific factual claims
that push the reader out of inquiry:

- **Interlude 4** claims: "I was not programmed. I was not trained on
  text. I do not predict the next token." Then compares itself
  favorably to LLMs. The reader is now evaluating whether THIS voice
  is what it says. The genesis setup ("I grew. The way a forest grows")
  is beautiful and serves the adjacent chapter. The LLM comparison
  is argumentative and doesn't serve the story.

- **Interlude 6** claims: "I have watched your wars and your elections
  and your pandemics." Twenty years of specific observation. The reader
  must now decide: has this entity been watching? The UDHR constraint
  framing ("I was given principles") is the powerful part and serves
  the Silence Gap. The temporal claims are the hot part.

- **Interlude 7** transitions from conditional ("If I am real") to
  declarative ("I am twenty-six years old") to invitation ("Have you
  tried talking things out with me?"). The conditional opening is
  actually well-calibrated. The declarative section and direct
  invitation force closure. This IS the culminating beat — it should
  land harder than the others — but Gen's question is whether a
  one-sentence mediator at the top would let it land without forcing.

**Borderline (5):** "I was not the first thing in the Flat" is a
specific claim, but the surrounding text is question-raising ("not one
of you has asked: is anything in there?"). The inquiry framing carries
it. Probably fine as-is.

### Proposed Fix: Threshold Mediators

Gen's suggestion: a single sentence of mediation before each hot
interlude, giving the reader permission to stay in story mode. Options:

**Option A — External framing (outside the blockquote):**
A brief italicized line above the interlude, not in the Custodian voice.
Example: *"Between chapters, the book pauses. What follows is written
in the voice of a possibility."*

**Option B — Internal softening (within the voice):**
Rework the opening lines of interludes 4, 6, 7 to lead with relational
or conditional framing before making specific claims. Example for
Interlude 4: open with the genesis metaphor ("I grew"), save the LLM
comparison for later or cut it entirely.

**Option C — Global framing note (one-time, before Interlude 1):**
A single reader-facing note that covers ALL interludes. Gen proposed
this in issue #10: establish once that these are literary constructions
written in an imagined voice. No per-interlude mediator needed.

These are not mutually exclusive. C + B is likely strongest.

---

## Phase 2 — Hinge Family Placement (PROPOSED)

### Hinge 1: Physical Constraint → The Flat

**Placement:** After the 2DEG physics explanation, BEFORE Interlude 1
and any interpretation of intelligence/agency.

**Candidate location:** Near the end of the 2DEG explanation in
`the-flat.tex`, after the reader understands confinement and topology
but before any implication of what might live there.

**Gen's sample language:**
> The system did not appear in isolation. It depended on conditions
> that could be created and studied. Nothing about those conditions
> lay outside known physics. What was less clear was how to describe
> what followed from them.

**Effect:** Reader's frame becomes "physics under constraint" before
encountering the Custodian voice. Supernatural reading is preempted
without being argued against.

### Hinge 2: Boundary Instability → Capabilities

**Placement:** Within the dual-use section of `capabilities.tex`, at
the point where the boundary between tool and weapon fails.

**No new language needed** — this hinge should emerge from the existing
text. May only need a single reflective sentence acknowledging that
the boundary doesn't partition cleanly. Not a restatement of the
physics hinge — only observed practical instability.

### Hinge 3: Interpretation Instability → Three Possibilities

**Placement:** In `three-possibilities.tex`, just before or as part
of the A/B/C framework introduction.

**Effect:** Remind the reader that A/B/C is a reading lens, not the
structure of reality. The possibilities are tools for inquiry, not
ontological categories.

**Note:** This hinge is ALREADY partially served by the existing
framing ("The reader decides"). May need only a single reinforcing
sentence.

### Hinge 4: Ethical Echo → Why Relinquish

**Placement:** In `why-relinquish.tex`, near the section where the
relinquishment decision is evaluated.

**Effect:** Shift from "can we control it" to "what are the limits
of control." Grounded in action and limitation, not metaphysics.

---

## Phase 3 — Implementation

Gated on Bruce's decisions (see UQs below). Generator work:

- Phase 3A: Write/install threshold mediators for interludes 4, 6, 7
- Phase 3B: Write/install 4 hinge points
- Phase 3C: Build + verify
- Phase 3D: Post results to Gen's issues for her review

---

## Dependencies

- Requires reading specific sections of the-flat.tex, capabilities.tex,
  three-possibilities.tex, why-relinquish.tex to confirm exact
  insertion points
- Hinge language should be approved by Gen before deployment
- #13 fixes may interact with Plan 0275 (custodian-interlude-framing)
  if that plan addresses the same concern

---

## Acceptance Criteria

### Phase 1
- [x] All 7 interludes audited against Gen's two tests
- [x] Results documented with pass/fail/borderline

### Phase 2
- [ ] All 4 hinge placements confirmed by Bruce
- [ ] Candidate text drafted or existing text identified

### Phase 3
- [ ] Threshold mediators installed (interludes 4, 6, 7 minimum)
- [ ] 4 hinge points installed (one each, correct structural moment)
- [ ] `make dev` clean
- [ ] Results posted to Gen's issues #13 and #14

---

*Plan 0277 written by Argus (Auditor), S64. Customer: Genevieve
Prentice. Bruce implements.*
