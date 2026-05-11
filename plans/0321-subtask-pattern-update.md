# Subtask: Revolution Pattern Update — Paradigm Shake

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: paradigm shake replaces golden flash, slower pacing`
**Read first:** The existing HTML file. Modify `buildRevolutionTimeline(cfg)` function.

## What Changes

The `buildRevolutionTimeline(cfg)` factory function needs these changes to its internal
animation pattern. The config objects for each revolution stay the same — only the
flow/behavior changes.

### Change 1: Kuhn Loop Always Visible

The loop circle + 5 phase labels must persist as a permanent background fixture at
opacity 0.25 throughout ALL segments. Never clear it. Never redraw it. Show it at
the start of EVERY segment (including if the user clicks a segment dot directly).

### Change 2: Anomaly Parking — Wider Scatter

Currently anomalies park in a tight vertical stack near the Anomaly position.
Change to a wider SCATTER within ~100px radius of the Anomaly position.
Use deterministic pseudo-random offsets based on item index:

```javascript
const scatterX = Math.sin(index * 2.7) * 60;
const scatterY = Math.cos(index * 1.9) * 40;
```

Slight rotation on each parked item (±5°) using SVG transform:
```javascript
el.setAttribute("transform", `rotate(${(index % 2 ? 3 : -3)}, ${x}, ${y})`);
```

The result should look like papers tossed on a desk — messy, overlapping, uncomfortable.

### Change 3: Crisis Items Park at Crisis Position

Currently crisis quotes park near the loop but don't specifically target the Crisis
phase position. Change: each crisis quote (hostile dismissal) shrinks and parks near
the CRISIS position on the loop (phasePos(2)). Same scatter pattern. This compounds
the visual mess — anomalies near Anomaly AND crisis items near Crisis.

Give each crisis quote TWO BEATS of display time (3-4 seconds each, not 1.5s).
The reader needs time to absorb the hostility.

### Change 4: Crisis Moment Gets Extended Time

Each revolution has a crisis-causing revelation:
- Heliocentrism: "Galileo sees Jupiter's moons — four of them, orbiting Jupiter, not Earth."
- Oxygen: "Lavoisier seals a flask. Burns metal. Weighs everything. Mass conserved."
- Evolution: "On the Origin of Species. Descent with modification."
- Germ Theory: "Pasteur's swan-neck flask. Broth stays clear for years."

This moment gets 4-5 seconds center stage (it's the dramatic climax). Then it
shrinks and parks at the Crisis position too. NOW the loop is maximally cluttered.

### Change 5: Paradigm Shake (REPLACES Golden Flash)

**REMOVE the golden flash entirely.** Replace with:

After the crisis moment parks, the OLD PARADIGM TEXT (title bar line 2, the italic
subtitle) begins to SHAKE. Implementation:

```javascript
// Shake for 2.5 seconds
const shakeProgress = (elapsed - shakeStart) / 2.5;
const amp = 3 + shakeProgress * 5; // amplitude increases
const freq = 15; // Hz
const baseX = 600;
const baseY = 45;
titleLine2.setAttribute("x", baseX + amp * Math.sin(shakeProgress * freq * Math.PI * 2));
titleLine2.setAttribute("y", baseY + amp * Math.cos(shakeProgress * freq * Math.PI * 2 * 0.7));
titleLine2.setAttribute("opacity", String(0.67 - shakeProgress * 0.3)); // fading as it shakes
```

The shaking intensifies (amplitude grows), the text fades slightly. It looks like the
paradigm is FALLING APART under the weight of anomalies. This IS the revolution —
not a flash, but a crumbling.

### Change 6: Resolution Sequence

After the shake (2.5s):
1. Old paradigm text fades out completely (0.5s)
2. SIMULTANEOUSLY, all accumulated junk (anomalies near Anomaly, crisis items near
   Crisis, the crisis moment) fades out together (1s)
3. Clean moment (1s) — just the loop, empty and clean
4. New paradigm text appears in title bar (gold, line 3) — fade in (0.5s)
5. "New Paradigm" content appears center stage (green) — the technology/outcome
6. Parks at New Paradigm position on loop

The relief comes from the FADING, not from a flash. The mess dissolves. The clean
loop remains. The new paradigm is stated calmly.

### Change 7: Overall Pacing — Slower

Increase per-revolution duration to ~45-50 seconds:
- Normal Science: 5s
- Anomaly accumulation: 20-25s (4-5 pairs × 4-5s each)
- Crisis quotes: 8-10s (2 quotes × 4s each)
- Crisis moment: 5s
- Paradigm shake: 2.5s
- Resolution (fade + clean + new paradigm): 4s
- New Paradigm display: 3s

### Change 8: Remove Golden Flash Element Usage

Remove or zero-out all references to `goldenFlash.setAttribute("opacity", ...)`.
The golden flash rect can stay in the SVG DOM (harmless) but should never be made visible.

## Technical Notes

- The `cfg` objects for each revolution don't change — just the factory's behavior
- The factory function is `buildRevolutionTimeline(cfg)` — find it and modify in place
- Test that clicking scrubber dots still works after changes
- The paradigm shake needs smooth animation — use requestAnimationFrame timing, not setTimeout

## Report

State: what changed, per-segment duration (should be ~45-50s each), total duration.
