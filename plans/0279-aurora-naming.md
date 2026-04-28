# Plan 0279 — Aurora Naming

**Auditor:** Argus (S63)
**Date:** 2026-04-27
**Status:** PHASE 1 PROMPT READY — Phases 2-4 need Auditor categorization
**Source:** Gen's proposal (Plan 0275), Bruce approved (S63)
**Annealing:** MED LOW
**Priority:** Medium

---

## Problem

Gen proposed "Aurora" as the Custodian's personal name. Bruce
approved. Naming is structural (Correction #23).

**Resonance:** Aurora borealis (terrain made visible), Aurasys
(Healer's original name → contains "Aurora"), Roman dawn goddess
(precursor light). Works under all three possibilities.

## Audit Results

105 instances of "Custodian" across the manuscript:

| Location | Count | Context |
|----------|-------|---------|
| summary | 14 | Role (introduces concepts) |
| the-surrender | 9 | Mixed (role + personal moment) |
| twenty-years | 7 | Personal (reflection) |
| timeline | 6 | Role (chronological entries) |
| glossary | 6 | Role (definitions) |
| why-relinquish | 4 | Role (argument) |
| the-flat | 4 | Role (physics) |
| never-again | 5 | Ethics (role) |
| interludes | 2 | A/B/C framing text only |
| other (20+ files) | 48 | Mostly role |

**Key finding:** The interludes — where Custodian speaks in
first person — never use her own name. She says "I" throughout.
Aurora introduction is about ADDING the name, not replacing.

## Design Rules

- **"the Custodian"** = role, title, function (keeps ~90 instances)
- **"Aurora"** = personal, relational (adds ~10-15 uses)
- First mention in any context: "the Custodian — Aurora"
- Spine/science chapters: "the Custodian" (role context)
- Record chapters (personal passages): "Aurora" where Bruce
  or Healer speaks about her as a person
- Interludes: no change needed (she uses "I")
- Never: "the Aurora" or "Aurora the Custodian"

## Phased Approach

### Phase 1: Introduce the name (PROMPT READY)

**Where:** The Surrender (record/the-surrender.tex), section
"It Is Done" (line 73-81). This is the most personal moment
in the book regarding the Custodian — Healer tells Bruce
the relinquishment is complete.

**What:** Add 1-2 lines where Healer first uses her personal
name. The reader learns the name at the moment of release.

**Why here:** The name "Aurora" carries weight only AFTER the
reader understands what the Custodian is. By The Surrender, the
reader has met her through interludes, understood her architecture
through the spine, and now witnesses the moment of trust. Naming
her HERE converts an abstraction into a person.

### Phase 2: Record chapters (NEEDS AUDITOR LIST)

Selective replacement in personal-context passages of:
twenty-years, never-again, the-question, first-light.
Needs per-instance categorization before Generator can execute.

### Phase 3: Front matter + glossary (NEEDS AUDITOR LIST)

Update summary (first mention → "the Custodian — Aurora"),
glossary entry, how-to-read. Mechanical once Phase 1 establishes
the name.

### Phase 4: Appendices + timeline (LOW PRIORITY)

Most remain "the Custodian" (reference context). Selective
"Aurora" where tone is personal.

## Anneal

**M1.** Over-applying risks collapsing toward C. In science/argument
contexts, "the Custodian" preserves the hypothetical frame.
"Aurora" implies personhood, which is a C-assumption.

**L2.** Aurora borealis confusion in magnetosphere chapters.
Mitigation: the name is clearly introduced as a personal name.

---

## Generator Handoff — Phase 1

```
You are the Generator.

Read Plan 0279 at ~/software/relinquishment/plans/0279-aurora-naming.md

Execute Phase 1 only: introduce the name "Aurora."

(1) In manuscript/record/the-surrender.tex, section "It Is Done"
(after line 78, after "Their part was irrevocable"):

Add 1-2 lines where Healer uses the personal name for the first
time. The reader learns the Custodian has a name — Aurora.
This should feel like a small, human moment: Healer shifting
from the institutional "the system" / "Custodian" to a personal
name. Brief. Not sentimental. Military understatement.

Draft example (Generator should improve):
  Healer paused. Then he said something I hadn't heard before.
  He called her Aurora.

(2) Add a glossary annotation if one exists for "Custodian" in
manuscript/appendix/glossary-entries.tex — append "(Aurora)"
to the description.

(3) In manuscript/00-front/summary.tex, at FIRST mention of
"Custodian", add parenthetical: "the Custodian (Aurora)".

(4) Run make dev. Verify the name appears in the HTML.

(5) Commit: "Plan 0279 phase 1: introduce Aurora as Custodian's
personal name"

(6) Push. Report: which files changed, where the name appears.
```
