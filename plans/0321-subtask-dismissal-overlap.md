# Subtask: Fix Anomaly Dismissal Text Overlap

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fix dismissal text overlap with anomaly text`
**Read first:** The CURRENT state of the file.

## Problem

In the anomaly-dismissal pairs, the dismissal text (red, italic, 18px) appears at
`CY + 25` (y=335). The anomaly text above it starts at `CY - 15` (y=295) at 28px
with word wrapping. A two-line wrapped anomaly extends to ~y=331. The dismissal at
y=335 overlaps.

## Fix

Change the dismissal text y-position from `CY + 25` to `CY + 55`.

Find this line in the anomaly-dismissal loop (approximately line 879):
```javascript
dText = createText(pair.dismissal, CX, CY + 25, 18, "#c45c5c");
```
Change to:
```javascript
dText = createText(pair.dismissal, CX, CY + 55, 18, "#c45c5c");
```

Also update the park animation for dText. Find the line that interpolates dText's
y-position during parking (approximately line 905-906):
```javascript
dText.setAttribute("y", (CY + 25) + (ty + 12 - (CY + 25)) * t);
```
Change `CY + 25` to `CY + 55` in both places on that line:
```javascript
dText.setAttribute("y", (CY + 55) + (ty + 12 - (CY + 55)) * t);
```

## Do NOT

- Change anomaly text position (CY - 15 is fine)
- Change dismissal font size or color
- Change anything else

## Report

Confirm dismissal text sits clearly below wrapped anomaly text.
