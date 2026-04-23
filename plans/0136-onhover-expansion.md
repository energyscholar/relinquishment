# Plan 0136: Systematic onHover Popup Expansion

**STATUS: ALL PHASES COMPLETE (2026-04-07)**
- Phase 0: Menu + control tooltips — COMPLETE (reader.js title attributes)
- Phase 1A: Definitions + hovertip calls (Tier 1) — COMPLETE (31 YAML terms, hovertip calls in hook/stack/summary)
- Phase 1A-6: PDF footnote decision — COMPLETE (hovertiphtml macro created for p3)
- Phase 1B: Title-line panel unification — DEFERRED (hardcoded panels work fine)
- Phase 2: p3 chapter hovertips (Tier 2) — COMPLETE (54 hovertip/hovertiphtml calls across 13 files)
- Phase 3: SVG illustrations — PARTIAL (5 SVGs in YAML; Bruce to add more manually)
- Phase 4: QA + polish — COMPLETE via Plan 0138

## Governing Rules

### 1. Science and text-stack only
**Popups are NEVER for story content. Only for science and text-stack content.**

Bruce will manually add a small number of story-related popups. The Generator must not create popups for character names, place names, plot events, personal history, or narrative elements. If a term is both story and science (e.g., "Guardian"), the popup covers ONLY the science dimension — the substrate physics, not the character.

### 2. p-Level escalation
- **p1 hover** (hook, The Stack) → popup shows **p2-level** content
- **p2 hover** (summary) → popup shows **p3-level** content
- **p3 hover** (main chapters) → popup shows **peer-reviewed definition** or cross-reference

Popup content is always ONE LEVEL DEEPER than the surrounding text.

### 3. One hovertip per term, first occurrence wins
Each term gets ONE `\hovertip{}` call, placed at its first meaningful appearance in reading order (determined by main.tex include order). The popup content bridges to the next level from THAT location. Do not double-up across p-levels. Later appearances render as `<em>` via the first-occurrence rule.

Example: "wormholes" first appears in The Stack (p1). It gets a p1→p2 popup there. In summary.tex (p2), it renders as `<em>` — fine, because the reader already saw the popup.

**Corollary:** Before placing any `\hovertip{}`, verify the term hasn't already fired earlier in reading order — including the 3 title-line rich panels (Relinquishment, Wormholes, the Flat).

### 4. Hover IDs for authoring feedback
Every `.hover-term` span gets a `data-hover-id` attribute (slugified YAML key, e.g., `data-hover-id="topological-order"`). Present in all builds — invisible, weighs nothing.

In non-FINAL builds, the popup panel shows a subtle gray footer: `[topological-order]`. This lets Bruce reference specific popups for feedback ("fix hover:soliton"). Stripped in `\FINAL` builds.

Feedback format: `hover:<id>` (e.g., "hover:edge-of-chaos needs an SVG").

---

## Current State

### Existing hovertip infrastructure
- `hover-definitions.yaml`: 16 terms defined (13 plain, 3 with target links)
- `\hovertip{}` macro in LaTeX → `HOVERSTART§term§HOVEREND` markers → `.hover-term` spans
- `data-hover` (plain text) and `data-hover-html` (rich HTML + SVG) attributes
- First-occurrence-only rule: subsequent uses render as `<em>`
- 3 rich panels on title line (Relinquishment, Wormholes, the Flat) — hardcoded in preprocess.py
- Copy Prompt One / Copy Prompt Two buttons — already have popups (implemented S54)

### Current \hovertip{} calls by file
| File | Terms | Count |
|------|-------|-------|
| hook.tex (p1) | grew, flat worlds | 2 |
| the-stack.tex (p1) | — | 0 |
| summary.tex (p2) | 2DEG, topological order, nonlocal, entanglement, wormholes, quantum teleportation, classical backchannel, autocatalytic, magnetosphere, encryption, topological protection, relinquishment, guided deduction, SAS | 14 |
| p3 chapters | — | 0 |

### Gap analysis
- **The Stack has ZERO hovertips.** Biggest gap — introduces 8 technology properties, wormholes, topological wormholes.
- **p1 has only 2 hovertips** across 2 files. Needs 6-8 more.
- **p2 has 14 hovertips**, all in summary. Some terms will become `<em>` if their first occurrence moves to The Stack (Rule 3). Missing terms: DARPA, Five Eyes, GCHQ, public-key cryptography, dual use, confabulation, falsifiable, Dunning-Kruger, Bletchley Park, convergence, soliton.
- **p3 has 0 hovertips.** Needs 30-40 across key chapters.

### Menu + control popups (Phase 0 — separate mechanism from \hovertip{})
Every visible element in the navigation UI should have a descriptive popup:
- **Chapter/section headings in the menu** — each menu item gets a 1-2 sentence summary popup describing what that chapter/section contains. Generated in reader.js from a data source (build-time injection or inline `title` attributes).
- **Part headings** (Guided Deduction, The Evidence Trail, Forgiveness) — summary of the part's arc.
- **Lower menu bar controls** — Expand All, AI Eval, Back, Top, § share, quick-jump links — each gets a descriptive tooltip explaining what it does.
- These are `title` attributes or custom tooltip divs in reader.js, NOT `\hovertip{}` calls. Different mechanism, same UX principle.

### Tone note
Bruce plans manual adjustments to add levity and humor to selected popups. The Generator should write accurate, clear definitions but not over-formalize tone — leave room for Bruce's voice. Popup content is a starting point, not final copy.

---

## Complete Term Inventory

### Tier 1: MUST HAVE — Terms a general reader will stumble on (p1 + p2)

Terms where a reader who doesn't know the word will lose the thread.

**NOTE:** Under Rule 3, each term appears ONCE. If a term is listed for both The Stack and summary, the `\hovertip{}` goes at first reading-order occurrence only. The popup bridges from THAT level.

#### p1: hook.tex (popup content = p2 level)

| # | Term | Current? | Popup content sketch |
|---|------|----------|---------------------|
| 1 | grew | YES | Self-organization, not engineering. Autocatalytic emergence. |
| 2 | flat worlds | YES | 2D layers in chips and magnetosphere. Topological order. |
| 3 | quantum computer | NO | Machine using quantum effects to solve problems no normal computer can. |
| 4 | master keys | NO | Cryptographic keys controlling access. Whoever holds them controls the system. |
| 5 | Universal Declaration of Human Rights | NO | 1948 UN document. 30 articles listing basic human rights. Written after WWII to say "never again." |

*"special forces" — STORY, skip.*

#### p1: the-stack.tex (popup content = p2 level)

| # | Term | Current? | Popup content sketch |
|---|------|----------|---------------------|
| 6 | stack (technology stack) | NO | Each technology does everything the one before it did, plus something new. Cumulative. |
| 7 | self-maintaining structure | NO | A structure that repairs and sustains itself. Candle recovers from wind. Cells repair damage. |
| 8 | self-organizes | NO | Global order from local rules. No central control. Ants, markets, immune systems. |
| 9 | topological wormhole | NO | Fold the paper so the two points touch. Real physics — 2016 Nobel Prize. More restricted than spacetime wormholes. |
| 10 | two dimensions | NO | Movement restricted to a flat sheet. The third dimension is physically gone, not just ignored. |
| 11 | threshold | NO | Below: nothing happens. Above: everything changes. Phase transitions in physics. |

*Note: title-line "Wormholes" rich panel fires before The Stack in reading order. "topological wormhole" is a distinct YAML key — different concept (restricted type vs. general). Verify no collision.*

#### p2: summary.tex (popup content = p3 level)

Terms already present (14) plus new additions. Under Rule 3, any term whose first occurrence moved to hook/Stack becomes `<em>` here — that's correct behavior.

| # | Term | Current? | Popup content sketch |
|---|------|----------|---------------------|
| 12-25 | (14 existing terms) | YES | — (definitions already in YAML) |
| 26 | DARPA | NO | US military's science agency. Created the internet, GPS, stealth. Funds what doesn't exist yet. |
| 27 | Five Eyes | NO | Intelligence alliance: US, UK, Canada, Australia, NZ. Share secrets with each other only. |
| 28 | GCHQ | NO | Britain's code-breaking HQ. Equivalent of NSA. Invented public-key crypto 1973, kept it secret 24 years. |
| 29 | public-key cryptography | NO | Encryption using paired keys. One public, one private. Basis of all internet security. |
| 30 | dual use | NO | Technology that is both useful and dangerous. Nuclear: power plants and bombs. Biology: vaccines and bioweapons. |
| 31 | confabulation | NO | Pattern-matching mind building a coherent narrative from real pieces that may not fit. Not lying — believing. |
| 32 | falsifiable | NO | A claim that tells you what would prove it wrong. Science requires this. Conspiracy theories don't. |
| 33 | Dunning-Kruger effect | NO | When limited knowledge produces overconfidence. You don't know what you don't know. |
| 34 | Bletchley Park | NO | British WWII codebreaking center. 10,000 people kept the secret for 35 years. Birthplace of computing. |
| 35 | convergence | NO | Independent lines of research pointing to the same conclusion from different directions. |
| 36 | soliton | NO | A wave that holds its shape. Doesn't spread out or break apart. Self-reinforcing. Found in oceans, fiber optics, plasma. |

*"HALO jump" — military technique, not science or text-stack. Skip (Bruce-manual if desired).*
*"COWS" — STORY. Skip (Bruce-manual if desired).*

### Tier 2: SHOULD HAVE — Terms in p3 chapters (popup = peer-reviewed definition)

Priority by frequency and reader-stumble risk.

#### HIGH PRIORITY (appear in 5+ chapters, central to argument)

| # | Term | First occurrence chapter | Popup content sketch |
|---|------|------------------------|---------------------|
| 37 | anyon | The Braid | Exotic 2D particle. Exchange two → any phase (not just +1 or -1). Only exist in 2D. |
| 38 | non-abelian anyon | The Braid | Anyon whose exchanges depend on ORDER. A then B ≠ B then A. Enables topological computation. |
| 39 | fractional quantum Hall effect | The Braid | Nobel 1998. Electrons in 2D under strong magnetic field → fractional charges. Proves anyons exist. |
| 40 | TQNN | Three Possibilities | Topological Quantum Neural Network. The book's central technology claim. All 8 stack properties. |
| 41 | braiding | The Braid | Moving anyons around each other. The PATH is the computation. Like tying knots in spacetime. |
| 42 | phase transition | The Demo | Sudden change at a threshold. Water→ice. Complexity→life. Gradual buildup, sudden shift. |
| 43 | edge of chaos | The Demo | Narrow regime between frozen order and random chaos. Where computation and life happen. |
| 44 | computational universality | The Demo | Any sufficiently complex system can compute anything any other system can. Turing's insight. |
| 45 | cellular automaton | Growing a Mind | Grid of cells following simple rules. Can generate unlimited complexity. Wolfram's central object. |
| 46 | decoherence | The Factoring Game | Loss of quantum behavior due to environment. The enemy of quantum computing. Topology defeats it. |
| 47 | quantum coherence | The Braid | Quantum system maintaining its wave-like behavior. Required for quantum computation. |

#### MEDIUM PRIORITY (appear in 2-4 chapters, important but less central)

| # | Term | Popup content sketch |
|---|------|---------------------|
| 48 | Shor's algorithm | Quantum algorithm that factors large numbers fast. Published 1994. Breaks RSA. |
| 49 | RSA | The encryption protecting most of the internet. Based on factoring being hard. |
| 50 | lattice gas automata | Hasslacher's model: simulate fluids on a grid. Simple rules → complex flow. |
| 51 | NK fitness landscape | Kauffman's model of evolution. N genes, K interactions. Rugged terrain. |
| 52 | Connection Machine | Hillis's 1985 supercomputer. 65,536 processors working in parallel. |
| 53 | Chern-Simons theory | Math linking knots to quantum physics. Witten's Fields Medal (1990). |
| 54 | knot invariant | Number describing a knot that doesn't change when you wiggle it. Connects to braiding. |
| 55 | Jones polynomial | A knot invariant. Computable by braiding anyons. Math-to-physics bridge. |
| 56 | HEMT / pHEMT | Transistor containing a 2DEG. In every phone, every satellite dish. Mass-produced. |
| 57 | MOSFET | The transistor in every chip. Contains a 2DEG at its oxide interface. Billions per chip. |
| 58 | NV center (nitrogen-vacancy) | Diamond defect maintaining quantum coherence at room temperature. Commercial quantum sensor. |
| 59 | room-temperature quantum coherence | Quantum behavior at 300K. Proven in NV-diamond, SiC, biological systems. Not speculative. |
| 60 | plasma sheet | Hot charged particles trapped in a 2D sheet by Earth's magnetic field. Thousands of km across. |
| 61 | heliospheric current sheet | Solar system's largest 2D structure. Separates magnetic polarities. Alfven's "ballerina skirt." |
| 62 | substorm | Explosive energy release in magnetotail. Drives auroras. Particle injection. |
| 63 | self-organized criticality | Systems naturally evolve to a critical state. Sandpiles. Earthquakes. Magnetosphere. |
| 64 | Schumann resonances | EM standing waves between Earth and ionosphere. 7.83 Hz fundamental. Natural waveguide. |
| 65 | wave-particle interaction | Energy exchange between EM waves and charged particles. How the magnetosphere communicates internally. |
| 66 | collisionless plasma | Plasma so thin particles rarely collide. Thermal arguments fail. Different physics. |
| 67 | Parable of the Tribes | Schmookler: competing groups cannot unilaterally choose peace. One aggressor forces all to arm. |
| 68 | information asymmetry | One party knows what the other doesn't. Extreme form = total strategic advantage. |
| 69 | parallel construction | Using a fake explanation to hide the real intelligence source. Legal in US courts. |
| 70 | gain-of-function research | Engineering pathogens to be more dangerous. The biology version of dual use. |
| 71 | directed evolution | Frances Arnold's Nobel technique. Artificial selection finds what rational design can't. |
| 72 | morphogenesis | How a single cell becomes a body. Turing's last paper (1952). Chemical gradients → biological form. |
| 73 | reaction-diffusion | Turing's math for pattern formation. Uniform chemicals → stripes, spots, spirals. |
| 74 | Boolean network | Kauffman's model: nodes with on/off states. At critical connectivity → cell-type attractors. |
| 75 | Kauffman's biogenesis | Life is not a lucky accident — an expected phase transition once chemistry is complex enough. |
| 76 | integrated information (Tononi) | Consciousness theory: a system is conscious if its information is integrated, not decomposable. |
| 77 | poised realm | Kauffman's quantum-classical boundary. Edge-of-chaos systems may sustain coherence longer. |

#### LOWER PRIORITY (single chapter, specialist terms — include if space permits)

| # | Term | Popup content sketch |
|---|------|---------------------|
| 78 | quasiparticle | Not a real particle — a collective excitation behaving like one. Phonon, anyon, hole. |
| 79 | braid group | Math describing how strands can cross. The algebra behind anyon computation. |
| 80 | Reidemeister moves | Three fundamental operations on knots. If two knots relate by these moves, they're equivalent. |
| 81 | topological insulator | Insulating inside, conducting on the surface. Room temperature. Topological protection without cooling. |
| 82 | graphene | Single atom layer of carbon. A natural 2DEG. |
| 83 | cyclotron frequency | How fast a charged particle orbits in a magnetic field. Sets the energy scale. |
| 84 | power-law decoherence | Edge-of-chaos systems may decohere slower than exponential. Extends quantum coherence window. |
| 85 | FMO complex | Bacterial protein using quantum coherence in photosynthesis. Nature 2007. |
| 86 | Langton parameter | Number measuring how close a cellular automaton is to the edge of chaos. Lambda ~0.91 = critical. |
| 87 | no-cloning theorem | You can't copy an unknown quantum state. Fundamental limit. Protects quantum crypto. |
| 88 | Bennett's theorem | Quantum teleportation requires a classical backchannel. No FTL. Period. |
| 89 | Dual EC DRBG | NSA-backdoored random number generator. Proven in 2013. Shows crypto subversion is real. |
| 90 | BULLRUN | NSA program to defeat encryption. Snowden 2013. Shows Five Eyes cryptanalysis ambitions. |
| 91 | zero-day exploit | Software flaw unknown to the vendor. Valuable cyber weapon. |
| 92 | Great Filter | Why don't we see aliens? Something kills technological civilizations. Fermi paradox. |
| 93 | QuIST | $100M DARPA quantum computing program (2002). Public evidence of serious investment. |
| 94 | Colossus | World's first programmable electronic computer. Bletchley Park 1943. Secret until 1970s. |
| 95 | Enigma | German cipher machine. Broken by Turing at Bletchley Park. Changed the war. |

**Total: 95 terms (36 Tier 1, 41 Tier 2 high+medium, 18 Tier 2 lower)**
Existing coverage: 16 terms in YAML. Net new: **79 terms**.

---

## Phase 0: Menu + Control Tooltips (Generator task, ~1 hour)

Prerequisite: none. Independent of Phase 1A — can be done in either order.

### 0a. Chapter/section menu tooltips
Every menu item in the collapsible navigation gets a `title` attribute with a 1-2 sentence descriptive summary. Content source: chapter opening paragraphs + Bruce's existing summaries.

Example menu tooltips:
- **Title Page** → "Cover, title, and the opening line."
- **How to Evaluate This Book with AI** → "Instructions for using an AI assistant to fact-check this book's scientific claims."
- **Guided Deduction** → "Part I: The story — how one team's work converged on a technology that doesn't officially exist."
- **The Demonstration** → "What happens when you drive a quantum substrate past the edge of chaos."
- **Genesis: The Edge of Chaos** → "The physics of how a self-organizing system crosses the threshold into life."
- **The Magnetosphere** → "Earth's magnetic field as a habitat — plasma sheets, current layers, and billions of years of stability."
- etc. (~30 menu items total)

### 0b. Lower menu bar control tooltips
Each control gets a `title` attribute:
- **Expand All** → "Open all chapters and sections at once"
- **AI Eval** → "Jump to instructions for evaluating this book with an AI assistant"
- **Back** → "Return to where you were reading before following a link"
- **Top** → "Scroll to the top of the page"
- **§** → "Copy a direct link to this section"
- **Quick-jump links** (Intro, Deduction, Evidence, Forgiveness) → "Jump to [Part Name]"
- **Breadcrumb** → "Your current location in the book"

### 0c. Implementation
- Menu tooltips: inject `title` attributes during `collapse_chapters()` in preprocess.py, reading from a new `menu-tooltips.yaml` or hardcoded dict
- Control tooltips: add `title` attributes directly in reader.js where elements are created
- Hover IDs not needed for these (they're navigation, not content)

**Note:** The science-only governing rule (Rule 1) applies to `\hovertip{}` content popups, NOT to menu tooltips. Menu tooltips naturally describe chapters which contain story — that's their job.

**Mobile limitation:** Native `title` attributes don't display on most mobile browsers (no hover event). Accept as desktop-only, or implement custom tooltip panels using the same mechanism as hover-terms. Desktop-only is acceptable for initial deployment; revisit if mobile analytics warrant.

**Gate 0:** All menu items and controls show tooltips on desktop hover. No interference with existing hover-term panels.

---

## Phase 1A: Definitions + Hovertip Calls (Generator task, ~1.5 hours)

### 1A-1. Hover ID infrastructure
- Add `data-hover-id` attribute emission to `hover_replace()` in preprocess.py (~2 lines)
- Add ID footer to `showPanel()` in reader.js (~5 lines), gated on absence of `final-build` class on `<body>`
- Ensure preprocess.py adds `class="final-build"` to `<body>` when `\FINAL` is defined
- Style: `font-size: 0.7em; color: #999; margin-top: 0.5em; font-family: monospace;`

### 1A-2. Extend hover-definitions.yaml
- Add all new Tier 1 terms (20 new definitions)
- Add Tier 2 high-priority terms (11 new definitions)
- Each definition: ≤50 words, clear to target reading level
- Format: plain string for most; dict with `text` + `target` for terms with a natural go-to section

### 1A-3. Add \hovertip{} calls to The Stack
Currently ZERO. Add: stack, self-maintaining structure, self-organizes, topological wormhole, two dimensions, threshold.
Popup content = p2 level (one step deeper than p1 prose).

### 1A-4. Add \hovertip{} calls to hook.tex
Currently 2. Add: quantum computer, master keys, Universal Declaration of Human Rights.
Popup content = p2 level.

### 1A-5. Add \hovertip{} calls to summary.tex
Currently 14. Add: DARPA, Five Eyes, GCHQ, public-key cryptography, dual use, confabulation, falsifiable, Dunning-Kruger effect, Bletchley Park, convergence, soliton.
Popup content = p3 level.
**Check:** Under Rule 3, verify which of the existing 14 terms now have an earlier first occurrence in hook/Stack. Those become `<em>` in summary — confirm this is acceptable.

### 1A-6. PDF footnote decision (BRUCE INPUT NEEDED)
Adding ~70 `\hovertip{}` calls = ~70 new PDF footnotes. Options:
1. All hovertips footnote in PDF (simple, possibly cluttered)
2. Create `\hovertiphtml{}` variant — HTML-only, no PDF footnote — for p3 chapter terms
3. Cap total PDF footnotes at ~40 (prioritize p1+p2, skip most p3)

**Recommendation:** Option 2. p1/p2 readers benefit from footnotes. p3 readers are technically trained and don't need them.

**BLOCKER for Phase 2.** Generator cannot proceed with p3 hovertips until Bruce decides whether to use `\hovertip{}` (with PDF footnote) or `\hovertiphtml{}` (HTML-only) for p3 terms.

**Gate 1A:** `make html` succeeds. All new hovertips render. First-occurrence rule verified (grep for duplicate `.hover-term` on same key). Hover IDs visible in dev build, absent in FINAL. Visual spot-check of 5 popups.

---

## Phase 1B: Title-Line Panel Unification (Generator task, ~1 hour)

Move the 3 hardcoded rich panels (Relinquishment, Wormholes, the Flat) from preprocess.py into hover-definitions.yaml.

### 1B-1. Extend YAML format
Add `html` key support for raw HTML + SVG content. Example:
```yaml
relinquishment:
  text: "Voluntarily surrendering power..."
  html: "<p>...</p><svg>...</svg>"
  target: "#preface"
```

### 1B-2. Update preprocess.py
- Read `html` key from YAML
- Apply `html_mod.escape()` to produce `data-hover-html` attribute
- Remove hardcoded Python for 3 title-line panels (~60 lines deleted)
- Ensure title-line terms register in `hover_seen` set

### 1B-3. Test
- Rich panels render identically to before
- First-occurrence tracking works across title-line and body hovertips
- SVG content survives HTML escaping round-trip

**Gate 1B:** Title-line panels visually identical before/after. `hover_seen` correctly prevents downstream collisions. Phase 1B is optional for initial deployment — hardcoded panels work fine. Do 1A first.

---

## Phase 2: p3 Chapter Hovertips (Generator task, ~2 hours)

### 2a. Add \hovertip{} calls to p3 chapters
Work through Tier 2 terms (items 37-95).
- First occurrence only — check main.tex reading order before placing
- Definition pitched at peer-reviewed level (p3 readers)
- Estimated: 30-40 new \hovertip{} calls across ~15 chapters

### 2b. Priority chapter ordering (by reading order, matching main.tex)
1. **Three Possibilities** (pos01) — TQNN first mention
2. **The Factoring Game** (pos09) — RSA, decoherence, Shor's algorithm, qubit
3. **The Braid** (pos10) — anyon, braiding, FQHE, quantum coherence, Chern-Simons, knot invariant, braid group
4. **The Demo** (pos11) — phase transition, edge of chaos, computational universality, Connection Machine, NV center
5. **Genesis** (pos13) — lattice gas, autocatalytic set
6. **Growing a Mind** (pos14) — cellular automaton, morphogenesis, reaction-diffusion
7. **First Light** (pos15) — Shor's algorithm (if not in pos09), parallel construction, BULLRUN, NK fitness landscape
8. **The Network** (pos20) — MOSFET, HEMT, Boolean network, Jones polynomial
9. **What Is the Flat** — plasma sheet, collisionless plasma, Schumann resonances
10. **Instantiation** (pos24) — integrated information, directed evolution
11. **The Magnetosphere** (pos32) — heliospheric current sheet, substorm, SOC, self-organized criticality
12. **Extension** (pos27) — Great Filter, Parable of the Tribes, information asymmetry
13. **Firmware Update** — room-temperature quantum coherence, power-law decoherence, Kauffman's biogenesis
14. **Remaining chapters** — 1-2 terms each

### 2c. Density check
After placing all hovertips, review each chapter. **If any single page has >4 hover-terms visible, flag for review.** Dense clusters suggest the chapter is doing its own explaining and popups add clutter, not clarity.

### 2d. Add to hover-definitions.yaml
All Tier 2 terms that received \hovertip{} calls.

**Gate 2:** `make html` succeeds. Grep confirms no term appears as `.hover-term` twice. No chapter exceeds density threshold without review. Total hovertip count: 55-75 across book.

---

## Phase 3: SVG Illustrations + Rich Panels (Generator task, ~2 hours)

### 3a. SVG candidates
Terms where a simple diagram adds understanding no words can:

| Term | SVG concept | Priority |
|------|-------------|----------|
| anyon / braiding | Two particles braiding around each other, worldlines in 2+1D | HIGH |
| phase transition | Temperature axis, sudden jump at critical point | HIGH |
| edge of chaos | Spectrum: frozen <-- edge --> chaos, with "life" arrow at edge | HIGH |
| fractional quantum Hall effect | 2D electron sheet in magnetic field, Landau levels | MEDIUM |
| self-organized criticality | Sandpile with avalanches at all scales | MEDIUM |
| NK fitness landscape | Rugged 3D terrain with peaks and valleys | MEDIUM |
| magnetosphere | Cross-section: bow shock, magnetopause, plasma sheet, tail | MEDIUM |
| Shor's algorithm | Factoring: big number → two primes, classical vs quantum time | LOW |
| reaction-diffusion | Turing spots/stripes forming from uniform initial condition | LOW |

*"technology stack" SVG removed — duplicates the LaTeX table already on the page.*

### 3b. Build rich panels
For SVG candidates: create `data-hover-html` panels with:
- 2-3 sentence explanation
- Inline SVG (≤ 15KB each)
- "Go to section →" link where applicable
- Hover ID footer (dev builds only)

### 3c. Panel sizing
Current: 400px x 300px. Rich panels with SVG may need 500px x 400px. Test and adjust `max-width` / `max-height` in html.css.

**Gate 3:** All SVG panels render correctly. Touch-friendly on mobile (600px breakpoint). No panel clips or overflows.

---

## Phase 4: QA + Polish (Generator task, ~1 hour)

### 4a. Puppeteer automated checks
- Every `.hover-term` has either `data-hover` or `data-hover-html`
- Every `.hover-term` has `data-hover-id`
- No term appears as `.hover-term` more than once (first-occurrence rule)
- All `target` links resolve to existing anchors
- Panel doesn't overflow viewport on 375px-wide screen
- Hover ID footer visible in dev build, absent in FINAL build
- Copy Prompt buttons still have working popups (regression check)

### 4b. Content review
- Every popup is SCIENCE or TEXT-STACK, never STORY
- p1 popups contain p2-level language
- p2 popups contain p3-level language
- p3 popups contain peer-reviewed definitions
- No popup references characters, plot events, or personal narrative

### 4c. Density review
- Check chapters with highest hovertip count
- Flag any page with >4 visible hover-terms for Bruce review

### 4d. Maintenance documentation
- Update hover-definitions.yaml header comment with term count
- Add source tracking: for terms whose definition draws from a specific chapter, note the source

**Gate 4:** Full build clean. Puppeteer QA passes. Bruce visual review.

---

## Scope + Resource Budget

| Metric | Value |
|--------|-------|
| Total terms (final target) | 75-95 |
| Currently defined | 16 |
| Net new definitions | 59-79 |
| New \hovertip{} calls | ~60 across ~20 files |
| New SVG illustrations | 6-9 |
| Estimated YAML size | 300-400 lines |
| Generator phases | 4 (1A+1B can be done in 1 session, 2-4 in 1-2 more) |

---

## Story-Content Exclusion List

These terms appear in the book but are STORY, not SCIENCE. **No popups.**
Bruce may add some manually — that's his call.

- David Lane / Healer (character)
- Bruce Stephenson (character)
- COWS (organization — story, not science)
- Srebrenica, Bosnia, K2 (places/events)
- Tony Tether (person)
- The walk-out, the confession (plot events)
- IRA sniper attack, Sydney Olympics (story)
- HALO jump (military technique — story context, not science)
- special forces (story)

## Borderline Terms (Bruce decides)

These are both story and science. The plan defaults to SCIENCE-ONLY popup content:

| Term | Science dimension (popup-eligible) | Story dimension (skip) |
|------|-----------------------------------|----------------------|
| Guardian / Aurasys | Substrate physics, TQNN architecture, magnetospheric habitat | Character, motivations, ethical choices, history |
| relinquishment | Bill Joy's 2000 essay, ethical framework concept | The act itself in the story |
| master keys | Cryptographic key hierarchy, what they control | The moment of surrender |
| UDHR | The document, its 30 articles, its 1948 origin | Why the team chose it |
| Three Possibilities A/B/C | Structural framework for evaluating claims | — |
| "forgiveness > permission" | — | Thematic through-line |

---

## Verification

1. `grep -rc 'hovertip' manuscript/ --include='*.tex'` — count before and after each phase
2. `wc -l build/hover-definitions.yaml` — track growth
3. `make html && puppeteer QA` — every phase gate
4. Manual review: open HTML, hover 10 random terms, verify p-level escalation
5. Confirm: zero story-only popups in final build
6. Confirm: hover IDs visible in dev, stripped in FINAL
7. Confirm: no chapter exceeds density threshold without review

---

## Annealing Record

### Pass 1 (HIGH): First-occurrence collision
The first-occurrence rule conflicts with p-level escalation when the same term appears at multiple p-levels. If "wormholes" gets a \hovertip{} in both The Stack (p1) and summary (p2), only the first fires. The p2→p3 bridge is lost.

**Fix:** Added Governing Rule 3 — one hovertip per term, first occurrence wins. Popup bridges from that location. Later appearances become `<em>`. Removed duplicate term entries from Tier 1 inventory. Added corollary about title-line panels.

### Pass 2 (MEDIUM): PDF footnote explosion
~70 new \hovertip{} calls = ~70 new PDF footnotes. Dense chapters could have 5-10 footnotes per page, degrading print experience.

**Fix:** Added Phase 1A-6 decision point with 3 options. Recommended Option 2 (`\hovertiphtml{}` variant for p3 terms). Requires Bruce input before Phase 2.

### Pass 3 (MEDIUM): Story content leaking into "science" popups
Several proposed popups leaked story content: COWS ("the faction who walked it out"), HALO jump (military technique), UDHR ("Guardian's ethical framework"), master keys ("surrendering them = permanent").

**Fix:** Removed COWS and HALO from Tier 1. Rewrote popup sketches for UDHR and master keys to pure science/document content. Audited all sketches against governing rule.

### Pass 4 (MEDIUM): Phase 1e underscoped
Moving hardcoded title-line panels to YAML requires YAML format extension (`html` key), preprocess.py refactoring (~50 lines), and HTML escaping pipeline testing. Bigger than a configuration change.

**Fix:** Split Phase 1 into 1A (definitions + hovertip calls) and 1B (title-line panel unification). Independent gates. 1B is optional — hardcoded panels work fine. Do 1A first.

### Pass 5 (LOW): Bookkeeping
- Removed "technology stack" SVG (duplicates existing LaTeX table)
- Fixed YAML size estimate (200→300-400 lines)
- Noted Phase 2 ordering must follow main.tex include order, not edit order
- Clarified phase/tier mapping (Phase 1A = Tier 1 only, Phase 2 = Tier 2)
- Added density check (>4 hover-terms per page = flag for review)
- Cross-referenced nav bar tooltips as out-of-scope
- Cross-referenced Copy Prompt popups as already done

### Pass 6 (LOW): Hover ID system
Bruce requested UIDs for referencing popups in feedback. Added `data-hover-id` attribute (all builds) + visible `[id]` footer (dev builds only, stripped in FINAL). ~7 lines of implementation. Added to Phase 1A as infrastructure item.

### Pass 7 (LOW): Final polish
- Fixed missing Phase 1A section header (formatting error from edit)
- Mobile `title` attributes don't work — noted as desktop-only limitation, not falsely claimed via long-press
- Clarified governing rule scope: science-only applies to `\hovertip{}` popups, NOT menu tooltips (which naturally describe story-containing chapters)
- Marked Phase 1A-6 (PDF footnote decision) as explicit BLOCKER for Phase 2
- Changed "parallel" to "independent" for Phase 0 / Phase 1A relationship (one Generator, sequential work)
- Fixed verification grep syntax (`**` requires globstar; use `grep -rc` instead)

### Convergence
7 passes. Amplitude well below threshold — Pass 7 was formatting, wording, and one honest limitation disclosure. No structural, medium, or design issues remain unfixed.

**Confidence: 9/10.** First-occurrence collision resolved cleanly. PDF footnote question flagged for Bruce (BLOCKER). Story-content leaks caught and fixed. Hover ID system adds authoring ergonomics at negligible cost. Mobile tooltip limitation honestly disclosed. Remaining 1/10: actual popup density in The Braid and The Demo chapters — only visual testing reveals whether it helps or clutters.
