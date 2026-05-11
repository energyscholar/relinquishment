# Subtask: Visual Cycle — Title Fix, Title Bar Positioning, Green→Blue Transition

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fix title, separate title bar from loop, green-to-blue cycle transition`
**Read first:** The CURRENT state of the file.

## Change 1: Fix Title

Line ~328: change `"The Kuhn Cycle"` to `"The Structure of Scientific Revolutions"`.
Line ~6: change `<title>` to match.

## Change 2: Title Bar Background Panel

The white 26px old paradigm text at y=50 completely covers the blue "NORMAL SCIENCE"
loop label at phasePos(0) which is at y=40 (top of circle). These are different
visual layers that shouldn't overlap.

**Fix:** Add a semi-transparent dark background rectangle to `titleBar`, inserted
as the FIRST child (behind the text). This visually separates the title bar from
the loop beneath it.

In the SVG markup (inside the `<g id="title-bar">`), add before the text elements:
```xml
<rect x="100" y="5" width="1000" height="85" rx="8" fill="rgba(26,26,46,0.85)"/>
```

This creates a dark panel behind the title text. The loop's NORMAL SCIENCE label
at y=40 is now visible BELOW this panel — it sits on the loop circle at the edge
of the dark area. The title bar text reads clearly on its own background.

## Change 3: Old Paradigm Position Matches New Paradigm Position

The old paradigm at the START of each revolution should occupy the SAME position
and size that the new paradigm will occupy at the END. This way, the viewer literally
sees the new paradigm take the old one's place.

Currently:
- titleLine2 (old paradigm): y=50, 26px
- titleLine3 (new paradigm after replacement): y=78, 28px

**Fix:** Unify them. Both should use y=60, 26px. Change:
- titleLine2: y=50 → y=60 (in factory setup keyframe AND segment 0 setup)
- titleLine3: y=78 → y=60 (but only appears AFTER titleLine2 is struck/faded)
- titleStrike: y values match titleLine2's new position (y1=60, y2=60)
- "OLD PARADIGM" label: y=33 → y=43 (stays above titleLine2)
- titleLine1 (revolution name): stays at y=22

The title bar background rect: adjust height if needed to contain y=22 through y=60.

In the death sequence replacement, when titleLine2 fades and titleLine3 appears:
- titleLine2 fades to 0 (not just 0.25 — fully hidden)
- titleLine3 appears at y=60 (same spot), green, 26px
- The text literally REPLACES the old text in the same space

## Change 4: Green → Blue Color Transition

After the new paradigm appears green at y=60 and the 3.5s hold completes,
add a 2s color transition where titleLine3 fill changes from green (#5c9c5c) to
blue (#4a90d9). This shows the new paradigm BECOMING the next era's orthodoxy —
the revolutionary idea becomes normal science.

Add a new keyframe after the hold:
```javascript
kf.push({ t: holdEnd, dur: 2, fn(p) {
  const t = easeInOutCubic(p);
  const r = Math.round(92 + (74 - 92) * t);
  const g = Math.round(156 + (144 - 156) * t);
  const b = Math.round(92 + (217 - 92) * t);
  titleLine3.setAttribute("fill", `rgb(${r},${g},${b})`);
}});
```

After the transition, the text sits there in blue — it IS the new normal science.
Then the segment ends and the next revolution begins. Update timing constants
to account for the +2s.

## Change 5: Segment 0 Title

In segment 0 setup (line ~328), the title is now "The Structure of Scientific
Revolutions" (Change 1). The old paradigm text ("The accepted theory explains
everything we see.") should use the same y=60 position as the factory revolutions.

## Change 6: Transition Years Display — Concurrent, Not Separate

Currently `transitionYears` appears as a tiny muted center-stage text (16px, 0.6
opacity) in its own step. Change: display it CONCURRENT with the green→blue
transition, positioned in the lower center area (CX, CY + 100), slightly larger
(20px), at 0.7 opacity. It should fade in during the hold (step 5 of the
replacement sequence) and persist through the green→blue transition.

Example display: "~150 years" appears below center while the new paradigm sits
green at top, stays visible as it transitions to blue. The reader absorbs both:
THIS is the new paradigm, and it took THIS long.

Move the transition note keyframe so it starts at the beginning of the hold
(concurrent), not as a separate sequential step. Remove the `clearCenter()` call
from the transition note — other center-stage content may still be visible.

Also verify the transitionYears values are historically accurate:
- Heliocentrism: "~150 years" (1543→1687) ✓
- Oxygen: "~19 years" (1770→1789) — should be "~17 years" (1772→1789)
- Evolution: "~122 years" (1831→1953) — should be "~94 years" (1859 Origin → 1953 Modern Synthesis publication) or keep as-is if counting from Beagle voyage
- Germ Theory: "~38 years" (1847→1885) ✓
- Relativity: "~32 years" (1887→1919) ✓
- Quantum: "~27 years" (1900→1927) ✓
- Plate Tectonics: "~56 years" (1912→1968) ✓
- DNA: "~9 years" (1944→1953) ✓

Only fix Oxygen if it says 19 (should be 17).

## Do NOT

- Change the death sequence order
- Change animation logic beyond what's specified
- Remove any existing visual elements

## Report

State: confirm title fixed, confirm title bar has dark background, confirm old/new
paradigm share same position (y=60), confirm green→blue transition works, confirm
transitionYears displays concurrently with hold, updated per-segment durations.
