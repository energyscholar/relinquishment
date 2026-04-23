# Plan 0222 — Kauffman Button Sequence (4-panel SVG)

**Status:** SUPERSEDED by 0222a/b/c  
**Author:** Generator (design approved by Bruce)  
**Scope:** `build/preprocess.py`  
**Rationale:** The Kauffman buttons-and-threads analogy is the book's primary on-ramp to phase transitions, but readers are getting it from words alone. Four inline SVGs illustrate the *process* of the thought experiment — scatter, connect, cluster, snap — so the phase transition is visual before the reader maps it to chemistry or computation. Then the existing 11-domain SVG (currently hover-only) is promoted to an inline figure, showing the same metaphor applied to the book's argument. Pedagogical sequence: learn the analogy, then see it used.

## Design Specification

### Consistent elements across all 4 panels

- **Dimensions:** `width="380" height="220" viewBox="0 0 500 290"`
- **Wrapper:** The filmstrip uses a single `<figure class="inline-svg button-sequence">` (see Changes §1). Individual panel SVGs have no wrapper.
- **Floor:** dashed line at y=250: `<line x1="20" y1="250" x2="480" y2="250" stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>`
- **Buttons:** 30 circles, r=9, fill `#c4a97d` (warm tan), stroke `#a88b5e`, stroke-width 1, drop-shadow filter. No labels. Same 30 (x,y) positions across all panels — buttons that are "on the floor" sit at y=240; lifted buttons rise above.
- **Threads:** stroke `#666`, stroke-width 1.2, opacity 0.6. Taut when lifted (straight diagonal to lifted positions). The critical thread in Panel 4 is stroke `#c0392b` (red), stroke-width 2.
- **Counter:** bottom-right corner, small text showing `threads / buttons` ratio. Font: Georgia serif, size 10, fill #999.
- **Caption font:** Georgia serif, size 10, fill #555, centered below floor line. Each panel's caption is rendered as `<text>` inside the SVG, not as a separate HTML element.

### 30 button positions (x coordinates, floor y=240)

Use these x-positions for horizontal scatter (buttons spread across the floor):

```
x_positions = [
    35, 60, 88, 110, 138, 158, 182, 205, 228, 248,
    272, 295, 315, 340, 362, 385, 408, 432, 455, 475,
    50, 75, 125, 170, 215, 260, 305, 350, 395, 440,
]
```

Rows: first 20 buttons at y=240 (floor), last 10 at y=225 (slightly staggered for depth). When lifted, buttons rise to their designated y-position (varies by panel).

### Panel 1: "Scatter"

- **All 30 buttons on the floor.** No threads. No lifting.
- **Counter:** `0 / 30`
- **Caption:** *"Ten thousand buttons on a floor."*
- **Visual purpose:** Establish the setup. Inert. Nothing connects.

### Panel 2: "First threads"

- **6 threads** connecting random pairs, spread across the layout (not adjacent buttons only — the randomness matters).
- **One pair lifted:** One connected pair rises above the floor — the top button at y≈180, its partner at y≈195. Thread between them goes taut. All other connected pairs stay flat.
- **24 buttons** unconnected, on floor.
- **Counter:** `6 / 30`
- **Caption:** *"Pick up one button. Only its partner lifts."*

### Panel 3: "Clusters"

- **14 threads.** Ratio 14/30 = 0.47 — just below Kauffman's 1/2 threshold.
- **Constraint: fragmented.** Several disconnected clusters: at least 4 clusters of varying sizes (2, 3, 4, 5 buttons). No giant component — the largest cluster should be ≤8 buttons. ~8–10 buttons remain fully isolated.
- **One cluster lifted** (the largest, ~5 buttons): lifted as a unit from one button, others dangling at y=145–170. All other clusters stay on the floor. This shows that lifting still only grabs a small piece.
- **Visual key:** The two largest clusters should be positioned near each other but visibly disconnected — no thread between them. This sets up Panel 4.
- **Counter:** `14 / 30`
- **Caption:** *"Small clusters — three, five, eight. The clusters grow slowly."*

### Panel 4: "Phase transition"

- **15 threads.** Ratio 15/30 = 0.50 — exactly at Kauffman's threshold.
- This panel represents a later moment: between Panel 3 and Panel 4, the process continued off-screen. The topology has evolved — more threads were added, clusters grew and merged. We show the moment the giant component snaps into existence.
- **Topology constraint:** 14 grey threads form two large sub-networks (roughly equal size, ~10–12 buttons each) that are NOT connected to each other. One **red thread** (stroke `#c0392b`, stroke-width 2) bridges them. This is thread 15 — the one that crosses the threshold. The two sub-networks together span 22–25 buttons; the rest are isolated.
- **Cascade:** Lifting one button from the top of the network now pulls up **22–25 of 30 buttons.** Only 5–8 truly isolated buttons remain on the floor. The visual should feel like a net being hauled from one point — threads taut at various angles, buttons at staggered heights (highest near the lift point at y≈60, lowest dangling at y≈200).
- **Counter:** `15 / 30` — with the "15" in bold or red to mark the threshold.
- **Caption:** *"One more thread. The whole room lifts."*

## Changes

### 1. `build/preprocess.py` — Add `inject_button_sequence()` function

Add a new function `inject_button_sequence(html_path)` following the pattern of `inject_flat_diagram()`:

- Contains four SVG strings: `BUTTONS_SVG_1` through `BUTTONS_SVG_4`
- **All four panels are wrapped in a single `<figure class="inline-svg button-sequence">`** container, displayed as a vertical filmstrip (serial sequence). Individual panels are separated by minimal spacing. One shared `<figcaption>` at the bottom: *"Kauffman's buttons and threads — scatter, connect, cluster, snap."*
- **Layout:** Stack the four SVGs vertically inside the figure. Each panel gets a subtle label in the top-left corner (Panel 1: "scatter", Panel 2: "first threads", Panel 3: "clusters", Panel 4: "phase transition") using small grey text, font-size 9.
- **Single injection point:** Insert the entire filmstrip after the `</p>` following text containing `"Below the threshold: isolated clusters. Above it: a giant connected web."` — this is the end of the two-paragraph description (lines 28–30 of genesis.tex). The filmstrip appears after the full analogy is stated, as a visual summary of the process just described.

If the marker is not found, skip silently.

Print: `"  Button sequence: 4-panel filmstrip injected"`

**Call site:** Add `inject_button_sequence(html_path)` in the post-processing pipeline, after `inject_flat_diagram` and before `fix_html_glossary_names`. (~line 2431 area, find the call sequence.)

### 2. `build/preprocess.py` — Add `inject_domain_buttons()` function

After the filmstrip, inject the existing 11-domain button SVG as an **inline figure** — not just a hover tooltip. This is the payoff: the reader just learned what buttons-and-threads means, now they see it applied to the book's argument.

**Injection point:** After the `</p>` following text containing `"five published research streams had independently matured"` — this is the paragraph (line 61 of genesis.tex) where the five fields are named. The 11-domain diagram appears immediately after, showing the network those five fields create.

**Source SVG:** Copy the SVG from `hover-definitions.yaml` key `buttons-and-threads` into the function as a constant. Modifications for inline display:

- **Wider:** Change `width="380"` → `width="460"`, keep viewBox as-is (the SVG scales).
- **Remove the hand/lever:** Delete the `<path d="M 248,18...">` (lever shape), the `<line x1="250" y1="28"...>` (lever stem), and the `<line x1="250" y1="48"...>` (thread from lever to NN button). The filmstrip already taught "lifting" — the inline version is a static network diagram, not a demonstration of lifting. The NN button stays; only the lever above it is removed.
- **Add a bridge label:** Above the dashed grey threads, add a small text annotation: `"— missing bridges —"` in grey italic, font-size 8. This makes the dashed lines' meaning self-evident without requiring the tooltip's explanatory paragraph.
- **Keep everything else:** colored clusters, domain labels, TQC dangling, floor line, "One thread holds" caption, attribution.
- **Wrap** in `<figure class="inline-svg domain-buttons">` with figcaption: *"The same metaphor, applied to this book. Eleven scientific domains, connected by published cross-references. TQC dangles by a single thread."*

The hover tooltip in `hover-definitions.yaml` stays **unchanged** — it still works as a quick reference when readers hover "buttons" elsewhere in the book.

If the marker is not found, skip silently.

Print: `"  Domain buttons: inline diagram injected"`

**Call site:** Immediately after `inject_button_sequence()` in the post-processing pipeline.

### 3. Manuscript files — No changes

The tex files are NOT modified. The SVGs are injected during HTML post-processing, same as the Flat diagram. This keeps the LaTeX clean and the SVGs maintainable in one place (preprocess.py).

## What is NOT changed

- `hover-definitions.yaml` — the 11-domain button SVG tooltip stays as-is (still works as hover)
- LaTeX source files — no modifications
- PDF output — inline SVGs are HTML-only

## Acceptance Tests

After `make html`:

1. **Filmstrip present:** `grep -c 'button-sequence' output.html` returns at least 1 (the container figure).
2. **All 4 panels inside:** The filmstrip container contains exactly 4 `<svg` elements, in order: scatter, first threads, clusters, phase transition.
3. **Button count:** Each filmstrip SVG contains exactly 30 `<circle` elements with r="9".
4. **Thread counts (excluding floor line):** Panel 1: 0 thread `<line` elements (1 floor line only). Panel 2: 6 + 1 floor = 7 total. Panel 3: 14 + 1 = 15 total. Panel 4: 15 + 1 = 16 total. Count threads by subtracting the floor `<line` from total `<line` count per SVG.
5. **Red thread:** Panel 4 contains exactly one `<line` with stroke="#c0392b".
6. **Counter text:** Each panel shows its thread/button ratio.
7. **Domain diagram present:** `grep -c 'domain-buttons' output.html` returns at least 1.
8. **Domain diagram position:** The `domain-buttons` figure appears AFTER the `button-sequence` figure in the HTML.
9. **11 domain labels:** The domain diagram contains exactly 11 labeled circles (NN, Neuro, CMP, TFT, ACS, Auto, CE, Par, NLD, Mat, TQC).
10. **Hover tooltip intact:** `hover-definitions.yaml` key `buttons-and-threads` is still present in hover-data JSON.
11. **No LaTeX changes:** `git diff manuscript/` shows no modifications.
12. **Visual check:** Open the HTML, scroll to Chapter "Genesis". After "Buttons and Threads" text: 4-panel filmstrip (the analogy). After "From Chemistry to Computation" text: 11-domain diagram (the application). Pedagogical sequence: learn the metaphor, then see it applied. Both should be clearly legible and visually consistent (same floor line, same button style).

## Handoff Prompt

```
You are the Generator. Read and execute plans/0222-kauffman-button-sequence.md.

One file to modify: build/preprocess.py. Two new functions:

1. inject_button_sequence() — 4-panel vertical filmstrip in one <figure>,
   injected after "Below the threshold / Above it" paragraph.
2. inject_domain_buttons() — the 11-domain SVG from hover-definitions.yaml,
   adapted for inline display (wider, no hand/lever, add "missing bridges"
   label), injected after "five published research streams" paragraph.

Add both calls in the post-processing pipeline after inject_flat_diagram.
No manuscript changes. Run make html and verify all 12 acceptance tests.
Report completion.
```
