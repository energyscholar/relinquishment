# Subtask A1: JS Animation Engine + Abstract Kuhn Cycle

**Output:** `build/images/scientific-revolutions-draft.html` (overwrite entirely)
**Commit:** `Plan 0321 A1: JS engine + abstract Kuhn cycle`

## What to Build

A single HTML file containing one inline SVG (1200x700 viewbox) with a JavaScript
animation engine. Dark background (#1a1a2e), light text (#e8e0d0), serif font (Georgia).

The file has TWO parts:
1. A timeline scrubber bar at the bottom
2. An animated abstract Kuhn cycle

Nothing else. No chapter text. No historical revolutions. No prose.

## Part 1: Timeline Scrubber

A horizontal bar across the bottom of the SVG. 9 dots evenly spaced.
- Dot 0: "Abstract" — gold, active
- Dots 1-8: labeled "1" through "8" — gray, inactive (placeholder for future subtasks)
- Clicking an active dot jumps the animation to that segment
- A thin progress bar fills left-to-right within the active segment's dot-to-dot span
- Play/pause button (▶/⏸) at left end of the scrubber bar

Implement in JS. The engine must support:
- `playSegment(n)` — play segment n from start
- `seekTo(n, phaseFraction)` — jump to a specific phase within segment n
- `pause()` / `resume()`
- A state machine tracking: current segment, current phase (0-4), playing/paused

## Part 2: Abstract Kuhn Cycle Animation (~15 seconds)

The Kuhn cycle has 5 phases displayed as positions on a large circle/loop:
1. Normal Science (top, blue #4a90d9)
2. Anomaly (right, amber #d4a574)
3. Crisis (bottom-right, red #c45c5c)
4. Revolution (bottom, gold #d4a017)
5. New Paradigm (left, green #5c9c5c)

### Animation Flow

The CENTER of the circle is the stage. One thing at a time. Big, clear, readable.

| Time | What happens |
|------|-------------|
| 0-3s | "NORMAL SCIENCE" appears center stage (48px, blue). Reader absorbs. |
| 3s | Text shrinks to 16px + flies in an arc to its circle position (top). An arc of the circle path draws from start to that position. Label stays. |
| 3-6s | "ANOMALY" appears center (48px, amber). |
| 6s | Shrinks to 16px + flies to circle position (right). Circle arc extends. Now 2 labels on the loop. |
| 6-9s | "CRISIS" appears center (48px, red). Previous labels on the loop are visible — screen getting busier. |
| 9s | Shrinks + flies to position. Circle arc extends. Three labels + arcs visible. Cluttered. |
| 9-11s | "REVOLUTION" appears center (48px, gold, glowing). |
| 11s | GOLDEN FLASH (full-SVG gold overlay, 0.4s). All accumulated labels and arcs on the loop FADE OUT during flash. Screen clears to just the center gold text. Relief. |
| 11-13s | Clean moment. Just "REVOLUTION" glowing center. |
| 13-15s | All 5 labels REDRAW cleanly at their circle positions (fade in, 16px, neat). Complete circle path draws. This is the RESOLVED state — orderly, not cluttered. The contrast with the messy accumulation is the point. |

### The Clutter-to-Clear Principle

This is the core teaching device. As phases accumulate on the loop (Normal → Anomaly → Crisis), the screen gets BUSIER. Small icons, labels, connecting lines pile up. The visual discomfort IS the crisis. Then the Revolution phase CLEARS everything — golden flash, clean slate. The relief IS the revolution. The reader FEELS the pattern before any historical examples demonstrate it.

### After the Abstract Cycle

The resolved Kuhn cycle (all 5 labels, complete circle path) remains visible. After a 1s pause, a pulsing golden arrow appears at the "Anomaly" position with text: "YOU ARE HERE". This is the static resting state.

Clicking Play again replays the full animation from the start.

## Style Notes

- Schoolhouse Rock energy. Bold, fun, slightly exaggerated.
- Text animations: pop-scale on entry (slight overshoot, ease-out)
- Fly-to-position: smooth arc, not straight line (ease-in-out, ~0.5s)
- Golden flash: full-SVG overlay, opacity 0→0.6→0 over 0.4s
- Circle path: dashed or dotted line connecting the 5 positions, draws progressively
- All animations JS-driven (requestAnimationFrame or setTimeout chain)

## Report

After creating, state: total file size, animation duration, what works, what needs polish.
