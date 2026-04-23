# Plan 0222b — Kauffman Filmstrip Polish (Analogy Correction + Visual Refinement)

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor
**Priority:** Low
**EV:** Stable — corrects analogy accuracy (T3 improvement), no F-mode triggers
**Scope:** `build/preprocess.py` (filmstrip SVG constants only)
**Phase:** 2 of 3 (0222a scaffold DONE → 0222b filmstrip polish → 0222c domain polish)

## Analogy Corrections

The 0222a scaffold got the Kauffman sequence slightly wrong. The correct process:

1. **Scatter** — Ten thousand buttons on the floor. (Correct in 0222a.)
2. **Tie** — Pick up two buttons at random. Tie them together with a thread. Toss them back. (0222a showed "connecting" on the floor — the action is pick-up/tie/toss-back.)
3. **Repeat** — Do step 2 about 4,800 times (almost half of 10,000). Early on, picking up a button might lift a small clump. Toward the end, you start picking up clusters.
4. **Phase transition** — Pick up one button **from the middle** and the **whole net** lifts, hanging down on **both sides** like a net being hauled up. That's emergence.

### Caption fixes needed:
- Panel 2 caption "Pick up one button. Only its partner lifts." — **Wrong.** This describes the tying step, not an observation. Should describe what you see when you pick up a random button early: you get a small clump at most.
- Panel 4 visual — buttons should cascade **down from center**, hanging on both sides, not cascading from one end. The lift point is a button near the middle of the x-range.

## Revised Panel Structure (5 panels)

Split the middle into early-clusters and late-clusters to show the slow buildup before the snap.

### Panel 1: "Scatter" (unchanged)
- 30 buttons on floor. 0 threads.
- Counter: `0 / 30`
- Caption: *"Ten thousand buttons on a floor."*

### Panel 2: "Tie and toss"
- 30 buttons on floor. 6 threads visible (representing early ties).
- Show the action: two buttons slightly lifted above the floor (y≈220) as if being picked up to tie, connected by a fresh thread. The rest on the floor with a few existing threads between floor-level pairs.
- Counter: `6 / 30`
- Caption: *"Pick up two at random. Tie them together. Toss them back."*

### Panel 3: "Early clusters"
- 30 buttons, 10 threads. Small clusters (2s and 3s). Pick up one button and maybe its partner lifts. Nothing dramatic.
- One pair lifted: button at y≈185, partner at y≈200. Everything else on the floor.
- Counter: `10 / 30`
- Caption: *"A few hundred ties in. Small clumps — two, three buttons."*

### Panel 4: "Growing clusters"
- 30 buttons, 14 threads. Ratio 14/30 = 0.47, just below threshold. Several clusters (sizes 3, 4, 5, 8). Largest cluster lifted from one button — 5-6 buttons dangle. Two large clusters are near each other but visibly disconnected (setup for Panel 5).
- Counter: `14 / 30`
- Caption: *"Almost halfway. The clusters are getting bigger."*

### Panel 5: "Phase transition"
- 30 buttons, 15 threads (14 grey + 1 red). Ratio = 0.50.
- **Lift point:** A button near x≈250 (center of the layout), lifted to y≈45.
- **Net shape:** Buttons hang **down on both sides** from the center lift point, like a fishing net hauled from its middle. Leftmost connected buttons dangle at y≈180-200 on the left, rightmost at y≈180-200 on the right. The visual is a **catenary/V-shape** — highest in the center, drooping to both sides.
- 22-25 buttons connected and lifted. 5-8 isolated buttons remain on floor.
- The one red thread is the bridge that completed the giant component.
- Counter: `15 / 30` (15 in red/bold)
- Caption: *"One more thread. Pick up one button — the whole room lifts."*

## Changes

### 1. `build/preprocess.py` — Replace filmstrip panels

Replace the current 4-panel filmstrip code with 5 panels per the revised structure above. The injection function signature, marker detection, and figure wrapper remain identical — only the SVG content changes and one additional panel is added.

**Button positions:** Use natural-looking scatter (not grid). The x_positions from 0222a are acceptable as a starting point but should be jittered slightly for organic feel.

**Panel 5 cascade geometry:** The lift point button is near the center. Connected buttons hang in a V/catenary:
- Buttons directly connected to the lift point: y ≈ 80-100
- Buttons one hop away: y ≈ 120-140
- Buttons two hops away: y ≈ 150-170
- Buttons at the extremes of the chain: y ≈ 185-200
- Thread angles should be taut (straight lines from each button to its connected neighbors)

**Figcaption update:** Change from "scatter, connect, cluster, snap" to: *"Kauffman's buttons and threads — scatter, tie, cluster, snap."*

### 2. No other changes

- Injection logic unchanged
- `inject_domain_buttons()` unchanged
- No manuscript changes

## Acceptance Tests

1. **5 panels:** The filmstrip container now contains exactly 5 `<svg` elements
2. **30 buttons each:** Each panel has exactly 30 circles, r=9
3. **Thread counts:** Panel 1: 0. Panel 2: 6. Panel 3: 10. Panel 4: 14. Panel 5: 15 (14 grey + 1 red)
4. **Red thread:** Panel 5 has exactly one `<line` with stroke="#c0392b"
5. **Counter in Panel 5:** Shows `15 / 30` in red/bold
6. **Lift-from-center:** In Panel 5, the highest button (lowest y value) has an x coordinate between 200 and 300 (center region)
7. **V-shape cascade:** In Panel 5, buttons with x < 150 and x > 350 have y values > 170 (edges hang lower)
8. **Captions correct:** Panel 2 contains "Tie them together", not "Only its partner lifts"
9. **Figcaption:** Contains "scatter, tie, cluster, snap" (not "connect")
10. **Build succeeds:** `make html` exits 0
11. **Domain diagram unaffected:** `grep -c 'domain-buttons' output.html` still returns ≥1
