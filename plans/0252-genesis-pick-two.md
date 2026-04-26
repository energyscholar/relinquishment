# Plan 0252 — Genesis: Pick Two (Kauffman Interactive Filmstrip)

**Status:** PROPOSED  
**Author:** Auditor (Argus)  
**Scope:** `build/build-puzzles.py`, `build/puzzle-data.yaml`  
**Rationale:** The current Genesis puzzle (`pz-sim-t3-001`, SIM/threads type) fails to teach. User clicks "Add Thread" 15 times with no agency, no surprise, no teaching moment. The "Phase Transition!" flash vanishes after 1.8 seconds, then reveals a dense p3 abstract about anyonic quasiparticles. The puzzle neither matches Kauffman's actual experiment nor communicates why phase transitions matter.

Redesign to match Kauffman faithfully: pick up two buttons at random, tie a thread, toss them back. Phase transition diagnosed when two randomly selected buttons are **already connected to the same mass**. The user doesn't engineer the transition — they discover it.

## Design

### Core mechanic

- 20 buttons scattered along a floor line (SVG canvas, ~420×300)
- Single button: **"Pick Two"**
- Each click: two random buttons highlight → briefly lift above the floor (with any connected cluster members rising too) → thread draws between them → all settle back
- Clusters color-code automatically (reuse existing `CLUSTER_COLORS` + `getClusters()`)
- Counter: `Threads: N`

### Win condition

**Two selected buttons are already in the same connected component AND that component contains ≥ 50% of all buttons.** The thread is redundant. The discovery IS the lesson.

This matches Kauffman: below threshold, random picks find strangers. Above threshold, random picks find neighbors. The moment you pick two that are already connected to the mass — that's the phase transition.

### The three phases (invisible to user)

The user does the same action every time. The system's response changes:

1. **Early (ratio < 0.3):** Picks grab isolated buttons. Small pairs form. Lift shows just 2 buttons rising. Nothing interesting — "just tying random buttons."
2. **Building (0.3–0.45):** Some picks grab buttons already in clusters. Clusters merge. Lift shows 4, 6, 8 buttons rising together. The growing lift height teaches growing connectivity.
3. **THE MOMENT (ratio ~0.5):** User clicks Pick Two. Both buttons are in the same giant component. The ENTIRE web lifts with them — 10+ buttons rising as one mass. The thread is redundant. "Already connected."

### Filmstrip-style animation

Not smooth animation — `setTimeout` + re-render (matching existing codebase pattern):

1. Two buttons glow yellow (highlight via re-render, ~100ms delay)
2. Set `liftY` on both selected nodes and all their cluster members. Re-render — nodes draw at `n.y + n.liftY`. Lift heights: -60px for selected, -40px for 1-hop neighbors, -25px for 2-hop, etc. Connected threads stay taut (edges render using lifted positions). Hold for ~400ms.
3. Thread draws between the two selected buttons (add to edges array, re-render)
4. Reset all `liftY` to 0, re-render — settle back to floor (~300ms setTimeout)
5. `sim.animating = false` — next click allowed

Total per-click: ~1 second. Fast enough to avoid boredom, slow enough to see what lifted.

### Phase transition moment (special treatment)

When the win condition triggers:

1. Both selected buttons lift — and the **entire giant component** rises with them (10+ buttons)
2. A red thread draws between them (visually redundant — they're clearly already connected by multiple paths through the web)
3. The lifted mass stays up (does NOT settle back)
4. Floor below is nearly empty
5. Teaching text appears in the transition-flash div:

> *"Already connected. You did the same thing every time — picked two at random and tied a thread. You didn't design this network. The structure organized itself."*

6. After 5 seconds: settle, reveal puzzle abstract, mark solved

### Button label and counter

- Button: "Pick Two" (from YAML `button_label` field)
- Counter format: `Threads: N` (simpler than `N / 20` — the ratio doesn't need to be shown; the VISUAL teaches the lesson)
- When animating: button disabled (prevents rapid-fire clicks during transitions)

### Visual consistency with book filmstrip

The book chapter (preprocess.py `inject_button_sequence()`) has a 6-panel Kauffman filmstrip with 30 buttons on a dashed floor line. The puzzle should share visual DNA:

- Button r=10 (slightly smaller for 20 buttons), cluster-colored fills from `CLUSTER_COLORS`
- Floor: dashed line at y≈260, stroke `#ccc`, dasharray `4,4`
- Drop shadow filter (same `feDropShadow` spec as filmstrip)

## Changes

### 1. `build/puzzle-data.yaml` — Update `pz-sim-t3-001`

Replace the current entry with:

```yaml
  - id: pz-sim-t3-001
    type: sim
    sim_type: threads
    topic: t3
    level: p1
    category: science
    title: "Genesis: The Edge of Chaos"
    gateway_blurb: "Pick up two buttons at random. Tie a thread. Toss them back. Keep going until something changes."
    question: "Kauffman's buttons and threads: pick up two at random, tie them together, toss them back. Keep going."
    button_label: "Pick Two"
    node_count: 20
    win_ratio: 0.5
    hint: "Keep picking. You'll know when it happens."
    hint_threshold: 10
    teaching_text: "Already connected. You did the same thing every time — picked two at random and tied a thread. You didn't design this network. The structure organized itself."
    abstract: "Non-abelian anyonic quasiparticles in a fractional quantum Hall system, subjected to structured electromagnetic perturbation, can undergo autocatalytic self-organization at the edge of chaos, producing an emergent topological quantum neural network. Unlike conventional quantum computer design, which requires engineered gate sequences, the proposed system requires only the establishment of critical conditions in the substrate; computational architecture emerges spontaneously from the physics."
```

New YAML fields: `button_label`, `node_count`, `win_ratio`, `teaching_text`.

### 2. `build/build-puzzles.py` — `build_json()` SIM branch

Pass new fields through to JSON. In the `elif t == 'sim':` branch, for `sim_type == 'threads'`:

```python
d['hint_threshold'] = puzzle.get('hint_threshold', 12)
d['node_count'] = puzzle.get('node_count', 20)
d['win_ratio'] = puzzle.get('win_ratio', 0.5)
d['button_label'] = puzzle.get('button_label', 'Add Thread')
d['teaching_text'] = puzzle.get('teaching_text', '')
```

### 3. `build/build-puzzles.py` — Rewrite `initThreads()` JS

Replace `initThreads(el, d)` and `addThread(id)` with the Pick Two mechanic. Approximately 120 lines replacing the current ~40. The `renderTSvg(sim)` function is shared and mostly reused.

**Key implementation requirements:**

1. **Button scatter:** Place `N` buttons along floor (y≈260), jittered horizontally. Use seeded PRNG for reproducibility (same seed approach as resilience sim).

2. **Pick Two mechanic:** Each click selects a random unused pair. Check if both are in the same component (via `ufFind`). If same component AND component ≥ `win_ratio * N`: phase transition. Otherwise: add edge, union, settle. **Critical:** after each edge addition, if the giant component now ≥ `winRatio * N`, scan forward in the pair queue for any pair where both members are in the giant component, and swap it to position `pi` (next pick). This guarantees the "already connected" discovery fires within 1 click of the actual threshold — no accidental skip-past.

3. **Lift animation:** Before adding the edge, compute which nodes to lift:
   - The two selected nodes (lift highest, -60px)
   - All nodes in the same cluster as either selected node (lift proportional to hop distance from selected, minimum -20px)
   - Apply via temporary `liftY` property on each node; render uses `n.y + (n.liftY || 0)`
   - Use `setTimeout` for animation timing (matching existing codebase pattern — no CSS transitions on SVG)

4. **Thread rendering:** Existing `renderTSvg` draws edges and nodes. Extend to show:
   - Highlighted pair (yellow stroke, thicker border)
   - Lifted positions (using `liftY` offsets)
   - Red thread for the redundant win-condition edge

5. **Settle:** Reset all `liftY` to 0, re-render.

6. **Button appearance:** Keep cluster-colored fills (from `CLUSTER_COLORS`), consistent with the existing sim and the book's color-coded cluster pedagogy. Use `r=10`, drop shadow filter. Cluster colors teach cluster membership visually — the reader sees clusters merge as colors unify.

7. **Win display:** Replace the transition-flash text with `d.teaching_text`. Use a longer timeout (5 seconds instead of 1.8) to let the reader absorb the teaching beat. The lifted mass stays up during this time.

8. **Lock during animation:** Set `sim.animating = true` at click start, `false` at settle end. Ignore clicks while animating.

### 4. CSS additions (minor)

None required — existing `.transition-flash`, `.node-circle`, `.glow`, and `.sim-svg` classes handle the visual needs. The lift animation is done via SVG attribute manipulation, not CSS transitions.

## What is NOT changed

- `renderTSvg(sim)` structure — enhanced, not replaced
- `ufFind`, `ufUnion`, `getClusters`, `largestCluster` — shared utilities, unchanged
- Resilience sim (`initResilience`) — separate sim_type, untouched
- Book filmstrip (preprocess.py `inject_button_sequence`) — separate system, untouched
- Other puzzle types — untouched

## Acceptance Tests

After `make puzzles`, open `docs/downloads/puzzles.html`:

| # | Test | Expected |
|---|------|----------|
| 1 | Page loads without JS errors | Console clean |
| 2 | Genesis puzzle shows "Pick Two" button (not "Add Thread") | Button label from YAML |
| 3 | Click "Pick Two" — two buttons highlight and lift briefly | Visible lift ~400ms |
| 4 | Connected cluster members lift with selected buttons | If button A is in a 4-node cluster, all 4 lift |
| 5 | Thread appears between selected pair after lift | New edge rendered |
| 6 | All nodes settle back to floor after ~1 second | Smooth return |
| 7 | Rapid clicking during animation is ignored | No double-fire, no state corruption |
| 8 | After ~10 picks, clusters visibly merge (color changes) | Multiple clusters → fewer, larger clusters |
| 9 | Hint appears after 10 threads if not yet solved | "Keep picking. You'll know when it happens." |
| 10 | Win condition: picks two that are already in same ≥50% cluster | Teaching text appears, buttons stay lifted |
| 11 | Teaching text matches YAML `teaching_text` field | "Already connected..." |
| 12 | Teaching text displays for ≥4 seconds before settling | Not a 1.8s flash |
| 13 | After teaching text: nodes settle, abstract revealed | Standard revealPuzzle(id) flow |
| 14 | Counter shows thread count | "Threads: N" increments |
| 15 | `build_json()` passes `node_count`, `win_ratio`, `button_label`, `teaching_text` | Check JSON output |
| 16 | Button style matches book filmstrip (warm tan or cluster-colored) | Visual consistency |
| 17 | Other puzzles unaffected | Scroll through all 29, no regressions |

## Risk: Win condition timing

The phase transition might trigger too early (at 6 threads) or too late (at 15+) depending on random pair order. Mitigation: the pair list is pre-shuffled, so the sequence is random but deterministic per session. With 20 nodes and `win_ratio=0.5`, the giant component typically forms around 10-12 threads (matching Kauffman's N/2 prediction). If testing shows the transition fires too early to be interesting, increase `node_count` to 24 or lower `win_ratio` to 0.6.

## Handoff Prompt

```
You are the Generator. Read and execute plans/0252-genesis-pick-two.md.

Two files to modify:
1. build/puzzle-data.yaml — update pz-sim-t3-001 with new fields (button_label,
   node_count, win_ratio, teaching_text, updated question/hint/gateway_blurb)
2. build/build-puzzles.py — pass new YAML fields in build_json() SIM branch,
   then rewrite initThreads()/addThread() as the Pick Two mechanic (~120 lines).

Core change: "Add Thread" becomes "Pick Two." Each click lifts two random
buttons (and their cluster) briefly before tying. Win condition: the two
selected buttons are ALREADY in the same cluster containing ≥50% of nodes.
Teaching text replaces the flash. Reuse existing union-find utilities.

Run make puzzles and verify all 17 acceptance tests. Report completion.
```
