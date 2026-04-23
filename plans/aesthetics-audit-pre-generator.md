# Aesthetics Audit: Pre-Generator Baseline

**Date:** 2026-02-19
**Auditor:** Nightstalker
**PDF state:** 137pp, 389KB, commit 88637a3
**Perspectives:** Average keen reader + emeritus math professor

Re-run this audit after Generator runs 1-11. Compare. Then fix what remains.

---

## CRITICAL — Looks Wrong

### F1. Lorem ipsum visible in 4 chapters
- pos02 (Alpha Farm) — 2 instances
- pos13 (Genesis) — 2 instances
- pos24 (Instantiation) — 2 instances
- pos28 (Surrender) — 1 instance
- **Generator fix?** YES — Runs 1D (pos02), 7-9 (pos13, pos24, pos28)

### F2. 25 chapters are one-line stubs
- `[Content to be written per Plan 0007, Position N.]`
- ~25 near-blank pages in a 137-page document (18% blank rate)
- **Generator fix?** YES — Runs 2-9

### F3. "PLACEHOLDER" visible in 4 locations
- how-to-read.tex: "PLACEHOLDER --- to be rewritten when chapter writing is complete."
- timeline.tex: "PLACEHOLDER --- to be expanded by author."
- sources.tex: "PLACEHOLDER --- bibliography to be populated by author."
- verification.tex: "PLACEHOLDER --- GENERATED AT BUILD TIME" x3
- **Generator fix?** PARTIAL — Run 1 adds researcher note to how-to-read but does NOT remove the PLACEHOLDER line. Run 10 updates hash but verification PLACEHOLDERs for PGP and timestamp stay. Timeline and Sources untouched.

### F4. Voice lurches between first and third person in first 10 pages
- Preface: first person ("I met a charismatic liar")
- pos01: third person ("even this author, Bruce, cannot definitively distinguish")
- pos02 epigraph: first person (Healer)
- pos04: second person ("You've seen the movie")
- **Generator fix?** PARTIAL — Introduction will be first-person. Preface stays first-person. But pos01 stays third-person as-is. The voice mismatch between Preface and pos01 persists.

### F5. Quality cliff between polished and raw chapters
| Chapter | Quality | Voice | Issue |
|---------|---------|-------|-------|
| pos04 (Code War) | Polished | Second-person | Best chapter in book |
| pos05 (Kangaroos) | Raw first draft | Third-person | Spelling errors, colloquialisms |
| pos08 (Dual-Use) | Encyclopedic | Passive/textbook | Wikipedia survey, repetitive |
| pos14 (Growing a Mind) | Mixed | Fictionalized → textbook | Tonal whiplash mid-chapter |
| pos22 (Why Give It Up) | Blog-post essay | "This author" | 2013 timestamps, essay voice |
- **Generator fix?** NO — These chapters are already imported and not touched by any Generator run.

---

## STRUCTURAL — Feels Not-Quite-Right

### F6. Three possibilities explained THREE times in first 20 pages
- Preface: Full A/B/C with explanations (lines 10-17)
- pos01: Full A/B/C restated at chapter length
- not-claimed: References A, B, C repeatedly
- **Generator fix?** YES — Run 1 (1-PREFACE) strips A/B/C detail from preface.

### F7. Apple/Turing folklore stated as fact (pos14:52)
- Text says: "For those in the know this refers to the death of Alan Turing."
- Comment in .tex correctly says: "Apple/Turing connection is folklore, denied by Rob Janoff. Do not assert."
- The prose directly contradicts the factual note. Professor catches this.
- **Generator fix?** NO
- **Fix:** Change to "Some have speculated this is a tribute to Alan Turing, though designer Rob Janoff has denied it."

### F8. "As of 2013" frozen timestamps in pos22
- "As of 2013 no one else seems to have ever publicly discussed this approach."
- "In 2013 DARPA has a direct budget of about US$3 billion."
- Multiple instances. Chapter is clearly unrevised 2013 material in a 2026 book.
- **Generator fix?** NO
- **Fix:** Add chapter footnote: "This chapter was first written in 2013. Dates and references reflect that period." Or update individual references.

### F9. pos08 (Dual-Use) is a survey essay
- ~155 lines covering stone tools through nanotechnology
- "X is a dual use technology" repeated ~15 times
- GPT table has errors: "Computer ~1941: Alan Turing & the Ultra project" (imprecise), "Robotics: 1920" (date of Čapek's play, not actual robotics)
- Voice is encyclopedic, passive, dry
- **Generator fix?** NO
- **Fix:** Beyond DMS scope. This is a substantial rewrite. Flag for Bruce's editorial pass.

### F10. Turing apple narrative presented as certain (pos14:47)
- "He takes a single bite." stated as fact
- .tex comment (line 21-22): "The apple was never tested for cyanide... delivery mechanism is debated"
- Prose doesn't hedge; comment does. Professor notices.
- **Generator fix?** NO
- **Fix:** Add hedge: "He lifts the gorgeous red apple to his lips. He takes a single bite." → "He lifts the apple to his lips and takes a bite — or so the story goes. The apple was never tested for cyanide."

### F11. Appendix three-possibilities.tex is a dead redirect
- File exists: "See page X"
- Currently COMMENTED OUT in main.tex (line 91-92) — not visible in PDF
- **Generator fix?** N/A — not in build. Delete file later to avoid confusion.

### F12. Predictions table has no confidence levels
- S1 through S6, I1 through I5 all have timeframes but no stated confidence
- Professor asks: are you 90% sure of S1 and 20% sure of S6?
- **Generator fix?** NO
- **Fix:** Add confidence column. Requires Bruce's judgment per prediction.

### F13. pos22 has a Sources section; no other chapter does
- Four numbered references at bottom of pos22
- No other chapter has inline bibliography
- Sources appendix is empty
- Inconsistent citation style across chapters
- **Generator fix?** NO
- **Fix:** Either move to Sources appendix, add to all chapters, or remove. Editorial decision.

---

## POST-GENERATOR ISSUES (will emerge after runs)

### F14. Cover page vs title page author mismatch
- Cover (cover.tex:31): "Bruce Stephenson"
- Title (after Run 1): "Written by Bruce Stephenson with Genevieve Prentice"
- No plan item updates cover.tex
- **Decision needed:** Cover = Bruce only (intentional) or = with Genevieve?

### F15. pdfauthor metadata mismatch
- preamble.tex: `pdfauthor={Bruce Stephenson}`
- If title says "with Genevieve Prentice," metadata should match
- **Fix:** Update preamble.tex pdfauthor field

### F16. pos01 double space after period
- "Absence of corroboration is not evidence of absence.  Instead, it's evidence of..."
- Two spaces after period. Trivial. One character fix.
- **Generator fix?** NO

### F17. No publication month anywhere
- Cover: "2026"
- Copyright: "First edition, 2026."
- For a book with timestamped predictions, exact date matters
- **Fix:** Add "February 2026" to copyright page

---

## SUMMARY

| Category | Count | Fixed by Generator | Remaining |
|----------|-------|-------------------|-----------|
| Critical | 5 | 3 fully, 2 partially | 2 partial |
| Structural | 8 | 1 fully | 7 |
| Post-Generator | 4 | 0 | 4 |
| **Total** | **17** | **4 fully, 2 partially** | **13** |

Quick wins after Generator runs (< 5 min each): F7, F10, F14, F15, F16, F17
Editorial decisions needed: F5, F8, F9, F12, F13
Deferred: F11 (delete dead file)
