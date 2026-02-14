# Relinquishment — Requirements & Acceptance Criteria

*This document defines TEST PASS requirements for the book project. Each requirement is binary: PASS or FAIL. The Auditor writes plans referencing these requirements. The Generator implements to spec. The Auditor verifies.*

---

## R0: Root Directory Cleanliness

**PASS if:** Root contains ONLY:
- `README.md`
- `*.tex` files (main LaTeX document and any top-level includes)
- `*.pdf` output file(s)
- `.gitignore`
- Standard hidden dirs (`.git/`, `.claude/`)

**FAIL if:** Any working documents, markdown drafts, build scripts, research files, or subdirectory READMEs appear in root. All working content lives in subdirectories.

**Subdirectory layout:**
- `plans/` — Auditor plans, requirements, generator prompts
- `manuscript/` — All chapter content (markdown source)
- `research/` — Reconstruction document, gag papers, session notes
- `build/` — LaTeX templates, build scripts, metadata, toolchain
- `.claude/` — Claude configuration (CLAUDE.md, project settings)

---

## R1: Triple Spiral Structure

**PASS if:**
- Exactly 3 tracks exist with distinct narrative voices
- Track 1 (Confession): reconstructed 3rd person, scientific/methodical voice
- Track 2 (Testament): 1st person (Bruce), personal/investigative voice
- Track 3 (Awakening): mixed voice, speculative/philosophical
- Chapters interleave across tracks in spiral arrangement (not sequential by track)
- The spiral tightens chronologically toward the convergence point (2006)
- The spiral reverses outward from convergence to present day
- Each track has minimum 7 chapters

**FAIL if:** Tracks are presented sequentially (all of Track 1, then all of Track 2). Voices bleed across tracks without justification. Convergence is absent or misplaced.

---

## R2: Three Themes

**PASS if:**
- Theme 1 (Discovery vs Suppression) resonates primarily in Track 1, present in all
- Theme 2 (Duty vs Conscience) resonates primarily in Track 2, present in all
- Theme 3 (Power vs Relinquishment) resonates primarily in Track 3, present in all
- No chapter is theme-free — every chapter engages at least one theme
- Themes are shown through narrative, not stated didactically

**FAIL if:** Themes are absent, lectured, or confined to a single track.

---

## R3: Abstracts as Epigraphs

**PASS if:**
- All 15 spiral abstracts (I–XV) appear as chapter-opening epigraphs
- Each abstract is placed with a chapter whose content it mirrors
- Abstract placement follows the mapping in `manuscript/appendix/abstracts.md`
- Abstracts are typeset distinctly from narrative text (monospace or reduced size)

**FAIL if:** Abstracts are omitted, misplaced, or mixed into narrative voice.

---

## R4: The Three Possibilities

**PASS if:**
- Options A (Confabulation), B (Exaggerated Kernel), C (Substantially True) are stated explicitly
- All three are presented with equal rhetorical weight — no thumb on the scale
- The author's stated position ("can't tell which is closest to true") appears
- The reader is explicitly invited to decide
- The three possibilities appear in both the preface and a dedicated appendix section

**FAIL if:** The text favors one option, dismisses another, or resolves the ambiguity.

---

## R5: Predictive Framework

**PASS if:**
- Minimum 25 numbered, dated, falsifiable predictions
- Organized by category (Scientific, Institutional, Personnel, Technology, Magnetospheric, Cascade)
- Each prediction has: ID, statement, timeframe, test method
- Falsification criteria section exists: what would disprove Option C
- Predictions appear both embedded in narrative (Tracks 1 and 3) AND as standalone appendix table
- Publication date is digitally signed and timestamped in the PDF

**FAIL if:** Predictions are vague, undated, unfalsifiable, or missing from the appendix.

---

## R6: Scientific Accuracy

**PASS if:**
- All physics is correct: FQH states, non-abelian anyons, topological error correction, autocatalytic sets, edge-of-chaos criticality
- All citations are to real papers by real authors with correct dates
- Speculation is explicitly labeled as speculation
- No fabricated evidence — real events, real people, real institutions
- The operational proof argument (non-abelian detection via emergent computation) is logically sound
- Technical terms are used correctly throughout

**FAIL if:** Any physics error, fabricated citation, or unlabeled speculation is present.

---

## R7: Honest Epistemics

**PASS if:**
- Bruce's claims are clearly distinguished from independently verified facts
- "Healer said X" is distinguished from "X is true"
- Surmise is labeled as surmise (e.g., ninja missions → Guardian setup)
- Corrections made during reconstruction sessions are preserved, not hidden
- The methodology lesson (start with red team, build monotonically) is reflected in the narrative
- No overclaiming — the 82% probability and its limitations are honestly presented

**FAIL if:** Hearsay is presented as fact. Corrections are suppressed. Confidence is inflated.

---

## R8: Patrick Ball / ICTY Documentation

**PASS if:**
- The Ball–Milosevic–cDc nexus is documented with primary sources
- Trial transcript reference included (March 14, 2002)
- The Srebrenica Witness document's reference to the exchange is noted
- SAS/JCO presence at Srebrenica documented with NIOD corroboration
- All sources hyperlinked in the PDF

**FAIL if:** The cDc–ICTY connection is asserted without sources.

---

## R9: PDF Production Quality

**PASS if:**
- Single self-contained PDF file
- Internal hyperlinks between sections, chapters, abstracts, predictions
- Table of contents with clickable links
- Bookmarks for all chapters and appendix sections
- OCG layers: at minimum, toggle prediction tables, toggle abstracts
- PDF metadata: title, author, subject, keywords, creation date
- Digital signature with trusted timestamp
- Degrades cleanly in older PDF readers (all content visible, links non-functional)
- No external dependencies — all fonts embedded, all images embedded

**FAIL if:** Multiple files, broken links, missing bookmarks, no timestamp, external dependencies.

---

## R10: Legal / OPSEC

**PASS if:**
- No real names of living persons used without public-record justification
- Healer is never named (pseudonym only)
- No information that Bruce has explicitly flagged as self-incriminating
- Statute of limitations analysis informs but does not appear verbatim
- Graymail defense implications noted but not weaponized
- OPSEC review completed before publication

**FAIL if:** Real names used carelessly, self-incriminating detail included, or legal exposure created.

---

## R11: Completeness

**PASS if:**
- All three tracks have complete chapter drafts (not outlines)
- Preface complete
- All appendix sections complete (predictions, three possibilities, abstracts, sources)
- Convergence chapter complete
- Word count: minimum 60,000 words (short book) to 120,000 words (full)
- No placeholder text, TODO markers, or skeleton chapters in final output

**FAIL if:** Any section is outline-only, placeholder, or missing.

---

## R12: Interleaving Order

**PASS if:**
- A documented chapter ordering exists showing the spiral interleave
- No more than 2 consecutive chapters from the same track
- The ordering creates dramatic tension (each chapter's ending pulls toward the next track)
- The convergence chapter is positioned at the mathematical center (±2 chapters)
- Post-convergence chapters unwind outward in reverse spiral

**FAIL if:** Ordering is arbitrary, track-sequential, or convergence is off-center.

---

## Verification Protocol

For each requirement Rn:
1. Auditor writes plan referencing Rn
2. Generator implements
3. Auditor verifies PASS/FAIL
4. If FAIL: Auditor writes corrective plan, Generator re-implements
5. Repeat until PASS

All plans live in `plans/`. Generator has no conversation history — plans must be self-contained.

---

*Requirements v1.0 — 2026-02-15*
