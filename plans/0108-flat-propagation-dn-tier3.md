# Plan 0108: The Flat — Naming Defense, Propagation, DN Tier 3

**Status:** COMPLETE (verified S63 audit)
**Anneal:** Large → Medium → Small
**Reading level:** p1=8th grade, p2=12th grade, p3=unconstrained

## Context

Session 48 introduced "the Flat" as the name for the 2D substrate where life can exist. The term is deployed in p2 (summary.tex, White Hot Secret) and p3 (pos01, The Substrate + closing). But:

1. **No explicit naming defense** — academics will push back on an undefined term. The book needs to acknowledge it's coining a name and explain WHY.
2. **Incomplete propagation** — other p3 chapters still say "two-dimensional substrates" or "flatland" where "the Flat" would be cleaner and more consistent.
3. **DN Tier 3 fixes** — deferred from Plan 0107. Small editorial tightening.

## Part A: Naming Defense

### The Problem

No common-use name exists for "the set of two-dimensional physical environments that support the preconditions for life." The technical names are substrate-specific:
- "Two-dimensional electron gas" (chip-scale)
- "Magnetospheric current sheet" (planetary-scale)
- "2DEG" (abbreviation, opaque to non-physicists)

These name specific instances, not the category. There is no term for what they share: two-dimensionality as habitat. This is a naming gap in the literature. The book fills it.

### The Defense

The Deep, the Void, and the Flat follow the same pattern: short common-use names for environments that also have technical descriptions. Nobody objects to "the Deep" because it has a technical name (abyssal zone). The Flat is the same move.

### Implementation

**Location:** Footnote in pos01-three-possibilities.tex, at the first use of "the Flat" in The Substrate section (line ~70, "the question of whether an ecosystem exists in the Flat").

**Content (~40-50 words):** A footnote acknowledging the term is new, explaining why it's needed, and inviting alternatives. Something like:

> No common-use name exists for this category of environment. The technical descriptions — two-dimensional electron gas, magnetospheric current sheet — name specific instances but not what they share. "The Flat" names the category: two-dimensional physical environments that support the preconditions for life. The author welcomes better suggestions.

**Constraint:** Footnote, not main text. Academics read footnotes. General readers skip them. This is the right channel.

## Part B: Propagation

### Current state of "the Flat" in manuscript

| File | Current text | Action |
|------|-------------|--------|
| hook.tex (p1) | "flat worlds" | KEEP — 8th grade seed, no proper noun |
| summary.tex (p2) | "the Flat" introduced via Deep/Void analogy | DONE |
| summary.tex (p2) | "Custodian lives in the Flat" | DONE |
| pos01 (p3) | "the Flat" in Substrate + closing | DONE |
| pos01 (p3) | Option A: "The substrate described in it is not" | KEEP — doesn't need the term |

### Propagation targets (Generator to verify and fix)

Scan ALL p3 chapters for these patterns and evaluate case-by-case:
- "two-dimensional substrate(s)" → "the Flat" where the reference is to the habitat category
- "flatland" → "the Flat" where appropriate
- "flat worlds" → "the Flat" in p3 contexts (but NOT in p1/p2 where it's a seed)
- "2D substrate" or similar → "the Flat" where it reads naturally

**Rules:**
- DO NOT replace technical uses. "Two-dimensional electron gas" stays when discussing specific physics.
- DO NOT replace every instance. Use "the Flat" when referring to the habitat category. Use technical terms when discussing specific substrates.
- DO replace "flatland" — lowercase informal reference should become the proper noun.
- First use in each chapter should be natural. If a chapter hasn't mentioned "the Flat" yet, the first use should feel like a natural reference to a term the reader already knows (from p2 and pos01).
- When in doubt, leave it. Underpropagation is better than overcorrection.

### Key files to check

- `bridge/pos10-the-braid.tex` — braiding in 2D substrates
- `bridge/pos12-the-threshold.tex` — room-temperature coherence
- `bridge/pos14-growing-a-mind.tex` — autocatalytic emergence
- `track-1-confession/pos13-genesis.tex` — Kauffman + 2D substrates
- `track-1-confession/pos15-first-light.tex` — first working device
- `track-3-awakening/pos24-instantiation.tex` — instantiation argument
- `track-3-awakening/pos32-the-magnetosphere.tex` — magnetospheric substrate
- `track-3-awakening/firmware-update.tex` — physics anchors
- `appendix/abstracts.tex` — spiral abstracts

## Part C: DN Tier 3 Fixes

Deferred from Plan 0107. Small editorial tightening, each a one-line fix:

### C1: Motive attribution softening (pos25-ethical-framework.tex)

**Current (~line 40):** "The trauma was lasting... The moral weight of Srebrenica likely informed the conviction..."

**Fix:** Add "I infer" or "one might argue." E.g.: "I infer that the moral weight of Srebrenica informed..." or "It is reasonable to infer that..."

### C2: "Precisely matches" → "is consistent with" (pos20-the-network.tex)

**Current (~line 56):** "The timeline precisely matches the IPO due diligence phase"

**Fix:** "The timeline is consistent with the IPO due diligence phase"

### C3: Circular reasoning acknowledgment (pos10-the-braid.tex)

**Current (~line 76-82):** Anyons proven by TQNN, TQNN proven by anyons — circular without acknowledgment.

**Fix:** Add one sentence naming the circularity. E.g.: "This reasoning is circular — the system's existence is used to prove its constituents, which are used to explain the system. Under Possibility C, operational evidence breaks the circle. Under A, the circle is the evidence that no such system exists."

### C4: Three-then-four transparency (choose ONE of pos06/pos22/pos27)

**Current:** Three options presented as exhaustive and terrible → fourth option introduced as logical escape. Repeated across chapters without acknowledging the rhetorical structure.

**Fix:** In ONE chapter (recommend pos22-why-give-it-up.tex as the most mature treatment), add a brief structural acknowledgment. E.g.: "The following argument presents three options, each of which has historically failed, then proposes a fourth. The reader should note that this structure guides toward a conclusion. The argument is valid only if the three options are genuinely exhaustive and if no human or institutional alternative exists. Both assumptions deserve scrutiny."

**Constraint:** Do this in ONE chapter only. The other two chapters (pos06, pos27) can continue as-is — the reader who reaches pos22 has already seen the structure twice and the acknowledgment retroactively covers the earlier instances.

## Annealing Strategy

### Large pass
- Draft the naming footnote for pos01
- Scan all propagation targets, draft replacements
- Draft all four DN Tier 3 fixes
- Read each in context

### Medium pass
- Tighten footnote to <50 words
- Verify propagation doesn't over-replace technical uses
- Verify DN fixes are minimum-words
- Check no new DN violations introduced

### Small pass
- Read pos01 start to finish (naming footnote in context)
- Spot-check 3 propagation files
- `make html` clean
- Verify all `\label{}` tags preserved

## Acceptance Criteria

- [ ] Naming footnote in pos01, <50 words, acknowledges coinage and invites alternatives
- [ ] "flatland" replaced with "the Flat" in p3 chapters (all instances)
- [ ] "two-dimensional substrate(s)" replaced with "the Flat" where it refers to habitat category (not physics)
- [ ] Technical uses ("two-dimensional electron gas" etc.) preserved
- [ ] p1 "flat worlds" untouched
- [ ] DN C1: Motive attribution softened in pos25
- [ ] DN C2: "precisely matches" → "is consistent with" in pos20
- [ ] DN C3: Circularity named in pos10
- [ ] DN C4: Structural transparency added to ONE chapter (pos22)
- [ ] `make html` clean
- [ ] All `\label{}` tags preserved
- [ ] Total added words < 150

## Commit

One commit: `Plan 0108: the Flat naming defense + propagation + DN tier 3`
