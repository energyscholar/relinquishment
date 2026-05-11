# Subtask: Engine Tweaks Part 1 — Parameters and Small Fixes

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: engine part 1 — loop persists, slower parks, blue bigger, old paradigm label`
**Read first:** The existing HTML file. Focus on `clearStage()` and `buildRevolutionTimeline(cfg)`.

These are small parameter changes and one-line fixes. No behavioral rewrite.

## Change 1: Loop Persists Across Segments

`clearStage()` (line ~217) wipes loopLabels and cyclePath. Fix:

In `showLoopFrame()` (both the one in segment 0 ~line 248 AND the one in the
factory ~line 637), after creating each phase label element, set:
`el.dataset.persist = "1";`

Also set: `cyclePath.dataset.persist = "1";`

Add a guard at the TOP of each `showLoopFrame()`:
```javascript
if (cyclePath.dataset.persist) return;
```

In `clearStage()`, change the loopLabels wipe from:
```javascript
while (loopLabels.firstChild) loopLabels.removeChild(loopLabels.firstChild);
```
to:
```javascript
[...loopLabels.children].forEach(ch => { if (!ch.dataset.persist) loopLabels.removeChild(ch); });
```

And wrap the cyclePath reset lines in: `if (!cyclePath.dataset.persist) { ... }`

## Change 2: Slower Park Movements

In `buildRevolutionTimeline()`, find every park keyframe that has `dur: 0.5` where
the `fn(p)` interpolates position toward a `phasePos()` target. Change `dur: 0.5`
to `dur: 1.5`. There are approximately 4 occurrences:
- Normal Science park (~line 708): `dur: 0.5` → `dur: 1.5`
- Anomaly park (~line 768): `dur: 0.5` → `dur: 1.5`
- Crisis park (~line 862): `dur: 0.5` → `dur: 1.5`
- Crisis moment park (~line 905): `dur: 0.5` → `dur: 1.5`

After changing each `dur`, update the timing constants at the top of the factory
function. Currently the timeline is computed with variables like:
```javascript
const normalEnd = 5.5;
const anomalyEnd = normalEnd + N * 5;
```

Change `N * 5` to `N * 6` (each anomaly pair gets +1s for slower park).
Change crisis timing to account for +1s per park.
Change momentEnd offset to account for +1s slower park.

The timing variables cascade — adjust each one that follows a park animation.

## Change 3: Blue Normal Science Text Bigger

Line ~687: change `30` to `36` in `createText(cfg.normal.main, CX, CY - 15, 30, ...)`.
Line ~691: change the pop-scale reference: `Math.round(30 * ...)` → `Math.round(36 * ...)`.
Line ~715: change the park shrink: `Math.round(30 - 20 * t)` → `Math.round(36 - 26 * t)`.

## Change 4: Label "OLD PARADIGM" in Title Bar

In the setup keyframe (t=0, dur=0.5, line ~669), after `titleLine2.textContent = cfg.title2`,
add:
```javascript
const oldLabel = createText("OLD PARADIGM", 600, 28, 10, "#e8e0d0", { opacity: 0.4 });
oldLabel.setAttribute("letter-spacing", "2");
titleBar.appendChild(oldLabel);
```

## Do NOT

- Change the death sequence order (that's Part 2)
- Change crisis quote timing (that's Part 2)
- Add text wrapping (that's Part 3)
- Touch segment 0 logic beyond the showLoopFrame guard
- Change config objects

## Report

State: confirm loop visible after switching segments via scrubber dots, confirm
slower park animations, confirm blue text larger, confirm "OLD PARADIGM" label visible.
