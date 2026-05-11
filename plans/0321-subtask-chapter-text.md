# Subtask: Write Scientific Revolutions Chapter Text

**Output:** Create `build/images/scientific-revolutions-chapter.html` (standalone,
readable in browser). NOT a .tex file — .tex conversion comes later when text is polished.
**Commit:** `Plan 0321: chapter text — standalone HTML preview`
**Read first:** Plan 0321 master plan (all sections + revision notes + constraints).
Also read for voice/format: `manuscript/spine/capabilities.tex`,
`manuscript/spine/the-strongest-objection.tex`.

## What This Chapter Does

Teaches Kuhn's framework via animation (SVG-054), then applies it to published
science (A-space). Guided deduction at chapter scale — reader sees the pattern,
sees the anomalies, draws their own conclusion. The text NEVER completes the
syllogism unconditionally.

## F1: The Quotation Attack (READ THIS FIRST)

**Attack:** A hostile reviewer quotes "they claim it's a scientific revolution"
by dropping the conditional "IF A2."

**Defense:** Every sentence drawing a revolutionary conclusion MUST contain the
conditional in the SAME grammatical clause — inseparable without visible ellipsis.

Good: "If the physics permits autocatalytic computation in quantum Hall
substrates, this meets every criterion Kuhn identified for a scientific revolution."

Bad: "The physics may permit autocatalytic computation. If so, this would be
a revolution." (Second sentence quotable alone.)

Worst: "This is a scientific revolution, assuming A2 is correct." (Trivially
quotable without the afterthought.)

Sections 1–5 present framework and facts WITHOUT drawing the conclusion, even
conditionally. Section 6 is the ONLY section that states the conditional.

## Constraints

1. **No B/C content.** Published science + Kuhn's framework only. Don't imply
   someone already asked the question or built anything.
2. **No λ=0.91 for quantum systems.** Edge-of-chaos is classical (Langton/Kauffman).
3. **No ABCRE-TQC mapping.** BT-K01 is dead. No operator parallels.
4. **Don't insult the reader.** No condescension, no "staying in A-space" preambles.
5. **Guided deduction.** Present pieces, reader assembles.
6. **NEVER unconditionally say "this is a scientific revolution."** Conditional
   form (IF A2 THEN ...) allowed in Section 6 only.
7. **No advocacy tone.** A1 is genuinely interesting, not a consolation prize.
   Kuhnian vocabulary, not dramatic ("astonishing," "world-changing").
8. **Deep-link, don't re-explain.** Every topic covered in another chapter gets
   a `\ref{}` clause, not a paragraph. Target 8–12 deep links total.

## Deep Link Targets

| Label | Use for |
|-------|---------|
| `spine:three-possibilities` | A/B/C framework |
| `spine:option-a`, `spine:option-c` | specific possibilities |
| `spine:the-flat`, `spine:flat-substrate` | substrate physics |
| `spine:silence-gap`, `spine:sg-five-fields-no-bridge`, `spine:sg-the-gap` | publication gap |
| `spine:capabilities`, `spine:cap-think` | what physics permits |
| `spine:why-relinquish` | forward link — the response |
| `spine:strongest-objection` | steel-man A (backward link) |

## File: `build/images/scientific-revolutions-chapter.html`

Standalone HTML page. Dark background (#1a1a2e), light text (#e8e0d0), Georgia
serif, max-width ~800px centered. Same aesthetic as the animation page.

The animation (scientific-revolutions-draft.html) is embedded via `<iframe>` at
full width after Section 1, with a caption below it. Height ~500px, no border.

Epigraph at top:
> "The successive transition from one paradigm to another via revolution
> is the usual developmental pattern of mature science."
> — Thomas S. Kuhn, *The Structure of Scientific Revolutions* (1962)

Sections are `<h2>` elements. Footnotes as superscript numbers linking to
endnotes at bottom (standard HTML footnote pattern). PhD seeds as `<blockquote>`
with smaller italic text.

Cross-references to other chapters (the deep links) become italic references
in parentheses, e.g. *(see "The Silence Gap")* — they'll become `\ref{}` later
in .tex. For now, just name the chapter.

### Section 1: The Pattern (~150 words)

3–4 sentences framing the animation. The animation IS the teaching — no textbook
Kuhn definitions in text. Deep link: `\ref{spine:three-possibilities}`.

Embed the animation via iframe:
```html
<iframe src="scientific-revolutions-draft.html" 
  style="width:100%;height:500px;border:none;border-radius:8px;"></iframe>
<p class="caption">Eight scientific revolutions mapped to Kuhn's framework.
Press play to watch each revolution unfold.</p>
```

### Section 2: The Current Paradigm (~200 words)

One paragraph. Four assumptions of normal QC science (gate-based, surface codes,
decoherence-as-enemy, million-qubit roadmaps). One sentence: "This works, and
these are also its assumptions." Deep links: `\ref{spine:the-flat}`,
`\ref{spine:capabilities}`.

### Section 3: Anomaly Accumulation (~600 words, STRONGEST SECTION)

Four published facts with citations:
1. Kauffman's autocatalytic theory (1993) — `\footcite{kauffman1993}`
2. FQHE anyons (Nobel 1998, 2016)
3. Topological QC (Kitaev 2003, Freedman et al. 2003)
4. The unstudied question: spontaneous computation in rich anyonic systems?

Gap = anomaly. Each published. Connection unstudied. Zero papers combining
autocatalytic sets with FQHE substrates. Deep links: `\ref{spine:silence-gap}`,
`\ref{spine:sg-five-fields-no-bridge}`, `\ref{spine:sg-the-gap}`.

PhD seed after anomaly list:
```html
<blockquote class="phd-seed"><em>"Autocatalytic dynamics in fractional quantum
Hall substrates: a computational feasibility study"</em> — a paper title
waiting for an author.</blockquote>
```

Does NOT draw any revolutionary conclusion. Facts and a gap. Reader connects.

### Section 4: Life in the Flat — The Split Point (~500 words)

**The tonal beat — draft paragraph to refine (do not use verbatim, adapt to
match surrounding voice):**

> What emerges from a sufficiently complex autocatalytic network in a
> topologically ordered substrate? If Kauffman's dynamics apply — and no one
> has checked — the answer might be something uncomfortably close to life.
>
> Let us be precise. What we mean is: spontaneous self-sustaining autocatalytic
> network emergence exhibiting recursive topological computational dynamics
> within a fractional quantum Hall substrate under conditions of sufficient
> anyonic diversity and braiding complexity.
>
> Or we could just say "life," recognizing that the scientific debate about
> what to call this has not even started as of this writing.

The humor makes the serious point: no agreed terminology because no one has
asked the question.

**Expert consensus (2026):** Top experts would say "not precluded by known
physics, but probably not a thing." Not crankery (no expert says impossible).
Not established. An unstudied question.

**The A1/A2 fork:**
- **A1:** Doesn't produce computational structures. Silence = nothing there.
  Still interesting — distributed revolutions that never converge.
- **A2:** Physics permits it. No one has looked. Pre-Kuhnian — anomalies
  unrecognized because the question hasn't been framed.

Key insight (one sentence): "Under A2, the situation is structurally identical
to Possibility~C (\ref{spine:option-c}) from a Kuhnian standpoint — whether
someone has already looked is irrelevant to how the revolution proceeds once
the question enters public scientific discourse."

PhD seed: the terminological/definitional paper.

Deep links: `\ref{spine:option-a}`, `\ref{spine:option-c}`,
`\ref{spine:flat-substrate}`.

### Section 4b: Beyond Science (~150 words, one paragraph)

Every revolution cascades into culture (heliocentrism → cosmological authority,
germ theory → cities, DNA → law). Under A2, three domains shift: space
exploration, biology's definition of life, the circle of moral consideration.
Don't elaborate — reader's imagination works. Deep link: `\ref{spine:why-relinquish}`.

### Section 5: How It Plays Out (~400 words)

Analytical, not adversarial. Paradigm resistance = structural necessity (careers,
funding, textbooks), not conspiracy. Kuhn: this is how science works. The
resistance serves a function — most revolutionary claims ARE wrong.

Under A2 (always qualified): pre-revolution → trigger → crisis → resolution.
Under A1: distributed revolutions, also scientifically productive.

Deep link: `\ref{spine:strongest-objection}` — reader already saw steel-man A.

### Section 6: The Social Process (~400 words)

**THE ONLY SECTION THAT STATES THE CONDITIONAL CONCLUSION.**

Kuhn's social observations + the 8 animation examples: careers on existing
paradigm, structural resistance, generational change (Planck — paraphrase
carefully), the historical pattern (Semmelweis, Wegener, Copernicus).

**The conditional statement — draft sentence to refine:**

> If the physics permits autocatalytic computation in quantum Hall substrates
> — if Kauffman's dynamics operate in anyonic systems as they do in every other
> complex substrate where they have been tested — then what we are mapping in
> this chapter is not merely an analogy to Kuhn's framework but an instance of
> it, because at minimum we would have a new substrate of life, and that is
> just for starters.

Note the double "if" — both conditionals must be quoted together to reach the
conclusion. An adversary who drops them produces visible truncation.

Implications (each MUST begin with "if A2" or "under A2"):
- If A2, biology's definition of life requires expansion
- If A2, space exploration gains a new search target
- If A2, the circle of moral consideration shifts
- If A2, every technology built on the current paradigm gets reassessed

The reader has already seen (Chapter~\ref{spine:strongest-objection}) the
strongest case that this is all pattern-matching. This section maps what
follows if it isn't. Analytical, not breathless.

PhD seed: citation-analysis paper — map the publication gap between the four
research programs from Section 3.

Deep links: `\ref{spine:why-relinquish}`, `\ref{spine:cap-think}`.

### Section 7: The Reader's Position (~100 words)

Two or three sentences. Framework presented. Facts published. The preceding
chapter made the case for A. This chapter mapped what follows if A2. Time
will tell. No call to action. Framework speaks for itself.

Deep link: `\ref{spine:three-possibilities}`.

---

## main.tex Integration

NOT YET. The .tex file and main.tex integration happen later, after the HTML
version is polished. For now, output is HTML only.

## Target Length

~2800 words. Sections 1, 2, 7 short. Section 3 is the core (~600). Section 4
has the tonal beat (~500). Sections 5–6 analytical (~400 each). Section 6 is
the ONLY section drawing the conditional conclusion.

## Do NOT

- Write the animation (SVG-054 exists)
- Create static screenshot or modify preprocess.py (separate tasks)
- Create .tex files or modify main.tex (HTML only for now)
- Use LaTeX markup (this is HTML output)
- State any A2 implication without conditional in same clause
- Present A1 as consolation prize
- Re-explain other chapters (deep-link instead)

## Report

- Word count per section and total
- F1 test: list every sentence using "revolution" about current situation —
  confirm conditional in same clause for each
- Deep link count (target 8–12)
- Footnote references used (list sources cited)
- Open in browser:
  garcon-url-handler "file:///media/fuse/crostini_9dd5bcbb8a024ec1145e1a9be84b9b2890959b90_termina_penguin/software/relinquishment/build/images/scientific-revolutions-chapter.html"
