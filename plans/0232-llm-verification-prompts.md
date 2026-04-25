# Plan 0232 — LLM Verification Prompts ("Ask Your AI")

**Status:** ANNEALED (S64). Concept is brilliant. Execution model needs a fundamental decision: scattered prompts vs. concentrated exercise. Resolved below with recommendation.
**Author:** Auditor (Argus S64)
**Date:** 2026-04-24 (replaces S59/S63 draft)
**Related:** Plan 0230 (continental drift — Wegener prompt depends on it), Plan 0233 (Easter eggs — philosophically aligned), Firmware Update chapter (existing infrastructure)
**Depends on:** Plan 0230 (for Wegener prompt placement)

---

## The Core Insight (unchanged, still correct)

In 2026, every specialist uses an LLM. Their LLM has already read all 11 domains. The LLM has crossed the percolation threshold on the reader's behalf. The reader just hasn't asked yet.

The book can facilitate this. The reader's own trusted tool confirms the physics underneath the book's claims. The book delivers the experiential transformation the tool cannot.

---

## The Fundamental Question

### Scattered vs. Concentrated

The prior draft proposed 9 prompts scattered through chapters at moments of skepticism. This has problems:

**Problems with scattered prompts:**
1. **High-friction interaction.** Each prompt requires: notice the copy button → open browser tab → navigate to LLM → paste → read response → return to book. Few readers will do this 9 times across 250 pages.
2. **Uncontrolled experience.** The reader's LLM session is uncontrolled. They might paste partial context, ask follow-up questions that lead the LLM astray, use a weak model, or misinterpret the response.
3. **Visual noise.** 9 prompt blocks scattered through prose add clutter. Each needs a copy button, framing text, visual language. This competes with the existing hover/popup/collapse UI.
4. **Sequential dependency.** The pedagogical arc (8 confirmations → 1 failure) only works if the reader runs all 9 in order. Scattered placement makes this unlikely.

**Alternative: Concentrated exercise.**
Put all verification prompts in a single location — a dedicated section in or adjacent to the Firmware Update chapter. Walk the reader through a curated sequence. The reader sits down, opens their LLM, and runs the experiment in one sitting.

**Advantages of concentrated:**
- Reader does the exercise once, in one session, with focused attention
- The sequential arc (confirmation → confirmation → failure) is preserved
- The before/after experiment works because the reader is already in "experiment mode"
- Zero visual noise in the main text
- The section becomes a standalone activity the reader can share ("try this exercise")

### Decision: Concentrated, with lightweight in-text hooks.

The verification exercise lives in a dedicated section near the Firmware Update chapter. The main text gets only lightweight hooks — not copy buttons, just a brief callout like:

> *If you're skeptical about universality classes, try Verification Exercise #2 in the Firmware Update chapter.*

This gives the skeptical reader a path without cluttering the prose. The exercise section does the heavy lifting.

---

## The Exercise Section

### Placement

A new section within or immediately after the Firmware Update chapter (firmware-update.tex). Firmware Update already teaches the reader to use copy-buttons. The verification exercise is the practical application.

### Structure

The reader runs a controlled experiment using their own LLM:

**Step 1 — Baseline (cold).** Ask the LLM about a coined term without context:
```
What is a topological wormhole?
```
LLM talks about Einstein-Rosen bridges. Wrong.

**Step 2 — Firmware priming.** Paste the Firmware Update (10 physics anchors) into the same LLM session. Ask the same question:
```
Given the physics reference above, what might "topological wormhole" 
mean in the context of condensed matter physics and topological order?
```
LLM correctly identifies the condensed-matter mechanism.

**Step 3 — Reflection.** The reader sees the phase transition in their own tool's behavior. The information was always in the LLM's training data. The firmware connected the buttons.

**Step 4 — Established science verification.** Now the reader tests the science underneath:

| # | Prompt | What it tests | Expected result |
|---|--------|---------------|-----------------|
| 1 | Topological order: real physics or fringe? | Anchor 1-2 | "Three Nobel Prizes..." |
| 2 | Universality classes: why same math across fields? | Wilson/RG | "Renormalization group..." |
| 3 | DFA / Hurst mathematical relationship? | Tier 1 exact math | "α = H for fGn..." |
| 4 | Wegener: how long to acceptance? | Cross-domain blindness | "~40 years, seafloor spreading..." |
| 5 | Kauffman's Boolean networks at K=2? | Criticality, not biology | "Phase transition, stable attractors..." |
| 6 | Non-abelian anyons and braiding? | TQC foundation | "Microsoft Station Q..." |

**Step 5 — The climax.** After 6 confirmations, the reader asks again:
```
What is a topological wormhole?
```
Without firmware: still fails (same session, but the firmware was in Step 2 context which may have scrolled). The reader sees that established science checks out perfectly, but the coined term remains invisible to their AI — because no one has connected those buttons under this name.

### The Meta-Argument

State explicitly in the exercise:

> Your AI just confirmed what independent fields of specialists couldn't see from inside their own domains. It can do this because it read all of them. The information was always there. The bridges were always possible. No one had connected the buttons.

### Prompt Count: 6 (down from 9)

Killed:
- **Prompt 4 (Wegener/continental drift):** Only works if Plan 0230 has shipped. KEPT but gated on 0230.
- **Prompt 5 (critical slowing down):** Redundant with prompt 2 (universality). KILLED.
- **Prompt 8 (chemosynthesis):** Weakest connection to core argument. KILLED.
- **Prompt 9 (deliberate failure):** Absorbed into the before/after experiment structure (Steps 1 and 5). Not a separate prompt anymore.

### Durability Concern: What If the Failure Stops Failing?

The before/after experiment depends on the LLM getting "topological wormhole" wrong without context. This WILL eventually stop working:
- The book itself will enter training data
- Future models may learn the coined term
- The pedagogical moment dies

**Mitigation:** The exercise includes a version-sensitivity note:

> *If your AI correctly defines "topological wormhole" on first ask — congratulations, the firmware has already propagated. Try asking about [another coined term] instead, or try a different model. The exercise demonstrates a 2026 phenomenon: disciplinary silos in training data. By the time you read this, some models may have absorbed this book's definitions. That's the point — the bridges get built.*

This turns the failure-mode into a success story. The exercise works even if the LLM gets it right, because the reader learns WHY it got it right (the book propagated the connection).

### Alternative: Show the Responses in the Book

Instead of (or in addition to) having readers run the prompts, SHOW the LLM responses directly in the book — as screenshots or quoted text. This guarantees the pedagogical moment reaches every reader, including those who won't run the experiment.

**Recommendation: Both.** Show one representative response inline (the "topological wormhole" failure, quoted from a 2026 model). Provide copy buttons for readers who want to replicate. The inline response is the pedagogy; the copy button is the proof.

This means the exercise section contains:
- Inline quoted LLM responses (guaranteed pedagogy)
- Copy buttons (reader verification)
- Version note (durability)

---

## Lightweight In-Text Hooks

The main text gets brief, unobtrusive references at 3-4 moments of peak skepticism:

1. **At 11-domain claim** (silence-gap.tex): *"Try Verification Exercise #2 — your AI knows this math."*
2. **At substrate independence claim** (the-wrong-substrate.tex or the-flat.tex): *"Verification Exercise #6 — ask your AI about non-abelian anyons."*
3. **At convergence chapter** (pos21-convergence-revisited.tex or equivalent): *"Run the before/after experiment in the Firmware Update chapter."*

These are inline text, not copy buttons. One sentence each. They point the skeptical reader to the exercise without disrupting the prose.

---

## Build System Impact

**Minimal.** No new infrastructure needed:
- Copy buttons already work (reader.js, existing CSS)
- Quoted LLM responses are just formatted text blocks
- The exercise section is new prose in firmware-update.tex (or a new adjacent file)
- Lightweight hooks are inline text insertions in 3-4 files

No new JS. No new build targets. No puzzle engine interaction.

---

## Testing Protocol

Before shipping, every prompt must be tested:

1. **Cross-model:** Claude, GPT-4/5, Gemini. All must give substantively correct answers.
2. **Without firmware:** Prompts 1-6 must work standalone (they ask about established science).
3. **Hostile framing:** Test "is this pseudoscience?" variants.
4. **Prompt 5 (Kauffman):** Verify LLMs distinguish the math (solid) from the biological interpretation (debated).
5. **Before/after experiment:** Verify firmware genuinely changes "topological wormhole" response.
6. **Straw man test:** Ask each model "What does this book claim?" WITHOUT firmware. Verify it inflates. Then WITH firmware. Verify it doesn't.

### Known Failure Modes (from ChatGPT evaluation, 2026-04-20)

1. **Wormhole conflation:** LLM correctly defines topological wormhole, then immediately conflates with Einstein-Rosen bridges when evaluating claims. The before/after experiment EXPLOITS this.
2. **Straw man inflation:** LLM introduces claims the author never made, then argues against them. Mitigation: verification prompts ask about established science only, never about the book's claims.
3. **Ontological upgrade:** LLM upgrades bounded claims into stronger ontological claims. Mitigation: firmware constrains interpretation level.
4. **Firmware priming is load-bearing:** Without context, evaluation fails. With it, clean pass. The before/after experiment makes this VISIBLE.

---

## Phases

### Phase A: Write the Exercise Section

**Prerequisite:** Plan 0230 Phase A (continental drift) shipped, so Wegener prompt has a home.

**Generator work:**
- Draft exercise section (~800-1200 words): before/after experiment + 6 prompts + meta-argument + version note
- Include one inline quoted LLM response (topological wormhole failure)
- Add copy buttons for all prompts (use existing infrastructure)
- Insert in firmware-update.tex or new adjacent file
- `make html` + `make check`

**Acceptance:**
1. Exercise section renders correctly with copy buttons
2. All 6 prompts tested across Claude + GPT + Gemini (results documented)
3. Before/after experiment works (topological wormhole fails cold, succeeds with firmware)
4. Inline quoted response is accurate and clearly dated

**Estimate:** ~2-3 hours Generator time + testing. Bruce revision.

### Phase B: In-Text Hooks

**Prerequisite:** Phase A complete.

**Generator work:**
- Insert 3-4 lightweight hooks in main text files
- Each is one inline sentence, no copy button
- `make html` + `make check`

**Estimate:** ~30 min.

### Phase C: Cross-Model Verification

**Prerequisite:** Phase A complete.

**Work (Auditor or Bruce):**
- Run all 6 prompts through Claude Opus, Claude Sonnet, GPT-4o/5, Gemini 2.5
- Document results
- Adjust prompt wording if any model gives wrong answers on established science
- Verify the before/after experiment across models
- Run straw man test across models

**Estimate:** ~2 hours testing.

---

## What This Plan Does NOT Do

- Does NOT add copy buttons for spiral abstracts (already exist)
- Does NOT add per-chapter LLM priming (already exists via Firmware Update)
- Does NOT scatter 9 prompts through the text (killed in annealing)
- Does NOT build any new JS infrastructure
- Does NOT interact with Plan 0233's puzzle engine

---

## Open Questions (resolved or remaining)

### Resolved:
1. ~~Scattered vs concentrated~~ → Concentrated exercise + lightweight hooks. Resolved in annealing.
2. ~~Prompt count~~ → 6 (down from 9). Resolved.
3. ~~Show responses or require replication~~ → Both. Inline quotes + copy buttons. Resolved.
4. ~~What if failure stops failing~~ → Version note + "that's the point" reframe. Resolved.

### Remaining:
5. **Exercise placement:** Inside firmware-update.tex (as a new section) or as a separate adjacent file? Leaning toward new section in firmware-update.tex to keep the LLM-interaction story in one place.
6. **Which 2026 model to quote for inline response?** Should be a model the reader recognizes. Claude or ChatGPT most recognizable. Date the quote.
7. **Gen's input:** Does "try this exercise" feel empowering or patronizing? Gen's aesthetic veto applies.

---

## Annealing Log (S64, 5-pass — one past comfort)

### HIGH — all candidates:
1. ✓ Before/after experiment — strongest pedagogical element. KEEP.
2. ✓ Established-science verification prompts — confirms the foundation. KEEP.
3. ✓ Deliberate failure (topological wormhole) — absorbed into before/after structure. KEEP.
4. ✗ 9 scattered prompts — killed. High friction, visual noise, sequential dependency unlikely.
5. ✗ Per-chapter spiral abstract copy-buttons — killed. Already exist.
6. ✗ Three distinct button types (Firmware / Verify / Experiment) — killed. One exercise section, one visual language.
7. ✗ Chemosynthesis prompt — killed. Weakest connection to core argument.
8. ✗ Critical slowing down prompt — killed. Redundant with universality.

### MEDIUM — test each surviving element:
- Before/after experiment: pedagogical centerpiece. Reader proves it to themselves. KEEP.
- 6 prompts: each tests a real physics claim. All verifiable. None asks about coined terms. KEEP.
- Inline quoted responses: guarantees pedagogy reaches non-experimenters. KEEP.
- Lightweight hooks: low disruption, high utility for skeptical readers. KEEP.
- Version note: future-proofs the exercise. KEEP.

### LOW pass 1 — interactions:
- 0232 ↔ 0230: Wegener prompt (#4) depends on continental drift section existing. Gate Phase A on 0230 Phase A. ✓
- 0232 ↔ 0233: independent. No code overlap. ✓
- 0232 ↔ Firmware Update: exercise section extends existing chapter. Same copy-button infrastructure. ✓
- 0232 ↔ reader.js: no new JS needed. Existing copy-button handlers suffice. ✓

### LOW pass 2 — failure modes:
- Reader doesn't run the exercise: inline quoted responses still deliver the pedagogy. ✓
- LLM gets "topological wormhole" right: version note reframes as success. ✓
- LLM gets established science wrong: testing protocol catches this pre-ship. ✓
- Prompts work on Claude but not GPT: cross-model testing required in Phase C. ✓
- Exercise section makes Firmware Update too long: firmware-update.tex is 179 lines. Adding 800-1200 words of exercise adds ~80-100 lines. Total ~280 lines. Still within chapter-length norms. ✓

### LOW pass 3 — extra pass (past comfort):
- **Will readers actually DO this?** The concentrated exercise reduces friction, but it's still "put down the book, open your AI, paste 7 things, read 7 responses." How many readers do this? Probably <10% of readers, but >50% of specialist/technical readers — the exact audience that needs it most. The inline quotes reach everyone; the exercise reaches the skeptics. This is the right split.
- **What about readers who use the prompts in bad faith?** A hostile reviewer could paste prompts, get confirmation, then say "the AI just agrees with everything." Mitigation: the prompts ask about ESTABLISHED SCIENCE (Nobel Prizes, published math, textbook material), not about the book's claims. The LLM is confirming physics, not endorsing a narrative. The framing must make this distinction knife-sharp: "Your AI is confirming the published physics underneath these claims. Whether the claims themselves follow from that physics is a question the book asks you to evaluate."
- **The meta-argument is load-bearing but easy to miss.** "Your AI just confirmed what specialists couldn't see from inside their domains" is a powerful insight. But it's buried in an exercise section that <10% of readers will reach. Consider: put the meta-argument in the main text (or a popup), separate from the exercise. The insight — that cross-domain verification is now trivially easy in 2026 — is important even for readers who never run a prompt. The exercise demonstrates it; the insight should be stated independently.
- **The exercise has a shelf life.** By 2028-2030, LLMs will likely know "topological wormhole" from training data that includes this book. The before/after experiment may not work. The version note helps, but the exercise may need revision for future editions. This is acceptable — the Firmware Update chapter already contains a "date stamp" disclaimer (line 9-11). The exercise inherits the same temporal framing.
- **Testing burden.** Phase C requires running 6 prompts × 4 models × 2 conditions (with/without firmware) = 48 tests. Plus straw man tests. This is ~2 hours of careful work. Temptation to skip will be high. Make Phase C a checkpoint — don't ship without it.

**Rating: 7/10.** Concept brilliant, execution clarified. Concentrated exercise solves the scattered-prompts problem. Inline quotes guarantee pedagogy reaches non-experimenters. But: depends on 0230 for Wegener prompt, Gen aesthetic veto unresolved, testing burden is real. The plan is executable once 0230 ships.

---

## Execution Order (all three plans)

```
0233 Phase 1 (puzzle MVP)     ──┐
0233 Phase 2a (egg infra)     ──┤── can run in parallel
0230 Phase A (continental drift)┘
                                 
0230 Phase B (unbuilt bridge) ── after 0230 A

0233 Phase 2b (ULTRA II migration) ── after 0233 2a + Bruce decisions
0233 Phase 2c (reference review) ── after 2b
0233 Phase 2d (verification) ── after 2c

0232 Phase A (exercise section) ── after 0230 A (Wegener prompt needs a home)
0232 Phase B (in-text hooks) ── after 0232 A
0232 Phase C (cross-model testing) ── after 0232 A

0233 Phase 3 (remaining puzzles) ── after Phase 1 playtest + Bruce/Gen design
```

Estimated total: ~20-25 hours Generator time across ~8-10 sessions, plus Bruce/Gen creative work on puzzles and prose revision.
