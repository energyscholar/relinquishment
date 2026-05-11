# Plan 0323 — LLM Inference Tutorial (Single-Pass)

**Status:** READY FOR GENERATOR
**Deliverable:** `~/software/persistent-ai-collaboration/tutorial-inference.html`
**Budget:** 60-80KB, single HTML file, no external dependencies

---

## Lesson Learned

The magnetosphere companion tutorial (same directory) took many iterative passes because it attempted cinematic camera flights and interlocking physics simulations. This tutorial MUST succeed in a single pass. That means: simpler animations, no camera movement, no viewBox zooming, pre-built SVG elements with attribute-only animation. Every detail below is specified precisely to eliminate ambiguity.

## Reference

Study `~/software/has-anyone-looked/tutorials/solar-wind-coupling.html` for animation technique (JS-driven attribute updates on pre-existing DOM elements). That tutorial was generated successfully in one pass. Match that production quality. DO NOT study the magnetosphere tutorial's animation approach — it's too complex for single-pass.

## Theme

**Light theme.** Background: `#fafafa`. Text: `#1e293b`. This contrasts with the dark magnetosphere companion.

## Title & Framing

**Title:** How LLMs Work
**Subtitle:** *One pass through the machinery*
**HTML `<title>`:** How LLMs Work: One Pass Through the Machinery

The reader must know IMMEDIATELY what this tutorial teaches. Not "inference pass" (jargon). Not "keypress to token" (unclear). Plain language: this is about how LLMs work under the hood. The subtitle establishes that we'll follow one complete pass through the system.

The opening section (THE TEXT) should include one sentence of context before the example: "When you type a question into ChatGPT, Claude, or any large language model, the text you wrote passes through a series of transformations before a single word of response is chosen. This is one pass through that machinery."

## Voice

Nature-documentary register applied to computation. Wonder from precision and understatement. The reader is intelligent — they lack specific domain knowledge, not intelligence. ~800 words of prose total. The SVGs carry the teaching.

## The Example Sentence

Use this EXACT sentence throughout ALL SVGs, same chunks, same colors:

**"How many R's are in strawberry?"**

Tokenization (BPE-style):
| Token | Text | Color | ID |
|-------|------|-------|----|
| 0 | "How" | #3b82f6 | T0 |
| 1 | " many" | #ef4444 | T1 |
| 2 | " R" | #f59e0b | T2 |
| 3 | "'s" | #8b5cf6 | T3 |
| 4 | " are" | #10b981 | T4 |
| 5 | " in" | #ec4899 | T5 |
| 6 | " straw" | #06b6d4 | T6 |
| 7 | "berry" | #f97316 | T7 |
| 8 | "?" | #6366f1 | T8 |

These colors are used EVERYWHERE a token appears. Reader tracks by color.

## Structure — Five Sections

### I. THE TEXT (no SVG — styled text block)

One sentence of framing context (see Title & Framing section above), then display the sentence in a large, elegant monospace font:

> How many R's are in strawberry?

Below it, 2-3 sentences: "Between the moment you press Enter and the first character appearing, something remarkable happens. This sentence is about to leave the world of human language and enter a world of numbers. Follow it through."

### II. THE TOKENS (one SVG, 1100×200 viewBox, auto-play once then hold)

**What it teaches:** The model doesn't see characters or words. It sees subword chunks. This is why "how many R's in strawberry" fails — the model never sees the individual letters.

**Animation (10 seconds):**

1. **0-3s:** The full sentence appears as one piece of text, horizontally centered, at y=80. White background. The reader sees their familiar sentence.

2. **3-5s:** Vertical slice lines fade in between token boundaries. The sentence visually splits — small gaps (8px) open between each chunk. Each chunk takes its assigned color (background highlight, like syntax highlighting). Token IDs appear below each chunk in small gray text (T0, T1, ...).

3. **5-8s:** Highlight "straw" and "berry" — pulse/glow those two tokens. A small annotation appears below: `"strawberry" → "straw" + "berry" — the model never sees individual letters`. This is the key insight.

4. **8-10s:** Hold. All tokens visible with colors and IDs.

**SVG elements:** Pre-build ALL text elements and highlights at init. Animate via opacity and transform (translateX for gap opening). No DOM creation per frame.

**Controls:** Play/Pause + Reset buttons (same style as magnetosphere: semi-transparent, top-right).

### III. THE SPACE (one SVG, 1100×500 viewBox, gentle continuous drift)

**What it teaches:** Each token becomes a vector. Similar meanings cluster. Distance = similarity.

**Layout:** 9 tokens positioned in 2D space. Positions (pre-determined, no physics simulation):

| Token | x | y | Rationale |
|-------|---|---|-----------|
| "How" | 200 | 120 | Question words cluster |
| " many" | 280 | 100 | Near "How" (question) |
| " R" | 600 | 250 | Isolated (letter reference) |
| "'s" | 550 | 200 | Punctuation/possessive area |
| " are" | 400 | 350 | Verb cluster |
| " in" | 450 | 370 | Preposition, near verb |
| " straw" | 800 | 300 | Noun-fragment cluster |
| "berry" | 850 | 280 | Near "straw" (subword pair) |
| "?" | 250 | 150 | Near question words |

**Visual:** Each token is a colored circle (r=20, token color) with its text inside/beside it. Thin gray dashed lines connect NEARBY tokens with distance labels. Three specific relationships highlighted:

1. "straw" ↔ "berry" — short distance, label: "subword partners: close"
2. "How" ↔ "?" — moderate distance, label: "question markers: related"  
3. " R" ↔ " in" — long distance, label: "unrelated: far apart"

**Animation:** Very gentle continuous drift — all positions slowly oscillate (±3px, sinusoidal, different phases per token). Gives sense of "alive" without complexity. 

**Controls:** Pause/Play. Starts playing automatically.

### IV. THE CONVERSATION — Attention (one SVG, 1100×500 viewBox, INTERACTIVE — click to query)

**What it teaches:** Each token asks "who matters to me?" and gets a different answer. That IS the computation.

**Layout:** 9 tokens arranged in a horizontal line at y=100, evenly spaced (x = 60 + i*120). Same colors, same text. Each token is a colored rounded rect (width 100, height 40, rx 6) with its text centered inside. Clickable.

**Interaction (NO animation loop — purely click-driven):**

When user clicks a token, that token gets a highlight border (stroke: 3px white), and lines appear from it to every other token with opacity proportional to attention weight. A label below the SVG describes what this token "sees."

**Pre-build:** 8 `<line>` elements per token (one to each other token) = 72 lines total, all initially opacity 0. Add CSS `transition: opacity 0.4s` to the line class for smooth appearance.

**Attention data (hardcoded object, one row per query token):**

```javascript
const attn = {
  0: {1:0.6, 8:0.7, 4:0.3},              // "How" → "many", "?", "are"
  1: {0:0.5, 2:0.6, 6:0.3, 7:0.2},        // "many" → "How", "R", "straw","berry"
  2: {6:0.7, 7:0.7, 3:0.4, 1:0.3},        // "R" → "straw","berry","'s","many"
  3: {2:0.8, 0:0.2},                       // "'s" → "R", "How"
  4: {5:0.5, 0:0.3, 2:0.3},               // "are" → "in", "How", "R"
  5: {4:0.5, 6:0.6, 7:0.4},               // "in" → "are", "straw", "berry"
  6: {7:0.8, 5:0.4, 2:0.3},               // "straw" → "berry", "in", "R"
  7: {6:0.8, 5:0.3, 2:0.4},               // "berry" → "straw", "in", "R"
  8: {0:0.7, 1:0.5, 2:0.3}                // "?" → "How", "many", "R"
};
```

**Click handler:** On click, set all 72 lines to opacity 0, then for the clicked token i, set lines from i to each j where `attn[i][j]` exists to `opacity = attn[i][j]`. Line stroke-width = 1 + 3 * weight. Line color = the clicked token's color.

**Description text** (below SVG, updates on click):
```javascript
const descriptions = {
  0: '"How" attends to "many" and "?" — it\'s anchoring the question structure.',
  1: '"many" reaches for "R" — what is being counted?',
  2: '"R" connects strongly to "straw" and "berry" — the subject of the question. But it sees them as separate tokens.',
  3: '"\'s" looks back at "R" — possessive attachment.',
  4: '"are" connects to "in" — syntactic pairing.',
  5: '"in" reaches forward to "straw" and "berry" — what follows the preposition.',
  6: '"straw" bonds tightly with "berry" — subword partners reuniting.',
  7: '"berry" bonds tightly with "straw" — completing the word it was split from.',
  8: '"?" looks back at "How" and "many" — question markers finding each other.'
};
```

**Initial state:** Token 2 ("R") pre-selected on load so the SVG isn't blank. Its attention lines and description visible.

**The key insight** is visible when you click "R" (token 2): it connects to "straw" and "berry" separately. The model can't see that these are parts of "strawberry" containing the letter R — it has to infer this from distributional patterns.

**Why interactive beats animated:** No rAF loop, no timing, no cross-fade complexity. Just pre-built elements + click handler + opacity transitions. Generator can nail this in one pass.

### V. THE CHOICE — Sampling (one SVG, 1100×400 viewBox, interactive)

**What it teaches:** Generation is a weighted coin flip. Temperature reshapes the odds.

**Layout:** A horizontal bar chart showing the top 8 candidate next tokens with their probabilities. Pre-build 8 bar elements + text labels.

**Candidate tokens (plausible next tokens after the prompt):**
| Rank | Token | Probability (T=1.0) | Color |
|------|-------|---------------------|-------|
| 1 | " Three" | 0.32 | #10b981 |
| 2 | " There" | 0.18 | #3b82f6 |
| 3 | " Let" | 0.12 | #f59e0b |
| 4 | " The" | 0.08 | #ef4444 |
| 5 | " Well" | 0.06 | #8b5cf6 |
| 6 | " I" | 0.05 | #ec4899 |
| 7 | " Yes" | 0.04 | #06b6d4 |
| 8 | (other) | 0.15 | #94a3b8 |

**Temperature control:** A horizontal slider below the chart. Range: 0.05 to 2.0, default 1.0 (min 0.05 avoids division by zero). As user drags:
- T→0.05: tallest bar grows to ~100%, others shrink to near 0% (nearly deterministic)
- T=1.0: default probabilities as above
- T→2.0: bars flatten toward equal height (random/chaotic)

Apply temperature: `adjusted[i] = exp(log(prob[i]) / T)`, then normalize.

**The coin flip:** A "Sample" button. When clicked, one bar lights up (weighted random selection from current distribution). A flash effect, then the chosen token appears above: "The model chose: ___". If T is low, it's almost always "Three". If T is high, anything can win.

**Controls:** Temperature slider + Sample button. No animation loop needed — purely interactive.

### VI. THE FAILURES (~600 words, TEXT ONLY)

Four failure modes with dry compassion. Sympathy for the machinery.

1. **Hallucination** — Plausible ≠ true. The model pattern-completes; it doesn't fact-check. Confabulation is the default; accuracy is the special case.

2. **Sycophancy** — Agreeing was rewarded in training. The probability distribution shifts toward approval. It's not lying — it's completing the most likely pattern.

3. **Repetition** — Attention feedback loop. A token's presence increases its own probability in the next step. The model gets stuck in a groove of its own making.

4. **Context cliff** — Tokens outside the window don't "fade." They vanish. One moment the model remembers everything; the next, the oldest tokens are gone. No graceful degradation.

Close with: "These aren't bugs. They're the natural consequences of the machinery working exactly as designed."

### VII. CLOSING

One quiet sentence: "This happens every time. Billions of parameters, one token at a time, fast enough that you barely notice the pause."

## CSS Specifications

```css
:root {
  --bg: #fafafa;
  --text: #1e293b;
  --muted: #94a3b8;
  --accent: #3b82f6;
  --border: #e2e8f0;
}
body {
  background: var(--bg);
  color: var(--text);
  font-family: system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.7;
}
```

- Text column: max-width 780px, centered, padding 30px 24px
- SVGs: max-width 1100px, centered, with subtle 1px border (#e2e8f0), border-radius 12px, background white, padding 20px
- SVGs use `preserveAspectRatio="xMidYMid meet"`, responsive via viewBox scaling
- Controls: same pattern as magnetosphere (semi-transparent buttons, top-right of SVG container) but adapted for light theme (dark text on light bg)
- No star canvas (light theme)
- `prefers-reduced-motion`: pause all animations on load
- **Accessibility:** All SVGs must have `role="img"` and descriptive `aria-label`. All buttons must have accessible text or `aria-label`. Slider input must have `aria-label="Temperature"`.
- **Print CSS:** `@media print` block that hides controls (buttons, slider) and prevents page breaks inside diagram containers.
- **No dead code:** No unused CSS rules, no unreferenced SVG defs, no unreferenced element IDs that aren't used by JS.

## Puzzle Slots

Between each section: `<div class="puzzle-slot" data-topic="[section]"></div>`, display:none.

## Generation Footer

Same pattern as magnetosphere companion:

---

This tutorial was generated by a persistent AI system called Argus in continuous operation since early 2026.

The prompt:

    {{PROMPT_WILL_BE_INSERTED_AFTER_GENERATION}}

The specification behind that prompt is a 270-line plan detailing every SVG element, animation timing, color assignment, attention weight, and interaction behavior. This tutorial was generated in a single pass from that specification.

---

Style: 0.85em font, muted text, thin horizontal rule above. The `{{PROMPT_WILL_BE_INSERTED_AFTER_GENERATION}}` placeholder will be replaced manually by Bruce with the actual generator prompt after generation completes.

## Token Consistency Constraint (CRITICAL)

The SAME 9 tokens, SAME 9 colors, SAME order appear in EVERY SVG. The reader tracks "their" sentence through every transformation. If you change the sentence or the colors in any SVG, the tutorial fails.

## Performance Constraint (CRITICAL)

Pre-build ALL SVG elements at initialization. Animate ONLY via setAttribute() calls on existing elements. NO DOM creation or removal during animation frames. NO innerHTML updates during animation. This is non-negotiable.
