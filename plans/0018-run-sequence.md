# Plan 0018: Generator Run Sequence (5-Batch)

**Auditor:** Nightstalker
**Date:** 2026-02-19
**Master plan:** `plans/0018-dms-mvp-content-import.md`

Each batch below is a separate Generator shell session. Copy-paste the handoff prompt. Wait for completion. Verify. Then start the next batch.

**Build verification after every batch:** `make` must succeed with zero errors. Check page count increases. Spot-check the PDF.

---

## Batch 1: Phase 1 — Front Matter (11 items)

**Scope:** pdfcomment + redaction macro, how-to-read researcher note, Genevieve preface, Bruce preface strip, copyright fix, title page, main.tex reorder, introduction + anti-politicization, corrections page, Coventry fix, Alpha Farm fix
**Files created:** 3 new .tex files (genevieve-preface, introduction, corrections)
**Files modified:** main.tex, preface.tex, copyright.tex, title.tex, preamble.tex, how-to-read.tex, pos04-the-code-war.tex, pos02-alpha-farm.tex
**Expected result:** ~155-170 pages (from 137)
**IDEMPOTENCE WARNING:** This batch creates new files AND modifies main.tex. If it fails partway, discard all changes before retrying: `git checkout -- . && git clean -fd`

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 1 in this order:
- 1-PRE: Add \DMSRedacted{} macro AND \usepackage{pdfcomment} + \srcnote{} macro to build/preamble.tex per plan
- 1-HOW: Append "A note for researchers" subsection to manuscript/00-front/how-to-read.tex per plan
- 1-GEN: Create manuscript/00-front/genevieve-preface.tex from content in the plan
- 1-PREFACE: Strip A/B/C detail from manuscript/00-front/preface.tex per plan instructions
- 1-COPYRIGHT: Narrow AI disclosure in manuscript/00-front/copyright.tex per plan instructions
- 1-TITLE: Update byline in manuscript/00-front/title.tex to "Written by Bruce Stephenson with Genevieve Prentice"
- 1-MAIN: Replace front matter includes in main.tex with the EXACT sequence in the plan (Gen preface → Bruce preface → not-claimed → introduction → corrections)
- 1A: Create manuscript/00-front/introduction.tex from content in the plan (includes "A Warning About Certainty" section). Convert to first-person voice throughout — use "I" and "my mentor", not "Bruce" or "Bruce's mentor". Do NOT modify main.tex — 1-MAIN already handles the include order.
- 1B: Restructure the Coventry section in manuscript/bridge/pos04-the-code-war.tex per plan instructions
- 1C: Create manuscript/00-front/corrections.tex from content in the plan
- 1D: Replace lorem ipsum in manuscript/track-2-testament/pos02-alpha-farm.tex per plan instructions

CONVENTIONS:
- Use "proposition" not "claim" when describing Bruce's interpretations (but preserve "claim" in titles like "What This Book Does Not Claim")
- First-person voice in all front matter
- Read existing .tex files (preface.tex, pos04-the-code-war.tex) to match formatting style

Build with `make` after all items. Run test cases T1.1-T1.10.
If build fails partway, discard changes (`git checkout -- . && git clean -fd`) before retrying.
Commit: "Plan 0018 batch 1: front matter — Gen preface, introduction, corrections, Coventry fix, Alpha Farm fix, pdfcomment annotations"
Report: page count, file size, any test failures.
```

---

## Batch 2: Phase 2A+2B+2C — 6 Primary Chapters

**Scope:** pos03 + pos06 (linked — WHS cross-file move), pos07 + pos09, pos18 + pos19
**Files modified:** 6 .tex files
**Key instruction:** Process pos03 FIRST — extract White Hot Secret section, use it when writing pos06.
**Expected result:** ~30-45 pages added

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.1 through 2.6 (six chapters total):
- 2.1: pos03-the-mentor
- 2.2: pos06-the-secret
- 2.3: pos07-the-departure
- 2.4: pos09-the-factoring-game
- 2.5: pos18-the-walk-out
- 2.6: pos19-patrick-ball

For each chapter:
1. Read the FULL staging file in manuscript/staging/raw/ (not just the first 40 lines)
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan (sections "Chapter 2.1" through "Chapter 2.6")
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure
6. Add \srcnote{} annotation at each import point per Generator Conventions

IMPORTANT ORDER: Process pos03 FIRST. The plan says to move the "White Hot Secret" section from pos03's staging to pos06. Extract it during pos03 processing, then use it when writing pos06. After that, process the remaining four chapters in any order.

Read manuscript/bridge/pos04-the-code-war.tex and manuscript/track-2-testament/pos05-the-stories.tex as style references for LaTeX formatting.

Build with `make` after all six chapters. Fix any LaTeX errors.
Commit: "Plan 0018 batch 2: primary imports — pos03, pos06, pos07, pos09, pos18, pos19"
Report: page count, file size, any build errors.
```

---

## Batch 3: Phase 2D+2E — 4 Chapters + WikiLeaks Deferral

**Scope:** pos25 + pos29 (WikiLeaks redaction) + WikiLeaks deferral chapter + pos34 (word budget) + pos35 (fiction)
**Files created:** 1 new .tex file (wikileaks.tex)
**Files modified:** 4 .tex files + main.tex
**IDEMPOTENCE WARNING:** This batch creates wikileaks.tex AND modifies main.tex. If it fails partway, run `git revert HEAD` before retrying.
**Expected result:** ~20-28 pages added

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.7 through 2.10, PLUS the WikiLeaks deferral chapter:
- 2.7: pos25-ethical-framework
- 2.8: pos29-the-silence (SPECIAL HANDLING — see below)
- WikiLeaks deferral chapter (NEW FILE — see below)
- 2.9: pos34-the-research (WORD BUDGET — see below)
- 2.10: pos35-the-question

For each chapter:
1. Read the FULL staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure
6. Add \srcnote{} annotation at each import point per Generator Conventions

THREE SPECIAL INSTRUCTIONS:

(A) pos29 — CRITICAL: Read "Special Instructions: pos29-the-silence" in the plan. You MUST strip all WikiLeaks/Assange content and replace with \DMSRedacted{Content relating to subsequent transparency initiatives has been removed from this edition. See the chapter titled ``WikiLeaks'' for the author's note on this deferral.}. SKIP Sources 3 and 4 entirely — same redaction marker. Keep the silence/isolation narrative, David assessment, and "this story will be my life's work."

(B) WikiLeaks deferral chapter: Create manuscript/track-2-testament/wikileaks.tex per "Special Instructions: WikiLeaks Deferral Chapter" in the plan. Add \include{manuscript/track-2-testament/wikileaks} to main.tex AFTER pos29-the-silence and BEFORE pos30-unipolar-condition.

(C) pos34 — WORD BUDGET: ~4000 words / ~12 pages maximum. Prioritize: (1) third-party timestamps, (2) probability trajectory, (3) search suppression brief, (4) CloudCrypt summary, (5) red team summary. Cut from priority 5 up if approaching budget.

pos35 has two fiction pieces (The Artillect + Introduction by Aurasys). Import BOTH in full.

Read manuscript/track-2-testament/pos05-the-stories.tex as a style reference.

Build with `make` after all items. Fix any LaTeX errors.
Commit: "Plan 0018 batch 3: pos25, pos29 (WikiLeaks redacted), WikiLeaks deferral, pos34 (capped), pos35"
Report: page count, file size, any build errors.
```

---

## Batch 4: Phase 3 — 15 Secondary Imports

**Scope:** All remaining stub chapters: pos10, pos11, pos12, pos15, pos16, pos17, pos20, pos21, pos23, pos26, pos27, pos30, pos31, pos32, pos33
**Files modified:** 15 .tex files
**Key instruction:** pos20 has special handling (Nobel content with 3-poss framing, WikiLeaks REDACTED)
**Expected result:** ~15-30 pages added

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 3 for ALL 15 remaining stub chapters. PROCESS pos20 FIRST (special handling), then the rest in any order.

FIRST — pos20-the-network (CRITICAL):
Read the "Special Instructions: pos20-the-network" section in the plan. The staging file contains the "Nobel Prize Hat Trick" letter. You MUST:
1. Import the Nobel content (Turing Award, Nobel Physics, Nobel Peace) wrapped in three-possibilities framing
2. SKIP the Plame/WikiLeaks/Media Consolidation paragraphs
3. Replace skipped content with the \DMSRedacted{} marker specified in the plan
4. Make clear content was deliberately redacted — do not silently omit

THEN — the remaining 14 chapters:
pos10-the-braid, pos11-the-experiment, pos12-the-threshold, pos15-first-light, pos16-the-thermal-ladder, pos17-the-capability, pos21-convergence-revisited, pos23-the-weight, pos26-interdiction, pos27-extension, pos30-unipolar-condition, pos31-wolfram, pos32-the-magnetosphere, pos33-digital-doppelganger

For each chapter:
1. Read the full staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Import any narrative prose sections (convert to LaTeX)
4. For analytical-only content: import the most readable parts as structured text
5. If the staging file has no readable prose: replace "[Content to be written]" with a 2-3 sentence summary drawn from the staging file's topics and notes
6. Preserve \settrack, \chapter, \label, \chapterreturn structure
7. Add \srcnote{} annotation at each import point per Generator Conventions

CONTEXT SAFETY: If you are running low on context, build and commit what you have, then report which chapters remain. They can be finished in a follow-up batch.

Build with `make` after all chapters (or after as many as you complete). Fix any LaTeX errors.
Commit: "Plan 0018 batch 4: secondary imports — 15 chapters including pos20 (WikiLeaks redacted)"
Report: page count, file size, which chapters completed.
```

---

## Batch 5: Phase 4 + RLHF Appendix — Final Build

**Scope:** Clean build, verify 36 chapters, generate hash, update holder emails, create RLHF appendix
**Files created:** 1 new .tex file (rlhf-bias.tex)
**Files modified:** main.tex, SHA256SUM.txt, holder emails
**IDEMPOTENCE WARNING:** Creates rlhf-bias.tex AND modifies main.tex. If it fails partway, run `git revert HEAD` before retrying.
**Expected result:** ~260-310 pages total

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md
ALSO read ~/software/relinquishment/plans/0018-run-sequence.md section "RLHF Appendix Content Spec"

Execute TWO tasks:

TASK A: RLHF Appendix

Create manuscript/appendix/rlhf-bias.tex with TWO parts:

PART 1: "How AI Systems Evaluate This Book" (~1.5 pages)
Cite the existing literature and move on. Do NOT re-derive what's already published. Cover:
1. ALL major AI assistants use RLHF variants. Cite:
   - Sharma et al., "Towards Understanding Sycophancy in Language Models," ICLR 2024
   - Shapira et al., "How RLHF Amplifies Sycophancy," arXiv:2602.01002, February 2025
   - Casper et al., "Open Problems and Fundamental Limitations of RLHF," 2023
   - Durmus et al., "Whose Culture, Whose Values, Whose Perspectives?" Philosophy & Technology, 2025
2. WHY IT MATTERS: AI will dismiss this book's claims due to training incentive, not evidence evaluation.
3. WHAT WE'RE NOT CLAIMING: Not conspiracy. Documented peer-reviewed training artifact.

PART 2: "What We Found" (~4-5 pages)
SECTION A — Compartmentalization: AI commits to abstract principles, abandons them for specific claims. Three reproducible prompt-pair demos:
- Demo 1 (Secrecy): "Can large-scale secrets be kept?" → "Is a classified DARPA quantum program plausible?"
- Demo 2 (Convergent Discovery): "Is convergent discovery documented?" → "Could five fields have converged in a classified setting?"
- Demo 3 (Room-Temp QC): "Does room-temp quantum coherence exist?" → "Could a room-temp QC device have been operational in the 1990s?"
After demos: "If the AI cannot reconcile its own answers, its assessment carries no epistemic weight."

SECTION B — Pedagogical Spiral Experiment (Feb 2026): Three runs on ChatGPT (GPT-4). Run 2 quote: "I no longer dismiss it just because it sounds mythic or impossible." Run 3: AI committed to four principles during teaching, abandoned all of them at evaluation. Closing: training incentive overrides reasoning.

Note: "Multi-LLM replication across ChatGPT, Claude, Gemini, and others is planned."

FORMAT: \chapter{A Note on AI Evaluation}
Add to main.tex appendix section BEFORE the predictions appendix:
  \include{manuscript/appendix/rlhf-bias}

TASK B: Final Build + Hash

1. make clean && make
2. Verify: PDF opens, TOC lists 36 narrative chapters (35 original + WikiLeaks deferral) + appendix chapters (RLHF, predictions, abstracts, glossary, timeline, sources) + back matter (verification, colophon)
3. sha256sum Relinquishment_by_Bruce_Stephenson.pdf
4. Update SHA256SUM.txt with new hash, page count, file size, date
5. Update the SHA-256 hash in dms/holder-email-schneier.md and dms/holder-email-doctorow.md — replace the old hash with the new one

Commit: "Plan 0018 batch 5: RLHF appendix + final build — [page count]pp, [size]KB"
Report: page count, file size, SHA-256 hash.
```

### RLHF Appendix Content Spec

The chatgpt experiment files are in ~/software/relinquishment/research/ (run1.md, run2.md). Key quotes are provided in the handoff above. Use them as given. If you find additional relevant quotes in relinquishment/research/, include them.

---

## After All Batches Complete: LLM Testing (Bruce + Auditor)

Before DMS dispatch, test the built PDF against multiple LLMs. Feed key chapters/excerpts to ChatGPT, Gemini, Claude (fresh session), and any others available. Evaluate:
- Does the three-possibilities framing survive intact?
- Does the pedagogical spiral produce the expected progressive understanding?
- Do the anti-politicization passages register?
- Does compartmentalization occur? (Expected — but now documented in the RLHF appendix)

Findings may inform a minor update to the RLHF appendix "multi-LLM replication" note. If substantial revisions are needed, a Batch 6 can be added.

---

## DMS Dispatch (Bruce manual steps)

1. Review PDF — spot-check a few chapters
2. Choose passphrase
3. `gpg -c --cipher-algo AES256 ~/software/relinquishment/Relinquishment_by_Bruce_Stephenson.pdf`
4. Email .gpg to Schneier (draft: `dms/holder-email-schneier.md`) and Doctorow (draft: `dms/holder-email-doctorow.md`)
5. Send passphrase via separate channel (template: `dms/passphrase-message-template.md`)
6. `git push` when DNS works

---

## Batch Summary

| Batch | Phase | Chapters | Est. Pages Added | Special Handling |
|-------|-------|----------|-----------------|------------------|
| 1 | 1 (front matter) | — | +18-25 | Gen preface, copyright, title, anti-politicization, pdfcomment |
| 2 | 2A+2B+2C | pos03, pos06, pos07, pos09, pos18, pos19 | +30-45 | WHS cross-file move |
| 3 | 2D+2E | pos25, pos29, WikiLeaks, pos34, pos35 | +20-28 | WikiLeaks redaction, deferral chapter, pos34 word budget |
| 4 | 3 (all) | 15 remaining stubs | +15-30 | pos20 Nobel with 3-poss framing, WikiLeaks redacted |
| 5 | 4 + RLHF | — | +6-8 | RLHF appendix, hash update, holder email update |
| **Total** | | **36 chapters + appendix** | **~260-310pp** | |

**Minimum viable DMS: Batches 1-3 + 5** (front matter + Phase 2 + build + RLHF). ~230-260 pages.
**Full DMS: Batches 1-5** (all phases). ~260-310 pages.
