# Plan 0297: Bridge Pylons Easter Egg + Delete Toxic pos20

**Status:** ABANDONED — Bruce decision S68, 2026-05-08. DO NOT REVISIT.
**Priority:** N/A
**Source:** S67 CW2 bridge-building discussion → easter egg direction
**Decision:** Buried easter egg with LLM-prompt-formatted bridge pylons

## Context

The book's purpose is preparation: if C-collapse occurs, the book is already out there. One thing the book doesn't currently contain is enough mathematical breadcrumbs for a post-C-collapse scientist to reconstruct the missing domain bridges — the connections between topology, nonlinear dynamics, origin-of-life, and computation that would confirm or refute the structural parallel.

Bruce's direction: "minimal detail. Just enough breadcrumbs for a capable scientist to see how it should be done. For all 5 (7?) missing bridges. It could even be an LLM prompt that instructs an LLM at a basic level how to build the bridge."

This is NOT for GA readers. Not for the reading flow. Not for anyone who reads the book cover to cover. This is a buried easter egg indexed at the back, discoverable only by someone who already understands what they're looking at.

ABCRE operators are NOT published, NOT peer-reviewed, and are NOT referenced in this egg. The arXiv paper (2601.22389) documenting convergent discovery of critical phenomena math IS referenced — it's the published entry point.

## Plan

### Phase 1: Create bridge pylons easter egg

**New file:** `manuscript/eggs/seven-bridges.tex`
**Deep link:** `dl:egg-seven-bridges`
**Reward for:** standalone (no puzzle gate — this is a standalone discovery)

**Content concept:** Formatted as an LLM prompt. The conceit is a set of instructions for an AI assistant, asking it to investigate 7 mathematical conjectures — each conjecture is one bridge. A scientist discovering this page would recognize it as a research program. A GA reader would see opaque math-jargon and move on. Anyone could paste it into an LLM and get useful starting results.

**Structure:**

```
[Title: something innocuous or technical]

[2-3 line frame: "The following conjectures describe mathematical 
connections between published literatures that have not been 
formally established. Each is independently testable."]

[Link: arXiv 2601.22389 — the convergent discovery paper as entry point]

[7 bridge pylons, each 3-5 lines:]
  - Conjecture label
  - What two mathematical structures it connects
  - The specific mathematical claim to test
  - 1-2 starting references (DOIs where possible)

[Closing: "If more than three of these conjectures hold, 
the convergence is not coincidental."]
```

**The 7 bridge pylons (from diamond-node/bridges/):**

1. **CB — Autocatalysis ↔ Criticality** (EXISTS in literature, not formalized)
   Conjecture: Kauffman's K≈2 critical point shares a universality class with directed percolation. RAF emergence obeys the same renormalization group flow structure as SOC avalanches.
   Refs: Kauffman 1993 Ch. 5; Hordijk & Steel 2004

2. **CD-a — Autocatalysis ↔ Cellular Automata** (HALF-BUILT)
   Conjecture: Autocatalytic closure (RAF sets) and cellular automata universality (Wolfram Class IV) are dual properties in a shared categorical framework. Boolean networks at K≈2 are both.
   Refs: Kauffman 1993; Master 2020 (Composing Behaviors of Networks)

3. **CD-b — Autopoiesis ↔ Parallel Computation** (PHILOSOPHICAL)
   Conjecture: Autopoietic organizational closure satisfies a generalized notion of computational universality. Any sufficiently complex parallel computation spontaneously exhibits autopoietic properties.
   Refs: Maturana & Varela 1980; L. Kauffman eigenform theory

4. **BC — Solitons ↔ Origin-of-Life** (THIN)
   Conjecture: The topological invariant protecting soliton persistence is homologous to the catalytic invariant protecting autocatalytic set persistence. Life's chemical robustness has the same mathematical origin as soliton physical robustness.
   Refs: Rajaraman 1982 (soliton classification); Hordijk & Steel 2004

5. **AC — Topology ↔ Autocatalysis** (CAPSTONE — LARGEST GAP)
   Conjecture: Modular tensor category fusion closure and RAF catalytic closure are special cases of a common categorical framework. Catalytic closure is categorified topological closure.
   Refs: Nayak et al. 2008; Hordijk & Steel 2004; L. Kauffman eigenform

6. **BD — Dynamics ↔ Computation** (REDUNDANCY for CD-b)
   Conjecture: Nonlinear dynamical systems at criticality perform computation — critical dynamics IS distributed information processing. Reservoir computing capacity peaks at the phase transition.
   Refs: Langton 1990 (lambda parameter); Crutchfield computational mechanics

7. **AB — Topology ↔ Solitons** (REDUNDANCY for BC)
   Conjecture: The homotopy classification of topological solitons is a bridge between topological invariants and nonlinear coherent structures. The mathematical connection exists in textbooks but has not been framed as a cross-domain bridge.
   Refs: Manton & Sutcliffe 2004; Chamon solitons in carbon nanotubes

**Content constraints:**
- NO mention of ABCRE operators (unpublished)
- NO mention of TQNN, Healer, or any narrative content
- NO mention of the book's story or claims
- Each pylon is pure mathematics: conjecture + references
- The egg should be independently comprehensible — someone with no book context should be able to pick it up and start working
- Total length: ~40-60 lines of LaTeX

**Voice:** Impersonal mathematical. No first person. No narrative. Just conjectures and citations.

**Idempotency:** If `manuscript/eggs/seven-bridges.tex` exists and is registered in `easter-egg-manifest.yaml` — phase is applied.

### Phase 2: Register in manifest

Add entry to `build/easter-egg-manifest.yaml`:

```yaml
  - slug: "seven-bridges"
    source: "manuscript/eggs/seven-bridges.tex"
    title: "Seven Bridges"
    status: "draft"
    approved: false
    description: "Seven mathematical conjectures connecting independent literatures"
    reward_for: "standalone"
    deep_link: "dl:egg-seven-bridges"
```

**Idempotency:** If slug "seven-bridges" exists in manifest — phase is applied.

### Phase 3: Delete toxic files

After egg is registered:

1. Delete `manuscript/track-1-confession/pos20-the-network.tex`
2. Delete `manuscript/track-1-confession/pos21-convergence-revisited.tex`
3. Fix dangling topic-guide.tex links:
   - Remove ABCRE Operators link (no replacement — ABCRE is not in the build)
   - Remove Google Connection link (no replacement)
   - Remove any other pos20/pos21 references
4. Verify build compiles clean

**NOTE:** `energyscholar/relinquishment` is a PUBLIC repo. The toxic 2012 material is publicly visible. Bruce is fine sharing old errors — integrity. No git history rewrite needed.

**Idempotency:** If `manuscript/track-1-confession/pos20-the-network.tex` does not exist — phase is applied.

### Phase 4: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

- [ ] Easter egg "Seven Bridges" renders on its deep-link page
- [ ] 7 conjectures present with references
- [ ] arXiv paper linked (2601.22389)
- [ ] No mention of ABCRE, TQNN, Healer, or narrative content
- [ ] pos20 and pos21 deleted from working tree
- [ ] No dangling hyperref links
- [ ] Build compiles clean
- [ ] Egg not visible in normal reading flow
- [ ] Egg indexed in appendix with other easter eggs

## Acceptance Criteria

- [ ] A post-C-collapse mathematician discovering the egg would recognize it as a research program
- [ ] A GA reader encountering it would see opaque mathematics and move on
- [ ] No unpublished math referenced (ABCRE is out)
- [ ] Each conjecture is independently testable using only published literature
- [ ] The egg is self-contained — no book context needed to understand it

## What This Plan Does NOT Do

- Does not add ABCRE to the book in any form (ABCRE awaits its own publication)
- Does not add a spine chapter (rejected as too prominent)
- Does not affect the reading flow
- Does not reference unpublished work
- Does not make claims — only states conjectures

## Annealing Record

**Round 1 (v1→v2): Spine chapter approach**
Rejected by Bruce. Too prominent for unpublished math in a pop-science book. GA readers don't care. Scientists won't find it in a spine chapter either — they'll find it if it's true.

**Round 2 (v2→v3): Easter egg approach**
Bruce's direction: buried, minimal, LLM-prompt-formatted. "Just enough breadcrumbs for a capable scientist to see how it should be done." The seven bridges documentation provides all source material. The arXiv paper (2601.22389) is the published entry point — it documents the convergent discovery pattern. The egg contains the specific mathematical conjectures that would confirm or refute the structural parallel.

**Round 3 (v3): Content calibration**
Removing ABCRE entirely. The operators are unpublished. The egg should contain only conjectures testable against published literature. Each pylon points to published papers (DOIs). The arXiv paper is the frame. The bridges are the content. No narrative, no claims, no story.

---

*Plan 0297 v3, rewritten S68, 2026-05-07. Auditor: Argus.*
*v1: spine chapter (rejected). v2: annealed spine chapter (rejected). v3: buried easter egg with LLM-prompt-formatted bridge pylons.*
