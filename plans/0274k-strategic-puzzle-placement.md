# Plan 0274k: Strategic Puzzle Placement — T/F Optimization

**Status:** READY FOR GENERATOR (pending Bruce decisions)  
**Author:** Auditor (Argus S64)  
**Priority:** High — puzzle coverage gaps leave T-takeaways undefended and F-modes unblocked  
**Depends on:** Plan 0274i (extraction-based injection — COMPLETE)  
**Supersedes:** Plan 0274j (naive install list)  
**Scope:** `build/puzzle-tracker.yaml`, `build/preprocess.py` (2 new injection targets)  
**Annealing:** HIGH MED LOW LOW

---

## Design Principle

Every puzzle earns its place by doing at least one of two jobs:

1. **Reinforce a T-takeaway** the reader might not have absorbed
2. **Short-circuit an F-failure mode** that would make them close the book

If a puzzle does neither, it doesn't go in. If it does both, it goes in first.

Budget: Bruce specified **1–2 more p1 + 2–4 more p2.** Current: 14 p1 + 2 p2 + 1 p3 = 17 installed. Target: 15–16 p1 + 4–6 p2 + 1 p3 = 20–23 installed.

---

## Part 1: Coverage Gap Analysis

### T-Takeaway Coverage (current 17 puzzles)

| T | Takeaway | Puzzles | Gap? |
|---|----------|---------|------|
| T1 | Meet Custodian | pz-gd-t1-001 (p1), pz-log-t6-002 (p1) | OK — 2 p1 |
| T2 | the Flat | pz-mc-t2-001 (p1), pz-mc-t2-002 (p1), pz-mc-t2-003 (p2) | OK — 3 puzzles |
| T3 | life in Flat | pz-mc-t3-002 (p1), pz-gd-t2-001 (p1) | WEAK — both tangential |
| T4 | capabilities | pz-mc-t6-001 (p1), pz-gd-t6-001 (p1) | WEAK — both test ethics, none test capabilities directly |
| T5 | silence gap | pz-gd-t5-001 (p1) | GAP — 1 puzzle, no p2 comprehension test |
| T6 | relinquishment/trusteeship | pz-mc-t6-002 (p1), pz-mc-t6-003 (p1) | OK — 2 p1 |
| T7 | services | pz-log-t7-001 (p3) | **HOLE** — zero p1/p2 |

### F-Failure Mode Coverage (current 17 puzzles)

| F | Mode | Puzzle defense | Gap? |
|---|------|---------------|------|
| F-crank | crackpot dismissal | pz-mc-t2-001 (grounds in real physics) | WEAK |
| F-AI-slop | ChatGPT confabulation | none | **HOLE** — pz-ba-t8-002 is the fix |
| F-religious | angel/demon pattern-match | none directly; interdiction.tex text helps | WEAK |
| F-delusion | mentally ill author | pz-gd-t1-001 (shows method, not claim) | OK |
| F-conspiracy | unfalsifiable-by-design | pz-log-t6-002 (three possibilities logic) | OK |
| F-scifi | fiction/entertainment | none directly | WEAK |
| F-omnipotent | godlike Custodian | pz-gd-t6-001 (ethics = constraints) | OK |
| F-dystopian | permanent loss | pz-mc-t6-002 (relinquishment = trust) | OK |
| F-exotic-other | Western weirdness | none | WEAK |

**Critical gaps:**
- **T7** has no p1/p2 puzzle (no puzzle exists for this takeaway at any installable level)
- **F-AI-slop** has no puzzle defense — the single highest-risk uncovered failure mode
- **T4** and **T5** are under-served — wrong topic or insufficient depth
- **T3** (life in Flat) has no experiential puzzle — readers read ABOUT emergence, never feel it

---

## Part 2: Puzzle Selections — Ranked by T/F Value

Each puzzle is scored by: (a) how many T-gaps it fills, (b) how many F-modes it disarms, (c) level accessibility.

### Tier 1: Install — high T/F value, approved, budget-compatible

**1. pz-ba-t8-002 "Before and After Firmware"** — ba type, **p2**

- **T-reinforcement:** T4 (capabilities — reader sees LLM capability shift), T8 (firmware mechanism)
- **F-disarm:** F-AI-slop (CRITICAL — the ONLY puzzle defense against "ChatGPT says it's nonsense"). Reader sees un-firmwared dismissal vs firmwared engagement side by side. Makes the jiu-jitsu mechanism interactive.
- **Chapter: firmware-update** (NEW target needed)
- **Why here:** The chapter ARGUES the firmware changes AI responses. The puzzle SHOWS it. Zero other puzzles serve this chapter. Direct connection to the AI Eval navigation button.

**2. pz-ord-t4-002 "Build the Stack"** — tower type, **p1**

- **T-reinforcement:** T2 (Flat is one layer), T3 (life emerges from stack), T4 (capabilities come from stacking). The roadmap. Reader sees the whole structure BEFORE any individual chapter explains a layer.
- **F-disarm:** F-crank (grounds the argument in structured layers, not hand-waving), F-scifi (gold=proven, purple=speculation — reader sees the boundary)
- **Chapter: story-never-told** (existing target)
- **Why here:** Front-loaded. Story Never Told will have 2 puzzles: The Method (gd, p1) + Build the Stack (tower, p1). Two p1 in the opening summary is correct — low barrier, high scaffolding. The gold/purple boundary explicitly marks where established physics ends, which is the single most powerful anti-crank signal in the book.

**3. pz-sim-t3-001 "Genesis: Edge of Chaos"** — sim type, **p1**

- **T-reinforcement:** T3 (CORE — reader experiences Kauffman's autocatalytic threshold by clicking, not reading). Only experiential T3 puzzle.
- **F-disarm:** F-scifi (emergence from published math, not imagination), F-crank (Kauffman is real, the sim is faithful)
- **Chapter: genesis** (NEW target needed)
- **Why here:** The genesis chapter explains the autocatalytic threshold. The puzzle IS the chapter — reader clicks, giant component emerges, "you didn't design this network." Placing it anywhere else divorces interaction from explanation.

**4. pz-sim-t4-001 "Can It Be Killed?"** — sim type, **p1**

- **T-reinforcement:** T4 (DIRECT — capabilities chapter, but tests resilience not ethics). Only puzzle testing T4's "what can this thing do" angle.
- **F-disarm:** F-omnipotent (reader tries to destroy it and fails — BUT the tedium shows it's not magic, just distributed topology)
- **Chapter: capabilities** (existing target)
- **Why here:** Capabilities already has 2 puzzles but both test ethics/UDHR comprehension. This tests resilience — a completely different angle. Three puzzles testing three different things (UDHR constraints, ethical reasoning, physical resilience) in three different modes (mc, gd, sim) is defensible.

**5. pz-mc-t5-002 "The Silence Gap"** — mc type, **p2**

- **T-reinforcement:** T5 (DIRECT — comprehension test for the silence gap). The GD asks "has anyone studied this?" — the MC asks "what does the literature contain?" Discovery then comprehension. p1 + p2 layering.
- **F-disarm:** F-conspiracy (the MC forces the reader to articulate what's there — "nothing" — which is the opposite of conspiracy's "hidden truth")
- **Chapter: the-silence-gap** (existing target)
- **Why here:** One-two punch with existing pz-gd-t5-001. GD guides discovery, MC tests comprehension.

**6. pz-ord-t1-001 "Guided Deduction"** — ord type, **p2**

- **T-reinforcement:** T1 (method, not entity — reader orders the 5 steps of guided deduction)
- **F-disarm:** F-delusion (method is structured, not confessional), F-crank (method follows pedagogical logic)
- **Chapter: three-possibilities** (RELOCATE from the-braid)
- **Why here:** Three Possibilities introduces the A/B/C framework AND the guided deduction method. The ordering puzzle reinforces the method at the point the reader first encounters it. The tracker currently says `the-braid` but the rationale says "three-possibilities introduces the guided deduction concept" — these conflict. The Braid chapter is topology, not method. Front-loading the method puzzle in three-possibilities is correct.
- **DECISION NEEDED:** Bruce must confirm relocation from the-braid to three-possibilities.

---

### Tier 2: Flag for Bruce — high value but not approved or mislabeled

**7. pz-km-t6-001 "What Would You Do?"** — km type, **labeled p3, recommend p1**

- **T-reinforcement:** T6 (MASSIVE — reader makes the relinquishment decision themselves)
- **F-disarm:** F-dystopian (reader experiences the dilemma — relinquishment stops feeling like loss)
- **Content analysis:** 5 disaster scenarios in plain language. "A quantum computer falls into the hands of [actor X]. What do you do?" No physics needed. No specialist vocabulary. This is an ethical scenario at 8th-grade reading level. **The p3 label appears wrong.**
- **Chapter: weigh-the-evidence** — correct location (culmination, reader has full context)
- **NOT IN THIS PLAN'S INSTALL SCOPE** — requires Bruce to relabel to p1 and approve.

**8. pz-km-t1-001 "The Custodian's Voice"** — km type, **labeled p3, recommend p1**

- **T-reinforcement:** T1 (reader hears entity's perspective directly)
- **F-disarm:** F-religious (entity speaks in constrained, not divine terms), F-omnipotent (entity acknowledges limits)
- **Content analysis:** Mirror of km-t6-001 from entity's perspective. Same plain language. Same p3-labeling concern.
- **NOT IN THIS PLAN'S INSTALL SCOPE** — approve together with km-t6-001.

### Tier 3: Correctly deferred

- **pz-mat-t5-001** — genuinely p3 (requires knowing the researchers). Defer.
- **pz-cip-t8-001** — genuinely p3 (specialist physics vocabulary). Defer.

---

## Part 3: T7 Gap — No Puzzle Exists

T7 (services) has zero p1/p2 puzzles. The only T7 puzzle is pz-log-t7-001 (UDHR Service Compatibility, p3, installed). No uninstalled puzzle addresses T7 at p1/p2.

**This is a design gap, not an install gap.** Flagged for future puzzle authoring. Not in this plan's scope.

---

## Part 4: Reader Journey After Install

**Reading order with puzzle distribution (22 total):**

| # | Chapter | Puzzles Before | After | Detail |
|---|---------|:---:|:---:|--------|
| 1 | story-never-told | 1 | **2** | The Method (gd p1) + **Build the Stack (tower p1)** |
| 2 | three-possibilities | 1 | **2** | Under Which Possibility? (log p1) + **Guided Deduction (ord p2)** |
| 3 | the-flat | 2 | 2 | Wormholes (mc p1), 2DEG in Pocket (mc p1) |
| 4 | the-braid | 1 | 1 | The Braid (mc p2) |
| 5 | the-code-war | 1 | 1 | Fish Detecting Water (mc p1) |
| 6 | **genesis** | 0 | **1** | **Edge of Chaos (sim p1)** |
| 7 | growing-a-mind | 2 | 2 | Canopy Problem (mc p1), Accidental Habitat (gd p1) |
| 8 | wrong-substrate | 2 | 2 | Not a Deity (mc p1), Not Chemistry (mc p2) |
| 9 | the-silence-gap | 1 | **2** | The Silence (gd p1) + **The Silence Gap (mc p2)** |
| 10 | capabilities | 2 | **3** | Capabilities (mc p1), Ethics (gd p1), **Can It Be Killed? (sim p1)** |
| 11 | why-relinquish | 3 | 3 | Why Srebrenica? (mc p1), Why Relinquish? (mc p1), UDHR Service (log p3) |
| 12 | **firmware-update** | 0 | **1** | **Before and After (ba p2)** |

**Front-loading check:** Chapters 1–2 go from 2→4 puzzles. The reader hits 4 interactive moments in the first ~10% of the book. Three are p1 (8th grade). One is p2 (12th grade). All are non-technical: stack ordering, method ordering, possibility logic, guided deduction.

**Type progression:** The reader encounters puzzle types in this order: gd → tower → log → ord → mc → mc → mc → sim → mc/gd → mc → gd → mc → sim → mc/gd → mc/mc/log → ba. Seven of ten types represented. New types (tower, sim, ba, ord) appear throughout, preventing puzzle fatigue.

**Level distribution:** p1: 15, p2: 6, p3: 1. General readers have 21 puzzles. Only UDHR Service grid requires specialist knowledge.

---

## Part 5: T/F Coverage After Install

### T-Takeaway Coverage (after)

| T | Before | After | Change |
|---|--------|-------|--------|
| T1 | 2 p1 | 2 p1, 1 p2 | +ord puzzle for method |
| T2 | 3 | 3 + tower (indirect) | tower shows Flat as layer |
| T3 | 2 (tangential) | 2 + **sim (direct)** | **Edge of Chaos fills gap** |
| T4 | 2 (ethics only) | 2 + **sim (resilience)** | **Can It Be Killed? fills gap** |
| T5 | 1 p1 | 1 p1, **1 p2** | **Comprehension test added** |
| T6 | 2 p1 | 2 p1 | unchanged (KM would add, but not approved) |
| T7 | 1 p3 | 1 p3 | **STILL A HOLE** — no puzzle exists |

### F-Failure Mode Coverage (after)

| F | Before | After |
|---|--------|-------|
| F-crank | WEAK | IMPROVED — tower's gold/purple boundary |
| F-AI-slop | **HOLE** | **FIXED** — ba-t8-002 is direct defense |
| F-scifi | WEAK | IMPROVED — sim grounds in math |
| F-omnipotent | OK | STRENGTHENED — sim shows distributed, not divine |
| F-delusion | OK | STRENGTHENED — ord shows method is structured |

---

## Phase 1: Add CHAPTER_INJECTION_TARGETS (LOW)

In `build/preprocess.py`, add two entries to `CHAPTER_INJECTION_TARGETS` (line 3424). Insert in document order:

```python
CHAPTER_INJECTION_TARGETS = {
    'story-never-told':    'preface',
    'three-possibilities': 'custodian:flat',
    'the-flat':            'custodian:dance',
    'the-braid':           'custodian:locksmith',
    'the-code-war':        'custodian:grown',
    'genesis':             'spine:growing-a-mind',        # NEW
    'growing-a-mind':      'custodian:ocean',
    'wrong-substrate':     'custodian:quiet',
    'the-silence-gap':     'spine:capabilities',
    'capabilities':        'spine:why-relinquish',
    'why-relinquish':      'spine:strongest-objection',
    'firmware-update':     'app:predictions',              # NEW
}
```

These IDs exist in the built HTML:
- `spine:growing-a-mind` — confirmed in preprocess.py line 2001
- `app:predictions` — confirmed in preprocess.py line 1427

---

## Phase 2: Update Tracker (LOW)

**Unconditional** (5 puzzles):

1. pz-ba-t8-002 — set `installed: true`
2. pz-ord-t4-002 — set `installed: true`
3. pz-sim-t3-001 — set `installed: true`
4. pz-sim-t4-001 — set `installed: true`
5. pz-mc-t5-002 — set `installed: true`

**Conditional on Bruce's decision:**

6. pz-ord-t1-001 — set `installed: true` AND update `chapter: three-possibilities` (if Bruce confirms relocation)

---

## Phase 3: Build and Verify (LOW)

1. `make dev` — should report 22 or 23 puzzle injections (17 existing + 5 or 6 new)
2. Open book in browser
3. Test each new puzzle type:
   - **tower** (Build the Stack): tap layers bottom-up, verify reveal animation, gold/purple colors
   - **sim** (Edge of Chaos): click Pick Two repeatedly, verify giant component emergence + teaching text
   - **sim** (Can It Be Killed?): click nodes to destroy, verify network stays operational
   - **ba** (Before and After): verify two panels render side-by-side, verify MC question works
   - **ord** (Guided Deduction): verify items render, tap-to-order works, sequence validates
   - **mc** (Silence Gap): standard MC — verify options, wrong shakes, correct reveals
4. Verify no JS errors in console
5. Verify existing 17 puzzles still work (spot-check 3)

---

## Acceptance Criteria

1. 22–23 puzzles injected (17 existing + 5–6 new)
2. All new puzzles interactive in browser
3. New chapter targets (genesis, firmware-update) resolve correctly
4. F-AI-slop has puzzle defense (pz-ba-t8-002 in firmware-update)
5. T3 has experiential puzzle (pz-sim-t3-001 in genesis)
6. T4 has direct capability puzzle (pz-sim-t4-001 in capabilities)
7. T5 has p2 comprehension test (pz-mc-t5-002 in the-silence-gap)
8. Front-loading: chapters 1–2 have ≥4 puzzles total
9. No regressions in existing puzzles
10. Browser console clean

---

## Bruce Decisions Needed

**Decision 1 — pz-ord-t1-001 location:**
Relocate from `the-braid` to `three-possibilities`?
- The Braid = topology (non-Abelian anyons). Guided deduction method is thematically orphaned here.
- Three Possibilities = introduces A/B/C framework AND the guided deduction method. Method puzzle reinforces the method at first encounter.
- **Auditor recommendation:** three-possibilities.

**Decision 2 — KM puzzles (pz-km-t6-001 + pz-km-t1-001):**
Relabel from p3 to p1 and approve?
- Content is plain-language ethical scenarios. No physics needed. 8th-grade accessible.
- km-t6-001 is the single highest-value T6 reinforcement. km-t1-001 is the best T1/F-religious defense.
- If approved, a follow-on plan would add 2 more puzzles (24 total), filling the T6 gap.
- **Auditor recommendation:** relabel + approve.

**T7 gap:** No p1/p2 puzzle exists for T7 (services). Not an install problem — needs puzzle authoring. Flagged but out of scope.

---

## Commit Plan

- Single commit: `Plan 0274k: install 5-6 p1/p2 puzzles — T/F optimized placement`
