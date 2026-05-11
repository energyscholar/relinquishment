# Subtask A2: Heliocentrism Revolution + Title Bar + Year Display

**Output:** Modify `build/images/scientific-revolutions-draft.html` (extend, don't overwrite)
**Commit:** `Plan 0321 A2: Heliocentrism revolution + title bar + year display`
**Read first:** The existing HTML file from Subtask A1. Preserve all existing code (JS engine, abstract cycle, scrubber). Add to it.

## What to Build

Add three new mechanisms to the existing animation engine, plus Revolution 1 content.

### Mechanism 1: Title Bar

A persistent header area at the top of the SVG (y: 15-45). Two lines:
- **Line 1 (20px, white):** Revolution name + date span. E.g., "The Copernican Revolution (1543–1687)"
- **Line 2 (15px, #e8e0d0aa italic):** The old paradigm stated as confident FACT. Not labeled "belief" — stated with the certainty people had.

Title bar fades in when a revolution starts, persists throughout.
On revolution resolve: Line 2 gets a strikethrough (CSS/SVG line drawn through it). A new gold line appears below: the new paradigm. Pause 2s. Then title bar fades out before next revolution.

Title bar is EMPTY during the abstract cycle (segment 0). Only appears for segments 1+.

### Mechanism 2: Year Display

Small text (14px, #e8e0d088) in the upper-right corner (x: 1150, y: 30, right-aligned).
Shows the SPECIFIC YEAR for the current phase. Years JUMP between phases (no smooth ticker).
The irregular jumps teach the rhythm: centuries of calm, decades of upheaval.

### Mechanism 3: Revolution Segment Pattern

Each revolution is a new segment (segment 1, 2, etc.) using the existing engine's `playSegment(n)` API. The scrubber dot for that segment becomes active (gold, clickable).

Each revolution follows this 20-second beat structure:

| Time | Phase | Color | Center Stage |
|------|-------|-------|-------------|
| 0-4s | Normal Science | Blue #4a90d9 | Big text: what people SAW/BELIEVED. Then text shrinks + flies to "Normal Science" position on Kuhn loop. |
| 4-8s | Anomaly | Amber #d4a574 | Big text: what didn't fit. Shrinks + flies to "Anomaly" position. |
| 8-12s | Crisis/Refusal | Red #c45c5c | Speech bubble with dismissive quote. Shrinks + flies to "Crisis" position. Screen now cluttered with 3 items on loop. |
| 12-16s | Revolution | Gold #d4a017 | The dramatic moment. Golden flash at 12s clears the loop. Clean gold text center. |
| 16-20s | New Paradigm | Green #5c9c5c | What it gave us. Fades in clean. Title bar strikethrough + new paradigm. |

The Kuhn cycle loop (from abstract) stays visible as the FRAME. Revolution content accumulates at the same 5 positions. This reinforces the pattern learned in the abstract cycle.

## Revolution 1: Heliocentrism

**Scrubber:** Activate dot 1. Label: "1". Gold when active.

**Title bar:**
- Line 1: "The Copernican Revolution (1543–1687)"
- Line 2: "The earth is at the center. The sun, moon, and stars revolve around it."
- On resolve: strikethrough Line 2. New: "The earth moves around the sun. The solar system is vast."

**Year display per phase:**
- Normal: "~1400"
- Anomaly: "1543"
- Crisis: "1543–1610"
- Revolution: "1610"
- New Paradigm: "1687"

**Phase content (center stage text, 36px unless noted):**

**Normal (0-4s, blue):**
"The sun rises east, crosses the sky, sets west."
Pause 1.5s. Then below (24px): "They built a model to explain this."
Small icon: nested circles (Earth center, simple orbits). This is what people LIVED.

**Anomaly (4-8s, amber):**
"Mars stops. Goes backward. Then forward again."
Below (20px): A counter animates: "Epicycles needed: 12... 37... 52... 79"
The counter ticking up IS the accumulation of patches. Getting ugly.

**Crisis (8-12s, red):**
Speech bubble shape containing:
*"The Earth MOVES? Absurd. I can feel that it doesn't."*
Below (16px, muted): "De Revolutionibus — ignored for 70 years"

**Revolution (12-16s, gold):**
Golden flash at 12s clears accumulated loop elements.
"Galileo points his telescope at Jupiter."
Below (24px): "Four moons. Orbiting Jupiter. Not Earth."
Small icon: circle (Jupiter) with 4 tiny dots around it.
Name appears small below (14px): "Galileo, 1610"

**New Paradigm (16-20s, green):**
"Navigation. Celestial mechanics. Space travel."
Small icon: simple solar system (sun center, orbits).
Title bar resolves (strikethrough + new paradigm in gold).

## Technical Notes

- Register segment 1 in the engine's segment map alongside segment 0
- When segment 1 starts, clear the abstract cycle's "YOU ARE HERE" if visible
- The Kuhn cycle loop labels (Normal Science, Anomaly, Crisis, Revolution, New Paradigm) from the abstract stay as faint guides (opacity 0.3) — the revolution content appears at the same positions but with historical specifics
- Speech bubble: rounded rect with a small triangle pointer, fill #c45c5c22, stroke #c45c5c
- Keep the same animation patterns from A1: pop-scale entry, arc fly-to-position, golden flash clear

## Report

State: file size, segment 1 duration, what works, what needs tuning.
