# Aesthetics Audit: Post-Generator Comparison

**Date:** 2026-02-19
**Auditor:** Nightstalker
**PDF state:** 195pp, 655KB (up from 137pp, 389KB)
**Generator batches:** 5 (front matter, Batch 2-4 chapter content, Batch 5 RLHF appendix + hash)
**Files read for this audit:** 22 .tex files across all tracks + front/back matter

---

## COMPARISON TABLE: F1-F17

| Finding | Pre-Generator Status | Post-Generator Status | Action Needed? |
|---------|---------------------|----------------------|----------------|
| **F1. Lorem ipsum in 4 chapters** | pos02, pos13, pos24, pos28 all had lorem ipsum | **pos02 FIXED** (Alpha Farm rewritten). **pos13, pos24, pos28 STILL HAVE LOREM IPSUM.** pos13 has 5 paragraphs of lorem. pos24 has 4 paragraphs. pos28 has 1 paragraph. | **YES -- CRITICAL.** 3 chapters still have visible lorem ipsum in the PDF. |
| **F2. 25 chapters are one-line stubs** | 25 near-blank pages | **FIXED.** All 25 stub chapters now have substantive content. No `[Content to be written]` text remains anywhere. | No. |
| **F3. PLACEHOLDER visible** | 4 locations: how-to-read, timeline, sources, verification | **PARTIAL.** how-to-read.tex line 7 still says `PLACEHOLDER --- to be rewritten`. timeline.tex and sources.tex still say `PLACEHOLDER`. Verification PLACEHOLDERs removed (replaced with git hash mechanism). | **YES.** 3 PLACEHOLDERs remain visible in PDF. |
| **F4. Voice lurches (1P vs 3P)** | Preface 1P, pos01 3P, pos02 epigraph 1P, pos04 2P | **IMPROVED.** Introduction is now strong first-person. Preface is clean first-person. Genevieve preface is appropriate third-person (distinct voice). pos01 still uses third-person ("this author, Bruce"). The lurch between Introduction (1P) and pos01 (3P) remains. | **YES -- editorial.** pos01 third-person is now more jarring against the strong 1P Introduction. |
| **F5. Quality cliff between polished and raw** | pos04 polished, pos05/pos08/pos14/pos22 raw/encyclopedic | **NOT FIXED.** These chapters were not touched by any Generator batch. pos08 is still an encyclopedic survey. pos14 still has the fictionalized Turing narrative with factual errors. pos22 is still 2013-era blog prose. pos05 (Kangaroos) was removed from build but the file still exists. | **YES -- editorial pass needed.** These are Bruce's domain. |
| **F6. Three possibilities explained 3x** | Preface, pos01, not-claimed all had full A/B/C | **FIXED.** Preface now references "three possibilities" without repeating A/B/C detail. Introduction carries the full explanation. pos01 has A/B/C at chapter length (appropriate -- it IS the chapter). not-claimed references but does not re-explain. Repetition reduced from 3x to appropriate layering. | No. |
| **F7. Apple/Turing folklore stated as fact** | pos14:52 asserts connection | **NOT FIXED.** pos14 line 52 still reads: "For those in the know this refers to the death of Alan Turing." The factual note in the comment (line 51) correctly flags it as folklore denied by Rob Janoff, but the prose contradicts the note. | **YES -- quick fix.** Change to hedged language. |
| **F8. "As of 2013" frozen timestamps** | pos22 has multiple 2013 dates | **NOT FIXED.** pos22 line 22: "In 2013 DARPA has a direct budget of about US$3 billion." pos22 line 75: "As of 2013 no one else seems to have ever publicly discussed this approach." Multiple present-tense 2013 references in a 2026 book. | **YES -- editorial.** Add vintage note or update. |
| **F9. pos08 is a survey essay** | 155 lines, repetitive "X is dual use" | **NOT FIXED.** pos08 is untouched. Still encyclopedic, passive, with GPT table errors (Computer ~1941, Robotics 1920). 156 lines. | **YES -- editorial rewrite.** Beyond DMS scope. |
| **F10. Turing apple presented as certain** | pos14:47 | **NOT FIXED.** pos14 line 47: "He takes a single bite. He relishes the taste of bitter almonds." Presented as fact. The .tex comment flags uncertainty but prose is definitive. | **YES -- quick fix.** Add hedge. |
| **F11. Appendix three-possibilities.tex dead redirect** | File exists, commented out of build | **UNCHANGED.** File still exists. Still commented out. Harmless but confusing to anyone reading source. | **LOW -- delete file.** |
| **F12. Predictions table has no confidence levels** | S1-S6, I1-I5 with timeframes but no confidence | **NOT FIXED.** Predictions table has been expanded (now 5 categories: Scientific, Institutional, Personnel, Technology Anomalies, Magnetospheric) but still no confidence column. | **YES -- requires Bruce's judgment.** |
| **F13. pos22 has Sources section; no other chapter does** | Inconsistent citation style | **PARTIALLY WORSE.** pos08 also has a Sources section (4 items). pos22 has Sources (4 items). No other chapter has inline bibliography. The sources appendix (sources.tex) is still a PLACEHOLDER. Two chapters with sources, 33 without. | **YES -- editorial decision.** |
| **F14. Cover vs title author mismatch** | Cover: "Bruce Stephenson" / Title: "with Genevieve Prentice" | **NOT FIXED.** cover.tex line 31: "Bruce Stephenson". title.tex line 35: "Written by Bruce Stephenson with Genevieve Prentice". Intentional or oversight? | **DECISION NEEDED.** |
| **F15. pdfauthor metadata mismatch** | preamble.tex: pdfauthor={Bruce Stephenson} | **NOT FIXED.** build/preamble.tex line 42: `pdfauthor={Bruce Stephenson}`. Title page says "with Genevieve Prentice." Metadata should match. | **YES -- quick fix.** |
| **F16. pos01 double space after period** | Line 24, two spaces after "absence." | **NOT FIXED.** pos01 line 24: "Absence of corroboration is not evidence of absence.  Instead" -- two spaces still present. | **YES -- trivial.** |
| **F17. No publication month** | Cover: "2026", Copyright: "First edition, 2026." | **NOT FIXED.** cover.tex: "2026". copyright.tex: "First edition, 2026." No month. For a book with timestamped predictions, "February 2026" matters. | **YES -- quick fix.** |

---

## NEW FINDINGS (Post-Generator)

### F18. GENERATOR TODO comment visible in pos22 source (NEW)
- pos22 lines 37-41: A 5-line `% GENERATOR TODO: Insert PKC technical section here` comment. While this is only visible in source (not PDF), it indicates planned content that was never written. The same TODO exists in the source markdown. The PKC section is a gap in the pedagogical spiral.
- **Action:** Write the PKC section or remove the TODO and note the gap.

### F19. "DMS MVP import -- not final prose" comment in 25 chapters (NEW)
- Every Generator-populated chapter (Batches 2-4) has `% DMS MVP import from staging/raw/ --- not final prose` on line 6. This is appropriate as a source comment and invisible in PDF. However, 4 chapters also have a **visible** italicized notice in the PDF: "Source material collected for this chapter. The following is structured source material; narrative prose is under development."
- Affected: pos10 (The Braid), pos26 (Interdiction), pos30 (Unipolar Condition), pos32 (The Magnetosphere).
- **Action:** Remove visible "source material" notices or convert to proper prose.

### F20. DMSRedacted blocks reference WikiLeaks chapter (NEW)
- 4 `\DMSRedacted{}` blocks across pos20 (2 instances) and pos29 (2 instances) all say: "See the chapter titled 'WikiLeaks' for the author's note on this deferral."
- The WikiLeaks chapter (wikileaks.tex) exists and is only 3 lines of content: "The author has material on this topic that he has chosen not to include in this edition." This is clean and appropriate.
- **Action:** None needed. The redaction + deferral pattern is coherent. Verify it renders well in PDF.

### F21. Content duplication between pos06 and pos15 (NEW)
- pos06 (The Secret) section "The Reconstructed Model" (lines 64-82) and pos15 (First Light) section "The Emergence Mechanism" (lines 14-26) contain nearly identical content: same substrate/generation/emergence/nature/tuning/control description list, same "key insight" paragraph.
- This is the same material imported from HEALER-RECONSTRUCTION.md into two different chapters. A reader hitting pos15 nine chapters after pos06 reads the same technical description verbatim.
- **Action:** Differentiate. pos06 should introduce at high level; pos15 should go deeper with new detail. Or consolidate into one location with a cross-reference.

### F22. pos03 (The Mentor) has spelling errors and raw draft quality (NEW)
- Line 22: "New South Whales" (should be Wales)
- Line 31: double period ".."
- Line 44: "tresspassers" (should be trespassers, repeated line 48)
- Line 68: "Mujahadeen" (should be Mujahideen)
- Line 84: "Operation Dessert Shield" (should be Desert Shield)
- Line 92: "epiphane" (should be epiphany), "decied" (should be decided)
- Line 70: "operate ," (extra space before comma)
- This chapter is raw biography import. Voice is third-person omniscient for the first half, then switches to first-person Bruce memoir. The tonal whiplash is significant.
- **Action:** Spelling fixes are quick wins. Voice unification is editorial.

### F23. pos22 (Why Give It Up) is 196 lines -- longest chapter by far (NEW)
- pos22 is approximately 8,500 words. Most Generator-populated chapters are 1,000-2,500 words. The original pre-Generator chapters (pos04, pos08, pos14) are 2,000-5,000 words. pos22 is an outlier at nearly double the next longest.
- This is the complete "ch3-relinquishment" source dump. It reads as a standalone essay, not as a chapter in a spiral pedagogy. It front-loads the entire COWS story, relinquishment mechanism, and Guardian creation -- material that the pedagogical spiral is supposed to teach incrementally across tracks 1 and 3.
- **Action:** This is the structural outlier the pre-Generator audit flagged as F9's sibling. Needs editorial decision: split, trim, or restructure.

### F24. WikiLeaks chapter is 3 lines (too short) (NEW)
- wikileaks.tex has exactly 3 lines of content + a `\chapterreturn`. In the PDF this is a chapter heading with one sentence and a blank page. The chapter is intentionally deferred, but a full chapter page for one sentence is aesthetically poor.
- **Action:** Either expand the deferral note (explain WHY it's deferred -- safety of individuals), or demote from chapter to a section/note within an adjacent chapter.

### F25. \srcnote annotations throughout all DMS chapters (NEW, GOOD)
- 75 `\srcnote` annotations across 25 chapters. These are hidden PDF annotations recording provenance. This is excellent for the researcher audience and was specified in the how-to-read guide. No action needed -- noting as a positive.

---

## SUMMARY

| Category | Pre-Generator Count | Fixed | Partially Fixed | Not Fixed | New Issues |
|----------|-------------------|-------|-----------------|-----------|------------|
| Critical (F1-F5) | 5 | 2 (F2, F6) | 2 (F3, F4) | 1 (F5) | -- |
| Structural (F6-F13) | 8 | 1 (F6) | 0 | 7 | -- |
| Post-Generator (F14-F17) | 4 | 0 | 0 | 4 | -- |
| New (F18-F25) | -- | -- | -- | -- | 8 (1 good) |
| **Total** | **17** | **3** | **2** | **12** | **7 needing action** |

### Quick wins (< 5 min each, Generator-fixable)
- F1: Remove lorem ipsum from pos13, pos24, pos28 (3 files)
- F3: Remove 3 PLACEHOLDER lines (how-to-read, timeline, sources)
- F7: Hedge Apple/Turing folklore in pos14
- F10: Hedge Turing apple certainty in pos14
- F15: Update pdfauthor to include Genevieve
- F16: Remove double space in pos01
- F17: Add "February" to copyright and cover year
- F19: Remove 4 visible "source material" notices
- F22: Fix spelling errors in pos03 (7 corrections)

### Editorial decisions needed (Bruce only)
- F4: Unify voice in pos01 (currently 3P against 1P Introduction)
- F5: Quality pass on pos08, pos14, pos22 (encyclopedic/raw)
- F8: Handle 2013 timestamps in pos22
- F9: Rewrite or trim pos08 dual-use survey
- F12: Add confidence column to predictions
- F13: Standardize citation approach (inline vs appendix)
- F14: Cover authorship decision (Bruce only vs with Genevieve)
- F21: Resolve pos06/pos15 content duplication
- F22: Voice unification in pos03
- F23: pos22 structural outlier (8,500 words, front-loads spiral)
- F24: WikiLeaks chapter too short for standalone chapter page

### Deferred
- F11: Delete dead three-possibilities.tex appendix file
- F18: Write PKC section or remove TODO
