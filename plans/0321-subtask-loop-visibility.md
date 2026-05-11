# Subtask: Fix Loop Visibility During Abstract Cycle

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fix loop visibility during abstract cycle`
**Read first:** The CURRENT state of the file.

## Problem

The Kuhn loop (circle + 5 phase labels) disappears during the first Abstract
cycle (segment 0), but is visible during all other segments.

## Likely Causes and Fixes

### Fix A: showLoopFrame guard too aggressive

The factory's `showLoopFrame()` has `if (cyclePath.dataset.persist) return;` which
skips entirely if the loop was already created. This means it never resets opacity.

Change BOTH `showLoopFrame()` functions (segment 0 ~line 327 and factory ~line 697)
from:
```javascript
if (cyclePath.dataset.persist) return;
```
to:
```javascript
if (cyclePath.dataset.persist) {
  cyclePath.setAttribute("opacity", "0.25");
  [...loopLabels.children].forEach(el => {
    if (el.dataset.persist) el.setAttribute("opacity", "0.25");
  });
  return;
}
```

This ensures the loop is always reset to 0.25 opacity at the start of each segment,
even if it already exists.

### Fix B: Segment 0 brightens loop at end but doesn't dim it back

At ~t=32.5 in segment 0, the loop labels and cyclePath get brightened from 0.25
to 1.0 (the "You Are Here" reveal). When segment 1 then starts, the loop is at
full opacity 1.0 instead of 0.25. Fix A above handles this — the factory's
showLoopFrame will reset to 0.25.

### Fix C: Verify loop is created before any fade runs

In segment 0, the loop is created at t=0 via showLoopFrame(). The accumulated
elements fade at t=29-30. At t=30, elements are removed from loopLabels. Verify
that the removal at ~line 576 only removes elements from `accumulatedEls`, not
the persistent loop labels. The current code looks correct (iterates accumulatedEls
only), but verify.

## Do NOT

- Change the persist mechanism itself
- Change animation timing or sequence
- Touch factory revolution configs

## Report

Confirm: loop circle + 5 phase labels visible throughout segment 0 playback,
loop resets to 0.25 opacity when any segment starts.
