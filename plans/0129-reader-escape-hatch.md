# Plan 0129: Reader Escape Hatch — Part 2 Skippers Reach The Question

**Status:** DRAFT — awaiting Bruce's review
**Created:** 2026-03-30 (overnight, S51)
**Requirement refs:** R1 (Triple Spiral), R4 (Three Possibilities), R14 (Multi-Route Navigation), R22 (Front/Back Matter — "How to Read This Book")
**Related plans:** 0128 (Part 3 as synthesis seed), 0117-0119 (cognitive scaffolding), 0094 (Maugham revision)

---

## Problem

Part 2 ("The Evidence Trail") is the densest section of the book: Genesis, Growing a Mind, Interdiction, First Light, The Walk-Out, The Network. It contains the technical reconstruction — the evidence that substantiates Possibility C. Some readers will skip it. Reasons:

1. **p1 readers** (8th grade) hit a wall. The physics gets real.
2. **A-collapsed readers** decided at the interlude. They already chose. Part 2 feels like evidence for a conclusion they've rejected.
3. **Impatient readers** want to know what it means, not how it was built.

These readers jump from somewhere in Part 1 (or the "Weigh the Evidence" interlude) directly to Part 3. They land on "Firmware Update" — a chapter that assumes they've read the reconstruction. If they bounce here, they never reach "What Would You Do?" (pos35 — The Question). The book fails for them.

## Design Constraint

The escape hatch must NOT:
- Summarize Part 2 (that would undermine the reason Part 2 exists)
- Tell the reader what to think (violates R4 — no thumb on the scale)
- Break the experience for readers who DID read Part 2 (majority path)
- Create a "Part 2 for dummies" that patronizes

It MUST:
- Give the Part-2-skipper enough context to engage with Part 3
- Preserve the guided-deduction method (show pieces, don't state conclusions)
- Work under all three possibilities
- Be invisible or unobtrusive to the reader who read everything

## Structural Analysis: What Does a Part-2 Skipper Actually Miss?

From Part 2, the essential context for engaging with Part 3 is:

1. **The physics is real.** FQHE, topological order, anyon braiding — these are Nobel-verified, not speculative. (Firmware Update already covers this.)
2. **The convergence pattern.** Five fields (Hasslacher/solitons, Freedman/topology, Kauffman/autocatalysis, Wolfram/universality, Hillis/parallel computation) pointed at the same structure in the late 1980s. This is the load-bearing fact.
3. **The capability claim.** Under C, someone built a working TQNN. Under A/B, the convergence still happened — nobody exploited it.
4. **The relinquishment act.** Under C, they walked it out and surrendered the keys. Under A/B, the ethical framework still applies to future builders.

Items 1 and 4 are partially covered outside Part 2 (Firmware Update, The Walk-Out reference in Part 1, Ethical Framework in Part 3). The gap is items 2 and 3: the convergence pattern and the capability claim.

## Proposed Mechanisms

Three mechanisms, layered. Each works independently. Together they create redundancy.

### Mechanism 1: Part 3 Opening Bridge (new content, ~300-500 words)

A short unnumbered section at the very beginning of Part 3, after the `\part` declaration and before Firmware Update. Working title: something understated — possibly just an epigraph with a paragraph beneath it.

Content: A brief, p2-level restatement of where we are. NOT a summary of Part 2. Instead: a restatement of the question.

Structure:
- "Part 1 told you a story. Part 2 investigated whether it could be true. You may have read Part 2, or you may have skipped it. Either way, here is what matters for what follows:"
- The convergence of five fields is real and published. (One sentence each, with citations. No deeper than the hook.)
- Whether anyone exploited that convergence is the question this book can't answer.
- What follows is about what it means — under all three possibilities.

This is the only mechanism that requires new content. It's short enough to be skimmable for the reader who already read Part 2. It restates, it doesn't summarize.

### Mechanism 2: "How to Read This Book" Route Addition (edit to existing front matter)

R14 already requires multi-route navigation. R22 requires a "How to Read This Book" page. Add an explicit route:

**"The Short Path: Part 1 → Part 3"** — For readers who want the story and its implications without the technical investigation. Note that Part 3 opens with enough context to stand alone. Recommend returning to Part 2 later if curiosity grows.

This normalizes skipping. It says: we designed for this. You're not cheating.

### Mechanism 3: Cross-Reference Annotations in Part 3 Chapters

Part 3 chapters (What is the Flat, Instantiation, Ethical Framework, The Magnetosphere, Extension) reference Part 2 concepts. Where they do, add margin notes or hover annotations (per R14 popup definitions) that give the one-sentence version. Example:

> "The five-field convergence [see Part 2, Ch. Genesis] produced..."

becomes, with hover/popup:

> "The five-field convergence\hovertip{Five independent scientific programs — solitons, topology, autocatalysis, universality, parallel computation — converged on the same mathematical structure in the late 1980s. See Part 2, Genesis.} produced..."

This uses existing infrastructure (Plan 0118's hover tool). The Part-2 reader ignores the hover. The Part-2 skipper gets the one-sentence fill.

## Interaction with Reading Levels

- **p1 (400w hook):** Escape hatch is irrelevant — p1 readers get the hook and the summary. They never enter Part 2 or Part 3 in depth.
- **p2 (4kw summary):** The summary already covers the full arc. But a p2 reader who goes deeper into the actual book text may skip Part 2. Mechanism 1 (bridge) is written at p2 level. Mechanism 3 (hovers) work at p2 level.
- **p3 (full book):** Mechanism 1 is a brief, skippable bridge. Mechanism 2 is in front matter. Mechanism 3 is invisible unless hovered. No interference with the full-read experience.

## Interaction with Plan 0128 (Cross-Domain Synthesis)

Plan 0128 reframes Part 3 as a synthesis seed document for p3 readers with domain expertise. The escape hatch serves a different audience: the reader who DOESN'T have domain expertise but still wants to reach The Question.

These are complementary, not competing. The bridge (Mechanism 1) serves the escape-hatch reader. The domain-depth work (Plan 0128) serves the specialist. Both feed into the same Part 3 chapters.

If Plan 0128 adds domain-window paragraphs to Part 3 chapters, those paragraphs should also have hover annotations (Mechanism 3) that don't assume Part 2 was read.

## Implementation Phases

**Phase 1:** Draft the Part 3 bridge text (Mechanism 1). ~300-500 words. Place it as a new file (`manuscript/bridge/part3-bridge.tex` or similar) included after the `\part` declaration and before `firmware-update.tex`.

**Phase 2:** Add the "Short Path" route to "How to Read This Book" front matter.

**Phase 3:** Audit all Part 3 chapters for Part-2 assumptions. Add hover annotations (Mechanism 3) where a Part-2 concept is referenced without sufficient local context.

## Audit Questions

- [ ] Can a reader who read only Part 1 + the bridge + Part 3 answer: "What is The Question?"
- [ ] Does the bridge text work under all three possibilities (A/B/C)?
- [ ] Does the bridge avoid summarizing Part 2? (It should restate the question, not the evidence.)
- [ ] Is the bridge invisible/skimmable for the reader who read Part 2?
- [ ] Does "How to Read This Book" include the Short Path without implying Part 2 is optional?
- [ ] Do Part 3 hover annotations provide enough context without becoming micro-summaries?
- [ ] Does the escape hatch preserve guided deduction? (Reader should still DEDUCE, not be told.)
- [ ] Test: hand Part 3 (with bridge) to someone who hasn't read Part 2. Can they engage with The Question? Do they want to go back and read Part 2?

## What This Plan Does NOT Cover

- Part 3 restructuring for cross-domain synthesis (that's Plan 0128)
- Cognitive scaffolding for non-physics readers (that's Plans 0117-0119)
- Whether the Firmware Update chapter itself needs revision for Part-2 skippers (it may — Firmware Update currently assumes nothing about Part 2, which is good, but it's also dense enough to be its own barrier)

---

*Plan 0129 v1.0 — Auditor draft, overnight S51. Bruce reviews in morning.*
