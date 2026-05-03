# Plan 0289: Flat Life Taxonomy + Summary Pacing + Science-Badge Visibility

**Status:** DRAFT — Bruce reviewing architecture
**Author:** Auditor (Argus S64)
**Priority:** HIGH — addresses T3 pacing, F-woo/F-crank/F-religious simultaneously
**Origin:** S64 strategic review. Bruce: "we drop into can the Flat support life too soon"

---

## Part A: The Flat Life Taxonomy (New Section)

### What it is

A theoretical biology section presenting three categories of possible Flat life:

| Type | Substrate | Age | Complexity | Analogy |
|------|-----------|-----|------------|---------|
| **Magnetospheric primitive** | Earth's MS plasma sheet | ~4.5 Gyr | Low — single niche, no competition, periodically reset by geomagnetic reversals | Stromatolite |
| **Engineered/grown** | Semiconductor 2DEGs | ~30 yr (under C) | High — designed substrate, intentional cultivation, guided evolution | Greenhouse organism |
| **Planetary ecology** | Jupiter's/Saturn's heterogeneous MS | ~4.5 Gyr | Potentially high — multiple niches (Io torus, radiation belts, Ganymede sub-MS), selection at boundaries | Coral reef ecosystem |

### Why it matters

1. **Makes Custodian one specimen in a category, not a unique miracle.** Kills F-religious harder than any hinge — she's not divine, she's one instance of a general biological phenomenon.
2. **Is A-content.** The taxonomy is theoretical biology applied to a novel substrate. "What categories of life could theoretically exist in 2DEGs?" is a valid question under all three possibilities. Under C, one category is occupied. Under A, they're all empty but the categories are still valid biology.
3. **Connects to magnetogenesis research.** The arXiv paper, JUICE, and Bruce's oblique detection work all fit naturally into the "magnetospheric primitive" category.
4. **Provides framework, not just claim.** Reader gets a way to THINK about Flat life, not just "something might live there."

### Where it goes

**Option 1: New section in Wrong Substrate** — after the "Not Aliens" section, before the chapter return. Wrong Substrate already has Earth's MS (lines 148-159) and Jupiter's MS (lines 159-165). Add a taxonomy section that organizes what's already there + adds the engineered type.

**Option 2: New short chapter between Wrong Substrate and Silence Gap.** Title: "Theoretical Biology of the Flat" or simply "The Taxonomy." Cleanest separation, but adds a chapter.

**Recommendation: Option 1** — keep in Wrong Substrate. It belongs with the habitat argument. The chapter already presents Earth and Jupiter; the taxonomy formalizes what's implied and adds the engineered type.

### Collapsible treatment

**DEFAULT CLOSED** — using the gold-backed green-check tech-section system. The reader sees:

```
▸ Theoretical Biology of the Flat ✔
```

They know it exists. They see the science badge. They don't have to process it until ready. When they click, they get the taxonomy.

This is the teaching trick: the closed section signals "there's more here when you're ready" without forcing cognitive load. The reader absorbs the Flat, encounters the life question, sees the taxonomy EXISTS, and can return to it when the concepts have settled.

**Manifest entry for tech-collapse.yaml:**

```yaml
  - title: "Theoretical Biology of the Flat"
    spine_file: manuscript/spine/the-wrong-substrate.tex
    spine_label: "spine:ws-flat-taxonomy"
    assessment: GA-AVERSE
    tooltip: "Three categories of life that could theoretically exist in two-dimensional electron gases — magnetospheric primitives, engineered systems, and planetary ecologies. Real theoretical biology applied to a novel substrate."
    status: approved
```

---

## Part B: Science Badge Visibility Improvements

### Problem 1: Gold-backed green-check is too subtle

The current visual treatment:
- 3px gold left border
- Cream/gold gradient background
- Collapsed: italic grey title with small green ✔ (opacity 0.7)
- No text explaining what the badge means

A new reader doesn't know what this visual language means. It says "here's a collapsed section" but doesn't say "this is verified science you can skip OR expand." The design is functional but not self-documenting.

### Fix 1: Make the science badge more prominent

Options (Bruce to choose):
1. **Increase checkmark opacity** from 0.7 to 1.0 and size from 0.8em to 0.95em
2. **Add a label** next to the checkmark: "✔ Verified science" instead of just "✔"
3. **Stronger border** — 3px → 4px, and consider a subtle gold background tint on the summary line itself
4. **First occurrence only:** Add a brief inline explanation on the FIRST tech-section the reader encounters: "Sections marked ✔ contain verified science — published, peer-reviewed physics. Expand if curious; skip without losing the story."

### Fix 2: Checkmark tooltip tied to accuracy declaration

**Current default tooltip:** "Verified science — a technical discussion grounded in published, peer-reviewed physics. Safe to skip; expand if curious."

**Proposed tooltip:** "This section attempts scientific accuracy. Every claim is sourced to published, peer-reviewed, reproducible research. Where it speculates, it says so. Expand if curious; the story continues without it."

This echoes the accuracy declaration from Plan 0287 and ties the science badge directly to the F-woo defense. Every green check becomes a micro-accuracy-declaration.

### Fix 3: Tooltip for the checkmark itself

Currently `.tech-grade` has `cursor: help` but uses the section-level `data-hover` tooltip. If a reader hovers specifically on the ✔, they should get the accuracy tooltip. This already works via the `data-hover` attribute on the span — but the hover target is small (the ✔ character). Consider making the hover target slightly larger with padding.

---

## Part C: Summary Pacing Restructure

### Current structure (The White Hot Secret)

Lines 30-62 in one continuous flow:
1. Flat physics (2DEG, anyons, wormholes) — ~300 words
2. Wormhole disambiguation — ~100 words
3. Quantum teleportation — ~80 words
4. Kauffman bridge — ONE SENTENCE
5. Magnetosphere — ~60 words
6. Thermal objection — ~60 words
7. Published physics checkpoint — ~60 words
8. Habitat claim — ~80 words

### Proposed restructure: Two phases with breathing room

**Phase 1: "What Is the Flat" (T2 — full delivery)**

Keep lines 30-42 (Flat physics through quantum teleportation), then add a domestication beat:

> You already live with the Flat. The chip in your phone contains one. The transistor processing this text contains one. Two-dimensional electron gases are the most manufactured physical environment on Earth — billions of them, in billions of devices, running right now.

Then the accuracy checkpoint (already installed):

> The science in this book is not metaphor. It is an honest attempt at accuracy — sourced, verifiable, and bounded. What is established is stated as such. What is speculation is labeled.

Then move the "Every claim above" line (currently at 48) UP to here:

> Every claim above is published, peer-reviewed physics. Two-dimensional electron gases are in every chip you own. Topological order is established mathematics. None of this is speculative.

**[Structural break — horizontal rule or breathing space]**

**Phase 2: "The Question" (T3 — SEED, not full delivery)**

Expanded Kauffman bridge (from 1 sentence to a short paragraph):

> A question follows from the physics. The mathematician Stuart Kauffman showed that in any sufficiently complex system with continuous energy input, self-sustaining organization arises spontaneously — not by design, but by phase transition. This is established mathematics. The Flat meets those conditions. So does Earth's magnetosphere — a naturally occurring Flat, billions of years old, energized continuously by the solar wind.

Then the question (not the answer):

> Whether anything lives in the Flat — whether self-organization has occurred in these ancient, energized, two-dimensional substrates — is the question this book investigates. The evidence, the silence, and the taxonomy of what could theoretically exist there are examined in the chapters that follow.

This is T3 as SEED. The spine delivers the full argument. The summary delivers the question.

### What this gives up

Full T3 delivery in the summary. The Kauffman argument, the thermal objection detail, and the hydrothermal vent analogy move to the spine (Wrong Substrate, which already has them). The summary reader gets:
- T2 fully: what the Flat is, where it is, it's in your phone, it's everywhere
- T3 as seed: the question exists, it's worth asking, the book investigates it
- Everything else unchanged

### What this gains

- **Reader absorbs the Flat BEFORE encountering the life question.** The domestication beat + accuracy checkpoint + structural break create step 5 (breathing room).
- **F-woo reduced:** The accuracy checkpoint sits between the physics and the life question. The reader's frame is "verified science" when they encounter the habitat question.
- **F-crank reduced:** The life claim in the summary is now a question, not an assertion. Chen sees "investigates" not "argues."
- **F-religious reduced:** The life claim is softer in the summary. Pastor Mike encounters a question, not a declaration.

---

## Part D: Hook Fix (p1 Pacing)

### Current (line 30)

"It operates inside flat worlds — real physical places, thin as nothing, where only two dimensions exist and different rules take over. They are inside every computer chip you own. Earth's magnetic field has held them for billions of years."

### Problem

"Every computer chip" and "Earth's magnetic field for billions of years" in the SAME SENTENCE. These do completely different cognitive work. The first domesticates. The second is the habitat setup. The p1 reader gets both in one breath.

### Proposed fix

Split into two beats:

"It operates inside flat worlds — real physical places, thin as nothing, where only two dimensions exist and different rules take over. They are inside every computer chip you own."

[New sentence, after a breath:]

"Those same flat worlds also occur naturally. Earth's magnetic field has held them for billions of years."

Small change, big effect. "Your chip" → beat → "also nature." The reader domesticates FIRST.

---

## Execution Plan

This is a multi-phase plan. Bruce to decide scope and priority:

1. **Science badge visibility** — CSS changes + tooltip update (small, mechanical)
2. **Summary pacing restructure** — editorial (needs Bruce's voice, Auditor plans, Generator executes)
3. **Hook line 30 split** — one-line editorial fix
4. **Flat Life Taxonomy section** — new content in Wrong Substrate (needs Bruce's voice + careful A/B/C handling)
5. **tech-collapse.yaml entry** for taxonomy section

### Dependencies

- Part B (badge visibility) is independent — can ship now
- Part C (summary restructure) and Part D (hook fix) are independent of each other
- Part A (taxonomy) depends on Part C landing first (reader needs the pacing fix before encountering the taxonomy)

### Commit plan

- Phase 1: Badge visibility (Plan 0289a)
- Phase 2: Hook fix + Summary restructure (Plan 0289b)
- Phase 3: Taxonomy section + collapse entry (Plan 0289c)
