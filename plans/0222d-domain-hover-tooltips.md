# Plan 0222d — Domain Button Hovers + Tooltip Sync

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor
**Priority:** Medium
**Scope:** `build/preprocess.py` (domain SVG constant) + `build/hover-definitions.yaml`
**Phase:** 4 of 4 (0222a scaffold → 0222b filmstrip → 0222c domain rebuild → 0222d hovers)

## Purpose

Two fixes:
1. **Per-button rich tooltips** on the inline domain diagram — tap/hover any domain button to learn what it is
2. **Sync the `buttons-and-threads` hover tooltip** in hover-definitions.yaml — still shows old SVG (NN, Neuro, lever)

## Why this works without reader.js changes

Reader.js line 1080: `querySelectorAll('[data-hover], [data-hover-id]')` — binds to ANY element with `data-hover`, including SVG `<g>` elements inside inline SVGs.

Reader.js line 1136: `e.target.closest('[data-hover], [data-hover-id]')` — event delegation walks up from tapped `<circle>` or `<text>` to parent `<g data-hover>`. Works in all modern browsers on SVG elements.

Reader.js line 1044: `termRect.bottom + gap` — `getBoundingClientRect()` works on SVG `<g>`, returns viewport-relative coords. Tooltip positions correctly.

No reader.js patch needed. Verified.

---

## Phase 1: Per-button tooltips on inline domain diagram

### File: `build/preprocess.py`, function `inject_domain_buttons()` (line 2581)

### Current structure (lines 2615-2638):

```
  <!-- buttons -->
  <circle cx="250" cy="55" .../>     ← line 2616 (Topo)
  <circle cx="190" cy="108" .../>    ← line 2617 (TFT)
  ... (11 circles, lines 2616-2626)
  <!-- button labels -->
  <text x="250" y="59" ...>Topo</text>    ← line 2628
  <text x="190" y="112" ...>TFT</text>    ← line 2629
  ... (11 labels, lines 2628-2638)
```

### Required structure:

Replace the separate circles block + labels block with 11 `<g>` groups. Each `<g>` contains its circle + label and has a `data-hover` attribute. Buttons must still render AFTER threads (draw order preserved).

```xml
  <!-- domain buttons (interactive) -->
  <g data-hover="Topology \u2014 the mathematics of shape and invariance. Knot theory, manifold classification. Freedman\u2019s Fields Medal." style="cursor:pointer">
    <circle cx="250" cy="55" r="16" fill="#2471a3" stroke="#1a5276" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="250" y="59" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">Topo</text>
  </g>
  <g data-hover="Topological field theory \u2014 where quantum physics meets topology. Witten 1989: TQFT from knot invariants." style="cursor:pointer">
    <circle cx="190" cy="108" r="16" fill="#2980b9" stroke="#2471a3" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="190" y="112" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">TFT</text>
  </g>
  ... etc for all 11
```

### Circle-to-label pairing (exact line mapping):

| Button | Circle (line) | Label (line) | data-hover text |
|--------|--------------|-------------|-----------------|
| Topo | 2616 `cx=250 cy=55` | 2628 | Topology \u2014 the mathematics of shape and invariance. Knot theory, manifold classification. Freedman\u2019s Fields Medal. |
| TFT | 2617 `cx=190 cy=108` | 2629 | Topological field theory \u2014 where quantum physics meets topology. Witten 1989: TQFT from knot invariants. |
| CMP | 2618 `cx=310 cy=108` | 2630 | Condensed matter \u2014 the fractional quantum Hall effect, 2D electron gases, anyon excitations. Laughlin-Stormer-Tsui Nobel 1998. |
| TQC | 2619 `cx=250 cy=220` | 2631 | Topological quantum computation \u2014 braiding non-Abelian anyons for fault-tolerant gates. Freedman-Kitaev-Wang 2002. The single thread. |
| Sol | 2620 `cx=58 cy=82` | 2632 | Soliton physics \u2014 stable, self-reinforcing wave packets. Hasslacher\u2019s lattice-gas automaton (1986). Classical topological protection. |
| NLD | 2621 `cx=58 cy=140` | 2633 | Nonlinear dynamics \u2014 chaos, bifurcations, self-organized criticality. The mathematics of systems far from equilibrium. |
| ACS | 2622 `cx=442 cy=82` | 2634 | Autocatalytic sets \u2014 Kauffman\u2019s theory of self-organization. Phase transitions in random graphs. Life as a critical phenomenon. |
| Auto | 2623 `cx=442 cy=140` | 2635 | Autopoiesis \u2014 Maturana and Varela (1980). Self-producing systems. The boundary between living and non-living. |
| CE | 2624 `cx=372 cy=228` | 2636 | Computational universality \u2014 Wolfram\u2019s Principle of Computational Equivalence. Sufficiently complex systems compute, regardless of substrate. |
| Par | 2625 `cx=372 cy=278` | 2637 | Parallel computation \u2014 Hillis\u2019s Connection Machine. Massively parallel architectures that scale. |
| Mat | 2626 `cx=110 cy=252` | 2638 | Materials science \u2014 the engineering discipline that builds the substrates. pHEMT, MOSFET, semiconductor fabrication. |

### Important notes:

- **Use `\u2014` for em dash and `\u2019` for apostrophes** in the Python string — these are Unicode escapes inside the triple-quoted `DOMAIN_SVG` constant. They render as `—` and `'` in the HTML output.
- **No double quotes** inside `data-hover` values (values are double-quoted HTML attributes). All descriptions above are double-quote-free. ✓
- **Draw order preserved:** All `<g>` groups appear after threads (after line 2614). Each `<g>`'s circle renders, then its label on top. Since no buttons overlap (minimum separation 50px > 32px diameter), no circle can cover another button's label. ✓
- **TQC arrow** (line 2640) stays outside any `<g>` — it's decoration, not a button.
- **Captions and legend** stay unchanged.

---

## Phase 2: Update `buttons-and-threads` hover tooltip

### File: `build/hover-definitions.yaml`, line 237

The current entry (lines 237-239) has the old SVG with NN, Neuro, lever. Replace the entire `html:` value.

### New content for the entry:

**Intro paragraph:**
```html
<p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>Buttons and threads</strong> \u2014 Kauffman\u2019s thought experiment, mapped to eleven scientific domains in five clusters. Solid threads: published cross-references. Dashed grey: bridges no one has built.</p>
```

**SVG:** Copy the diagram portion of the inline SVG (lines 2587-2643 of preprocess.py) with these modifications:

1. **Rendered size:** `width="380" height="280"` (smaller for tooltip)
2. **ViewBox:** `viewBox="0 0 500 390"` (crops out legend below y=390)
3. **Remove `<title>` element** (line 2588) — tooltip is already a hover panel; native title tooltip would be nested/redundant
4. **Rename filter ID:** `dbtn-sh` → `dbtn-sh-tt` everywhere (the `<filter id=` definition AND all 11 `filter="url(#...)"` references). Prevents collision with the inline diagram's filter on the same page.
5. **NO `<g data-hover>` wrappers** — keep circles and labels flat (no tooltip-within-tooltip). Use the original "all circles then all labels" structure.
6. **NO legend elements** — everything from line 2644 onward (legend circles, text, thread samples) is omitted. The intro paragraph text serves as legend.
7. **Keep:** floor line, all threads, all buttons, all labels, TQC arrow, both caption lines.

### Filter rename checklist:

In the tooltip SVG, find and replace:
- `id="dbtn-sh"` → `id="dbtn-sh-tt"` (1 occurrence, in `<filter>` definition)
- `url(#dbtn-sh)` → `url(#dbtn-sh-tt)` (11 occurrences, one per circle)

### YAML formatting:

The hover-definitions.yaml uses `html: |` (literal block scalar). The entire HTML content (intro `<p>` + `<svg>...</svg>`) goes indented under `html: |`. Line breaks within the SVG are fine in YAML literal blocks. Double quotes in SVG attributes are fine — no escaping needed in literal blocks.

The existing entry is one very long line (line 239). The replacement can use multiple indented lines for readability.

---

## Acceptance Tests

1. **Per-button hovers work:** Hover Topo → tooltip shows "Topology — the mathematics of shape..."
2. **All 11 buttons wrapped:** 11 `<g data-hover=` elements in the inline domain diagram
3. **Cursor pointer:** All domain buttons show pointer cursor on hover
4. **Tooltip text accurate:** Each description matches table above (spot-check 3: Topo, TQC, Mat)
5. **`buttons-and-threads` tooltip updated:** No "NN", no "Neuro", no `M 248,18` (lever) in hover-data JSON
6. **Filter ID separation:** Inline SVG has `dbtn-sh`, tooltip has `dbtn-sh-tt`
7. **Tooltip SVG correct:** Same 11 domain positions and thread network as inline diagram
8. **No legend in tooltip:** Tooltip SVG has no `Topological` or `Nonlinear` legend text
9. **Mobile touch:** Tapping a domain button on phone shows tooltip (tested via touch delegation)
10. **Build succeeds:** `make html` exits 0
11. **Filmstrip unaffected:** 6-panel filmstrip still renders
12. **Other hovers unaffected:** Hover on "five scientific disciplines" still works

## Handoff Prompt

```
You are the Generator for Plan 0222d (domain hover tooltips).

Read: ~/software/relinquishment/plans/0222d-domain-hover-tooltips.md

Two changes to two files:

PHASE 1 — `build/preprocess.py`, function `inject_domain_buttons()`:
Replace the separate "buttons" block (11 circles, lines 2616-2626) and
"button labels" block (11 texts, lines 2628-2638) with 11 <g> groups.
Each <g> wraps one circle + its label and has data-hover="..." with the
domain description from the plan table. Add style="cursor:pointer" to
each <g>. Use \u2014 for em dashes and \u2019 for apostrophes. Keep
draw order: all <g> groups after the thread lines. The TQC arrow,
captions, and legend stay outside any <g>.

PHASE 2 — `build/hover-definitions.yaml`, the `buttons-and-threads`
entry (line 237-239): Replace the html value. New intro <p> per plan.
New SVG: copy the diagram from Phase 1 but (a) width=380 height=280,
(b) viewBox="0 0 500 390", (c) remove <title>, (d) rename filter
dbtn-sh → dbtn-sh-tt in definition AND all 11 url() references,
(e) NO <g data-hover> wrappers (flat circles+labels), (f) no legend
elements. Keep floor, threads, buttons, labels, arrow, captions.

After: `make dev`, commit as "Plan 0222d: per-button domain tooltips +
tooltip sync", push. Report completion ≤5 lines with deviations.
```
