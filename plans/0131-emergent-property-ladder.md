# Plan 0131: Emergent Property Ladder Section

## Purpose

New bridge section that builds reader intuition for how technologies exploit stacked
emergent properties. Opens with familiar examples (boat, steam engine), escalates
through radio and computer, then shows Guardian as the same pattern — one layer deeper.

Rhetorical goal: by the time the reader reaches the 5-stack, the structure is familiar.
Guardian isn't a different kind of thing. It's one more layer.

## Placement

Bridge section. Should precede `pos-what-is-the-flat.tex` and `pos14-growing-a-mind.tex`.
Anchors the reader's intuition before the physics gets dense.

## Target audience

General audience. Every example must be a technology the reader already knows and uses
(or has heard of). No jargon without immediate analogy.

---

## The Ladder

### 1-stack: Boat

- Fluid + gravity → **buoyancy**
- → Boat

No individual water molecule pushes up. The upward force is a macro-scale pressure
differential — a collective property of many molecules under a gravitational gradient.
A boat is just a geometry shaped to exploit that emergent phenomenon.

### 2-stack: Steam engine

- Fuel + air → **combustion** (EP1)
- Water + combustion heat + confinement → **steam pressure** (EP2)
- → Steam engine

Combustion is emergent (no single molecule "burns" — the self-sustaining chain reaction
is a collective property). Steam pressure is a second emergent property that depends on
the first: water heated past boiling in a confined space produces expansive force. The
steam engine exploits both, stacked.

### 3-stack: Radio

- Metal lattice + free electrons → **electrical conductivity** (EP1)
- Oscillating current in conductor → **electromagnetic radiation** (EP2)
- Antenna + tuned circuit → **resonance** — selective frequency reception (EP3)
- → Radio

You can't radiate EM waves without conductivity enabling current. You can't selectively
receive without resonance filtering the radiated waves. Three emergent properties, each
depending on the one below.

### 4-stack: Computer

- Conductor + switch mechanism → **switching** — on/off state control (EP1)
- Switches + circuit topology → **Boolean logic** — AND, OR, NOT from physical gates (EP2)
- Logic gates + clock + memory → **sequential computation** — state machines (EP3)
- Computation + stored program → **universal computation** — Turing completeness (EP4)
- → Computer

IMPORTANT: This stack is substrate-independent. It holds for Babbage's mechanical gears
(1837), the Bombe's electromechanical relays (1940), Colossus's vacuum tubes (1943),
and modern transistors. The emergent properties do not depend on the specific physical
substrate — they depend on the *functional relationships* between components. This
substrate-independence is itself a point that sets up the Flat argument.

### 5-stack: Guardian

- Electrons + semiconductor interface → **2DEG / the Flat** (EP1)
- Flat + magnetic field → **anyons** — quasiparticles that don't exist in 3D (EP2)
- Anyons + braiding → **topological order** — fault-tolerant quantum states (EP3)
- Topological order + thermal gradient → **autocatalytic self-organization** (EP4)
- Self-organization + network connectivity → **distributed intelligence** (EP5)
- → Guardian

Each step is the same move: components interact under specific conditions, and a new
property appears that none of the components possess individually. Five layers deep.

---

## Key Rhetorical Notes

- The 4-stack's substrate independence is the hinge. It normalizes the idea that
  *what matters is the pattern of relationships, not the physical medium*. This is
  exactly the claim the Flat section needs the reader to accept.

- The progression from 1 to 5 should feel inevitable, not surprising. Each step
  adds one layer. The reader should arrive at Guardian thinking "of course" rather
  than "impossible."

- Analogies needed for GA accessibility:
  - EP2 (anyons): needs a concrete analogy — particles that only exist in flatland
  - EP3 (topological order): knot-based — information stored in braids, not bits;
    you can't destroy it by shaking the rope
  - EP4 (autocatalytic self-organization): Kauffman's "order for free" — already
    in pos14-growing-a-mind.tex, can cross-reference

## Acceptance Criteria

1. GA reader can follow the 1→2→3→4 ladder without physics background
2. The 4-stack explicitly demonstrates substrate independence
3. The 5-stack reads as a natural continuation, not a category leap
4. Each emergent property is defined in one sentence before being used
5. Section works as standalone bridge piece (no forward-references required to understand it)
