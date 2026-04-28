# Plan 0280 — Magnetopause Hinge Passage

**Auditor:** Argus (S63)
**Date:** 2026-04-27
**Status:** PROMPT READY
**Source:** Gen's Document 4 (Plan 0275), Bruce chose Triad (S63)
**Annealing:** MED LOW
**Priority:** High — Tier 1 in Plan 0275

---

## Problem

The magnetopause passage in The Wrong Substrate currently reads
as technical exposition. Gen's proposal: frame it as the answer
to a real question Gen asked Bruce — "Where does this phenomenon
exist in nature?" — which shifts the frame from device/artifact
to nature/habitat/commons.

Key line: "You do not own an ocean because you learned to sail it."

## Scene Spec (from Gen)

**What happened:** Bruce explaining 2DEG to Gen. She asks
"Where does this exist in nature?" — meaning where do these
quantum substrates exist outside laboratories? Bruce realizes
the frame shift: the Flat isn't a manufactured thing, it's a
natural environment. The magnetosphere is habitat, not hardware.

**Register:** Brief, ordinary, Bruce's first-person perspective.
Not self-congratulatory. The insight belongs to Gen's question,
not Bruce's answer. Memory/witness frame.

**Emotional function:** The reader has spent chapters learning
about 2DEGs in chips. Now they learn this substrate exists at
planetary scale, in nature, maintained by the solar wind for
billions of years. The reframe: if it's nature, possession is
the wrong category. This directly serves T3 (life in the Flat)
and T6 (trusteeship — you can't own an ocean).

## Placement

**Chapter:** The Wrong Substrate (spine/the-wrong-substrate.tex)

**Where:** BEFORE the existing magnetosphere exposition. The
chapter currently opens with physics. Gen's hinge should precede
that — the reader meets the QUESTION before the ANSWER.

**Marker:** Insert before `\section*{The Invisible Ocean}` —
between the Haldane epigraph/opening italics and the first
section header.

**Length:** 150-250 words. One scene. Brief.

## Content Guidance

The passage should:
- Be in Bruce's first-person voice (Record register, even
  though this is a spine chapter — the hinge crosses tracks)
- Show Gen asking the question naturally (dinner, conversation)
- Show Bruce's realization: "I'd been thinking about it as
  technology. She was asking about it as nature."
- NOT explain the physics (the chapter does that immediately
  after)
- End with the reader primed to read the magnetosphere section
  as "habitat survey" not "physics lecture"

The passage should NOT:
- Be longer than 250 words
- Include the "sail an ocean" line literally (let the reader
  arrive there — the chapter earns it)
- Make Gen a mouthpiece (she asks a genuine question, not a
  Socratic setup)
- Explain who Gen is (the preface handles that)

## Acceptance Criteria

- [ ] 150-250 word passage in Bruce's voice
- [ ] Placed before The Invisible Ocean section
- [ ] Gen asks the question, Bruce realizes the reframe
- [ ] No physics explanation in the passage itself
- [ ] Works under A/B/C (the question is real regardless)
- [ ] `make dev` clean
- [ ] Does not disrupt the chapter's existing flow

---

## Generator Handoff

```
You are the Generator.

Read Plan 0280 at ~/software/relinquishment/plans/0280-magnetopause-hinge.md

Execute: Write the magnetopause hinge passage.

(1) Read manuscript/spine/the-wrong-substrate.tex for context
and register.

(2) Write a 150-250 word passage in Bruce's first-person voice.
Scene: Bruce explaining 2DEGs to Genevieve. She asks "Where
does this exist in nature?" Bruce realizes the frame shift —
he'd been thinking technology, she was asking about nature.
Brief, ordinary, not self-congratulatory. The insight belongs
to her question.

Content guidance and constraints are in the plan. Read them.

(3) Insert the passage BEFORE \section*{The Invisible Ocean},
after the opening italic line. Add a \vspace{0.5cm} separator.

(4) Run make dev. Verify the passage appears in the HTML before
the magnetosphere exposition.

(5) Commit: "Plan 0280: magnetopause hinge passage — Gen's
question reframes substrate as habitat"

(6) Push. Report: word count, placement confirmed, build status.
```
