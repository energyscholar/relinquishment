# Plan 0186 — Predictions: review, tighten, insert as prose

**Type:** Three-phase plan. Phase 1 = Generator audit of existing predictive language across the manuscript (produces a research artifact, not a book edit). Phase 2 = Auditor + Bruce tightening pass (this is a planning cycle, not a Generator task). Phase 3 = Generator inserts final tightened predictions as prose into summary.tex. Halt-and-report at any unclear candidate.

## Context

9-reader low-anneal panel identifies Chen's core residual: the book doesn't make a **dated falsifiable prediction of its own**. The book implicitly touches several empirical claims (MS life signature, room-temp TQC, guided-deduction pedagogy as observable behavior, silence-gap argument) but none are consolidated as testable forecasts with dates and failure criteria.

Bruce (2026-04-13): review what we already have, improve and tighten, then promote to prose.

**Bigger than a one-paragraph insertion.** Predictions are a new book-level move — they commit the book to falsifiable claims under A/B/C. Worth doing carefully.

## Phase 1 — Audit existing predictive language (commit: research artifact only)

**Generator task.** No book edit. Output is a research document.

**Sweep scope:**

```
manuscript/00-front/*.tex
manuscript/track-1-confession/*.tex
manuscript/track-2-testament/*.tex
manuscript/record/*.tex
manuscript/appendix/*.tex
manuscript/spine/*.tex
```

**Grep patterns (union, then dedupe):**

```
grep -rn -iE "\b(predict|prediction|forecast|expect|will be|by (19|20)[0-9]{2}|falsif|testable|detectab|signature|anomal)" manuscript/ --include="*.tex"
```

For each hit, classify:

| Class | Definition | Example |
|---|---|---|
| **P-dated** | Already has a year + failure criterion | "...detectable by 2030, else treat C as falsified" |
| **P-implicit** | States a testable claim but no date/failure mode | "...the Flat can support intelligent life" |
| **P-rhetorical** | Uses predictive word but not actually a prediction | "expect the reader will find..." |
| **P-backward** | Describes a past event as predicted (history, not forecast) | "Healer predicted this in 2003" |

**Output artifact:** `research/predictions-audit-2026-04-13.md`. Structure:

- Summary: total hits, counts per class, top surfaces (files).
- Table per P-implicit and P-dated hit: file:line, current phrasing (verbatim), classification, auditor-notable flags (e.g., C-violation risk, bare claim, under-specified).
- **No edits proposed yet.** This is raw catalog.

**Acceptance (Phase 1):**

1. Research artifact exists with ≥ the grep's hits, classified.
2. Zero manuscript files modified.
3. No commit required if repo policy keeps research/ untracked; otherwise single commit `Plan 0186 phase 1: predictions audit`.

**Halt-and-report:** if grep returns <10 hits or >500 hits, flag pattern calibration issue; don't press on with a junk catalog.

## Phase 2 — Auditor + Bruce tightening (no Generator)

**Planning cycle, not execution.** Auditor reads the audit artifact, identifies 3-7 candidate predictions worth promoting. For each candidate:

- Current phrasing (from audit).
- Proposed tightened phrasing with explicit year + falsification criterion.
- Which persona it addresses (Chen, Arjun, Reeves, etc.).
- A/B/C scope (does it hold under A? only under C?).
- Risk (does the tightened claim overreach? does it commit the book to something Bruce isn't comfortable defending?).

Auditor surfaces the short-list to Bruce via `AskUserQuestion` with 4-6 options (pick N to promote, drop N, tighten N further).

Bruce picks. Auditor writes final phrasing for each promoted prediction into `plans/0186-predictions-final.md` — a small sub-artifact that Phase 3 Generator reads verbatim.

**No commit.** Phase 2 outputs a plan sub-artifact consumed by Phase 3.

## Phase 3 — Insert final predictions as prose (commit 2)

**Generator task.** Reads `plans/0186-predictions-final.md`. Inserts the predictions into `manuscript/00-front/summary.tex` at the insertion point Bruce specifies in Phase 2 (options: dedicated "Predictions" subsection; interleaved with A/B/C framing; end of summary as a "Commitments" close; etc.).

**Style constraints:**

- Prose, not a bullet list. The book is a prose document.
- Each prediction: year + what's expected + failure date + failure interpretation. Short.
- Under Possibility~X labels where a prediction is possibility-specific (mirrors the 0183 C-violation fix).

**Acceptance (Phase 3):**

1. Predictions block present in summary.tex at the location Phase 2 specified.
2. Each prediction contains: a year, a test, a failure criterion.
3. `grep -nE "\b20[2-4][0-9]\b" manuscript/00-front/summary.tex` shows the new prediction years.
4. `make` HTML build clean.
5. Word count increases by the expected token count (Phase 2 specifies target).

**Commit 2:** `Plan 0186 phase 3: insert dated falsifiable predictions into summary.tex`

## Re-test (Auditor, after Phase 3 lands)

Run 9-reader panel at **low-medium anneal** (between low and medium). Probes:

- Chen: expect ⚠ → ✅.
- Doctorow: watch for "conspiracy smell" if predictions sound too specific about Custodian.
- Rachel: watch for dystopian-flavor if failure language reads doom-ish.
- Reeves: watch for philosophy-of-science nit on falsification framing.

Auditor reports side-by-side delta vs low-anneal baseline (668f1ba).

## Build + push

After Phase 3 commit lands clean, push per `feedback-build-to-website.md`.

## Rollback

Phase 3 is one commit. `git revert` reverts all prediction prose cleanly. Phase 1 artifact stays (useful regardless).

## Handoff report (Generator, per phase)

**Phase 1 (4 lines):**
1. Grep total hit count.
2. Class counts (P-dated / P-implicit / P-rhetorical / P-backward).
3. Path to saved research artifact.
4. Any surprises (e.g., prediction found in unexpected file).

**Phase 3 (4 lines):**
1. Commit SHA.
2. Acceptance grep + word-count results.
3. Build result.
4. Push result + URL if pushed.

## Notes

- Arjun's citation-tooltip friction is NOT in this plan. Separate future plan when ready.
- Don't conflate predictions with claims the book already makes. Predictions add *dates and failure criteria* to claims — that's the new thing.
- Resist the temptation to promote every testable claim. 3-5 is probably right. More than 7 dilutes; fewer than 3 may not satisfy Chen.
