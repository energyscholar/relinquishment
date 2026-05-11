# Subtask: Revolution 2 — Oxygen (Segment 2)

**Output:** `build/images/segment2-oxygen.js` (NEW file, just the function)
**Commit:** `Plan 0321: segment 2 function (Oxygen)`

## What to Write

Write a single JavaScript function `buildSegment2Timeline()` that returns `{ keyframes, duration }`.
Follow this exact template from the existing codebase:

```javascript
function buildSegment2Timeline() {
  const TOTAL = 38; // adjust to actual total
  const accumulatedEls = [];
  const years = [/* year per phase */];

  function setYear(yr) {
    yearDisplay.textContent = yr;
    yearDisplay.setAttribute("opacity", "0.55");
  }

  function showLoopFrame() {
    cyclePath.setAttribute("d", fullCirclePath());
    cyclePath.setAttribute("stroke-dasharray", "6,4");
    cyclePath.removeAttribute("stroke-dashoffset");
    cyclePath.setAttribute("opacity", "0.25");
    for (let i = 0; i < 5; i++) {
      const p = phasePos(i);
      const el = createText(phases[i].name, p.x, p.y, 12, phases[i].color, { opacity: 0.25 });
      el.setAttribute("font-size", "12");
      loopLabels.appendChild(el);
    }
  }

  function addLoopContent(idx, shortText, color) {
    const p = phasePos(idx);
    const offset = accumulatedEls.length * 14; // stack vertically
    const el = createText(shortText, p.x, p.y + 18 + offset, 11, color);
    el.setAttribute("font-weight", "normal");
    el.setAttribute("letter-spacing", "0");
    loopLabels.appendChild(el);
    accumulatedEls.push(el);
  }

  const kf = [];
  // ... keyframes here ...
  return { keyframes: kf, duration: TOTAL };
}
```

Available helper functions (DO NOT redefine them, just call them):
- `createText(text, x, y, size, color, opts)` — creates SVG text element
- `phasePos(i)` — returns {x, y} for phase position on Kuhn loop (0=Normal, 1=Anomaly, 2=Crisis, 3=Revolution, 4=New Paradigm)
- `fullCirclePath()` — returns SVG path string for the loop circle
- `easeOutBack(t)`, `easeInOutCubic(t)`, `easeOutCubic(t)` — easing functions
- `CX=600, CY=310, CR=270` — circle center and radius

Global elements (reference by ID, already exist):
- `centerStage` — container for center text
- `loopLabels` — container for loop position labels
- `cyclePath` — the circle path element
- `goldenFlash` — golden flash overlay rect
- `titleBar`, `titleLine1`, `titleLine2`, `titleStrike`, `titleLine3` — title bar elements
- `yearDisplay` — year text in upper-right

## Revolution 2 Content: Oxygen

**Title bar:**
- Line 1: "The Chemical Revolution (1770–1789)"
- Line 2: "When things burn, they release phlogiston — an invisible fire element."
- Resolve line 3: "Combustion consumes oxygen. Mass is conserved."

**Years:** "~1700" | "1772" | "1774" | "1777" | "1783" | "1789"

**Beat structure:**

| Time | Phase | Content |
|------|-------|---------|
| 0-0.5s | Setup | Show loop frame + title bar fade in |
| 0.5-4s | Normal Science (blue) | Center: "Things burn. The flame rises. Something escapes into the air." Below (24px): "Georg Stahl's phlogiston theory. (~1703)" Year: ~1700 |
| 4-5s | Fly to loop | Normal text shrinks + flies to Normal Science position |
| 5-9s | Anomaly 1 | Center (amber): "Burn a piece of metal. Weigh the ash. It got HEAVIER." Year: 1772 |
| 9-10.5s | Dismissal 1 | Below (20px, muted): "Phlogiston has negative weight." |
| 10.5-11s | Park | Both shrink + fly to Anomaly position |
| 11-15s | Anomaly 2 | Center: "Seal a flask. Burn something inside. Total weight unchanged." |
| 15-16.5s | Dismissal 2 | "The phlogiston is still in the flask." |
| 16.5-17s | Park | Fly to Anomaly (offset from first) |
| 17-20s | Anomaly 3 | "Priestley isolates a gas that makes things burn MORE vigorously." Year: 1774 |
| 20-21.5s | Dismissal 3 | "He calls it 'dephlogisticated air.' Problem solved." |
| 21.5-22s | Park | Fly to Anomaly (more clutter) |
| 22-24s | Anomaly 4 | "Every anomaly gets a special exception. The theory bends." Year: 1777 |
| 24-25.5s | Dismissal 4 | "Different substances contain different amounts of phlogiston." |
| 25.5-26s | Park | Fly (maximum clutter now) |
| 26-27s | Pause | Reader sees mess |
| 27-30s | Crisis (red) | Bubble: "The theory explains everything — and therefore nothing." Parks at Crisis. |
| 30-31s | Flash | Golden flash opacity 0.3. Clutter clears. |
| 31-35s | Revolution (gold) | "Lavoisier seals a flask. Burns metal. Weighs everything." Below: "Mass conserved. A new element: oxygen." Name: "Lavoisier, 1783" Year: 1783 |
| 35-38s | New Paradigm (green) | "The periodic table. Conservation of mass. Modern chemistry." Title bar: strikethrough line 2, show line 3 gold. Year: 1789 |

## Style Notes

- Keyframes: array of `{ t, dur, fn(progress) }` — same format as segment 1
- Pop-scale on text entry: `easeOutBack(p)` for scale
- Fly-to-position: `easeInOutCubic` for arc
- Golden flash: max opacity **0.3** (toned down)
- Anomaly parking: offset each successive pair vertically (+14px) so they scatter, don't stack neatly
- Speech bubble for Crisis: create a rounded rect behind the text (rx=8, fill="#c45c5c22", stroke="#c45c5c")

## Output

Write ONLY the function to `build/images/segment2-oxygen.js`. No HTML wrapper. No other functions.
The file should contain exactly one function: `buildSegment2Timeline()`.
