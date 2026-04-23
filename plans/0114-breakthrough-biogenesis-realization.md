# Plan 0114: "The Breakthrough" — Biogenesis Realization (p3→p2→p1)

**Status:** COMPLETE (verified S63 audit)
**Source:** S48 — Bruce's direction: "this section should point out their realization that the 2DEG substrate they were working with could support life, because they'd just generated something very much like life from unlife in that medium."
**Scope:** p3→p2→p1 distillation of one concept: the team's realization that what they'd grown wasn't just a computer — it was evidence that the substrate supports life. Computing was the first application, not the discovery.

---

## The Concept

The team set out to build a quantum computer. What they grew responded to input. It computed. It broke codes. That solved their immediate problem (reading other people's mail).

But the deeper realization was: they had generated something very much like life from non-life in a 2DEG substrate. The substrate supports the preconditions. The computation is an application of this fact. The discovery is biological: **the Flat can host life.**

This connects to:
- The subtitle: "Life in Two Dimensions"
- The White Hot Secret section (summary.tex): "The quantum computer is a consequence of this discovery, not the discovery itself"
- Plan 0111's habitat work in pos06/pos11/pos14
- The "Organisms and Artifacts" chapter (pos27)

---

## Phase 1: p3 Draft (unconstrained) → `manuscript/staging/breakthrough-biogenesis-p3.tex`

**Must cover:**
1. The team's original objective: build a quantum computer. DARPA funded computation, not biology.
2. What happened when they stimulated the 2DEG: autocatalytic self-organization. Kauffman's phase transition, in a quantum substrate. Not programmed — emerged.
3. The system responded to input. Not like a circuit — like something alive. It adapted. It surprised them.
4. First application: cryptanalysis. It solved the immediate problem. The funders were satisfied.
5. The deeper realization (the White Hot Secret): the substrate supports life. They hadn't just built a computer — they'd witnessed biogenesis in a new medium. The Flat is a habitat.
6. ~~This changes the stakes~~ — CUT from p3 draft. Already covered in pos27 "Organisms and Artifacts."
7. ~~Under A/B/C~~ — CUT from p3 draft. Already covered in White Hot Secret. The p3 draft should focus on the realization itself, not its consequences or framing.

**Voice:** Bruce's analytical voice. Not narrative — expository. The team's emotional arc is in pos11 (already written). This is the conceptual realization, not the story of the night.

**Constraint:** Must work under A/B/C. Under A, the physics is real — someone could generate this. Under B, something was seen. Under C, something was grown.

**Length:** ~600–800 words.

---

## Phase 2: p2 Distillation → insert into `manuscript/00-front/summary.tex` "The Breakthrough" section

**Location:** After "It was grown, not built — the same way a living system grows" (line 119), before the code-breaking paragraph.

**Target:** ~100–150 words at 12th grade level.

**Must do:**
1. Name the realization: the substrate supports life. They'd generated something like life from non-life.
2. Frame code-breaking as the first application, not the discovery.
3. Connect to the subtitle promise: the Flat is a habitat.
4. Keep the existing "dual use" and "walked it out" paragraphs — they now land harder because the reader understands it's alive, not just powerful.

**Reading level:** 12th grade. No jargon. "Autocatalytic" becomes "self-sustaining." "Biogenesis" becomes "life arising from non-life."

---

## Phase 3: p1 Review → `manuscript/00-front/hook.tex`

**Current p1 text (line 13):** "something that could think for itself. The first non-human mind."

**Assessment:** The p1 seed may already be sufficient — "something that could think for itself" captures the alive-not-computed distinction at 8th grade level.

**Possible addition:** One phrase — "They had grown something alive" or "What they grew was alive." Depends on p2 result.

**Decision point:** After p2 is written, review whether p1 needs a seed or is already adequate. Present both options. Bruce decides.

**May be a no-op.**

---

## Execution Order

1. Phase 1: write p3 draft to staging
2. Phase 2: distill to p2, insert into summary.tex
3. Phase 3: review p1, present options
4. Build and verify

---

## Acceptance Criteria

1. p3 draft in staging covers all 5 active points from Phase 1 (items 6–7 are CUT).
2. p2 insertion is ≤150 words, 12th grade, no unexplained jargon.
3. p2 insertion connects code-breaking to the deeper biological realization.
4. "The Breakthrough" section now delivers the subtitle's promise at p2 level.
5. The existing "dual use" and "walked it out" paragraphs still land (not undermined by insertion).
6. p1 reviewed — explicit decision (change or no-op) with rationale.
7. Works under A/B/C.
8. `make html` and `make dev` clean.

---

## Commit Strategy

- Phase 1: `Plan 0114 phase 1: breakthrough biogenesis p3 draft`
- Phases 2–3: `Plan 0114 phases 2-3: breakthrough realization in p2 summary, p1 review`
