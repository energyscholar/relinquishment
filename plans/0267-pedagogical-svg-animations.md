# Plan 0267 — Pedagogical SVG Animations

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR (after Bruce approval)
**Parent:** Plan 0251 (SVG Content Improvement)
**Sibling:** Plan 0266 (cover magnetosphere animation — DONE, ca6f46a)
**Annealing:** HIGH LOW LOW (3 passes)

---

## Problem

Five inline chapter SVGs are static diagrams that show STRUCTURE. Four
of them teach concepts whose essence is PROCESS — self-sustaining
cycles, dynamic stability, dimensional confinement, and epistemic
status. Static images cannot show process. Animated images can. The
difference is pedagogical, not decorative.

For a GA reader who may never have encountered autocatalysis or
edge-of-chaos dynamics, the animation IS the explanation. Show first,
tell second. A million-viewer audience needs visual teaching that works
on first encounter without specialized vocabulary.

---

## The Five Animations

### 1. Autocatalytic Loop — "the cycle runs"

**File:** `build/preprocess.py`, inside `inject_genesis_illustrations()`
**SVG:** `fig-autocatalytic-loop` (300×200, Genesis chapter)
**Concept:** Self-sustaining catalytic network

**Animation:** Three small dots (r=3, fill=#d4a017, brighter than the
arrow color #8b6914) travel along the three arrow paths, cycling
continuously. Each dot follows one arrow: A→B, B→C, C→A. Staggered
by 1/3 of the period so a dot is always in transit on every arrow.

**Technical:** `<animateMotion>` with inline `path` attribute on each
dot circle. The path data matches the existing arrow `<path d="...">`.

| Dot | Path (existing arrow) | Dur | Begin |
|-----|----------------------|-----|-------|
| A→B | `M 170,46 Q 210,55 210,106` | 2.4s | 0s |
| B→C | `M 196,142 Q 150,170 100,142` | 2.4s | 0.8s |
| C→A | `M 72,110 Q 60,70 135,42` | 2.4s | 1.6s |

Each dot fades at its destination (opacity 0.8→0 over last 15% of
path) and appears fresh at its origin. This creates a visual "consumed
and produced" cycle that maps to catalysis.

**Implementation per dot:**
```xml
<circle r="3" fill="#d4a017" opacity="0">
  <animateMotion dur="2.4s" repeatCount="indefinite" begin="0s"
    path="M 170,46 Q 210,55 210,106"/>
  <animate attributeName="opacity"
    values="0;0.85;0.85;0.85;0" keyTimes="0;0.1;0.7;0.85;1"
    dur="2.4s" repeatCount="indefinite" begin="0s"/>
</circle>
```

**Bytes:** ~450 (3 dots × ~150 each)

**What the reader learns:** The network doesn't just connect — it
*runs*. The cycle is continuous. Stop any one reaction and the whole
system dies. This is why "self-sustaining" matters.

---

### 2. Substrate Parallel — "same process, different medium"

**File:** `build/preprocess.py`, inside `inject_genesis_illustrations()`
**SVG:** `fig-substrate-parallel` (420×200, Genesis chapter)
**Concept:** Chemistry and quantum braiding = same mathematics

**Animation:** Mirror of Animation 1. Three cycling dots in EACH half
of the split panel. Left (warm): #d4a017 dots on warm arrow paths.
Right (cool): #5dade2 dots on cool arrow paths. SAME timing, SAME
stagger, different colors. The reader sees the same cycling process
in two different substrates simultaneously.

**Warm-side paths (existing arrows):**

| Dot | Path | Dur | Begin |
|-----|------|-----|-------|
| A→B | `M 104,60 Q 120,70 122,95` | 2.4s | 0s |
| B→C | `M 116,112 Q 95,125 75,112` | 2.4s | 0.8s |
| C→A | `M 60,96 Q 55,75 88,58` | 2.4s | 1.6s |

**Cool-side paths (existing arrows):**

| Dot | Path | Dur | Begin |
|-----|------|-----|-------|
| a→b | `M 314,95 Q 340,85 350,93` | 2.4s | 0s |
| b→c | `M 349,109 Q 345,125 337,130` | 2.4s | 0.8s |
| c→a | `M 322,138 Q 305,125 302,112` | 2.4s | 1.6s |

**Implementation:** Same pattern as Animation 1. Cool dots use
fill=#5dade2. Duration and keyTimes IDENTICAL to warm dots.

**Bytes:** ~900 (6 dots × ~150 each)

**What the reader learns:** The bridge text says "same mathematics."
The animation PROVES it — identical motion pattern, different substrate
colors. This is the core argument of the Genesis chapter made visual.

**Critical constraint:** Timing MUST match Animation 1 exactly (2.4s
period, 0/0.8/1.6 stagger). When the reader scrolls from the
autocatalytic loop to the substrate parallel, the same rhythm appears
in a new context. Recognition reinforces understanding.

---

### 3. Edge of Chaos — "frozen, alive, flying apart"

**File:** `build/preprocess.py`, inside `inject_genesis_illustrations()`
**SVG:** `fig-edge-of-chaos` (400×160, Genesis chapter)
**Concept:** The narrow regime where computation and life are possible

**Animation:** Three contrasting behaviors across three panels. The
contrast IS the lesson.

**Frozen panel (left, blue):** NO ANIMATION. The grid is rigid. The
complete absence of motion in the frozen panel is pedagogically
essential — it IS the concept of frozen order. Do NOT animate this.

**Edge panel (center, green):** Two animation types:
1. **Connection flow:** 4 of the 7 connection paths get
   `stroke-dasharray="3,4"` + animated `stroke-dashoffset` (values
   "0;-7", dur 2s). Shows active information flow through the network.
   The connections are alive — data is moving through them.
2. **Node breathing:** 4 of the 7 green nodes get subtle opacity
   oscillation (e.g., 0.9→0.6→0.9 over 3-5s, staggered). The nodes
   are active, processing, responding.

| Element | Animation | Values | Dur | Begin |
|---------|-----------|--------|-----|-------|
| Path 1 (160,38→172,58) | stroke-dashoffset | 0;-7 | 2.0s | 0s |
| Path 3 (172,58→188,72) | stroke-dashoffset | 0;-7 | 2.0s | 0.5s |
| Path 5 (188,72→200,92) | stroke-dashoffset | 0;-7 | 2.0s | 1.0s |
| Path 7 (195,42→200,92) | stroke-dashoffset | 0;-7 | 2.0s | 1.5s |
| Node cx=160 | opacity | 1;0.6;1 | 4.0s | 0s |
| Node cx=188 | opacity | 1;0.6;1 | 4.5s | 1.0s |
| Node cx=175 | opacity | 1;0.6;1 | 5.0s | 2.0s |
| Node cx=200 | opacity | 1;0.6;1 | 3.5s | 0.5s |

**Chaos panel (right, red):** Dots drift randomly apart.
`<animateTransform type="translate">` on 5 of 9 dots. Small random
displacements, long periods, different directions. Slow enough to be
subliminal — the reader senses disorder without tracking individual
dots.

| Dot (cx,cy) | translate values | Dur |
|------------|-----------------|-----|
| (258,30) | 0,0; 4,-3; -2,5; 3,-1; 0,0 | 7s |
| (335,42) | 0,0; -3,4; 5,-2; -1,3; 0,0 | 8s |
| (270,55) | 0,0; 2,-4; -4,2; 1,-3; 0,0 | 9s |
| (320,65) | 0,0; -5,1; 3,-3; -2,4; 0,0 | 7.5s |
| (295,85) | 0,0; 3,3; -2,-4; 4,-1; 0,0 | 8.5s |

**Bytes:** ~1,400 (edge connections ~400, edge nodes ~320, chaos ~500,
style block ~80, whitespace/overhead ~100)

**What the reader learns:** The frozen panel is dead. The chaos panel
is lost. The edge panel is the only one where anything purposeful
happens. This three-way contrast is the single most powerful visual
teaching moment in the book. No amount of text can match the visceral
experience of seeing three regimes behave differently in real time.

---

### 4. Flat Cross-Section — "confined but moving"

**File:** `build/preprocess.py`, inside `inject_flat_diagram()`
**SVG:** `fig-flat-cross-section` (300×130, The Flat chapter)
**Concept:** Electrons confined to two dimensions

**Animation:** 6 of the 9 electron dots drift horizontally within the
2DEG layer. Animate `cx` attribute — NEVER `cy`. The electrons move
left and right but NEVER up and down. The animation embodies
dimensional confinement.

| Electron (cx) | cx values | Dur | Begin |
|--------------|-----------|-----|-------|
| 70 | 70;78;62;70 | 4.5s | 0s |
| 100 | 100;92;108;100 | 5.2s | 0.8s |
| 135 | 135;142;128;135 | 4.0s | 1.5s |
| 165 | 165;158;172;165 | 4.8s | 0.3s |
| 195 | 195;203;187;195 | 5.5s | 2.0s |
| 225 | 225;218;232;225 | 4.3s | 1.2s |

cx ranges: ±8 from center. All stay within the 2DEG layer bounds
(x=30 to x=270). Three smaller background electrons (r=2) remain
static for depth.

**Bytes:** ~600 (6 electrons × ~100 each)

**What the reader learns:** Electrons in the Flat are free to move
within their plane — but they cannot escape it. The horizontal drift
with zero vertical motion is the concept of 2D confinement made
visceral. The reader's eye follows the electrons left and right and
unconsciously registers that they never go up or down.

---

### 5. Domain Network Dashed Bridges — "not yet built"

**File:** `build/preprocess.py`, inside `inject_domain_buttons()`
**SVG:** `fig-domain-buttons` (460×440, Genesis chapter)
**Concept:** Published connections vs. speculative bridges

**Animation:** The 5 dashed lines (cross-cluster bridges + hanging
bridges) pulse in opacity. Solid published threads remain constant.
The visual contract: solid = established fact, pulsing = "this
connection exists in theory but no one has published the proof."

**Dashed elements to animate:**

| Element | Type | Current opacity | Values | Dur |
|---------|------|----------------|--------|-----|
| CE↔NLD bridge | line | 0.35 | 0.20;0.50;0.20 | 3.5s |
| CE↔ACS bridge | line | 0.35 | 0.20;0.50;0.20 | 4.0s |
| Par↔Auto bridge | line | 0.35 | 0.20;0.50;0.20 | 3.8s |
| Mat↔NLD bridge | line | 0.35 | 0.20;0.50;0.20 | 4.2s |
| CE→Topo hanging | path | 0.4 | 0.25;0.55;0.25 | 4.5s |
| ACS→TQC hanging | path | 0.4 | 0.25;0.55;0.25 | 5.0s |

Staggered begin times (0, 0.5, 1.0, 1.5, 2.0, 2.5s) prevent
synchronized pulsing.

The NLD↔ACS solid cross-cluster thread and all intra-cluster solid
threads: NO ANIMATION. The solidity IS the point.

**Bytes:** ~540 (6 elements × ~90 each)

**What the reader learns:** The reader's eye naturally distinguishes
the static (published) connections from the pulsing (speculative) ones.
The argument's structure becomes visual: "most of this is established
science — but this part, and this part, are the speculation." The
reader can literally see where the solid ground ends and the bridge
begins.

---

## Accessibility

Each animated SVG gets a `<style>` block inside `<defs>`:

```xml
<style>
@media (prefers-reduced-motion: reduce) {
  animate, animateMotion, animateTransform { display: none; }
}
</style>
```

~85 bytes per SVG. When reduced motion is preferred, all SMIL elements
are hidden and the SVG renders identically to the current static
version. Zero JavaScript dependency — works in any browser that
supports the media query.

Total accessibility overhead: ~425 bytes (5 SVGs × 85).

---

## Text Compression Opportunities

Animations don't just illustrate — they teach. When a diagram teaches
a concept visually, nearby explanatory text may become partially
redundant. These are OPPORTUNITIES, not mandates. Bruce and Gen decide
what to cut.

### Autocatalytic loop area

**Current figcaption (16 words):** "An autocatalytic loop: each
molecule catalyzes the next. The network sustains itself."

**With animation (3 words):** "An autocatalytic loop."

The cycling dots show "each molecule catalyzes the next" and "sustains
itself." The caption becomes a label.

### Edge of chaos area

**Current figcaption (19 words):** "The edge of chaos: a narrow regime
between frozen order and formless chaos where complex systems can
compute."

**With animation (3 words):** "Frozen. Edge. Chaos." — or removed
entirely.

The animated contrast across three panels shows what the caption
explains. The panel labels ("frozen", "edge", "chaos") are already in
the SVG.

**Body text opportunity (genesis.tex line 44):** "But not all
self-sustaining systems are interesting. A frozen crystal sustains
itself. So does a fire. One is too ordered to compute; the other, too
chaotic to remember." (~30 words)

With the animated diagram, these sentences set up what the animation
already shows. Could be cut or compressed to: "Not all self-sustaining
systems compute." (~6 words). The diagram carries the rest. But this
is Bruce's prose — his call.

### Substrate parallel area

**Current figcaption (22 words):** "Different substrates, same
mathematics: catalytic chemistry (left) and quantum braiding (right)
share the same self-sustaining loop structure."

**With animation (4 words):** "Different substrates. Same mathematics."

The mirror animation proves the claim. Left/right labels are in the
SVG. "Self-sustaining loop structure" is shown by the cycling dots.

### Flat cross-section area

**Current figcaption (14 words):** "The Flat: a two-dimensional
electron gas sandwiched between bulk semiconductor layers."

**With animation:** No change recommended. The caption names the
technical term (2DEG) which the animation can't convey. Keep as-is.

**SVG subtitle text:** "electrons confined to two dimensions" — the
animation embodies this, so the text becomes a label confirming what
the eye already sees. Could be shortened to "confined to two
dimensions" but savings are trivial.

### Total text savings

~60 words from figcaptions + up to ~25 words from genesis.tex body
text = **~85 words.** Not "a lot" in absolute terms. But the
pedagogical lift is enormous: the remaining text is freed from
explanatory duty and can focus on implications, connections, and voice.

**The bigger payoff is FUTURE text.** Once these animations are live,
new content can reference concepts more briefly. "Remember the cycling
dots" or "like the edge-of-chaos diagram" becomes a visual shorthand
that replaces paragraphs of re-explanation. The animations create a
visual vocabulary the reader carries forward.

---

## Phasing

### Phase 1: Genesis Trio

**Scope:** Animations 1 (autocatalytic loop), 2 (substrate parallel),
3 (edge of chaos). All in `inject_genesis_illustrations()`.

**Why grouped:** Same function, same chapter, and Animations 1+2 share
timing (2.4s cycle, must match). Animation 3 is independent but
adjacent in the reading flow.

**Order within phase:** Build Animation 1 first. Copy its timing to
Animation 2's warm side, then build the cool side. Build Animation 3
last (most complex).

**Byte budget:** ~2,750 bytes + ~255 bytes (3 × 85 accessibility)
= ~3,005 bytes

**Acceptance criteria:**
- [ ] 3 cycling dots on autocatalytic loop, staggered, fade at destination
- [ ] 6 mirror dots on substrate parallel (3 warm, 3 cool), same timing as #1
- [ ] Edge of chaos: frozen=static, edge=flowing connections + breathing nodes, chaos=drifting dots
- [ ] All three have `<style>` block for prefers-reduced-motion
- [ ] `make dev` clean
- [ ] Visual inspection in browser (check timing, contrast, subtlety)

### Phase 2: Flat Cross-Section

**Scope:** Animation 4. In `inject_flat_diagram()`.

**Byte budget:** ~600 + 85 = ~685 bytes

**Acceptance criteria:**
- [ ] 6 electrons drift horizontally only (animate cx, NEVER cy)
- [ ] All cx ranges stay within 2DEG bounds (30–270)
- [ ] 3 background electrons remain static
- [ ] `<style>` block for prefers-reduced-motion
- [ ] `make dev` clean

### Phase 3: Domain Network Bridges

**Scope:** Animation 5. In `inject_domain_buttons()`.

**Byte budget:** ~540 + 85 = ~625 bytes

**Acceptance criteria:**
- [ ] 6 dashed elements pulse in opacity (staggered)
- [ ] All solid threads remain completely static
- [ ] Interactive hover tooltips still work (no interference)
- [ ] `<style>` block for prefers-reduced-motion
- [ ] `make dev` clean

---

## Total Budget

| Component | Bytes |
|-----------|-------|
| Animation 1 (autocatalytic) | ~450 |
| Animation 2 (substrate parallel) | ~900 |
| Animation 3 (edge of chaos) | ~1,400 |
| Animation 4 (flat electrons) | ~600 |
| Animation 5 (domain bridges) | ~540 |
| Accessibility (5 × 85) | ~425 |
| **Total** | **~4,315** |

Comparable to Plan 0266's +4,180 bytes. Combined: ~8.5 KB of animation
across the entire book.

---

## What NOT to Animate

- **Filmstrip panels:** Sequential layout IS the animation
- **Canopy problem:** Static composition already tells the story
- **Earth in cover magnetosphere:** Ground truth stays grounded
- **Solid threads in domain network:** Solidity IS the point
- **Frozen panel in edge of chaos:** Stasis IS the point
- **Any text, caption, or label**
- **Grid-sequence SVGs** (epub-only, not in HTML)

---

## Quality Standard

Bruce: "Expect millions of viewers someday." These animations must:

1. **Teach on first encounter** — no instructions needed
2. **Work at any viewport width** — 320px phone to 4K display
3. **Degrade gracefully** — reduced-motion users get the current
   (excellent) static diagrams
4. **Be subtle** — the reader should FEEL the concept, not notice
   "oh, there's an animation." The motion serves comprehension, not
   attention-grabbing
5. **Survive print** — PDF/print CSS hides animations. Static diagram
   must stand alone (it already does)
6. **Hold up to scrutiny** — a physics professor should see the
   autocatalytic dots and think "yes, that's how catalytic cycles work,"
   not "that's a cute animation"

---

## Annealing Log (HIGH LOW LOW — 3 passes)

### Pass 1 (HIGH) — Animation design and pedagogical audit

Read all 5 SVGs in full from preprocess.py source. Mapped each
animation to the specific concept it teaches. Key design decisions:

1. **animateMotion for cycling dots (Animations 1+2):** Considered
   animate cx/cy along path manually. Rejected: `<animateMotion>` with
   inline `path` is purpose-built for this, cleaner, and more precise.
   The path data already exists in the arrow elements.

2. **Three contrasting behaviors for edge of chaos (Animation 3):**
   Considered animating all three panels. Rejected: the ABSENCE of
   animation in the frozen panel IS the pedagogical message. Stasis
   teaches stasis. Similarly, the chaos panel's animation must be
   aimless, not rhythmic — Brownian drift, not pulse.

3. **cx-only for flat electrons (Animation 4):** Considered
   animateTransform translate. Rejected: animate `cx` directly is
   cleaner and makes the constraint explicit in the code (there is
   no cy animation because confinement is the point).

4. **Shared timing for Animations 1+2:** The substrate parallel's
   power comes from recognizing the SAME pattern in a different medium.
   If timing differs, the mirror breaks. Locked at 2.4s period,
   0/0.8/1.6 stagger — identical in both SVGs.

5. **Text compression assessed:** Read surrounding text for all 5
   diagrams. Found ~85 words compressible (mainly figcaptions). Body
   text compression is possible (~25 words in genesis.tex) but touches
   Bruce's voice — flagged as opportunity, not directive. The bigger
   payoff is future: animations create visual vocabulary that makes
   future text leaner.

6. **Accessibility approach:** CSS `@media (prefers-reduced-motion)`
   inside each SVG's `<style>` block. No JavaScript dependency. Works
   because SVGs are inline HTML (preprocess.py injects them directly).
   `display:none` on SMIL elements prevents animation computation.
   Tested approach: same technique used in modern SVG animation
   libraries.

### Pass 2 (LOW) — Interaction with existing plans

**Plan 0251 (parent):** These animations enhance 5 existing SVGs from
Plan 0251's manifest. No conflict — Plan 0251's phasing doesn't cover
animation (it covers creation and insertion of NEW SVGs). This plan
operates on EXISTING SVGs.

**Plan 0266 (cover animation):** Different file (reader.js vs.
preprocess.py). Different accessibility approach (JS `motionOk` vs.
CSS media query). No interaction. Consistent style: both use SMIL,
both use `repeatCount="indefinite"`, both respect reduced-motion.

**Plan 0262 (A/B/C compression):** Touches genesis.tex text but not
SVG content. If body text near the diagrams is later compressed
(gen's GP09), the animations remain unaffected — they're in
preprocess.py, not in .tex files.

**Plan 0242 (Genesis visual sprint):** COMPLETE. Created these 4
genesis SVGs. This plan animates them.

### Pass 3 (LOW) — Generator feasibility

All 5 animations are specified with exact SMIL elements, paths,
timing values, and byte budgets. The Generator does not need to
exercise editorial judgment — every parameter is provided. The only
judgment call: fine-tuning opacity keyTimes in the cycling dots if
the fade-at-destination doesn't look smooth in browser. The plan
provides starting values; the Generator may adjust by ±10% based on
visual inspection.

Content matching: each SVG has a unique `id` attribute
(`fig-autocatalytic-loop`, `fig-edge-of-chaos`, etc.). The Generator
finds each SVG by ID in preprocess.py source, adds the animation
elements, and runs `make dev`.

**Risk:** The edge-of-chaos chaos-panel animation is the most
subjective — "random-looking drift" requires the translate values to
look genuinely disordered, not rhythmic. The plan provides 5 different
value sets with different durations (7s–9s). If all 5 are implemented,
the visual should read as disorder. If it reads as synchronized, the
Generator should increase duration variation.

**Rating: 9/10.** The 1-point gap: chaos-panel animation tuning and
browser-specific SMIL rendering differences may require one adjustment
pass after initial implementation. All other animations are
mechanically determined by their specifications.

---

## Generator Handoff (Phase 1)

```
You are the Generator.

Read Plan 0267 at ~/software/relinquishment/plans/0267-pedagogical-svg-animations.md

Execute Phase 1 (Genesis Trio): Add SMIL animations to three SVGs in
build/preprocess.py, function inject_genesis_illustrations().

(1) fig-autocatalytic-loop: Add 3 cycling dots with animateMotion
per the plan's Animation 1 spec. Each dot: circle r=3 fill=#d4a017
with animateMotion + opacity fade. Timing: 2.4s period, begin 0/0.8/1.6s.

(2) fig-substrate-parallel: Add 6 mirror dots (3 warm #d4a017, 3 cool
#5dade2) per Animation 2 spec. SAME timing as Animation 1 (2.4s, same
staggers).

(3) fig-edge-of-chaos: Frozen panel: NO CHANGES. Edge panel: add
stroke-dasharray + animated stroke-dashoffset on 4 connection paths,
opacity breathing on 4 nodes. Chaos panel: add animateTransform
translate on 5 dots per the plan's value tables.

Add <style> block for prefers-reduced-motion in each SVG's <defs>.
Run `make dev`. Open in browser and verify: cycling dots visible,
mirror timing matches, edge connections flow, chaos dots drift without
rhythm. Report completion.
```

## Generator Handoff (Phase 2)

```
You are the Generator.

Read Plan 0267 at ~/software/relinquishment/plans/0267-pedagogical-svg-animations.md

Execute Phase 2 (Flat Cross-Section): Add SMIL animations to
fig-flat-cross-section in build/preprocess.py, function
inject_flat_diagram().

Animate cx on 6 electron circles per Animation 4 spec. NEVER animate
cy. Add <style> block for prefers-reduced-motion in <defs>. Run
`make dev`. Verify electrons drift horizontally only. Report completion.
```

## Generator Handoff (Phase 3)

```
You are the Generator.

Read Plan 0267 at ~/software/relinquishment/plans/0267-pedagogical-svg-animations.md

Execute Phase 3 (Domain Network Bridges): Add SMIL opacity animations
to 6 dashed elements in fig-domain-buttons in build/preprocess.py,
function inject_domain_buttons().

Animate opacity on dashed lines/paths per Animation 5 spec. Solid
threads: NO CHANGES. Add <style> block for prefers-reduced-motion in
<defs>. Run `make dev`. Verify dashed bridges pulse, solid threads
static, hover tooltips still work. Report completion.
```

---

*Plan 0267 written by Argus (Auditor), S63. Annealed 3 passes
(HIGH LOW LOW). Rating 9/10. Child of Plan 0251. Five animations,
three phases, ~4.3 KB total. Pedagogical, not decorative.*
