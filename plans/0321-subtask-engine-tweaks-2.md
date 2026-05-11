# Subtask: Engine Tweaks Part 2 — Crisis Sequential + Death Sequence Reorder

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: engine part 2 — crisis one-at-a-time, death sequence reordered`
**Read first:** The existing HTML file. Focus on the crisis section and death sequence
in `buildRevolutionTimeline(cfg)`. Part 1 will have already landed (slower parks,
loop persistence, etc.) so read the CURRENT state of the file.

## Change 1: Crisis Quotes One-at-a-Time

Currently the factory has two hardcoded crisis quote blocks (crisisQ1Start,
crisisQ2Start) that appear at CY-20 and CY+30 simultaneously visible.

Replace with a loop over `cfg.crisis` array. Each quote gets its own cycle:
1. Clear center (instant)
2. Create speech bubble + quote text, fade in (0.5s)
3. Hold for reader to absorb (3s)
4. Shrink + fly to phasePos(2) with scatter offset (1.5s — matching Part 1's slower parks)

Compute timing: `const crisisPerQuote = 5;` (0.5 + 3 + 1.5)
```javascript
for (let ci = 0; ci < cfg.crisis.length; ci++) {
  const cStart = pauseEnd + ci * crisisPerQuote;
  // ... keyframes for this single quote ...
}
const crisisEnd = pauseEnd + cfg.crisis.length * crisisPerQuote;
```

Each quote parks at phasePos(2) with `scatterOffset(N + ci + 2)` and
`leanAngle(N + ci + 2)` — same scatter pattern as anomalies but at Crisis position.

Use the existing speech bubble pattern (rounded rect behind text) that's already
in the code — just create one bubble per quote instead of two at once.

## Change 2: Death Sequence Reorder

After the crisis moment parks at Revolution position (phasePos(3)), the current
code does: old→center→shake→fade→junk fade→clean→NP center→NP park→tech.

Change to this order (reuse existing animation patterns, just rearrange):

**Step 1: New Paradigm appears center (2.5s)**
Same as current "Step 5+6" block (~line 986-1006) but moved EARLIER.
`cfg.title3` appears center stage, green, 42px, bold, easeOutBack pop-scale.
Hold 2s. DO NOT update title bar yet.

**Step 2: New Paradigm parks at phasePos(4) (1.5s)**
Same as current "Step 7" block (~line 1011-1028) but moved EARLIER.
Shrinks + flies to phasePos(4). Parks visibly (opacity 0.7, 11px).
Add to `accumulatedEls` so it's tracked.

**Step 3: Old Paradigm moves to center (2s)**
Same as current "Step 1" (~line 930-944). titleLine2 fades, duplicate appears
at title position, interpolates down to CY, grows to 40px. `easeInOutCubic`.
NO SHAKE — remove the shake keyframe entirely.

**Step 4: Old + all mess fades (1.5s)**
The big centered old paradigm fades to 0. SIMULTANEOUSLY, all `accumulatedEls`
(which now includes the parked NP) fade to 0. Then remove from DOM.
Same as current "Step 3" + "Step 4" combined into one 1.5s fade.

**Step 5: Clean moment (1s)**
Just the persistent loop. Empty, calm.

**Step 6: New Paradigm rises from loop to center (1.5s)**
NEW ANIMATION: create text `cfg.title3` at phasePos(4) position (11px, green).
Interpolate: position → (CX, CY), font-size 11 → 42px. `easeInOutCubic`.
Reader sees it physically travel from its loop position to center stage.

**Step 7: New Paradigm moves to title bar (1.2s)**
NEW ANIMATION: from center (CX, CY, 42px) interpolate to (600, 60, 14px).
`easeInOutCubic`. As it arrives, update title bar:
- `titleLine2` reappears at opacity 0.3 with strikethrough
- `titleLine3.textContent = cfg.title3`, show gold, opacity 1
- `titleStrike` opacity 1

**Step 8: Tech + transition (existing, unchanged)**
Tech text appears center, parks at phasePos(4). Transition note. Final pause.

## Timing

Recompute the timing constants from `momentParkEnd` onward:
```javascript
const npCenterStart = momentParkEnd;        // NP appears center
const npParkStart = npCenterStart + 2.5;    // NP parks
const npParkEnd = npParkStart + 1.5;        // NP parked
const deathMoveStart = npParkEnd;           // Old moves center
const deathMoveEnd = deathMoveStart + 2;    // Old at center
const fadeStart = deathMoveEnd;             // Everything fades
const fadeEnd = fadeStart + 1.5;            // Fade complete
const cleanEnd = fadeEnd + 1;              // Clean moment
const riseStart = cleanEnd;                // NP rises from loop
const riseEnd = riseStart + 1.5;           // NP at center
const toTitleStart = riseEnd;              // NP moves to title
const toTitleEnd = toTitleStart + 1.2;     // NP at title bar
const techStart = toTitleEnd;              // Tech outcome
```

## Do NOT

- Change anything from Part 1 (loop persistence, slower parks, blue text, label)
- Touch segment 0 (abstract cycle)
- Change config objects
- Add text wrapping (that's Part 3)

## Report

State: per-segment durations (will be longer due to sequential crisis + reorder),
confirm crisis quotes appear one-at-a-time with individual park animations,
confirm death sequence shows NP park → old dies → NP rises → NP to title bar.
