# Subtask: Abstract Kuhn Cycle Rewrite — Full Pattern Demo

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: abstract cycle demonstrates full anomaly-crisis-shake pattern`
**Read first:** The existing HTML file. Rewrite `buildSegment0Timeline()` function.

## Purpose

The abstract cycle (segment 0) currently just shows 5 phase labels flying to the loop.
Rewrite it to DEMONSTRATE the full revolution pattern using abstract vocabulary.
The reader learns the process here, then recognizes it in each historical example.

## New Abstract Cycle (~30 seconds)

The Kuhn loop is the permanent background (visible at 0.25 opacity from the start).
The abstract cycle traces through the FULL pattern with general words.

### Phase 1: Normal Science (0-4s, blue)

Center stage (48px): "The accepted theory explains everything we see."
Below (24px): "Textbooks are written. Careers are built."
Both shrink + fly to Normal Science position on loop.

### Phase 2: Anomaly Accumulation (4-16s, amber)

Four anomaly-dismissal pairs, each ~3s:

| # | Anomaly (center, amber) | Dismissal (below, muted) |
|---|------------------------|-------------------------|
| 1 | "Something doesn't fit." | "It's probably measurement error." |
| 2 | "It happens again." | "Add a special case to the theory." |
| 3 | "A third anomaly." | "The theory is fine. The data is noisy." |
| 4 | "The special cases outnumber the rules." | "The theory works. Don't question it." |

Each pair shrinks and parks near Anomaly position (scattered, messy — same scatter
pattern as historical revolutions).

### Phase 3: Crisis (16-22s, red)

Two crisis quotes, ~3s each:

1. "Anyone who questions the theory is not a serious scientist."
   → Parks near Crisis position
2. "And yet — someone looks where no one has looked."
   → Parks near Crisis position

Loop is now cluttered with anomalies near Anomaly + crisis items near Crisis.

### Phase 4: Crisis Moment (22-26s, gold)

Center (36px, gold): "An observation the old theory cannot explain."
Extended display (4s). Then shrinks and parks at Crisis position.
Maximum clutter.

### Phase 5: Paradigm Shake (26-28.5s)

A placeholder paradigm text appears in title bar position (or center):
"THE ACCEPTED THEORY" — in white, bold.
It begins to SHAKE (same shake animation as historical revolutions).
Amplitude increases. Text fades slightly. Paradigm crumbling.

### Phase 6: Resolution (28.5-35s)

1. "THE ACCEPTED THEORY" fades out completely (0.5s)
2. All accumulated junk fades out simultaneously (1s)
3. Clean moment (1s) — just the loop, empty and calm
4. "A new theory explains everything — including the anomalies." appears CENTER STAGE (green, 48px, bold) — pop-scale entry, same treatment as every other phase. Reader absorbs (2s).
5. Text SHRINKS and FLIES to the New Paradigm position on the loop (same arc animation as all other phases). Parks there at 16px.
6. This completes the full circle — all 5 positions now have content that arrived via center stage.

**This step is critical.** The New Paradigm must appear big and center, then move to its loop position. The reader sees the FULL cycle: center → loop for every single phase. Don't skip it.

### Phase 7: "You Are Here" (35-37s)

The completed loop with all 5 phase labels at full opacity (fade from 0.25 → 1.0).
Golden pulsing arrow at Anomaly: "YOU ARE HERE"
Resting state.

## Style Notes

- Same scatter/mess aesthetic as historical revolutions
- Same shake animation parameters
- The abstract vocabulary is GENERAL — no specific science, no names, no dates
- The pattern should feel familiar when it repeats with Copernicus, Lavoisier, etc.
- Schoolhouse Rock energy — bold, clear, slightly playful

## Technical Notes

- This replaces the existing `buildSegment0Timeline()` function
- Uses the same helpers (createText, phasePos, etc.)
- Does NOT use the revolution factory function (this is a standalone sequence)
- The paradigm shake here can be simpler since there's no title bar — just create
  a temporary text element that shakes, or use the title bar elements temporarily

## Report

State: segment 0 duration (should be ~34s), what the mess looks like at peak clutter.
