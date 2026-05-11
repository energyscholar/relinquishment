# Subtask: Engine Bug Fixes — Parking Positions + Text Overflow

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: fix parking positions, add text wrapping, reduce center text size`
**Read first:** The CURRENT state of the file (Parts 1+2 have already landed).

Four bugs to fix. All are in `buildRevolutionTimeline(cfg)` or global helpers.

## Bug 1: Revolution Observation Parks at Wrong Position

The crisis moment (the observation that causes the revolution, e.g. "Galileo points
his telescope at Jupiter...") should park at **phasePos(3)** (Revolution position,
~225° on the loop). It's currently parking beyond Crisis instead.

**Fix:** Find the keyframe that parks the crisis moment. Verify it uses `phasePos(3)`,
NOT `phasePos(2)`. The variable should be something like:
```javascript
const pos = phasePos(3);  // Revolution position, NOT Crisis
```
If the Part 2 reorder accidentally changed this to phasePos(2), change it back to 3.

## Bug 2: DNA Revolution Crisis Items Park at Wrong Angle (~265° instead of ~165°)

In segment 8 (DNA, N=4 anomalies), crisis quotes fly to ~265° (open space on left)
instead of ~165° (Crisis position). This is likely a scatter offset issue — for
high indices, `scatterOffset()` produces offsets large enough to push items far from
the target phasePos.

**Fix:** Check the `scatterOffset()` function. The scatter radius should be CLAMPED
so items stay near their target phase. Current code:
```javascript
function scatterOffset(index) {
  return { x: Math.sin(index * 2.7) * 60, y: Math.cos(index * 1.9) * 50 };
}
```

The problem: at high index values (e.g. index=6,7 for DNA crisis items), the
offset can be up to 60px in x and 50px in y — which on the loop's scale can push
items to a completely different phase position. Reduce the scatter radius:
```javascript
function scatterOffset(index) {
  return { x: Math.sin(index * 2.7) * 40, y: Math.cos(index * 1.9) * 30 };
}
```

Also verify that crisis items in ALL segments use `phasePos(2)` (Crisis position).

## Bug 3: Text Wrapping Utility (prevents overflow)

Long center-stage text scrolls off screen left and right. Add a helper function
NEAR the existing `createText` function (~line 130):

```javascript
function createWrappedText(text, x, y, size, color, maxChars) {
  maxChars = maxChars || 38;
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
    tspan.setAttribute("x", String(x));
    tspan.setAttribute("dy", i === 0 ? "0" : String(Math.round(size * 1.3)));
    tspan.textContent = lines[i];
    el.appendChild(tspan);
  }
  return el;
}
```

Replace `createText(...)` with `createWrappedText(...)` at these call sites
inside `buildRevolutionTimeline()`:

1. Normal Science main text — the blue center text
2. Anomaly text — the amber center text
3. Crisis quote text — the red text inside speech bubbles
4. Revolution main text — the gold center text
5. New Paradigm center text (cfg.title3) — the green text

Search for `createText(cfg.` and `createText(pair.anomaly` and similar patterns.
Do NOT wrap: parked/truncated text, sub-lines, title bar text, small labels.

When animating font-size changes on wrapped text, also update tspan `dy`:
```javascript
el.querySelectorAll('tspan').forEach((ts, i) => {
  if (i > 0) ts.setAttribute('dy', String(Math.round(newSize * 1.3)));
});
```

## Bug 4: Center-Stage Paradigm Text Too Big

When old/new paradigm text appears at center stage, it's too large and overflows.

- Old paradigm moving to center: currently grows to 40px. Change to **32px**.
- New Paradigm at center: currently 42px. Change to **34px**.
- Use `createWrappedText` for BOTH (with maxChars=38).

Find the keyframes where `cfg.title2` (old paradigm) and `cfg.title3` (new paradigm)
are displayed at center stage and reduce their target font sizes.

## Do NOT

- Change the death sequence order (Part 2 got this right)
- Change timing/pacing
- Touch segment 0 (abstract cycle)
- Change config objects

## Report

State: confirm revolution observation parks at phasePos(3), confirm DNA crisis
items park near phasePos(2), confirm no text overflows viewport, list any strings
that still clip.
