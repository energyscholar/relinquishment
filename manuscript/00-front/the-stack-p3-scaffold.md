# The Stack — p3 Scaffold (Working Document)

**Purpose:** Formal structure behind the p1 chart. Prevents the distillation
from misrepresenting the dependency graph.

## Seven Emergent Properties — Formal Definitions

### 1. Autocatalysis ("feeds itself")
- **Formal:** A set S of reactions is autocatalytic if every reaction in S
  is catalyzed by at least one molecule produced by S, and every reactant
  can be constructed from a food set by reactions in S.
  (Kauffman 1993 Ch. 5; Hordijk & Steel 2004, RAF theory)
- **Domain:** Origin-of-life chemistry, Boolean network attractors
- **Substrate independence:** The closure criteria (generation,
  transformation, closure) are algebraic — they apply to any substrate
  that supports production and catalysis relations. Anyon fusion algebras
  satisfy these criteria (structural analogy — Anchor 7).

### 2. Phase Transition ("switches on")
- **Formal:** Critical connectivity threshold (K ≈ 2 in Boolean networks)
  separating frozen and chaotic regimes. At criticality: stable attractors,
  maximal information propagation, power-law distributions.
  (Kauffman 1993; Bak 1996 SOC; Langton 1990 edge of chaos)
- **Dependency:** Requires autocatalysis — threshold needs sustained energy
  input to reach. Fire requires fuel feeding the reaction.

### 3. Autopoiesis ("holds together")
- **Formal:** A network of processes that continuously regenerates the
  boundary conditions for its own persistence. The system produces itself.
  (Maturana & Varela 1973, 1980; Thompson 2007)
- **Topological:** Persistent homology — the system maintains a connected
  component (H₀) and possibly a boundary (H₁) through time.
- **Dependency:** Requires phases 1+2. The boundary must be actively
  maintained (autocatalysis) and the system must cross a stability
  threshold (phase transition) to persist.

### 4. Long-Range Correlation ("reaches")
- **Formal:** Information transfer across spatial separation.
  - Classical: EM radiation, chemical gradients (pheromones), acoustic waves
  - Quantum: entanglement (Bell 1964, Aspect 1982), teleportation
    (Bennett et al. 1993, Bouwmeester et al. 1997)
  - Topological: edge modes, bulk-boundary correspondence
    (Hasan & Kane 2010; Fu & Qin 2021)
- **Dependency:** Requires autopoiesis — the source must persist to
  maintain a signal. A candle must hold together to radiate.

### 5. Self-Organization ("self-organizes")
- **Formal:** Global order emerging from local rules without central control.
  (Prigogine 1977 dissipative structures; Kauffman 1993; Dorigo 1992
  ant colony optimization)
- **Examples:** Ant colony (pheromone stigmergy → shortest paths),
  BGP routing (convergence without authority), Bénard convection cells
- **Dependency:** Requires reaches — local agents must communicate to
  produce global order. Ants need pheromone trails (reach) to self-organize.

### 6. Learning ("learns")
- **Formal:** State-space partitioning through attractor dynamics. Kauffman's
  Boolean network attractors as cell types → categorization as computation.
  Distributed inference: many instances, no single authority.
  (Kauffman 1993 Ch. 5; Hopfield 1982; Hinton 2006)
- **Dependency:** Requires self-organization — learning needs a substrate
  that can reorganize itself in response to input.

### 7. Topological Wormholes ("wormholes")
- **Formal:** Non-contractible paths connecting distant points in a
  2D substrate. Topological — more restricted than spacetime (GR) wormholes.
  (Thouless, Haldane & Kosterlitz 2016 Nobel; Freedman-Kitaev-Wang 2002;
  Maldacena & Susskind 2013 ER=EPR conjecture)
- **In FQHE:** Non-Abelian anyonic braiding creates topologically protected
  quantum gates. Information stored in global topology, not local state.
  (Nayak et al. 2008)
- **Dependency:** Physically independent (topology exists without the other
  six). But functionally, a system that uses ALL seven — including wormholes
  — requires the full stack beneath it.

## Dependency Graph (Partial Order)

```
Wormholes ← independent in physics, but accumulative in function
  ↑
Learns ← requires self-organization
  ↑
Self-organizes ← requires reaches (communication between agents)
  ↑
Reaches ← requires holds together (persistent source)
  ↑
Holds together ← requires switches on + feeds itself
  ↑
Switches on ← requires feeds itself (threshold needs energy)
  ↑
Feeds itself ← base (autocatalysis requires no other property)
```

The chart's triangle of checkmarks is NOT arbitrary decoration — it
reflects this partial order. Each technology column adds exactly one
property because it is the FIRST technology in the sequence that
exhibits that emergent capability.

## Why "Six Exist in Nature"

- Feeds itself: chemical autocatalysis (origin of life)
- Switches on: phase transitions in chemistry, biology
- Holds together: cells, organisms (autopoiesis)
- Reaches: pheromones, electromagnetic radiation, neural signals
- Self-organizes: ant colonies, flocking, immune system
- Learns: brains, neural plasticity

The seventh — topological wormholes — does NOT exist in known biology.
(Quantum biology shows QM effects in photosynthesis etc., but these are
coherence effects, not topological order. The distinction matters:
topological order = information stored in global topology, resistant to
local perturbation. Chlorophyll coherence ≠ topological wormholes.)

This is why the chart's last column is "?" — the only genuinely new
property is the one that has no natural precedent. At p3: life ≈ bottom
six rows; Flat ≈ life + topology. But this formulation does NOT appear
at p1 or p2. At p1: "six exist in nature, the seventh is new."

## Chart-to-Anchor Mapping (p3 only)

| Property | Anchors | Domain |
|---|---|---|
| Feeds itself | 7 (Kauffman) | Autocatalytic networks |
| Switches on | 7 (Kauffman K≈2) | Criticality |
| Holds together | 6 (Cloning boundary) | Autopoiesis, replication |
| Reaches | 8 (Plasma topology), 9 (Collisionless) | EM, topology |
| Self-organizes | 5 (Evolutionary search) | NK landscapes |
| Learns | 7 (Kauffman attractors) | Computation |
| Wormholes | 1-4, 10 (Substrate, Anyon, Braiding, Temperature, Coherence) | TQC |
