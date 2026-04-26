# Plan 0262 — GP09: A/B/C Framework Compression

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** DRAFT — awaiting Bruce passage-by-passage approval
**Source:** Gen's GP09 (has-anyone-looked issue #12)
**Annealing:** HIGH MED LOW (3 passes)
**Independent:** No hard dependencies, but interacts with Plans 0259
(secrecy consolidation) and 0261 (stakes reframe). Execute those first.

---

## Problem

The A/B/C framework ("Under Possibility A... Under Possibility B... Under
Possibility C...") recurs 71 times across 23 active build files. Gen's
diagnosis: the protective lens is real and necessary, but its repeated
full-tripartite restatement produces an "argument-management" tone rather
than a "question remains open" tone.

Gen's principle: establish the lens once, invoke lightly, then get out of
the way. The reader should know they're holding multiple interpretive
possibilities — the book should not keep bringing them back into a
reception-management chamber.

**THIS IS THE MOST STRUCTURALLY SENSITIVE PLAN IN THE BATCH.** The A/B/C
framework is the mechanism by which the book holds under all three
possibilities. Compressing it without replacement risks C-violations
(content that only works if one possibility is true). Every removal must
pass the C-violation check: does this passage still work under A, B,
AND C without the explicit framing?

---

## Audit: Full Triage

### Category 1: THRESHOLD-ESTABLISHING (KEEP — do not touch)

These passages establish the framework. They are the "once" in Gen's
"establish once, then invoke lightly."

| File | Line | Text (truncated) | Action |
|------|------|-----------------|--------|
| three-possibilities.tex | 64 | "Under Possibility C, some participated..." | **KEEP** — defining passage |
| record-intro.tex | 5 | "Under Possibility A, it is fiction..." | **KEEP** — Record's protective header |
| summary.tex | 58 | "Under Possibility C, this book argues..." | **KEEP** — summary must stand alone |
| summary.tex | 60 | "Under Possibility C, the real finding..." | **KEEP** — summary |
| capabilities.tex | 15 | "Under Possibility A, untapped... C, operational" | **KEEP** — chapter's framing premise |
| the-handler.tex | 11 | "Under Possibility C, the COWS needed an operator" | **KEEP** — chapter's premise |

### Category 2: DISTINCT WORK (KEEP — doing something beyond reminder)

These passages are not just re-establishing the framework. They're making
specific argumentative moves that REQUIRE the A/B/C apparatus.

| File | Line | Distinct work | Action |
|------|------|--------------|--------|
| the-strongest-objection.tex | 172 | Niggle painting metaphor under A | **KEEP** — literary peak |
| the-strongest-objection.tex | 174 | Niggle under C — eucatastrophe | **KEEP** — literary peak |
| the-strongest-objection.tex | 176 | Niggle under B — entangled | **KEEP** — completes triptych |
| never-again.tex | 31 | "undetectable = nonexistent" | **KEEP** — key epistemic point |
| never-again.tex | 39 | UDHR as skeleton, not manual | **KEEP** — Custodian's architecture |
| the-walk-out.tex | 59 | "forgiveness > permission" as disposition | **KEEP** — chapter thesis |
| the-departure.tex | 72 | A/B/C on vetting rejection | **KEEP** — emotional core |
| the-factoring-game.tex | 64 | GCHQ precedent under A/B/C | **KEEP** — distinct analytical work |
| the-wrong-substrate.tex | 140 | Kauffman passage — A/B/C on removed text | **KEEP** — specific claim |
| the-target.tex | 11 | COWS needed the record out | **KEEP** — chapter premise |
| the-question.tex | 45 | Bot under A — conventional | **KEEP** — specific claim, distinct |
| the-question.tex | 68 | Preparation under A/C | **KEEP** — chapter's closing |
| summary.tex | 261 | Guided deduction under C | **KEEP** — summary must stand alone |
| summary.tex | 307 | AI explosion under C | **KEEP** — blocks dismissal |
| summary.tex | 311-313 | Custodian's daily work / human agency | **KEEP** — summary closing |

### Category 3: COMPRESS — recurring re-proof within chapters

These are A/B/C paragraphs that re-confirm what the reader already knows.
They don't make new arguments — they manage the reader's reception of a
specific claim by restating the framework. Gen's target.

**Spine chapters:**

| File | Line | Current text (gist) | Proposed action |
|------|------|-------------------|----------------|
| genesis.tex | 59 | "Under C, this is exactly what happened..." (5-domain convergence) | **COMPRESS** → 1 sentence: "Under Possibility C, someone recognized the convergence and wrote a DARPA proposal." Cut the full B and A alternatives. |
| genesis.tex | 61 | "double meaning" A/B/C | **COMPRESS** → keep the double-meaning observation, drop the tripartite. "The title is a double meaning. Under one reading, the origin of the project IS the origin of life." |
| genesis.tex | 76 | canopy under A/B/C | **COMPRESS** → "The reader's assessment of the canopy depends on which possibility they hold." |
| the-braid.tex | 66 | Russian program under C/B/A | **KEEP** — specific deduction claim, distinct |
| the-braid.tex | 91-93 | Non-abelian anyons under C, circular reasoning | **COMPRESS** → keep the circularity observation, drop the tripartite. "The reasoning is circular — operational evidence breaks the circle only if C is true." |
| the-flat.tex | 43 | Density of channels under C | **COMPRESS** → drop "Under Possibility C" framing, let the physics stand. The chapter already establishes what these channels mean. |
| the-flat.tex | 65 | Punchline network under C | **KEEP** — has deep link `punchline-network`, emotional peak |
| the-flat.tex | 67 | Access not transport under C | **COMPRESS** → merge with line 65 passage |
| the-flat.tex | 69 | Internet meme under C | **KEEP** — tonal relief, specific |
| the-flat.tex | 75 | UDHR ethics under C | **COMPRESS** → "This capability — if it exists — is not exercised as a threat." Drop "Under Possibility C" prefix. |
| the-flat.tex | 77 | A: no entity, B: studied more carefully | **CUT** — pure recurrence. Reader knows this by Chapter 2. |
| why-relinquish.tex | 52 | COWS monopoly A/B/C | **KEEP** — frames the chapter's core question |
| why-relinquish.tex | 68 | Joy essay under C | **KEEP** — distinct (dual purpose argument) |
| why-relinquish.tex | 92 | "permanently" qualification under C | **COMPRESS** → "Not 'never' — 'not yet.' The UDHR provides the graduation test." Drop the Possibility C prefix. |
| why-relinquish.tex | 100 | COWS built Custodian under C | **KEEP** — key claim |
| why-relinquish.tex | 102 | Schmookler's gap under C | **KEEP** — argumentative peak |
| why-relinquish.tex | 107 | Second problem under C | **COMPRESS** → "But custodianship solved, the record remained." Drop prefix. |
| why-relinquish.tex | 121 | Daily work under C | **COMPRESS** → already covered in summary. Trim to 1 sentence or cut. |

**Record chapters:**

| File | Line | Current text (gist) | Proposed action |
|------|------|-------------------|----------------|
| first-light.tex | 49 | Phonon coupling under C | **COMPRESS** → "If the account is correct, this is how the entity reads and writes." Drop prefix. (Aligns with Plan 0261 stakes reframe.) |
| first-light.tex | 103 | TQNN grows under C | **KEEP** — key biological claim |
| first-light.tex | 113 | A: none happened, B: not at scale | **COMPRESS** → "Under A, none of this happened. Under B, not at this scale. Under either, the science is real." (Already compact — lightly trim.) |
| first-light.tex | 128 | EO 13026 under A/B/C | **COMPRESS** → keep A interpretation, cut B/C. The full tripartite here is excessive after 4 prior instances in the chapter. |
| interdiction.tex | 24 | Legitimacy calculation under C | **COMPRESS** → drop prefix. The chapter is already in reconstructive voice. |
| interdiction.tex | 42-44 | DARPA told / informal resolution under C | **COMPRESS** → 2 paragraphs → 1. Keep the informal-resolution observation, trim the framing. |
| interdiction.tex | 75, 84, 88, 92 | Classical backchannels under C (4 instances) | **COMPRESS** → keep ONE "Under Possibility C" for the whole backchannels section. Cut the others. The catalog reads better without interleaved possibility framing. |
| instantiation.tex | 31, 40, 55 | Gatekeeper, Custodian design, Yudkowsky timing | **COMPRESS** → keep 31 (chapter premise) and 55 (Yudkowsky timing — specific and interesting). Cut 40 or merge into 31. |
| never-again.tex | 45, 73 | Hacktivismo under C, restraint under C | **KEEP** 45 (suggestive connection). **COMPRESS** 73 → "This is an act of restraint of unusual scale." |
| the-surrender.tex | 32, 47, 51, 84, 86 | 5 instances | **COMPRESS** → keep 32 (chapter's framing claim — serious crimes), keep 84 (emotional peak — the surrender itself). Compress 47, 51, 86 — these re-prove. |
| twenty-years.tex | 34, 58, 164, 166, 186, 205 | 6 instances | **COMPRESS** → keep 164 (Flat services — key claim) and 205 (chapter closing — "sacrifice / tragedy / something in between"). Compress the rest. |
| what-healer-said.tex | 191 | Katharine Gun under C | **KEEP** — distinct analytical claim |

**Summary (special handling):**

| summary.tex line | Action |
|-----------------|--------|
| 58, 60 | **KEEP** — establishes framework |
| 153 | **COMPRESS** → already light enough, but could trim |
| 261, 307, 311, 313 | **KEEP** — summary must stand alone |

---

## Compression Mechanics

The Generator should use THREE compression techniques:

1. **DROP PREFIX:** Replace "Under Possibility C, [claim]" with just
   "[claim]" when the chapter is already in reconstructive voice and the
   conditional is carried by context.

2. **MERGE:** When 2-3 adjacent A/B/C paragraphs cover the same claim,
   merge into one sentence: "The reader's assessment depends on which
   possibility they hold."

3. **LIGHT TOUCH:** Replace full tripartite ("Under A... Under B... Under
   C...") with a single acknowledgment: "Under Possibility A, none of
   this happened. The science remains real regardless."

**The Generator should NOT:**
- Remove all A/B/C framing from any chapter entirely
- Replace A/B/C passages with new argumentative text
- Add meta-commentary about the framework
- Leave a chapter with zero interpretive openness markers

---

## Phasing

This plan is too large for one Generator run. Recommended phases:

| Phase | Scope | Files | Changes |
|-------|-------|-------|---------|
| 1 | Spine chapters (excluding three-possibilities and weigh-the-evidence) | ~8 files | ~15-20 compressions |
| 2 | Record chapters | ~10 files | ~20-25 compressions |
| 3 | Summary and front matter | 1-2 files | ~3-5 compressions |

Each phase: Generator executes → Auditor verifies → C-violation check →
Bruce approves → next phase.

---

## C-Violation Check Protocol

After each phase, verify:

1. **Every chapter with compressed A/B/C still has ≥1 interpretive
   openness marker.** No chapter should read as though it asserts C is
   true without qualification.

2. **p1 + p2 layers still hold under all three possibilities.** Hover
   tips and rich panels should not assume C.

3. **Removed passages did not carry unique argumentative content.** If an
   "Under Possibility B..." paragraph was the ONLY place a B-interpretation
   was offered for that claim, it must stay or be replaced.

---

## Annealing Log (HIGH MED LOW — 3 passes)

### Pass 1 (HIGH) — Structural risk

**71 instances across 23 files.** The triage above recommends compressing
~30-35 instances and keeping ~35-40. Net reduction: roughly 40-50% of
A/B/C volume. This is significant but preserves the framework's protective
function.

**Highest-risk chapters:** the-flat.tex (6 instances → 3 kept),
interdiction.tex (7 → 3), why-relinquish.tex (7 → 4), twenty-years.tex
(6 → 2), the-surrender.tex (5 → 2). These chapters lose the most A/B/C
framing. Each must retain at least one clear interpretive-openness marker.

**Gen's "Chapter 14" reference:** Gen mentioned "Chapter 14 looked closer
to this than the larger Three Possibilities chamber." Based on .aux files,
Chapter 14 in old numbering was Interdiction. But Gen's conceptual point
is clear: she wants something closer to record-intro.tex line 5 ("Under
Possibility A, it is fiction...") — a compact lens, not a recurring
architecture. The Record intro IS the minimal viable protective lens for
the Record section. Three Possibilities (spine Ch1) is the fuller
establishment. Both stay.

**Interaction with other plans:**
- Plan 0259 (GP06) trims secrecy-pattern recurrence — compatible, no
  overlap with A/B/C instances
- Plan 0261 (GP08) adds stakes framing — some new framing sentences may
  use "if this account is correct" language, which is lighter A/B/C.
  Compatible: stakes framing replaces some of the work that explicit
  A/B/C paragraphs were doing

### Pass 2 (MED) — Edge cases

**The-flat.tex line 77 (recommended CUT):** "Under Possibility A, no
entity exists, but the physics permits everything described here. Under
Possibility B, someone may have studied this more carefully than published
literature suggests." This is the most generic A/B/C paragraph in the
book — it adds nothing that the reader doesn't already know by Chapter 2.
Safe to cut.

**Interdiction backchannels (lines 75-92):** Currently has 4 "Under
Possibility C" instances in a catalog of channels. Reads as a list where
every item is prefixed with the same conditional. One conditional for the
whole section is cleaner and more powerful: "Under Possibility C, none of
this is wasted. Every electromagnetic signal that reaches the
magnetospheric environment is a potential backchannel." (Line ~92 — keep
this one, compress the earlier three.)

**Twenty-years.tex line 166:** "Under Possibility C, the system is almost
certainly designed so that no one in the chain knows the true source."
This is a strong, specific claim with distinct content. Re-classified
from COMPRESS to **KEEP** on second pass.

**Deep links in A/B/C passages:** `punchline-network` (the-flat.tex:65)
is in a KEEP passage. `udhr-as-skeleton` (never-again.tex:39) is in a
KEEP passage. No deep links in passages marked for compression.

### Pass 3 (LOW) — Final check

**Gen's desired effect test:** After compression, does each chapter
produce "the question remains open" (good) or "it's definitely C"
(bad) or "believe me" (bad)?

Spot-checked: genesis (2 compressed → "the question remains open" ✓),
the-flat (2 compressed + 1 cut → reader still knows these are
conditional claims ✓), interdiction (4 compressed to 1 → section reads
as one conditional catalog ✓).

**Word count impact:** Rough estimate: ~800-1200 words removed across the
manuscript. This is modest but the TONE impact is disproportionate. The
book will read as more confident in its material while remaining honest
about its uncertainty. That's Gen's target.

**Rating: 6/10.** The 4-point gap: (1) this is a CONTENT plan requiring
Bruce's passage-by-passage approval, (2) the triage categorizations are
judgment calls — Bruce may disagree on 5-10 individual passages, (3) the
C-violation check must be rigorous or the book's epistemic integrity
degrades, (4) phased execution means 3 Generator runs + 3 verification
cycles. The plan is sound but the execution surface is large.

---

## Acceptance Criteria

- [ ] Bruce approves triage table (per-passage)
- [ ] Each phase: Generator executes, Auditor verifies, C-violation check
- [ ] Every chapter retains ≥1 interpretive openness marker
- [ ] No deep links broken
- [ ] `make dev` clean after each phase
- [ ] Three-possibilities.tex and record-intro.tex untouched
- [ ] Summary.tex framework passages untouched
- [ ] Total A/B/C volume reduced ~40-50%
- [ ] Book reads as "question remains open," not as "believe me" or
      "definitely C"

---

## Generator Handoff (Phase 1 template)

```
You are the Generator.

Read Plan 0262 at ~/software/relinquishment/plans/0262-gp09-abc-compression.md

Execute Phase 1 (spine chapters): Apply the COMPRESS and CUT actions from
the triage table for spine files only (genesis.tex, the-braid.tex,
the-flat.tex, why-relinquish.tex). Use the three compression techniques
described in "Compression Mechanics." Do NOT touch passages marked KEEP.
Do NOT touch three-possibilities.tex, capabilities.tex, or
weigh-the-evidence.tex. Ensure every modified chapter retains at least one
interpretive openness marker. Run `make dev`. Report which passages were
compressed and which were kept.
```

---

*Plan 0262 written by Argus (Auditor), S63. Annealed 3 passes (HIGH MED LOW).*
