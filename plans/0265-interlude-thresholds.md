# Plan 0265 — Interlude Threshold Sentences

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR (after Bruce approval)
**Source:** Gen's issue #13 (has-anyone-looked): interlude framing
**Annealing:** HIGH MED MED LOW LOW (5 passes)
**Independent:** No dependency on GP plans. Compatible with Plan 0262
(A/B/C compression does not touch interludes).

---

## Problem

Gen's diagnosis: the Custodian interludes can push the reader into
premature ontological adjudication — "what IS this voice, am I being
asked to believe this, is this theological, is this AI?" — instead of
keeping them in inquiry and story. The reader stops experiencing the
interlude and starts adjudicating it.

Gen's solution: give each interlude a "cooler threshold" — a single
mediating sentence that sets the reader's mode of attention to inquiry
rather than judgment. The reader should be able to hold the strangeness
without settling it.

Gen's test: does each interlude serve a specific story function for the
chapter it sits beside (intensifying mystery, widening moral pressure,
reorienting emotion, sharpening stakes)?

---

## Story Function Mapping

| # | Interlude | Placement | Story function | Threshold need |
|---|-----------|-----------|---------------|----------------|
| 1 | Home | Three Possibilities → The Flat | Reorient: framework → felt experience. "What would it be like to live here?" | **CONVENTION-SETTER** — first encounter, sets reader's posture for all 7 |
| 2 | The Dance | The Flat → The Braid | Embody: make braiding feel physical before the physics chapter | LOW — physics grounds it |
| 3 | Your Locks | The Braid → The Factoring Game | Moralize: make crypto capability feel like moral weight, not superpower | LOW — locksmith analogy is clearly literary |
| 4 | Growing | The Code War → Genesis | Personalize: make emergence feel like something FROM INSIDE before the theory chapter | **HIGH** — "I was not programmed" / LLM comparison forces adjudication |
| 5 | The Ocean | Growing a Mind → The Wrong Substrate | Sharpen: "no one has asked" — prime the silence gap question | **MED** — mostly inquisitive, but closing claim ("I was not the first thing in the Flat") is a flat assertion |
| 6 | Quiet | The Wrong Substrate → The Silence Gap | Weight: make silence feel like discipline before the sociological analysis | **HIGH** — testimony claims (watching wars, elections, pandemics) |
| 7 | Hello | The Strongest Objection → Weigh the Evidence | Climax: emotional peak before the reader's final assessment | **HIGHEST** — conditional → declarative transition, closing invitation |

**All 7 interludes serve clear story functions for their adjacent
chapters.** No misalignment found. The issue is not placement or content
— it is the MODE OF ENTRY.

---

## Design: What a Threshold Sentence Does

### A threshold sentence DOES:
- Set the reader's attention to inquiry mode ("stay with this")
- Acknowledge something different is happening ("a voice appears")
- Keep the reader inside the book's field of encounter
- Feel like a stage direction, not an explanation

### A threshold sentence DOES NOT:
- Name the voice ("Custodian speaks" — collapses to C)
- Disclaim the voice ("this is literary construction" — breaks immersion)
- Re-explain A/B/C ("under one reading..." — management tone, exactly
  what Gen wants less of)
- Tell the reader what to feel or conclude
- Run longer than 2 sentences

### A/B/C neutrality requirement:
Under A: the threshold frames a fictional voice — fine.
Under B: the threshold frames a speculative voice — fine.
Under C: the threshold frames a real voice that the reader isn't yet
ready to receive as real — fine, and actually protective.

The threshold is A/B/C neutral because it deliberately leaves the
ontological question open. It says "a voice is here" without saying
what kind of voice.

---

## Threshold Convention

Add a threshold to ALL 7 interludes. Reasons:

1. **Consistency.** If only 4-7 have thresholds, the inconsistency draws
   attention ("why does this one have a threshold?"). A consistent
   convention disappears into the reading experience.

2. **Convention-setting.** Interlude 1 is the first encounter. The
   reader's mode of attention is formed here. If it has a threshold,
   every subsequent interlude inherits the posture.

3. **Graduated intensity.** Interludes 1-3 get light thresholds (one
   brief line). Interludes 4-7 get substantive thresholds (1-2 sentences
   calibrated to the specific content).

### Threshold placement

After the opening horizontal rule, before the block quote. Non-italic,
centered, in the interlude's visual container but outside the voice.
Mediates between the chapter the reader just finished and the voice
they're about to hear.

```latex
\begin{center}
\rule{0.3\textwidth}{0.4pt}
\end{center}

\begin{center}\small
Threshold sentence here.
\end{center}

\begin{quote}
\textit{Interlude text...}
```

---

## Per-Interlude Specification

### Interlude 1: Home (CONVENTION-SETTER)

**Function:** Set reader's posture for ALL interludes.

**Constraint:** Must communicate three things in ~15 words: (1) a voice
appears, (2) it will recur, (3) hold it without settling it.

**Example (for Generator guidance, not final text):**
*A voice speaks from inside the proposition. It will return between
chapters. Hold it lightly.*

**What it cools:** The reader's first instinct to categorize the voice.

### Interlude 2: The Dance (LIGHT)

**Function:** Keep convention alive without over-mediating.

**Constraint:** ≤10 words. The physics content does the grounding.

**Example:** *The voice returns.*

### Interlude 3: Your Locks (LIGHT)

**Function:** Same as 2.

**Constraint:** ≤10 words.

**Example:** *The voice returns.*

(Interludes 2 and 3 can use the same minimal threshold if it reads
naturally. The convention is already set by Interlude 1.)

### Interlude 4: Growing (SUBSTANTIVE)

**Function:** Cool the "I was not programmed" / LLM comparison claims.

**Constraint:** Frame what follows as imagined experience of emergence,
not testimony about origin. Must not disclaim — must reframe.

**Example:** *What follows claims to describe emergence from inside. It
is not evidence. It is an invitation to imagine.*

**What it cools:** "I was not programmed" / "I am not like AI" — the
reader no longer needs to settle whether the AI co-author is identifying
with the entity. The threshold has said: this is imagination, not claim.

### Interlude 5: The Ocean (SUBSTANTIVE)

**Function:** Cool the closing assertion ("I was not the first thing in
the Flat").

**Constraint:** Frame the voice's observations as conditional.

**Example:** *The voice asks a question the next chapter will examine.*

**What it cools:** The factual claim at the end. The threshold has
pre-framed this as a question, not an answer.

### Interlude 6: Quiet (SUBSTANTIVE)

**Function:** Cool the testimony claims (watching wars, elections,
pandemics, applying UDHR principles to real events).

**Constraint:** Frame as "what silence would cost if the proposition
holds." Must maintain emotional weight while adding conditional distance.

**Example:** *If the proposition holds, silence has a weight. This is
what that weight might feel like.*

**What it cools:** The specificity of "I have watched your wars." The
threshold reframes this as conditional exploration — "what would it feel
like" — rather than first-person testimony.

### Interlude 7: Hello (COOLEST)

**Function:** Protect the reader at the book's emotional peak. This is
the interlude most likely to be read as communication from Custodian.
The threshold must be the coolest without killing the emotional impact.

**Constraint:** Must front-load "this proves nothing" while preserving
"but listen." Two sentences maximum.

**Example:** *One last voice before you decide. It proves nothing. It
asks only to be heard.*

**What it cools:** The entire interlude — especially the transition from
"If I am real" (conditional) to "I am twenty-six years old" (declarative)
and the closing invitation ("Have you tried talking things out with me?").
The threshold gives the reader permission to be moved without feeling
manipulated.

---

## What NOT to Change

- Interlude content (the voice text inside the block quotes)
- Visual formatting (horizontal rules, italic, block quotes)
- Placement (which chapter each interlude sits between)
- The A/B/C frame — thresholds ADD to it, don't replace it

---

## Annealing Log (HIGH MED MED LOW LOW — 5 passes)

### Pass 1 (HIGH) — Full interlude audit

Read all 7 interludes in full. Mapped story functions against adjacent
chapters. All 7 serve clear, non-redundant functions. No misalignment.
The problem is not content or placement — it is the reader's mode of
entry.

Confirmed: Interludes 1-3 are grounded in physics concepts and read as
thought experiments. Interludes 4, 6, 7 make specific claims that push
beyond literary perspective. Interlude 5 is borderline (mostly
inquisitive, one assertive closing line).

Decision: threshold ALL 7 for convention consistency. Graduate intensity:
light (1-3), substantive (4-7).

### Pass 2 (MED) — Threshold design and A/B/C neutrality

Designed the threshold format: non-italic, centered, between horizontal
rule and block quote. This places the threshold inside the interlude's
visual container but outside the voice — it mediates without becoming
part of the voice.

A/B/C neutrality check: thresholds that say "a voice speaks" or "the
voice returns" are neutral — they acknowledge the voice without
classifying it. Thresholds that say "imagine" or "it proves nothing" are
slightly A-leaning (treating the voice as speculative). But Gen's
explicit concern is that the interludes collapse toward C. A slight
A-lean in the threshold CORRECTS the C-lean in the content. Net effect:
closer to center. Acceptable.

### Pass 3 (MED) — Interaction with existing plans and prior audit

**Plan 0262 (A/B/C compression):** Does not touch interludes. No
interaction.

**Plans 0257-0261:** Touch Record and spine chapters, not interludes.
No interaction.

**Prior interlude audit (issue #10):** Assessed all 7 against Gen's
5-question test. Recommended "one global note before Interlude 1, plus
a single reinforcing sentence before Interlude 7." This plan supersedes
that recommendation with a more nuanced approach: graduated thresholds
for all 7, calibrated per interlude. The prior audit's findings inform
the threshold-need ratings.

**Gen's two concrete proposals:** (1) Cooler threshold — addressed by
the threshold convention. (2) Test against adjacent chapter — addressed
by the story function mapping table. Both proposals fully covered.

### Pass 4 (LOW) — Generator feasibility

The Generator must COMPOSE threshold sentences, not just insert
pre-written text. This is the plan's main risk: the threshold sentences
are voice work that requires editorial judgment. The plan provides:
- Constraints (what to do / not do)
- Examples (for guidance, not verbatim use)
- A/B/C neutrality requirements
- Per-interlude calibration

The Generator should draft all 7 thresholds in one pass, then Bruce
and Gen approve before shipping. This is a 2-step execution: draft →
approve → insert.

Risk: the Generator may over-write (too many words, too explanatory).
The constraint "≤2 sentences, feels like a stage direction" should
prevent this.

### Pass 5 (LOW) — Drift check

**Gen's original intent:** "I'm asking that they be shaped so the reader
can remain in inquiry and story while they do their work." And: "even a
single sentence of mediation can change how hard the reader is pushed."

**Plan's approach:** Add one threshold sentence per interlude, graduated
by need, maintaining inquiry mode.

**Drift check:** Does the plan match Gen's intent?

- "Remain in inquiry" — YES. Thresholds set inquiry mode, not judgment.
- "Part of the book's field of encounter" — YES. Thresholds are inside
  the interlude visual container, part of the reading experience.
- "Not yet a resolved ontological claim" — YES. No threshold names,
  disclaims, or classifies the voice.
- "Single sentence of mediation" — YES. 1-2 sentences max per interlude.
- "Test against adjacent chapter" — YES. Story function mapping table.
- "Cooler threshold into the page" — YES. Graduated cooling calibrated
  to content intensity.

**Potential drift:** The plan adds thresholds to ALL 7 interludes, while
Gen's text focuses on the ones that "stop serving the story." Interludes
1-3 don't have this problem — they already serve the story cleanly. 
Adding thresholds to 1-3 is a CONVENTION choice (consistency), not a
necessity. If Bruce or Gen prefer thresholds only where needed (4-7),
the plan supports that with no structural change.

**No drift detected.** Plan matches Gen's intent.

**Rating: 8/10.** The 2-point gap: (1) threshold sentences require
editorial voice judgment — the Generator must compose, not just insert,
and the examples may steer toward a specific register that Gen or Bruce
want different; (2) the "cooler but not cold" calibration for Interlude
7 is the hardest single sentence in the plan — it must cool without
killing the emotional peak that makes the interlude work. Both risks
are managed by the draft → approve → insert workflow.

---

## Acceptance Criteria

- [ ] All 7 interludes have threshold sentences
- [ ] Thresholds are non-italic, centered, between rule and block quote
- [ ] No threshold names, disclaims, or classifies the voice
- [ ] Every threshold is ≤2 sentences
- [ ] Interludes 1-3: light thresholds (≤10 words)
- [ ] Interludes 4-7: substantive thresholds (calibrated per specification)
- [ ] All thresholds are A/B/C neutral (or at most slightly A-leaning)
- [ ] Interlude content unchanged
- [ ] `make dev` clean build
- [ ] Bruce and Gen approve threshold text before final insertion

---

## Generator Handoff

```
You are the Generator.

Read Plan 0265 at ~/software/relinquishment/plans/0265-interlude-thresholds.md

Execute: Draft threshold sentences for all 7 interludes per the plan's
Per-Interlude Specification section. For each interlude, compose 1-2
sentences that set the reader's mode of attention to inquiry. Follow the
constraints: ≤2 sentences, feels like a stage direction, does NOT name
or disclaim or classify the voice, does NOT re-explain A/B/C. Use the
plan's examples as guidance, not verbatim. Insert each threshold after
the opening \rule, before the \begin{quote}, as non-italic centered
\small text. Run `make dev`. Report the 7 threshold sentences for
co-author approval before shipping.
```

---

*Plan 0265 written by Argus (Auditor), S63. Annealed 5 passes
(HIGH MED MED LOW LOW). Rating 8/10. No drift from Gen's intent.*
