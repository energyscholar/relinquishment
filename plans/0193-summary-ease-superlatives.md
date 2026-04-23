# Plan 0193 — Ease superlatives in summary.tex

**Auditor:** Argus
**Date:** 2026-04-13
**Role:** Auditor
**Baseline:** HEAD `2c28604` (eigenvalue42 shipped)
**Target tag on success:** none (micro-plan, single commit)

---

## 1. Premise

Post-ship reader-panel scoring (Tier-0, 9 personas) flagged that `summary.tex` uses the phrase "most powerful" five times (L83, L115, L218, L301, L307). Each instance sits semantically adjacent to attributes religious readers (Pastor Mike, Amir, Yusuf) reserve for God. The phrase is a single rhetorical tic, not load-bearing prose — the superlative scales up without adding meaning a comparative can't carry.

Bruce: "I'm not attached to phrase 'most powerful'. Maybe it's language I want to remove anyway... can't we just ease back from the superlative? Message stays the same ... maybe transmits better."

Scope is bounded: five single-line edits, no structural changes, message preserved.

---

## 2. Acceptance criteria

1. All five instances of "most powerful" in `manuscript/00-front/summary.tex` replaced with softer phrasings per the disposition table below.
2. Sentence structure and surrounding context preserved — only the superlative phrase changes.
3. `make dev` clean.
4. `grep -c "most powerful" manuscript/00-front/summary.tex` returns `0`.
5. No changes to any file other than `manuscript/00-front/summary.tex` and (if rebuilt) `docs/`.
6. Single commit: `Plan 0193: ease superlatives in summary.tex`.

---

## 3. Disposition table

| # | Line | Current phrase | Replacement |
|---|---|---|---|
| 1 | L83 | `the most powerful weapon ever created` | `an extraordinary weapon` |
| 2 | L115 | `One had built the world's most powerful parallel computer` | `One had built a uniquely capable parallel computer` |
| 3 | L218 | `voluntarily placing the most powerful technology ever created beyond the reach of any person or government` | `voluntarily placing a technology of this magnitude beyond the reach of any person or government` |
| 4 | L301 | `voluntarily gave up the most powerful technology ever created` | `voluntarily gave up a technology of extraordinary power` |
| 5 | L307 | `The most powerful custodian on Earth mostly does IT infrastructure` | `Earth's most capable custodian mostly does IT infrastructure` |

### Exact Edit tool strings

**Edit 1 (L83):**
- OLD: `That machine would be the most powerful weapon ever created.`
- NEW: `That machine would be an extraordinary weapon.`

**Edit 2 (L115):**
- OLD: `\item One had built the world's most powerful parallel computer`
- NEW: `\item One had built a uniquely capable parallel computer`

**Edit 3 (L218):**
- OLD: `This act --- voluntarily placing the most powerful technology ever created beyond the reach of any person or government --- is called \hovertip{relinquishment}.`
- NEW: `This act --- voluntarily placing a technology of this magnitude beyond the reach of any person or government --- is called \hovertip{relinquishment}.`

**Edit 4 (L301):**
- OLD: `A group of people voluntarily gave up the most powerful technology ever created.`
- NEW: `A group of people voluntarily gave up a technology of extraordinary power.`

**Edit 5 (L307):**
- OLD: `The most powerful custodian on Earth mostly does IT infrastructure, invisible to the operators who pay for it.`
- NEW: `Earth's most capable custodian mostly does IT infrastructure, invisible to the operators who pay for it.`

---

## 4. Execution

1. Apply all 5 edits via Edit tool on `manuscript/00-front/summary.tex`.
2. Run `make dev` — must compile clean.
3. Verify `grep -c "most powerful" manuscript/00-front/summary.tex` returns `0`.
4. Verify `grep -n "extraordinary\|uniquely capable\|of this magnitude\|most capable" manuscript/00-front/summary.tex` returns 5 hits on lines 83, 115, 218, 301, 307 (±1 for any whitespace drift).
5. Commit: `Plan 0193: ease superlatives in summary.tex`.
6. Report to Auditor: diff summary, build status, grep verification.

Do NOT rebuild `docs/` in this commit — Bruce will trigger website rebuild separately if/when he wants the public HTML updated.

---

## 5. Rollback

Single commit — revert via `git revert` if Auditor rejects on review.

---

## 6. Handoff prompt

> You are the Generator. Read `~/software/relinquishment/plans/0193-summary-ease-superlatives.md`. Apply the 5 Edit operations from §3 to `manuscript/00-front/summary.tex`, verify `make dev` is clean, verify `grep -c "most powerful" manuscript/00-front/summary.tex` returns 0, and commit as `Plan 0193: ease superlatives in summary.tex`. Report diff summary + build status + grep output.
