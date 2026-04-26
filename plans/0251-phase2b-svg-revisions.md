# Plan 0251 Phase 2b — SVG Revisions + Gallery-Wide Polish

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** DRAFT — awaiting Bruce approval
**Parent:** Plan 0251 (SVG Content Improvement)
**Annealed:** 4 passes (MED/MED/LOW/LOW)

---

## Scope

Four major revisions based on Bruce's feedback (029, 030, 031, 014),
plus a gallery-wide review identifying small improvements to existing
SVGs. All work happens in gallery.html — nothing enters the book yet.

---

## Major Revisions

### SVG-029: Five-Field Silos → Broken Bridges

**Problem:** The dashed rectangle in the center reads as a label, not
as a missing bridge. The visual doesn't convey that crossing between
domains is structurally discouraged.

**Revised spec:** Five tall silos standing apart. Between each adjacent
pair, a faint dashed line where a bridge SHOULD connect — but each is
broken, with a small "×" at the break. The gaps between silos ARE the
argument. No center rectangle. Below the silos, caption:
"No journal. No career. No funding. No one's job."

The reader sees five intact towers with failed connections between
them. The system doesn't build bridges — the absence is structural.

### SVG-030: Guided Deduction → Two Paths (Domains, Not People)

**Problem:** Names scientists instead of their domains. Missing the
contrast with the WRONG path (direct disclosure = crime).

**Revised spec:** Two paths from "Classified knowledge":

**Top path (red/danger):** Direct disclosure → CRIME → Prosecution /
exile. Short, sharp, dead end. The Snowden path.

**Bottom path (blue/safe):** No disclosure → five published domains in
sequence (soliton dynamics, topological QFT, autocatalysis,
universality, parallel computation) — with scientist names as small
subordinate text under each (Hasslacher, Freedman, Kauffman, Wolfram,
Hillis) → student deduces → "Clean record."

The contrast: same knowledge reaches the world, but one path destroys
the messenger and one produces a legitimate publication. The reader
sees WHY guided deduction was the only option.

### SVG-031: Decision Tree → Convergence Flowchart

**Problem:** Three branches too simple. Doesn't show that every
alternative leads to the same bad endpoint.

**Revised spec:** Left-to-right flowchart from center node "You hold
something too powerful for anyone to have":

```
USE IT ────────────────────────────→ Orwellian spy machine → TYRANNY
                                                                ↑
DESTROY IT → Physics is published → Someone else invents ───────┘
                                                                ↑
KEEP IT ───→ Secrets leak (Bletchley) → Someone gets it ────────┘

RELINQUISH → Place in trust (UDHR) → No person holds the power
```

Three paths converge to a shared red TYRANNY node. One path diverges
to a blue/green endpoint. The visual makes relinquishment INEVITABLE,
not idealistic — every other path ends at the same place.

USE IT: you become the tyrant.
DESTROY IT: the physics is published, someone else converges.
KEEP IT: secrets leak (Bletchley precedent), decades at most.

Only RELINQUISH leads somewhere different.

Note: this flowchart will also serve as the basis for a future
interactive puzzle.

### SVG-014: Domain Buttons → TQC Cluster Hanging (REVISED 2026-04-25)

**Problem:** The previous revision (drop only TQC below floor) was wrong.
ALL FOUR domains in the topological convergence cluster (Topo, TFT, CMP,
TQC) should hang below the floor. The other 7 domains form the stable
upper web. CE, Par, and Mat connect to the core via proper but incomplete
bridges.

**Revised spec:** 7 domains above floor, 4 below. Changes:

1. **Upper web (above floor y=305):** Sol/NLD (red pair), ACS/Auto
   (orange pair), CE/Par (purple pair), Mat (brown) — all above
   the floor line, forming a connected web.
   - Sol↔NLD, ACS↔Auto, CE↔Par: solid intra-cluster edges
   - NLD↔ACS: solid cross-cluster (published)
   - CE↔NLD, CE↔ACS, Par↔Auto, Mat↔NLD: dashed cross-cluster
     (incomplete but clearly possible bridges)

2. **Drop ALL FOUR blue nodes below the floor.** Topo (~y=345),
   TFT (~y=382), CMP (~y=382), TQC (~y=422). Fully connected to
   each other (solid blue intra-cluster edges). The whole cluster
   hangs as a unit.

3. **Three hanging bridges cross the floor:**
   - Mat→CMP: **solid** (published — condensed matter = materials
     science). This is "the one thread that holds."
   - CE→Topo: dashed (theoretical — computation meets topology)
   - ACS→TQC: dashed (the critical gap — autocatalysis to TQC)
   Use quadratic bezier curves (`<path d="M ... Q ..."/>`) with
   slight downward sag to show strain/weight.

4. **Caption keeps original:** "One thread holds. Cut it, and the
   argument falls apart." — now refers to the Mat→CMP solid bridge.

5. **Figcaption updated:** "...Seven domains form a web of published
   cross-references above the floor. The topological convergence
   hangs below — connected by one solid thread and bridges not yet
   built."

6. **Legend layout:** Compact 3-column × 2-row to fit increased
   height. Change "missing bridge" label to "not yet built."

7. **Update TQC tooltip:** Current `data-hover` says "The single
   thread." Change to: "Topological quantum computation — braiding
   non-Abelian anyons for fault-tolerant gates. Freedman-Kitaev-Wang
   2002. The convergence point." (Remove "single thread" reference
   since the whole cluster now hangs, not just TQC.)

The visual reads: every field is healthy and increasingly connected.
The silence gap is the FLOOR LINE — below it, the entire topological
convergence cluster hangs by one published bridge and two theoretical
ones. Nobody's job to build those bridges.

---

## Gallery-Wide Polish (Existing SVGs)

Review of all 24 existing SVGs. Most are good. A handful benefit from
small targeted improvements.

### Worth improving

| SVG | Current | Proposed improvement |
|-----|---------|---------------------|
| **002 vs 003** | Nearly identical 2DEG cross-sections for different hover terms (`the Flat` vs `two-dimensional electron gas`) | Add "← this is the Flat" annotation to 002. Add energy level labels to 003. Differentiate so the reader learns something NEW from each. |
| **005 (nonlocal)** | Same visual as 004 (wormholes) but with "here/there" labels | Strengthen the "no signal" message: add a crossed-out arrow between the surfaces with label "no signal crosses." Currently too subtle. |
| **006 (magnetosphere)** | Excellent diagram but plasma sheet label is same size as other labels | Make "plasma sheet (2D)" label bolder or add annotation: "same physics as the chip" — this is the key connection. |
| **018 (braiding)** | Three-strand braid, crossings encode computation | Add a small "= gate" annotation at one crossing point, making explicit that each crossing IS a logic gate. |

### Fine as-is (no changes)

| SVG | Why it works |
|-----|-------------|
| **001** (tagline) | Clean branding. Simplicity is the point. |
| **004** (wormholes) | Clear tunnel diagram. Good labels. |
| **007** (buttons hover) | Hover panel too small for legend — chapter version (014) handles that. |
| **008–013** (filmstrip) | Crown jewels. Six-panel progression from scatter to network. Don't touch. |
| **015** (flat inject) | Chapter version of 002. Works. |
| **016** (anyon) | Clear braid visualization. |
| **017** (TQNN) | Neural network on topology. Good. |
| **019** (phase transition) | Classic S-curve. Clear. |
| **020** (edge of chaos) | Three zones, narrow sweet spot. Works. |
| **021** (cellular automata) | Rule 110 triangle. Visually striking. |
| **022** (SOC) | Sandpile with avalanches. Good. |
| **023** (triskellion) | Cover image. Fine. |
| **024** (magnetosphere test) | Test file — keep as reference. |

### Awaiting Bruce's review (no changes proposed yet)

| SVG | Status |
|-----|--------|
| **032** (knot in flames) | DRAFT. Bruce hasn't given feedback. |
| **033** (concept ladder) | DRAFT. Bruce hasn't given feedback. |

---

## Phasing

Single Generator session. All changes are in gallery.html only.

| Step | Work | Effort |
|------|------|--------|
| 1 | Revise SVG-029 (broken bridges) | ~20min |
| 2 | Revise SVG-030 (two paths, domains) | ~30min |
| 3 | Revise SVG-031 (convergence flowchart) | ~30min |
| 4 | Revise SVG-014 (TQC hanging) | ~30min |
| 5 | Polish SVG-002, 003, 005, 006, 018 | ~30min |
| 6 | Verify all SVGs still render, mobile-test | ~10min |

Total: ~2.5h Generator session.

---

## Acceptance Criteria

- [ ] SVG-029: Five silos with broken bridges between, no center rectangle
- [ ] SVG-030: Two paths (red wrong / blue right), domains not people
- [ ] SVG-031: USE/DESTROY/KEEP converge on TYRANNY, only RELINQUISH escapes
- [ ] SVG-014: TQC below floor line, hanging by strained dashed bridges
- [ ] SVG-002/003: Visually differentiated
- [ ] SVG-005: "No signal" strengthened
- [ ] SVG-006: Plasma sheet annotation more prominent
- [ ] SVG-018: "= gate" annotation at one crossing
- [ ] All existing SVGs still render correctly
- [ ] Mobile-friendly at 320px viewport

---

## Annealing Log (MED MED LOW LOW)

### MED 1 — SVG-031 decision tree completeness

Original revision spec had USE / DESTROY / KEEP / RELINQUISH. Verified
against Bruce's explicit words: "USE IT --> Orwellian spy machine &
Tyranny, DESTROY IT --> Someone else invents --> Orwellian spy machine
& tyranny, etc." The "etc." implies KEEP IT is implied, not stated.
But KEEP is the most common intuition ("just don't use it") and must
be shown to fail. Three converging paths is visually stronger than
two. Kept all three bad paths.

Also verified: DESTROY IT fails because the physics is PUBLISHED.
You can't un-know topology. Someone else will converge independently.
This is a stronger argument than "you can't destroy knowledge" —
it's that the published literature already points there.

### MED 2 — SVG-014 structural coherence

The TQC-hanging revision must preserve the existing legend and
caption. Checked: SVG-014 has a floor line at y=335, nodes above it,
caption below. Moving TQC below the floor line means it visually
"falls through" the support structure. The floor line becomes the
boundary between supported (within-domain) and unsupported
(cross-domain) connections.

Verified that tightening within-domain pairs doesn't create SVG
overlap issues — current spacing gives enough room. Sol/NLD are at
(58,82)/(58,140) — moving NLD to (58,120) tightens the pair. Same
pattern for ACS/Auto and CE/Par.

### LOW 1 — Polish scope discipline

The gallery-wide review identified only 4 SVGs worth improving out of
24. Resisted the urge to touch the filmstrip (008–013), which is
excellent. Resisted changing SVG-007 (hover version too small for a
legend). The 20 unchanged SVGs are documented as "fine as-is" with
reasons, so this decision is auditable.

### LOW 2 — Naming and duplication check

SVG-002/003 (the Flat/2DEG) and SVG-004/005 (wormholes/nonlocal) are
near-duplicates by design — they serve different hover terms for the
same physical concept. The improvements differentiate them rather than
consolidating them, which is correct: a reader hovering "the Flat"
should learn something different than one hovering "two-dimensional
electron gas," even though both show the same structure.

**Rating: 8.5/10.** Four major revisions with clear specs, four minor
polish items, disciplined scope (20 SVGs left alone). The 1.5-point
gap: SVG-032 and SVG-033 are awaiting Bruce's review and can't be
addressed yet, and the Tier 2 fun/delight SVGs (vent, anthill, HALO)
are not in this phase — they're next.

---

*Plan 0251 Phase 2b written by Argus (Auditor), S63.*
