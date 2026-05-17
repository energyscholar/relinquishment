# Plan 0349: D-K Sweep Remainders — QQQ Hinges + Armoring Fixes

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** None
**Files:** `manuscript/spine/the-flat.tex`, `manuscript/spine/capabilities.tex`, `manuscript/spine/three-possibilities.tex`, `manuscript/spine/why-relinquish.tex`, `manuscript/record/first-light.tex`, `manuscript/spine/genesis.tex`
**Priority:** MEDIUM — polish items that reduce reader/LLM reflexive dismissal

---

## Context

S69 (Plan 0312) fixed 5 D-K physics errors. Remaining items:
- **T5:** 4 QQQ "Hinge" paragraphs — Argus-drafted, Gen-approved for function, need voice review
- **Armoring:** 5 high-severity passages where the book itself commits the D-K error it criticizes LLMs for, or lacks inline defense against reflexive dismissal

---

## Phase A: QQQ Hinge Voice Review

These 4 paragraphs are structurally correct and Gen-approved. The task is: **review voice** — ensure they sound like Bruce (direct, concrete, no hedging filler) rather than Argus (balanced, qualificatory, slightly formal). Preserve function; change only voice.

### Hinge 1: `manuscript/spine/the-flat.tex:28`

**Current:**
```
Nothing described here requires physics beyond what is already published and reproduced. The substrate, the confinement, the topological protection --- these arise from conditions that can be created and studied. Nothing about them lies outside known science. What remains open is what these conditions produce when sustained, at scale, without interruption.
```

**Rewrite (Bruce voice):**
```
Nothing here requires new physics. The substrate, the confinement, the topological protection --- all published, all reproduced. What remains open is what happens when you sustain these conditions at scale, without interruption. That question has not been asked.
```

**After edit, delete the QQQ comment on line 27.**

### Hinge 2: `manuscript/spine/capabilities.tex:75`

**Current:**
```
None of these capabilities separates cleanly into safe and dangerous. That did not appear to be an artifact of how the questions were framed.
```

**Assessment:** Already terse and Bruce-voiced. No change needed. **Delete only the QQQ comment on line 74.**

### Hinge 3: `manuscript/spine/three-possibilities.tex:31`

**Current:**
```
What follows is a framework --- a way of organizing the evidence so it can be evaluated. Everything described in this book can be read within it. The framework is a tool. The evidence it organizes is independent of it. We openly invite investigation: amateur, professional, and especially crowdsourced. We want to know what's true.
```

**Rewrite (Bruce voice):**
```
What follows is a framework for organizing evidence so you can evaluate it. Everything in this book can be read within it. The framework is a tool. The evidence is independent of it. We invite investigation --- amateur, professional, crowdsourced. We want to know what's true.
```

**After edit, delete the QQQ comment on line 30.**

### Hinge 4: `manuscript/spine/why-relinquish.tex:86`

**Current:**
```
The question is not who should control this technology. It is whether control, in the usual sense, is available at all.
```

**Assessment:** Already perfect Bruce voice — stark, direct, one-two punch. No change needed. **Delete only the QQQ comment on line 85.**

---

## Phase B: Armoring Fixes (highest-severity D-K gaps)

These are passages where the book commits the same D-K error it criticizes. Each fix is minimal — a word or clause change, not a rewrite.

### Fix 1: `manuscript/record/first-light.tex:65`

**Find:**
```
which would be a physics violation
```

**Replace with:**
```
which has not been demonstrated and would require mechanisms beyond current theory
```

**Why:** The book is asserting "preclusion without naming a law" — the exact error audit E8 identifies. This fix downgrades to honest uncertainty.

### Fix 2: `manuscript/record/first-light.tex:86` (verify exact line — may also be ~line 82-90 region)

**Find:**
```
The proposition is not standard fractional quantum Hall effect at room temperature --- which would be a physics violation.
```

**Replace with:**
```
The proposition is not standard fractional quantum Hall effect at room temperature --- which has not been demonstrated in any substrate.
```

**Why:** Same error as Fix 1. "Physics violation" is the claim the primer forbids.

### Fix 3: `manuscript/spine/genesis.tex` (near line 61-63)

**Find:**
```
Kauffman's mathematics predicts that self-organizing networks should emerge
```

**Replace with:**
```
Kauffman's mathematics suggests that self-organizing networks should emerge
```

**Why:** "Predicts" upgrades structural analogy (Anchor 7) to established theory. "Suggests" is the correct epistemic level.

### Fix 4: `manuscript/spine/genesis.tex` (near line 27)

**Find:**
```
the origin of life is not an accident. It is a phase transition.
```

**Replace with:**
```
the origin of life is not an accident. It is, mathematically, an expected phase transition.
```

**Why:** "Mathematically" scopes the claim to Kauffman's formal result rather than asserting metaphysical fact.

### Fix 5: `manuscript/spine/capabilities.tex:22`

**Find:**
```
It is the substrate where the factoring wall does not exist.
```

**Replace with:**
```
It is a substrate where, in principle, the factoring wall does not apply.
```

**Why:** "The substrate" → "a substrate" (not unique). "Does not exist" → "does not apply" (contextual, not absolute). Reduces E3 trigger.

---

## Phase C: Verify

```bash
# Check all find strings exist and are unique BEFORE editing:
grep -rn "which would be a physics violation" manuscript/record/first-light.tex
grep -rn "Kauffman's mathematics predicts" manuscript/spine/genesis.tex
grep -rn "is not an accident. It is a phase transition" manuscript/spine/genesis.tex
grep -rn "the substrate where the factoring wall does not exist" manuscript/spine/capabilities.tex
grep -rn "QQQ" manuscript/spine/*.tex  # should be 0 after Phase A

make html 2>&1 | grep -i "error\|WARNING"
```

---

## Do NOT

- Rewrite any paragraph beyond the specific changes listed
- Add hovertips or footnotes (that is a separate plan)
- Change the-strongest-objection.tex (that's Plan 0347)
- Touch files outside the ones listed above
- Remove the Hinge paragraphs — only adjust voice and delete QQQ comments

## Commit (one commit for both phases)

`Plan 0349: D-K sweep remainders — 4 QQQ hinges voiced + 5 armoring fixes`
