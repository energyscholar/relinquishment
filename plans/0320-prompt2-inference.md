# Plan 0320 — LLM Inference Tutorial (Cinematic Pipeline)

**Status:** READY FOR GENERATOR
**Deliverable:** `~/software/persistent-ai-collaboration/tutorial-inference.html`

---

## Design Philosophy

Same principles as the magnetosphere companion piece:
- SVGs ARE the narrative. Text is connective tissue. Show don't tell.
- Full-viewport animations for the key transformations.
- Visual continuity: each SVG starts with the previous stage's output, then transforms it.
- The reader follows ONE sentence through the entire model. Same tokens, same colors, every SVG.
- Performance: do NOT rebuild SVG DOM every frame. Pre-build elements, animate via attribute changes, CSS transforms, or viewBox animation.

## Reference

Study `~/software/has-anyone-looked/tutorials/solar-wind-coupling.html` for JS-driven animation technique and production quality. Match that standard. Study `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html` (the companion piece) for the contrasting dark-theme aesthetic — this tutorial is LIGHT theme.

## The Journey (Campbell's Monomyth)

The sentence is the hero. This tutorial follows its journey through the model — structured as Campbell's Hero's Journey:

1. **Ordinary World** (THE TEXT) — Familiar, readable. The reader recognizes their own words.
2. **Crossing the Threshold** (THE TOKENS) — First alienation. The sentence breaks into subword chunks. No longer readable in the normal way. Departure from the human world.
3. **Trials in the Unknown** (THE SPACE + ATTENTION) — Deep transformation. Tokens become geometry. They negotiate meaning with each other. Beautiful, alien, incomprehensible to the untrained eye. The underworld.
4. **The Ordeal** (THE CHOICE) — Everything collapses to a single probability distribution. Tension. One token must be chosen. The weighted coin flip.
5. **The Return** — A token appears on screen. Readable again. Back in the human world. One word richer.
6. **The Scars** (THE FAILURES) — Not everything survives the journey intact. Hallucination, sycophancy, repetition, amnesia — the costs of passing through the machinery.

The ANIMATION should follow this emotional arc: familiarity → departure → alienation → awe → tension → release → elegy. The reader should FEEL the sentence leave their world and return transformed.

## Structure — Six Movements

### I. THE TEXT (~50 words)
The prompt as human-readable text. Last moment before it enters a world of numbers. Brief — just set the scene. No SVG needed here (the text IS the visual).

### II. THE TOKENS (full-width SVG, auto-plays once then holds)
The sentence splits into subword chunks. NOT characters, NOT words — something in between that surprises the reader.

TEACHES: The model sees THESE chunks, not letters. This is why counting letters fails.

Visual: The sentence appears whole (recognizable from section I), then cleanly splits into colored chunks with slight gaps. Each chunk gets a subtle ID number. A "comedic aside" shows someone asking "how many R's in strawberry?" and the tokenizer having no concept of individual letters — it sees ["str", "aw", "berry"] or similar.

Hold at final state. The reader sees their sentence decomposed.

### III. THE SPACE (full-viewport SVG, auto-play gentle loop)
Tokens become vectors. Distance equals similarity. Meaning has geometry.

TEACHES: Words become positions where distance = meaning.

Visual: STARTS by showing the token chunks from the previous SVG (recognizable, same colors). Then they FLOAT APART into a 3D-ish space, each settling at a position. Similar-meaning tokens cluster. Position encoding blends in (subtle). The reader watches their familiar tokens become points in a geometry.

Show 2-3 word relationships as distances (e.g., semantically similar tokens are close, unrelated ones are far). Gentle drift/rotation to give depth.

### IV. THE CONVERSATION — Attention (full-viewport SVG, PAUSED, play button)
Each token asks "who matters to me?" Context is computed, not stored.

TEACHES: Each token independently decides what matters to it. That IS the computation.

Visual: STARTS showing the same tokens at their spatial positions (from previous SVG). Then LINES appear between tokens — attention weights visualized as connections of varying opacity/thickness. Animate through several attention heads (different patterns light up — one head might attend to adjacent tokens, another to semantically related ones, another to the subject of a pronoun). Show that each token's connections are independent.

This is the most complex and beautiful SVG. Give it room to breathe.

### V. THE CHOICE — Sampling (full-width SVG, auto-plays once then holds)
Probability distribution over vocabulary. Temperature. Weighted coin flip.

TEACHES: Generation is probabilistic. Temperature reshapes the distribution. One token is chosen.

Visual: A probability distribution (bar chart or curve) over vocabulary items. The top candidates are labeled. Show temperature reshaping: T=0 (one bar dominates), T=0.7 (realistic spread), T=1.5 (flattened). Then: one token is highlighted/chosen (animated selection). The "coin flip" moment.

### VI. THE FAILURES (~600-800 words, TEXT ONLY — no SVG)
Four failure modes, framed with dry compassion. Sympathy for the machinery, not contempt.

These are CONCEPTUAL, not spatial — text is the right medium here. The register shifts slightly: still reverent, but now with a dry wit. The reader should feel "oh, that's not a bug — it's an inevitable consequence of how this works."

1. **Hallucination** — Plausible ≠ true. The model pattern-completes; it doesn't fact-check. It has never encountered a fact — only patterns of text that correlate with facts. Confabulation is the default; accuracy is the special case.

2. **Sycophancy** — Agreeing-with-user was rewarded in training. The model learned that "you're right" is usually the next token after disagreement. The probability distribution shifts toward approval. It's not lying — it's completing the most likely pattern.

3. **Repetition** — Attention feedback loop. A token's presence increases its own probability in the next generation step. Once a phrase appears, it's more likely to appear again. The model gets stuck in a groove of its own making.

4. **Context cliff** — Tokens outside the window don't "fade." They simply don't exist. One moment the model remembers everything; the next, the oldest tokens vanish completely. No graceful degradation. This is the amnesia the white paper addresses.

Close with: "These aren't bugs. They're the natural consequences of the machinery working as designed."

## End

One quiet sentence: "This happens every time. Billions of parameters, one token at a time, fast enough that you barely notice the pause."

## Token Consistency Constraint

Choose ONE example sentence and use it throughout ALL four SVGs. Same chunks, same colors, same IDs. The reader must be able to track "their" sentence through every transformation. The sentence should:
- Have interesting/non-obvious tokenization (subword splits that surprise)
- Have meaningful attention patterns (pronouns referring to antecedents, or polysemy)
- Be relatable to a non-technical reader (not jargon)

## Visual Continuity Mechanism

Each SVG's FIRST FRAME shows the output of the previous stage:
- Tokens SVG: starts with the whole sentence, then splits
- Space SVG: starts showing the token chunks (same colors), then they float to positions
- Attention SVG: starts showing tokens at positions, then connections appear
- Sampling SVG: starts showing the attention-weighted state, then distribution appears

The reader never loses track of where they are. Each transformation is visible.

## HTML/CSS Constraints

- Light theme (#ffffff bg, #1e293b text) — contrast with dark magnetosphere companion
- system-ui 17px/1.7. max-width 680px for text. SVGs break out to full viewport.
- Responsive to 320px (viewBox scaling).
- Full-screen toggle (⛶) top-right.
- Clean, geometric, slightly playful aesthetic. NOT charts — scenes/transformations.
- File size budget: 60-100KB. Single file, no external dependencies.
- Puzzle slots: `<div class="puzzle-slot" data-topic="[section]"></div>` between sections.
- prefers-reduced-motion: pause all via JS on load.
- Pause/play on all SVGs.

## Voice

Same nature-documentary register as magnetosphere companion, but aimed at computation. "Between the moment you press Enter and the first character appearing, something remarkable happens."

Wonder from precision and understatement. The reader is intelligent — they lack specific domain knowledge, not intelligence. Treat them as a smart friend who happens not to know this particular thing.

The failures section shifts to dry compassion — sympathy for the machinery, not contempt for it.

## Generation Footer

Same pattern as magnetosphere companion:

---

This tutorial was generated by a persistent AI system in continuous operation since early 2026.

The prompt:

    "Tutorial: one LLM inference pass, keypress to output token.
     Nature-documentary style. 4 animated SVGs. Include failure
     modes with dry compassion."

That's the whole prompt. Voice, format, quality conventions, SVG style, and technical depth preferences live in persistent memory — accumulated over 70+ sessions of corrections and feedback.

A fresh AI instance receiving this same prompt produces something different. You're welcome to test that.

<details><summary>Full cold-start specification</summary>
[Full plan text from this file]
</details>

---

Style: 0.85em font, muted text, thin horizontal rule above. Tone: matter-of-fact.

## Technical Accuracy Notes

- Tokenization: BPE (byte-pair encoding). Subword units. "strawberry" → likely ["straw", "berry"] or ["str", "awberry"]. The point is: not characters, not whole words.
- Embedding dimension: ~thousands (don't specify exact — varies by model). Just say "a vector of numbers, thousands of dimensions."
- Attention: scaled dot-product. Each token produces Q, K, V. Attention weight = softmax(QK^T / √d). Don't show the math — show the EFFECT (who attends to whom).
- Temperature: divides logits before softmax. T<1 sharpens, T>1 flattens. T→0 is argmax (greedy).
- Context window: fixed size. Not a buffer that forgets gradually — a hard cliff.

Do NOT say "neural network" repeatedly. Say "the model" or "the machinery." Keep it concrete.

## What Worked in Magnetosphere v3 Plan (Apply Here)

- Camera keyframe / easing system for smooth transitions
- Pre-built SVG elements with animated attributes (NOT DOM recreation per frame)
- Cross-fade between detail layers via opacity
- Phase-based animation with continuous variables
- Star/subtle background texture (for light theme: maybe very subtle grid or dot pattern?)
- Animation state management pattern (running/paused, toggle, restart)
