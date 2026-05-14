---
Plan-UID: 0322 Patch A
Status: READY FOR GENERATOR
---

# Patch A: Add Text-Block Navigation Dots to Magnetosphere Tutorial

## Problem

The tutorial has 3 nav dots (fixed, right side) linking to 3 SVG scenes. But 3 text blocks between the scenes are unreachable from the nav. Gen's first experience: found dots, saw all animations, couldn't find the text.

## What to modify

File: `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html`

## Content structure (current)

1. Opening scene (`#opening-wrap`) — **has dot**
2. Text block 1 (line ~430, class `text-col`) — **no dot**
3. Circuit scene (`#circuit-container`) — **has dot**
4. Text block 2 (line ~576, class `text-col`) — **no dot**
5. Gate scene (`#gate-container`) — **has dot**
6. Text block 3 (line ~660, class `text-col`) — **no dot**

## Changes

### 1. Add IDs to the 3 text blocks

- Line ~430 `<div class="text-col">` → `<div class="text-col" id="text-opening">`
- Line ~576 `<div class="text-col">` → `<div class="text-col" id="text-circuit">`
- Line ~660 `<div class="text-col">` → `<div class="text-col" id="text-gate">`

### 2. Add 3 text-dot nav entries to `<nav id="section-nav">`

Current nav (line ~292):
```html
<nav id="section-nav">
  <a href="#opening-wrap" data-label="Opening"><span></span></a>
  <a href="#circuit-container" data-label="Circuit"><span></span></a>
  <a href="#gate-container" data-label="Gate"><span></span></a>
</nav>
```

Replace with (interleave text dots after each scene dot):
```html
<nav id="section-nav">
  <a href="#opening-wrap" data-label="Opening"><span></span></a>
  <a href="#text-opening" data-label="The Field" class="text-dot"><span></span></a>
  <a href="#circuit-container" data-label="Circuit"><span></span></a>
  <a href="#text-circuit" data-label="The Storm" class="text-dot"><span></span></a>
  <a href="#gate-container" data-label="Gate"><span></span></a>
  <a href="#text-gate" data-label="The Impact" class="text-dot"><span></span></a>
</nav>
```

### 3. Add CSS for `.text-dot` style (visual distinction)

Text dots should be **square with rounded corners** (4px border-radius) instead of circular, same size (10×10px). This creates a subtle shape distinction: circles = animations, rounded squares = text. Same color scheme, same hover behavior, same active glow.

Add after the existing `#section-nav a:hover::after` rule:

```css
#section-nav a.text-dot {
  border-radius: 3px;
}
#section-nav a.text-dot.active {
  background: var(--accent);
  border-color: var(--accent);
  box-shadow: 0 0 8px var(--accent);
}
```

### 4. Update the scroll-spy JS

In the scroll-spy section (line ~2311), update the `ids` array and observer:

Replace:
```js
const ids = ['opening-wrap','circuit-container','gate-container'];
```
With:
```js
const ids = ['opening-wrap','text-opening','circuit-container','text-circuit','gate-container','text-gate'];
```

And update the observer to also observe the text blocks. The existing code at the bottom:
```js
ids.forEach(id => { const el = document.getElementById(id); if(el) spy.observe(el); });
```
This already handles any ID in the array, so no change needed there — just the `ids` array update.

### 5. Update the gap in `#section-nav`

Current gap is 16px between 3 dots. With 6 dots, reduce to 12px to keep the nav compact:

Change `gap: 16px;` to `gap: 10px;` in the `#section-nav` rule.

## Design rationale

- **Rounded squares vs circles:** Subtle shape difference that communicates "different content type" without breaking the visual language. Circles = cinematic scenes, squares = text narration. The reader doesn't need to understand this consciously — it just feels like the nav has two kinds of stops.
- **Labels:** "The Field", "The Storm", "The Impact" — short, evocative, match the tutorial's register.
- **Active color:** Text dots glow `var(--accent)` (purple) instead of `var(--earth-cyan)` (cyan) for scene dots. Two colors, two content types.

## Constraints

- Do NOT modify any SVG content, text content, or animation code
- Do NOT change the existing 3 scene dots' behavior
- Keep the nav hidden on mobile (the existing `@media (max-width: 700px)` rule already handles this)

## Report format

"Plan-UID: 0322 Patch A complete. 3 text-dot nav entries added, scroll-spy updated to 6 sections."
