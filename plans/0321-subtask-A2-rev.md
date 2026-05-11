# Subtask A2-rev: Heliocentrism Revision — Anomaly Accumulation + Slower Pacing

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321 A2-rev: Heliocentrism — anomaly accumulation, slower pacing`
**Read first:** The existing HTML file. Preserve abstract cycle (segment 0) and engine. Rewrite segment 1.

## Changes from Previous Version

### 1. Kuhn Cycle Loop: PERSISTENT, Never Redrawn

The loop with 5 phase labels from the abstract cycle stays visible at low opacity (0.25)
throughout ALL segments. Do NOT clear and redraw it. It's the permanent frame.
When revolution content flies to a position, it parks NEAR the corresponding phase label,
not replacing it.

### 2. Golden Flash: Toned Down

Reduce flash max opacity from 0.6 to 0.3. Keep the timing and clear effect.
The flash should feel like dawn breaking, not a bomb going off.

### 3. Timeline Scrubber: Show Years

Each scrubber dot should show the revolution's start year below the dot label:
- Dot 0: "Abstract" (no year)
- Dot 1: "1543"
- Dot 2: "1770"
- Dot 3: "1859"
- Dot 4: "1847"
- Dot 5: "1905"
- Dot 6: "1900"
- Dot 7: "1912"
- Dot 8: "1944"

Year text: 10px, below the label, muted (#e8e0d055).

### 4. Normal Science Phase: Name the Model Builder

Replace "They built a model to explain this" with:
"Ptolemy built a model to explain this. (~150 AD)"
Give the man credit. Name and approximate date.

### 5. ANOMALY PHASE: The Big Change

This is the core revision. The anomaly phase is NO LONGER a single text beat.
Instead, it's a SEQUENCE of individual anomalies, each alternating with a dismissive
response. The anomalies accumulate visually — each one shrinks down small and parks
in a cluster near the "Anomaly" position on the Kuhn loop.

**Pattern for each anomaly:**
1. Anomaly text appears center stage (36px, amber)
2. Reader absorbs (2s)
3. Dismissal speech bubble appears below (20px, muted, in a small rounded-rect bubble)
4. Reader absorbs (1.5s)
5. BOTH shrink to ~10px and fly to park near the Anomaly position on the loop
6. They stay there (small, readable if you squint, creating visual clutter)
7. Next anomaly appears center stage

**Heliocentrism anomalies (5 anomaly-dismissal pairs):**

| # | Anomaly (amber, center) | Dismissal (muted bubble) |
|---|------------------------|-------------------------|
| 1 | "Mars stops. Reverses direction. Then moves forward again." | "Add an epicycle." |
| 2 | "Jupiter wobbles off its predicted path." | "Another epicycle." |
| 3 | "Planets get brighter and dimmer throughout the year." | "The sphere is slightly off-center." |
| 4 | "Epicycles needed: 40... 52... 79..." (counter animates) | "The math works. Don't question the model." |
| 5 | "Copernicus: what if the Earth moves around the Sun? (1543)" | "Interesting mathematics. But obviously the Earth doesn't move." |

After all 5 pairs have accumulated near the Anomaly position, the cluster is visibly
messy. Pause 1s to let the reader SEE the clutter. THEN move to Crisis phase.

**Timing:** Each pair takes ~4s (2s anomaly + 1.5s dismissal + 0.5s fly). 5 pairs = ~20s
for the anomaly section alone. The total revolution duration extends to ~40s.
THAT'S FINE. Slower is better. The accumulation IS the lesson.

### 6. Crisis Phase

After anomalies have accumulated, the Crisis phase adds 1-2 more hostile quotes:
- *"The Earth MOVES? Absurd. I can feel that it doesn't."*
- *"De Revolutionibus — ignored for 70 years."*

These also shrink and park near the Crisis position. Screen is now cluttered with
anomalies AND dismissals AND crisis quotes. Maximum visual discomfort.

### 7. Revolution Phase

Golden flash (toned down, opacity 0.3) clears the accumulated clutter.
"Galileo points his telescope at Jupiter." + "Four moons. Orbiting Jupiter. Not Earth."
This part stays roughly the same as before but with the reduced flash.

### 8. New Paradigm Phase

Same as before. Title bar strikethrough + new paradigm in gold.
"Navigation. Celestial mechanics. Space travel."

## Updated Beat Structure (~40 seconds total for Heliocentrism)

| Time | Phase | What happens |
|------|-------|-------------|
| 0-5s | Normal Science | Sun crosses sky. Ptolemy builds model (~150 AD). Nested circles icon. |
| 5-25s | Anomaly Accumulation | 5 anomaly-dismissal pairs, each ~4s. Each shrinks + parks near Anomaly position. Clutter grows. |
| 25-26s | Pause | Reader sees the accumulated mess. |
| 26-30s | Crisis | Hostile quotes. More clutter near Crisis position. |
| 30-32s | Revolution | Golden flash (opacity 0.3). Clutter clears. Galileo + telescope. |
| 32-36s | Clean moment | "Four moons. Orbiting Jupiter." Name: Galileo, 1610. |
| 36-40s | New Paradigm | Title bar resolves. Navigation. Space travel. |

## Technical Notes

- The anomaly parking cluster: position the shrunken items in a loose cluster around
  the Anomaly phase position on the loop. Offset each item slightly so they don't
  overlap perfectly — create visual mess, not a neat stack.
- Shrunken anomaly text: 10-12px, opacity 0.7. Readable if you look closely but
  the MASS of them is what matters, not individual legibility.
- The persistent Kuhn loop labels should be behind (lower z-order than) the
  revolution content that parks near them.
- Update the year display in upper-right to show years jumping per anomaly too.

## Report

State: file size, segment 1 duration (should be ~40s), anomaly count visible, what works.
