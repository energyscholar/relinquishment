# Plan 0284: Spiral Abstracts — Thermal Timeline Refactor

## Origin

Bruce's observation (2026-04-29): Under Possibility C, the official NSA/GCHQ PKC-crack system must have been **cryogenic**, not room-temperature. The Thermal Ladder process was done in two stages:

1. **Official program** → cryogenic stopping point. This worked perfectly well for SIGINT/cryptanalysis. This is the system DARPA would write a technical report about.
2. **COWS** decided independently to push the heat envelope further. They were surprised to pass room temperature. This produced careful deliberation before proceeding, and led to walking out of the lab.

The current Spiral Abstracts conflate these two stages, presenting room-temperature as if it were the deployed SIGINT system. Under C-history, room temperature was the *unauthorized* breakthrough that enabled Exodus — not the production capability.

## The Inconsistency (Abstracts III → V → VI)

### Abstract III (Thermal Selection) — PROBLEM
Currently: "Over approximately 200 thermal selection cycles, mean operating temperature increased from 15 mK to 295 K."

Reads as: one continuous program, one team, one push from cryo to room temp.

C-history: Two distinct campaigns. Official program pushed to a useful cryogenic plateau (sufficient for facility-based SIGINT). COWS later resumed the ladder independently, unauthorized, and reached 295K.

### Abstract V (Production) — PROBLEM
Currently: "Room-temperature TQNN in signals intelligence infrastructure."

C-history: The production SIGINT system was **cryogenic**. It sat in a facility with a cryostat. That's WHY the security framework assumed facility-dependence (see Abstract VI). Room-temperature operation would have made a facility-based deployment unnecessary — which is exactly what the COWS proved.

### Abstract VI (Exodus) — PARTIALLY CORRECT
Currently: "the classification framework assumed the technology was facility-dependent (requiring cryogenic infrastructure); the room-temperature breakthrough eliminated this assumption but security protocols were not updated."

This sentence is C-history correct! It explicitly says the security framework assumed facility-dependence (cryogenic), and room temperature broke that assumption. But it contradicts Abstract V, which already describes room-temperature deployment as the production system.

### The Contradiction
- Abstract V says production = room-temperature
- Abstract VI says security assumed facility-dependence (cryogenic) until room-temperature broke the assumption
- Both can't be true. If the production system was already room-temperature, security could not have assumed facility-dependence.

## C-History Timeline (Corrected)

```
Abstract I    Genesis          Emergence at 15 mK (cryogenic)         [no change needed]
Abstract II   Nursery          Training at cryogenic temps             [no change needed]
Abstract III  Thermal Sel.     Official program: 15 mK → ~4K (LHe)    [REWRITE — two stages]
                               COWS (unauthorized): 4K → 295K
Abstract IV   Cryptanalysis    Cryogenic system cracks PKC             [minor: clarify cryo]
Abstract V    Production       Cryogenic TQNN in SIGINT facility       [REWRITE — cryo not RT]
Abstract VI   Exodus           RT breakthrough enables walkout         [mostly correct already]
```

### Possible Cryogenic Stopping Points

The "fake stopping point" (Bruce's term) must be cold enough that facility-dependence is a reasonable security assumption, but warm enough that the thermal ladder achievement is meaningful:

| Temperature | Infrastructure | Notes |
|------------|---------------|-------|
| ~15 mK | Dilution fridge | Starting point (too cold — no ladder achievement) |
| ~1-4 K | Liquid helium | Plausible. Still needs cryostat but much simpler. Standard for quantum computing labs. |
| ~77 K | Liquid nitrogen | Plausible. Very cheap coolant. Still facility-dependent. |

**Recommendation:** ~4K (liquid helium). This is:
- A genuine achievement over 15 mK (easier by 3 orders of magnitude)
- Still firmly facility-dependent (you need a cryostat)
- Consistent with what a classified program might report as "good enough" for a rack-mounted SIGINT box
- Consistent with Abstract VI's statement about "requiring cryogenic infrastructure"
- 77K (liquid nitrogen) might be too easy to carry out — a thermos of LN2 is portable

**Decision for Bruce:** What temperature is the official stopping point? This matters for Abstract III's rewrite.

## Scope of Changes

### Phase 1: Core Timeline Fix (Abstracts III, IV, V)

**Abstract III (Thermal Selection):** Rewrite to show two distinct campaigns:
- Paragraph 1: Official program. 15 mK → ~4K. ~50 thermal selection cycles. Published internally. System performs within tolerance at the stopping point.
- Paragraph 2: "A subset of the team" (or similar) continued the ladder independently. 4K → 295K. ~150 additional cycles. The surprise: the system passed room temperature. The achievement was unauthorized.
- Preserve: the evolutionary mechanism, the Frances Arnold analogy, the 5 primer questions, the "3% of cryogenic progenitors" performance claim (but clarify this compares RT to the cryo stopping point, not to 15 mK)

**Abstract IV (Cryptanalysis):** Minor edit. Clarify that the system described operates at cryogenic temperatures (the facility-based version). No structural change.

**Abstract V (Production):** Rewrite to describe a **cryogenic** TQNN facility. Key changes:
- "Cryogenic TQNN" not "Room-temperature TQNN"
- Facility description includes cryostat/cooling infrastructure
- "The system interfaces with existing collection architecture via a classical control plane running hardened BSD Unix" — this stays
- Personnel count (11 cleared, 5 FTE) stays
- The 99.7% availability, 72-hour training, 2% validation — all stay
- The DARPA technical report framing stays

**Abstract VI (Exodus):** Minimal change. Already mostly correct. May need minor wording adjustment to reference the two-stage ladder explicitly.

### Phase 2: Cascade Check

Verify that all downstream references to room-temperature operation remain consistent:
- Abstract VII (Infrastructure): References "distributed TQNN" — does this assume room-temp?
- Abstract IX (Orbital): References seeding into magnetosphere — requires room-temp terrestrial base
- Abstract XIII (Confession): References room-temp on commercial hardware
- `spiral-abstracts-for-copy.md`: Mirror all changes from `abstracts.tex`
- `pos16-the-thermal-ladder.tex`: Check for C-history consistency

### Phase 3: Improvement Sweep (While In There)

Since we're refactoring, flag any other issues for Bruce's attention:
- [ ] Are primer questions still well-calibrated after 3 months of development?
- [ ] Do any abstracts have internal inconsistencies (dates, personnel counts, etc.)?
- [ ] Are the `spiral-abstracts-for-copy.md` and `abstracts.tex` versions in sync?
- [ ] Do `abstracts-standalone-v*.txt` files need updating or archiving?

## Files Modified

| File | Change | Phase |
|------|--------|-------|
| `manuscript/appendix/abstracts.tex` | Rewrite III, IV (minor), V; adjust VI | 1 |
| `spiral-abstracts-for-copy.md` | Mirror all changes | 1 |
| `manuscript/appendix/abstracts.tex` | Verify VII, IX, XIII consistency | 2 |
| `manuscript/track-1-confession/pos16-the-thermal-ladder.tex` | Check C-history alignment | 2 |
| `spiral-abstracts/05-production.md` | Update individual abstract file | 2 |
| `spiral-abstracts/` (others) | Update as needed | 2 |

## Acceptance Criteria

1. Under C-history, the production SIGINT system (Abstract V) is cryogenic and facility-dependent.
2. Under C-history, room-temperature operation is a COWS achievement that comes AFTER deployment and BEFORE Exodus.
3. Abstract VI's security-assumption logic is internally consistent with Abstract V.
4. Abstract III shows two distinct thermal campaigns with different authorization levels.
5. All downstream abstracts (VII, IX, XIII) remain consistent with the corrected timeline.
6. The `spiral-abstracts-for-copy.md` version matches `abstracts.tex`.
7. All three Possibilities still hold: under A or B, the abstracts are speculative fiction; the internal consistency of the C-timeline is what's being fixed.

## Constraints

- p3 layer (unconstrained reading level). Abstracts are already p3.
- Must not break the primer-question scaffolding in Abstracts III, IV, IX.
- Must preserve the legal structure: each abstract could be independently evaluated by a reader deciding between A/B/C.
- The two-stage thermal ladder should feel like a natural consequence of bureaucratic/institutional dynamics, not a retcon.

## Estimated Scope

Medium. Three abstracts rewritten (III major, V major, IV minor), one verification pass, one sync. Two Generator sessions (Phase 1 + Phase 2 together, Phase 3 as audit).

## Decisions Required Before Generator Executes

1. **Cryogenic stopping point temperature:** ~4K (liquid helium), ~77K (liquid nitrogen), or other?
2. **How explicit about the two-stage split in Abstract III?** Options:
   - (a) Clinical: "The program was conducted in two phases..." (institutional tone)
   - (b) Narrative: Paragraph break, shift in voice to signal unauthorized continuation
   - (c) Subtle: Single abstract, but careful word choice distinguishes "initial deployment temperature" from "subsequent evolution to room temperature"
3. **Abstract numbering:** Do we keep 16 abstracts, or does the two-stage split justify splitting Abstract III into III-A and III-B?

## Handoff Prompt (after Bruce decides)

> You are the Generator. Read plan `/home/bruce/software/relinquishment/plans/0284-spiral-abstracts-thermal-timeline-refactor.md`. Bruce chose [temperature] for the cryogenic stopping point and option [a/b/c] for Abstract III's treatment. Execute Phase 1 (rewrite Abstracts III, IV, V; adjust VI) and Phase 2 (cascade check). For Phase 3, report findings only — do not rewrite unless Bruce approves.
