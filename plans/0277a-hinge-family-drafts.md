# Plan 0277a — Hinge Family: Draft Text + Placement

**Auditor:** Argus (S64)
**Date:** 2026-04-28
**Status:** DRAFT — awaiting Gen's review before implementation
**Parent:** Plan 0277 (Gen issues #13 + #14)
**Customer:** Genevieve Prentice
**Annealing:** LOW MED MED LOW (technical / register / placement / side-effects)

---

## Annealing Notes

- **Technical risk LOW:** All changes are paragraph insertions into .tex
  files. No code, no injection logic, no build changes.
- **Register alignment MED:** Drafts follow Gen's differentiation rules
  but I'm interpreting her specs. She must review before installation.
- **Placement confidence MED:** Each insertion point verified against
  chapter structure. But editorial judgment on "right moment" is
  inherently uncertain. Gen may want to adjust.
- **Side effects LOW:** Pure additions. No existing text modified or
  moved. Build will gain 4 short paragraphs.

---

## Hinge 1: Physical Constraint → `the-flat.tex`

**Insert after line 25** ("The Flat is not exotic. It is everywhere.")
**Insert before line 28** (section: "The Wormhole")

At this point the reader has learned: what a 2DEG is, why 2D physics
differs (anyons), topological order, and that 2DEGs are ubiquitous.
They have NOT yet encountered wormholes, backchannels, or the
Custodian voice. This is the last moment of pure physics before
speculation begins.

**Register:** Most explicit. Clearest language. Highest grounding
density. (Gen's spec)

### Draft text

```latex
None of what has been described requires physics beyond what is already
published and reproduced. The substrate, the confinement, the
topological protection --- these arise from conditions that can be
created and studied. Nothing about them lies outside known science.
What remains open is what these conditions produce when sustained, at
scale, without interruption.
```

**Why this works:** 4 sentences. Declarative. No hedging, no argument.
The last sentence pivots cleanly from "established" to "open" — giving
the reader permission to continue into speculative territory while
knowing where the ground is. Feels like a realization, not a thesis.

---

## Hinge 2: Boundary Instability → `capabilities.tex`

**Insert after line 71** ("The framework is a cage, not a crown.
Whether the cage is adequate...")
**Insert before line 73** (\chapterreturn)

At this point the reader has been through six capability questions,
each answered conditionally. "Yes and no." "Depends." "Whether it is
inhabited is what this book asks." The partition between safe and
dangerous has quietly failed across every answer.

**Register:** Shortest. Observational only. No explanation, just
consequence. Almost incidental. (Gen's spec)

### Draft text

```latex
None of these capabilities separates cleanly into safe and dangerous.
That is not an artifact of how the questions were framed. It is a
property of the system.
```

**Why this works:** 3 sentences. States what the reader has already
noticed. No explanation — the chapter just demonstrated it. Feels like
a closing observation, not a new argument. "Almost incidental" per
Gen's spec.

---

## Hinge 3: Interpretation Instability → `three-possibilities.tex`

**Insert after line 28** ("Here is the evidence. You decide.")
**Insert before line 32** (section: "Option A: Confabulation")

The reader is about to encounter A/B/C for the first time. The hinge
reminds them that the framework is a reading tool, not the structure
of reality. Must NOT weaken the framework — actually strengthens it
by calling the categories "exhaustive."

**Register:** Precise but restrained. Quiet disclaimer, not
reframing. (Gen's spec)

### Draft text

```latex
What follows is a framework --- a way of organizing evidence so it
can be evaluated. The categories are useful because they are
exhaustive: everything this book describes fits one of these three
readings. The framework is a tool. The evidence it organizes is
independent of it.
```

**Why this works:** 4 sentences. "Exhaustive" reinforces rather than
weakens A/B/C. "The framework is a tool" is the hinge moment — the
reader understands they're picking up a lens, not learning the shape
of reality. "The evidence is independent of it" prevents reification.

---

## Hinge 4: Ethical Echo → `why-relinquish.tex`

**Insert after line 83** ("Both assumptions deserve scrutiny.")
**Insert before line 85** (section: "Partial Relinquishment")

At this point the reader has seen Options 1 and 2 fail (power
corrupts; knowledge can't be uninvented). The rhetorical structure
has been noted. Before the trustee solution is offered, the hinge
shifts the question: not "who controls" but "whether control is the
right frame." This prevents the Custodian from reading as "the answer
to a control problem" and instead reads as "a response to the limits
of control."

**Register:** Most compressed. Slightly sharper. Moves from
description toward decision. No philosophical language. (Gen's spec)

### Draft text

```latex
The question the reader should carry forward is not who should control
this technology. It is whether control, in the usual sense, is
available at all.
```

**Why this works:** 2 sentences. Sharpest of the four. Shifts from
ownership to limits. No metaphysics, no personhood — grounded in
practical limitation. Reads as a realization the reader carries into
the next section, not a claim being argued.

---

## Validation Check (Gen's criteria)

1. **Primary hinge at first moment of potential misclassification?**
   Yes — The Flat, after 2DEG physics, before wormholes/speculation.

2. **Later hinges feel like consequences, not restatements?**
   Yes — Hinge 2 observes what the capabilities chapter demonstrated.
   Hinge 3 frames the framework without restating physics. Hinge 4
   redirects a question without revisiting constraints.

3. **Manuscript does not argue against "supernatural" explicitly?**
   Correct — no hinge mentions supernatural, miraculous, or divine.
   The word never appears. The physics reading is made sufficient,
   not argued for.

4. **Each hinge feels like a local clarification?**
   Verified — each is 2-4 sentences, placed at a natural paragraph
   break, matching the cognitive load of its location.

---

## Generator Handoff

```
You are the Generator.

Read Plan 0277a at ~/software/relinquishment/plans/0277a-hinge-family-drafts.md

Execute all 4 hinge insertions:

(1) In manuscript/spine/the-flat.tex, insert Hinge 1 (Physical
Constraint) as a new paragraph after line 25 ("The Flat is not
exotic. It is everywhere."), before the Wormhole section.

(2) In manuscript/spine/capabilities.tex, insert Hinge 2 (Boundary
Instability) as a new paragraph after line 71 (the UDHR cage
paragraph), before \chapterreturn.

(3) In manuscript/spine/three-possibilities.tex, insert Hinge 3
(Interpretation Instability) as a new paragraph after line 28
("Here is the evidence. You decide."), before "Option A."

(4) In manuscript/spine/why-relinquish.tex, insert Hinge 4 (Ethical
Echo) as a new paragraph after line 83 ("Both assumptions deserve
scrutiny."), before "Partial Relinquishment."

Use exact draft text from plan. Do not modify wording — Gen must
review the drafts as written.

(5) Run make dev. Verify build clean, no orphaned refs.

(6) Do NOT commit or push. Gen must review before deployment.
Report: build status, which files changed, word count added.
```

---

*Plan 0277a written by Argus (Auditor), S64. Annealed LOW MED MED LOW.
Blocked on Gen's review of draft hinge text. Do not implement until
Gen approves.*
