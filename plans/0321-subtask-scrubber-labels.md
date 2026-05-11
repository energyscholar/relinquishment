# Subtask: Scrubber Labels + Active Indicator

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: scrubber labels name each revolution, active dot highlighted`
**Read first:** The CURRENT state of the file. Focus on `buildScrubber()` and the
`segmentLabels` array.

## Change 1: Meaningful Scrubber Labels

The `segmentLabels` array currently reads:
```javascript
const segmentLabels = ["Abstract", "1", "2", "3", "4", "5", "6", "7", "8"];
```

Change to short, recognizable names:
```javascript
const segmentLabels = ["Abstract", "Copernicus", "Oxygen", "Darwin", "Germs", "Einstein", "Quantum", "Tectonics", "DNA"];
```

These are short enough to fit under each dot. The `scrubberYears` array already
has the dates — keep those too, shown below the names.

## Change 2: Tooltips on Hover

In `buildScrubber()`, add a `<title>` child element to each dot's `<g>` group.
This gives native browser tooltip on hover.

```javascript
const tip = document.createElementNS(SVG_NS, "title");
tip.textContent = fullNames[i];  // e.g. "The Copernican Revolution (1543–1687)"
g.appendChild(tip);
```

Add a `fullNames` array:
```javascript
const fullNames = [
  "Abstract Kuhn Cycle",
  "The Copernican Revolution (1543–1687)",
  "The Chemical Revolution (1770–1789)",
  "The Darwinian Revolution (1831–1953)",
  "The Germ Theory Revolution (1847–1885)",
  "The Relativistic Revolution (1887–1919)",
  "The Quantum Revolution (1900–1927)",
  "The Continental Drift Revolution (1912–1968)",
  "The DNA Revolution (1944–1953)"
];
```

## Change 3: Active Dot Indicator

When a segment is playing, its scrubber dot should be visually distinct:
- Active dot: radius 9 (larger), bright gold fill (#d4a017), white stroke, 2px
- Inactive dots: radius 6, dim fill (#d4a01766), no stroke

In `buildScrubber()`, give each dot circle an id or store references in an array:
```javascript
const dotCircles = [];
// ... inside the loop:
dotCircles.push(c);
```

Add a function `updateActiveDot(n)`:
```javascript
function updateActiveDot(n) {
  dotCircles.forEach((c, i) => {
    if (i === n) {
      c.setAttribute("r", "9");
      c.setAttribute("fill", "#d4a017");
      c.setAttribute("stroke", "#fff");
      c.setAttribute("stroke-width", "2");
    } else {
      c.setAttribute("r", "6");
      c.setAttribute("fill", "#d4a01766");
      c.setAttribute("stroke", "none");
    }
  });
}
```

Call `updateActiveDot(n)` at the top of `playSegment(n)`.

## Change 4: Label Font Size

The scrubber label text (revolution names) should be **10px** — slightly smaller
than current 11px to fit the longer names. Keep text-anchor="middle" and the
same y positions.

## Do NOT

- Change scrubber positioning (x coordinates, y baseline)
- Change click behavior (already works)
- Change progress bar behavior
- Touch animation code

## Report

Confirm: labels show revolution names, tooltips show full titles on hover,
active dot is highlighted, inactive dots are dimmed.
