# Subtask: Fix Revolution Pattern — Everything Parks, Paradigm Death Sequence

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: everything parks at loop position, paradigm death sequence`
**Read first:** The existing HTML file.

## Two Jobs

### Job 1: Convert Segment 1 (Heliocentrism) to Factory

Delete the hand-built `buildSegment1Timeline()` function. Replace it with a factory
call using the same `buildRevolutionTimeline(cfg)` pattern as segments 2-4.

Heliocentrism config:

```javascript
{
  title: "The Copernican Revolution (1543–1687)",
  oldParadigm: "The earth is at the center. The sun, moon, and stars revolve around it.",
  newParadigm: "The earth moves around the sun. The solar system is vast.",
  normalText: "The sun rises east, crosses the sky, sets west. Earth feels still.",
  normalSub: "Ptolemy's geocentric model. (~150 AD)",
  normalYear: "~1400",
  anomalies: [
    { text: "Mars stops. Reverses direction. Then moves forward again.", dismiss: "Add an epicycle.", year: "1543" },
    { text: "Jupiter wobbles off its predicted path.", dismiss: "Another epicycle.", year: "1550" },
    { text: "Planets get brighter and dimmer throughout the year.", dismiss: "The sphere is slightly off-center.", year: "1580" },
    { text: "Epicycles needed: 40... 52... 79...", dismiss: "The math works. Don't question the model.", year: "1600" },
    { text: "Copernicus: what if the Earth moves around the Sun?", dismiss: "Interesting mathematics. But obviously the Earth doesn't move.", year: "1543" },
  ],
  crisisQuotes: [
    "The Earth MOVES? Absurd. I can feel that it doesn't.",
    "De Revolutionibus — ignored for 70 years.",
  ],
  crisisYear: "1543–1610",
  crisisMoment: "Galileo points his telescope at Jupiter. Four moons — orbiting Jupiter, not Earth.",
  crisisMomentYear: "1610",
  crisisMomentName: "Galileo, 1610",
  newParadigmTech: "Navigation. Celestial mechanics. Space travel.",
  newParadigmYear: "1687",
  transitionYears: "~150 years",
}
```

### Job 2: Update Factory — The Full Parking + Paradigm Death Pattern

Every item that appears center stage must eventually SHRINK and PARK at its Kuhnian
phase position on the loop. Nothing vanishes. The loop accumulates everything.

**The 5 parking zones (one per Kuhnian phase):**

1. **Normal Science position** — Normal text parks here
2. **Anomaly position** — All anomaly-dismissal pairs park here (messy scatter)
3. **Crisis position** — All crisis quotes park here (messy scatter)
4. **Revolution position** — The crisis moment parks here after its big reveal
5. **New Paradigm position** — New paradigm text parks here after center stage

**Messy parking rules:**
- Each parked item gets a pseudo-random lean angle: `rotate(${sin(i*3.1)*8}, x, y)` degrees (±8°)
- Scatter radius: 80px around the phase position
- Offset: `x + sin(i*2.7)*60`, `y + cos(i*1.9)*50`
- Items can overlap. That's GOOD. The mess IS the point.
- Font size when parked: 9-11px
- Opacity when parked: 0.6-0.8

**The Paradigm Death Sequence (replaces current resolution):**

After the crisis moment parks at Revolution position, the loop is maximally cluttered.
Then:

1. **Old paradigm moves to center** (1.5s): The title bar subtitle text (old paradigm)
   GROWS and MOVES from its title bar position to CENTER STAGE. Gets big (40px).
   It's now dominant, filling the center. This is its last stand.

2. **Old paradigm shakes** (2.5s): The big centered old paradigm text vibrates with
   growing amplitude (3→10px). Frequency ~15Hz. It's falling apart visually.
   Meanwhile it's also slowly fading (opacity 1.0 → 0.3).

3. **Old paradigm fades out** (0.5s): Final fade to 0.

4. **Clean moment** (1s): All accumulated junk on the loop fades out together (1s).
   Just the clean Kuhn loop remains (0.25 opacity labels).

5. **New Paradigm enters center** (2s): New paradigm statement appears CENTER STAGE
   (48px, green, bold, pop-scale entry). E.g., "The earth moves around the sun."
   Reader absorbs.

6. **Title bar updates** (simultaneous with step 5): Old paradigm text in title bar
   gets strikethrough. New paradigm appears in gold below it. The old text is small
   and weak above; the new text is prominent.

7. **New Paradigm parks** (0.5s): Center text shrinks + flies to New Paradigm position
   on the loop.

8. **Technology/outcome** (2s): Brief green text center: "Navigation. Celestial
   mechanics. Space travel." Then parks at New Paradigm position too.

9. **Transition note** (1s): Small text fades in: "~150 years" (or whatever
   `cfg.transitionYears` says). Shows how long the revolution took.

10. **Pause** (1.5s): Clean state. Loop has faint labels only. Ready for next revolution.

**Duration per revolution: ~50-55 seconds.** That's fine. Slow is good.

## Technical Notes

- Remove the entire hand-built `buildSegment1Timeline()` function
- Add Heliocentrism config to the `segmentBuilders` array or equivalent dispatcher
- The factory changes apply to ALL factory-built revolutions (segments 1-4)
- Verify scrubber dot 1 still works after conversion
- The old paradigm "moving to center" animation: interpolate x from 600 (title position)
  to 600 (center, same x), y from 45 to CY (310), and font-size from 15 to 40

## Report

State: segment 1 duration (should be ~50s), total duration all segments, confirmation
that anomalies/crisis/revolution/paradigm all park visibly on loop.
