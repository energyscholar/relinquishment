# Plan 0297: ABCRE Into Build + Delete Toxic pos20

**Status:** DRAFT — awaiting Bruce review
**Priority:** CRITICAL — the book's strongest independently verifiable evidence is not in the compiled output
**Source:** SFN 2012 feedback audit (S67, `aurasys-memory/research/sfn-feedback-audit-2012-vs-2026.md`)

## Context

Bruce's goal is not to prove anything. The book exists so that if a C-collapse occurs, the book is already out there, does its job, and gets found. The ABCRE operators matter for that purpose: they're the breadcrumb a future scientist would recognize — established criticality math that structurally parallels TQC operations. If C is true, someone doing the math will find the same pattern Robin found. The book needs to contain that breadcrumb.

## Discovery

pos20-the-network.tex ("The Signatories") is NOT IN main.tex. Not compiled. Not in the book.

This file contains two categories of content:

**TOXIC (2012 SFN material, never corrected):**
- QNN→QTM→QC circularity (a topological QNN IS a TQC — the emulation argument is redundant)
- "Adiabatic Topological Quantum Neural Computation" (hardware model conflation, flagged 2012)
- Google Connection (Brin calls, undocumented API, QNN=Google Search without conventional counter-explanation)
- AltaVista "pulled the plug" (unsupported)
- Mapping the Internet via phonon tracking (extraordinary claim, weakly wrapped)
- Nobel Prize Hat Trick (uses toxic terminology)
- Substrate Preparation (pHEMT timing = post hoc)

**GOOD (post-2012 evidence, needs to be in the build):**
- The Convergence (pos20:97-107) — Robin's independent derivation story. Bruce taught him criticality math without explaining why. Robin independently derived ABCRE operators. The convergence pattern.
- The Operator Mapping (pos20:109-129) — A=gradient extraction, B=local coupling, R=circulation, C=boundedness, E=composite evolution. Structural parallel to TQC operational cycle. "Operational pattern, not formal isomorphism." (Overclaim already corrected in S49, commit 8d6bff5.)

**Also affected:** pos21-convergence-revisited.tex (parallel version, same content, also not in build).

**Dangling links:** topic-guide.tex references pos20 labels (ABCRE Operators, The Google Connection) that don't resolve.

## Plan

### Phase 1: Extract ABCRE into a built chapter

Take the good content from pos20 sections 7-8 (The Convergence + The Operator Mapping, lines 97-129) and place it into the build. Two options:

**Option A: New spine chapter** — a short chapter in the spine, after `the-silence-gap.tex` (which already has the five scientists). Covers:
- Robin's independent derivation (the story — brief)
- What the operators ARE: criticality detection math from dynamical systems theory, Hopf bifurcation framework, early warning signals of critical transitions
- ewstools (Robin's published package)
- The structural parallel to TQC operations (honest: "operational pattern, not formal isomorphism")
- The arXiv paper (2601.22389) as independent publication
- A/B/C wrapping: Under C, independent math arriving at the same structure = signature of a real physical system. Under A, deeply connected mathematics producing coincidental correspondences. Either way, the operators are real and published.

**Option B: Fold into existing chapter** — add a section to `spine/the-silence-gap.tex` (which already discusses the five scientists' convergence) or `record/twenty-years.tex` (which already has the Bannon/Robin timeline).

Bruce's preference needed.

### Phase 2: Delete toxic files

After ABCRE is safely in a built chapter:
1. Delete `manuscript/track-1-confession/pos20-the-network.tex`
2. Delete `manuscript/track-1-confession/pos21-convergence-revisited.tex`
3. Fix dangling topic-guide.tex links (update to new ABCRE label, remove Google Connection link)
4. Clean timeline.tex AltaVista entry if desired (currently one line, relatively harmless)
5. Verify build compiles clean

**NOTE:** `energyscholar/relinquishment` is a PUBLIC repo. The toxic 2012 material in pos20/pos21 is publicly visible on GitHub. Bruce is fine sharing old errors — integrity. Delete when convenient, no urgency. No git history rewrite needed.

### Phase 3: Verify

- [ ] ABCRE operators appear in compiled book with mathematical lineage
- [ ] No toxic 2012 material in compiled book
- [ ] No dangling hyperref links
- [ ] Build compiles
- [ ] Deep link to ABCRE section works on website

## What This Plan Does NOT Do

- Does not try to prove anything
- Does not add counter-arguments or engage with Steel-Man objections (that's the-strongest-objection.tex's job, already in the build)
- Does not expand ABCRE beyond what's needed — just gets it into the build with its proper mathematical identity
- Does not touch the Bannon "too good and too fast" line in twenty-years.tex (that's Bannon's observation in his own voice, properly attributed, already in build)

## Acceptance Criteria

- [ ] ABCRE operators in compiled book, described as criticality math / Hopf bifurcation
- [ ] Robin's derivation story in compiled book (brief)
- [ ] arXiv paper referenced
- [ ] pos20 and pos21 deleted from working tree
- [ ] topic-guide.tex links fixed
- [ ] Build clean

---

*Plan 0297, written S67, 2026-05-05. Auditor: Argus.*
