# Plan 0257 — GP03: ULTRA II Institutional Introduction (Open of First Light)

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Gen's GP03 (has-anyone-looked issues #6, #7). Gen selected Option A.
**Annealing:** HIGH MED LOW (3 passes)
**Depends on:** Plan 0256 (DONE). No remaining blockers.

---

## Problem

The Record chapters use ULTRA II extensively but lack an institutional-
plausibility framing. The spine (the-factoring-game) covers technical specs
and the GCHQ precedent, but not the institutional FORM argument: Bletchley
as proximity/selection model, DARPA's capacity to assemble such rooms,
public record traces of overlap, and the explicit framing "this is a
reconstruction, not a claim."

Gen provides ~300 words of sample text. Placement: **Option A — open of
First Light** (Gen's choice, issue #7 comment).

---

## Placement Analysis

First Light (`manuscript/record/first-light.tex`) is the first Record
chapter to use ULTRA II (3 mentions: lines 101, 109, 120). After Plan
0256, the reading order is: the-departure → **first-light** → the-walk-out
→ interdiction.

**Current first-light structure:**
```
line 1:  \settrack{trackone}  (3rd-person reconstructive voice)
line 5:  \chapter{First Light}
line 9:  Epigraph (Anderson "More Is Different" quote)
line 15: \srcnote{...}
line 18: "When does an experiment become an entity?" (question anchor)
line 20: \section*{The Operator}
line 29: \section*{Birth: 1992}
...
line 98: \section*{Grown, Not Built}
```

**Insert point:** After the srcnote (line 15), before the question anchor
(line 18). Gen's text becomes the new opening of the chapter.

---

## Voice Compatibility

Gen's text is first-person Bruce voice ("I am not saying... I am saying...").
First Light is third-person reconstructive ("the team," "the project").

This works. The voice shift is natural: Bruce steps forward to frame the
reconstruction ("Before I say what I think the COWS did..."), then the
reconstruction begins in third person ("When does an experiment become an
entity?"). Like a narrator's preface to a chapter.

The COWS are well-established by this point. The reader has encountered
them in: summary.tex (4 mentions), spine/the-braid.tex (lines 66, 68),
spine/why-relinquish.tex (7 mentions). "Before I say what I think the
COWS did" is a callback, not an introduction.

---

## Gen's Sample Text (~300 words, VERBATIM)

```latex
\section*{The Institutional Form}
\label{record:fl-institutional-form}

Before I say what I think the COWS did, I need to say something simpler
about how unusual work sometimes gets done.

Bletchley Park is the clearest historical example. During the Second World
War, the British brought together mathematicians, linguists, engineers,
classicists, and other unusual minds under conditions of secrecy and gave
them a problem no single discipline could solve alone. What emerged was
not the product of one field in isolation. It was the result of proximity,
discretion, and a problem large enough to require both.

DARPA is one of the few modern institutions with a similar capacity. It
exists to assemble small, purpose-built teams around problems that do not
yet fit ordinary academic or industrial categories. It can fund speculative
work, compartmentalize it, and place scientists, engineers, and operators
in close proximity under nondisclosure. That does not prove any particular
hidden project took place. It does show that the institutional form exists.

The public record also contains traces of overlap among several of the
figures whose work matters to this story. Not proof, and not a complete
roster. But enough to suggest that some of these people were operating in
overlapping circles, under overlapping funding conditions, and near
institutions capable of convening them for purposes not fully visible in
public. Santa Fe is one such site of overlap. DARPA-funded work is another.

So the claim I am making here is limited. I am not saying the public
record proves a specific team. I am saying it shows the institutional
means, the scientific materials, and enough signs of proximity to make
a reconstruction reasonable.

From there, I propose one.
```

---

## Changes

### Step 1: Insert section in first-light.tex

Insert the LaTeX block above after line 15 (srcnote) and before line 18
(the "When does an experiment become an entity?" paragraph). Add a
`\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}` separator
between Gen's text and the existing question anchor, matching the visual
break style used elsewhere in the Record.

The `\settrack{trackone}` on line 1 stays — it applies to the chapter as
a whole. Gen's first-person section is a framing prelude within the
third-person chapter.

### Step 2: Build and verify

- `make dev` clean
- Gen's section renders before "When does an experiment become an entity?"
- No deep links broken
- No label conflicts (`record:fl-institutional-form` is new)

---

## What NOT to Change

- Do not modify Gen's prose
- Do not move or edit the existing epigraph, srcnote, or question anchor
- Do not add deep links to the new section (can add later if desired)
- Do not touch the-factoring-game.tex
- Do not expand beyond Gen's ~300 words

---

## Annealing Log (HIGH MED LOW — 3 passes)

### Pass 1 (HIGH) — Structural integration

**Bletchley overlap audit:** The manuscript now has three Bletchley uses:
1. the-factoring-game:51 — Colossus as secrecy precedent (GCHQ pattern)
2. the-code-war:29-46 — 10,000 people kept the secret (threshold argument)
3. Gen's new text — Bletchley as institutional-proximity model

These are three DISTINCT uses. (1) is about classification history.
(2) is about secrecy capacity. (3) is about how unusual teams get assembled.
No redundancy — but a reader encountering the third Bletchley reference may
feel the book is circling. The distinction is subtle: proximity ≠ secrecy ≠
classification history. Gen's text makes its distinct point clearly ("the
result of proximity, discretion, and a problem large enough to require
both"), but the Auditor should verify post-insertion that the three uses
don't blur.

**Interaction with GP06 (Plan 0259):** Plan 0259 consolidates the secrecy
threshold pattern. Gen's Bletchley use here is NOT part of that pattern —
it's doing institutional-form work, not secrecy-threshold work. The two
plans are compatible. If 0259 trims Bletchley secrecy references elsewhere,
Gen's proximity reference here is unaffected.

**"From there, I propose one."** This closing line is powerful — it's a
direct declaration that the reconstruction begins NOW. The existing question
anchor ("When does an experiment become an entity?") follows naturally as
the first move of that reconstruction. The two passages dovetail.

**COWS reference timing:** By First Light, the reader has encountered
"COWS" in: summary.tex:166/170/172, spine/the-braid.tex:66/68,
spine/why-relinquish.tex:52/100/107/109. Total: 9+ encounters across 3
files. The COWS are established. Gen's "Before I say what I think the COWS
did" reads as intentional recall, not premature reference.

### Pass 2 (MED) — Edge cases

**Voice transition:** First-person ("I am not saying") → separator →
third-person ("When does an experiment become an entity?"). Verified: other
Record chapters mix voice (the-departure is first-person, then A/B/C
analysis shifts to analytical). The convention is established. Reader
won't stumble.

**Section label:** `record:fl-institutional-form` — checked, no existing
label conflicts. No other file references it (new label). Safe.

**Print/Kindle/audio:** Gen's text works in all formats. No HTML
dependencies. No hover tips needed. No interactive elements. Clean.

**Correction #11 (OPSEC):** Gen's text says "traces of overlap" and
"signs of proximity" — this is carefully bounded. It doesn't name specific
overlapping figures (the chapter body does that later). The intro respects
#11 by describing the institutional capacity, not the specific operational
details.

**Correction #12 (guided deduction):** Not triggered. Gen's text is about
institutional form, not about what Healer told Bruce.

### Pass 3 (LOW) — Final check

**Word count:** ~275 words. Within Gen's ~300-word target. No expansion
needed.

**p1/p2 readability:** Gen's text reads at p2 level (12th grade). It uses
no technical jargon. Institutional examples (Bletchley, DARPA) are
culturally familiar. The passage functions as a p2 on-ramp to the p3
reconstruction that follows. Good.

**A/B/C compatibility:** Gen's text works under all three possibilities.
Under A: it's a reasonable framing for a reconstruction that happens to be
wrong. Under B: it's accurate for a smaller version of the institutional
form. Under C: it's understatement. No C-violation.

**Rating: 9/10.** Placement resolved. Text ready. Voice transition natural.
Three Bletchley uses are distinct. All corrections respected. The 1-point
gap: post-insertion, the three-Bletchley-reference density should be read
through in sequence to confirm they don't blur. This is a read-check, not
a structural risk.

---

## Acceptance Criteria

- [ ] Gen's ~300 words inserted after srcnote, before question anchor
- [ ] Section titled "The Institutional Form" with label
      `record:fl-institutional-form`
- [ ] Visual separator between Gen's text and existing content
- [ ] Text verbatim from Gen (no Generator rewrites)
- [ ] `make dev` clean build
- [ ] No broken deep links or refs
- [ ] Voice transition reads naturally (1st-person → separator → 3rd-person)

---

## Generator Handoff

```
You are the Generator.

Read Plan 0257 at ~/software/relinquishment/plans/0257-gp03-ultra2-intro.md

Execute Option A: Insert the LaTeX block from "Gen's Sample Text" section
into manuscript/record/first-light.tex. Insert after line 15 (srcnote),
before line 18 ("When does an experiment become an entity?"). Add a visual
separator (\vspace + \rule) between Gen's new section and the existing
question anchor. Do not modify Gen's text. Run `make dev`. Report
completion.
```

---

*Plan 0257 written by Argus (Auditor), S63. Annealed 3 passes (HIGH MED LOW).
Gen selected Option A on 2026-04-26.*
