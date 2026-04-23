# Plan 0222a — Kauffman Button Sequence: Scaffold

**Status:** DONE (executed in non-Argus shell; verified by Argus S59)
**Author:** Auditor
**Priority:** High
**EV:** Stable — no T/F regression. T3 (life in the Flat) gets a visual on-ramp to phase transitions. T5 (silence gap) gets the domain diagram inline. No F-mode triggers (diagrams are factual).
**Scope:** `build/preprocess.py`
**Phase:** 1 of 3 (0222a scaffold → 0222b filmstrip polish → 0222c domain polish)
**Parent:** Supersedes Plan 0222

## Purpose

Get the injection machinery working and the SVGs visible so Bruce can review structure, placement, and pedagogical flow. The SVGs will be ugly — correct structure, correct counts, wrong aesthetics. That's the point: nail the skeleton before polishing.

## Changes

### 1. `build/preprocess.py` — Add `inject_button_sequence()` function

New function following the pattern of `inject_flat_diagram()`.

**Contains:** Four SVG strings (`BUTTONS_SVG_1` through `BUTTONS_SVG_4`) wrapped in a single `<figure class="inline-svg button-sequence">`.

**SVG requirements (structure only — aesthetics deferred to 0222b):**

- **Dimensions:** Each panel `width="380" height="220" viewBox="0 0 500 290"`
- **Floor:** Dashed line at y=250 in each panel
- **Buttons:** 30 circles per panel, r=9, fill `#c4a97d`, stroke `#a88b5e`. Positions can be rough/grid-like — exact scatter deferred to 0222b.
- **Panel 1 "Scatter":** 30 buttons on floor. 0 threads. Counter: `0 / 30`. Caption: *"Ten thousand buttons on a floor."*
- **Panel 2 "First threads":** 30 buttons, 6 threads connecting random pairs, 1 pair lifted. Counter: `6 / 30`. Caption: *"Pick up one button. Only its partner lifts."*
- **Panel 3 "Clusters":** 30 buttons, 14 threads, several disconnected clusters (largest ≤8), one cluster lifted. Counter: `14 / 30`. Caption: *"Small clusters — three, five, eight. The clusters grow slowly."*
- **Panel 4 "Phase transition":** 30 buttons, 15 threads (14 grey + 1 red `#c0392b`), 22-25 buttons lifted from one point. Counter: `15 / 30`. Caption: *"One more thread. The whole room lifts."*
- **Panel labels:** Top-left corner of each SVG, small grey text (font-size 9): "scatter", "first threads", "clusters", "phase transition"
- **Filmstrip layout:** Vertical stack inside one `<figure>`. Shared figcaption at bottom: *"Kauffman's buttons and threads — scatter, connect, cluster, snap."*

**Injection point:** After the `</p>` following the text `"Below the threshold: isolated clusters. Above it: a giant connected web."` in the rendered HTML (from `genesis.tex` line 33). If marker not found, skip silently.

**Print:** `"  Button sequence: 4-panel filmstrip injected"`

### 2. `build/preprocess.py` — Add `inject_domain_buttons()` function

Injects the existing 11-domain button SVG as an inline figure.

**Source SVG:** Copy from `hover-definitions.yaml` key `buttons-and-threads` (line 239). Modifications for inline display:

- Change `width="380"` → `width="460"`, keep viewBox as-is
- Remove the hand/lever: delete the `<path d="M 248,18...">` (lever shape), the `<line x1="250" y1="28"...>` (lever stem), and the `<line x1="250" y1="48"...>` (thread from lever to NN button). The NN button stays.
- Add text annotation above dashed grey threads: `"— missing bridges —"` in grey italic, font-size 8
- Keep everything else: colored clusters, domain labels, TQC dangling, floor line, captions, attribution

**Wrap** in `<figure class="inline-svg domain-buttons">` with figcaption: *"The same metaphor, applied to this book. Eleven scientific domains, connected by published cross-references. TQC dangles by a single thread."*

**Injection point:** After the `</p>` following text containing `"five published research streams had independently matured"` (from `genesis.tex` line 64). If marker not found, skip silently.

**Print:** `"  Domain buttons: inline diagram injected"`

### 3. Call site

Add both calls in the post-processing pipeline in `build/preprocess.py`, after `inject_flat_diagram` and before `fix_html_glossary_names`. Order: `inject_button_sequence()` then `inject_domain_buttons()`.

### 4. No manuscript changes

LaTeX files untouched. SVGs injected during HTML post-processing only.

## What is NOT changed

- `hover-definitions.yaml` — the 11-domain tooltip stays as-is
- LaTeX source files — no modifications
- PDF output — inline SVGs are HTML-only

## Acceptance Tests

After `make html`:

1. **Filmstrip present:** `grep -c 'button-sequence' output.html` returns ≥1
2. **4 panels:** The filmstrip container contains exactly 4 `<svg` elements
3. **30 buttons each:** Each panel SVG contains exactly 30 `<circle` elements with r="9"
4. **Thread counts:** Panel 1: 0 threads. Panel 2: 6. Panel 3: 14. Panel 4: 15 (14 grey + 1 red)
5. **Red thread:** Panel 4 has exactly one `<line` with stroke="#c0392b"
6. **Counters:** Each panel shows its ratio text
7. **Domain diagram present:** `grep -c 'domain-buttons' output.html` returns ≥1
8. **Domain diagram after filmstrip:** `domain-buttons` appears after `button-sequence` in HTML
9. **11 domain labels:** Domain diagram has 11 labeled circles (NN, Neuro, CMP, TFT, ACS, Auto, CE, Par, NLD, Mat, TQC)
10. **No lever:** Domain diagram contains no `<path d="M 248,18` (lever removed)
11. **Hover tooltip intact:** `buttons-and-threads` key still present in hover-data JSON
12. **No LaTeX changes:** `git diff manuscript/` shows no modifications
13. **Build succeeds:** `make html` exits 0, deep-link verification passes
