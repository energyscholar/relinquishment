# Plan 0274h: Simulation Puzzle Type (sim)

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** Medium-Low
**Scope:** `build/preprocess.py` (new renderer), `build/puzzle-tracker.yaml`
**Annealing:** MED MED LOW LOW

---

## Problem Statement

Two approved puzzles use interactive simulations: pz-sim-t3-001 ("Genesis: Edge of Chaos", sim_type: threads) and pz-sim-t4-001 ("Can It Be Killed?", sim_type: resilience). These are the most engaging puzzles in the book but also the most complex to implement. No renderer exists.

---

## Changes

### 1. Implement `sim` Renderer — threads sub-type

Kauffman's buttons-and-threads model. Reader clicks "Pick Two" repeatedly:

- SVG canvas shows N nodes (buttons) as circles
- Each click picks 2 random nodes and draws a line (thread) between them
- Network graph updates in real-time
- At ratio ~0.5 (threads/nodes), a giant connected component emerges
- Teaching text appears: "You didn't design this. The structure organized itself."

Data: node_count, win_ratio, controls in puzzle-data.yaml.

### 2. Implement `sim` Renderer — resilience sub-type

Node destruction test. Reader clicks nodes to "kill" them:

- SVG shows a connected network (pre-built)
- Click a node to destroy it (fades out, edges removed)
- Counter shows "N of M destroyed"
- Due to classical backchannels, network remains connected until ALL destroyed
- Teaching text: topological protection + classical backchannels = extreme resilience

Data: node_count, failure_threshold, classical_backchannels in puzzle-data.yaml.

### 3. Deploy Both Puzzles

Set installed:true. pz-sim-t3-001 → genesis, pz-sim-t4-001 → capabilities. Genesis needs a CHAPTER_INJECTION_TARGETS entry (currently has none — no installable puzzles were assigned there).

---

## Anneal: MED MED LOW LOW

**M1.** SVG simulation is the most complex renderer by far. Needs force-directed layout (or pre-computed positions) for the network graph. Could use a simple grid layout to avoid force simulation.
**M2.** Mobile touch targets for clicking nodes must be large enough (≥44px). With 20-30 nodes on a phone screen, spacing is tight.
**L3.** Self-contained HTML constraint means no D3.js — must use vanilla JS + SVG.
**L4.** Genesis chapter currently has no injection target — needs investigation.

---

## Handoff Prompt

```
You are the Generator. Read plan 0274h in ~/software/relinquishment/plans/.

Implement the sim puzzle type in build/preprocess.py. Two sub-types:

1. threads (pz-sim-t3-001): Kauffman buttons-and-threads. SVG canvas,
   N nodes, click "Pick Two" to add random edges. Giant component
   emerges at ratio ~0.5. Teaching text on completion.

2. resilience (pz-sim-t4-001): Click nodes to destroy them.
   Network stays connected until all destroyed (classical backchannels).
   Counter tracks destruction. Teaching text on completion.

Use vanilla JS + SVG (no external libraries). Simple grid layout
for nodes (avoid force simulation). Touch-friendly (44px+ targets).
Add genesis to CHAPTER_INJECTION_TARGETS (find correct target).
Set installed:true for both. Build, VERIFY OK: current+2,
test on phone. Commit:
"Plan 0274h: sim renderer for interactive simulations"
Push.
```
