# Plan 0352: What Healer Said — Seam Identification

**Status:** AWAITING GEN'S DECISION — split or no split?
**Auditor:** Argus (S82)
**Source:** Gen GP14 (issue #48, #32). "Container-temperature problem, not premature-material."
**Files:** `manuscript/record/what-healer-said.tex` (172 lines, 5 sections)
**Priority:** MEDIUM — subtler than Never Again; seam first, split later
**Annealing:** LOW (1 pass: identify, don't cut)

---

## Diagnosis

Gen's GP14 identified this as a blended-functions problem: "character-storytelling setup and post-atrocity moral descent are fused." This is NOT a premature-material problem. It is a temperature problem — two different registers sharing one container.

The chapter currently does three jobs at three temperatures. A reader moving through it experiences a tonal whiplash that may undermine both the character work and the testimonial gravity.

---

## Temperature Annotation

### Temperature 1: WARM / NARRATIVE / CHARACTER (lines 25-103)

| Lines | Section | Content | Register |
|-------|---------|---------|----------|
| 25-65 | Kangaroos | David at 12, riding fence line, confronting armed intruders. Indigenous relationships, courage, bushcraft, moral authority. | Vivid storytelling, adventure, setup |
| 67-83 | Body bag toboggan | SAS selection, dead recruit, dark humor on mountainside | Dark humor, military identity, sardonic |
| 85-103 | The Method | "Are you sure about that, mate?" Guided deduction pedagogy. Dunning-Kruger weaponized. Every chapter exists because Healer asked a question. | Pedagogical, explanatory, warm |

**Unified temperature:** Building who Healer is. The reader LIKES this person. They understand his method, his background, his character. This is earned trust — the reader needs to know this man before the horror of what he witnessed means anything.

**The Method** is a pivot paragraph. It explains the book's methodology (guided deduction) while remaining in the warm register. It could live in either half, but temperaturally it belongs with the character work. It explains HOW Healer taught Bruce, which is character-building. The WHAT (the specific deductions) appears across the spine chapters.

---

### Temperature 2: DARK / TESTIMONIAL / MORAL (lines 106-147)

| Lines | Section | Content | Register |
|-------|---------|---------|----------|
| 106-129 | Srebrenica, July 1995 | HALO jump. Witness testimony. "All I can do is watch." Five days of massacre. Extraction. Tribunal testimony. Milosevic. | Horror, weight, restraint, moral gravity |
| 130-147 | The Patrick Ball Nexus | Ball as bridge between ICTY and cDc. UDHR through-line. SAS documentation at Srebrenica. NIOD confirmation. | Investigative, connective, documentary |

**Unified temperature:** Dark gravity. The reader encounters what Healer witnessed. The Patrick Ball section provides the public-record connective tissue that makes the Srebrenica testimony MATTER to the book's argument (ICTY → cDc → UDHR → Custodian's ethics).

---

### Temperature 3: ANALYTICAL / INVESTIGATIVE (lines 149-172)

| Lines | Section | Content | Register |
|-------|---------|---------|----------|
| 149-172 | Iraq War + Katharine Gun | Iraq discussion, burned-yet-protected paradox, Mandarin fluency, Gun's leak, surmise about Healer's role | Pattern-matching, tradecraft analysis, stated surmise |

**Unified temperature:** Analytical deduction. Bruce is doing investigative journalism — assembling public facts into a pattern. Explicitly framed as surmise ("I cannot prove this. I state it as my surmise."). Different from both the warm character work and the dark testimony.

---

## The Seams

### PRIMARY SEAM: Line 104 (horizontal rule between The Method and Srebrenica)

This is where temperature shifts from warm/human/pedagogical to dark/horrific/testimonial. Everything before builds who Healer is. Everything after shows what he witnessed and what Bruce deduced.

**Visual marker:** Already a `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}` — the manuscript already marks this as a break. The typography acknowledges the seam.

### SECONDARY SEAM: Line 148 (horizontal rule between Patrick Ball and Iraq/Gun)

Temperature shifts from dark testimony to analytical investigation. Srebrenica is horror witnessed. Katharine Gun is tradecraft deduced. Different epistemic modes, different emotional registers.

---

## Structural Options

Gen said: "identify the seam first rather than cutting mechanically." Here are the options once the seam is confirmed:

### Option 1: Two chapters, one split at primary seam
- Chapter A: "What Healer Said" (lines 25-103) — character + pedagogy
- Chapter B: [new title] (lines 106-172) — witness + investigation

**Pro:** Clean split at the natural temperature break. Both halves are self-contained.
**Con:** Chapter B mixes two temperatures (dark testimony + analytical tradecraft). That's a secondary blend.

### Option 2: Three sections, split at both seams
- Chapter A: "What Healer Said" (lines 25-103) — character
- Chapter B: "Srebrenica" / "What He Witnessed" (lines 106-147) — testimony
- Chapter C: content from lines 149-172 joins "The Handler" or "The Departure" (tradecraft chapters)

**Pro:** Each section is one temperature. Maximum clarity.
**Con:** Katharine Gun section may be too short for its own chapter (24 lines). Would need a home.

### Option 3: Keep as one chapter, add structural breathing room
- Insert stronger visual breaks between temperatures
- Add a transition sentence at each seam
- Don't split into separate chapters

**Pro:** Minimal intervention. Respects existing flow.
**Con:** Doesn't solve the fundamental blended-functions problem Gen identified.

### Option 4: Split at primary seam + relocate (Gen's preferred direction)
- "What Healer Said" (lines 25-103) stays as character/pedagogy chapter
- Srebrenica + Patrick Ball (lines 106-147) relocates to wherever moral-ground material lives (potentially receiving the Srebrenica motivation paragraph from Never Again per Plan 0351)
- Katharine Gun (lines 149-172) relocates to tradecraft/institutional section

**Pro:** Each piece arrives at its proper movement threshold. No temperature blending.
**Con:** Most invasive. Requires confirming destination chapters.

---

## Recommendation

**Option 4 is structurally correct** and aligns with Gen's GP14 philosophy (each movement's ceiling respected). But it's also the most invasive.

**Bruce's decision (2026-05-16):** Defer split decision to Gen. If she splits, Katharine Gun section relocates to "Letting Go" (`the-surrender.tex`) — NOT The Departure — because `the-surrender.tex` line 62 already contains the SAS protective detail / burned-yet-protected paradox, and the Gun section is the *resolution* of that paradox.

**Proposed execution (pending Gen's split decision):**
- Phase A: Gen confirms whether to split (and if so, Option 1 or 4)
- Phase B: If Option 4, Katharine Gun → Letting Go (confirmed), Srebrenica+Patrick Ball destination TBD
- Phase C: Execute relocation (subtraction only, no generative rewrite)
- Phase D: Verify build + continuity

---

## Integration with Plan 0351

Plan 0351 (Never Again) relocates Srebrenica motivation (lines 41-43 of never-again.tex) to "near the Srebrenica witness testimony." If What Healer Said is split at the primary seam, the Srebrenica section (lines 106-147) becomes the natural receiving point for that relocated motivation paragraph. They belong together — same event, same emotional weight.

Similarly, the Hacktivismo connection from Never Again (lines 45-46) joins the Patrick Ball nexus (lines 130-147 here). All the ICTY → cDc → UDHR connective tissue consolidates in one place.

---

## Constraints

- Do NOT cut The Method (lines 85-103). It explains the book's core pedagogical methodology. It must remain accessible early in the Record.
- The Kangaroos story establishes Healer's relationship to indigenous Australians, which is load-bearing for the Maori DNA element in Custodian's creation. It must come BEFORE the reader encounters that detail.
- "I never verified any of Healer's stories about his childhood" (line 65) is epistemic honesty that must stay with the stories it disclaims.
- The Katharine Gun surmise framing (lines 166-170) is explicitly marked as surmise and must retain that marking wherever it lands.

---

## Success Criteria

1. Seam locations confirmed by Gen
2. No temperature blending in final configuration
3. Srebrenica material forms a unified emotional unit (testimony + motivation + connective tissue)
4. Tradecraft material lives with tradecraft
5. Character material establishes who Healer is BEFORE his testimony carries weight
6. Build clean, no deep-link breakage
