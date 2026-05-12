# Subtask: SVG-055 — "Not Precluded" Expert Consensus Spectrum

**Output:** Create inline SVG in `build/images/scientific-revolutions-chapter.html`
(inside Section 4, after the A1/A2 fork presentation)
**Commit:** `Plan 0321: SVG-055 — expert consensus spectrum with animated historical markers`
**Read first:** The chapter HTML, Plan 0321 master plan (SVG-055 spec, lines 321–331).

## What This Image Does

A horizontal spectrum bar from "Impossible" to "Established." Historical markers
show where previous revolutions STARTED on this spectrum and where they ENDED.
A gold marker shows where "Autocatalytic QH Computation, 2026" sits RIGHT NOW.

The gold marker doesn't move. The historical markers migrate. The contrast
between movement (past revolutions resolving) and stillness (current question
unresolved) is the visual argument.

## Layout

```
 Impossible ←─────────────────────────────────→ Established
     |          |              |            |          |
  "absurd"  "probably    "not precluded"  "likely"  "obvious"
              not"            ▲
                              │
                     Autocatalytic QH (2026)
                         [GOLD, STILL]

  Historical markers (animate left→right over time):
  ● Continental drift:  "absurd" (1912) → "obvious" (1965)   53 years
  ● Germ theory:       "probably not" (1847) → "obvious" (1880)  33 years
  ● Heliocentrism:     "absurd" (1543) → "established" (1687)  144 years
```

## Visual Design

- Dark background matching chapter (#1a1a2e)
- Spectrum bar: gradient from red (#c45c5c, impossible) through amber (#d4a017,
  not precluded) to green (#5c9c5c, established). ~800px wide, 8px tall.
- Five labeled tick marks along the bar (Impossible, Probably Not, Not Precluded,
  Likely, Established). Cream text (#e8e0d0), 12px.
- Historical markers: small circles (8px), white stroke, colored fill matching
  their final position (green when "obvious"). Each has a label below with
  name + year range. 11px, muted (#aaa).
- Gold marker: larger (12px), gold fill (#d4a017), bold stroke, pulsing glow
  (subtle CSS animation, 2s cycle). Label below: "Autocatalytic QH, 2026" in
  gold, 13px.
- Annotation at bottom: *"Every revolution starts here. Most things that start
  here are not revolutions."* Italic, 11px, muted.

## Animation

On load (or on scroll into view), historical markers animate from their START
position to their END position over 3 seconds (staggered 0.5s apart):

1. Continental drift slides from "absurd" to "established" (1.5s)
2. Germ theory slides from "probably not" to "established" (1.5s)
3. Heliocentrism slides from "absurd" to "established" (1.5s)

After all three settle, brief pause (1s), then the gold marker fades in at
"not precluded" with a gentle pulse. It stays. Everything else moved. It didn't.

Use CSS animations or lightweight JS. IntersectionObserver to trigger on scroll
is ideal (animation plays when user scrolls to it, not on page load).

## Wrapping

Wrap in `<details open>` accordion matching the animation's style:
```html
<details open class="svg-panel">
  <summary>Expert Consensus Spectrum — Where Are We?</summary>
  <svg ...>...</svg>
  <p class="caption"><em>"Every revolution starts here. Most things that start
  here are not revolutions."</em></p>
</details>
```

## Size

Inline SVG, not iframe. ViewBox ~900x200. Small enough to sit comfortably
in the 800px text column without scrolling.

## Do NOT

- Make the gold marker move (it stays at "not precluded" — that's the point)
- Add interactivity beyond the initial animation
- Change chapter text
- Use external libraries

## Report

Confirm: animation plays on scroll, gold marker stays still, historical markers
migrate, annotation visible. Screenshot or open in browser.
