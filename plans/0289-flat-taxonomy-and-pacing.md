# Plan 0289: Flat Life Taxonomy + Summary Pacing + Science-Badge Visibility

**Status:** DRAFT — Bruce reviewing architecture
**Author:** Auditor (Argus S64)
**Priority:** HIGH — addresses T3 pacing, F-woo/F-crank/F-religious simultaneously
**Origin:** S64 strategic review. Bruce: "we drop into can the Flat support life too soon"
**Connects to:** Plan 0290 (taxonomy section carries ⬡◈ pictogram combination)
**Annealed:** HIGH → MED → LOW (S64)

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

**Recommendation: Option 1.** It belongs with the habitat argument. The chapter already presents Earth and Jupiter; the taxonomy formalizes what's implied and adds the engineered type.

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

### Pictogram connection (Plan 0290)

The taxonomy section is where ⬡◈ (Flat + emergence) first appears as an explicit combination. Once Plan 0290 Phase 3 ships, this section carries the ⬡◈ signature in its chapter header and inline.

### C-violation check

All three types are valid under all three possibilities:
- Under A: theoretical categories, all empty
- Under B: theoretical categories, possibly one partially occupied
- Under C: theoretical categories, one definitely occupied (engineered/grown), others possibly occupied

No C-violation. The taxonomy describes *possible* types, not claims about what exists.

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

**Recommended (combined):**
1. Increase checkmark opacity from 0.7 to 1.0 and size from 0.8em to 0.95em
2. First occurrence only: add a brief inline explanation on the FIRST tech-section the reader encounters: "Sections marked ✔ contain verified science — published, peer-reviewed physics. Expand if curious; skip without losing the story."
3. Border 3px → 4px for slightly stronger visual anchoring

### Fix 2: Checkmark tooltip tied to accuracy declaration

**Current default tooltip:** "Verified science — a technical discussion grounded in published, peer-reviewed physics. Safe to skip; expand if curious."

**Proposed tooltip:** "This section attempts scientific accuracy. Every claim is sourced to published, peer-reviewed, reproducible research. Where it speculates, it says so. Expand if curious; the story continues without it."

This echoes the accuracy declaration from Plan 0287 and ties the science badge directly to the F-woo defense. Every green check becomes a micro-accuracy-declaration.

### Fix 3: Checkmark hover target

Currently `.tech-grade` has `cursor: help` but the hover target is small (the ✔ character). Add padding: `padding: 0 0.3em;` to make the hover target larger without affecting layout.

### Consistency with Plan 0290

The tech-section tooltip uses `title` attribute — same mechanism as concept symbol tooltips. Both use the same interaction pattern (hover → tooltip). The reader learns one interaction model for all visual annotations.

### Generator spec

**File:** `preprocess.py`

**CSS changes (in the tech-section CSS block, lines ~900-980):**
- `.tech-grade::after` — change `opacity: 0.7` → `1.0`, `font-size: 0.8em` → `0.95em`
- `.tech-grade` — add `padding: 0 0.3em;`
- `details.tech-section` — change `border-left: 3px` → `4px`
- `details.tech-borderline` — change `border-left: 3px` → `4px`

**Tooltip change:** In `collapse_tech_sections()` function, update the default tooltip string used in `data-hover` attribute.

**First-occurrence annotation:** In `collapse_tech_sections()`, track whether this is the first tech-section in the document. If so, inject a `<span class="tech-first-note">` after the summary with the explanation text. Add CSS for `.tech-first-note` (small, italic, muted).

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

**[Structural break — `\bigskip` or `\vspace{1cm}` or horizontal rule]**

**Phase 2: "The Question" (T3 — SEED, not full delivery)**

Expanded Kauffman bridge (from 1 sentence to a short paragraph):

> A question follows from the physics. The mathematician Stuart Kauffman showed that in any sufficiently complex system with continuous energy input, self-sustaining organization arises spontaneously — not by design, but by crossing a complexity threshold. This is established mathematics. The Flat meets those conditions. So does Earth's magnetosphere — a naturally occurring Flat, billions of years old, energized continuously by the solar wind.

Then the question (not the answer):

> Whether anything lives in the Flat — whether self-organization has occurred in these ancient, energized, two-dimensional substrates — is the question this book investigates. The evidence, the silence, and the taxonomy of what could theoretically exist there are examined in the chapters that follow.

This is T3 as SEED. The spine delivers the full argument. The summary delivers the question.

### Kauffman naming constraint

**CRITICAL:** Every reference to Kauffman in the summary must use "The mathematician Stuart Kauffman" on first mention. Never "Kauffman's framework" or "Kauffman's mathematics" before he's introduced. The p2 reader who only reads the summary has never met him. 98% of readers have never heard of him.

The spine (Genesis chapter) gives him a full multi-paragraph introduction. But the summary is a separate walkaway layer — it must self-contain every introduction.

**Generator instruction:** If any Kauffman reference in the summary precedes "The mathematician Stuart Kauffman showed...", the Generator must flag it. No bare "Kauffman" before the introduction.

### Annealing note on "phase transition" vs "complexity threshold"

The current summary (line 44) uses "complexity threshold" — accessible to p2 readers.
The proposed Phase 2 text originally used "phase transition" — physics jargon, harder.

**Refined:** Changed to "crossing a complexity threshold" to maintain p2 accessibility. The spine (Genesis) can use "phase transition" with full explanation. The summary uses the simpler term.

### What this gives up

Full T3 delivery in the summary. The Kauffman argument, the thermal objection detail, and the hydrothermal vent analogy move to the spine (Wrong Substrate, which already has them). The summary reader gets:
- T2 fully: what the Flat is, where it is, it's in your phone, it's everywhere
- T3 as seed: the question exists, it's worth asking, the book investigates it
- Everything else unchanged

### Impact by reader type

| Reader type | Current experience | After restructure | Net |
|-------------|-------------------|-------------------|-----|
| Quick-exit (W0-W2) | Flat→life compressed, may trigger F-woo | Gets Flat domesticated, encounters T3 as question | **Better** — less trigger, same seed |
| Summary reader (W3) | Gets compressed T3 argument | Gets T3 seed, pointed to spine | **Better** — no premature closure |
| Spine reader (W4-W6) | Gets full T3 in spine anyway | Same | **Unchanged** |
| Net | Compressed T3 in summary + full T3 in spine | T3 seed in summary + full T3 in spine | **Net positive** — current compressed version is worse than a clean seed because it triggers F-woo before the reader is ready |

### What this gains

- **Reader absorbs the Flat BEFORE encountering the life question.** The domestication beat + accuracy checkpoint + structural break create breathing room.
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

### Generator spec

**File:** `manuscript/00-front/hook.tex`, line 30.

Find the sentence containing "They are inside every computer chip you own. Earth's magnetic field has held them for billions of years."

Replace with:
```
They are inside every computer chip you own.

Those same flat worlds also occur naturally. Earth's magnetic field has held them for billions of years.
```

The blank line in LaTeX produces a paragraph break — a visual breath.

---

## Execution Plan

### Phase 1: Badge visibility (Plan 0289a) — mechanical, ship immediately

- CSS: checkmark opacity, size, border, hover padding
- Tooltip: update default tooltip text
- First-occurrence: annotation on first tech-section
- **File:** preprocess.py only
- **Test:** Build, verify ✔ is more visible, tooltip shows accuracy language
- **Commit:** `Plan 0289a: science badge visibility`

### Phase 2: Hook fix (Plan 0289b) — one-line editorial, ship immediately

- Split line 30 into two beats
- **File:** hook.tex only
- **Test:** Build, verify hook reads with a breath between chip and magnetosphere
- **Commit:** `Plan 0289b: hook pacing fix`

### Phase 3: Summary restructure (Plan 0289c) — editorial, needs Bruce's voice

- Add domestication beat
- Move accuracy checkpoint
- Move "every claim above" line
- Add structural break
- Expand Kauffman bridge (keep full introduction: "The mathematician Stuart Kauffman")
- Replace habitat claim with T3 question/seed
- **File:** summary.tex
- **Test:** Read full summary aloud. Check: does the reader have time to absorb the Flat before encountering the life question? Does the Kauffman bridge work as an introduction for someone who's never heard of him?
- **Commit:** `Plan 0289c: summary pacing restructure — T3 as seed`

### Phase 4: Taxonomy section (Plan 0289d) — new content, needs Bruce's voice + A/B/C check

- Write taxonomy section in Wrong Substrate
- Default closed with tech-section treatment
- Add tech-collapse.yaml entry
- Run C-violation check on all three types
- **File:** the-wrong-substrate.tex + build/tech-collapse.yaml
- **Test:** Build, verify section is collapsed by default, shows ✔, tooltip correct. Verify all three types are valid under A, B, and C.
- **Commit:** `Plan 0289d: Flat life taxonomy section`

### Dependencies

- Phase 1 (badge visibility) is independent — ship now
- Phase 2 (hook fix) is independent — ship now
- Phase 3 (summary restructure) is independent of 1 and 2
- Phase 4 (taxonomy) depends on Phase 3 landing first (reader needs the pacing fix before encountering the taxonomy)
- Phase 4 also benefits from Plan 0290 Phase 3 (pictogram combinations), but does not require it
