# Subtask: Write Scientific Revolutions Chapter Text

**Output:** Create `manuscript/spine/scientific-revolutions.tex` + add to `main.tex`
**Commit:** `Plan 0321: chapter text — The Structure of Scientific Revolutions`
**Read first:** Plan 0321 master plan (all sections + revision notes + constraints).
Also read for voice/format: `manuscript/spine/capabilities.tex`,
`manuscript/spine/the-strongest-objection.tex`.

## What This Chapter Does

Teaches Kuhn's framework, applies it to published science, and lets the reader
draw their own conclusions. The animation (SVG-054) teaches the framework
through 8 historical examples. The chapter text applies it to the current
situation in quantum physics — entirely from published, A-space science.

## FAILURE MODE DEFENSES

These are the specific ways this chapter can go wrong. Read them before writing.

### F1: The Quotation Attack

**Attack:** A hostile reviewer quotes the chapter as "they claim it's a scientific
revolution" by dropping the conditional "IF A2."

**Defense:** Every sentence that draws a revolutionary conclusion MUST contain
the conditional in the SAME grammatical clause. Never separate "if A2" from
"then revolution" by a paragraph break, a section break, or even a sentence
boundary. The conditional and the conclusion must be grammatically inseparable
so that quoting the conclusion without the conditional requires visible
truncation (ellipsis).

**Test:** For every sentence that uses the word "revolution" applied to the
current situation: can an adversary excerpt it without the "if"? If yes, rewrite.

Good: "If the physics permits autocatalytic computation in quantum Hall
substrates, this meets every criterion Kuhn identified for a scientific revolution."
(Cannot quote the conclusion without the "if" — they're in one sentence.)

Bad: "The physics may permit autocatalytic computation. If so, this would be
a revolution." (An adversary quotes only the second sentence, which starts
with "if so" — weaker, detachable.)

Worst: "This is a scientific revolution, assuming A2 is correct."
(The qualification is an afterthought. Trivially quotable without it.)

### F2: Completing the Syllogism (Constraint #7 / Correction #12)

The chapter teaches what revolutions look like (8 examples), then presents
anomalies in current science. It NEVER says unconditionally "this is a
scientific revolution" or "we are in a paradigm shift." The reader
completes the syllogism themselves. This is guided deduction (#12).

The conditional form "IF A2, THEN this meets Kuhn's criteria" is allowed
in Section 6 only. Sections 1–5 present the framework and facts without
drawing the conclusion at all — even conditionally.

### F3: Advocacy Tone (Correction #7: Red Team First)

The chapter must not read as arguing that A2 is true. A1 must get FAIR
treatment — not as a consolation prize, but as a genuinely interesting
outcome (distributed revolutions across multiple fields that never converge).
Start at 50/50 between A1 and A2. Build nothing beyond what the evidence
supports. The reader decides.

### F4: B/C Content Leakage

When discussing "what happens when someone asks the question publicly" —
don't imply someone already has, beyond this book's existence. No references
to who may have built what. No timeline of development. No insider knowledge.
Everything in this chapter is derivable from published papers + Kuhn's book.

### F5: Excitement Escalation

The implications of A2 are enormous. The temptation is to get breathless.
Stay analytical. Let the reader get excited; the author stays cool. Use
Kuhnian vocabulary ("paradigm shift," "anomaly accumulation," "crisis phase"),
not dramatic vocabulary ("astonishing," "world-changing," "unprecedented").

### F6: Redundancy (Deep Link Instead)

Don't re-explain physics from The Flat, evidence from The Silence Gap, or
capabilities from Capabilities. Deep-link to them. This saves words AND
reduces risk of saying too much. Every topic already covered elsewhere should
be a `\ref{}` with a brief clause, not a paragraph.

### F7: ABCRE/λ=0.91 Contamination

BT-K01 is dead. No ABCRE-TQC mapping. No λ=0.91 for quantum systems.
Edge-of-chaos is Langton/Kauffman (classical). Whether a quantum analog
exists is the open question, not a claimed answer.

---

## Deep Links (use liberally throughout)

Cross-reference these labels. Each deep link replaces a paragraph of
re-explanation with a clause:

| Label | Chapter | Use for |
|-------|---------|---------|
| `spine:three-possibilities` | Three Possibilities | the A/B/C framework |
| `spine:option-a` | Three Possibilities | Possibility A specifically |
| `spine:option-c` | Three Possibilities | Possibility C specifically |
| `spine:the-flat` | The Flat | substrate physics |
| `spine:flat-substrate` | The Flat | specific substrate section |
| `spine:silence-gap` | The Silence Gap | the publication gap |
| `spine:sg-five-fields-no-bridge` | The Silence Gap | five fields, no bridge |
| `spine:sg-the-gap` | The Silence Gap | the specific gap |
| `spine:capabilities` | Capabilities | what the physics permits |
| `spine:cap-think` | Capabilities | computation question |
| `spine:why-relinquish` | Why Relinquish? | forward link to response |
| `spine:strongest-objection` | The Strongest Objection | steel-man A |
| `spine:so-the-hobbit-in-the-mirror` | The Strongest Objection | the honest self-demolition |

Pattern: `As discussed in Chapter~\ref{spine:silence-gap}, five research
programs have developed independently...` — not a re-explanation, just a pointer.

Aim for 8–12 deep links across the chapter. This makes the chapter harder to
excerpt out of context (it's visibly part of a larger argument) and saves words.

---

## File: `manuscript/spine/scientific-revolutions.tex`

### Header

```latex
\settrack{trackbridge}
% VOICE: expository/analytical — Kuhnian framework applied to published science
% Plan 0321 — The Structure of Scientific Revolutions
% CONSTRAINT #7: Never unconditionally say "this is a scientific revolution"
% Conditional form (IF A2 THEN ...) allowed in Section 6 only.

\chapter{The Structure of Scientific Revolutions}
\label{spine:scientific-revolutions}

\begin{quote}\small\textit{%
``The successive transition from one paradigm to another via revolution
is the usual developmental pattern of mature science.''%
}\par\raggedleft --- Thomas S.\ Kuhn, \emph{The Structure of Scientific
Revolutions} (1962)\end{quote}

\vspace{0.5cm}
```

Use `\footcite{key}` for citations, matching capabilities.tex pattern.
Use `\section*{Title}` with `\label{spine:sr-sectionname}` for sections.

### Section 1: The Pattern (~150 words)

\label{spine:sr-the-pattern}

3–4 sentences framing the animation. The animation IS the teaching. Text says
"here is a pattern that has repeated eight times in the history of science" and
invites the reader to watch. Reference Kuhn once. No textbook definitions.

Deep link: `\ref{spine:three-possibilities}` (the framework the reader already has).

Figure placeholder (static image doesn't exist yet):

```latex
% SVG-054: animated in HTML, static in PDF
\begin{figure}[ht]
\centering
% \includegraphics[width=\textwidth]{build/images/scientific-revolutions-static.pdf}
\caption{Eight scientific revolutions mapped to Kuhn's framework. In the
interactive edition, press play to watch each revolution unfold.}
\label{fig:kuhn-map}
\end{figure}
```

### Section 2: The Current Paradigm (~200 words)

\label{spine:sr-current-paradigm}

One paragraph. The 4 assumptions of normal quantum computing science:
- Gate-based architecture
- Surface codes for error correction
- Decoherence as the fundamental enemy
- More qubits = more capability (million-qubit roadmaps)

One sentence: "This works, and these are also its assumptions."

Deep links: `\ref{spine:the-flat}` (the substrate physics these assumptions
sit on), `\ref{spine:capabilities}` (what the physics permits).

### Section 3: Anomaly Accumulation (~600 words, STRONGEST SECTION)

\label{spine:sr-anomaly-accumulation}

The argumentative core. Four published facts:
1. Kauffman's autocatalytic theory (1993) — `\footcite{kauffman1993}`
2. FQHE anyons (Nobel 1998 Tsui/Störmer/Laughlin, 2016 Thouless/Haldane/Kosterlitz)
3. Topological QC theory (Kitaev 2003, Freedman et al. 2003)
4. The question no one has asked: does a sufficiently rich anyonic system
   spontaneously compute?

The gap between them is the anomaly. Each fact is published. The connection
is unstudied. Cite the S74 literature search: zero papers combining
autocatalytic set theory with FQHE substrates.

Deep links: `\ref{spine:silence-gap}` (the five fields),
`\ref{spine:sg-five-fields-no-bridge}` (no bridge between them),
`\ref{spine:sg-the-gap}` (the specific gap).

**PhD seed** after the anomaly list:
```latex
\begin{quote}\small
\textit{``Autocatalytic dynamics in fractional quantum Hall substrates:
a computational feasibility study''} --- a paper title waiting for an author.
\end{quote}
```

**F2 check:** This section presents facts and a gap. It does NOT draw the
conclusion that this constitutes a revolution. The reader does that.

### Section 4: Life in the Flat — The Split Point (~500 words)

\label{spine:sr-the-split-point}

**The tonal beat:** Use the word "life" — visibly catch yourself — switch to
the 20-word scientific mouthful ("spontaneous self-sustaining autocatalytic
network emergence exhibiting recursive topological computational dynamics"
or similar) — snap back to plain language: "Or we could just say 'life,'
recognizing that the scientific debate about what to call this has not even
started as of this writing." The humor makes the serious point.

**Expert consensus (2026):** Honestly state that a science-aware LLM, and
presumably top human experts, would say "not precluded by known physics,
but probably not a thing." Not crankery (no expert says impossible). Not
established (no one says probably true). An unstudied question.

**The A1/A2 fork:**
- **A1:** Autocatalytic dynamics don't produce computational structures in
  FQHE substrates. The silence gap (Chapter~\ref{spine:silence-gap}) is
  silence because there's nothing there. Still interesting — distributed
  revolutions across condensed matter, complexity theory, and quantum
  information that never converge.
- **A2:** The physics permits it. No one has looked. The anomalies exist
  but haven't been recognized as anomalies because the question hasn't
  been framed.

Key insight (one sentence): "Under A2, the situation is structurally
identical to Possibility~C (\ref{spine:option-c}) from a Kuhnian standpoint."

Deep links: `\ref{spine:option-a}`, `\ref{spine:option-c}`,
`\ref{spine:flat-substrate}`.

**PhD seed:** The terminological/definitional paper.

**F3 check:** A1 is presented as genuinely interesting, not a consolation prize.

### Section 4b: Beyond Science (~150 words, one paragraph)

Historical precedent: every scientific revolution cascades into culture
(heliocentrism → cosmological authority, germ theory → urban planning,
DNA → law and agriculture). Name three domains that would shift under A2
(space exploration, biology's definition of life, the circle of moral
consideration) without elaborating. Let the reader's imagination work.

Deep link: `\ref{spine:why-relinquish}` (forward — this connects to why
the response matters).

### Section 5: How It Plays Out (~400 words)

\label{spine:sr-how-it-plays-out}

**Tone: analytical, not adversarial.** Paradigms resist replacement by
structural necessity (careers, funding, textbooks organized around them).
Kuhn was clear: this is how science works, not a conspiracy. The resistance
serves a function — most revolutionary claims ARE wrong.

**Under A2** (always qualified):
- Pre-revolution: scattered publications, no connecting framework
- Trigger: someone asks the question publicly
- Crisis: existing paradigms face a challenge from emergence-based approaches
- Resolution: either falsification (reverts to A1) or new paradigm

**Under A1:**
- The distributed revolutions still occur — Kauffman's work finds new
  substrates, FQHE physics reveals new phenomena, TQC develops — they just
  never converge. This is also scientifically productive.

Deep link: `\ref{spine:strongest-objection}` — the reader has already seen
the strongest case for A (Chapter~\ref{spine:strongest-objection}). This
section maps what happens under each branch without repeating that argument.

### Section 6: The Social Process (~400 words)

\label{spine:sr-social-process}

**THIS IS THE ONLY SECTION WHERE THE CONDITIONAL CONCLUSION IS STATED.**

What happens socially when a paradigm shift begins? Draw on Kuhn and on
the 8 examples from the animation:
- Careers built on the existing paradigm (textbooks, funding, tenure)
- New frameworks not evaluated neutrally (structural, not conspiratorial)
- Generational change (Planck's observation — paraphrase carefully)
- The pattern: Semmelweis mocked, Wegener dismissed 50 years, Copernicus
  ignored 70. Not malice — structural.

**The conditional statement (F1 defense applies — read it):**

State directly, in one grammatically inseparable sentence: IF the physics
permits autocatalytic computation in quantum Hall substrates, then this
meets every criterion Kuhn identified for a scientific revolution — for
starters, we would have a new substrate of life, and that is just for starters.

This is a conditional. It does not claim A2 is true. It applies Kuhn's
framework to a specific hypothesis. The reader has already seen
(Chapter~\ref{spine:strongest-objection}) the strongest case that A2 is
NOT true.

**F1 test:** Can the conclusion be quoted without the "if"? If the conditional
and conclusion are in the same sentence, an adversary must use ellipsis to
separate them — which is visible truncation. Write it that way.

Implications under A2 (stated as conditional consequences):
- If A2, biology's definition of life requires expansion
- If A2, space exploration gains a new search target
- If A2, the circle of moral consideration shifts
- If A2, every technology built on the current paradigm gets reassessed

Each item must begin with "if" or "under A2" or equivalent conditional marker.
No implications stated as unconditional predictions.

Deep links: `\ref{spine:why-relinquish}` (the response to these implications),
`\ref{spine:cap-think}` (the computation question).

**PhD seed:** Citation-analysis paper — map the publication gap between the
four research programs from Section 3.

### Section 7: The Reader's Position (~100 words)

\label{spine:sr-the-readers-position}

Two or three sentences. You have the framework. The facts are published.
The preceding chapter (Chapter~\ref{spine:strongest-objection}) made the
strongest case that this is all pattern-matching. This chapter mapped what
follows if it isn't. Time will tell.

No call to action. No advocacy. The framework speaks for itself.

Deep link: `\ref{spine:three-possibilities}` (the reader's original
choice between A, B, and C).

---

## main.tex Integration

Add AFTER `the-strongest-objection` and BEFORE `interlude-07`:

```latex
\include{manuscript/spine/scientific-revolutions}   % Plan 0321
```

So lines 77–78 of main.tex become:
```latex
\include{manuscript/spine/the-strongest-objection}
\include{manuscript/spine/scientific-revolutions}   % Plan 0321
\input{manuscript/spine/interlude-07}
```

## Target Length

~2800 words total. Sections 1, 2, 7 are SHORT (framing). Section 3 is the
argumentative core (~600 words). Section 4 has the memorable tonal beat
(~500 words). Sections 5–6 are analytical (~400 words each). Section 6
(social process) is the ONLY section that draws the conditional conclusion.
It connects forward to Why Relinquish? (\ref{spine:why-relinquish}).

## Key Constraints (from Plan 0321)

1. **No B/C content.** Published science + Kuhn's framework only.
2. **No λ=0.91 for quantum systems.** Edge-of-chaos is classical.
3. **No ABCRE-TQC mapping.** BT-K01 is dead.
4. **No operator-by-operator parallels.**
5. **Don't insult the reader.**
6. **Guided deduction.** Present pieces, reader assembles.
7. **NEVER unconditionally state "this is a scientific revolution."**
   Conditional (IF A2 THEN ...) allowed in Section 6 only.

## Do NOT

- Write the animation (SVG-054 already exists)
- Create the static screenshot (separate task)
- Modify preprocess.py (HTML embed is a separate task)
- Create new LaTeX environments (use existing patterns)
- Add bibliography entries (note missing keys as `% TODO: add bib key`)
- State any implication of A2 without a conditional marker in the same clause
- Present A1 as a consolation prize (it's genuinely interesting)
- Re-explain content from other chapters (deep-link instead)

## Report

Confirm:
- Word count per section and total
- All 7 constraints honored (list each with pass/fail)
- F1 test: list every sentence that mentions "revolution" applied to current
  situation — confirm each has conditional in same clause
- Deep link count (target: 8–12)
- \footcite keys used (and any that need adding to .bib)
- `make dev` result
