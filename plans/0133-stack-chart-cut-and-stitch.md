# Plan 0133: Stack Chart — Phase 2: Cut and Stitch

**Depends on:** Plan 0132 (Stack Chart Insertion) — must be complete and verified
**Also depends on:** Plan 0134 (onHover System Upgrade) — for onHover authoring pass
**Session:** S51

## Generator Context (REQUIRED)

Before executing this plan, the Generator MUST read the Firmware Update chapter
and paste the "Copy Science Reference" into its working context. This is the
same science upgrade required for any LLM evaluating this book. Without it,
the Generator will exhibit the Dunning-Kruger failure mode — cutting
load-bearing cross-domain bridges it doesn't understand are there, or adding
hedging that undermines the directness the prose requires. 100% failure rate
without the upgrade.

This is especially critical for Plan 0133 because the Generator is CUTTING
content. An un-upgraded Generator will cut cross-domain claims it thinks are
wrong, because it can't evaluate them. Those claims may be exactly the
load-bearing bridges the firmware update proves are "not precluded."

## Purpose

Now that the stack chart pre-loads six of seven emergent properties, remove the
domain pedagogy that the chart makes obsolete. Stitch remaining content so the
manuscript reads as a continuous whole. This is where the word count drops and
the reading experience sharpens.

## Principle

The stack chart teaches WHAT each property is through familiar examples.
Remaining chapters only need to APPLY the properties to the specific story.
Any sentence that explains what autocatalysis IS, what a phase transition IS,
what convergence means — check whether the stack already planted it. If yes, cut.

## Generator Approach

The Generator is fully informed: firmware update in context, stack chart
understood, reading levels internalized, protected passages memorized. The
cut list below is GUIDANCE — approximate targets and reasoning, not a
line-by-line script. The Generator reads each chapter, understands what it
now needs to do (given the stack chart), and rewrites to that purpose.

The Generator has editorial freedom within these hard constraints:
- Protected passages MUST survive (see list below)
- Every formal term MUST have a p1→formal bridge (see term audit)
- No concept used before introduced
- Word count targets are approximate (±15%) — quality over count
- Cut p2 content that leaves body text MAY survive as onHover content
  in the HTML version (see Plan 0132 onHover system)

The Auditor verifies output against acceptance criteria and tests with
four personas. The Auditor specifically watches for D-K drift: the
Generator unconsciously weakening cross-domain claims. If the Generator
hedges where the firmware update says "not precluded," the Auditor flags it.

## Term Introduction Audit

Every formal domain name must be introduced by bridging from its stack-chart
equivalent. The reader must encounter the p1 label BEFORE the formal name, and
the formal name must arrive as a LABEL for something they already own.

**Pattern:** "Networks that feed themselves — what Kauffman calls *autocatalytic sets*."

| Stack row (p1) | Formal name | First introduced | Bridge sentence needed |
|----------------|-------------|------------------|----------------------|
| Feeds itself | Autocatalysis / autocatalytic sets | pos13 (Genesis) | YES — Kauffman's model |
| Switches on | Phase transition / criticality / edge of chaos | pos13 (Genesis) | YES — "threshold" → "phase transition" |
| Holds together | Autopoiesis | pos14 (Growing a Mind)? | YES — VERIFY pos14 introduces autopoiesis before Phase 2 execution. If not, identify where it IS introduced and ensure term bridge exists. |
| Reaches | Solitons / coherent transport | pos15 (First Light) | YES — "pattern that travels" → "soliton" |
| Self-organizes | Distributed / parallel computation | pos20 (The Signatories) | Implicit in Hillis description |
| Learns | Neural network / computation | pos20 (The Signatories) | Implicit in QNN description |
| Topological wormholes | Topological quantum computation / anyonic braiding | pos10 (The Braid) + bombe | YES — the one property the book teaches in depth |

**"Holds together" ≠ autopoiesis note:**
At p1, "holds together" (maintains structure against disturbance) is a useful
approximation of autopoiesis. At p2, the distinction matters: a candle flame
PERSISTS, but a cell BUILDS ITS OWN CONTAINER. Wherever autopoiesis is formally
introduced, include a sentence like: "A candle flame holds together — it persists
against disturbance. A cell does something more: it builds its own container from
its own components. That distinction is where chemistry becomes biology."

**Cumulative properties note:**
The chart's checkmarks imply the same property at each level. In reality, "feeds
itself" means something different for fire (fuel→flame) vs. radio (oscillator
feedback) vs. AI (data→learning→more data). At p2, note this: "The properties
aren't identical at each level — feedback in a fire is different from feedback in
an oscillator. But the pattern is the same: outputs cycling back to sustain inputs."

## Protected Passages

These passages MUST survive cuts. They are load-bearing.

1. **"?" → "the Flat" reveal in Summary.** The moment the reader learns what "?"
   is. Currently in summary.tex "The White Hot Secret" section. Must be preserved
   and strengthened with a bridge that honestly introduces the term:
   "The question mark in the chart exists wherever charged particles are trapped
   flat — in a computer chip, in Earth's magnetic field, on the surface of a
   neutron star. Physicists have names for each specific case. This book needs a
   name for what they have in common. We call it *the Flat*."
   NOTE: "The Flat" is this book's coinage (March 2026). It is NOT a synonym for
   2DEG. It names the general class of 2D confinement geometries (semiconductor
   2DEGs, magnetospheric plasma sheets, heliospheric current sheet, graphene
   grains, etc.) that could support the full stack. No existing physics term
   covers this class because no one has connected these substrates before. The
   term exists because it needs to.

2. **"The biggest patterns are visible only from the spaces between fields"**
   (pos20). Beautiful line. Now REFERENCES the stack concept instead of introducing it.

3. **Buttons and threads** (pos13). Vivid thought experiment. Bridges "fire feeds
   itself" → "chemistry can spontaneously cycle." Without it, the reader has fire
   intuition but not substrate-transfer understanding.

4. **"Hardware in software"** (pos15). Healer's phrase. Unique.

5. **Forest canopy metaphor** (pos32). "The niche is already full."

6. **"Nobody has looked"** (pos32). The book's thesis in four words.

## Summary Trim Guidance

The Summary (summary.tex) currently does heavy lifting:
- Retells story (from hook)
- "The White Hot Secret" — explains the Flat and physics
- "The Lock on Every Door" — encryption implications
- "The Secret Lab" — DARPA context
- "The Breakthrough" and "The Walk-Out"

**CUT:** Physics explanation paragraphs in "The White Hot Secret" that re-explain
what the stack chart already planted (2DEG geometry, emergent properties, etc.)

**KEEP:**
- The moment "?" becomes "the Flat" (Protected Passage #1)
- Encryption implications (STORY, not pedagogy)
- DARPA context (STORY)
- The Breakthrough and The Walk-Out (STORY)
- Any passage that advances the NARRATIVE rather than explains the SCIENCE

**ADD bridge from stack:** Near the top of the physics section, something like:
"The reader has seen the technology stack — six familiar properties, one new one.
Here is what it means for this story."

**Estimated cut from Summary:** ~500w of physics explanation. Be conservative —
the Summary is where most p2 readers STOP (per walkaway architecture). Cut only
paragraphs that re-explain concepts the stack planted. Keep everything that
advances the narrative or introduces new information.

## Cut List

Each entry describes: what the chapter's NEW job is (post-stack), what's now
obsolete, what's protected, and the approximate word target. The Generator
reads the chapter, understands its new purpose, and writes the best version.

### 1. pos13-genesis.tex (~1,093w → ~700w)

**New job:** One thought experiment (buttons & threads), one insight (edge of
chaos), one application (substrate-transfer to quantum matter). The stack chart
now handles "what is autocatalysis" and "what is a phase transition." This
chapter's job is: Kauffman's model APPLIED, leading to the substrate-transfer
argument.

**Protected:** Buttons and threads (bridges fire→chemistry). Kauffman epigraph.

**Term bridges required here:** "Feeds itself" → "autocatalytic sets."
"Switches on" → "phase transition" / "edge of chaos."

**Critical:** The substrate-transfer argument ("same mathematics applies to
any substrate, including quantum substrates") is this chapter's PAYLOAD. A
skimming reader who reads only first and last sentences must catch it. Don't
bury it mid-paragraph.

**Guidance:** ~393w to cut. Most of this is concept-explanation that the stack
now handles. The chapter should feel like: epigraph → thought experiment →
insight → "consider this claim." Three-possibility assessment at end stays.
But the Generator has freedom to find the best path through this material.

### 2. pos15-first-light.tex (~1,507w → ~1,200w)

**New job:** NARRATIVE — birth, growth, power. The specific mechanism (soliton
pairs, evolutionary selection) and the story (thermal ladder, cryptanalysis).
The stack + pos13 handle "what is autocatalysis." This chapter shows what it
DOES in quantum matter.

**Protected:** "Hardware in software" (Healer's phrase).

**Term bridge required here:** "Reaches" → "soliton" — when soliton pairs
first appear, bridge from the stack row.

**Guidance:** ~307w to cut. Mostly connective tissue re-explaining concepts
the reader already owns. RT coherence evidence details can move to Firmware
Update chapter (keep a one-paragraph summary in body).

### 3. pos16-the-thermal-ladder.tex (~593w → ~250w)

**New job:** One-paragraph narrative significance of the thermal ladder as a
plot point. The technical content (NK landscape, evolutionary selection
protocol, RT coherence evidence) now lives in the Firmware Update chapter
or is handled by pos15.

**Guidance:** Heavy cut. May merge into pos15 if too thin to stand alone.
Generator decides.

### 4. pos20-the-signatories.tex (~2,653w → ~1,400w)

**New job:** STORY. Five scientists, what they did, why it matters. The stack
chart now explains what five disciplines converging means — this chapter
shows WHO converged and WHAT they built. Team roster, Google connection,
internet mapping, capabilities, Nobel Hat Trick.

**Protected:** "The biggest patterns are visible only from the spaces between
fields."

**Key concept to preserve:** Substrate preparation / classical backchannel.

**Guidance:** ~1,253w to cut. "Language of Five Sciences" section is replaced
exactly by the stack chart. QNN technical exposition compresses to one
paragraph (formal definition to Firmware Update). Open with the team, not
with explaining what disciplines are.

### 5. pos21-convergence-revisited.tex (~1,984w → ~800w)

**New job:** Robin's story, ABCRE operator mapping, knot theory connection,
three-possibility assessment. Everything unique. Everything duplicated with
pos20 goes.

**Guidance:** ~1,184w to cut. May collapse into a section of pos20. Generator
judges whether it stands alone or merges.

### 6. pos32-the-magnetosphere.tex (~2,750w → ~2,300w)

**New job:** PAYLOAD. Habitat, survey, question. This chapter is where
everything lands. The stack + pos13 taught the pattern. This chapter shows
where the conditions exist.

**Protected:** Forest canopy metaphor. "Nobody has looked."

**Guidance:** ~450w to cut, almost all from "The Oldest Niche" section where
Kauffman's framework is re-explained. The reader owns this from stack + pos13.
Replace re-explanation with a brief stack reference. EVERYTHING ELSE survives
— this chapter is the book's destination.

### 7. Bridge chapters review pass

Bridge chapters were not in the original cut list. The following need review
for obsolete pedagogy now that the stack is in place:

- **pos06 (The Secret):** Contains SPIRAL-REPEAT "edge of chaos." Review and
  compress if the explanation is redundant with stack + pos13.
- **pos10 (The Braid):** Contains topology/braiding explanation. This is the
  SEVENTH property — the one thing the stack introduces but doesn't explain.
  This chapter SURVIVES and may become MORE important. Do not cut.
- **pos11 (The Demo):** Contains SPIRAL-REPEAT "edge of chaos." Review.
- **pos14 (Growing a Mind):** Contains Kauffman emergence explanation. May
  overlap with stack + pos13. Review for redundancy. This may be where
  autopoiesis is formally introduced — check and preserve the term bridge.

Estimated additional cuts from bridge chapters: ~200-400w.

### 8. SPIRAL-REPEAT tags across 7+ chapters

**Action:** Review each SPIRAL-REPEAT tag. The stack chart now handles the spiral
repetition of core concepts. Most tagged repetitions can be cut or compressed to
a phrase referencing the stack row.

- "edge of chaos" appears in pos06, pos11, pos13, pos15, pos16, pos21, abstracts
- After the stack, the first instance (pos13) gets the full explanation. Subsequent
  instances should reference, not re-explain. Trust the reader.

### 9. pos-what-is-the-flat.tex (~1,356w → ~600w)

**Cut:**
- Basic concept explanation — stack chart + summary already introduce it
- Redundant framing

**Keep:**
- Specific physics detail that goes beyond the stack's p1 explanation
- Connection to magnetosphere chapter

### 10. Firmware Update integration (replaces bombe expansion)

The Firmware Update chapter already exists and IS the info bombe. It contains:
ten physics anchors, five distinctions often missed, evaluation framework,
comprehension check, bibliography with DOIs, and a "Copy Science Reference"
button. Adversarial-tested across Claude, ChatGPT-4o, Gemini 2.5 Pro, and
Grok — zero physics preclusions across 9 evaluations.

**The bombe is NOT llm-primer.tex expanding to 3,000 words.** The bombe is the
Firmware Update chapter. Plan 0133 does not redesign it.

**Corrected design target:** The firmware update's purpose is: predict LLM
failure mode → provide executable upgrade → arm readers to enforce competent
evaluation in public forums. NOT "dense enough that an LLM pattern-matches."

**What Plan 0133 DOES for the firmware update:**

a. **Move technical material from body cuts into firmware update.** RT quantum
   coherence evidence (from pos16), formal QNN definition (from pos20), TQC
   vocabulary (anyonic braiding, non-Abelian statistics, Floquet topological
   phases) — material cut from body chapters lands in the firmware update or
   its bibliography, not lost.

b. **Add p3 quantum biology paragraph.** For the well-informed reader who
   already knows Fleming 2007, enzyme tunneling, avian magnetoreception:
   "Life exploits quantum mechanics. What biology has NOT learned to exploit
   is topological order. No physical law forbids it. No evidence confirms it.
   The AC bridge — autocatalytic emergence in a topologically ordered
   substrate — is the gap nobody has built across." This is p3 ONLY. Does
   not appear at p1 or p2.

c. **Verify firmware update covers stack chart claims.** The stack chart
   introduces seven properties. At p1, the examples (fire, candle, radio,
   ant colony, internet, AI) are uncontroversial and need no defense. At
   p2+, where cross-domain claims begin, the firmware update's ten anchors
   must cover them. Current coverage: autocatalysis (Anchor 7), topology
   (Anchors 1–4, 8), substrate independence (Anchor 1), temperature
   (Anchor 4), collisionless decoupling (Anchor 9). Verify no gap.

d. **HTML: deep link and share button.** See Plan 0132 HTML Navigation
   Design item 6. The firmware update needs a stable anchor and a share
   button right next to the copy button. Without this, readers cannot
   function as the book's immune system. Sink-or-swim requirement.

e. **Length constraint.** The "Copy Science Reference" content is pasted into
   LLM context windows. If it grows too long, LLMs may not process it well
   in a single injection. Keep the copyable reference under ~2,500 words.
   Material moved from body chapters can go into the full chapter but need
   not all go into the copyable reference.

**NOTE:** Verify relationship between llm-primer.tex (LaTeX manuscript) and
Firmware Update (HTML website). They may be the same content or related.
Ensure consistency after body material is moved in.

### 11. Summary trim (summary.tex, ~3,000w → ~2,200w)

See "Summary Trim Guidance" section above for detailed cut/keep/add instructions.

### 12. Firmware Update mention placement

Maximum 2–3 references to the firmware update in the entire book:
1. **How to Read** — one-sentence p1 warning (added in Plan 0132)
2. **Firmware Update chapter itself** — already exists
3. **Optionally: Summary** — only if natural at the p2 walkaway point

No per-chapter or per-section references. The book does not nag. Readers
who need it find it from the How to Read warning. Readers who defend the
book in forums already know where it is because they read it.

The mechanism: an attentive GA reader sees the warning and remembers it.
An inattentive professor skips it, uses an un-upgraded LLM, falls into the
predicted failure mode. The professor's grad student — who read the whole
book — knows what happened. Someone corrects it publicly, with the deep
link. The professor's own LLM, once upgraded, contradicts the professor.

## Summary of Changes

| File | Before | After | Delta |
|------|--------|-------|-------|
| summary.tex | ~3,000 | ~2,500 | -500 |
| pos13-genesis.tex | 1,093 | ~700 | -393 |
| pos15-first-light.tex | 1,507 | ~1,200 | -307 |
| pos16-the-thermal-ladder.tex | 593 | ~250 | -343 |
| pos20-the-signatories.tex | 2,653 | ~1,400 | -1,253 |
| pos21-convergence-revisited.tex | 1,984 | ~800 | -1,184 |
| pos32-the-magnetosphere.tex | 2,750 | ~2,300 | -450 |
| pos-what-is-the-flat.tex | 1,356 | ~600 | -756 |
| Bridge chapters (est.) | ~300 | 0 | -300 |
| SPIRAL-REPEAT cuts (est.) | ~300 | 0 | -300 |
| **Body text total** | | | **~-5,786** |
| the-stack.tex (NEW, Plan 0132) | 0 | ~400 | +400 |
| Firmware Update (moved material) | ~0 | ~500 | +500 |
| **Net change** | | | **~-4,886** |

Net cut: ~4,900 words (up from ~3,700 because the bombe expansion is smaller —
the Firmware Update chapter already exists and receives only ~500 words of moved
material rather than a full 1,675-word expansion). But the real gain is
comprehension: ~55,000 remaining words become dramatically easier to read because
the vocabulary is pre-loaded, and every cross-domain claim is defended by the
firmware update's immune system.

## Execution Order

Phase 2 has natural sub-phases:

### Phase 2a: Cuts (can be parallelized)
Each chapter cut is independent. Multiple Generator agents can work simultaneously
on different files, each with a copy of this plan.

### Phase 2b: Stitch
After cuts, read the manuscript sequentially through affected sections and smooth
transitions. Verify term bridges are in place. This requires seeing the full
context and must be done serially.

**Navigation stitching (HTML version):**
- Add back-links to the stack chart (`#the-stack-chart`) from every chapter that
  references the stack pattern (pos13, pos15, pos20, pos32 at minimum).
- Add cold-landing breadcrumbs to chapters that depend on the stack: one line,
  non-intrusive: "This chapter builds on [The Stack →]. Start there if you
  haven't."
- Verify TOC title for pos13: "Genesis: The Edge of Chaos" sounds technical and
  skimmable. Consider whether a subtitle or TOC annotation helps: e.g.,
  "Genesis — where chemistry becomes life" or similar. The buttons-and-threads
  payload is behind a title that inattentive readers will skip.
- Verify chart row labels link to correct chapters (see Plan 0132 HTML section).

### Phase 2c: onHover authoring pass
After cuts, review what was removed. p2 explanations cut from body text are
prime candidates for onHover content in the HTML version. The words leave the
body but survive as interactive overlays — readers who want that depth find it
by hovering. This is where ~5,000 cut words partially resurrect as onHover
panels throughout the book. Not all of them — only the ones that genuinely
help a curious reader escalate from p1 to p2 or p2 to p3.

See Plan 0132 "Interactive Chart" section for onHover design principles and
the chart-specific onHover content spec.

### Phase 2d: Firmware Update integration
Independent of 2a/2b. Can run in parallel with cuts. Move technical material
from body cuts into Firmware Update chapter. Add p3 quantum biology paragraph.
Verify anchor coverage against stack chart claims. Implement deep link + share
button. Keep copyable reference under ~2,500 words.

### Phase 2e: Verification
- Full PDF build
- Term introduction audit: verify every formal name has a p1→formal bridge
- Read front matter → pos13 → pos15 → pos20 → pos32 sequentially as GA reader
- Check: no concept used before introduced
- Check: no orphaned references to cut material
- Check: Firmware Update contains all moved material + p3 quantum biology
- Check: deep link and share button functional
- Check: copyable reference under ~2,500 words
- Check: protected passages intact
- Word count verification against targets

## Acceptance Criteria

1. No chapter re-explains a concept the stack chart already planted
2. Every cut is clean — no sentence fragments, no dangling references
3. Transitions between chapters still flow
4. Every formal domain name has a p1→formal bridge (term audit passes)
5. All protected passages intact
6. "?" → "the Flat" reveal preserved and strengthened in Summary
7. Firmware Update chapter contains all technical material moved from body
8. SPIRAL-REPEAT tags reviewed and most removed or compressed
9. Bridge chapters reviewed for obsolete pedagogy
10. Full PDF builds without errors
11. Net word count reduction ≥ 3,000 words
12. GA reader walkthrough (all four personas) finds no comprehension gaps
13. Firmware update deep link functional with share button next to copy button
14. No more than 3 firmware update mentions in entire book
15. p3 quantum biology paragraph present in firmware update (life uses QM,
    topological order is the only new thing, AC bridge is the empty gap)
16. Copyable science reference stays under ~2,500 words after material moves
17. No quantum biology at p1 or p2 — clean "six exist in nature" only
18. Cut p2 content reviewed for onHover resurrection — best explanations
    survive as interactive overlays in HTML version
19. onHover windows sized for 100–300 words + SVG support
