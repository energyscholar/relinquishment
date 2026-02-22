# Plan 0036: Session 13 Sequencing — Editorial + Structural + Cite-Don't-Rewrite

**Date:** 2026-02-21
**Author:** Nightstalker (Auditor)
**Context:** Session 13 produced ~15 TODOs (C12-C24), a complete cite-don't-rewrite audit (25 flagged sections, ~5,000 words replaceable), structural decisions (3-pass triskellion, web reader), and editorial fixes across 7 chapters. This plan sequences all pending work into an executable order that minimizes Bruce's pedagogical writing burden and maximizes Generator throughput.

**Core principle:** Bruce writes ONLY what no one else has written. Everything else is citations + short bridges. This reduces Bruce's ~25K new-word estimate significantly.

---

## Phase 1: Structure First (blocks everything else)

**Owner: Auditor -> Bruce approval -> Generator**
**Deps: None**

| Step | Task | Who | Status | Notes |
|------|------|-----|--------|-------|
| 1a | Finalize 3-pass architecture (C20) | A->B | PENDING | Define exact boundaries: Pass 1 = 400w hook, Pass 2 = 4,000w full human story + simple pedagogy, Pass 3 = 40,000w triskellion with skip mechanism. |
| 1b | Map every chapter to a spiral arm | A | **DONE** | `research/chapter-arm-map.md` — 10 Human, 13 Argument, 12 Technical. |
| 1c | Chapter-opening audit | A->G | **DONE** | Integrated into chapter-arm-map.md (Opening Type column). 14 open with pedagogy, 10 with human, 13 with argument. |
| 1d | Update Plan 0019 (ethical thread) | A | **DONE** | 2 CRITICAL + 3 HIGH red team fixes applied. Changelog appended to plan file. |

**Deliverable:** Updated structural docs, chapter-arm map, fixed Plan 0019.

---

## Phase 2: Cite-Don't-Rewrite Substitutions (biggest bang for effort)

**Owner: Bruce (with books) -> Generator (mechanical substitutions)**
**Deps: Phase 1 complete. Books in hand (C23).**
**Effect: Removes ~4,500 words of pedagogy Bruce would otherwise need to polish.**
**Audit docs:** `aurasys-memory/research/cite-dont-rewrite-audit.md` + `cite-dont-rewrite-sources.md`

| Step | Task | Who | Status | Notes |
|------|------|-----|--------|-------|
| 2a | Fix Einstein watchmaker quote (pos08:142) | G | **DONE** | Replaced fabricated quote with verified Newsweek 1947 quote. |
| 2b | pos08-dual-use.tex surgery (C18) | B->G | PENDING | Worst offender: ~2,500w encyclopedic GPT survey -> ~500w with Bresnahan/Trajtenberg citation. |
| 2c | pos14-growing-a-mind.tex surgery (C19/audit #11) | B->G | PENDING | ~1,200w Turing biography -> ~300w emotional core + Hodges citation. |
| 2d | pos09-the-factoring-game.tex surgery (C17) | B->G | PENDING | ~850w crypto primer -> ~200w with Singh/Levy citations. |
| 2e | pos04 morphogenesis section (audit #2) | B->G | PENDING | ~650w science teaching -> ~100w + Kauffman "dead/alive" quote (p.50). |
| 2f | pos22 Manhattan Project (audit #12) | B->G | PENDING | ~150w -> 2 sentences + Rhodes citation + Oppenheimer "sin" quote. |
| 2g | Remaining 8 hard flags | B->G | PENDING | Execute per audit recommendations. Each is ~100-200w replacement. |
| 2h | Fix all 6 duplications | G | PENDING | GPT list, Turing+morphogenesis, ULTRA recap, DARPA desc, white hot secret, PKC explanation. |

**Deliverable:** ~4,500 words of textbook material replaced with ~500 words of citations.

---

## Phase 3: Editorial Pass (Bruce's unique content)

**Owner: Bruce (with Auditor/Nightstalker in session)**
**Deps: Phase 1 (structure known). Can run parallel with Phase 2.**

| Step | Task | Who | Notes |
|------|------|-----|-------|
| 3a | Continue chapter-by-chapter editorial | B+A | Session 13 covered: preface, introduction, pos02, 03, 05, 06, 07. Remaining: pos01, 04, 08-35, convergence, appendices. |
| 3b | Apply C13 (reframe pos03 as Alpha Farm stories) | B | Voice change: God's-eye -> "He told me about..." |
| 3c | Apply C12 (reconcile Kangaroos across tellings) | B | Make pos03 version consistent with pos05 canonical telling. |
| 3d | Apply C22 (Healer/Turing/Daoism anecdote in pos14) | B | After UQs resolved. Humanizing addition. |
| 3e | Apply C14 (Kauffman biogenesis explanation) | B | ~200-400w. Needs At Home in the Universe in hand. |
| 3f | Apply C21 (2DEG as "Flatland" introduction) | B->G | ~300-500w. Depends on C14. |
| 3g | Apply C15 (QNN vs TQNN distinction + audit) | B->G | Bruce writes ~100-200w blurb, Generator audits 144 instances. |

**Deliverable:** All 35 chapters editorially reviewed. Unique content added where needed.

---

## Phase 4: Programmatic Cleanup (Generator-only, no Bruce writing)

**Owner: Generator**
**Deps: Phase 2 and 3 substantially complete.**

| Step | Task | Who | Notes |
|------|------|-----|-------|
| 4a | Execute Plan 0019 (ethical thread) | G | 3 batches. Fixed in Phase 1d. |
| 4b | Execute Plan 0021 (DMS red team fixes) | G | Coventry deletion, redaction format. |
| 4c | Execute Plan 0025 (manuscript hygiene) | G | PLACEHOLDERs, formatting, spelling. |
| 4d | C08 (resolve pos05-kangaroos 0-byte file) | G | Verify no collision with pos05-the-stories.tex. |
| 4e | S07 + S08 (PDF metadata + cross-ref audit) | G | Build system checks. |
| 4f | Bibliography .bib file creation | G | All 22 citations from cite-dont-rewrite-sources.md -> LaTeX bibliography. |

**Deliverable:** Clean manuscript ready for QA.

---

## Phase 5: Parallel Tracks (independent, ongoing)

| Task | Owner | Notes |
|------|-------|-------|
| C23: Acquire 3 books | B | Check house for Singh. Buy Rhodes + Kauffman (At Home). |
| X09: Recruit Gillian + Fiona | B | Send Pass 1 + Pass 2 as recruiting package. |
| C24: Web reader design | B+G | After Phase 1 structure is final. Gillian does visual identity. |
| D02: Domain registration | B | Register relinquishment.net/.org/.com early. |
| Contact David via analog channel | B | Before publication. Not urgent. |

---

## Verification

- [x] All 35 chapters tagged to spiral arm (Phase 1b) -- DONE 2026-02-21
- [x] Einstein watchmaker quote replaced (Phase 2a) -- DONE 2026-02-21
- [x] Plan 0019 red team fixes applied (Phase 1d) -- DONE 2026-02-21
- [x] Chapter-opening audit complete (Phase 1c) -- DONE 2026-02-21
- [ ] cite-dont-rewrite word count reduced by ~4,000 words (Phase 2)
- [ ] All 6 duplications resolved (Phase 2h)
- [ ] Remaining chapters editorially reviewed (Phase 3a)
- [ ] Plans 0019, 0021, 0025 executed (Phase 4)
- [ ] PDF builds clean after all changes
- [ ] Bibliography .bib file contains all 22 citations (Phase 4f)

---

*Plan by Nightstalker (Auditor), 2026-02-21.*
