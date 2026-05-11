# Subtask: Two Bugs — Blue Text Overlap + Abstract Observation Position

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fix blue text overlap, fix abstract observation parking at Revolution`
**Read first:** The existing HTML file.

## Bug 1: Blue Normal Science Text Overlap

In `buildRevolutionTimeline(cfg)`, the Normal Science main text and sub text overlap.

Main text is created at `CY - 15` (y=295) with font-size 36px and word wrapping.
A two-line wrapped string extends ~47px below the starting y. Sub text is created
at `CY + 25` (y=335) — which falls INSIDE the wrapped main text.

**Fix:** Change the sub text y position from `CY + 25` to `CY + 55`.

Find this line (approximately line 781):
```javascript
nSub = createText(cfg.normal.sub, CX, CY + 25, 17, "#4a90d9");
```
Change to:
```javascript
nSub = createText(cfg.normal.sub, CX, CY + 55, 17, "#4a90d9");
```

Also update the park animation for nSub (if it references CY + 25) to use CY + 55.

## Bug 2: Abstract Cycle Observation Parks at Wrong Position

In `buildSegment0Timeline()` (segment 0), the gold crisis moment observation
"An observation the old theory cannot explain" parks at **phasePos(2)** (Crisis).
It should park at **phasePos(3)** (Revolution).

Find these two occurrences (approximately lines 494 and 505):
```javascript
const pos = phasePos(2);
```
in the crisis moment parking section (around t=25.5 and t=25.9, the keyframes
that move and park "An observation the old theory cannot explain").

Change BOTH to:
```javascript
const pos = phasePos(3);
```

These are in the abstract cycle ONLY (segment 0). The factory function already
uses phasePos(3) correctly — do not change the factory.

**How to identify the right lines:** They are in the section commented
"Phase 4: Crisis Moment" within buildSegment0Timeline(). The parking keyframes
are at t=25.5 (the fly animation) and t=25.9 (the final park). Both use
phasePos(2) and scatterOffset(10). Change phasePos(2) to phasePos(3) in both.

## Do NOT

- Change any factory code (buildRevolutionTimeline is correct)
- Change any other phasePos references
- Change timing or sequence

## Report

Confirm: sub text no longer overlaps main text, abstract observation parks at
Revolution position (lower left of loop, not lower right).
