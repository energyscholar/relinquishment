# Subtask: Fix Crisis Quote Shrink Path

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fix crisis quote shrink path to Crisis position`
**Read first:** The CURRENT state of the file.

## Problem

Crisis quotes fly the wrong direction while shrinking to their parking position.
They end up at the right place, but take the wrong path. The cause is line ~970:

```javascript
cGroup.setAttribute("transform", `translate(${(tx - CX) * t}, ${(ty - CY) * t}) scale(${scale})`);
```

Using `translate` + `scale` on a `<g>` group creates compound transform issues —
the scale origin is (0,0) of the SVG, not the center of the group. The scaling
warps the translation path.

## Fix

Replace the group transform approach with direct element positioning, matching
how anomaly parking works (lines ~892-903). Instead of transforming the `<g>`
group, fade the group out and simultaneously move a simplified text element.

Replace the shrink keyframe (t: cStart + 2.5, dur: 1.5) with:

```javascript
kf.push({ t: cStart + 2.5, dur: 1.5, fn(p) {
  if (!cGroup) return;
  const t = easeInOutCubic(p);
  const pos = phasePos(2);
  const off = scatterOffset(N + ci + 2);
  const tx = pos.x + off.x, ty = pos.y + off.y;
  // Fade the speech bubble group out
  cGroup.setAttribute("opacity", String(1 - easeOutCubic(p)));
  // Move the text element inside the group toward target
  const textEl = cGroup.querySelector("text");
  if (textEl) {
    const startX = CX, startY = CY - 20;
    textEl.setAttribute("x", String(startX + (tx - startX) * t));
    textEl.setAttribute("y", String(startY + (ty - startY) * t));
    const fs = Math.round(18 - 9 * t);
    textEl.setAttribute("font-size", String(fs));
    textEl.querySelectorAll('tspan').forEach((ts, i) => {
      ts.setAttribute('x', String(startX + (tx - startX) * t));
      if (i > 0) ts.setAttribute('dy', String(Math.round(fs * 1.3)));
    });
  }
  // Shrink the bubble rect too
  const rect = cGroup.querySelector("rect");
  if (rect) {
    rect.setAttribute("opacity", String(1 - t));
  }
}});
```

This moves the text along a straight line from center to phasePos(2) while
fading. No compound transform. Same visual result as anomaly parking.

Remove any `cGroup.setAttribute("transform", ...)` — do not use group transforms.

## Do NOT

- Change where the crisis quote parks (phasePos(2) is correct)
- Change timing (1.5s duration is correct)
- Change the speech bubble creation or display
- Touch anomaly or revolution parking code

## Report

Confirm crisis quotes shrink along a straight path from center toward
phasePos(2) (Crisis position, lower right of loop).
