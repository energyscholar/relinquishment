# Subtask: Engine Tweaks Part 3 — Text Wrapping for Overflow

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: engine part 3 — text wrapping prevents overflow`
**Read first:** The existing HTML file. Parts 1 and 2 will have landed already.

## Problem

Long text strings at large font sizes (28-48px) overflow left/right of the 1200px
SVG viewport when centered at x=600. Example: a 50-character string at 36px is
roughly 900px wide — fine. But at 48px it's ~1200px — clipping on both sides.

## Solution

Add one utility function near the other helpers (after `createText`, ~line 130):

```javascript
function createWrappedText(text, x, y, size, color, maxChars) {
  maxChars = maxChars || 40;
  const words = text.split(' ');
  const lines = [];
  let current = '';
  for (const w of words) {
    if (current && (current + ' ' + w).length > maxChars) {
      lines.push(current);
      current = w;
    } else {
      current = current ? current + ' ' + w : w;
    }
  }
  if (current) lines.push(current);

  const el = document.createElementNS(SVG_NS, "text");
  el.setAttribute("x", x);
  el.setAttribute("y", y);
  el.setAttribute("text-anchor", "middle");
  el.setAttribute("fill", color);
  el.setAttribute("font-size", size);
  el.setAttribute("font-family", "Georgia, serif");
  el.setAttribute("font-weight", "bold");

  for (let i = 0; i < lines.length; i++) {
    const tspan = document.createElementNS(SVG_NS, "tspan");
    tspan.setAttribute("x", x);
    tspan.setAttribute("dy", i === 0 ? "0" : String(size * 1.3));
    tspan.textContent = lines[i];
    el.appendChild(tspan);
  }
  return el;
}
```

## Where to Use It

Replace `createText(...)` with `createWrappedText(...)` in these specific places
within `buildRevolutionTimeline()`:

1. **Normal Science main** — currently `createText(cfg.normal.main, CX, CY-15, 36, "#4a90d9")`.
   Change to `createWrappedText(cfg.normal.main, CX, CY-15, 36, "#4a90d9", 38)`.

2. **Anomaly text** — currently `createText(pair.anomaly, CX, CY-15, 28, "#d4a574")`.
   Change to `createWrappedText(pair.anomaly, CX, CY-15, 28, "#d4a574", 42)`.

3. **Revolution main** — currently `createText(cfg.revolution.main, CX, CY-15, 28, "#d4a017", ...)`.
   Change to `createWrappedText(cfg.revolution.main, CX, CY-15, 28, "#d4a017", 42)`.
   (Keep the glow filter — set it on the returned element after creation.)

4. **New Paradigm center** — currently `createText(cfg.title3, CX, CY, 42, "#5c9c5c")`.
   Change to `createWrappedText(cfg.title3, CX, CY, 42, "#5c9c5c", 35)`.

5. **Crisis quotes** — currently `createText(cfg.crisis[i], CX, yPos, 18, "#c45c5c")`.
   Change to `createWrappedText(cfg.crisis[ci], CX, yPos, 18, "#c45c5c", 48)`.

Do NOT wrap: parked text (already truncated), sub-lines (short), title bar text
(positioned at top with plenty of room), tech outcome text (usually short).

## Animation Compatibility

The wrapped text element works the same as `createText` for positioning — you can
still set `x`, `y`, `font-size`, `opacity` attributes on it. The tspans inherit
font-size from the parent. When the element animates (moves, scales), update the
parent `<text>` element just like before. The tspans follow.

One subtlety: when you change `font-size` on the parent during animation, also
update each tspan's `dy` to `newSize * 1.3` so line spacing stays proportional:
```javascript
el.querySelectorAll('tspan').forEach((ts, i) => {
  if (i > 0) ts.setAttribute('dy', String(newSize * 1.3));
});
```

Add this inside any animation keyframe that changes font-size on a wrapped element.

## Do NOT

- Change any animation sequence or timing (Parts 1+2 handled that)
- Touch the createText function itself (keep it for short text)
- Wrap text that doesn't need it (parked text, sub-lines, labels)

## Report

State: confirm no text clips outside viewport at any point during playback.
Check the longest strings in each revolution config.
