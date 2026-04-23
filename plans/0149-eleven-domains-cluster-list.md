# Plan 0149: Eleven Domains Cluster List

**Status:** DONE (implemented prior to 2026-04-10; confirmed by Generator B)

## Context

The book repeatedly references "five fields" or "five scientific disciplines" — the shorthand for the interdisciplinary convergence at the book's core. But the actual scope is 11 domains organized in 5 clusters. Bruce wants:
1. An inline passage in the Silence Gap chapter revealing the full 11 domains
2. A hovertip on "five fields" references showing the cluster structure at p2/p3

The 11 domains in 5 clusters:
```
Topological: Topology · Topological field theory · Condensed matter · TQC
Nonlinear:   Solitons · Nonlinear dynamics
Origin:      Autocatalysis · Autopoiesis
Computation: Universality · Parallel computation
Materials:   Materials science
```

## Phase 1: Hover definition

Add to `build/hover-definitions.yaml`:

```yaml
five scientific disciplines: "Five clusters, eleven domains: Topology · Topological field theory · Condensed matter · TQC | Solitons · Nonlinear dynamics | Autocatalysis · Autopoiesis | Universality · Parallel computation | Materials science. The 'five fields' shorthand maps to these clusters — each cluster contains disciplines that talk to each other but rarely cross cluster boundaries."
```

This single definition covers both "five scientific disciplines" and "five scientific fields" — the hovertip macro matches on the marked phrase.

## Phase 2: Silence Gap inline passage

In `manuscript/spine/the-silence-gap.tex`, insert a new passage between the end of field #5 (line 28, after the computational universality paragraph) and the `\section*{The Gap}` heading (line 30).

Insert:

```latex
\bigskip

\deeplink{eleven-domains}These five descriptions are shorthand. Each ``field'' is actually a cluster of disciplines. Solid-state physics alone spans condensed matter, topological field theory, and topological quantum computation --- three communities with different journals, different conferences, and different vocabularies. Complexity science spans autocatalytic sets and autopoietic theory. Nonlinear dynamics includes soliton physics. Add materials science --- the engineering discipline that builds the substrates --- and the five fields become eleven domains in five clusters.

The question is not whether any one of these domains has interesting results. Each does. The question is whether anyone has stood at the intersection of all eleven and asked what the combined picture looks like.
```

This is p2 level — accessible but precise. The `\deeplink{eleven-domains}` makes it shareable.

## Phase 3: Apply hovertips to build-path references

Add `\hovertip{}` wrapping to "five scientific disciplines" / "five scientific fields" / "five fields" in build-path files. Only wrap the FIRST or most prominent occurrence per file (avoid tooltip fatigue).

Target files and lines:

| File | Line | Current text | Wrap as |
|------|------|-------------|---------|
| `spine/the-silence-gap.tex` | 18 | `five scientific disciplines` | `\hovertip{five scientific disciplines}` |
| `spine/the-strongest-objection.tex` | 98 | `five scientific fields` | `\hovertip{five scientific fields}` |
| `record/the-handler.tex` | 92 | `five scientific fields` | `\hovertip{five scientific fields}` |
| `00-front/summary.tex` | 52 | `five fields` | `\hovertip{five fields}` |

**Skip these** (tooltip would be redundant or context doesn't fit):
- `spine/the-silence-gap.tex` line 35 — already has `\deeplink`, and the inline passage just explained it
- `record/the-handler.tex` line 138 — second occurrence in same chapter
- `00-front/how-to-read.tex` line 11 — structural/navigational text, tooltip would clutter
- `appendix/topic-guide.tex` line 69 — index entry, not prose
- `appendix/rlhf-bias.tex` line 64 — quoted prompt text, shouldn't be modified

**Hover definition matching:** The hovertip macro generates hover IDs from the marked phrase. We need THREE entries in `hover-definitions.yaml` since the phrases differ:
- `five scientific disciplines` → main definition
- `five scientific fields` → same text (or alias)
- `five fields` → same text (or alias)

Check if hover-definitions.yaml supports aliasing. If not, duplicate the definition text for all three keys.

## Phase 4: Build and verify

1. `make html` — no errors
2. Hover over "five scientific disciplines" in Silence Gap → tooltip shows 11 domains
3. Hover over "five scientific fields" in Strongest Objection → same tooltip
4. The eleven-domains passage appears between field #5 and "The Gap" section
5. Deep link `#dl:eleven-domains` scrolls to the passage
6. Push to website

## NOT in this plan

- Changing "five" to "eleven" in existing prose (the five-cluster shorthand is deliberate and correct)
- DN 11-domain → 5-cluster mapping discussion (separate concern, DN spec territory)
- Modifying non-build-path files (interlude/, convergence/, track-1-confession/)

## Verification

- [ ] Hover definition present for all three phrase variants
- [ ] Silence Gap has 11-domains passage with `\deeplink{eleven-domains}`
- [ ] 4 build-path files have hovertips on "five fields" variants
- [ ] `make html` clean
- [ ] Tooltips render correctly on hover
- [ ] Deep link `#dl:eleven-domains` works
