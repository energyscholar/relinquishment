# Plan 0018: Generator Run Sequence

**Auditor:** Nightstalker
**Date:** 2026-02-19
**Master plan:** `plans/0018-dms-mvp-content-import.md`

Each run below is a separate Generator shell session. Copy-paste the handoff prompt. Wait for completion. Verify. Then start the next run.

**Build verification after every run:** `make` must succeed with zero errors. Check page count increases. Spot-check the PDF.

---

## Run 1: Phase 1 — Front Matter (4 items)

**Scope:** Introduction, Corrections page, Coventry fix, Alpha Farm fix
**Files created:** 2 new .tex files
**Files modified:** main.tex, pos04-the-code-war.tex, pos02-alpha-farm.tex
**Expected result:** ~150-160 pages (from 137)

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 1 only (sections 1A, 1B, 1C, 1D). This involves:
- 1A: Create manuscript/00-front/introduction.tex from content in the plan. Add \include to main.tex between preface and not-claimed.
- 1B: Restructure the Coventry section in manuscript/bridge/pos04-the-code-war.tex per plan instructions.
- 1C: Create manuscript/00-front/corrections.tex from content in the plan. Add \include to main.tex after not-claimed.
- 1D: Replace lorem ipsum in manuscript/track-2-testament/pos02-alpha-farm.tex per plan instructions.

Read existing .tex files (preface.tex, pos04-the-code-war.tex, pos02-alpha-farm.tex) to match formatting style. The plan contains the full text for introduction and corrections — convert to LaTeX.

Build with `make` after all 4 items. Run test cases T1.1-T1.8.
Commit: "Plan 0018 phase 1: front matter — introduction, corrections, Coventry fix, Alpha Farm fix"
Report: page count, file size, any test failures.
```

---

## Run 2: Phase 2A — pos03 + pos06 (The Mentor + The Secret)

**Scope:** 2 chapters. These are linked: pos03 staging has the White Hot Secret content that moves to pos06.
**Files modified:** 2 .tex files
**Key instruction:** Process pos03 FIRST. Set aside the White Hot Secret section. Then process pos06 using that content.

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.1 (pos03-the-mentor) and 2.2 (pos06-the-secret) only.

For each chapter:
1. Read the staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan (section "Chapter 2.1" and "Chapter 2.2")
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure

IMPORTANT: Process pos03 FIRST. The plan says to move the "White Hot Secret" section from pos03's staging to pos06. Extract it during pos03 processing, then use it when writing pos06.

Read manuscript/bridge/pos04-the-code-war.tex as a style reference for LaTeX formatting.

Build with `make` after both chapters. Fix any LaTeX errors.
Commit: "Plan 0018 phase 2A: pos03 the mentor, pos06 the secret"
Report: page count, file size, any build errors.
```

---

## Run 3: Phase 2B — pos07 + pos09 (The Departure + The Factoring Game)

**Scope:** 2 chapters. Both have rich importable prose.

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.3 (pos07-the-departure) and 2.4 (pos09-the-factoring-game) only.

For each chapter:
1. Read the FULL staging file in manuscript/staging/raw/ (not just the first 40 lines)
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan (sections "Chapter 2.3" and "Chapter 2.4")
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure

Read manuscript/bridge/pos04-the-code-war.tex as a style reference for LaTeX formatting.

Build with `make` after both chapters. Fix any LaTeX errors.
Commit: "Plan 0018 phase 2B: pos07 the departure, pos09 the factoring game"
Report: page count, file size, any build errors.
```

---

## Run 4: Phase 2C — pos18 + pos19 (The Walk-Out + Patrick Ball)

**Scope:** 2 chapters.

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.5 (pos18-the-walk-out) and 2.6 (pos19-patrick-ball) only.

For each chapter:
1. Read the FULL staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan (sections "Chapter 2.5" and "Chapter 2.6")
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure

Read manuscript/bridge/pos04-the-code-war.tex and manuscript/track-2-testament/pos05-the-stories.tex as style references.

Build with `make` after both chapters. Fix any LaTeX errors.
Commit: "Plan 0018 phase 2C: pos18 the walk-out, pos19 patrick ball"
Report: page count, file size, any build errors.
```

---

## Run 5: Phase 2D — pos25 + pos29 (Ethical Framework + The Silence)

**Scope:** 2 chapters.

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.7 (pos25-ethical-framework) and 2.8 (pos29-the-silence) only.

For each chapter:
1. Read the FULL staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan (sections "Chapter 2.7" and "Chapter 2.8")
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure

Read manuscript/track-2-testament/pos05-the-stories.tex as a style reference.

Build with `make` after both chapters. Fix any LaTeX errors.
Commit: "Plan 0018 phase 2D: pos25 ethical framework, pos29 the silence"
Report: page count, file size, any build errors.
```

---

## Run 6: Phase 2E — pos34 + pos35 (The Research + The Question)

**Scope:** 2 chapters. Both are LONG staging files (413 and 109 lines). pos35 has fiction pieces.

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 2, chapters 2.9 (pos34-the-research) and 2.10 (pos35-the-question) only.

For each chapter:
1. Read the FULL staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Follow the per-chapter instructions in the plan (sections "Chapter 2.9" and "Chapter 2.10")
4. Import prose sections, convert markdown to LaTeX per the conversion rules table
5. Preserve \settrack, \chapter, \label, \chapterreturn structure

pos34 is the LARGEST staging file (~7200 words). Import the cloudCrypt archive timeline, third-party timestamps, and red team analysis. Use \begin{description} or \begin{enumerate} for structured lists.

pos35 has two fiction pieces (The Artillect + Introduction by Aurasys). Import BOTH in full.

Read manuscript/bridge/pos04-the-code-war.tex as a style reference.

Build with `make` after both chapters. Fix any LaTeX errors.
Commit: "Plan 0018 phase 2E: pos34 the research, pos35 the question"
Report: page count, file size, any build errors.
```

---

## Run 7: Phase 3 — Secondary Imports (15 chapters, batch 1: 5 chapters)

**Scope:** pos10, pos11, pos12, pos15, pos16

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 3 for these 5 chapters only: pos10-the-braid, pos11-the-experiment, pos12-the-threshold, pos15-first-light, pos16-the-thermal-ladder.

For each chapter:
1. Read the full staging file in manuscript/staging/raw/
2. Read the existing .tex stub
3. Import any narrative prose sections (convert to LaTeX)
4. For analytical-only content: import the most readable parts as structured text
5. If the staging file has no readable prose: replace "[Content to be written]" with a 2-3 sentence summary drawn from the staging file's topics and notes
6. Preserve \settrack, \chapter, \label, \chapterreturn structure

Build with `make` after all 5. Fix any LaTeX errors.
Commit: "Plan 0018 phase 3A: secondary imports — pos10, pos11, pos12, pos15, pos16"
Report: page count, file size.
```

---

## Run 8: Phase 3 — Secondary Imports (batch 2: 5 chapters)

**Scope:** pos17, pos20, pos21, pos23, pos26

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 3 for these 5 chapters only: pos17-the-capability, pos20-the-network, pos21-convergence-revisited, pos23-the-weight, pos26-interdiction.

Same instructions as Run 7. Read staging files, import prose, convert to LaTeX, build, commit.

Commit: "Plan 0018 phase 3B: secondary imports — pos17, pos20, pos21, pos23, pos26"
Report: page count, file size.
```

---

## Run 9: Phase 3 — Secondary Imports (batch 3: 5 chapters)

**Scope:** pos27, pos30, pos31, pos32, pos33

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 3 for these 5 chapters only: pos27-extension, pos30-unipolar-condition, pos31-wolfram, pos32-the-magnetosphere, pos33-digital-doppelganger.

Same instructions as Run 7. Read staging files, import prose, convert to LaTeX, build, commit.

Commit: "Plan 0018 phase 3C: secondary imports — pos27, pos30, pos31, pos32, pos33"
Report: page count, file size.
```

---

## Run 10: Phase 4 — Final Build + Hash

**Scope:** Clean build, verify all chapters, generate hash.

**Handoff prompt:**
```
You are the Generator. Read ~/software/relinquishment/plans/0018-dms-mvp-content-import.md

Execute Phase 4 only:
1. make clean && make
2. Verify: PDF opens, TOC lists all 35 chapters + front/back matter
3. sha256sum Relinquishment_by_Bruce_Stephenson.pdf
4. Update SHA256SUM.txt with new hash, page count, file size, date
5. Run test cases T4.1-T4.4

Commit: "Plan 0018 phase 4: DMS MVP final build — [page count]pp, [size]KB"
Report: page count, file size, SHA-256 hash.
```

---

## After All Runs Complete

Bruce manual steps:
1. Review PDF — spot-check a few chapters
2. Choose passphrase
3. `gpg -c --cipher-algo AES256 ~/software/relinquishment/Relinquishment_by_Bruce_Stephenson.pdf`
4. Email .gpg to Schneier (draft: `dms/holder-email-schneier.md`) and Doctorow (draft: `dms/holder-email-doctorow.md`)
5. Send passphrase via separate channel (template: `dms/passphrase-message-template.md`)
6. `git push` when DNS works

---

## Run Summary

| Run | Phase | Chapters | Est. Pages Added |
|-----|-------|----------|-----------------|
| 1 | 1 (front matter) | — | +15-20 |
| 2 | 2A | pos03, pos06 | +10-15 |
| 3 | 2B | pos07, pos09 | +10-15 |
| 4 | 2C | pos18, pos19 | +10-15 |
| 5 | 2D | pos25, pos29 | +8-12 |
| 6 | 2E | pos34, pos35 | +15-20 |
| 7 | 3A | pos10-12, pos15-16 | +5-10 |
| 8 | 3B | pos17, pos20-21, pos23, pos26 | +5-10 |
| 9 | 3C | pos27, pos30-33 | +5-10 |
| 10 | 4 (final) | — | 0 |
| **Total** | | **35 chapters** | **~250-300pp** |

**Minimum viable DMS: Runs 1-6** (Phase 1 + Phase 2). ~220-250 pages.
**Full DMS: Runs 1-10** (all phases). ~250-300 pages.
