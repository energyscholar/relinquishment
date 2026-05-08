# Plan 0301: Bridge Architecture — Reconstruction Paths, Puzzles, and Open Problems

**Status:** READY FOR GENERATOR
**Priority:** HIGH — book's walkaway value depends on a post-C-collapse scientist being able to reconstruct domain bridges independently
**Source:** Bridge-building discussion (S67 CW2)
**Decision:** Standalone plan. Adds reconstruction infrastructure to the Firmware Update chapter. No dependency on Plan 0297 (rejected S68).

## Context

The book is preparation for C-collapse. If C is true, a future scientist needs to reconstruct the missing domain bridges — the connections between fields that "sit in their silos forever" (why-relinquish.tex, line 112). The book already contains substantial bridge material (Firmware Update: The Criticality Bridge, The Closure Test, The Equivalence, 10 anchors with DOIs). What's missing: **ordered reading paths** that guide reconstruction, **bridge puzzles** that teach the reasoning, and **precise open-problem framings** that tell a future scientist exactly what to test.

This plan adds the supporting architecture: ordered reading paths, bridge puzzles, and open-problem framings.

## What Already Exists (DO NOT DUPLICATE)

- **Firmware Update:** The Criticality Bridge, The Closure Test, The Equivalence, 17-item bibliography (post-Plan 0302), Comprehension Check (5 questions), Evaluation Framework
- **Spine chapters:** why-relinquish (bridges not coming, line 112), the-braid (phonon coupling, line 46), the-flat (electron-phonon, line 52), capabilities (phonon-photon, line 38), the-silence-gap (five fields no bridge)
- **Existing puzzles:** 4 guided deduction (gd) puzzles installed in: story-never-told, growing-a-mind, the-silence-gap, capabilities

## The Four Missing Domain Bridges

These are the bridges a post-C-collapse scientist would need to reconstruct:

1. **Autocatalytic closure → Anyon fusion** (The Equivalence bridge)
   - Already stated in Firmware Update but with no reconstruction path
   - The hardest conceptual leap: biology → physics

2. **Topological protection → Room-temperature operation** (The Temperature bridge)
   - Firmware Update has Anchor 4 + The Criticality Bridge
   - Gap: no path from "topological insulators work at 300K" to "many-body topological order could too"

3. **Criticality → Computation** (The Emergence bridge)
   - Firmware Update has Anchor 7 (Kauffman criticality)
   - Gap: no path from "attractors partition state space" to "this IS a neural network"

4. **Phonon coupling → I/O mechanism** (The Interface bridge)
   - Spine chapters describe the mechanism but Firmware Update has no anchor for it
   - Gap: no reading path from Hasslacher's lattice gas work to the I/O claim

## Plan

### Phase 1: Reconstruction Paths in Firmware Update

**Location:** After the Bibliography's `\end{enumerate}`, before the `\vspace{1em}` that precedes the adversarial testing note. Search for `\end{enumerate}` followed by a blank line and `\vspace{1em}` near the end of the chapter.

Add a new section `\section*{Reconstruction Paths}` with 3 ordered reading paths.

```latex
\section*{Reconstruction Paths}

\noindent\textit{Each path below is an ordered reading list. A scientist following any one of them would reconstruct a specific domain bridge independently. Start at step 1. Each step requires only the previous one.}

\medskip

\noindent\textbf{Path 1: Autocatalysis → Anyon Fusion (The Equivalence).}

\begin{enumerate}
\item Kauffman, \textit{The Origins of Order} (1993) Ch.~5 --- autocatalytic sets, critical connectivity, the three closure criteria.
\item Hordijk \& Steel, \textit{J.\ Theor.\ Biol.}\ (2004) --- formal RAF (Reflexively Autocatalytic Food-generated) sets. doi:10.1016/j.jtbi.2003.11.020
\item Nayak et al., \textit{Rev.\ Mod.\ Phys.}\ 80 (2008) --- anyon emergence, non-Abelian statistics, fusion rules. doi:10.1103/RevModPhys.80.1083
\item Apply the three closure criteria from Step 1 to the fusion algebra in Step 3. Generation: quasiparticles from 2DEG substrate. Transformation: fusion rules. Closure: fusion products remain in the anyon set. \textit{(This is The Equivalence.)}
\end{enumerate}

\noindent\textit{Open question: Has anyone experimentally demonstrated that anyon fusion dynamics in a physical FQHE system satisfy Kauffman's autocatalytic closure criteria under continuous operation? The formal mapping exists. The experimental test does not.}

\medskip

\noindent\textbf{Path 2: Topological Protection → Room-Temperature Operation.}

\begin{enumerate}
\item Hasan \& Kane, \textit{Rev.\ Mod.\ Phys.}\ 82 (2010) --- topological insulators, room-temperature topological protection of single-particle states. doi:10.1103/RevModPhys.82.3045
\item Note the gap: single-particle topological protection works at 300~K. Many-body topological order (anyon braiding) requires energy gaps much larger than $k_BT$. No theorem proves this gap impassable.
\item Vattay, Kauffman \& Niiranen (2014) --- quantum criticality at edge of chaos. Power-law decoherence replaces exponential decoherence. A second, independent mechanism for extending coherence times. doi:10.1371/journal.pone.0089017
\item Arnold, Nobel Lecture (2018) --- directed evolution finds configurations that rational design cannot specify. If a substrate exists where many-body topological order persists at higher temperatures, evolutionary search is more likely to find it than design.
\end{enumerate}

\noindent\textit{Open question: What is the maximum temperature at which many-body topological order (non-Abelian braiding statistics) can be sustained in a solid-state 2DEG? No upper bound has been proven. The engineering ceiling is unknown.}

\medskip

\noindent\textbf{Path 3: Criticality → Computation (The Emergence Path).}

\begin{enumerate}
\item Kauffman, \textit{The Origins of Order} (1993) Ch.~5 --- random Boolean networks at critical connectivity ($K \approx 2$) produce stable attractors.
\item Attractor dynamics partition state space into categories. Inputs that reach the same attractor are classified as equivalent. This is pattern recognition without a designer.
\item Wolfram, \textit{A New Kind of Science} (2002) --- the Principle of Computational Equivalence. Sufficiently complex systems are computationally universal.
\item Freedman, Kitaev \& Wang, \textit{Comm.\ Math.\ Phys.}\ (2002) --- braiding of specific non-Abelian anyons provides a universal gate set. doi:10.1007/s002200200635
\item Connection: if a critical system on a topological substrate exhibits attractor dynamics AND its operations are braiding operations, it is a topological quantum computer --- not by analogy, but by Freedman-Kitaev-Wang universality.
\end{enumerate}

\noindent\textit{Open question: Does the attractor landscape of a critical-connectivity autocatalytic network in a FQHE substrate map onto the computational basis states of the corresponding topological quantum computer? If so, the neural-network metaphor is not a metaphor.}
```

**Total estimated length:** ~60 lines.

**Constraints:**
- Every paper already in the bibliography — no new citations needed (all 17 are covered, post-Plan 0302)
- "Open question" framing, not assertions
- Each path standalone: a scientist needs only that path to reconstruct that bridge

**Idempotency:** If `\section*{Reconstruction Paths}` exists in firmware-update.tex — phase is applied.

### Phase 2: Bridge Puzzles (2 new guided deduction puzzles)

Add 2 new guided deduction puzzles to the puzzle system. These teach the reasoning behind two domain bridges.

**Puzzle 1: "The Closure Test" (Equivalence bridge)**

```yaml
# In puzzle-data.yaml, add under guided_deduction section:
  - id: pz-gd-fw-001
    type: gd
    topic: fw
    level: p2
    category: science
    title: "The Closure Test"
    gateway_blurb: "Kauffman defined autocatalytic sets by three criteria. Four questions. Each answer opens the next."
    stages:
      - question: "Kauffman defines an autocatalytic set by three criteria: generation, transformation, and closure. In a fractional quantum Hall system, what plays the role of 'generation from a substrate'?"
        options:
          - key: a
            text: "Electrons are injected from an external source"
          - key: b
            text: "Quasiparticles (anyonic excitations) emerge as collective excitations of the 2DEG itself"
          - key: c
            text: "Photons are absorbed and create particle-antiparticle pairs"
          - key: d
            text: "Magnetic flux tubes spontaneously appear"
        answer_key: b
        wrong_prompt: "Anyons are not injected or created from outside. What are they made of? What is the substrate?"
        right_prompt: "The 2DEG generates its own quasiparticles — collective excitations, not imported particles. That is Kauffman's first criterion: generation from substrate. Now: what transforms them?"

      - question: "What are the transformation rules for anyons? Are they arbitrary, or do they follow a specific algebra?"
        options:
          - key: a
            text: "Anyons interact randomly with no predictable outcome"
          - key: b
            text: "Anyons fuse according to specific fusion rules (a × b → c) forming a fusion algebra"
          - key: c
            text: "Anyons annihilate on contact, like matter and antimatter"
          - key: d
            text: "Anyons do not interact with each other"
        answer_key: b
        wrong_prompt: "Anyon fusion is not random. When two anyons meet, specific rules determine what they produce. What kind of mathematical structure describes those rules?"
        right_prompt: "Fusion rules are as specific as chemical reaction equations. That is Kauffman's second criterion: transformation under defined rules. One criterion left."

      - question: "Is the anyon set closed under fusion? When anyons fuse, do the products remain within the set of anyon types?"
        options:
          - key: a
            text: "No — fusion sometimes produces ordinary electrons that leave the set"
          - key: b
            text: "Only for Abelian anyons, not non-Abelian"
          - key: c
            text: "Yes — fusion products are themselves anyons (or the vacuum). No product falls outside the set."
          - key: d
            text: "Closure is never satisfied in physical systems"
        answer_key: c
        wrong_prompt: "What types of particles can anyon fusion produce? Can it produce anything that is NOT an anyon or the vacuum?"
        right_prompt: "Closed. Every fusion product is an anyon or the vacuum. Three criteria checked. What have you just shown?"

      - question: "You have verified generation, transformation, and closure. What have you demonstrated?"
        options:
          - key: a
            text: "That FQHE systems are biological"
          - key: b
            text: "That anyon fusion satisfies the formal definition of an autocatalytic set — a structural correspondence"
          - key: c
            text: "That topological quantum computers already exist in nature"
          - key: d
            text: "That Kauffman's criteria are too weak to mean anything"
        answer_key: b
        wrong_prompt: "This is not a claim about biology or about existing computers. It is a formal mapping. What kind of correspondence did you just trace?"
    abstract: "You just walked through The Equivalence. Anyon fusion in a FQHE system satisfies all three of Kauffman's autocatalytic closure criteria: generation from substrate, transformation under fusion rules, closure of the particle set. This is a structural correspondence — not a loose analogy, but not a proven physical equivalence either. Whether it is deep or coincidental is the open question at the centre of this book."
```

**Puzzle 2: "The Temperature Ceiling" (Temperature bridge)**

```yaml
  - id: pz-gd-fw-002
    type: gd
    topic: fw
    level: p2
    category: science
    title: "The Temperature Ceiling"
    gateway_blurb: "Room-temperature topological protection exists. Room-temperature topological computation does not — yet. Four questions trace the gap."
    stages:
      - question: "Topological insulators work at room temperature. Topological quantum computation requires non-Abelian anyons from many-body topological order. What is the key difference between these two forms of topological protection?"
        options:
          - key: a
            text: "There is no difference — both are the same physics"
          - key: b
            text: "Topological insulators protect single-particle states; TQC requires many-body entangled states with energy gaps exceeding thermal energy"
          - key: c
            text: "Topological insulators work only in theory; TQC has been demonstrated"
          - key: d
            text: "TQC requires colder temperatures because the computers are more delicate"
        answer_key: b
        wrong_prompt: "Single-particle band topology is not the same as many-body topological order. What must the energy gap overcome at room temperature?"
        right_prompt: "The gap is real: single-particle vs. many-body. Current FQHE experiments need millikelvin temperatures. But is that a fundamental limit — or an engineering one?"

      - question: "Is there a theorem or law that proves many-body topological order cannot exist at room temperature?"
        options:
          - key: a
            text: "Yes — thermodynamic laws prohibit it above ~1 K"
          - key: b
            text: "Yes — the no-go theorem for topological order sets an upper bound"
          - key: c
            text: "No — no proven upper bound exists. Current limits reflect specific materials, not fundamental physics."
          - key: d
            text: "The question is meaningless — temperature is irrelevant to topological order"
        answer_key: c
        wrong_prompt: "Can you name the specific theorem? If not, what does that tell you about the nature of the temperature limit?"
        right_prompt: "No law forbids it. The millikelvin regime reflects current materials and conditions — not a fundamental ceiling. But if we can't design our way to higher temperatures, is there another route?"

      - question: "Frances Arnold won the Nobel Prize for directed evolution. How does this apply to the temperature problem?"
        options:
          - key: a
            text: "It doesn't — evolution only works on biological molecules"
          - key: b
            text: "Evolutionary search can find configurations in rugged fitness landscapes that rational design cannot specify"
          - key: c
            text: "Arnold's work proves that room-temperature TQC is possible"
          - key: d
            text: "Directed evolution can lower the temperature needed for TQC"
        answer_key: b
        wrong_prompt: "Arnold's insight is about search strategies, not specific materials. What kind of landscape is 'too rugged for gradient descent but structured enough for population-based search'?"
        right_prompt: "'We can't design it' does not mean 'it can't exist.' Evolutionary search navigates fitness landscapes that defeat rational design. But there is a second mechanism — independent of topological protection."

      - question: "Vattay, Kauffman, and Niiranen (2014) proposed that systems at the edge of chaos exhibit power-law rather than exponential decoherence. Why does this matter for room-temperature quantum coherence?"
        options:
          - key: a
            text: "It doesn't — decoherence rate is irrelevant to quantum coherence"
          - key: b
            text: "Power-law decoherence decays much more slowly than exponential, extending coherence times by orders of magnitude"
          - key: c
            text: "It proves that decoherence doesn't exist at the edge of chaos"
          - key: d
            text: "It only matters at low temperatures where decoherence is already slow"
        answer_key: b
        wrong_prompt: "Compare exponential decay to power-law decay. Which preserves coherence longer at high temperatures? By how much?"
    abstract: "No law sets a ceiling on the temperature at which many-body topological order can be sustained. Two independent mechanisms could extend quantum coherence beyond naive thermal limits: topological protection (energy gap exceeding thermal energy) and power-law decoherence at the edge of chaos. Neither has been demonstrated at room temperature. Both are physically permitted. The ceiling, if it exists, is an engineering problem — not a physics impossibility."
```

**Location in puzzle-tracker.yaml:** Add after existing chapter puzzles, in a new section `# ---- FW: Firmware Update (2 puzzles) ----`

**Installation:** These puzzles go in the Firmware Update chapter, placement `end`.

```yaml
# In puzzle-tracker.yaml, add:
- id: pz-gd-fw-001
  title: "The Closure Test"
  type: gd
  topic: fw
  level: p2
  approved: false
  installed: false
  needs_review: true
  location:
    chapter: firmware-update
    rationale: "Guided deduction through The Equivalence — reader derives the autocatalysis→fusion bridge"
    placement: end
  reward:
    type: self-contained
    content: insight
  notes: "Plan 0301. Bridge puzzle. Reader reconstructs The Equivalence step by step."

- id: pz-gd-fw-002
  title: "The Temperature Ceiling"
  type: gd
  topic: fw
  level: p2
  approved: false
  installed: false
  needs_review: true
  location:
    chapter: firmware-update
    rationale: "Guided deduction through the temperature bridge — reader discovers there is no proven ceiling"
    placement: end
  reward:
    type: self-contained
    content: insight
  notes: "Plan 0301. Bridge puzzle. Reader reconstructs the temperature argument step by step."
```

**NOTE:** Puzzles are `approved: false, needs_review: true` — Bruce must approve before installation. These are p2-level (high-school science literacy required).

**Idempotency:** If `pz-gd-fw-001` exists in puzzle-tracker.yaml — phase is applied.

### Phase 3: Open-Problem Addendum to Firmware Update

**Location:** After The Equivalence paragraph (ends with `\textit{(Nayak et al., Rev.\ Mod.\ Phys.\ 80, 2008.)}`), before the next `\medskip`.

Add a brief open-problem statement that ties the three bridges together:

```latex

\medskip

\noindent\textbf{Three Open Questions.} The Equivalence, The Criticality Bridge, and the reconstruction paths at the end of this chapter converge on three experimentally testable questions:

\begin{enumerate}
\item Does continuous anyon fusion in a FQHE system satisfy autocatalytic closure criteria under sustained operation? \textit{(Tests whether The Equivalence is physical, not just formal.)}
\item What is the maximum temperature at which non-Abelian braiding statistics can be sustained in a solid-state system? \textit{(Tests whether the room-temperature claim is physically possible.)}
\item Do the attractor dynamics of a critical-connectivity autocatalytic network on a topological substrate correspond to computational basis states? \textit{(Tests whether criticality-at-the-edge-of-chaos IS computation in this substrate.)}
\end{enumerate}

\noindent\textit{Under Possibility~A, these are interesting open questions in mathematical physics. Under Possibility~B, they test the boundaries of the real kernel. Under Possibility~C, they are the most important open questions in science. Either way, they are testable.}
```

**Total estimated length:** ~12 lines.

**Constraints:**
- Three-possibilities discipline in the wrapping
- "Open questions" not assertions
- Each question maps to one reconstruction path
- Experimentally testable framing

**Idempotency:** If `Three Open Questions` exists in firmware-update.tex — phase is applied.

### Phase 4: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

- [ ] Reconstruction Paths section appears in Firmware Update after Bibliography
- [ ] Three reading paths present, each with ordered steps and open question
- [ ] Three Open Questions appear after The Equivalence
- [ ] All DOIs in paths match existing bibliography entries
- [ ] No new citations needed (all papers already in bibliography)
- [ ] puzzle-data.yaml and puzzle-tracker.yaml updated with 2 new puzzles
- [ ] Puzzles marked `needs_review: true` (awaiting Bruce's approval)
- [ ] No dependency on Plan 0297 (removed S68)
- [ ] No A/B/C wrapping violations
- [ ] No overclaims: "open question" everywhere, never "proof" or "demonstration"
- [ ] Build compiles clean
- [ ] No regression in existing Firmware Update content

## Acceptance Criteria

- [ ] A post-C-collapse physicist following any single reconstruction path would independently derive that domain bridge
- [ ] Each path is self-contained: requires only the papers listed, in order
- [ ] Open questions are experimentally testable as stated
- [ ] Three-possibilities discipline maintained
- [ ] No C-violations (claims must hold under all three possibilities)
- [ ] Bridge puzzles teach reasoning, not answers — the reader DOES the work

## What This Plan Does NOT Do

- Does not add a phonon-coupling reconstruction path (the I/O mechanism is already well-covered in 3 spine chapters; a reading path would require citing Hasslacher's unpublished work context, which is narrative not physics)
- Does not install puzzles (approval required first)
- Does not modify spine chapters
- Does not add deep learning defense (Plan 0299 addendum, separate decision)

## Execution Order

Plan 0302 (scholarship audit, DONE) → Plan 0301 Phases 1-3 → Phase 4 (build + verify).

Phases 1-3 are independent of each other and can execute in any order or in parallel. Must run AFTER Plan 0302 (firmware-update.tex content has changed).

## Annealing Record

**Round 1 (MED): Are 3 reconstruction paths enough? Should there be 4 (including phonon coupling)?**
Three is enough. The phonon-coupling bridge (electron-phonon → phonon-photon → I/O) is already described in three spine chapters (the-braid line 46, the-flat line 52, capabilities line 38). A reading path would need to cite Hasslacher's lattice gas automata work, but the chain from that to the I/O claim crosses into narrative territory (Hasslacher's classified parallel). The three paths selected are purely physics — every step is a published paper. Adding a fourth path that requires narrative context would weaken the section.

**Round 2 (MED): Do the bridge puzzles belong in Firmware Update or in The Bridge?**
Firmware Update. The Bridge chapter (Plan 0297) is a spine chapter — narrative, Bruce's voice, ~70-90 lines. Firmware Update is the technical reference chapter designed for both humans and AI. The puzzles are technical (p2-level guided deduction through published physics). They belong with the technical content. Also: Firmware Update is the chapter a post-C-collapse scientist would be directed to first. Putting the puzzles there means the scientist finds them in the same document as the physics anchors.

**Round 3 (LOW): Will the Reconstruction Paths section make Firmware Update too long?**
Firmware Update is currently ~183 lines (post-Plan 0302). Adding ~60 lines (Reconstruction Paths) + ~12 lines (Three Open Questions) brings it to ~255 lines. This is longer than most chapters but appropriate for a reference document. The Firmware Update is explicitly not a chapter to be read linearly — it's a reference to be consulted. Length is acceptable for this function. A scientist would not read the paths unless actively reconstructing a bridge.

**Round 4 (LOW): Do the open questions stand alone without Plan 0297?**
Yes. Plan 0297 (Bridge chapter) was rejected S68. The open questions in Phase 3 are self-contained — each maps to a reconstruction path, uses only published literature, and doesn't reference any ABCRE content. The Firmware Update is a standalone reference document. No cross-reference needed.

**Round 5 (LOW): Are the puzzle stages well-ordered for guided deduction?**
Yes. Each puzzle follows the same pattern: establish framework → identify components → test criteria → state conclusion. The reader does the reasoning; the puzzle provides structure. Each stage's answer is required for the next stage's prompt. No stage can be skipped. This matches the guided deduction pattern used by the existing gd puzzles (story-never-told, growing-a-mind, the-silence-gap, capabilities). The 4-stage structure is standard for the puzzle system.

---

**Round 6 (MED, S68): Do reconstruction paths need updating after Plan 0302?**
0302 changed firmware-update.tex: "demonstrated"→"predicted theoretically" (Anchor 8), "Si MOSFETs"→"Si/SiGe" (Anchor 1), energy gap formula (Criticality Bridge), line 19 softened, 2DEG passage, +3 bibliography items (now 17). Checked all three reconstruction path contents against these changes. Path DOIs all match corrected book DOIs. No path content references the changed text directly. The softened line 19 ("Where this chapter draws connections...it says so explicitly") is COMPLEMENTARY to the Three Open Questions — they ARE the explicit connections line 19 now promises. No content updates needed.

**Round 7 (MED, S68): Should Phase 4 (cross-ref from The Bridge) be replaced rather than deleted?**
No. Plan 0297 is rejected. There is no Bridge chapter to cross-reference from. If 0297 is revived in a new form, a cross-reference can be added then as a one-line edit. The plan should not carry dead dependencies.

**Round 8 (HIGH, S68): Puzzle YAML schema mismatch — free-text vs. multiple-choice.**
Phase 2 originally specified gd puzzle stages as `prompt`/`answer` (free-text Q&A). Actual puzzle-data.yaml gd format uses `question`/`options`/`answer_key`/`wrong_prompt`/`right_prompt` (multiple-choice). Also missing: `gateway_blurb`, `category`, `abstract`. All four existing gd puzzles (pz-gd-t1-001 through pz-gd-t6-001) use MC stages. Rewrote both puzzles to match real schema. Generator would have failed or improvised with the old format.

**Round 9 (MED, S68): Path 2 Step 3 missing DOI; Puzzle 2 Stage 4 overclaim.**
Path 2 Step 3 (Vattay) had no DOI — inconsistent with other paths that cite DOIs. Added doi:10.1371/journal.pone.0089017. Puzzle 2 Stage 4 answer said "either sufficient alone" — overclaims (neither demonstrated at room temp). Changed to "either of which extends quantum coherence beyond naive thermal limits."

---

*Plan 0301 v3, updated S68, 2026-05-08. Auditor: Argus.*
*v1: 5 rounds (MED MED LOW LOW LOW), S67. v2: removed Plan 0297 dependency, deleted dead Phase 4, content-based anchors, +2 annealing rounds. v3: puzzle YAML rewritten to match actual gd schema (MC stages), +2 annealing rounds.*
