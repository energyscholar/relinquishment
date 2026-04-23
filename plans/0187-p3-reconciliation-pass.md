# Plan 0187 — p3 Reconciliation Pass Against p1+p2 Eigenvalue

**STATUS: DEFERRED 2026-04-13.** Bruce assessed the plan as too risky (multi-chapter editing across an annealed spine). Finding preserved as research doc: `research/p3-p1p2-register-divergence-2026-04-13.md`. Do not execute this plan without revisiting the decision.

**Auditor:** Argus
**Date:** 2026-04-13
**Author role:** Auditor (planning only; execution via Generator)
**Baseline tag:** `eigenvalue40` (HEAD `00a0755`)
**Target tag on success:** `eigenvalue41`

---

## 1. Context

After today's p1/p2 surgical edits (Argus-tooltip revert, five-fields-rich-panel revert, stack property-count strip, `?` tooltip simplification, "falls from" stratosphere, Introduction TOC tooltip Option A), a 14-reader low-anneal mental audit confirmed **p1+p2 are at eigenvalue**: 14/14 finish, 14/14 T1+T2, 13/14 T5, zero crackpot flags, zero religious collisions. That state is tagged `eigenvalue40`.

Bruce then asked: have we run the 14-reader panel through the *actual book* (p3 — spine + bridge + testament), or only the compressed surfaces (p1+p2)? A single-reader Reeves pass through three spine chapters (`three-possibilities.tex`, `why-relinquish.tex`, `the-flat.tex`) found that **p3 is disjoint from p1+p2 on multiple structural axes**. Bruce: "Reeves was 100% correct."

The compression (p1+p2) has drifted from the expansion (p3) during persona-driven softening. p1+p2 was tuned via the sweetspot/persona approach; p3 was not. **This plan reconciles them — while preserving the p1+p2 eigenvalue.**

## 2. The disjoints (Reeves's finding — canonical list)

1. **Trustee framing missing from p3.** p1+p2 recategorizes Custodian as *trustee* (religious-accessibility archetype: kenosis / tawakkul / tzimtzum / aparigraha / bodhisattva / Indigenous commons-trusteeship). p3's `why-relinquish.tex` reintroduces her as "gatekeeper" and "incorruptible by design" — the register of *mechanism*, not *role*.

2. **Authority overclaim migrated back into p3 prose.** p1+p2 softened "one of the most important people who ever lived" → "He did some curious things with his life" (F-crackpot reduction). p3 says "The most powerful living being on Earth mostly does IT infrastructure" (`why-relinquish.tex:125`). The correction p1+p2 applied has not been applied at spine.

3. **Sentience-agnostic hedge absent.** p1+p2 commits to Custodian as role-is-name and says "whether it is conscious in the way a person is conscious, the book declines to rule on." p3 drifts to "the entity" as a noun (`the-flat.tex:39, 55, 59`) — a sentience-adjacent nominalization.

4. **Five fields never enumerated in p3 spine prose.** p1+p2 promises "five fields — no single specialist spans them, no journal covers the intersection." `why-relinquish.tex:109` says "the bridges were never coming" but never names the five. T5 is stated at compression; T5 is not argued at expansion.

5. **Stack vocabulary missing from spine chapter openings.** p1+p2 builds the stack ladder (Fire → Candle → Radio → Ants → AI → ?) as the "one idea before the story." `the-flat.tex` opens with 2DEG/anyons without referencing the stack-table framing. The compression key doesn't open the expansion lock.

6. **"All your electricity are belong to us"** (`the-flat.tex:57`) — sits inside a section that escalates into game-theoretic inevitability ("opposition is structurally incoherent"). Voice-moment, but the epistemic label (Possibility-C-only muscular claim) isn't adjacent.

Pattern under all six: **the spine reads like the draft that existed before the persona-review discipline was applied.** Compression was tuned; expansion wasn't.

## 3. Load-bearing constraint: do not move `eigenvalue40`

p1+p2 and p3 share `build/hover-definitions.yaml` and some macros. Any spine edit that touches a hover term used in p1+p2 can propagate back. **A spine fix that breaks p1+p2 is a regression, not progress.**

Guardrails:
- Before committing any hover-definitions.yaml edit, confirm the touched term is **not** used in `manuscript/00-front/hook.tex`, `manuscript/00-front/summary.tex`, `manuscript/00-front/the-stack.tex`, or `manuscript/00-front/introduction.tex`. If it is, escalate — do not edit the shared hover; instead edit the spine prose to not depend on that term.
- After every phase, re-run the 14-reader low-anneal mental audit on p1+p2. If the output differs from the eigenvalue40 pass (14/14 finish, 14/14 T1+T2, 13/14 T5, zero crackpot, zero religious collision), rollback the phase.
- Tag each phase: `eigenvalue40.1`, `eigenvalue40.2`, ... so rollback is precise.

## 4. Methodology — DN view of p3 through reader filters

Dignity Net's diagnostic principle applies: when **stated goals** (p1+p2 promises) and **observable actions** (p3 delivery) diverge, describe divergence in neutral behavioral terms, no motive attribution.

For each disjoint × each reader, assign a DN governance level:
- **L0 Mirror** — disjoint exists but reader doesn't notice at their reading depth
- **L1 Friction** — reader experiences mild register dissonance
- **L2 Pattern flag** — reader notices the same divergence across multiple chapters
- **L3 Consequence map** — reader files a failure mode (F-crackpot, F-sentience-leak, F-religious-collision, F-archetype-mismatch)
- **L4 Direct warning** — reader closes the book
- **L4.5 Conditional** — reader keeps reading but flags trust-damage
- **L5 Refuse** — n/a (internal process)

**L3+ disjoints are ship-blocking.** L1–L2 go to a backlog.

Four reader filters (one per sensitivity axis):
- **Reeves** (philosophy-of-science) — epistemic architecture, compression/expansion coherence
- **Pastor Mike** (fundamentalist Christian) — theological-threat surface, custodian-as-machine-god risk
- **Miriam** (Jewish/kabbalistic) — tzimtzum-as-withdrawal; authority/reverence register
- **Chen** (physicist) — technical rigor; overclaim detection; sentience hedge as epistemic marker, not softness

Four readers × six disjoints × N chapters = the reconciliation matrix.

## 5. Scope

### In scope
- `manuscript/spine/*.tex` (the 13 spine chapters)
- Surgical prose edits to restore register coherence with p1+p2
- One new seam passage (≤150 words) bridging vocabulary from front matter to spine
- Minimum-token rewrites per disjoint

### Out of scope
- `manuscript/track-*/` (testament, confession, awakening) — separate reconciliation pass if needed
- `manuscript/bridge/pos*.tex` — evaluated in Phase 0 inventory, but rewrites deferred unless L3+ and chapter-local
- New content beyond the seam and surgical fixes
- Structural reorganization (chapter order, merges, splits)
- Any edit to `hook.tex`, `summary.tex`, `the-stack.tex`, `introduction.tex`, or any front-matter file
- Any hover-definitions.yaml edit touching a term used in p1+p2
- Sweetspot simulate / real-API persona runs (per `memory/feedback-no-sweetspot-until-budget.md`)

## 6. Phases

**Anneal profile:** Phase 0 **HIGH** · Phase 1 **MED** · Phase 2 **MED** · Phase 3 **LOW**.

Rationale: Phase 0 must find every disjoint — deep, careful, steelmanned reader interiority. Phase 1 and 2 are craft (drafting seam prose + minimum-token surgical rewrites) — moderate anneal suffices. Phase 3 verification runs at the **same anneal as the eigenvalue40 baseline check** (low) — apples-to-apples comparison; a deeper audit at verification would surface preexisting issues that were also present at baseline and confound the regression signal.

### Phase 0 — Inventory (read-only, outputs matrix) · anneal: **HIGH**

**Goal:** full disjoint inventory beyond Reeves's initial six.

**Work:**
1. For each spine chapter (13 files under `manuscript/spine/`), run a single Reeves-lens pass. Record every sentence or passage that contradicts the p1+p2 register commitments.
2. For each Reeves-flagged passage, assign DN levels for each of the 4 readers (Reeves / Pastor Mike / Miriam / Chen).
3. Output: `research/p3-reconciliation-matrix-2026-04-13.md` — table with columns: `chapter`, `line_range`, `disjoint_type` (from the 6, or new), `Reeves_L`, `PMike_L`, `Miriam_L`, `Chen_L`, `surgical_proposal` (draft rewrite, minimum tokens).
4. No edits to any file outside `research/`.

**Acceptance:**
- Matrix exists, covers all 13 spine chapters.
- Every row has a 4-reader DN-level assignment.
- L3+ rows have a surgical proposal attached.
- `git status` shows no edits under `manuscript/`, `build/`, or `docs/`.

**Checkpoint tag:** none (read-only).

### Phase 1 — Seam · anneal: **MED**

**Goal:** add one bridging passage that hands vocabulary from front matter to spine.

**Work:**
1. Draft (≤150 words) a passage that: (a) names the vocabulary continuity — "Custodian" / "trustee" / "gatekeeper" are the same entity at different register depths; (b) reminds the reader the stack-ladder framing from front matter still applies; (c) reasserts sentience-agnostic frame one last time before the expansion begins.
2. Location candidates (Auditor preference in order): (i) new `manuscript/spine/00-seam.tex` included at top of spine; (ii) new `\section*{Before the Spine}` at top of `spine/three-possibilities.tex`; (iii) new `\section*{From Compression to Expansion}` inserted between front matter and spine in the include order.
3. Build, render, diff HTML — confirm seam appears once, before spine chapter 1.
4. Run 14-reader low-anneal audit on p1+p2 (unchanged surfaces). Must match eigenvalue40 result exactly.
5. Run 4-reader audit on the seam itself.

**Acceptance:**
- Seam passage exists, ≤150 words, renders cleanly.
- p1+p2 14-reader audit matches eigenvalue40 (14/14 finish, 14/14 T1+T2, 13/14 T5, zero F-triggers).
- Seam passes 4-reader audit (all four finish, all four update their expectation, no F-triggers introduced).

**Checkpoint tag:** `eigenvalue40.1` — commit and tag only if both audits pass.

**Rollback:** if p1+p2 audit diverges from eigenvalue40, `git reset --hard eigenvalue40` and re-scope the seam.

### Phase 2 — Surgical fixes, DN-prioritized · anneal: **MED**

**Goal:** close all L3+ disjoints with minimum-token rewrites.

**Work:**
1. Sort the matrix from Phase 0 by highest DN-level across the 4 readers, descending.
2. Process in order:
   - For each L3+ disjoint: apply the surgical proposal from the matrix.
   - One commit per disjoint. Message format: `spine reconciliation: <chapter> <disjoint-type> (disjoint N/M)`.
   - After each commit: build, confirm p1+p2 HTML unchanged at the surface level (`git diff HEAD~1 docs/downloads/Relinquishment.html | grep -E '^[+-]' | head -40` — manual inspection for front-matter bleed).
3. After every ~5 surgical commits: run p1+p2 14-reader audit. Must match eigenvalue40.
4. After all L3+ disjoints processed, run 4-reader audit on the affected chapters.

**Surgical guidelines (per disjoint type):**
- **Trustee register drift:** prefer in-place noun swap ("gatekeeper" → "trustee" where archetype-register is called for; keep "gatekeeper" only where the mechanical-role meaning is load-bearing). Never both in same paragraph without framing.
- **Authority overclaim:** rewrite "the most powerful living being on Earth" → "a custodian with unusual reach." Minimum 5 tokens changed, maximum 15.
- **Sentience-leak nominalizations:** "the entity" → "Custodian" where referent is singular; drop to plural ("the custodian and its backchannels") where aggregation is meant.
- **Five-fields non-enumeration:** add one sentence naming the five (topology / TFT-condensed-matter-TQC / solitons-nonlinear-dynamics / autocatalysis-autopoiesis / universality-parallel-computation / materials-science → compress to 5 clusters, 11 domains) where the spine first leans on the claim. Reuse the plain-text `five fields` hover fallback language to stay below the eigenvalue threshold.
- **Stack-vocabulary absence:** add one callback sentence per chapter where the stack would anchor. Form: "Recall the stack. Chapter X is the [Nth rung / top rung]." Do not re-explain the stack; just reference it.
- **"All your electricity" + muscular capability:** add epistemic label inline. Form: `\deeplink{...}` or inline gloss: "Under Possibility C — and only under C — the capability described next is exercised at all."

**Acceptance per commit:**
- Build succeeds.
- `docs/downloads/Relinquishment.html` diff shows change only in intended chapter's section.
- No hover-definitions.yaml edits that touch front-matter terms.

**Acceptance for phase:**
- All L3+ disjoints closed.
- p1+p2 14-reader audit matches eigenvalue40 (run at end of phase).
- 4-reader audit on affected chapters reports all four finish, no new F-triggers.

**Checkpoint tag:** `eigenvalue40.2` — on phase completion.

**Rollback per commit:** if a single commit diverges p1+p2, `git revert <sha>`; continue with next disjoint.
**Rollback for phase:** if cumulative damage to p1+p2 appears, `git reset --hard eigenvalue40.1` and re-plan.

### Phase 3 — Verification · anneal: **LOW**

**Goal:** full acceptance run.

**Work:**
1. Run p1+p2 14-reader low-anneal audit. Must match eigenvalue40 exactly.
2. Run 4-reader (Reeves / Pastor Mike / Miriam / Chen) medium-anneal audit on the full spine. Report per reader × per chapter: finished?, T-coverage delta vs p1+p2, F-triggers raised, DN-level of any remaining disjoints.
3. If any remaining L3 disjoint: return to Phase 2 for that item.
4. If all remaining disjoints are ≤L2: accept and proceed to Phase 4.

**Acceptance:**
- p1+p2 eigenvalue held.
- Zero L3+ disjoints remaining across 4-reader × spine.
- All 4 readers finish the spine.
- F-trigger count on spine ≤ F-trigger count on eigenvalue40 p1+p2 audit (spine should not introduce new triggers beyond what compression already passes through).

### Phase 4 — Tag

**Work:** `git tag -a eigenvalue41 -m "p3 reconciliation pass: spine aligned to p1+p2 register (trustee archetype, sentience-agnostic hedge, stack-vocabulary callbacks, five-fields enumerated). p1+p2 14-reader audit unchanged."` then `git push origin eigenvalue41`.

## 7. Verification matrix summary

| Phase | Audit run | Pass criterion |
|---|---|---|
| 0 | (none — inventory only) | matrix complete, L3+ rows have surgical proposals |
| 1 | p1+p2 14-reader + 4-reader on seam | p1+p2 matches eigenvalue40; seam passes 4-reader |
| 2 | p1+p2 14-reader every ~5 commits; 4-reader on affected chapters at end | p1+p2 matches eigenvalue40 throughout; no new F-triggers |
| 3 | p1+p2 14-reader + 4-reader full spine | eigenvalue40 held; zero L3+ disjoints remain |
| 4 | (none — tagging) | n/a |

## 8. Risks

1. **Diffuse register drift resists surgical fix.** If disjoint count after Phase 0 is >30 and average rewrite spans >3 sentences, this becomes Phase-2-as-register-sweep — which is anneal-reset territory. Mitigation: if Phase 0 inventory shows >30 L3 disjoints, Auditor writes Plan 0188 to scope a chapter-at-a-time approach with per-chapter eigenvalue checkpoints.

2. **Hover-term coupling.** A surgical fix in the spine may require a hover definition edit that touches a term used in p1+p2. Mitigation: rewrite spine prose to not depend on that hover term; leave the hover alone.

3. **Voice-moment sacrifice.** "All your electricity are belong to us" is a deliberate register break. Naïve reconciliation would sand it off. Mitigation: contextualize (add epistemic label), don't remove.

4. **Chen's technical rigor vs archetype-softening.** Chen may flag a rewrite that softens a capability claim as "now vague." Mitigation: capability claims stay; only sentience nominalizations and archetype register soften.

5. **Eigenvalue drift from hover-fallback re-render.** If p1+p2 plain-text `five fields` fallback changes because of Phase 2 five-fields enumeration edit, p1+p2 audit can shift. Mitigation: create a separate spine-specific hover term (`five-fields-enumerated`) rather than editing the shared `five fields` entry.

## 9. Out-of-scope items for future plans

- Bridge + testament track reconciliation (Plan 0188 candidate)
- Genevieve Preface interaction with reconciled spine
- Religious-tradition deepening (Miriam tzimtzum expansion, Sandra Indigenous specificity, Amir/Yusuf engagement)
- Spine chart (stack-chart in `manuscript/spine/the-stack.tex`) — already corrected today

## 10. Handoff prompts

### To Generator for Phase 0

```
You are the Generator.
Read Plan 0187 at ~/software/relinquishment/plans/0187-p3-reconciliation-pass.md
Execute Phase 0 only (inventory).
Do not edit any file outside research/.
Output: research/p3-reconciliation-matrix-2026-04-13.md per the spec in §6 Phase 0.
Stop at phase end; report back.
```

### To Generator for Phase 1

```
You are the Generator.
Read Plan 0187 Phase 1.
Read research/p3-reconciliation-matrix-2026-04-13.md from Phase 0 output.
Draft the seam passage (≤150 words), place it per Auditor-preferred location (i) new spine/00-seam.tex.
Run the two audits specified in Phase 1 acceptance.
If pass: commit, tag eigenvalue40.1, push, report.
If fail: rollback, report what moved.
```

### To Generator for Phase 2

```
You are the Generator.
Read Plan 0187 Phase 2.
Process L3+ disjoints from Phase 0 matrix in descending DN-level order.
One commit per disjoint. Run p1+p2 14-reader audit every 5 commits.
If p1+p2 diverges from eigenvalue40 at any check: revert the last 5 commits and report.
On phase completion: tag eigenvalue40.2, push, report.
```

### To Generator for Phase 3+4

```
You are the Generator.
Read Plan 0187 Phase 3 and Phase 4.
Run full verification suite.
If all L3+ closed and p1+p2 holds: tag eigenvalue41, push, report.
If any L3 remains: report which, do not tag.
```

## 11. Success criteria (summary)

1. p1+p2 eigenvalue40 is preserved — 14-reader low-anneal audit output identical to today's.
2. Zero L3+ disjoints remain in the spine across Reeves / Pastor Mike / Miriam / Chen filters.
3. All 4 readers finish the spine at medium anneal.
4. F-trigger count on spine ≤ F-trigger count on eigenvalue40 p1+p2 audit.
5. Tag `eigenvalue41` exists and is pushed.
