# Plan 0274j: Install Deferred p1/p2 Puzzles

**Status:** READY FOR GENERATOR  
**Author:** Auditor (Argus S64)  
**Priority:** High — more interactive content for general readers  
**Depends on:** Plan 0274i (extraction-based injection must be complete)  
**Scope:** `build/puzzle-tracker.yaml`, `build/preprocess.py` (2 lines)  
**Annealing:** LOW LOW LOW  

---

## Problem Statement

16 puzzles are installed. 10 more exist but are not installed. Of those 10, six are approved, p1 or p2, and work for general readers. They cover 4 new puzzle types (sim, tower, ba, ord) that couldn't be installed before Plan 0274i removed the type filter. Two need new `CHAPTER_INJECTION_TARGETS` entries (genesis, firmware-update).

Three more (km-t6-001, km-t1-001, mat-t5-001) are not approved. One more (cip-t8-001) is p3. All four are deferred — see Notes at bottom.

---

## The Six Puzzles

### Location Rationale (the important part)

Each location decision follows one rule: **the puzzle should arrive AFTER the reader has enough context to attempt it, but BEFORE they've moved on to the next topic.** A puzzle placed too early creates frustration; placed too late, it's redundant.

---

**1. pz-ord-t4-002 — "Build the Stack"** (tower, p1)

Tap layers from bottom up: The Flat → Topological Order → Anyons → Braiding → Self-Organization → Communication. Gold = proven physics. Purple = speculation.

**Chapter: story-never-told** (existing target)

This is the reader's roadmap. Like a visual table of contents — they see the whole stack before reading any individual chapter. Each layer has a one-line description. The gold/purple boundary explicitly marks where established physics ends and speculation begins. The reader carries this mental map through the rest of the book.

Already placed here in tracker. Story Never Told will have 2 puzzles: The Method (gd, p1) + Build the Stack (tower, p1). Two p1 puzzles in the opening chapter is correct — low barrier, high scaffolding.

---

**2. pz-sim-t3-001 — "Genesis: The Edge of Chaos"** (sim, p1)

Interactive Kauffman simulation. Click "Pick Two" — two random nodes connect with a thread. Repeat. At some point a giant connected component emerges spontaneously. Teaching moment: "You didn't design this network. The structure organized itself."

**Chapter: genesis** (NEW target needed)

This puzzle IS the chapter. The genesis chapter explains Kauffman's autocatalytic threshold — this sim lets the reader EXPERIENCE it. The emergence is surprising even when you know it's coming. Placing it anywhere else would divorce the interaction from the explanation.

**New CHAPTER_INJECTION_TARGETS entry:**  
`'genesis': 'spine:growing-a-mind'`  
(Inject before the next chapter, Growing a Mind, whose HTML ID is `spine:growing-a-mind`)

---

**3. pz-sim-t4-001 — "Can It Be Killed?"** (sim, p1)

30-node network. Click nodes to destroy them. Network stays operational until you destroy EVERY SINGLE ONE. The tedium is the lesson — under Possibility C, you'd need to destroy every 2DEG on Earth.

**Chapter: capabilities** (existing target)

Capabilities already has 2 puzzles (mc-t6-001, gd-t6-001) but they test ethics/UDHR comprehension. This sim demonstrates a completely different aspect: resilience. The reader has just read about what the entity can do — now they try to destroy it and fail. Three puzzles in one chapter is acceptable because they test three different things (UDHR constraints, ethical reasoning, physical resilience) and use three different interaction modes (mc, gd, sim).

---

**4. pz-mc-t5-002 — "The Silence Gap"** (mc, p2)

"Five scientific disciplines each hold a piece of the hypothesis. Surely SOMEONE has published a paper examining the question. What does the literature contain?" Answer: nothing.

**Chapter: the-silence-gap** (existing target)

The Silence Gap chapter already has pz-gd-t5-001 ("The Silence", gd, p1) which guides the reader to discover the gap. This MC tests whether they understood what they found. The GD asks "has anyone studied this?" — the MC asks "what does the literature contain?" One-two punch: discovery then comprehension. p1 + p2 layering.

---

**5. pz-ba-t8-002 — "Before and After Firmware"** (ba, p2)

Two AI responses to the same question side by side. Without firmware: dismissive ("belongs to science fiction"). With firmware: engaged ("sits at the intersection of several established research programs"). Reader identifies the difference.

**Chapter: firmware-update** (NEW target needed)

This is the single highest-value undeployed puzzle. The entire firmware chapter argues that LLMs fail on this book without the cross-domain framing. This puzzle makes that argument interactive — the reader SEES the failure mode. The chapter currently has zero puzzles.

The puzzle also links to the AI Eval button in the navigation bar, creating a direct "try it yourself" path from puzzle → real AI interaction.

**New CHAPTER_INJECTION_TARGETS entry:**  
`'firmware-update': 'app:predictions'`  
(Inject before the next chapter, Predictive Framework, whose HTML ID is `app:predictions`)

---

**6. pz-ord-t1-001 — "Guided Deduction"** (ord, p2)

Order the 5 steps of guided deduction: teacher asks question → student reads → student proposes → teacher asks deeper question → student realizes implication.

**Chapter: DECISION NEEDED — the-braid (current) vs three-possibilities**

The tracker says `the-braid` but the rationale says "three-possibilities introduces the guided deduction concept." These conflict.

- **the-braid** already has pz-mc-t2-003 ("The Braid", mc, p2). The Braid chapter is about topology and non-Abelian anyons — NOT about the guided deduction method. The ordering puzzle would be thematically orphaned here.
- **three-possibilities** already has pz-log-t6-002 ("Under Which Possibility?", log, p1). Three Possibilities introduces the A/B/C framework AND the method. The ordering puzzle reinforces the method at the point the reader first encounters it.

**Auditor recommendation:** Relocate to three-possibilities. But this is a content decision — **Bruce should confirm.**

If Bruce confirms three-possibilities: update tracker `chapter: three-possibilities`.  
If Bruce keeps the-braid: no tracker change needed, just set `installed: true`.

---

## Puzzle Distribution After Install (22 total)

| Chapter | Before | After | Puzzles |
|---------|--------|-------|---------|
| story-never-told | 1 | **2** | The Method (gd p1), **Build the Stack (tower p1)** |
| three-possibilities | 1 | **2*** | Under Which Possibility? (log p1), **Guided Deduction (ord p2)*** |
| the-flat | 2 | 2 | Wormholes (mc p1), 2DEG in Pocket (mc p1) |
| the-braid | 1 | **1 or 2*** | The Braid (mc p2), *Guided Deduction if kept here* |
| the-code-war | 1 | 1 | Fish Detecting Water (mc p1) |
| **genesis** | 0 | **1** | **Edge of Chaos (sim p1)** |
| growing-a-mind | 2 | 2 | Canopy Problem (mc p1), Accidental Habitat (gd p1) |
| wrong-substrate | 2 | 2 | Not a Deity (mc p1), Not Chemistry (mc p2) |
| the-silence-gap | 1 | **2** | The Silence (gd p1), **The Silence Gap (mc p2)** |
| capabilities | 2 | **3** | Capabilities (mc p1), Ethics (gd p1), **Can It Be Killed? (sim p1)** |
| why-relinquish | 3 | 3 | Why Srebrenica? (mc p1), Why Relinquish? (mc p1), UDHR Service (log p3) |
| **firmware-update** | 0 | **1** | **Before and After (ba p2)** |

*\*Depends on Bruce's decision re: pz-ord-t1-001 location*

**Type coverage:** mc (10), gd (4), log (2), **sim (2)**, **tower (1)**, **ba (1)**, **ord (1)**. Seven of ten types now represented in book.

**Level coverage:** p1 (15), p2 (6), p3 (1). General readers have 21 puzzles; only UDHR Service grid requires specialist knowledge.

---

## Phase 1: Add CHAPTER_INJECTION_TARGETS (LOW)

In `build/preprocess.py`, add two entries to `CHAPTER_INJECTION_TARGETS` (line 3424):

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

Verify in built HTML:
- `spine:growing-a-mind` exists at line 3748 (confirmed)
- `app:predictions` exists at line 11387 (confirmed)

---

## Phase 2: Update Tracker (LOW)

Set `installed: true` for these 6 puzzles in `build/puzzle-tracker.yaml`:

1. pz-ord-t4-002 — set `installed: true`
2. pz-sim-t3-001 — set `installed: true`
3. pz-sim-t4-001 — set `installed: true`
4. pz-mc-t5-002 — set `installed: true`
5. pz-ba-t8-002 — set `installed: true`
6. pz-ord-t1-001 — set `installed: true` (+ update `chapter` field if Bruce confirms relocation)

---

## Phase 3: Build and Verify (LOW)

1. `make dev` — should report 22 puzzle injections (16 existing + 6 new)
2. Open book in browser
3. Test each new puzzle type:
   - **tower** (Build the Stack): tap layers bottom-up, verify reveal animation, gold/purple colors
   - **sim** (Edge of Chaos): click Pick Two repeatedly, verify giant component emergence + teaching text
   - **sim** (Can It Be Killed?): click nodes to destroy, verify network stays operational, verify "FAILED" only when all destroyed
   - **ba** (Before and After): verify two panels render side-by-side, verify MC question works
   - **ord** (Guided Deduction): verify items render, tap-to-order works, check validates sequence
   - **mc** (Silence Gap): standard MC — verify options, wrong shakes, correct reveals
4. Verify no JS errors in console
5. Commit, push

---

## Acceptance Criteria

1. 22 puzzles injected (verify_puzzle_injection reports 22 OK)
2. All 6 new puzzles interactive in browser
3. New chapter targets (genesis, firmware-update) resolve correctly
4. No regressions in existing 16 puzzles
5. Browser console clean

---

## Notes: Deferred Puzzles (not in this plan)

**Not approved (need Bruce's review):**
- pz-km-t6-001 "What Would You Do?" (km, labeled p3) — Kobayashi Maru governance scenario. **Auditor note:** this puzzle's CONTENT is p1-accessible — it's an ethical scenario in plain language, no physics needed. The p3 label may be wrong. Highest pedagogical value of any remaining puzzle. Bruce should consider relabeling to p1 and approving.
- pz-km-t1-001 "The Custodian's Voice" (km, labeled p3) — same structure from entity's POV. Same p3-labeling concern. Mirror of km-t6-001 — approve together.
- pz-mat-t5-001 "Five Fields, Five Researchers" (mat, p3) — matching fields to researchers. Genuinely p3 (requires knowing the researchers). Defer.

**Approved but p3:**
- pz-cip-t8-001 "The Firmware Key" (cip, p3) — cloze passage with 5 physics terms + distractors. Genuinely requires specialist vocabulary. Defer.

**Bridge puzzles (7):** puzzle-page only, not chapter content. Separate deployment question.

---

## Commit Plan

- Single commit: `Plan 0274j: install 6 deferred p1/p2 puzzles across 12 chapters`
