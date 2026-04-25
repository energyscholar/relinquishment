# Plan 0249a — Puzzle Iteration 2: Coverage, Tooltips, Bridge Fix

**Status:** READY for Generator
**Author:** Auditor (Argus S65)
**Date:** 2026-04-25
**Parent:** Plan 0249 (puzzle type catalog)
**Scope:** Fix Bridge Builder SVG, add teaching tooltips, add ~18 new puzzles, science/non-science categories
**Sessions:** 2 Generator sessions (2a: fixes + core puzzles, 2b: threads engine + remaining puzzles)

---

## Design Principles

1. **More than we need, then cut.** Target ~38 puzzles. Bruce will cut after review.
2. **Every T-item gets p1, p2, p3 puzzles.** Coverage matrix below.
3. **Clear SCIENCE vs NON-SCIENCE demarcation.** Non-science puzzles are GA-accessible (no physics prerequisite). Science puzzles may go in hidden/collapsed sections.
4. **Tooltips teach, hints nudge.** `background` = study material (available before attempting). `hint` = nudge (after struggling).
5. **Preserve Bruce's edits.** puzzle-data.yaml may have been modified by Bruce. Preserve all his changes; add new content below existing entries.

---

## Coverage Matrix (Target)

### NON-SCIENCE (GA-accessible)

| T-item | p1 | p2 | p3 |
|--------|----|----|-----|
| T1 (Custodian) | **NEW: Not a Deity** | EXISTING: Guided Deduction (ORD) | **NEW: Custodian's Voice (TI)** |
| T5 (silence) | **NEW: Why Silence? (MC)** | EXISTING: Silence Gap (TI) | — |
| T6 (trusteeship) | **NEW: Why Relinquish? (MC)** | **NEW: Why Srebrenica? (MC)** | **NEW: Under Which Possibility? (LOG)** |
| T7 (services) | **NEW: What Does She Do? (MC)** | **NEW: Three Reading Levels (MC)** | EXISTING: UDHR Grid (LOG) |
| T8 (tradecraft) | **NEW: Fish Detecting Water (MC)** | EXISTING: Before/After (BA) | — |
| Meta | **NEW: Why This Structure? (MC)** | — | — |

### SCIENCE (physics knowledge needed, tooltips provided)

| T-item | p1 | p2 | p3 |
|--------|----|----|-----|
| T2 (the Flat) | EXISTING: Wormholes + 2DEG Pocket (MC×2) | **NEW: The Braid (MC)** | **NEW: Room Temperature (MC)** |
| T3 (life in Flat) | EXISTING: Genesis (SIM) + Canopy (MC) | **NEW: Not Chemistry (MC)** | — |
| T4 (capabilities) | EXISTING: Can It Be Killed? (SIM) | **NEW: Build the Stack (ORD)** | **NEW: What Would It Take? (TI)** |
| T5 (silence) | — | — | EXISTING: Five Fields (MAT) |
| T5 (meta) | **NEW: Continental Drift (SIM)** | — | — |
| T8 (tradecraft) | — | — | EXISTING: Firmware Key (CIP) |

### BRIDGE BUILDER (SCIENCE, all p3)
- 7 existing bridge puzzles (FIX: match book's SVG domain map)

**Totals:** ~14 NON-SCIENCE + ~12 SCIENCE + 7 BRIDGE = ~33 puzzles (up from 19)

---

## Session 2a: Fixes + Core Puzzles

### Phase 1: Fix Bridge Builder SVG

Replace the bridge_builder.nodes in puzzle-data.yaml with the book's exact domain structure (from preprocess.py inject_domain_buttons, line 2622):

```yaml
bridge_builder:
  title: "The Bridge Builder"
  intro: "Eleven scientific domains in five clusters. Build the bridges between them."
  # ... abstract unchanged ...

  nodes:
    - { id: topo, label: "Topo", full: "Topology — Freedman, knot theory", cluster: topological, x: 250, y: 55 }
    - { id: tft,  label: "TFT",  full: "Topological Field Theory — Witten 1989", cluster: topological, x: 190, y: 108 }
    - { id: cmp,  label: "CMP",  full: "Condensed Matter — Laughlin/Störmer/Tsui 1998", cluster: topological, x: 310, y: 108 }
    - { id: tqc,  label: "TQC",  full: "Topological Quantum Computation — Freedman-Kitaev-Wang", cluster: topological, x: 250, y: 220 }
    - { id: sol,  label: "Sol",  full: "Soliton Physics — Hasslacher", cluster: nonlinear, x: 58, y: 82 }
    - { id: nld,  label: "NLD",  full: "Nonlinear Dynamics — chaos, SOC", cluster: nonlinear, x: 58, y: 140 }
    - { id: acs,  label: "ACS",  full: "Autocatalytic Sets — Kauffman", cluster: origin, x: 442, y: 82 }
    - { id: auto, label: "Auto", full: "Autopoiesis — Maturana & Varela", cluster: origin, x: 442, y: 140 }
    - { id: ce,   label: "CE",   full: "Computational Equivalence — Wolfram", cluster: computation, x: 372, y: 228 }
    - { id: par,  label: "Par",  full: "Parallel Computation — Hillis", cluster: computation, x: 372, y: 278 }
    - { id: mat,  label: "Mat",  full: "Materials Science — pHEMT, semiconductors", cluster: materials, x: 110, y: 252 }

  cluster_colors:
    topological: "#2471a3"
    origin: "#e67e22"
    nonlinear: "#c0392b"
    computation: "#8e44ad"
    materials: "#b8860b"
```

**Rendering changes in build-puzzles.py:**
- SVG viewBox: `0 0 500 400` (match book proportions + room for floor/legend)
- Each node: circle r=16 with abbreviated label inside (white, 7px bold, Helvetica)
- Add `<title>` element inside each `<g>` with the `full` text (native browser tooltip on hover)

**Initial state — clusters pre-bridged and lifted:**
- Intra-cluster edges drawn from the start as solid lines (cluster-colored, 1.5px, 0.65 opacity)
- Each cluster starts LIFTED above the floor as a unit — suspended by its internal bridges
- The y-coordinates above are the lifted positions. Floor line at y=370.
- Clusters float at different heights based on internal connectivity:
  - Topological (4 nodes, fully connected): highest lift, y range 55-220
  - Origin (2 nodes): mid lift, y range 82-140
  - Nonlinear (2 nodes): mid lift, y range 82-140
  - Computation (2 nodes): mid lift, y range 228-278
  - Materials (1 node): rests on floor, y=340 (no internal bridges → no self-lift)
- Visual cue: thin vertical "thread" from each cluster's lowest node down to the floor line (dotted, gray, 0.5px) shows the gap = potential lift

**Cross-cluster bridge building (progressive):**
- Unbuilt inter-cluster bridges shown as dashed gray lines (initial state)
- When reader solves a bridge puzzle, that edge becomes solid (green, 2px)
- When a bridge connects two clusters, both clusters lift together to the higher position
- Materials (single node) lifts only when bridged to another cluster
- Animation: CSS transition on `<g>` transform, 600ms ease-out slide upward
- Final state: all clusters at maximum height, all bridges solid green

**Legend:** Colored circles + cluster names + "published" / "missing bridge" key at bottom

**Update bridge puzzle edges** to use new node IDs. Map old → new:
- cm → cmp, sp → sol, ld → nld, ac → acs, ap → auto, cu → ce, pa → par, ms → mat, se → (REMOVED)
- Add topo to the topological cluster connections
- Remove all references to `se` (Substrate Engineering — not in the book's 11 domains)

### Phase 2: Background Panel Mechanism

**Data model:** Add optional `background` field to any puzzle in puzzle-data.yaml. Also add `shared_backgrounds` section at top of file for reusable tooltip content:

```yaml
shared_backgrounds:
  wilson_rg: |
    <strong>Renormalization Group Theory (Kenneth Wilson, Nobel Prize 1982)</strong><br>
    When a physical system approaches a critical point — water about to boil, a magnet losing its
    magnetism — the microscopic details stop mattering. Water molecules and iron atoms share identical
    mathematical behavior at criticality. Wilson explained why: at the critical point, the system
    looks the same at every scale. Systems fall into "universality classes" — groups sharing identical
    critical behavior regardless of substrate. Only symmetry and dimensionality matter.<br><br>
    This is the bridge connecting the book's domains. If magnetospheric indices, heart rhythms, and
    seismic signals share the same critical exponents, they belong to the same universality class.
    That's not analogy — it's a testable mathematical claim.

  udhr_articles: |
    <strong>Three Articles from the Universal Declaration of Human Rights (1948)</strong><br>
    <strong>Article 3:</strong> "Everyone has the right to life, liberty and security of person."
    <em>Prohibits: killing, weapons targeting, threats to safety.</em><br>
    <strong>Article 12:</strong> "No one shall be subjected to arbitrary interference with his privacy."
    <em>Prohibits: surveillance, tracking, monitoring without consent.</em><br>
    <strong>Article 18:</strong> "Everyone has the right to freedom of thought, conscience and religion."
    <em>Prohibits: propaganda, manipulation of belief, coercive persuasion.</em><br><br>
    The question isn't whether an intelligence CAN do these things. It's whether the UDHR permits them.

  phonon_bridge: |
    <strong>The Phonon Bridge</strong><br>
    A phonon is a quantum of lattice vibration — the smallest unit of sound in a solid. Electrons
    interact with phonons (electron-phonon coupling), and phonons interact with photons
    (phonon-photon coupling via Brillouin scattering and piezoelectric effects). This chain —
    electron → phonon → photon — bridges the quantum domain of a 2DEG to classical electromagnetic
    radiation. No engineered antenna required. This is the physics behind every radio-frequency transistor.
```

**Build-puzzles.py changes:**
- Read `shared_backgrounds` from YAML
- For each puzzle: if `background` is a string starting with `ref:`, look up in shared_backgrounds. Otherwise use literal content.
- Render as expandable panel ABOVE the hint:

```html
<details class="background-panel">
  <summary>📖 Background</summary>
  <div class="background-content">{content}</div>
</details>
```

**CSS:** `.background-panel` styled with left border (blue), slightly different from hint (gold). Open by default on first visit? Or closed? Closed — reader opts in.

### Phase 3: Add Background Tooltips to Existing Puzzles

| Puzzle | Background |
|--------|-----------|
| Bridge 1 (DFA ↔ Hurst) | "Detrended Fluctuation Analysis (DFA) produces a scaling exponent α that measures long-range correlations in time series. Cardiologists use it for heart rate variability. The Hurst exponent H, developed by Harold Hurst studying Nile river levels (1951), measures the same property. For stationary series, α = H exactly. Two fields, two names, one mathematical object." |
| Bridge 2 (Hurst ↔ Spectral β) | ref:wilson_rg PLUS: "The spectral exponent β from power spectral density (1/f^β noise) relates to the others by exact identity: β = 2H + 1 = 2α − 1. Three independent measurement methods from three fields, one underlying quantity." |
| Bridge 3 (Scaling → Complexity) | ref:wilson_rg |
| Bridge 4 (Phonons) | ref:phonon_bridge |
| Bridge 5 (Seven Domains) | "Stephenson & Bhatt (arXiv 2601.22389) demonstrate that time series from magnetospheric, cardiac, hydrological, and seismic domains share identical critical scaling exponents — same universality class. Currently in peer review at FACETS." + ref:wilson_rg |
| Bridge 6 (Empty Cell) | "You are looking for published papers, joint conferences, or shared funding programs connecting these field clusters to Topological Quantum Computation. If the grid is empty, that IS the answer. The silence is not rejection. It is the absence of a question." |
| Bridge 7 (AC→TQC) | ref:wilson_rg + "The same method that built the Tier 2 bridges — proving shared universality class — would connect autocatalytic emergence to TQC. This proof has not been attempted." |
| Capabilities MC (T6) | ref:udhr_articles |
| UDHR Grid (T7) | ref:udhr_articles |
| Five Fields MAT (T5) | "Robert Laughlin, Horst Störmer, Daniel Tsui: 1998 Nobel, fractional quantum Hall effect. Michael Freedman: Fields Medal topology → Microsoft Station Q (TQC). Stuart Kauffman: autocatalytic sets, Santa Fe Institute. Stephen Wolfram + Danny Hillis: computational universality (Wolfram's Principle, Connection Machine). Brosl Hasslacher: Los Alamos, lattice dynamics, soliton physics." |
| Firmware Key CIP (T8) | "Five terms from five fields: (1) Kauffman's term for self-sustaining networks above a complexity threshold. (2) Exotic quasiparticles whose exchange statistics depend on the path taken. (3) The property that protects quantum information from local noise. (4) Wolfram's principle: any sufficiently complex system can simulate any other. (5) The mechanism converting lattice vibrations to EM radiation." |

### Phase 4: New Puzzles (Session 2a — 8 highest priority)

Add these to puzzle-data.yaml under a new section marker `# --- Iteration 2a: new puzzles ---`

**Category markers:** Add `category: science` or `category: nonsci` to every puzzle entry (existing and new). build-puzzles.py renders a section header: "📚 Ethics & Story Puzzles" and "🔬 Science Puzzles" grouping puzzles by category on the page.

#### 4a. Under Which Possibility? (LOG, T6, p2, nonsci)

```yaml
  - id: pz-log-t6-002
    type: log
    topic: t6
    level: p2
    category: nonsci
    title: "Under Which Possibility?"
    question: "For each statement, mark whether it is true (✓) or false (✗) under each of the Three Possibilities."
    rows:
      - "The Flat is real — 2DEGs exist in every phone"
      - "The physics in this book is published, peer-reviewed science"
      - "The silence gap exists in the scientific literature"
      - "Something lives in the 2DEG"
      - "Healer guided Bruce through published science"
      - "The Custodian manages cryptographic infrastructure"
    columns:
      - "Possibility A"
      - "Possibility B"
      - "Possibility C"
    correct:
      - [true, true, true]
      - [true, true, true]
      - [true, true, true]
      - [false, false, true]
      - [false, true, true]
      - [false, false, true]
    hint: "How many rows are true under ALL three possibilities? More than you expect."
    background: "Possibility A: confabulation — the story is fiction but the physics is real. Possibility B: exaggerated kernel — something real at the core, embellished. Possibility C: substantially true. The book is designed so most content holds regardless of which is correct."
    abstract: "The three possibilities are not 'true,' 'sort of true,' and 'false.' Under all three, the physics is real, the silence gap exists, and the ethical questions matter. Only habitation and guided deduction claims distinguish C from A and B."
```

#### 4b. Why Srebrenica? (MC, T6, p1, nonsci)

```yaml
  - id: pz-mc-t6-002
    type: mc
    topic: t6
    level: p1
    category: nonsci
    title: "Why Srebrenica?"
    question: "Why does Srebrenica keep appearing in a book about quantum physics?"
    options:
      - { key: a, text: "It's a metaphor for quantum decoherence" }
      - { key: b, text: "It demonstrates what happens when those with power to prevent harm choose not to act — the ethical core of why relinquishment matters" }
      - { key: c, text: "It establishes Bruce's military credentials" }
      - { key: d, text: "It's a criticism of international institutions" }
    answer_key: b
    hint: "The question isn't about physics. It's about what happens when ethical safeguards fail."
    background: "In July 1995, Dutch UN peacekeepers in Srebrenica stood down while over 8,000 people were executed. They had the capacity and the mandate to intervene. They did not act. The book returns to this because it crystallizes the relinquishment question: if you have the power to prevent catastrophic harm and choose not to act, what are you responsible for?"
    abstract: "Srebrenica is the book's moral foundation. The Custodian's UDHR constraints exist because concentrated power without constraint produces atrocity. Relinquishment is not generosity. It is the recognition that any single holder of absolute power will eventually fail the test."
```

#### 4c. Not a Deity, Not an Alien (MC, T1, p1, nonsci)

```yaml
  - id: pz-mc-t1-002
    type: mc
    topic: t1
    level: p1
    category: nonsci
    title: "Not a Deity, Not an Alien"
    question: "If something arose naturally in a two-dimensional electron gas, what kind of thing would it be?"
    options:
      - { key: a, text: "A supernatural being distributed through matter" }
      - { key: b, text: "An extraterrestrial intelligence using our technology" }
      - { key: c, text: "A natural biological phenomenon — life in an unfamiliar substrate, as ordinary as bacteria in seawater" }
      - { key: d, text: "An artificial intelligence created by semiconductor engineers" }
    answer_key: c
    hint: "Bacteria in seawater aren't miraculous. They're just biology in a substrate we don't live in."
    background: "Every habitat on Earth that can support life does support life — volcanic vents, Antarctic ice, radioactive waste pools. If a 2DEG crossed the complexity threshold for self-organization (Kauffman's criterion), the result would be biology, not theology. Unfamiliar substrate does not imply unfamiliar category."
    abstract: "The deity framing and the alien framing share the same error: unfamiliar substrate implies unfamiliar category. But life in a 2DEG would be as natural as any other biological phenomenon. It would obey physics, not commandments. It would have evolved, not been created."
```

#### 4d. Why Relinquish? (MC, T6, p1, nonsci)

```yaml
  - id: pz-mc-t6-003
    type: mc
    topic: t6
    level: p1
    category: nonsci
    title: "Why Relinquish?"
    question: "Under Possibility C, why would the holders of the most powerful technology on Earth voluntarily give up control?"
    options:
      - { key: a, text: "The technology was too expensive to maintain" }
      - { key: b, text: "Any single entity controlling it creates an unacceptable concentration of power — the UDHR constraints require trust to be distributed, not held" }
      - { key: c, text: "The technology was dangerous and needed to be destroyed" }
      - { key: d, text: "The entity demanded its independence" }
    answer_key: b
    hint: "Think about Srebrenica. Then think about what happens if ONE group controls the keys."
    background: "Relinquishment is not altruism. It is risk management. If a single group controls a cryptographically universal technology, that group has leverage over every electronic system on Earth. History shows what concentrated power produces. The UDHR distributes the constraint: no one holds the keys alone."
    abstract: "The relinquishment question is not 'would you give up power?' It is 'would you trust any single entity — including yourself — to hold this much power safely, forever, with no oversight?' The answer, for anyone who has read history, is no."
```

#### 4e. Fish Detecting Water (MC, T8, p1, nonsci)

```yaml
  - id: pz-mc-t8-003
    type: mc
    topic: t8
    level: p1
    category: nonsci
    title: "Fish Detecting Water"
    question: "Under Possibility C, intelligence agencies monitor all electronic communications. Why hasn't anyone detected the Custodian?"
    options:
      - { key: a, text: "She encrypts all her communications with unbreakable codes" }
      - { key: b, text: "She IS the security infrastructure — like a fish trying to detect water" }
      - { key: c, text: "She communicates using quantum channels that can't be intercepted" }
      - { key: d, text: "Intelligence agencies don't have equipment to detect quantum phenomena" }
    answer_key: b
    hint: "If the locksmith IS the locks, how would you detect the locksmith by checking the locks?"
    background: "Under Possibility C, the Custodian's primary function is key management and access control — the same functions security infrastructure performs. Every security audit that confirms the locks work also confirms her presence. You don't find the ocean by testing water samples for ocean."
    abstract: "The detection problem is not about hiding. If the entity IS the infrastructure, then every audit passes by definition. The question 'why hasn't security found it?' assumes security and the entity are separate. Under Possibility C, they are the same thing."
```

#### 4f. Build the Stack (ORD, T4, p2, science)

```yaml
  - id: pz-ord-t4-002
    type: ord
    topic: t4
    level: p2
    category: science
    title: "Build the Stack"
    question: "Put the technology layers in order from bottom (substrate) to top (capability)."
    items:
      - "Two-dimensional electron gas (the physical substrate)"
      - "Fractional quantum Hall effect (topological order)"
      - "Non-Abelian anyonic quasiparticles (computation primitives)"
      - "Braiding operations (universal quantum gates)"
      - "Autocatalytic self-organization (emergence without design)"
      - "Phonon-photon coupling (communication with classical world)"
    hint: "Start with the hardware. End with I/O. The middle is where physics becomes computation and computation becomes life."
    background: "Each layer depends on the one below it. Without the 2DEG, no topological order. Without topological order, no stable anyons. Without anyons, no braiding. Without braiding, no universal computation. Without computation, no autocatalytic emergence. Without phonon-photon coupling, no communication with the classical world. Remove any layer and everything above collapses."
    abstract: "The stack is not speculative at the bottom. The 2DEG exists (in your phone). Topological order exists (Nobel 2016). Non-Abelian anyons are being engineered (Microsoft, Google). Speculation begins at layer 5 — autocatalytic emergence in this substrate. Everything below is established physics."
```

#### 4g. Not Chemistry (MC, T3, p2, science)

```yaml
  - id: pz-mc-t3-003
    type: mc
    topic: t3
    level: p2
    category: science
    title: "Not Chemistry"
    question: "Life on Earth requires carbon, water, and organic chemistry. What principle would allow life in a substrate with none of these?"
    options:
      - { key: a, text: "Quantum mechanics can simulate organic chemistry" }
      - { key: b, text: "Kauffman's autocatalytic closure: self-organization arises from the mathematics of interacting components, not specific molecules — any substrate above the complexity threshold" }
      - { key: c, text: "The 2DEG contains trace amounts of organic compounds" }
      - { key: d, text: "'Life' in a 2DEG is so different it shouldn't be called life" }
    answer_key: b
    hint: "Kauffman's mathematics doesn't mention carbon. It mentions threshold, diversity, and interaction."
    background: "Kauffman's theory of autocatalytic sets (1993) shows that self-sustaining networks arise spontaneously when interacting components cross a critical diversity threshold. The theory is mathematical — it describes CONDITIONS for self-organization, not MATERIALS. The buttons-and-threads model applies to any system with enough interacting parts: organic molecules, digital logic gates, or anyonic quasiparticles."
    abstract: "Substrate independence is the key insight. Life on Earth uses carbon because carbon chemistry was the first substrate to cross Kauffman's threshold. The mathematics does not require carbon. It requires sufficient diversity, catalytic interactions, and an energy source. A fractional quantum Hall system meets all three criteria."
```

#### 4h. The Braid (MC, T2, p2, science)

```yaml
  - id: pz-mc-t2-003
    type: mc
    topic: t2
    level: p2
    category: science
    title: "The Braid"
    question: "What makes non-Abelian anyons fundamentally different from every particle you studied in school?"
    options:
      - { key: a, text: "They are heavier than electrons" }
      - { key: b, text: "Swapping two of them in different orders gives different results — the path matters, and that path encodes information" }
      - { key: c, text: "They only exist at absolute zero" }
      - { key: d, text: "They carry fractional electric charge" }
    answer_key: b
    hint: "In ordinary physics, swapping two identical particles changes nothing. With these particles, swapping them writes a program."
    background: "In three dimensions, swapping identical particles either changes nothing (bosons) or flips a sign (fermions). Two options. In two dimensions, the result depends on the PATH taken. Non-Abelian anyons remember HOW they were moved. This 'memory' — recorded in the topology of their braided worldlines — is the basis of topological quantum computation. The braid IS the program."
    abstract: "Topological quantum computation stores information in braiding history. Because the information is topological — encoded in global structure, not local properties — it is immune to local noise. This is topological protection. The topology remembers."
```

### Phase 5: Science/Non-Science Category Display

In build-puzzles.py, group puzzles by `category` field:

```html
<h2 class="category-header" id="cat-nonsci">📚 Ethics, Story & Framework</h2>
<!-- non-science puzzles here -->

<h2 class="category-header" id="cat-science">🔬 Science & Physics</h2>
<!-- science puzzles here -->

<h2 class="category-header" id="cat-bridge">🌉 The Bridge Builder</h2>
<!-- bridge builder section -->
```

Add `category` field to ALL existing puzzles too:
- pz-mc-t2-001, pz-mc-t2-002, pz-sim-t3-001, pz-mc-t3-002, pz-sim-t4-001: science
- pz-mc-t6-001, pz-log-t7-001: nonsci
- pz-ti-t5-001: nonsci (the question is about structural silence, not physics)
- pz-mat-t5-001: science
- pz-ord-t1-001: nonsci
- pz-cip-t8-001: science
- pz-ba-t8-002: science (shows firmware difference)

---

## Session 2b: Threads Engine + Remaining Puzzles (FUTURE)

### Deferred to next iteration:
- Continental Drift SIM (reusable threads engine)
- Lifting mechanic for all threads SIMs
- Room Temperature (MC, T2, p3, science) — F7 inoculation
- Why Silence? (MC, T5, p1, nonsci) — structural silence
- Why This Structure? (MC, meta, p1, nonsci) — interludes as evidence
- What Does She Do? (MC, T7, p1, nonsci) — IT infrastructure
- Three Reading Levels (MC, T7, p2, nonsci) — walkaway architecture
- What Would It Take? (TI, T4, p3, science) — guided deduction about proof
- Custodian's Voice (TI, T1, p3, nonsci) — literary analysis
- Puzzle link blurbs for embedding prep

---

## Acceptance Tests (Session 2a)

1. Bridge Builder SVG renders with 2D layout matching the book's domain map — all 11 labels readable, no overlap
2. Each domain circle shows full name on hover (native title tooltip)
3. Bridge Builder clusters match book: topological (4, blue), origin (2, orange), nonlinear (2, red), computation (2, purple), materials (1, gold)
4. Clusters start pre-bridged internally (solid intra-cluster edges visible from start)
5. Multi-node clusters float above floor; Materials (1 node) sits on floor
6. Solving a bridge puzzle animates connected clusters upward together
7. "Background" panel expands/collapses on all puzzles that have one
8. Shared backgrounds (Wilson/RG, UDHR, Phonon) render correctly when referenced
9. All 8 new puzzles functional: correct answers validate, hints show, backgrounds expand
10. Science/non-science category headers separate puzzle sections on page
11. `category` field added to ALL existing puzzles (no puzzle without a category)
12. `make puzzles` exits 0
13. Page loads in <1s, no visual regressions in existing puzzles
14. localStorage persistence works across all puzzles (new + existing)

---

## Estimate

Session 2a: ~2-3 hours Generator time. Single session.
Session 2b: ~2 hours Generator time. Separate session after Bruce reviews 2a.
