# Subtask: SVG-056 — "The Fork" Consequence Horizon Diagram

**Output:** Create inline SVG in `build/images/scientific-revolutions-chapter.html`
(inside Section 4 "Life in the Flat," between the "Both branches" paragraph and
the SVG-055 Expert Consensus Spectrum)
**Commit:** `Plan 0321: SVG-056 — A1/A2 consequence fork diagram`
**Read first:** The chapter HTML (especially lines 305–311), this spec.

## What This Image Does

Shows the reader the *distance* between A1 and A2 — not where we are on the
spectrum (SVG-055 does that), but where each path *leads*. The visual argument
is geometric: A1 terminates in a single calm endpoint; A2 branches into a
cascade of implications that connect forward to later chapters.

The asymmetry in the diagram's shape IS the argument. The reader sees the
distance without anyone stating it.

## Why This Image Is Needed

The chapter text describes A1 and A2 in parallel paragraphs. The spectrum
shows where we sit in 2026. Neither visualizes the *consequence gap* —
the paradox that identical evidence produces wildly divergent futures
depending on a single untested question. This diagram fills that gap.

## Layout

```
             ┌─────────────────────────────────────────┐
             │  Three research programs:                │
             │  ● Autocatalytic set theory (Kauffman)   │
             │  ● Fractional quantum Hall anyons        │
             │  ● Topological quantum computation       │
             │                                          │
             │  No published work at their intersection.│
             └────────────────┬────────────────────────┘
                              │
                    Does autocatalytic closure
                    occur in FQHE substrates?
                              │
               ┌──────────────┴──────────────┐
               │                             │
            ┌──┴──┐                    ┌─────┴─────┐
            │ A1  │                    │    A2     │
            └──┬──┘                    └─────┬─────┘
               │                             │
        ┌──────┘                    ┌────────┼────────┐
        │                           │        │        │
   Five productive             Biology's  New search  Circle of
   fields advance.             definition targets    moral
   Good science                shifts        │      consideration
   continues.                      │    Planetary       │
                               "Can It  magneto-    "Why
                                Think?" spheres    Relinquish?"
```

The LEFT branch (A1) is a single box that terminates — calm, complete,
explicitly positive. "Good science continues" is not a consolation prize.
The RIGHT branch (A2) fans into three implication boxes, each connecting
forward via deep links to later chapters. The visual asymmetry reflects
consequence asymmetry, not probability.

## Visual Design

- **Background:** Dark, matching chapter (#1a1a2e). No separate panel —
  sits flush in the text flow with padding above and below.
- **Top box (shared evidence):** Rounded rect, subtle border
  (rgba(200,184,152,0.2)), muted fill (#1e1e35). Lists three research
  programs as bullets, then a visual separator (thin line or spacing),
  then "No published work at their intersection" in italic — making
  the gap visible within the diagram itself. 10px muted text. The box
  represents the SAME evidence both branches interpret.
- **Fork question:** Centered below the shared box, in italic Georgia,
  11px, gold (#d4a017). This is the hinge — the one question that
  separates the two futures. Text: "Does autocatalytic closure occur in
  FQHE substrates?"
- **Vertical line + split:** A single line descends from the shared box,
  splits into two branches via a Y-junction.
- **A1 box (left):** Small rounded rect, muted green border (#5c7c5c),
  labeled "A1" in small-caps at top. Interior text: "Five productive
  fields advance. Good science continues." One box, no children.
  Calm. Terminal. MUST feel complete and satisfactory — not truncated,
  not a consolation prize. The green border conveys "this is a fine
  outcome." Fill slightly darker than background (#161630).
- **A2 box (right):** Same size as A1, gold border (#d4a017), labeled
  "A2." Interior text: "A new paradigm." Below it, THREE child boxes
  descend via branching lines:
  1. **"Biology's definition shifts"** — connects to "Can It Think?" (deep link)
  2. **"New search targets"** — "Planetary magnetospheres, interstellar
     2DEGs" in 9px muted text
  3. **"Moral consideration"** — connects to "Why Relinquish?" (deep link)
- **Child boxes:** Smaller rounded rects. Same dark fill, thin border
  matching parent gold at reduced opacity. 10px Georgia text.
- **Deep link indicators:** The two boxes that connect to later chapters
  ("Can It Think?" and "Why Relinquish?") have a small arrow or
  chevron (→) and the chapter title in the deep-link color (#8a9a8a),
  italic, 9px.
- **Lines:** 1px, rgba(200,184,152,0.3). The A1 branch gets a single
  line. The A2 branch gets three lines fanning out. The visual weight
  disparity reinforces the asymmetry.
- **Caption below:** *"Same evidence. Same silence. Different futures."*
  Italic, 11px, muted (#908878), centered.

## Sizing

ViewBox: `0 0 700 340` — narrower than the spectrum (700 vs 900) because
this is a tree, not a timeline. Tall enough for three levels of boxes.
Fits comfortably in the 800px text column.

## Placement

Insert between the existing paragraph:
```
<p>Both branches are scientifically productive. A1 still advances five
fields. A2 opens a sixth. Neither is a consolation prize.</p>
```
and the existing SVG-055 `<details>` block.

No accordion wrapper needed — this is a compact static diagram that
should always be visible. It's the intellectual hinge of the section.

## Static — No Animation

This diagram is static. The geometry communicates instantly. Animation
would add nothing — the contrast between the single A1 endpoint and
the branching A2 tree is legible at a glance. The chapter already has
two animated elements (SVG-054 and SVG-055); a third would be fatiguing.

## Interaction

None. Purely visual. The deep link text in the child boxes is styled
but not clickable in this standalone preview — the book build system's
deep-link injection handles hyperlinking at build time.

## Constraint #7 Compliance

The diagram does NOT label A2 as "correct" or "more likely." Both
branches descend from the same shared evidence box with equal visual
weight at the fork point. A1 is labeled positively — "Five productive
fields advance. Good science continues." Not dismissive. A2 is labeled
"A new paradigm" — accurate if A2 obtains. The asymmetry in branching
reflects asymmetry in *consequences*, not in *probability*. The fork
question uses "Does...?" not "When..." — keeping it genuinely open.

## Crop Resistance

The fork structure must be visually integral — removing either branch
should look obviously incomplete. The Y-junction and shared evidence
box at top bind the two branches into a single unit. An adversary
who screenshots only the A2 branch should get a visually broken image
(junction line dangling, shared box truncated). Design the layout so
the fork is central, not separable.

## Do NOT

- Animate anything (static SVG)
- Make A2 visually "better" than A1 (larger, brighter, more prominent)
- State or imply which branch is more likely
- Add interactivity
- Change any chapter text
- Use external libraries or fonts beyond Georgia

## Report

Confirm: diagram renders correctly, A1/A2 branches visually balanced
at fork point, consequence asymmetry visible in branching structure,
deep link text present, caption visible. Open in browser and verify.
