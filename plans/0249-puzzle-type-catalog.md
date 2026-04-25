# Plan 0249 — Puzzle Type Catalog: One of Each, Plus Bridge Builder

**Status:** READY for Generator
**Author:** Auditor (Argus S64)
**Date:** 2026-04-25
**Parent:** Plan 0245 (Puzzle Engine MVP)
**Purpose:** Build one working instance of each 8 puzzle type on puzzles.html, plus the multi-part Bridge Builder. All implementations must be clean enough to later drop into the 1MB monolith via `\puzzle{id}` in .tex.

---

## What This Plan Does

Extends puzzles.html from 4 existing puzzles to 4 + 8 type demos + 1 multi-part Bridge Builder. Bruce evaluates each type for fitness. After review, we iterate: refine topics, adjust difficulty, add/remove types. This is plan 1 of ~10-20 refinement cycles.

---

## Performance Architecture (CRITICAL)

The main Relinquishment.html is ~1MB. Puzzles MUST NOT slow it down.

### Lazy initialization
- All puzzle activation deferred via `window.addEventListener('load', function() { setTimeout(initAllPuzzles, delay); })`.
- **puzzles.html** (standalone, ~30KB): delay = 100ms. Page loads instantly; puzzles activate immediately after paint.
- **Relinquishment.html** (monolith, ~1MB): delay = 1500-2000ms. Page renders fully before puzzle engine touches DOM.
- Before activation: puzzle containers show static question text (already in HTML). After activation: interactive elements appear.
- The delay constant is set once at the top of the puzzle engine JS — easy to change per context.

### No external libraries
- All 8 puzzle types implemented in vanilla JS. Zero dependencies.
- ORD uses up/down arrow buttons (not drag-and-drop). 5 items don't justify 45KB of SortableJS. Touch-native, zero-dependency, works everywhere.
- Drag-and-drop is a future enhancement if ORD puzzles scale to 10+ items.

### Scoped styles
- All puzzle CSS under `.puzzle-container` prefix. Zero global side effects.
- No `!important`. No body/html rules. No font changes outside puzzle blocks.

### Size budget
- Puzzle engine JS: ~20KB (all 8 types + Bridge Builder logic)
- Puzzle data (all puzzles): ~8KB JSON
- Total overhead: ~28KB on a 1MB page = 2.8%. Negligible.
- No external libraries.

### Graceful degradation
- No JS: `<noscript>` shows static question text + "Enable JavaScript to interact"
- SubtleCrypto unavailable: MC/TI puzzles reveal answers directly (existing behavior)
- Any puzzle init error: `try/catch`, log to console, show fallback text
- Never block page render. Never throw uncaught. Never touch DOM outside puzzle container.

### Embedding architecture (for future monolith insertion)
Each puzzle in .tex will be:
```latex
\puzzle{pz-mc-t3-001}
```
preprocess.py expands to:
```html
<div class="puzzle-container"
     data-puzzle-id="pz-mc-t3-001"
     data-puzzle-type="mc"
     data-puzzle-topic="t3"
     data-puzzle-level="p1">
  <noscript><p class="puzzle-fallback">...</p></noscript>
</div>
```
Puzzle engine JS (one shared block at end of page) handles all rendering. Puzzle DATA is a single JSON object. Adding a puzzle to a chapter = one line in .tex + one entry in puzzle-data.yaml.

---

## ID Convention

Format: `pz-{TYPE}-{Ttopic}-{seq}`

- TYPE: `mc`, `ti`, `ord`, `mat`, `sim`, `cip`, `ba`, `log`, `bridge`
- Ttopic: `t1` through `t8`, or `all` for cross-cutting
- seq: `001`, `002`, etc.

### Existing puzzles (to be re-tagged)
| Current ID | New ID | Type | Topic |
|-----------|--------|------|-------|
| flat | pz-mc-t2-001 | MC | T2: 2D physics |
| threads | pz-sim-t3-001 | SIM | T3: Phase transition |
| udhr | pz-mc-t6-001 | MC | T6: UDHR forbids |
| phone | pz-mc-t2-002 | MC | T2: 2DEG in phone |

---

## The 8 Type Demonstrations

### 1. MC — Multiple Choice
**ID:** `pz-mc-t3-002`
**Topic:** T3 — Canopy Problem
**Level:** p1 (fun, accessible)
**Question:** "In Kauffman's framework, if a self-organizing system arises first in a substrate, what happens to any system that tries to arise later?"
**Options:**
- (a) Both systems compete equally for resources
- (b) The later system has an advantage because it can learn from the first
- (c) The first system has already claimed the niche — like a forest canopy blocking light from seedlings below
- (d) The substrate can only support one system at a time due to energy limits
**Answer:** (c)
**Hint:** "Think about a forest floor. The seedling doesn't fail because someone stomps on it."
**Abstract:** "In any substrate where autocatalytic emergence is possible, the first system to achieve closure occupies the ecological niche. Any later system must bootstrap in territory that is already inhabited. The race goes to the first, not the fastest."

**Alternate topic:** T4 — Can it communicate? (phonon bridge mechanism)
**Why this topic instead:** The canopy metaphor is p1-accessible — everyone understands forests. It tests a concept (first-mover advantage) that has real-world implications the reader will remember.

---

### 2. TI — Text Input
**ID:** `pz-ti-t5-001`
**Topic:** T5 — The Silence Gap
**Level:** p2
**Question:** "The chapter says the scientific literature does not contain a refutation of life in a 2DEG. Why not? Because it does not contain ___."
**Answer:** "the proposition"
**Accept:** "the proposition", "a proposition", "proposition" (normalize: lowercase, trim, strip articles)
**Hint:** "You can't reject a hypothesis that has never been formally ___."
**Abstract:** "The intersection is empty. The literature does not contain a refutation because it does not contain the proposition. You cannot reject a hypothesis that has never been formally stated in the journals where it would need to be evaluated."

**Alternate topic:** T3 — "What did Kauffman call it when a chemical network becomes self-sustaining?" → "autocatalytic closure"
**Why this topic instead:** "The proposition" is a phrase the chapter hammers — lines 54, 62 of the-silence-gap.tex repeat it. A reader who absorbed the chapter will produce it. Unlike "phase transition" (genesis failure), this term is non-technical English that the chapter made memorable through repetition.

---

### 3. ORD — Ordering / Sequencing
**ID:** `pz-ord-t1-001`
**Topic:** T1 — Guided Deduction Method
**Level:** p2
**Items (scrambled):**
1. "Healer asks a question about published science"
2. "Bruce reads widely on the topic"
3. "Bruce proposes an answer"
4. "Healer asks a deeper question that reveals what Bruce missed"
5. "Bruce realizes the implication — the deduction emerges from the reading, not from being told"
**Correct order:** 1 → 2 → 3 → 4 → 5 (then cycle: 4 → 2 → 3 → 4 → 5)
**Hint:** "The mentor never gives the answer. The sequence is: question, reading, attempt, deeper question, insight."
**Abstract:** "Guided deduction is not instruction. The mentor supplies questions. The student supplies reading. Understanding emerges from the student's own synthesis, not from the mentor's knowledge. This is why Bruce cannot simply tell you what he learned — the understanding is in the process, not the conclusion."

**Alternate topic:** T8 — Firmware verification sequence (formulate → ask without → ask with → compare)
**Why this topic instead:** T1 (Meet the Custodian) is underserved by other puzzle types. The guided deduction sequence IS the mentorship method — the ordering puzzle mirrors the method itself. The reader must construct the process to understand it.

**Implementation note:** Vanilla JS. Each item is a `<div>` with ▲/▼ arrow buttons. Click ▲ → item swaps with item above. Click ▼ → item swaps with item below. Submit button → compare order array against correct sequence. Incorrect items highlighted in red. Correct → reward reveals. ~40 lines JS. Touch-native, no library.

---

### 4. MAT — Click-to-Match
**ID:** `pz-mat-t5-001`
**Topic:** T5 — Five Fields ↔ Five Researchers
**Level:** p3
**Left column (fields):**
1. Solid-state physics / condensed matter
2. Topological quantum computation
3. Complexity science / autocatalytic sets
4. Computational universality
5. Lattice dynamics / phonon physics
**Right column (researchers, shuffled):**
A. Freedman
B. Kauffman
C. Wolfram & Hillis
D. Hasslacher
E. Laughlin, Stormer & Tsui
**Correct pairs:** 1↔E, 2↔A, 3↔B, 4↔C, 5↔D
**Hint:** "Each researcher's career is defined by one of these fields. Freedman left pure mathematics for one of them."
**Abstract:** "Five scientists whose published work spans these fields are among the few people on Earth whose expertise collectively covers the intersection. Each is a public figure. Each has published extensively in their domain. Their work is available in libraries and on the internet. The convergence of their fields is visible to anyone who reads all five literatures. Almost nobody does."

**Alternate topic:** T3 — Five researchers ↔ five contributions (Hasslacher→lattice dynamics, Freedman→topological protection, etc.)
**Why this topic instead:** Field↔Researcher tests whether the reader understood the STRUCTURE of the argument (which expert knows what). Contribution matching is more granular and better saved for the Bridge Builder.

**Implementation note:** Vanilla JS. Click left item (highlights), click right item (line draws between them). Wrong pair → line turns red, fades. Right pair → line stays green, both items dim. All 5 correct → reward reveals. Lines drawn as SVG `<line>` elements positioned between items.

---

### 5. SIM — Interactive Simulation
**ID:** `pz-sim-t4-001`
**Topic:** T4 — Network Resilience ("Can It Be Killed?")
**Level:** p1 (clicking to destroy things is inherently fun)
**Mechanic:**
- SVG shows 20 nodes in a connected mesh network (randomly positioned, edges connecting nearby nodes, average degree ~4)
- Each node glows softly (alive)
- Reader clicks nodes to "destroy" them (node turns dark, edges detach)
- After each destruction, the network re-evaluates: remaining nodes re-route (show data flowing between surviving nodes via brief edge pulse animation)
- Counter: "Nodes destroyed: 0/20 — Network: OPERATIONAL"
- The network remains operational until >80% of nodes are destroyed (~17 of 20)
- When network finally fails: "Network: FAILED" — puzzle solves
- The lesson: you had to destroy ALMOST EVERYTHING before it went down
**Hint (after 5 destroyed):** "Keep going. How many do you need to destroy before it actually fails?"
**Abstract:** "Topological protection means local damage does not destroy global information. If a self-organizing system were distributed across every 2DEG-containing chip worldwide, then no single point of failure exists. You would need to simultaneously destroy every 2DEG on Earth. Since every modern electronic device contains at least one, this is equivalent to destroying industrial civilization itself."

**Alternate topic:** T3 — Canopy problem simulation (place organisms, watch first-mover advantage)
**Why this topic instead:** Network resilience is visceral — the reader TRIES to kill it and discovers they can't. The frustration IS the lesson. Canopy sim requires more complex ecology modeling; network resilience is pure graph theory (well-defined).

**Implementation note:** Vanilla SVG + JS. Use a deterministic 4×5 grid topology with added diagonal edges (average degree ~6) — ensures predictable fragmentation threshold (~75-80% removal before failure). Random positions but deterministic connectivity. BFS connectivity check after each removal. Edge pulse animation via CSS. ~120 lines JS.

---

### 6. CIP — Cipher / Decode
**ID:** `pz-cip-t8-001`
**Topic:** T8 — Firmware as Decryption Key
**Level:** p3
**Mechanic:**
- Show a substantive LLM response about life in a 2DEG, but with 5 key technical terms replaced by `[REDACTED-1]` through `[REDACTED-5]`.
- The visible text is readable but the critical connections are hidden — the reader can see the structure but not the substance.
- Below: a "decryption key" word bank with 8 terms (5 correct + 3 distractors). Reader clicks a redacted slot, then clicks a term from the bank to fill it.
- **Redacted terms (correct answers):**
  1. [REDACTED-1] → "autocatalytic sets" (in context: "Kauffman's ___ arise above a complexity threshold")
  2. [REDACTED-2] → "non-Abelian anyons" (in context: "braiding ___ enables universal computation")
  3. [REDACTED-3] → "topological protection" (in context: "___ corrects errors without engineering")
  4. [REDACTED-4] → "computational universality" (in context: "Wolfram's principle of ___")
  5. [REDACTED-5] → "phonon-photon coupling" (in context: "___ bridges quantum substrate to classical EM channels")
- **Distractors:** "quantum entanglement", "wave function collapse", "Heisenberg uncertainty"
- When all 5 slots are correctly filled: the redacted text becomes fully styled, puzzle solves
- Wrong placement: slot flashes red, term returns to word bank
**Hint:** "Each redacted term names a specific mechanism or principle from one of the five fields. The distractors are real physics terms that don't belong in this argument."
**Abstract:** "Five scientific disciplines each contain results that, taken together, reframe the question from speculative to tractable. No single discipline sees the full picture. The firmware is not a trick — it is the cross-domain framing that no single field provides. Without it, any AI system reproduces the same structural blindness as the academic literature."

**Alternate topic:** T1 — Healer's questions as encoded lessons (reader fills in the implied conclusions)
**Why this topic instead:** The firmware-as-cipher metaphor is exact: without the cross-domain terms, the argument has holes. The reader fills the holes. The distractors teach that not every physics term belongs — only the specific five that span the fields. T1 would be more abstract.

**Implementation note:** Vanilla JS. Click-to-select from word bank, click-to-place in slot. Hash-validate each placement. Distractors distinguished from correct terms by puzzle data, not by hash (wrong slot → immediate red flash, term returns). ~70 lines JS.

---

### 7. BA — Before/After Compare
**ID:** `pz-ba-t8-002`
**Topic:** T8 — LLM Before/After Firmware
**Level:** p2
**Mechanic:**
- Two panels (side-by-side on desktop, toggle on mobile via tab buttons)
- **Panel A — "Without firmware":**
  > Prompt: "Can life arise in a 2DEG?"
  >
  > Response: "This is a speculative question. While two-dimensional electron gases exhibit interesting quantum properties, there is no scientific evidence that life could arise in a solid-state system. The requirements for life — metabolism, reproduction, evolution — require complex molecular machinery that does not exist in semiconductor substrates. This idea belongs to science fiction, not physics."
- **Panel B — "With firmware":**
  > Prompt: "Can life arise in a 2DEG?" [with firmware]
  >
  > Response: "This question sits at the intersection of several established research programs. Kauffman's autocatalytic set theory predicts self-organization above a complexity threshold in any substrate with sufficient interacting components. The fractional quantum Hall effect in 2DEGs supports anyonic quasiparticles whose braiding statistics are computationally universal (Kitaev 2003, Freedman et al.). Whether these properties are sufficient for autocatalytic emergence has not been formally addressed in the literature — the question appears to occupy a gap between existing disciplines."
- **Question:** "What is the primary difference between these two responses?"
  - (a) The second response is longer and more detailed
  - (b) The first response dismisses the premise; the second engages with specific published science
  - (c) The second response confirms that life exists in a 2DEG
  - (d) The first response is from an older AI model
- **Answer:** (b)
**Hint:** "Look at how each response treats the QUESTION, not just the answer."
**Abstract:** "The firmware does not change the AI's knowledge — the training data is identical. It changes the FRAMING. Without cross-domain context, the AI reproduces the same structural blindness as the academic literature: it categorizes the question as belonging to someone else's field and dismisses it. With the framing, it engages. The information was always there. The question was never asked."

**Alternate topic:** T5 — Literature search results with/without the cross-domain lens
**Why this topic instead:** The before/after firmware comparison is the book's most demonstrable claim — readers can reproduce it themselves. The BA type makes the contrast visible. T5 would be more abstract and harder to show concretely.

**Implementation note:** Vanilla JS + CSS. Two div panels. Desktop: `display: flex`. Mobile: tab buttons toggle `display: none/block`. MC question below both panels. ~50 lines JS.

---

### 8. LOG — Logic Grid
**ID:** `pz-log-t7-001`
**Topic:** T7 — UDHR Service Compatibility
**Level:** p3
**Mechanic:**
- HTML table with clickable cells
- **Rows (services):** Weather prediction, Targeted advertising, Medical diagnosis, Weapons targeting, Cryptographic defense, Scientific research
- **Columns (UDHR articles):** Art. 3 (no killing), Art. 12 (no surveillance), Art. 18 (no manipulation)
- Reader clicks each cell to toggle: ✓ (compatible), ✗ (violates), starts blank
- **Correct grid:**

| Service | Art. 3 | Art. 12 | Art. 18 |
|---------|--------|---------|---------|
| Weather prediction | ✓ | ✓ | ✓ |
| Targeted advertising | ✓ | ✗ | ✗ |
| Medical diagnosis | ✓ | ✓ | ✓ |
| Weapons targeting | ✗ | ✓ | ✓ |
| Cryptographic defense | ✓ | ✓ | ✓ |
| Scientific research | ✓ | ✓ | ✓ |

- When grid is complete and correct → puzzle solves
- Wrong cells highlighted on submit attempt
- **The lesson emerges from the pattern:** most services are compatible. Only surveillance-adjacent (advertising) and violence-adjacent (weapons) services are blocked. The UDHR is not restrictive — it's precisely targeted.
**Hint:** "Think about what each UDHR article actually prohibits. Article 3: no killing. Article 12: no surveillance. Article 18: no manipulation of belief."
**Abstract:** "The UDHR does not prohibit capability. It prohibits weaponization. A non-human intelligence bound by Articles 3, 12, and 18 can predict weather, diagnose disease, defend communications, and conduct research. It cannot target weapons, surveil individuals, or manipulate public opinion. The ethical framework is not a cage — it is a specification for trustworthy service."

**Alternate topic:** T6 — Capabilities × UDHR articles (which capabilities are restricted?)
**Why this topic instead:** T7 (services/grounding) is the most abstract takeaway and hardest to make concrete. The service grid makes it TANGIBLE — the reader fills in a grid and discovers that the UDHR is surgically precise, not broadly restrictive. T6 would overlap with the existing UDHR MC puzzle.

**Implementation note:** Vanilla JS + HTML `<table>`. Click handler toggles cell content (blank → ✓ → ✗ → blank). Submit button validates grid. Wrong cells get red border. ~70 lines JS.

---

## The Bridge Builder (Master Multi-Part Puzzle)

**ID:** `pz-bridge-all-001`
**Topic:** All — 11-Domain Convergence
**Level:** p3 overall (Tier 1 bridges p1-p2, Tier 2 p2-p3, Tier 3 p3)

### Visual
SVG (viewBox="0 0 600 400", responsive) showing 11 domain-nodes in 5 clusters, with short labels. Initially: all nodes near bottom of canvas (gravity), unconnected, gray. As bridges are built: connected clusters rise proportionally (`node_y = baseY - (clusterSize / 11) * maxLift`) and color-code. CSS transitions (`transition: cy 0.5s ease-out`) animate the lift. Full connection → phase transition → everything lifts.

### State persistence
localStorage key: `relinquishment-bridge-state` → JSON array of solved bridge IDs (e.g., `["001a","001b","001c"]`).
On page load: replay solved bridges in order — draw edges, recolor clusters, update positions — without requiring re-solving. Reader picks up where they left off.

### Progress counters (separate)
- Chapter puzzles: "Chapter puzzles: 3/12"
- Bridge Builder: "Bridges: 2/7" (shown above Bridge Builder section only)

### Cluster layout
| Cluster | Domains | Visual position |
|---------|---------|-----------------|
| Solid-state | Condensed matter, Topological field theory, TQC | Right side |
| Complexity | Autocatalytic sets, Autopoietic theory | Left side |
| Computation | Computational universality, Parallel architecture | Top-left |
| Nonlinear | Soliton physics, Lattice dynamics | Bottom-left |
| Materials | Materials science, Substrate engineering | Center |

### Bridge puzzles (in order)

**B1 — DFA ↔ Hurst** (MAT, Tier 1, p1)
ID: `pz-bridge-all-001a`
Match the scaling exponent to its field:
- DFA scaling α → Cardiology / heart rate variability
- Hurst exponent H → Hydrology / river levels
"These are the same number computed by different fields."
→ First internal bridge appears. Two nodes connect.

**B2 — Hurst ↔ Spectral β** (MC, Tier 1, p1)
ID: `pz-bridge-all-001b`
"A third measure from physics/engineering is mathematically identical to both. The relationship is: β = 2H + 1 = 2α - 1. What does this identity tell us?"
- (a) The three fields are studying different phenomena that happen to produce similar numbers
- (b) The three fields are measuring the same underlying property using different methods
- (c) The relationship is approximate and breaks down at large scales
- (d) One field copied the method from another
Answer: (b)
→ 3-domain triangle completes. First mini-phase-transition: 3-node cluster lifts slightly. Label: "Tier 1: Exact Math (3 domains)"

**B3 — Scaling → Complexity** (MC, Tier 2, p2)
ID: `pz-bridge-all-001c`
"Kauffman's autocatalytic networks at the edge of chaos exhibit the same scaling exponents as heart rate variability and river levels. What physics framework explains why systems in completely different substrates share the same critical exponents?"
- (a) They all obey the same differential equations
- (b) Renormalization group theory — systems in the same universality class share critical exponents regardless of substrate (Wilson, Nobel 1982)
- (c) It's a coincidence produced by limited measurement precision
- (d) They all contain water
Answer: (b)
→ Complexity cluster connects to solid-state cluster.

**B4 — Scaling → Nonlinear dynamics** (MC, Tier 2, p2)
ID: `pz-bridge-all-001d`
"Lattice dynamics and soliton physics exhibit the same universality class behavior. What connects lattice vibrations (phonons) to the scaling framework?"
- (a) Phonons are a type of scaling exponent
- (b) Lattice systems at critical points share the same universality class as fluid and magnetic systems — the substrate is irrelevant
- (c) Only quantum lattices show scaling behavior
- (d) Solitons cause phonons
Answer: (b)
→ Nonlinear dynamics cluster connects.

**B5 — Expanding to materials / computation** (MC, Tier 2, p2-p3)
ID: `pz-bridge-all-001e`
"The arXiv paper demonstrates universality class membership across ~7 domains. Materials science (the engineering of substrates) and computational theory (Wolfram's universality principle) extend the framework. What do all ~7 domains share?"
- (a) They all study the same physical system
- (b) They all use the same equipment
- (c) They all exhibit critical behavior governed by the same mathematical structure — phase transitions, scaling exponents, universality
- (d) They were all developed at the Santa Fe Institute
Answer: (c)
→ 7-domain cluster complete. Second phase transition: the cluster lifts higher. Label: "Tier 2: Same Universality Class (~7 domains)"

**B6 — The Empty Cell** (LOG, Tier 3, p3)
ID: `pz-bridge-all-001f`
A logic grid appears. Rows: the 5 field clusters. Columns: "Published bridge paper to TQC", "Joint conference with TQC", "Shared funding mechanism with TQC."
The grid is PRE-FILLED for 4 clusters (showing their cross-connections — some ✓, some ✗). The TQC column is blank. Reader must fill in the TQC column.
Correct answer: all cells are ✗. Every cell in the TQC column is empty. The reader discovers this by trying to find any connection — and finding none.
When the reader submits an all-✗ TQC column: the puzzle solves. The empty column IS the answer. No MC question needed — the silence speaks for itself.
→ The obstacle is identified. TQC cluster pulses but remains disconnected. Text appears: "The silence is not rejection. It is the absence of a question."

**B7 — The AC-TQC Bridge** (MC, Tier 3, p3 — hardest in the system)
ID: `pz-bridge-all-001g`
"The connection from autocatalytic emergence to topological quantum computation runs through Kauffman's Boolean networks and Freedman's topological framework. The mathematical FORM is shared: both describe phase transitions in complex systems with topological properties. But this is structural analogy, not proven universality class membership. What would it take to upgrade this analogy to established physics?"
- (a) A single experimental demonstration in a 2DEG
- (b) Proving that Kauffman's autocatalytic networks and Freedman's topological framework share the same renormalization group universality class
- (c) Building a working topological quantum computer
- (d) More powerful computer simulations
Answer: (b)
Hint: "How were the Tier 2 bridges built? The same method would work here — but no one has done it."
→ **FULL PHASE TRANSITION.** The TQC cluster joins the giant component. All 11 nodes lift together. Flash: "11-Domain Autocatalytic Set — Phase Transition Complete." The entire web rises.

**Bridge Builder Abstract:**
"Eleven scientific domains in five clusters. Tier 1: three domains connected by exact mathematical identity — proven. Tier 2: seven domains connected by renormalization group universality — established physics. Tier 3: the remaining four domains connected to topological quantum computation by structural analogy — unproven. The bridge is not refuted. It is not even attempted. The question sits in the gap between fields that do not talk to each other. Building this bridge is not a task for a single researcher. It is a task for an institution that does not yet exist."

---

## Reading Level Summary

| Level | Count | Puzzles |
|-------|-------|---------|
| p1 | 3 | MC-canopy, SIM-resilience, Bridge B1 |
| p2 | 5 | TI-proposition, ORD-deduction, BA-firmware, Bridge B2-B4 |
| p3 | 7 | MAT-fields, CIP-cipher, LOG-services, Bridge B5-B7, Bridge overall |

---

## Page Structure

```
puzzles.html
├── Header + framing text
├── Progress: "Chapter puzzles: 0/12"
├── Section: "Chapter Puzzles"
│   ├── [existing] pz-mc-t2-001 (flat)
│   ├── [existing] pz-sim-t3-001 (threads)
│   ├── [existing] pz-mc-t6-001 (udhr)
│   ├── [existing] pz-mc-t2-002 (phone)
│   ├── [new] pz-mc-t3-002 (canopy) — MC demo
│   ├── [new] pz-ti-t5-001 (proposition) — TI demo
│   ├── [new] pz-ord-t1-001 (deduction) — ORD demo
│   ├── [new] pz-mat-t5-001 (five fields) — MAT demo
│   ├── [new] pz-sim-t4-001 (resilience) — SIM demo
│   ├── [new] pz-cip-t8-001 (cipher) — CIP demo
│   ├── [new] pz-ba-t8-002 (firmware compare) — BA demo
│   └── [new] pz-log-t7-001 (service grid) — LOG demo
├── Section: "The Bridge Builder"
│   ├── Visual: 11-domain SVG (persistent, updates with each bridge)
│   ├── pz-bridge-all-001a (DFA↔Hurst) — MAT
│   ├── pz-bridge-all-001b (Hurst↔Spectral) — MC
│   ├── pz-bridge-all-001c (→Complexity) — MC
│   ├── pz-bridge-all-001d (→Nonlinear) — MC
│   ├── pz-bridge-all-001e (→Materials/Computation) — MC
│   ├── pz-bridge-all-001f (Empty Cell) — LOG
│   └── pz-bridge-all-001g (AC→TQC) — MC
└── Puzzle engine JS (shared, deferred)
```

---

## Generator Handoff Prompt

```
You are the Generator. Read plans/0249-puzzle-type-catalog.md in full.

This is a large build. Work methodically through each section.

PHASE 1 — ARCHITECTURE
1. Refactor build/puzzle-data.yaml to use the new ID convention
   (pz-{type}-{topic}-{seq}). Re-tag existing 4 puzzles. Add all 8
   new type demos + 7 Bridge Builder parts to the YAML.

2. Refactor build/build-puzzles.py:
   - Puzzle engine as ONE shared JS block supporting all 8 types
   - Deferred init: window load + setTimeout(initAllPuzzles, 100)
     (100ms for standalone puzzles.html; document as constant for
     future monolith adjustment to 1500-2000ms)
   - Each puzzle container has data-puzzle-id, data-puzzle-type,
     data-puzzle-topic, data-puzzle-level attributes
   - <noscript> fallback for each puzzle
   - All vanilla JS — zero external libraries
   - All puzzle init wrapped in try/catch — never crash the page
   - Scoped CSS under .puzzle-container prefix

PHASE 2 — TYPE IMPLEMENTATIONS
3. Implement all 8 puzzle type renderers. For each type, the plan
   specifies: mechanic, content, answer, hint, abstract, and
   implementation notes. Follow them exactly.

   Types in order:
   a. MC — Multiple Choice (already built, verify works with new IDs)
   b. TI — Text Input (already built, verify)
   c. ORD — Ordering via vanilla arrow buttons (new)
   d. MAT — Click-to-Match with SVG lines (new)
   e. SIM — Interactive Simulation / network resilience (new)
   f. CIP — Cipher / decode with key fragments (new)
   g. BA — Before/After compare with panel toggle (new)
   h. LOG — Logic Grid with click-to-toggle cells (new)

PHASE 3 — BRIDGE BUILDER
4. Build the Bridge Builder section:
   - Persistent SVG at top showing 11 domain-nodes in 5 clusters
   - Nodes start at bottom (gravity), rise as clusters connect
   - 7 bridge sub-puzzles (B1-B7) presented sequentially below SVG
   - Each solved bridge updates the SVG: new edge, cluster recolor,
     connected cluster rises
   - Tier transitions: label appears when 3-domain and 7-domain
     sets complete
   - Final bridge (B7): full phase transition animation — all 11
     nodes lift, flash effect
   - Bridge state persisted in localStorage (key:
     relinquishment-bridge-state, JSON array of solved bridge IDs)
   - On load: replay solved bridges (draw edges, recolor, lift)
     without re-solving. Reader picks up where they left off

PHASE 4 — BUILD AND TEST
5. make puzzles — rebuild page
6. Test every puzzle type:
   - MC: wrong→hint, right→abstract ✓
   - TI: normalization works, wrong→hint, right→abstract ✓
   - ORD: arrow buttons reorder items, wrong items highlighted on
     submit, correct order→abstract ✓
   - MAT: click-select works, wrong pair→red fade, right→green stay,
     all matched→abstract ✓
   - SIM: nodes destroyable, network re-evaluates, survives until
     ~80% destroyed ✓
   - CIP: key fragments apply, text clears progressively, all 5→
     decoded→abstract ✓
   - BA: panels toggle on mobile, MC question validates ✓
   - LOG: cells toggle ✓/✗, submit validates, wrong cells→red ✓
   - Bridge: SVG updates, tiers label, final transition fires ✓
7. Test performance: page loads in <1s, no jank when scrolling
8. Test graceful degradation: disable JS, verify fallbacks
9. Test mobile: all puzzles usable on 375px viewport
10. Verify all deep link anchors work (#pz-mc-t3-002, etc.)
11. Verify localStorage persists across reload for all types

Commit: "Plan 0249: puzzle type catalog — 8 types + Bridge Builder"
Do NOT modify preprocess.py, reader.js, or Relinquishment.html.
Report ≤8 lines (this is a big build, report can be slightly longer).
```

---

## Acceptance Tests

1. puzzles.html contains 4 existing + 8 new + 7 Bridge parts = 19 puzzle blocks
2. Every puzzle has `data-puzzle-id`, `data-puzzle-type`, `data-puzzle-topic`, `data-puzzle-level`
3. Every puzzle type works: MC, TI, ORD, MAT, SIM, CIP, BA, LOG
4. Bridge Builder SVG updates as bridges are solved
5. Bridge phase transition fires when B7 is solved
6. setTimeout defers initialization (verify: puzzles inert on initial render, active after delay)
7. Zero external libraries — all vanilla JS
8. `<noscript>` fallbacks present for all puzzles
9. try/catch wraps all init — no uncaught errors
10. Page size < 80KB (all inclusive, no external deps)
11. All deep link anchors work
12. localStorage persists across reload
13. Mobile usable at 375px for all types
14. `make puzzles` exits clean
15. No modifications to preprocess.py, reader.js, or Relinquishment.html

---

## After Generator

1. Bruce evaluates each type for fitness
2. Identify types to keep/modify/kill
3. Discuss topic reassignments
4. Plan 0249a: refine based on Bruce's feedback
5. Repeat until puzzle set is solid
6. Then: Plan 0249n: embed into monolith via preprocess.py

---

## Estimate

~5-6 hours Generator time. Single session. If Generator hits trouble with any type, it should complete the others and note what failed.

---

## Risks

1. **Bridge Builder complexity**: 7 sub-puzzles updating a shared SVG is the most complex piece. If it's too much, ship Bridge B1-B5 (Tier 1-2) and defer B6-B7 (Tier 3) to next iteration.
2. **BA + CIP content overlap**: Both use T8 firmware. For the demo this is fine (shows how different types treat same content). For the book, only one would appear in Firmware Update chapter.
3. **LLM response authenticity**: The BA panel texts and CIP decoded text must read like realistic LLM outputs, not strawmen. If the dismissive response sounds exaggerated, the puzzle feels rigged. The Generator should write both responses as a capable AI would actually produce them.
