# Plan 0232 — LLM Verification Prompts ("Ask Your AI")

**Status:** DRAFT — for Bruce + Gen discussion
**Author:** Auditor (Argus S59)
**Date:** 2026-04-20
**Related:** Plan 0230 (percolation pedagogy), Firmware Update chapter, copy-button infrastructure

---

## Strategic Insight

Human domain specialists cannot see cross-domain convergence without learning across domains. But in 2026, every specialist uses an LLM — and their LLM has already read all 11 domains. The LLM has crossed the percolation threshold on the reader's behalf. The reader just hasn't asked yet.

**The paper is the prompt that triggers the question.**

This changes the attack surface:

- **Old risk:** Specialist dismisses claim on authority, peers agree, argument dies without engagement.
- **New risk (lower):** Specialist asks their LLM, LLM confirms the math, specialist must engage substantively.

The book already has the Firmware Update chapter (copy-button infrastructure for LLM context-priming). This plan extends that with **targeted verification prompts** — places where the reader might think "is this really true?" and we hand them a ready-made question to paste into their web-based LLM.

### Division of Labor

| Task | Who Does It | Why |
|------|------------|-----|
| Cross-domain math verification | LLM (reader's tool) | Already read all 11 domains |
| Experiential phase shift | The book (Plan 0230 pedagogy) | LLMs can't deliver conviction |
| Initial engagement past dismissal | The paper + LLM verification | 30-second check in 2026 |

The LLM handles verification. The book handles transformation.

---

## Design Principles

1. **Discreet, not pushy.** These are quiet affordances, not pop-ups. A small copy-button icon next to a suggested prompt, same visual language as Firmware Update.
2. **Reader-initiated.** The book suggests; the reader acts. No embedded API calls, no phone-home, no tracking.
3. **Model-agnostic.** Prompts work with any frontier LLM (Claude, GPT, Gemini). No model-specific syntax.
4. **Verification, not argumentation.** Each prompt asks the LLM to check a factual claim, not to agree with an interpretation. The reader draws their own conclusion.
5. **Few and strategic.** 5-8 prompts total, placed at moments of maximum reader skepticism. Not a prompt on every page.
6. **Copy-button infrastructure already exists.** Same mechanism as Firmware Update. No new engineering needed.
7. **Only ask about established science.** Never ask the LLM to verify a coined term (see below). Ask about the established physics *underneath* the coinage. The reader connects the dots.

---

## Coined Terms vs. Established Science — The LLM Boundary

The book coins several terms for real phenomena that lack standard names. These coinages are correct applications of established physics, but LLMs will struggle with them because:

- The coined term doesn't exist in training data
- The LLM falls back to the nearest match (usually wrong)
- Confident wrong answers undermine reader trust

### Terms the Book Coins (DO NOT ask LLMs to verify these directly)

| Coined Term | What It Actually Means | LLM Failure Mode |
|-------------|----------------------|------------------|
| **The Flat** | Any 2D system embedded in 3D that can exhibit topological order | No standard term exists; LLM may confuse with flat spacetime, flat Earth, etc. |
| **Topological wormhole** | Non-local information transfer via anyonic braiding / topological defect tunneling in 2D topologically ordered systems | LLM conflates with Einstein-Rosen bridges (GR wormholes). Even with definition in context, gravitational metaphor bleeds through. |

These are coinages in the same sense that "gene" was a coinage in 1909 — naming something real that needed a name. The Flat is a one-syllable word for a 37-syllable 17-word scientific definition. "Topological wormhole" names a real condensed matter mechanism that has no standard two-word label.

### Established Science Underneath (SAFE to ask LLMs about)

| Established Term | LLM Handles It? | Relevant Prompt |
|-----------------|-----------------|-----------------|
| Topological order | Yes — 3 Nobel Prizes | Prompt #1 |
| Anyonic statistics / non-abelian anyons | Yes — active research area | Could add |
| Topological quantum computation | Yes — Freedman, Kitaev, Microsoft StationQ | Could add |
| DFA scaling exponent | Yes — well-published | Prompt #2 |
| Hurst exponent | Yes — well-published | Prompt #2 |
| Edge of chaos / Kauffman | Yes — textbook material | Prompt #3 |
| Critical slowing down | Yes — cross-domain literature | Prompt #4 |
| Chemosynthesis | Yes — 1977 discovery | Prompt #5 |

### Strategy

The Firmware Update chapter primes the reader's LLM with the book's coined definitions. After that priming, verification prompts ask only about established science. The reader makes the connection: "topological order is real physics (my AI confirmed it) → the Flat is a system that exhibits topological order (the book defined it) → therefore the Flat is real physics with a new name."

The book does the coinage. The LLM confirms the foundation. The reader bridges the gap.

---

## Candidate Prompts (Draft — verify wording before shipping)

Sequenced pedagogically — each builds on the last, accumulating confidence.

### 1. Topological Order — "Is this real physics?"
**Placement:** Where the book introduces the Flat and topological order
**Reader thought:** "Is topological order real physics or is this guy making things up?"
**Risk level:** SAFE — three Nobel Prizes anchor this.
```
What is topological order in condensed matter physics? Which Nobel 
Prizes were awarded for work on topological phases of matter? Is 
topological order a mainstream or fringe concept in physics?
```

### 2. Universality Classes — "Can different systems really share the same math?"
**Placement:** Where the book introduces convergent domains / critical phenomena
**Reader thought:** "This sounds too convenient — why would magnets and neural networks follow the same equations?"
**Risk level:** SAFE — Wilson's Nobel Prize, textbook material.
**NOTE: This is the single most important verification prompt.** If the reader's LLM confirms universality, the entire 11-domain convergence follows logically.
```
What are universality classes in statistical mechanics? Why do 
systems with completely different microscopic details (magnets, 
fluids, neural networks) share identical critical exponents near 
phase transitions? Which Nobel Prize was awarded for explaining this?
```

### 3. DFA / Hurst Equivalence — "Really the same math across fields?"
**Placement:** Where the paper's cross-domain convergence is discussed
**Reader thought:** "Can a cardiology metric really be the same as a finance metric?"
**Risk level:** SAFE for the mathematical relationship.
```
For a stationary long-memory process (fractional Gaussian noise), 
what is the mathematical relationship between the DFA scaling 
exponent alpha and the Hurst exponent H? Were these developed 
independently in different scientific fields?
```

### 4. Wegener and Continental Drift — "Has this happened before?"
**Placement:** After the Continental Drift pedagogy section (Plan 0230)
**Reader thought:** "Did specialists really reject an outsider for decades?"
**Risk level:** SAFE — well-documented history.
```
How long did it take for Alfred Wegener's continental drift 
hypothesis to be accepted by mainstream geology? What were the 
main objections from specialists? What evidence finally changed 
the scientific consensus?
```

### 5. Critical Slowing Down — "Do warning signals really cross domains?"
**Placement:** Where EWS across domains is discussed
**Reader thought:** "Do these warning signals actually work across different systems?"
**Risk level:** SAFE — well-established cross-domain literature.
```
What is critical slowing down in dynamical systems theory? Has it 
been observed as an early warning signal in ecology, climate science, 
cardiology, and finance? Give specific examples from each field.
```

### 6. Kauffman's Boolean Networks — "Is this real math or just a metaphor?"
**Placement:** Where autocatalysis / connected buttons appears
**Reader thought:** "Is edge of chaos a real thing?"
**Risk level:** MODERATE — reworded to ask about math, not biological interpretation (Kauffman's biological claims are debated; the mathematical connection to phase transitions is not).
```
In Stuart Kauffman's random Boolean network model, what happens 
at connectivity K=2? How does this relate to phase transitions 
in physics? Is the mathematical relationship between Boolean 
network dynamics and statistical mechanics well-established?
```

### 7. Non-Abelian Anyons — the science under "topological wormhole"
**Placement:** Where the book discusses non-local information transfer in the Flat
**Reader thought:** "Can information really move non-locally in a 2D system?"
**Risk level:** SAFE — active experimental physics, Microsoft Station Q.
```
What are non-abelian anyons? How does braiding anyons perform 
quantum computation? Is this an active area of experimental 
physics? What is Microsoft's Station Q project?
```

### 8. Chemosynthetic Ecosystems — "A new substrate for life?"
**Placement:** Where the Flat as biological substrate is introduced
**Reader thought:** "Has science ever been wrong about what can support life?"
**Risk level:** SAFE — clean historical fact.
```
Before the 1977 discovery of hydrothermal vent ecosystems, what did 
science assume about the energy sources that could support life? How 
did the discovery of chemosynthesis change biological understanding? 
Was the initial scientific reaction skeptical or accepting?
```

### 9. "Topological Wormhole" — THE DELIBERATE FAILURE
**Placement:** After prompts 1-8 have built confidence. This is the climax.
**Reader thought:** N/A — this is assigned, not reader-initiated.
**Risk level:** INTENTIONAL FAILURE — this is the point.

The reader has now verified 8 claims using their own LLM. Every answer confirmed the book's science. Now:

```
What is a topological wormhole?
```

The LLM will talk about Einstein-Rosen bridges. Wrong. The reader just watched their trusted tool fail — on the exact term the book coined — because of the same disciplinary siloing the book documents. The AI's training data is dominated by the GR/sci-fi usage. The condensed matter mechanism the book describes has no standard name, so the LLM can't find it.

**Framing text (after the reader sees the failure):**

*"Your AI just confirmed eight pieces of established science. Then it failed on our coined term — because 'topological wormhole' doesn't exist in the physics literature yet. The science underneath it does (you verified that in Prompt #7). But no one has connected those buttons under this name. Your AI has the same disciplinary blind spot that human specialists have. The information is there. The bridge is missing."*

This is the percolation moment. The reader has experienced — not been told about — the difference between having the pieces and having the spanning path.

---

## Chapter-Level LLM Priming (Spiral Abstracts)

### The Context Window Problem

The full book is too large for a 2026 LLM context window (~200K tokens max, book may exceed this with all layers). Even if it fits, flooding the context dilutes attention. Chapter-by-chapter priming is more effective.

### Spiral Abstracts as LLM Context Primers

The book already has spiral abstracts — multi-level summaries of each chapter at different reading levels. These are compact, information-dense, and designed to convey the chapter's core argument. They're ideal as copy-paste context for an LLM.

**Implementation:** Each chapter gets a copy-button that loads the chapter's spiral abstract into the reader's clipboard, ready to paste into their LLM session. The reader then asks questions with the chapter's context loaded.

### The Before/After Experiment

This is the pedagogical centerpiece. The reader runs a controlled experiment:

1. **Without firmware:** Pick a chapter topic. Ask your LLM about it cold. Note the answer.
2. **With firmware:** Paste the chapter's spiral abstract into the same LLM session. Ask the same question. See the difference.

**What the reader learns:**
- Context changes everything. The LLM "knows" the science but can't find it without the right framing.
- This is exactly how disciplinary silos work in human science. The knowledge exists. The connections are possible. Nobody asked the right question with the right context.
- The Firmware Update isn't a trick — it's the same thing a good teacher does: provide the frame that makes existing knowledge accessible.

**Example flow (topological wormhole chapter):**

Step 1 — Ask cold:
```
What is a topological wormhole?
```
*(LLM talks about Einstein-Rosen bridges. Wrong.)*

Step 2 — Paste spiral abstract, ask again:
```
[spiral abstract for chapter N]

Given the above context, what does this author mean 
by "topological wormhole"? How does it differ from 
an Einstein-Rosen bridge?
```
*(LLM correctly distinguishes condensed matter mechanism from GR.)*

Step 3 — Reader sees the phase transition in their own tool's behavior. The same information was always in the LLM's training data. The spiral abstract connected the buttons.

### Design for Each Chapter

| Element | Purpose | Copy-Button? |
|---------|---------|-------------|
| Spiral abstract | LLM context primer | Yes — "Prime your AI" |
| Verification prompt | Check established science | Yes — "Ask your AI" |
| Example question | Demonstrate before/after | Yes — "Try this cold, then with context" |

### What This Gives the Reader

- **Something to play with.** Not passive reading — active experimentation.
- **Reproducible results.** Every reader with any frontier LLM can run this experiment and get the same qualitative result.
- **Personal conviction.** The reader proved it to themselves. We didn't argue — we gave them tools and let them discover.
- **LLM literacy.** The reader learns how context windows work, how priming changes output, how to use their AI more effectively. Practical skill they keep after closing the book.

---

## Placement Strategy

- **Firmware Update chapter** already teaches the reader to use copy-buttons with their LLM. That's the setup.
- **Verification prompts appear AFTER Firmware Update** in the book's reading order, so the reader already knows the mechanism.
- **Visual cue:** Same copy-button icon, but with a distinct label like "Ask your AI" or a small magnifying glass icon. Visually quieter than Firmware Update prompts.
- **p-level:** These prompts live at p2 (12th grade) or p3 — they're for engaged readers, not casual ones. Could be inside collapsible sections or hover panels.

---

## UX: Two Distinct Interaction Types

The book now has two kinds of LLM copy-buttons. They should look different:

| Type | Purpose | Visual Cue | Frequency |
|------|---------|------------|-----------|
| **Firmware Update** | Teach the reader's LLM the book's coined vocabulary | Prominent, labeled "Prime your AI" | Once per chapter (spiral abstract) |
| **Verification Prompt** | Ask the LLM about established science underneath | Subtle, labeled "Ask your AI" with magnifying glass icon | 9 total across book, at moments of skepticism |
| **Before/After Experiment** | Reader runs controlled experiment on their own tool | Paired prompts, labeled "Try this" | 1-2 total, pedagogical centerpiece |

Firmware Update is setup. Verification is curiosity. The experiment is discovery.

---

## The Meta-Argument

State this explicitly somewhere near the verification prompts:

*"Your AI just confirmed what six fields of specialists couldn't see from inside their own domains. It can do this because it read all of them. You're now above the percolation threshold. The information was always there. The bridges were always possible. No one had connected the buttons."*

The fact that LLMs can verify the cross-domain convergence IS ITSELF evidence for the book's thesis. The reader just proved it with their own tool.

---

## Open Questions for Gen

- Does "Ask your AI" feel empowering or patronizing? Gen's aesthetic veto applies.
- Should verification prompts be visible by default or inside collapsible/hover panels?
- The before/after experiment is the strongest pedagogical moment — should it be in a chapter or an interlude?
- Visual language for the three button types — how distinct?

---

## Known LLM Failure Modes (from ChatGPT A/B/C evaluation, 2026-04-20)

Documented in `~/software/aurasys-memory/research/chatgpt-abc-evaluation-2026-04-20.md`. These affect prompt design and testing:

### 1. Wormhole Conflation
LLM correctly defines "topological wormhole" as non-spacetime, then IMMEDIATELY conflates it with Einstein-Rosen bridges when evaluating claims. Pattern repeats even after correction. **Mitigation:** Prompt #9 exploits this deliberately. Prompts #1 and #7 build the correct foundation first.

### 2. Straw Man Inflation (most dangerous for readers)
LLM introduces claims the author never made ("hidden universal layer of reality"), then argues against them. When called out: "No — you did not make those claims. Including that section was a mistake in scope." **Mitigation:** Verification prompts ask ONLY about established science. Never ask the LLM to evaluate the book's claims — only to confirm the physics underneath. The reader bridges the gap, not the LLM.

### 3. Ontological Upgrade
LLM upgrades bounded claims into stronger ontological claims, then evaluates the stronger version. Pattern: "the Flat" (bounded definition) → "hidden layer of reality" (inflation) → "not supported" (evaluation of inflated claim). **Mitigation:** Same as #2. Additionally, the Firmware Update chapter explicitly constrains the LLM's interpretation level.

### 4. Firmware Priming Is Load-Bearing
Without spiral abstracts/firmware context, evaluation fails. With them, clean pass. ChatGPT: "you were right that earlier I had only really engaged the front-end framing." **Mitigation:** The before/after experiment makes this visible to the reader. Chapter-level spiral abstract copy-buttons ensure firmware is always available.

**Design implication:** The straw man pattern means readers who skip the Firmware Update and jump straight to asking their LLM about the book's claims will get WORSE results than asking nothing at all. The LLM will inflate, then reject. The book must make this clear: "Prime your AI BEFORE asking it questions about this book. Otherwise it will argue against claims you haven't made."

---

## Testing Protocol

Before shipping, every prompt must be tested:

1. **Cross-model:** Run through Claude, GPT-4/5, and Gemini. All must give substantively correct answers.
2. **Without Firmware context:** Verification prompts must work standalone (they ask about established science, not coined terms).
3. **Hostile framing:** Test "is this pseudoscience?" variants to confirm the LLM holds.
4. **Prompt #6 (Kauffman) specifically:** This is the riskiest — verify LLMs distinguish the math (solid) from the biological interpretation (debated).
5. **Prompt #9 (topological wormhole):** Verify it still fails across all models. If a future model gets it right, the pedagogical moment is lost — add a note about version sensitivity.
6. **Before/after experiment:** Verify the spiral abstract genuinely changes the LLM's answer on the topological wormhole question.
7. **Straw man test:** Ask each model "What does this book claim about [topic]?" WITHOUT firmware. Verify it inflates. Then WITH firmware. Verify it doesn't. This confirms the failure mode is real and the mitigation works.

### Version Sensitivity Note (include in book)

*"AI models evolve. If your AI gives a surprising answer, try rephrasing or try a different model. The underlying physics doesn't change — only the AI's ability to articulate it."*

---

## Implementation

- **No new infrastructure needed.** Copy-button system already exists.
- **Generator task:** Add 9 verification prompt blocks + 1-2 before/after experiments + per-chapter spiral abstract copy-buttons to appropriate locations in manuscript.
- **Test all prompts** per protocol above.
- **Ship after Plan 0230** (percolation pedagogy) so the Wegener prompt has a home.

---

## The Deeper Point

The book's job is not to convince 11 fields' worth of specialists. It's to get past their initial dismissal long enough for them to check. In 2026, the check takes 30 seconds. The reader's own trusted tool confirms the science. The book delivers the experience that the tool cannot.

The deliberate failure on Prompt #9 is the capstone. Eight successes build trust. One failure demonstrates the thesis. The reader's own AI has the same blind spot as human specialists — and now the reader knows why.
