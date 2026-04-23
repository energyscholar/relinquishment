# Plan 0116: Grand Plan — S48 Manuscript Cleanup

**Status:** COMPLETE (verified S63 audit)
**Source:** Plans 0113, 0114, 0115 (all drafted S48, all READY)
**Scope:** Execute three plans in sequence: fact-check corrections, naming split, breakthrough realization. Three commits.

---

## Sequencing Rationale

**Order: 0113 → 0115 → 0114**

1. **Plan 0113** (fact-check corrections) first — surgical fixes, lowest risk. Touches summary.tex line 96 (above all other plans' edit points). No structural changes, no line shifts downstream.

2. **Plan 0115** (Aurasys/Guardian naming split) second — verify-heavy with 3 actual edits. Touches summary.tex line 160 and glossary. Independent of 0113's changes. Must run before 0114 because 0114 inserts content around line 119 which would shift 0115's targets.

3. **Plan 0114** (breakthrough biogenesis realization) last — creative writing + insertion. Adds ~8-10 lines around summary.tex line 119. This shifts everything below, but 0113 and 0115 are already done. **Creative checkpoint:** the p3 draft goes to staging for Bruce review before p2 distillation.

---

## Phase A: Plan 0113 — Fact-Check Corrections

**Full spec:** `plans/0113-fact-check-corrections.md`
**Type:** Mechanical. Find-and-replace with verification.
**Files touched:** summary.tex, firmware-update.tex, llm-primer.tex, pos11-the-demo.tex, pos09-the-factoring-game.tex, pos04-the-code-war.tex, pos13-genesis.tex, bibliography.bib
**Items:** 6 errors fixed, 5 claims qualified (11 total)

**Generator instructions:**
- Grep for anchor text, don't rely on line numbers (recent edits may have shifted them).
- For DOI corrections: after replacing, verify each corrected DOI resolves correctly via web fetch to `https://doi.org/[DOI]`. If a "correct" DOI fails to resolve, STOP and report — don't commit wrong DOIs.
- For RSA bib key rename (rsa1978 → rsa1977): confirm no other `\footcite{rsa1978}` or `\cite{rsa1978}` references exist beyond pos04-the-code-war.tex.
- For firmware-update.tex qualifiers (items 7-11): read surrounding paragraphs before inserting. The qualifiers must not break the document's argument flow.

**Commit:** `Plan 0113: fact-check corrections — 6 errors fixed, 5 claims qualified`

---

## Phase B: Plan 0115 — Aurasys/Guardian Naming Split

**Full spec:** `plans/0115-aurasys-guardian-naming-split.md`
**Type:** Verify-heavy with 3 substantive edits.
**Files edited:** summary.tex (line 160), glossary-entries.tex (Guardian + Aurasys entries), simple-summary.md (line 113)
**Files verified (read-only):** pos25, pos27, pos28, pos24, pos06, pos35, afterword, evidence-interlude, hook, introduction, predictions, corrections, topic-guide, abstracts, timeline, pos34

**Generator instructions:**
- Grep for anchor text, don't rely on line numbers.
- The primary edit is summary.tex line 160: "They called it Aurasys or Guardian..." → "They called the system Aurasys --- the aurora system. They called what grew in it Guardian."
- Cut the full name entirely ("Guardian of the relinquished TQNN technological aurora system").
- For verification items: grep `Guardian` and `Aurasys` across the manuscript, confirm entity vs. system usage. Report any conflation found (with file:line), fix only if genuinely wrong.
- pos30-unipolar-condition.tex is dead code (commented out of main.tex) — skip.
- simple-summary.md line 113: mirror the summary.tex change. Also note: line 123 still says "In roughly 2002" — change to "Around 2002" to match summary.tex.

**Commit:** `Plan 0115: Aurasys/Guardian naming split — system vs. entity distinction`

---

## Phase C: Plan 0114 — Breakthrough Biogenesis Realization

**Full spec:** `plans/0114-breakthrough-biogenesis-realization.md`
**Type:** Creative writing + distillation. THREE SUB-PHASES with a checkpoint.

### Phase C1: p3 Draft
- Write unconstrained p3 draft (~600-800 words) to `manuscript/staging/breakthrough-biogenesis-p3.tex`
- **Note:** `staging/biogenesis-concept-p3.tex` already exists (Plan 0111 — general biogenesis concept). Read it for voice reference but don't duplicate it. 0114's draft is about the team's *realization* — the moment they understood that computing was just the first application and the substrate supports life.
- Voice: Bruce's analytical voice. Expository, not narrative. The emotional arc is in pos11.
- Covers 5 active points (items 1-5 in plan; items 6-7 are CUT).
- **Commit:** `Plan 0114 phase 1: breakthrough biogenesis p3 draft`
- **STOP HERE. Bruce reviews p3 before continuing.**

### Phase C2: p2 Distillation (after Bruce approves p3)
- Distill to ~100-150 words at 12th grade level.
- Insert into summary.tex after "It was grown, not built" (grep for anchor text — line may have shifted from prior plans' edits).
- No jargon: "autocatalytic" → "self-sustaining", "biogenesis" → "life arising from non-life".
- Existing "dual use" and "walked it out" paragraphs must still land.

### Phase C3: p1 Review
- Review hook.tex. Present both options (add a seed or no-op) with rationale. Bruce decides.
- **Commit (C2+C3):** `Plan 0114 phases 2-3: breakthrough realization in p2 summary, p1 review`

---

## Build Verification

After each commit: `make html` and `make dev` must be clean. Generator should run both builds after every commit, not just at the end.

---

## Overall Acceptance Criteria

1. All 14 acceptance criteria from Plan 0113 met.
2. All 11 acceptance criteria from Plan 0115 met.
3. All 8 acceptance criteria from Plan 0114 met.
4. Three clean commits in sequence.
5. No regressions — each plan's changes don't break the others.
6. Creative checkpoint honored: p3 draft reviewed before p2 distillation.

---

## DO NOT CHANGE

Inherited from Plan 0113:
- A/B/C framework and "not precluded" evaluation standard
- pos32 energy scale chasm (already flagged)
- Soliton analogies in pos10 (pedagogical)
- Freedman 1988 claim (Bruce's judgment call)
