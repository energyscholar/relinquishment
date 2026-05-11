# Subtask: Make Old Paradigm Text More Prominent

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: old paradigm bigger, brighter, better positioned in title bar`
**Read first:** The CURRENT state of the file.

## Problem

The old paradigm text (titleLine2) is faded, too small, and gets hidden under
other text. It should be the MOST PROMINENT thing on screen throughout each
revolution. Currently it's 26px at y=60, cream-colored (#e8e0d0), inside a dark
panel that ends at y=80. It's cramped and easy to miss.

## Fix 1: Enlarge Title Bar Panel

The background rect (line ~37) is currently:
```xml
<rect x="100" y="5" width="1000" height="75" .../>
```
Change to:
```xml
<rect x="100" y="5" width="1000" height="95" .../>
```

This gives more vertical space for the old paradigm text.

## Fix 2: Reposition and Enlarge Old Paradigm Text

**titleLine1** (revolution name): keep at y=22, 18px. This is a quiet header.

**titleLine2** (old paradigm): change from y=60, 26px to **y=72, 30px**.
Bigger, lower in the panel, more breathing room from titleLine1 above.
Color stays #e8e0d0 (white/cream), bold. Opacity must be **1.0** — never
faded during normal display.

Update ALL places that set titleLine2's y and font-size:
- SVG markup (line ~39): y="60" → y="72", font-size="26" → font-size="30"
- clearStage() (~line 297-300): y "60" → "72", font-size "26" → "30"
- Segment 0 setup (~line 365): y "60" → "72", font-size "26" → "30"
- Factory setup keyframe (~line 746): y "50" or "60" → "72", font-size → "30"
- Death sequence deathEl creation: starts at y=72, 30px (matching title position)

Search for ALL occurrences of `titleLine2.setAttribute("y"` and
`titleLine2.setAttribute("font-size"` and update consistently.

## Fix 3: Title Strike and New Paradigm Position

titleStrike (strikethrough line): y1 and y2 must match titleLine2's new y=72.
Search for all `titleStrike.setAttribute("y1"` and update to "72".

titleLine3 (new paradigm, appears after death): also y=72 to match.
Search for all `titleLine3.setAttribute("y"` and update to "72".

SVG markup (lines ~40-41): update y values to 72.

## Fix 4: OLD PARADIGM Label

The small "OLD PARADIGM" label (~line 793) positioned above titleLine2.
Currently at y=43. Change to **y=55** (stays above the now-lower titleLine2).

## Fix 5: Z-Order

The title bar group should render ON TOP of other content. In the SVG markup,
move `<g id="title-bar">` to AFTER `<g id="loop-labels">` and
`<g id="center-stage">` so it renders last (on top). SVG paints in document
order — later elements are on top.

Currently the order in the SVG is approximately:
```
cycle-path → loop-labels → center-stage → title-bar → ...
```
If title-bar is already after center-stage, it should paint on top. Verify this
is the case. If not, move it.

## Do NOT

- Change the death sequence timing or order
- Change the green→blue transition
- Change any animation besides positioning
- Touch loop or center-stage content

## Report

Confirm: old paradigm text at 30px, y=72, fully opaque, visible above all other
content throughout each revolution. Report any text that still overlaps it.
