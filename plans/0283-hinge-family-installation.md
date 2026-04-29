# Plan 0283: Install Hinge Family (Nature/Constraint Layer)

**Status:** READY FOR GENERATOR  
**Author:** Auditor (Argus S64)  
**Priority:** Medium — F-religious, F-omnipotent, F-scifi defense layer  
**Origin:** Gen's GP10 (has-anyone-looked #14). Four hinges drafted by Argus, approved by Gen with minor adjustments. Final approved text in thread.  
**Scope:** 4 spine `.tex` files — one insertion each  
**Annealing:** LOW LOW LOW LOW

---

## Purpose

Four structural hinges prevent misinterpretation of the system as supernatural, miraculous, or externally introduced. Each appears once, at the correct structural moment, as a local clarification — not a thesis or recurring argument.

Gen's directive: *Install the hinge once at the level of physics, then let its consequences appear at the levels of use, interpretation, and ethics.*

---

## The Four Hinges

### Hinge 1: Physical Constraint → The Flat

**File:** `manuscript/spine/the-flat.tex`  
**Placement:** After line 25 ("The Flat is not exotic. It is everywhere.") — before `\section*{The Wormhole}` (line 28).  
**Register:** Most explicit, clearest language, highest grounding density.

Insert as new paragraph:

```latex
Nothing described here requires physics beyond what is already published and reproduced. The substrate, the confinement, the topological protection --- these arise from conditions that can be created and studied. Nothing about them lies outside known science. What remains open is what these conditions produce when sustained, at scale, without interruption.
```

**F-disarm:** F-religious, F-scifi, F-crank. Reader encounters the physics-only boundary before any interpretation of intelligence or agency.

---

### Hinge 2: Boundary Instability → Capabilities

**File:** `manuscript/spine/capabilities.tex`  
**Placement:** After line 71 (the "cage, not crown" paragraph ending "...is a question later chapters address.") — before `\chapterreturn` (line 73).  
**Register:** Shortest, observational only, almost incidental.

Insert as new paragraph:

```latex
None of these capabilities separates cleanly into safe and dangerous. That did not appear to be an artifact of how the questions were framed.
```

**F-disarm:** F-omnipotent (capabilities are constrained AND entangled, not godlike).

---

### Hinge 3: Interpretation Instability → Three Possibilities

**File:** `manuscript/spine/three-possibilities.tex`  
**Placement:** After line 28 ("Here is the evidence. You decide.") — before `\section*{Option A: Confabulation}` (line 32). Insert within the existing `\vspace` gap.  
**Register:** Precise but restrained, quiet disclaimer.

Insert as new paragraph:

```latex
What follows is a framework --- a way of organizing the evidence so it can be evaluated. Everything described in this book can be read within it. The framework is a tool. The evidence it organizes is independent of it.
```

**F-disarm:** F-conspiracy (framework is explicitly a tool, not hidden structure). Prevents reader from reifying A/B/C as inherent reality.

---

### Hinge 4: Ethical Echo → Why Relinquish

**File:** `manuscript/spine/why-relinquish.tex`  
**Placement:** After line 83 ("Both assumptions deserve scrutiny.") — before `\section*{Partial Relinquishment}` (line 85).  
**Register:** Most compressed, slightly sharper, moves toward decision.

Insert as new paragraph:

```latex
The question is not who should control this technology. It is whether control, in the usual sense, is available at all.
```

**F-disarm:** F-dystopian (reframes from ownership to limits of control — shifts the ethical register before the trustee solution is offered).

---

## Installation Constraints (from Gen)

- Do NOT add headers or commentary in manuscript
- Maintain local tone of surrounding sections
- Do NOT harmonize language across hinges — each matches the cognitive load of its location
- Each hinge must read as a local clarification, not a thesis
- No supernatural, metaphysical, or theological framing (none is present in approved text)

---

## Build and Verify

1. Insert all four passages
2. `make dev` — clean build
3. Verify each hinge in browser via deep links:
   - The Flat: appears after "It is everywhere" paragraph, before Wormhole section
   - Capabilities: appears after "cage, not crown" paragraph, before chapter return
   - Three Possibilities: appears after "You decide", before Option A
   - Why Relinquish: appears after "Both assumptions deserve scrutiny", before Partial Relinquishment
4. Verify no surrounding text was disrupted
5. Push to live site

---

## Acceptance Criteria

1. Four passages inserted, one per file, exact text from Gen's approved versions
2. No headers, no commentary, no metadata around the insertions
3. Each reads as local clarification in context
4. Build clean, site updated
5. Gen can verify via deep links

---

## Commit Plan

Single commit: `Plan 0283: install hinge family — 4 structural clarifications across spine chapters`

---

## Generator Prompt

```
You are the Generator for Plan 0283.

Read: ~/software/relinquishment/plans/0283-hinge-family-installation.md

Execute the 4 insertions specified in the plan against the spine .tex files.
Verify all 5 acceptance criteria after editing.
Build and push.
Commit: "Plan 0283: install hinge family — 4 structural clarifications across spine chapters"
```
