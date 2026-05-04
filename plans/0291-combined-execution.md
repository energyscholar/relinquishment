# Plan 0291: Combined Execution — Plans 0288/0289/0290

**Status:** READY TO EXECUTE
**Author:** Auditor (Argus S65)
**Origin:** S65 annealing of Plans 0288 (strategic review), 0289 (taxonomy + pacing), 0290 (pictogram system)
**Annealed:** HIGH → MED → LOW across 3 passes

---

## Overview

Four phases executing the annealed outputs of Plans 0288-0290. Each phase is one Generator shell, one commit. Detail files in `plans/prompt-{A,B,C,D}-*.md`.

## Idempotency

All four prompts are idempotent. Each starts with a guard that checks whether the phase has already been applied. If fully applied: exit with no changes. If partially applied: fix only the missing parts. Safe to run twice.

All prompts include: absolute paths, branch state (main), website push after build, manifest-first ordering, C-violation checks where applicable. Per Handoff Preflight Checklist (bruce-se-methodology.md, S65).

## Decisions Made (S65 Annealing)

| Decision | Resolution | Rationale |
|----------|-----------|-----------|
| Plan 0288 | COMPLETE (analysis only) | Its output is 0289 + 0290. No execution needed. |
| Taxonomy placement | Before "Not Aliens" | Chapter keeps dramatic "Nobody has looked." ending |
| Taxonomy badge | tech-borderline (ⓘ) | Theoretical framework, not established physics |
| First-occurrence badge note | Yes | One-line explanation on first tech-section |
| Pictogram Tier 2 (⚙⎈⊞) | CUT | Only 9 occurrences total. Revisit if Tier 1 works. |
| Legend panel | CUT | If teaching sequence works, legend unnecessary |
| The Question 4-symbol convergence | Header signature only | Avoids density jump in teaching progression |
| Fallback injection (no hover anchor) | Skip with warning | Don't inject without semantic anchor point |
| Summary back-half trimming | DEFERRED | Let restructure land, Bruce reviews, then trim |
| Taxonomy C-violation | None — categories not claims | Valid under all three possibilities |

## Execution Order

```
Phase A → Phase B (review gate) → Phase C (regression gate) → Phase D (gated on C)
```

| Phase | File | Risk | Commit gate | Build |
|-------|------|------|-------------|-------|
| A — Mechanical fixes | prompt-A-mechanical.md | LOW | Auto | make html |
| B — Content | prompt-B-content.md | MEDIUM | Bruce reviews diff | make dev |
| C — Symbol injection | prompt-C-symbols.md | MEDIUM-HIGH | ⬡ count = 14 | make html |
| D — Combinations | prompt-D-combinations.md | MEDIUM | Phase C working | make html |

## Phase A: Mechanical Fixes

Badge CSS (bigger/brighter ✔, wider border), badge tooltip update, first-occurrence explanation, hook pacing fix (split line 30), concept symbol CSS (7-symbol block), concept-symbols.yaml manifest creation.

**Handoff:**
```
You are the Generator.
Read ~/software/relinquishment/plans/prompt-A-mechanical.md and execute all 6 tasks.
Read Plan 0290 in plans/0290-pictogram-language-system.md for the CSS block (lines 286-347) and YAML manifest (lines 85-228).
Build with make html. Verify ⬡ count = 14.
One commit.
```

## Phase B: Content

Summary restructure: domestication beat + structural break + Kauffman bridge expansion + T3 as seed. Taxonomy section in Wrong Substrate (before "Not Aliens", tech-borderline).

**Handoff:**
```
You are the Generator.
Read ~/software/relinquishment/plans/prompt-B-content.md and execute both tasks.
Read Plans 0288 and 0289 in plans/ for full context.
Build with make dev. Show git diff. Do NOT commit — I review first.
```

## Phase C: Symbol Injection

Generalize inject_concept_symbols() for 3 hover-anchored concepts: flat (⬡), emergence (◈), custodian (◉). Same logic as existing flat injection, extended.

**Handoff:**
```
You are the Generator.
Read ~/software/relinquishment/plans/prompt-C-symbols.md and execute.
Regression gate: ⬡ count must remain 14 after changes.
Build with make html. Report all concept counts. One commit.
```

## Phase D: Combinations + Header Signatures

Two combination moments (⬡◈ in Wrong Substrate, ◈◉ in Instantiation). Chapter-header symbol clusters in collapsed summaries.

**Handoff:**
```
You are the Generator.
Read ~/software/relinquishment/plans/prompt-D-combinations.md and execute.
Prerequisite: Phase C committed and working.
Build with make html. Verify combinations are adjacent. One commit.
```

## Remaining Work (not in this plan)

From Plan 0288's gap analysis, still unaddressed:
- T7 (services) visibility
- F-religious early theological disarm
- Convergence visualization (five pillars)
- Coupling question in pop-science voice
- Reader HTML metadata update
- Pictogram Tier 2 (⚙⎈⊞) — revisit after Tier 1 assessment
- Summary back-half redundancy trimming (after Phase B review)
