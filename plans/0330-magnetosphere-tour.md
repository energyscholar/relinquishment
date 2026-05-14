# Plan 0330: Our Neighborhood — A Magnetosphere Tour

## Context

Bruce's animated magnetosphere tutorial received positive reviews from multiple sources. This plan extends the concept to a multi-stop tour of five solar system magnetospheres, using Carl Sagan's narrative style ("Ship of the Imagination") with full scientific accuracy maintained via visible scale/time indicators and a telescope metaphor.

The tour is adjunct to the book — a standalone artifact linked from "The Wrong Substrate" section. It demonstrates that magnetospheres are universal structures with dramatic variation, reinforcing the book's thesis about substrate-independent phenomena.

## Design Philosophy

### The Sagan Register

Carl Sagan's Cosmos established the template:
- **First person plural** — "we," "our" — the viewer is a participant, not an observer
- **Wonder before data** — lead with what's extraordinary, then explain why
- **Scale as narrative device** — "If the Earth were the size of a marble..." — make the incomprehensible visceral
- **Historical human stories** — who discovered this, what did they expect, what surprised them
- **Gentle correction** — "Space is not what the movies taught you. Space is patience."
- **Philosophical return** — start from home, travel outward, come back to what it means
- **Comfortable silence** — moments where the visual speaks and the text is absent

Text narration appears as overlays timed to animation phases. No rendered character — Carl is a voice (text), not a figure. The narration IS Carl.

### Scientific Accuracy Framework

The accuracy problem: real distances span 7 orders of magnitude (Ganymede's 5,000 km magnetosphere vs the 120 AU heliosphere). Real travel times at 1G acceleration span days. Traditional documentaries fake both. We don't.

**The solution: three always-visible instruments.**

1. **Distance scale bar** — shows current spatial scale (km, RE, RJ, AU). Updates continuously. When we zoom, you see the scale change.
2. **Time multiplier** — shows current time compression (1x, 100x, 10,000x, etc.). When we speed up to cross interplanetary space, you see the multiplier change.
3. **Telescope magnification** — shows current zoom level (1x, 10x, 100x). When we zoom into a distant target, you see the magnification.

These three indicators mean we never cheat. Every visual choice is transparent. The viewer always knows what they're looking at and how it's been adjusted for viewing. This IS the innovation — cinematic quality with scientific honesty.

### The Spacecraft

Unnamed research vessel (keeps focus on the tour, not the ship). Capabilities:
- Main viewport (the animation frame)
- Adjustable telescope (zoom/magnification — narrative justification for scale changes)
- Magnetometer (field strength overlay — color-coded field lines)
- Plasma analyzer (density/composition readouts)
- "Deep scan" mode (cutaway views showing internal structure — sci-fi but honest about being interpretive)
- 1G acceleration drive (physics-accurate travel between stops)

The ship is rendered as a small, clean silhouette — not the focus. When stationary at a magnetosphere, the ship icon is in a corner showing our vantage point. During transit, the ship is centered with the destination ahead.

## Narrative Arc

### The Journey

| Segment | Stop | Key Feature | Emotional Register |
|---------|------|-------------|-------------------|
| 1 | Earth | The familiar — set up concepts | Home, recognition |
| 2 | Transit | Crossing the void | Patience, scale |
| 3 | Jupiter | The giant — everything bigger | Awe, overwhelm |
| 4 | Ganymede | Magnetosphere within magnetosphere | Surprise, intimacy |
| 5 | Saturn | Delicate vs violent (Enceladus vs Io) | Beauty, contrast |
| 6 | Heliosphere | The biggest one — pull all the way back | Perspective, return |

This follows the Cosmos pattern: familiar → outward → exotic → intimate → vast → philosophical return.

### Travel Physics (1G acceleration, flip at midpoint)

| Leg | Distance | Travel time | Max velocity |
|-----|----------|-------------|-------------|
| Earth → Jupiter | 4.2 AU | ~6.6 days | 2,770 km/s (0.9% c) |
| Jupiter → Saturn | 4.3 AU | ~6.0 days | 2,830 km/s |
| Saturn → Heliosphere edge | ~85 AU | ~25 days | 12,600 km/s |

Transit segments are compressed (time multiplier visible) but the physics is real. The scale indicator shows AU counting up. Stars barely move — accurate and worth narrating.

## File Structure

```
~/software/has-anyone-looked/tutorials/
  tour-magnetospheres.html        — hub page (tour overview, navigation, context)
  tour-01-earth.html              — Earth's magnetosphere
  tour-02-jupiter.html            — Transit + Jupiter + Io torus + Galileo
  tour-03-ganymede.html           — Ganymede's mini-magnetosphere (inside Jupiter)
  tour-04-saturn.html             — Transit + Saturn + Enceladus
  tour-05-heliosphere.html        — Transit + full heliosphere + Voyager + finale
```

Each file is self-contained HTML+SVG+CSS (same pattern as existing tutorials). The hub page provides context and links. Each segment ends with a "Continue →" link to the next.

## Storyboard: Segment by Segment

### Segment 1: Earth (tour-01-earth.html)

**Opening scene:** Black. Stars appear. A pale blue dot grows.

Carl: "We begin where all great journeys must — at home."

**Scene 1.1 — Approach** (~30s)
- Earth grows from point to disk. Moon visible.
- Telescope magnification increases (1x → 5x → 20x).
- Scale bar transitions from AU to thousand-km to RE.

**Scene 1.2 — Magnetosphere revealed** (~45s)
- Magnetometer activates. Field lines appear — dipolar near Earth, compressed on dayside, stretched into tail on nightside.
- Carl: "What you're seeing is invisible. No human eye has ever seen a magnetic field. But our instruments can, and what they reveal is a cathedral of force — sculpted by the solar wind into a shape no one predicted until they measured it."
- Solar wind particles stream in from the left. Bow shock appears.
- Labels appear: bow shock, magnetopause, plasmasphere, radiation belts, tail.

**Scene 1.3 — The substorm** (~30s)
- Tail stretches, reconnects, brightens. Aurora appears at poles.
- Carl: "Every few hours, the tail breaks. Stored energy releases toward the poles. On the ground, this is an aurora. From here, it's a magnetic earthquake."
- Brief sensor overlay: field strength graph showing the sudden change.

**Scene 1.4 — Departure** (~20s)
- Camera pulls back. Earth shrinks. Scale bar transitions to AU.
- Carl: "Earth's magnetosphere extends perhaps 60,000 kilometers sunward. A respectable bubble. What lies ahead dwarfs it by a factor of one hundred."
- Time multiplier appears: "1x → 1000x → 100,000x"
- Jupiter appears as a bright point ahead.

**End: "Continue to Jupiter →"**

---

### Segment 2: Jupiter (tour-02-jupiter.html)

**Scene 2.1 — Transit** (~20s)
- Ship centered. Distance counter climbs (AU). Time multiplier visible (100,000x).
- Stars don't move (accurate). Jupiter's point brightens slowly.
- Carl: "At one gravity of acceleration — the comfortable pull you feel standing on Earth — Jupiter is six days away. In those six days, nothing happens. The stars barely shift. Space is not what the movies taught you. Space is patience."
- Midpoint: ship rotates 180° for deceleration (accurate).

**Scene 2.2 — Jupiter approach** (~30s)
- Telescope increases magnification. Jupiter resolves from point to disk.
- Galilean moons visible as points. Scale bar transitions to RJ.
- Carl: "Jupiter's magnetosphere is the largest structure in the solar system. If you could see it from Earth, it would appear larger than the full Moon."

**Scene 2.3 — Io plasma torus** (~45s)
- Enter magnetosphere. Field lines appear — nothing like Earth's dipole. Distorted, massive.
- The Io plasma torus appears — a glowing doughnut tilted to the equatorial plane.
- Carl: "Io — Jupiter's innermost large moon — is the most volcanically active body in the solar system. Its volcanoes eject sulfur dioxide into space. Jupiter's magnetic field captures this material and sweeps it into a torus — a doughnut of plasma rotating with the planet every ten hours. One hundred million tons of ionized sulfur, glowing in ultraviolet."
- Deep scan: cutaway showing torus cross-section with density gradient.
- Io visible as a small disk with active volcanic plumes.

**Scene 2.4 — Galileo's crossings** (~30s)
- Ship moves to Galileo's orbital path.
- Carl: "From 1995 to 2003, the Galileo spacecraft crossed Jupiter's magnetosphere at least 16 times. Each crossing took weeks. Each one measured something different."
- Galileo spacecraft icon appears (accurate shape — the deployed high-gain antenna dish that failed to open, the asymmetric boom). Its orbital path traces through the magnetosphere.
- 16 crossing points marked along the path with year labels.
- Sensor overlay: magnetic field measurements from actual Galileo data (stylized).

**End: "We don't leave Jupiter. Not yet. Something smaller awaits. →"**

---

### Segment 3: Ganymede (tour-03-ganymede.html)

**Scene 3.1 — Descent to Ganymede** (~20s)
- Telescope zooms in toward Ganymede. Scale bar transitions from RJ to RG.
- Carl: "Ganymede is the largest moon in the solar system — larger than Mercury. But that's not why we're here."

**Scene 3.2 — The nested magnetosphere** (~45s)
- Ganymede's own magnetic field appears — a small dipole INSIDE Jupiter's giant field.
- Carl: "Ganymede has its own magnetosphere. Not borrowed from Jupiter. Its own. Generated by an iron core, just like Earth's. A magnetosphere inside a magnetosphere. The only moon in the solar system with this distinction."
- Split view: Jupiter's field (background, large scale) and Ganymede's field (foreground, small scale). The boundary between them is visible.
- Carl: "At this boundary, Jupiter's field and Ganymede's field collide. The physics is the same as Earth's magnetopause — magnetic pressure balancing plasma pressure. But the scale is 1,000 times smaller, and it's happening inside another magnetic field entirely."
- Deep scan: Ganymede cross-section showing iron core, liquid water ocean (suspected), ice shell, and the field emanating from the core.

**Scene 3.3 — The JUICE mission** (~15s)
- Carl: "ESA's JUICE spacecraft arrives at Ganymede in 2031. It will orbit this moon and map this nested magnetosphere in detail. For now, we have Galileo's flybys — three passes, enough to know the field exists, not enough to understand it fully."
- Brief: what JUICE will measure.

**Scene 3.4 — Departure from Jupiter** (~15s)
- Camera pulls back from Ganymede → Jupiter system → departure.
- Scale bar returns to AU. Time multiplier climbs.
- Carl: "We leave the largest magnetosphere for one that is, in some ways, more beautiful."

**End: "Continue to Saturn →"**

---

### Segment 4: Saturn (tour-04-saturn.html)

**Scene 4.1 — Transit** (~15s)
- Similar to Jupiter transit but shorter narration.
- Carl: "Saturn is only slightly farther from Jupiter than Jupiter is from us. Six more days."

**Scene 4.2 — Saturn approach** (~30s)
- Saturn resolves with rings. Rings are NOT the magnetosphere — worth narrating.
- Carl: "The rings are not the magnetosphere. They are ice and rock, orbiting within it. The magnetosphere extends far beyond the rings — roughly 20 Saturn radii on the dayside, further than the eye naturally draws."
- Magnetometer activates. Saturn's field appears — remarkably symmetric, nearly perfectly aligned with the rotation axis (unusual, worth narrating).
- Carl: "Saturn's magnetic field is almost perfectly aligned with its rotation axis. This should not be possible — dynamo theory predicts a tilt. Saturn refuses to cooperate with our theories. This has troubled physicists for decades."

**Scene 4.3 — Enceladus** (~45s)
- Zoom toward Enceladus. Tiny moon.
- Water geysers erupt from the south pole — jets of water ice reaching hundreds of kilometers into space.
- Carl: "Enceladus is 500 kilometers across. The distance from San Francisco to Los Angeles. From its south pole, geysers of liquid water erupt through cracks in the ice, feeding particles directly into Saturn's magnetosphere. Where Io screams with sulfur volcanoes, Enceladus whispers with water."
- The E-ring appears — a faint, diffuse ring fed by Enceladus's geysers.
- Carl: "The material from these geysers creates Saturn's E-ring — the largest and most diffuse planetary ring in the solar system. One small moon, feeding an entire ring system."
- Cassini spacecraft path visible. Carl: "Cassini flew through these geysers. Tasted the water. Found salt, silica, and molecular hydrogen — signatures consistent with hydrothermal vents at the bottom of Enceladus's ocean."

**Scene 4.4 — Contrast** (~15s)
- Split panel: Io (violent, sulfur, Jupiter) vs Enceladus (delicate, water, Saturn).
- Carl: "Two moons. Both feeding their planet's magnetosphere. One with fire. One with water. The same physics, expressed through utterly different chemistry."

**End: "One more stop. The biggest one. →"**

---

### Segment 5: Heliosphere (tour-05-heliosphere.html)

**Scene 5.1 — Pulling back** (~30s)
- Camera pulls back from Saturn. All planets visible as points.
- Scale bar climbs through AU rapidly. 10 AU... 50 AU... 100 AU.
- Carl: "We've been touring magnetic bubbles inside a magnetic bubble. The Sun has its own magnetosphere. We call it the heliosphere, and it is the largest structure created by our star."
- The heliosphere boundary appears — the termination shock, the heliosheath, the heliopause.

**Scene 5.2 — Structure** (~30s)
- The heliosphere shape: blunt nose facing the interstellar wind, elongated tail.
- Carl: "The heliosphere is shaped by the same physics as Earth's magnetosphere — a flow of particles (interstellar medium) compressing a magnetic field (the Sun's). The shapes are analogous. The scale is not. Earth's magnetosphere extends 60,000 kilometers. The heliosphere extends 120 AU — nearly 18 billion kilometers."
- Sensor overlay: solar wind speed, density, magnetic field strength — all decreasing outward.
- Termination shock labeled: where solar wind drops below the speed of sound.
- Heliopause labeled: where solar wind meets interstellar medium.

**Scene 5.3 — Voyager** (~30s)
- Voyager 1 and Voyager 2 positions marked.
- Carl: "Two spacecraft have crossed this boundary. Voyager 1, in 2012. Voyager 2, in 2018. They are the only human-made objects in interstellar space. Their instruments still transmit. Their signal, after 22 hours of travel at the speed of light, is received by antennas on Earth with a power of 10^-16 watts — ten billion times weaker than the power needed to operate a digital watch."
- Voyager's golden record briefly visible. Carl: "They carry a message. A gold record with greetings in 55 languages, music by Bach and Chuck Berry, and an image of a woman nursing a child. A message in a bottle, thrown into an ocean we have barely begun to map."

**Scene 5.4 — Finale: The return** (~30s)
- Camera continues pulling back. The heliosphere becomes a point.
- Then reversal: zoom back in. Through the heliosphere. Past Saturn. Past Jupiter. Past Earth's magnetosphere. Down to the surface.
- Carl: "Five magnetospheres. Five variations on a single theme: a magnetic field, deformed by a flowing plasma, creating a boundary between inside and outside. Earth, Jupiter, Ganymede, Saturn, the Sun itself. The physics is the same. The scale varies by a factor of ten million. The substrates — iron cores, metallic hydrogen, solar convection — could not be more different. And yet the structures rhyme."
- Final frame: Earth from the surface. Stars above. The magnetosphere — invisible but present.
- Carl: "The longest journey in science is the one from seeing something to understanding it. We have seen these structures. We are still on the journey."

**End: Credits, links to data sources, link back to book.**

---

## Implementation Approach: Storyboard-First

### Phase 0: Wireframe storyboard (THIS PLAN)
- Text descriptions of every scene (above) ✓
- Timing estimates per scene
- Scale/time indicator values at each transition
- Narration text drafted

### Phase 1: Skeleton animations (5 rough HTML files)
- Each file: basic SVG with geometric shapes (circles for planets, lines for field lines, rectangles for labels)
- Correct timing and transitions
- Scale/time/magnification indicators working
- Narration text appearing at correct times
- Navigation links between segments
- NO polish: no gradients, no smooth curves, no beauty. Boxes and lines.
- **Goal: the hard problems (timing, scale transitions, narrative flow) are solved**

### Phase 2: Physics pass
- Accurate magnetosphere shapes (bow shock curves, tail geometry, torus cross-section)
- Correct relative sizes and distances
- Real data references (Galileo crossing dates, Voyager positions, Cassini flyby dates)
- Accurate spacecraft shapes (Galileo's asymmetric antenna, Cassini's shape, Voyager's boom)
- Field line topology per planet (dipolar, stretched, compressed)

### Phase 3: Visual polish
- Gradient fills for plasma regions
- Smooth field line curves (bezier paths)
- Planet surface details (Jupiter bands, Saturn rings, Earth continents)
- Geyser/volcano particle effects
- Color-coded field strength
- Cinematic transitions between scenes
- Typography and layout refinement

### Phase 4: Narration polish
- Final Carl text editing — read aloud for cadence
- Timing adjustments to match visual beats
- Add/remove silence beats
- Philosophical coherence check (does the arc work?)

### Phase 5: Hub page + book integration
- tour-magnetospheres.html overview page
- Link from "The Wrong Substrate" section of the book (external link, clearly marked)
- README update for tutorials index

## Generator Execution Notes

- Each segment is ONE Generator task (one deliverable per agent)
- Phase 1: 5 Generator prompts, one per segment, each ≤8K tokens
- Phases 2-4 iterate on existing files
- The scale/time/magnification indicator is a SHARED component — implement once in Segment 1, copy pattern to all others
- SVG animations use CSS @keyframes (proven pattern from existing tutorials)
- Each file targets ≤200KB (current tutorials range 50-150KB)
- Total estimated: 5-8 Generator sessions for Phase 1, 3-5 for Phase 2, 2-3 for Phase 3

## Verification

1. Each segment loads and runs in browser
2. Scale/time indicators update correctly at every transition
3. Narration text is readable and correctly timed
4. Navigation links work between all segments
5. Physics spot-check: magnetosphere sizes, travel times, spacecraft dates
6. Total file size for all segments
7. Book link works from "The Wrong Substrate"

## Risk Assessment

**High risk:** Scope creep. Five segments × four phases = 20 units of work. Storyboard-first approach mitigates: if Phase 1 reveals that 5 segments is too many, we can cut to 3 (Earth, Jupiter, Heliosphere) without losing the narrative arc.

**Medium risk:** SVG performance with complex animations. Mitigated by keeping particle counts low and using CSS transforms (GPU-accelerated) over SVG animate elements.

**Low risk:** Scientific accuracy. Bruce has the domain knowledge. Galileo/Cassini/Voyager data is well-documented.

**Schedule:** This is not on the critical path for book release. It's a parallel workstream that enhances the book but doesn't block it.
