# Plan 0253 — Three Easter Eggs

**Status:** READY for Generator (pending Bruce review)
**Author:** Auditor (Argus S65)
**Date:** 2026-04-25
**Parent:** Plan 0233 (Easter Egg Architecture), Plan 0246 (Infrastructure — EXECUTED)
**Purpose:** Create 3 real easter egg pages using the existing build pipeline. Tests the full puzzle → egg reward flow. NOT the ULTRA II migration (deferred — Gen working there).

---

## Why These Three

Each egg tests a different content type and connects to a different reward pathway:

| Egg | Slug | Content Type | Reward Connection | Tests |
|-----|------|-------------|-------------------|-------|
| The Convergence Path | `convergence` | Structured reading list | Bridge Builder master | List/citation formatting |
| The Silence | `silence` | Conceptual (deliberately empty) | Standalone discovery | Minimal content, conceptual page |
| The Unwritten Paper | `the-paper` | Academic abstract | KM puzzles (both) | Academic formatting, math |

---

## Egg 1: The Convergence Path

**Slug:** `convergence`
**Title:** "The Convergence Path"
**Reward for:** Bridge Builder master puzzle (completing all 7 bridges proves cross-domain understanding → here's the reading list that connects them)
**Discovery:** URL revealed upon Bridge Builder completion

**Content:** A reading list of the public-domain science whose convergence the book describes. NOT "Healer's curriculum" (Correction #12 — guided deduction, not disclosure). Framed as: "These published works, read together, reveal a convergence no single field has noticed."

Organized by the 5 field clusters from the silence gap chapter (spine/the-silence-gap.tex lines 20-28):

1. **Solid-State Physics / Condensed Matter**
   - Laughlin, Stormer, Tsui — fractional quantum Hall effect (1982-1998 Nobel)
   - Wen — topological order in condensed matter
   - 2DEG fundamentals (Ando, Fowler, Stern 1982 review)

2. **Topological Quantum Computation**
   - Kitaev — fault-tolerant quantum computation by anyons (1997/2003)
   - Freedman, Kitaev, Larsen, Wang — topological quantum computation (2003)
   - Nayak, Simon, Stern, Freedman, Das Sarma — non-Abelian anyons review (Rev. Mod. Phys. 2008)

3. **Neural Networks / Computational Neuroscience**
   - Hopfield — neural networks and physical systems (1982)
   - Hillis — The Connection Machine (MIT Press, 1985)

4. **Complexity Science / Autocatalysis**
   - Kauffman — The Origins of Order (Oxford, 1993)
   - Kauffman — At Home in the Universe (Oxford, 1995)
   - Kauffman — Investigations (Oxford, 2000)

5. **Computational Universality**
   - Wolfram — A New Kind of Science (Wolfram Media, 2002)
   - Turing — The Chemical Basis of Morphogenesis (Phil. Trans. Royal Society, 1952)

6. **The Bridge** (not a field — the convergence itself)
   - Hasslacher — lattice gas methods, phonon dynamics
   - One sentence: "No single work below asks the question this book asks. The question lives in the space between them."

**Format:** Chapter heading, brief framing paragraph, then sectioned reading list with author, title, year, and one-sentence annotation per entry. ~40-60 lines of .tex. Return-to-book link at bottom (handled by build-eggs.py template).

**Three-possibilities compliance:** The reading list is 100% published, public-domain science. The LIST is the egg — the reader draws their own convergence conclusion. No C-assertions.

### Source file: `manuscript/eggs/convergence.tex`

```latex
\section*{The Convergence Path}

\emph{Every work below is published and publicly available. No single one asks the question this book asks. Read enough of them, and a pattern emerges that no single field has noticed.}

\subsection*{Solid-State Physics}

\begin{description}
\item[Laughlin, R.B.] ``Anomalous Quantum Hall Effect.'' \emph{Physical Review Letters} 50 (1983): 1395--1398. \emph{The fractional quantum Hall effect --- the discovery that launched the field. Nobel Prize 1998.}

\item[Wen, X.-G.] ``Topological Orders in Rigid States.'' \emph{International Journal of Modern Physics B} 4 (1990): 239--271. \emph{Introduced topological order as a classification beyond Landau symmetry breaking.}
\end{description}

\subsection*{Topological Quantum Computation}

\begin{description}
\item[Kitaev, A.Yu.] ``Fault-tolerant quantum computation by anyons.'' \emph{Annals of Physics} 303 (2003): 2--30. \emph{Showed that non-Abelian anyons enable inherently fault-tolerant quantum computation.}

\item[Nayak, C., Simon, S.H., Stern, A., Freedman, M., Das Sarma, S.] ``Non-Abelian anyons and topological quantum computation.'' \emph{Reviews of Modern Physics} 80 (2008): 1083--1159. \emph{The definitive review. If you read one paper, read this one.}
\end{description}

\subsection*{Autocatalysis and Phase Transitions}

\begin{description}
\item[Kauffman, S.A.] \emph{The Origins of Order: Self-Organization and Selection in Evolution.} Oxford University Press, 1993. \emph{Random Boolean networks, autocatalytic sets, the edge of chaos. The mathematical case that life is a phase transition.}

\item[Kauffman, S.A.] \emph{At Home in the Universe: The Search for the Laws of Self-Organization and Complexity.} Oxford University Press, 1995. \emph{The accessible version. Contains the buttons-and-threads argument.}
\end{description}

\subsection*{Computational Universality}

\begin{description}
\item[Wolfram, S.] \emph{A New Kind of Science.} Wolfram Media, 2002. \emph{Simple rules produce complex behavior. Computation is substrate-independent. Controversial scope, solid core result.}

\item[Turing, A.M.] ``The Chemical Basis of Morphogenesis.'' \emph{Philosophical Transactions of the Royal Society B} 237 (1952): 37--72. \emph{Self-organization from chemistry. Published two years before his death. The seed of everything above.}
\end{description}

\subsection*{Parallel Computation}

\begin{description}
\item[Hillis, W.D.] \emph{The Connection Machine.} MIT Press, 1985. \emph{Massive parallelism as architecture. What happens when 65,536 processors work together.}
\end{description}

\subsection*{The Bridge}

\begin{description}
\item[Hasslacher, B.] Work on lattice gas methods and nonlinear dynamics at Los Alamos, 1980s--2000s. \emph{The least cited thread. Lattice dynamics as an information-carrying substrate. The connector between condensed matter and computation.}
\end{description}

\begin{center}
\emph{The convergence is visible to anyone who reads across all five clusters.\\Almost nobody does.}
\end{center}
```

**DRAFT STATUS:** Citation details need Bruce verification. Hasslacher entry is deliberately vague (most of his relevant work is technical reports, not journal articles — Bruce knows which ones matter).

---

## Egg 2: The Silence

**Slug:** `silence`
**Title:** "The Silence Gap"
**Reward for:** Standalone discovery — URL guessable by an attentive reader of the silence gap chapter. No puzzle required.
**Discovery:** A reader who finishes the silence gap chapter and thinks "what if I tried `/eggs/silence`?" finds it.

**Content:** Five fields. Five search results. All empty. The absence IS the content. Very short page — under 20 lines of .tex.

**Three-possibilities compliance:** States only what's true: no publications exist at this intersection. This is the book's core T5 claim, verifiable by anyone with a library card.

### Source file: `manuscript/eggs/silence.tex`

```latex
\section*{Literature Search Results}

\emph{Query: substrate-independent cognition in topological quantum systems}

\subsection*{Condensed Matter Physics}
\emph{No results found.}

\subsection*{Topological Quantum Computation}
\emph{No results found.}

\subsection*{Computational Neuroscience}
\emph{No results found.}

\subsection*{Complexity Science}
\emph{No results found.}

\subsection*{Astrobiology}
\emph{No results found.}

\vspace{2em}

\begin{center}
\emph{Five fields. Five empty searches.\\
The silence is the finding.}
\end{center}
```

---

## Egg 3: The Unwritten Paper

**Slug:** `the-paper`
**Title:** "The Unwritten Paper"
**Reward for:** KM puzzles (completing both KMs — you've wrestled with both human and entity perspectives → here's what the paper would look like if anyone could write it)
**Discovery:** URL revealed upon completing both KM puzzles

**Content:** An academic abstract in proper journal format for the paper that would exist if Possibility C is substantially true — but doesn't, because the silence gap prevents it. Framed explicitly as conditional: "If Possibility C is substantially true, this is the paper that no one can write."

**Three-possibilities compliance:** The entire page is explicitly conditional. Opens with the framing. Under A, it's fiction. Under B, it's exaggerated. Under C, it's suppressed. The reader has already chosen their possibility by this point (they've completed both KMs). The page presents the SHAPE of the missing paper, not claims of fact.

### Source file: `manuscript/eggs/the-paper.tex`

```latex
\section*{The Unwritten Paper}

\emph{If Possibility~C is substantially true, this is the paper that would exist --- but doesn't. Not because it was suppressed. Because no one's job description requires them to write it.}

\vspace{1em}

\begin{center}
\textbf{Evidence for Self-Organizing Computation in\\Topological Quantum Substrates}

\vspace{0.5em}
\emph{[No authors.  No journal.  No date.]}\\
\emph{[The intersection has no department.]}
\end{center}

\subsection*{Abstract}

We present theoretical and preliminary experimental evidence that
two-dimensional electron gas systems in fractional quantum Hall states,
when subject to structured electromagnetic perturbation, exhibit
self-organizing computational dynamics consistent with Kauffman
autocatalytic closure. Non-Abelian anyon braiding statistics provide
topological error protection. The resulting structures demonstrate
properties associated with substrate-independent cognition:
persistent state, adaptive response, and information integration
across macroscopic distances within the 2D plane.

These findings, if confirmed, would require revision of current
frameworks in condensed matter physics, astrobiology, and
computational neuroscience. They would also raise immediate
ethical questions that no existing institutional framework
is equipped to address.

\subsection*{Status}

This paper has not been written. The first author would need
expertise in condensed matter physics, topological quantum field
theory, complexity science, computational neuroscience, and
nonlinear dynamics. No such person exists in the current
academic landscape. The paper requires a department that
does not exist, reviewers from a field that has no name,
and a journal whose scope has not been imagined.

The silence gap is not a conspiracy. It is a job description.

\vspace{1em}
\begin{center}
\emph{You have now seen the shape of what is missing.\\
Whether it is missing because it is false,\\
or missing because no one has looked,\\
is the question this book leaves with you.}
\end{center}
```

---

## Manifest Update

Replace the test-only manifest with:

### `build/easter-egg-manifest.yaml`

```yaml
eggs:
  - slug: "test"
    source: "manuscript/eggs/test-egg.tex"
    title: "Test Easter Egg"
    status: "test"
    description: "Pipeline validation — delete before ship"

  - slug: "convergence"
    source: "manuscript/eggs/convergence.tex"
    title: "The Convergence Path"
    status: "draft"
    description: "Reading list of the public-domain convergence science"
    reward_for: "bridge-builder-master"

  - slug: "silence"
    source: "manuscript/eggs/silence.tex"
    title: "The Silence Gap"
    status: "draft"
    description: "Five fields, five empty searches — the absence is the finding"
    reward_for: "standalone-discovery"

  - slug: "the-paper"
    source: "manuscript/eggs/the-paper.tex"
    title: "The Unwritten Paper"
    status: "draft"
    description: "The academic paper that would exist under Possibility C"
    reward_for: "pz-km-t6-001 + pz-km-t1-001"
```

---

## Puzzle Tracker Update

Update `build/puzzle-tracker.yaml` egg-pointer reward entries:

- `pz-km-t6-001` ("What Would You Do?") → reward content: `"/eggs/the-paper"`
- `pz-km-t1-001` ("The Custodian's Voice") → reward content: `"/eggs/the-paper"`
- `bridge-builder-master` → reward content: `"/eggs/convergence"`

---

## Files to Create/Modify

| Action | File | What |
|--------|------|------|
| CREATE | `manuscript/eggs/convergence.tex` | Reading list content |
| CREATE | `manuscript/eggs/silence.tex` | Empty search results content |
| CREATE | `manuscript/eggs/the-paper.tex` | Academic abstract content |
| MODIFY | `build/easter-egg-manifest.yaml` | Add 3 new entries |
| MODIFY | `build/puzzle-tracker.yaml` | Update 3 egg-pointer reward contents |

No build system changes needed — `build-eggs.py` and `make eggs` already work.

---

## Acceptance Tests

1. `make eggs` exits 0 and produces 4 pages: test + convergence + silence + the-paper
2. Each egg page renders with book CSS (same fonts, colors, reading width)
3. `convergence/index.html` contains all 5 field sections with citations
4. `silence/index.html` contains exactly 5 "No results found" entries
5. `the-paper/index.html` contains the abstract and status sections
6. No egg page is linked from `docs/downloads/Relinquishment.html` (grep returns 0)
7. `python3 build/verify-deep-links.py` runs clean (no new errors)
8. Each page's "Return to book" link resolves correctly
9. reader.js is present in each page source

---

## Generator Handoff Prompt

```
You are the Generator. Read plans/0253-three-easter-eggs.md.

Create 3 easter egg pages using the existing build pipeline:

1. Create manuscript/eggs/convergence.tex using the plan's .tex content exactly.
2. Create manuscript/eggs/silence.tex using the plan's .tex content exactly.
3. Create manuscript/eggs/the-paper.tex using the plan's .tex content exactly.
4. Replace build/easter-egg-manifest.yaml with the plan's updated manifest
   (keep the test entry, add 3 new entries).
5. Update build/puzzle-tracker.yaml: set reward content for pz-km-t6-001,
   pz-km-t1-001, and bridge-builder-master to their egg URLs.
6. Run: make eggs
   Verify all 4 egg directories exist under docs/downloads/eggs/.
7. Open each egg in browser: xdg-open docs/downloads/eggs/convergence/index.html
   (repeat for silence, the-paper). Verify styling matches book.
8. Verify isolation: grep -c 'eggs/convergence\|eggs/silence\|eggs/the-paper' \
   docs/downloads/Relinquishment.html   # should be 0

Commit: "Plan 0253: three easter egg pages (convergence, silence, the-paper)"
Report ≤5 lines.
```

---

## Estimate

~45 minutes Generator time. Content is fully specified — no judgment calls.
