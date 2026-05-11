# Plan 0320 — Magnetosphere Tutorial v3 (Orientation + Continuity Fix)

**Status:** READY FOR GENERATOR
**Deliverable:** `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html` (replaces v2)

---

## Critical Fix: Orientation Convention

**Sun is ALWAYS left. Magnetosphere nose points LEFT (sunward). Tail extends RIGHT (anti-sunward).**

This must be consistent across ALL four SVGs. In v2, The Breath had a flipped x-axis (`EX - wx * SCALE` instead of `EX + wx * SCALE`), making the entire magnetosphere backwards. The Opening was correct. Use the Opening's convention everywhere.

Solar wind particles always stream LEFT → RIGHT. They arrive from the Sun (left) and hit the nose (left side of magnetopause). This is non-negotiable.

## Critical Fix: Visual Continuity

Each SVG must visually connect to the next. The reader should recognize "this is a detail view of THAT thing I just saw." Technique: each animation's starting frame matches (or references) the previous animation's end frame, with a highlighted region showing where the zoom goes next.

Progression:
1. Opening ENDS at full magnetosphere view (nose left, tail right, breathing)
2. Gate STARTS showing the same full magnetosphere, highlights the dayside nose region, then ZOOMS IN to show reconnection detail there
3. Circuit STARTS showing recognizable Earth with MS overlay (same shape as Opening's end-state), then reveals the current paths flowing within it
4. Breath shows the same full MS view (same shape/orientation as Opening end-state) but now animated through the substorm cycle

The viewer should feel: "Oh, that small part of the big picture is now being shown up close."

## The Opening — Camera as Spaceflight

**Layout:** The Opening SVG is the FIRST thing on the page. The title ("The Magnetosphere / Earth's invisible ocean") overlays the TOP of the SVG as a heading — both are at the same position. No separate header section above it. The SVG starts at the top of the page, behind the title.

**Narration:** The intro text ("One hundred and fifty million kilometres away, the Sun exhales...") does NOT appear as a separate text section. Instead it appears as pop-up narration WITHIN the animation, in dead space, timed to the camera journey. Narration fades in/out as the camera moves.

**Field lines near title:** Ensure no blue field lines cross behind the title text at the top of the frame. Clip or suppress elements in the title zone.

**Camera path (spaceflight, not just pan/zoom):**

The viewer is FLYING THROUGH SPACE. The camera has a 3D trajectory:

1. **Approach Sun** (5-8s): We fly TOWARD the Sun. It grows from a point to fill maybe 30% of frame. Corona visible. Solar wind emitting outward. The viewer feels forward motion.

2. **Turn toward Earth** (3-5s): Camera turns. Sun rolls off the left side of frame. We're now facing the direction the solar wind is traveling. Stars drift.

3. **Follow the solar wind** (5-8s): We're traveling WITH the wind toward Earth. Particles stream past/beside us. Earth appears as a dot ahead, growing. Centered in frame.

4. **Front view of magnetosphere** (5-8s): Earth fills center of frame. We see the MS HEAD-ON — a roughly circular shield. Solar wind deflects AROUND it (particles streaming past to the sides). Bow shock visible as a shell in front. This view is intuitive: "oh, it's a shield." Hold.

5. **Pan to side view** (5-8s): Camera arcs around to the classic side view. Sun now far off-screen left. Tail extends rightward. Moon orbit visible. This is the textbook view but we EARNED it by arriving cinematically.

6. **Fast time with Moon** (5-8s): Show several lunar orbits (Moon circling). MS "dancing" — breathing fast with solar wind variations. The system is alive and rhythmic.

7. **Slow time, zoom to detail** (5-8s): Time slows. Zoom into the interesting part of the MS (dayside boundary where reconnection happens — setup for the Gate). Labels appear: bow shock, magnetopause, plasma sheet, cusps.

Total: ~40-50 seconds. Repeat button at end. Distance and time indicators throughout.

The viewer's experience: "I just flew from the Sun to Earth and watched the magnetosphere form around me."

## The Gate — Pedagogy First, Mechanism Second

v2/v3 problem: Gate shows context briefly then jumps to the abstract reconnection diagram. Reader doesn't understand WHY this matters or what's at stake.

**Principle:** Setting up WHY we care about the gate is MOST of the pedagogy. The actual mechanism (X-line, field lines merging) is a small, simple thing once the context is established.

**Structure:**

1. **Context from Opening** (3-5s): Show the full magnetosphere (same shape as Opening's end-state). Dayside magnetopause highlighted. Text overlay: "This boundary holds. Until it doesn't."

2. **The sealed vessel** (5-8s): Show solar wind streaming past the magnetosphere. Everything deflects. The boundary is closed. Nothing gets in. IMF arrows pointing NORTHWARD (parallel to Earth's field). The system is stable. Build the reader's understanding: "OK, so normally this is just a shield."

3. **The southward turn** (3-5s): IMF arrows rotate to point SOUTHWARD. Visual cue — color shift, warning. Something is about to change. "But when the Sun's field points the other way..."

4. **The gate opens** (5-8s): NOW zoom to the dayside nose. Show the actual reconnection — opposing field lines approach, merge at X-point, reconfigure. Energy release flash. But this is the PAYOFF after context, not the opening move.

5. **Consequence** (3-5s): Zoom back out slightly. Show open field lines now draped over poles. The sealed vessel is breached. Solar wind energy pours through. This connects to the next section (Circuit).

Total: ~20-30 seconds. Paused at start (play button). The reader must EARN the reconnection by first understanding the sealed state.

The viewer's experience: "Oh — it's normally sealed, but when the field flips, the boundary breaks, and energy floods in. THAT's why this matters."

## The Circuit — Recognizable Earth + Camera Movement

v2 problem: Earth looks blobby. Circuit exists in isolation. No sense of scale or spatial context.

v3 produced a good Circuit (Bruce: "much better, very nice!"). v4 enhancement: add camera movement.

**Requirements:**

1. Earth is RECOGNIZABLE: Sphere with continent suggestions (simple land shapes, blue/green). Slowly rotating. Reader instantly thinks "that's Earth."
2. Magnetosphere as transparent overlay: Magnetopause boundary visible as translucent shell (same shape as other SVGs).
3. Show the DRIVER: Solar wind from left → reconnection at nose → open field lines over poles → current driven down.
4. Circuit path: Current down field lines, across ionosphere (Pedersen current), back up. Animated dots/dashes.
5. Aurora glow where current enters ionosphere.
6. Labels: "Birkeland current ↓/↑", "Pedersen current" (NOT "R1").

**Camera movement (new):**

The Circuit should NOT be a static view. Camera moves to show spatial relationships:

1. **Wide view** (5-8s): Show the full system — Earth centered, magnetosphere envelope visible, bow shock, Sun direction indicated off-left. The reader sees WHERE the circuit sits relative to the whole MS.
2. **Rotate/tilt** (3-5s): Camera arcs to show the 3D nature — the circuit is a LOOP in 3D space, not a flat schematic. Show the oval auroral zone from a slightly tilted perspective.
3. **Zoom in** (5-8s): Push in to the current paths. See the dots flowing. See individual Birkeland currents descending into the polar ionosphere. Aurora glow visible.
4. Optional: zoom back out briefly to re-establish context, then loop.

Scale references visible: Earth-Moon distance indicator, bow shock position, direction to Sun.

Starts PAUSED. Gentle continuous loop once playing.

The viewer's experience: "This circuit is ENORMOUS — here's where it sits in the magnetosphere — and here's the current flowing down into the atmosphere right now."

## The Breath — Substorm Cycle (Correct Orientation)

v2 problems: (a) x-axis flipped (magnetosphere backwards), (b) Earth at x=350 in 1600-wide viewport (too far left, tail goes off-screen left).

v3 requirements:

1. **Correct orientation:** Use SAME w2s convention as Opening. Sun/solar wind from LEFT. Nose LEFT. Tail RIGHT. 
2. **Composition:** Earth roughly centered vertically and positioned at ~25-30% from left (enough room for the tail to extend rightward without going off-screen).
3. **Same MS shape** as Opening end-state — viewer recognizes "same system, now I'm watching it change over time."
4. Phase animation (30 seconds):
   - Growth: tail stretches rightward, plasma sheet thins, energy loading. Kp indicator: Quiet→Active.
   - Expansion: near-Earth neutral line forms, dipolarization front races earthward (rightward-to-leftward), aurora flares. Kp: Active→Storm.
   - Recovery: tail relaxes, aurora dims, system resets. Kp returns toward Quiet.
5. AE index plot (small, corner) with scanning cursor showing current phase.
6. Space weather indicator (Kp bar).
7. Phase label (Growth / Expansion / Recovery).
8. Plays once, holds at end, Repeat button appears.

## Critical Technical Constraint: Animation Performance

v2's Opening zoom was BROKEN in browser. Cause: clearing and recreating all SVG DOM elements every frame (60fps DOM thrashing). 

v3 MUST use a performant animation approach. Options (choose one):

**Option A (recommended): Animated SVG viewBox + pre-built scene layers.**
Draw all detail layers once into nested `<g>` groups at correct world positions. Animate the SVG `viewBox` attribute itself to create zoom/pan. Each layer has opacity tied to viewBox state. No DOM creation per frame — only attribute updates. This is how SVG was designed to zoom.

**Option B: CSS transforms on `<g>` groups.**
Draw scene elements into groups. Apply CSS `transform: translate() scale()` to the root group, animated via JS. Still no DOM recreation — just transform updates.

**Option C: Canvas 2D (for complex particle systems only).**
If particle count makes SVG impractical, use a `<canvas>` overlay for particles only. Keep structural elements (magnetopause, field lines, labels) in SVG.

DO NOT rebuild the SVG DOM tree every frame. That approach does not produce smooth animation in any browser.

## Shared Technical Notes

- viewBox 1600×900 for full-viewport scenes, ~1100×600 for wide scenes
- Pre-build SVG elements; animate via attribute changes and transforms
- `prefers-reduced-motion`: pause all on load (check `window.matchMedia`)
- Star canvas background (from v2 — keep it)
- CSS: dark theme #0a0a1a, vars for palette, text column 680px, SVGs break out to full width
- File size budget: 80-120KB
- Opening: AUTO-PLAYS on page load. Repeat button appears at end.
- Gate, Circuit, Breath: ALL START PAUSED (play button visible). Reader scrolls at own pace, clicks play when ready.
- Pause/play toggle on all SVGs.
- Fullscreen toggle (⛶) top-right.

## Text (~500 words)

Keep the nature-documentary register from v2 — it worked. Brief connective text between SVGs. The visuals carry the teaching; text provides emotional resonance and names the phenomena.

Closing sentence: "This is happening right now, above your head, whether anyone is watching or not."

## Puzzle Slots

Keep the `<div class="puzzle-slot" data-topic="..."></div>` pattern from v2.

## Generation Footer

Same pattern as v2 — gold rule, short prompt, "that's the whole prompt" framing, accordion with full plan.

Short prompt for reader display:
```
"Magnetosphere tutorial. Cinematic journey from Sun to aurora.
 Full-viewport animated SVGs. Visual continuity between scenes.
 Show don't tell."
```

## What Worked in v2 (Preserve)

- Camera keyframe system with easing
- Catmull-Rom interpolation for smooth paths
- Shue-model boundary shapes (parametric magnetopause/bow shock)
- Dipole field line parametrization (L-shell)
- Cross-fade between detail layers via opacity
- Solar wind particle deflection at bow shock
- Phase-based substorm animation with continuous variables
- AE index plot with scanning cursor
- Star canvas background
- Animation state management pattern (animRunning, animStart, toggleAnim, restartAnim)

## What Must Change from v2

1. Breath: flip x-axis to match Opening convention
2. Breath: center composition (Earth at ~25-30% from left)
3. Opening: smooth travel from Sun to Earth (not a jump)
4. Opening: FIX BROKEN ANIMATION — do NOT rebuild DOM every frame (see Technical Constraint above)
5. Gate: add context-first zoom (show where on MS this happens)
6. Circuit: recognizable Earth (rotating sphere with continents)
7. Circuit: show solar wind driving the circuit
8. Circuit: drop "R1" labels → "Birkeland current"
9. All: visual continuity between consecutive SVGs
10. All: use performant animation (viewBox animation or CSS transforms, not DOM thrashing)

## Context

The best tutorials in ~/software/has-anyone-looked/tutorials/ were generated in ONE pass with no refinement. This is the third iteration of this tutorial. The quality bar is: get it right on this pass. Study the reference tutorial (solar-wind-coupling.html) for animation technique — it uses JS-driven attribute updates on pre-existing DOM elements, NOT per-frame DOM recreation.
