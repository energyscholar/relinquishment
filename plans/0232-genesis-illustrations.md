# Plan 0232 — Genesis Chapter Illustrations

**Status:** DRAFT — for Bruce review and refinement
**Author:** Auditor (Argus S60)
**Chapter:** Genesis: The Edge of Chaos (1988–1992)
**Scope:** 4 new inline SVGs for the book's foundational science chapter

---

## Why Genesis

Genesis is the concept-dense chapter where Jane (p1, 8th grade) and Rachel (p2, 12th grade) encounter autocatalytic sets, phase transitions, edge of chaos, and the canopy metaphor for the first time. It already has strong illustration coverage — the 6-panel filmstrip and the domain buttons map. But three concepts are currently text-only with no visual support, and one has a literal TODO in the source.

**Existing inline illustrations in Genesis:**
- Filmstrip (SVG-008 through SVG-013) — 6 panels after "connected web"
- Domain buttons (SVG-014) — after "five published research streams"

**Existing hover-only (popup, not inline):**
- Buttons network (SVG-007) — on "buttons" term
- Phase transition curve (SVG-019) — on "phase transition" term
- Edge of chaos zones (SVG-020) — on "edge of chaos" term

## The Principle: High-Quality Use of Images

Not "more images" — images that do work the text can't.

Each proposed SVG passes three tests:
1. **Does the text need it?** Would Jane get stuck here without a visual?
2. **Is it load-bearing?** Does removing it weaken comprehension?
3. **Does it echo?** Does it connect to something the reader already saw?

Images that merely decorate are worse than no images — they teach the reader to skip illustrations.

## Reader Journey Through Genesis

The chapter builds an argument in five steps. Here's where the visual gaps are:

```
§1 Life Is Expected
    TEXT: "life is a phase transition, not an accident"
    VISUAL SUPPORT: none (OK — the claim is set up, not yet explained)

§2 Buttons and Threads
    TEXT: scatter → tie → net → snap → autocatalytic sets
    VISUAL: ✅ 6-panel filmstrip (physical metaphor)
    GAP: The chemistry version (A→B→C→A) is described in one
         sentence but never shown. Jane reads "catalytic reactions"
         and has nothing to anchor it to. The filmstrip showed
         BUTTONS — now show MOLECULES doing the same thing.
         → SVG-025 autocatalytic-loop

§3 The Edge of Chaos
    TEXT: frozen vs. chaotic vs. edge
    VISUAL: hover-only (SVG-020, popup)
    GAP: TODO comment already in source (line 46-49).
         The hover SVG fires only if the reader hovers on the
         exact term. The concept is too central to be popup-only.
         → SVG-026 edge-of-chaos-inline

§4 From Chemistry to Computation
    TEXT: "the same principle applies to any substrate"
    VISUAL: none
    GAP: This is the chapter's key intellectual move. Jane needs
         to SEE that the same math governs molecules in a beaker
         AND quasiparticles in a 2DEG. Side-by-side comparison
         is the natural visual form.
         → SVG-027 substrate-parallel

§5 The Canopy Problem
    TEXT: "A forest canopy owns the light"
    VISUAL: none
    GAP: The darkest implication in the chapter. A seedling dies
         not because it's attacked but because the canopy already
         claimed the light. The metaphor is vivid in text but a
         simple cross-section makes it visceral.
         → SVG-028 canopy-problem
```

## The Four SVGs

### SVG-025: Autocatalytic Loop
**Placement:** After "The whole network sustains itself."
**What it shows:** Three molecules (A, B, C) arranged in a circle with curved arrows. A catalyzes B → B catalyzes C → C catalyzes A. Self-sustaining loop.
**Visual language:** Warm organic colors (amber/brown), simple circular layout. Echoes the filmstrip's buttons-and-threads aesthetic — same concept, different substrate.
**Jane test:** "Oh — the buttons with threads was THIS. Molecules helping each other exist."
**Rachel test:** "Autocatalytic closure — the network property that makes it self-sustaining."
**Difficulty:** Low. Clean geometry.

### SVG-026: Edge of Chaos (Inline)
**Placement:** After "best able to evolve as well." (Kauffman quote, line 51)
**What it shows:** Three visual regimes side by side:
- LEFT: frozen crystal lattice (rigid blue grid, nothing moves)
- CENTER: narrow green band with interconnected but flexible nodes (life, computation)
- RIGHT: chaotic scatter (red dots flying apart, no structure)
**Visual language:** Extends existing SVG-020 hover design but with concrete substrate visuals instead of abstract labels. The green band is narrow — emphasizes that the sweet spot is small.
**Jane test:** "Too stiff, too wild, juuust right. Like Goldilocks."
**Rachel test:** "The three regimes map to actual dynamical states. The edge is a phase boundary."
**Difficulty:** Medium. Based on existing SVG-020 but richer.

### SVG-027: Substrate Parallel
**Placement:** After "the threshold was crossed."
**What it shows:** Split panel. Left: warm-colored beaker with organic molecules and catalytic arrows between them (echoes SVG-025's loop). Right: blue-colored 2DEG substrate with anyonic quasiparticles and braiding arcs (echoes SVG-017 TQNN). Center bridge: "same mathematics" with a threshold line.
**Visual language:** Warm left, cool right, shared structure in the middle. The visual argument: different stuff, same math, same result.
**Jane test:** "Wait — the molecule thing and the computer chip thing are doing the SAME THING?"
**Rachel test:** "Kauffman's threshold applies substrate-independently. The 2DEG is just another beaker."
**Difficulty:** Highest. Two visual systems unified. Must be clear without being reductive.

### SVG-028: Canopy Problem
**Placement:** After "the ecological niche is full."
**What it shows:** Cross-section of a forest. Two or three tall trees with full green crowns at top, catching all the sunlight (yellow rays from above). Below: a tiny seedling in deep shadow. The seedling is reaching upward. No light reaches it.
**Visual language:** Simple, almost children's-book illustration quality. The darkness below is the point. No labels needed — the image is the argument.
**Jane test:** "The little tree can't grow because the big trees got there first."
**Rachel test:** "First-mover advantage. The niche is occupied. This applies to any substrate."
**Difficulty:** Low-medium. Organic shapes (trees) are harder than geometric, but the composition is simple.

## Sequencing and Reading Flow

The 4 new SVGs + 2 existing sequences create this visual rhythm through Genesis:

```
§2  Filmstrip (6 panels)     — buttons scatter → snap     [PHYSICAL]
§2  Autocatalytic loop        — A → B → C → A              [CHEMICAL]
§3  Edge of chaos             — frozen | edge | chaotic     [REGIME]
§4  Substrate parallel        — beaker ↔ 2DEG               [BRIDGE]
§4  Domain buttons            — 11 fields, 5 clusters       [CONVERGENCE]
§5  Canopy                    — trees block seedling         [CONSEQUENCE]
```

The filmstrip is physical. The loop translates to chemistry. The edge of chaos defines the operating regime. The substrate parallel makes the leap. The domain buttons show who got close. The canopy shows what it means.

Each image echoes the one before. That's high-quality use of images.

## Annealing Log

**High temperature (all candidates considered):**
1. Autocatalytic loop ✓
2. Edge of chaos inline ✓
3. Substrate parallel ✓
4. Canopy problem ✓
5. "Life is expected" vs "life is an accident" comparison — KILLED: too abstract, duplicates text
6. DARPA proposal timeline (1988-1992) — KILLED: domain buttons already show convergence; timeline is text information
7. Great Filter visual — KILLED: not in Genesis chapter; belongs in final chapter if anywhere

**Medium temperature (testing load-bearing):**
- All 4 survivors pass the "remove it and comprehension drops" test
- SVG-027 (substrate parallel) is the riskiest — if poorly executed, it oversimplifies. But if well executed, it's the single most valuable illustration in the chapter because it carries the thesis
- SVG-026 could just deploy existing SVG-020 inline. Decision: enhance it. The hover version is designed for a 300px popup; the inline version should be richer with concrete regime examples. A deployment-only task would be cheaper but miss the opportunity.

**Low temperature (placement precision):**
- SVG-025 marker verified: "The whole network sustains itself." appears once in genesis.tex line 36
- SVG-026 marker verified: "best able to evolve as well." appears in Kauffman quote, line 51 region
- SVG-027 marker verified: "the threshold was crossed." appears once in line 62
- SVG-028 marker verified: "the ecological niche is full." appears once in line 75
- No marker collisions. All unique in the chapter.

## Implementation Notes

- Each SVG gets built in `hover-definitions.yaml` OR as a constant in `preprocess.py`, following the existing patterns
- Inline injection via `preprocess.py` (new `inject_*` functions), following the `inject_flat_diagram` pattern
- Gallery manifest (`build/gallery-manifest.yaml`) already has placeholder entries for all 4
- After building, regenerate gallery (`python3 build/generate-gallery.py`) and open in browser
- Build order: SVG-025 first (simplest, validates the pipeline), then SVG-026, SVG-028, SVG-027 last (hardest)

## Open Questions for Bruce

1. **SVG-025 molecule count:** Three (A→B→C→A) is cleanest. Four or five would be more realistic but noisier. Preference?
2. **SVG-026 concrete examples:** Should the three regimes show abstract patterns (grid, network, scatter) or named substrates (crystal, brain, gas)?
3. **SVG-027 scope:** Full split-panel, or simpler "same loop, different color" approach?
4. **SVG-028 tone:** Children's-book simple, or more diagrammatic? The text is dark; should the image be gentle or stark?
