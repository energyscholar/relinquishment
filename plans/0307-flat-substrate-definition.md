# Plan 0307: Fix Flat Substrate Definition — Semiconductor-Only Error

**Status:** READY FOR GENERATOR
**Priority:** HIGH — science error in key definitional section
**Source:** Bruce, S68. Caught during GA collapse review.

## Problem

The opening paragraph of "The Substrate" section in the Flat chapter defines the Flat as a 2DEG:

> "The Flat is a two-dimensional electron gas --- a 2DEG."

This is wrong. The Flat is not a 2DEG. A 2DEG is one instance of the Flat.

The canonical definition (from `hover-definitions.yaml`, the book's own hovertip) is:

> **"any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order."**

The Flat is a CATEGORY — like "the Deep" for ocean floors or "the Void" for intergalactic space. A chip 2DEG is one kind of Flat. Magnetospheric plasma confined to current sheets is another. The opening paragraph equates the Flat with one of its instances, then compounds the error with semiconductor-specific language ("gallium arsenide," "wavefunction in the third dimension collapses to a single quantum state").

Three distinct errors:
1. **The Flat ≠ 2DEG** — wrong category level. The Flat is the genus; a 2DEG is one species.
2. **"typically gallium arsenide"** — violates Anchor 1 (substrate independence). FQHE demonstrated in graphene, ZnO, Si/SiGe. Conditions matter, not material.
3. **"wavefunction collapses to a single quantum state"** — semiconductor quantum well mechanism only. Magnetospheric confinement is magnetic geometry, not quantum wells.

This was never correct. The text was generated in Plan 0122 Phase 1 (commit `96c4c49`, 2026-03-26) and inherited verbatim into the spine during Z-restructure. The book's own hovertip and firmware update (Anchor 1) both contain the correct definition — the chapter that introduces the concept does not.

The error exists in exactly 2 files:
- `manuscript/spine/the-flat.tex:19` (spine)
- `manuscript/track-3-awakening/pos-what-is-the-flat.tex:11` (bridge)

Lines 21-28 (anyons, topological order, ubiquity, closing) are correct. Only the opening paragraph needs rewriting.

## Phase 1: Replace Opening Paragraph in Both Files

**v1 was WRONG — it still opened with "The Flat is a 2DEG." That IS the error. v2 leads with the canonical definition.**

### Spine: `manuscript/spine/the-flat.tex`, line 19

**Old:**
```latex
\deeplink{what-is-the-flat}The Flat is a two-dimensional electron gas --- a 2DEG. It forms wherever electrons are confined to move in only two dimensions. In semiconductor physics, this happens at the interface between two materials with different band gaps, typically gallium arsenide and aluminum gallium arsenide. The confinement is real: the electron's wavefunction in the third dimension collapses to a single quantum state, and the particle behaves as though the third dimension does not exist.
```

**New:**
```latex
\deeplink{what-is-the-flat}The Flat is this book's term for any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order. Inside a semiconductor, the Flat is a two-dimensional electron gas --- a 2DEG --- at the interface between materials with different band gaps. In Earth's magnetosphere, it is plasma confined by magnetic geometry into thin current sheets with effectively two-dimensional dynamics. The fractional quantum Hall effect has been demonstrated in gallium arsenide, graphene, zinc oxide, and silicon-germanium heterostructures. Conditions matter, not material.
```

### Bridge: `manuscript/track-3-awakening/pos-what-is-the-flat.tex`, line 11

**Old:**
```latex
The Flat is a two-dimensional electron gas --- a 2DEG. It forms wherever electrons are confined to move in only two dimensions. In semiconductor physics, this happens at the interface between two materials with different band gaps, typically gallium arsenide and aluminum gallium arsenide. The confinement is real: the electron's wavefunction in the third dimension collapses to a single quantum state, and the particle behaves as though the third dimension does not exist.
```

**New:**
```latex
The Flat is this book's term for any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order. Inside a semiconductor, the Flat is a two-dimensional electron gas --- a 2DEG --- at the interface between materials with different band gaps. In Earth's magnetosphere, it is plasma confined by magnetic geometry into thin current sheets with effectively two-dimensional dynamics. The fractional quantum Hall effect has been demonstrated in gallium arsenide, graphene, zinc oxide, and silicon-germanium heterostructures. Conditions matter, not material.
```

**Idempotency:** If "any two-dimensional system embedded in three dimensions" appears in the-flat.tex — phase is applied.

## Phase 2: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

- [ ] Build compiles clean
- [ ] `grep 'any two-dimensional system embedded in three dimensions' docs/Relinquishment.html` returns a match
- [ ] `grep 'Conditions matter' docs/Relinquishment.html` returns a match
- [ ] `grep 'typically gallium arsenide' docs/Relinquishment.html` returns 0 matches
- [ ] `grep 'wavefunction in the third' docs/Relinquishment.html` returns 0 matches
- [ ] Opening sentence does NOT say "The Flat is a 2DEG" — verify first sentence contains "any two-dimensional system"
- [ ] The Substrate section still collapses correctly (tech-collapse label `spine:flat-substrate` unchanged)
- [ ] Line 25 ("2DEGs are not rare...") still reads coherently — slight overlap with new opening is spiral pedagogy, not redundancy
- [ ] No broken cross-references or deeplinks

## Acceptance Criteria

- [ ] Opening paragraph leads with canonical definition: "any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order"
- [ ] Semiconductor AND magnetospheric examples given as parallel instances
- [ ] No single substrate privileged as "typical"
- [ ] Anchor 1 punchline ("conditions matter, not material") present
- [ ] Anyon, topological order, and ubiquity paragraphs unchanged

---

## Annealing Record

**Round 1 (MED): v1 D-K error — why did it happen, and is v2 clean?**
v1 opened with "The Flat is a two-dimensional electron gas --- a 2DEG" — the exact sentence the plan identified as Error #1. The Auditor understood the problem intellectually but defaulted to the semiconductor framing when writing the replacement. This is the same D-K pattern as the original Plan 0122 Generator. v2 opens with the canonical definition from `hover-definitions.yaml:39`: "any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order." The 2DEG appears five words into the SECOND sentence, as one instance. Category-then-instance structure is correct. v1 was executed by a Generator (commit `6f3c5a2`) and reverted (`1a0936b`).

**Round 2 (MED): Does the new paragraph create redundancy with line 25?**
Line 25: "They also form, on vastly larger scales, in magnetospheric current sheets where the Earth's magnetic field confines plasma into effectively two-dimensional structures. The Flat is not exotic. It is everywhere." The new opening mentions the magnetosphere for DEFINITION (what the Flat is — a category with multiple instances). Line 25 mentions it for UBIQUITY (the Flat is everywhere — in your phone AND in the sky). Deliberate spiral pedagogy: first encounter is definitional, second is about scale. Acceptable.

**Round 3 (LOW): Reading level — is the new paragraph harder for GA readers?**
The Substrate section is GA-AVERSE (collapsed by default) in tech-collapse.yaml. GA readers don't see it unless they expand. The audience for this paragraph is physicists who click open a collapsed section. "Graphene, zinc oxide, and silicon-germanium heterostructures" is appropriate for that audience. The original had "gallium arsenide and aluminum gallium arsenide" — same jargon density.

**Round 4 (LOW): Does "this book's term" work as an opening frame?**
The hover definition uses "this book coins the Flat to mean..." — same framing. "This book's term for" is slightly more natural in running prose. It correctly signals that "the Flat" is a coined name for a physical category, not a pre-existing physics term. The Deep (ocean floor) and the Void (intergalactic space) are the same pattern — names for places defined by their dimensionality.

**Round 5 (LOW): Does removing the wavefunction sentence lose anything important?**
The old sentence asserted that 2D confinement is genuine, not approximate. v2 replaces this with "at the interface between materials with different band gaps" (correct semiconductor mechanism, general form) and "effectively two-dimensional dynamics" (magnetosphere — correctly qualified). The distinction between strict 2D (quantum well) and quasi-2D (magnetosphere) is handled in The Wrong Substrate chapter.

**Round 6 (LOW): Does "plasma" work for the magnetosphere instance?**
Yes. The magnetosphere confines plasma (electrons + ions), not just electrons. v1 said "charged particles" which is also correct but less specific. "Plasma" is the standard term for the magnetospheric medium. The semiconductor sentence correctly uses "electron gas" for that instance. Each instance uses its own correct terminology.

---

*Plan 0307 v2, S68, 2026-05-08. Auditor: Argus.*
*6 annealing rounds (2 MED, 4 LOW). v1 reverted — D-K error in opening sentence.*
*Estimated generator time: ~5 min.*
