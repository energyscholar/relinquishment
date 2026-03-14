# Master TODO — Relinquishment Release Checklist

**Created:** 2026-02-16 (Session 9, Auditor)
**Last Audit:** 2026-02-26 (Session 25, Auditor — full status update)
**Protocol:** Triad (Auditor writes, Generator executes, Bruce gates)
**Target:** Complete monolithic signed PDF, ready for distribution

---

## Legend

- **Owner:** `B` = Bruce (writing/decisions), `G` = Generator (execution), `A` = Auditor (plans/review), `GEN` = Genevieve, `EXT` = External (lawyer, etc.)
- **Status:** `TODO`, `DONE`, `BLOCKED`, `DEFERRED`, `SUPERSEDED`, `NEEDS REVIEW`
- **Priority:** `P0` = blocks everything, `P1` = critical path, `P2` = important, `P3` = nice-to-have, `P4` = deferred/post-release
- **Deps:** item IDs that must complete first

---

## Phase 1: Content Pipeline

_Status as of 2026-02-26: ALL chapters have substantial content. Book is 224pp/748KB. The original "5/35 complete, 28/35 stub" assessment is obsolete. Plans 0018-0051 populated all chapters. 138 \aidraft markers remain across 13 files awaiting Bruce's prose pass._

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| C01 | ~~Groups B-H content dedup + assembly~~ | — | — | SUPERSEDED | — | All content imported via Plans 0018+. staging/ dirs no longer exist. Dedup handled per-chapter during rewrite plans. |
| C02 | ~~Process 25 staging files~~ | — | — | SUPERSEDED | — | Staging workflow abandoned. Content went directly into .tex files. |
| C03 | Bruce's aidraft writing pass | B | P1 | IN PROGRESS | — | **138 \aidraft markers across 13 files.** Heaviest: pos34b (34), pos34 (27), pos19 (15), pos02 (13), pos16 (10). Only 1 \aidraftchapter remaining (pos34b). Bruce replaces AI structural drafts with his own prose. |
| C04 | ~~Move raw/ → cleaned/~~ | — | — | SUPERSEDED | — | Staging workflow abandoned. |
| C05 | ~~Import cleaned files into .tex stubs~~ | — | — | DONE | — | All chapters populated via Plans 0018, 0038-0041, 0043-0048. |
| C06 | ~~Place epigraph abstracts~~ | — | — | DONE | — | Plan 0037 executed (17 epigraphs, Session 17). |
| C07 | ~~Resolve pos11 structural problem~~ | — | — | SUPERSEDED | — | Miller-Urey = 1953 origin-of-life experiment (primordial soup). Originally proposed as analogy for TQNN emergence. Kauffman's biogenesis in pos13 (C14) serves this purpose better and is already done. pos11 cleanly covers DARPA project history/COWS formation. |
| C08 | pos05-kangaroos.tex (0 bytes) | G | P2 | NEEDS REVIEW | — | File still empty (0 bytes). Content exists in pos05-the-stories.tex (Track 2). May be intentionally empty — verify no collision needed. |
| C09 | ~~QNN→TQNN standardization~~ | — | — | SUPERSEDED | — | Replaced by C15. |
| C10 | ~~Remove Lorem ipsum~~ | — | — | DONE | — | Grep confirms zero occurrences across all .tex files. |
| C11 | "Possibilities" #283 → Three Possibilities explicit link | G | P2 | TODO | — | pos19 documents cDc #283 content but doesn't explicitly note the title prefigures the book's framework. Add one sentence. |
| C12 | ~~Reconcile Kangaroos across tellings~~ | — | — | DONE | — | Bruce confirmed "already handled by inline text" (Session 25, Plan 0051 Phase 4). pos03 has editorial comment noting the discrepancy; pos05 is canonical. |
| C13 | Reframe pos03 Healer biography as Alpha Farm stories | B | P1 | TODO | — | Major voice change still needed. pos03 still reads as 3rd-person omniscient biography. TODO comments in pos03 confirm this is outstanding. |
| C14 | ~~Explain Kauffman biogenesis BEFORE 2DEG application~~ | — | — | DONE | — | pos13 lines 27-66: buttons-and-threads thought experiment, phase transition, edge of chaos, application to 2DEG substrate. Comprehensive, before pos15. |
| C15 | QNN vs TQNN: distinction paragraph + full usage audit | A→G | P1 | TODO | — | PARTIAL: glossary defines TQNN but no QNN entry. 75× QNN + 69× TQNN used interchangeably. Need: (1) one paragraph distinguishing QNN (broad) from TQNN (topological, specific), (2) glossary entry for QNN, (3) full audit of all 144 uses — fix wrong ones. Needs Auditor plan. |
| C16 | TQNN as nanotechnology: teach distinction | B | P2 | TODO | C14, C15 | Depends on C14 and C15 being resolved first. |
| C17 | pos09 crypto primer: cite-don't-rewrite | B→G | P1 | TODO | C23 | Blocked on acquiring Singh *The Code Book*. Replace sophomoric primer with citations. |
| C18 | pos08 general technologies: cite-don't-rewrite | B | P1 | TODO | C23 | Blocked on acquiring reference books. Keep MOSFET/2DEG paragraph, compress encyclopedia sections. |
| C19 | "Cite, don't rewrite" exhaustive audit | A→B | P1 | TODO | — | Systematic pass. Pairs naturally with Plan 0050 (bibliography). Run together. |
| C20 | ~~Collapse 4 passes to 3 (triskellion)~~ | — | — | DONE | — | Bruce confirmed done (Session 25). Current 5-checkpoint structure is final. |
| C21 | ~~Introduce 2DEG as "two-dimensional universe"~~ | — | — | DONE | — | pos10 line 21: "electrons confined to a flat plane... these exotic particles can only exist in flatland; in three-dimensional space, the topology that makes braiding meaningful collapses." Explicit Flatland analogy. |
| C22 | Add Healer's Turing reincarnation + Daoism to pos14 | B | P2 | TODO | — | Still needs UQ decisions from Bruce. Humanizing detail. |
| C23 | Acquire 3 books for cite-don't-rewrite | B | P1 | TODO | — | Singh *The Code Book*, Rhodes *Making of the Atomic Bomb*, Kauffman *At Home in the Universe*. Blocks C17, C18. Check house first — Gen may have Singh. |
| C24 | ~~Web reader pipeline~~ | — | — | DONE | — | Plan 0049 executed: EPUB/HTML/Markdown pipeline built. Dynamic reading paths + SSML are future enhancements (post-release). |

### Content Status Summary (Updated 2026-02-26)
- **SUBSTANTIAL chapters:** 35/36 (all have >50 lines of real content)
- **EMPTY:** 1/36 (pos05-kangaroos.tex, intentionally empty)
- **Awaiting Bruce's prose:** 13 files with 138 \aidraft markers
- **Book size:** 224 pages, 748KB, ~58K words

---

## Phase 2: Front Matter

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| F01 | Cover design | GEN→G | P2 | TODO | — | Genevieve decides. TikZ triskellion placeholder currently. |
| F02 | Title page finalize | G | P2 | TODO | F01 | Currently basic. Needs final design after cover. |
| F03 | ~~How-to-read.tex~~ | — | — | DONE | — | 35 lines, 569 words. Explains 4-pass spiral, track system, reading order. |
| F04 | Dedication page | B | P3 | TODO | — | Does Bruce want one? Decision needed. |
| F05 | ~~Copyright page~~ | — | — | DONE | — | Dual license, AI disclosure, integrity notice. Updated Plan 0051 (65% probability). |
| F06 | ~~Preface~~ | — | — | DONE | — | |
| F07 | ~~"What This Book Does Not Claim"~~ | — | — | DONE | — | Plan 0012 executed. |
| F08 | Legal note (names, sources, fair use) | — | — | DONE | — | **NEW.** Plan 0051 phase 2. Covers real names, reported speech, fair use, AI drafting. |

---

## Phase 3: Appendices

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| A01 | ~~Predictions appendix~~ | — | — | DONE | — | |
| A02 | ~~Abstracts appendix~~ | — | — | DONE | — | 35+ chapter abstracts. |
| A03 | ~~Timeline appendix~~ | — | — | DONE | — | 241 lines, 119 entries, 1985-2025. Updated Plan 0051 (hypothesis markers). |
| A04 | Sources bibliography | A→G | P2 | TODO | — | Currently stub ("in preparation"). **Plan 0050 ready to execute.** biber installed. |
| A05 | Glossary expansion | A→G | P2 | TODO | — | 10 entries exist. **Plan 0050 phase 4** adds ~15-20 more + \gls{} placement. |
| A06 | Session transcripts appendix | B | P3 | DEFERRED | — | Decision shifted: Acknowledgements says "methodology described in Engine chapter, session logs in project archive." No separate appendix needed. |
| A07 | Verbatim 2013 documents appendix | A→G | P2 | TODO | — | Highest temporal-consistency value. Cryptome post, Slashdot comment, Autobiography excerpt. Not yet built. |
| A08 | Ch22 verbatim original in appendix | A→G | P2 | TODO | — | 2013 original preserved verbatim. Subset of A07. |
| A09 | "Why Bruce?" profile distillation | B→A→G | P3 | TODO | — | |
| A10 | Mysak Costa Rica joint memoir | B | P3 | TODO | — | |
| A11 | Mysak co-authored paper (Erdos number) | B | P3 | TODO | A10 | |
| A12 | Bill Joy article licensing inquiry | B→EXT | P3 | TODO | — | |
| A13 | RLHF/AI evaluation appendix | — | — | DONE | — | **NEW.** `rlhf-bias.tex` — 135 lines, compartmentalization demos + pedagogical spiral experiments. Updated Plan 0051 (pulled RLHF promise). |
| A14 | DMS recipients note | — | — | DONE | — | **NEW.** `dms-note.tex` — Plan 0045. Note to DMS recipients. |

---

## Phase 4: Back Matter

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| B01 | ~~Verification page~~ | — | — | DONE | — | 41 lines. SHA-256, timestamps, Cryptome/Slashdot/Blogspot/Substack refs, contact email. |
| B02 | PGP key generation/distribution | B | P2 | TODO | — | Decision needed: keyserver, personal site, appendix, QR code? |
| B03 | ~~Colophon~~ | — | — | DONE | — | |
| B04 | About the author | B | P3 | TODO | — | Does Bruce want one? Decision needed. |

---

## Phase 5: Build System & Production

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| S01 | Docker installation + test | G | P2 | TODO | — | Dockerfile exists (672 bytes), never tested. Required for `make final`. |
| S02 | PDF/A-4 compliance | G | P2 | TODO | S01 | tagpdf configured but untested. |
| S03 | PDF/UA-2 accessibility tagging | G | P2 | TODO | S01 | |
| S04 | Crypto signing pipeline | A→G | P1 | TODO | B02 | Needs PGP key decision first. |
| S05 | Print layout testing | G | P3 | TODO | S01 | build/print.tex exists (132 bytes, minimal). |
| S06 | ~~Size budget check~~ | — | — | DONE | — | 748KB, well under 25MB limit. No raster images. Safe. |
| S07 | ~~PDF metadata~~ | — | — | DONE | — | hypersetup configured: title, author (Bruce + Genevieve), subject, keywords. |
| S08 | Cross-reference audit | G | P2 | TODO | — | Verify all \label/\ref pairs valid. Check .log for warnings. |
| S09 | Full requirements pass (R0-R26) | A | P1 | TODO | — | Run every requirement against current manuscript. |

---

## Phase 6: Accessibility & Versions

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| V01 | ~~Short summary (~400 words)~~ | — | — | DONE | — | hook.tex. ~400 words, DN-filtered. |
| V02 | ~~Summary chapter (~3,500 words)~~ | — | — | DONE | — | summary.tex. 272 lines. |
| V03 | Medium version (~10,000 words) | B | P3 | TODO | — | Scale summary.tex to ~10Kw. Post-release is fine. |
| V04 | Age-10 accessible version | B | P4 | DEFERRED | — | |
| V05 | Multiple language translations | EXT | P4 | DEFERRED | — | |

---

## Phase 7: Legal & OPSEC

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| L01 | Attorney review — real names | EXT | P1 | TODO | — | Legal note (Plan 0051) provides framework. Attorney must review before public release. |
| L02 | OPSEC final pass | A | P1 | TODO | — | Plan 0051 was a defensive pass (14 gaps). Formal OPSEC audit still needed. |
| L03 | Errata process design | A | P2 | TODO | — | |
| L04 | ISBN decision | B | P3 | TODO | — | |

---

## Phase 8: Distribution & Release

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| D01 | ~~Deadman's switch~~ | — | — | DONE | — | SENT 2026-02-20. Schneier, Doctorow, Gilmore. 90-day check-in 2026-05-21. |
| D02 | Domain + web hosting | B | P2 | TODO | — | Plan 0049 built EPUB/HTML pipeline. Needs hosting decision. |
| D03 | Archive.org upload | G | P2 | TODO | S04 | |
| D04 | IPFS pinning | G | P3 | TODO | S04 | |
| D05 | Day-0 outreach package | A→B | P1 | TODO | — | |
| D06 | Gmail filter setup | B | P2 | TODO | — | 5 min task. 6 filters for 6 tokens. |
| D07 | arXiv paper submission | B | P3 | TODO | — | |
| D08 | DMS update | B | P1 | TODO | — | **NEW.** Holders have Feb 20 PDF. Need to send updated PDF with Plans 0038-0051 changes + cover email. Blocked on PDF rebuild. |

---

## Phase 9: QA & Final Release

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| Q01 | Genevieve aesthetic review | GEN | P1 | TODO | — | Send her current PDF. She has veto power. |
| Q07 | Genevieve rewrites her preface | GEN | P1 | TODO | — | Current preface (genevieve-preface.tex) was written for early draft. Book has changed substantially — dossiers, B/C sharpening, structural revision. Gen should rewrite to reflect current state. Date still says Feb 2026. |
| Q02 | Beta readers (2-3 trusted) | B | P2 | TODO | — | |
| Q03 | Full proofread | B | P1 | TODO | — | |
| Q04 | Verify 3rd-party timestamps still live | A→G | P1 | TODO | — | Cryptome, Slashdot, Blogspot, Substack. Screenshot + Wayback if fragile. |
| Q05 | Final build + sign + verify | G | P0 | TODO | ALL | Last step. |
| Q06 | ~~Multi-LLM evaluation test~~ | — | — | DONE | — | RLHF appendix (rlhf-bias.tex) documents 3 ChatGPT runs + compartmentalization demos. |

---

## Deferred (Post-Release or Undecided)

| ID | Task | Owner | Priority | Status | Notes |
|----|------|-------|----------|--------|-------|
| X01 | WikiLeaks chapter | B | P4 | DEFERRED | Plan 0044 executed WikiLeaks scrub. Chapter is redacted placeholder. |
| X02 | Angerman direct contact | B | P4 | DEFERRED | Timing: near-final manuscript. |
| X03 | NTP/power grid dataset analysis | A | P4 | DEFERRED | |
| X04 | Print edition | B | P4 | DEFERRED | |
| X05 | Audiobook edition | B | P4 | DEFERRED | |
| X06 | Language translations | EXT | P4 | DEFERRED | |
| X07 | Domain/criticality map review | B→A | P3 | TODO | Bruce has corrections pending. |
| X08 | Convergence order analysis | A | P3 | TODO | |
| X09 | Recruit Gillian + Fiona | B | P2 | TODO | Send them Pass 1 + Pass 2 to explain project. |

---

## Plans Ready to Execute (not yet run)

| Plan | What | Owner | Priority | Notes |
|------|------|-------|----------|-------|
| 0042 | Steel-Man Possibility A | GEN | P2 | Spec for Genevieve. Awaiting her. |
| 0050 | Bibliography + glossary (4 phases) | G | P1 | biber installed. Ready to launch. |

---

## Critical Path (Updated 2026-02-26)

The content pipeline bottleneck (C01-C05) is CLEARED. All chapters have content. The new critical path is:

```
IMMEDIATE (parallel, no dependencies):
  Plan 0050 (bibliography + glossary)     — G, ~3 hrs
  D08 (DMS update PDF + email)            — B, 30 min
  D06 (Gmail filters)                     — B, 5 min
  Q04 (verify timestamps still live)      — A→G, 30 min

SHORT-TERM (Bruce's writing + decisions):
  C03 (aidraft writing pass, 138 markers) — B, ongoing
  C13 (pos03 Alpha Farm reframe)          — B, major rewrite
  C23 (acquire 3 books)                   — B, buy/borrow
  C17+C18 (cite-don't-rewrite)            — B→G, after C23

MEDIUM-TERM:
  C14+C15+C21 (pedagogical setup)         — B→G, verify/write
  A07 (verbatim 2013 appendix)            — A→G
  L01 (attorney review)                   — EXT
  Q01 (Genevieve aesthetic review)        — GEN

FINAL:
  Q03 (full proofread)                    — B
  S04 (signing pipeline)                  — A→G
  S09 (requirements pass)                 — A
  Q05 (final build + sign + ship)         — G
```

---

## Guardian morphogenesis detail for pos24

**Priority:** HIGH
**Source:** Bruce, session 2026-02-22 (pos30 UQ session)

Guardian's design intent (for pos24-instantiation.tex):
- Virtual human body grown via morphogenesis
- Virtual organs, virtual limbic system
- Intent: grow a being that might feel empathy for humans, not something utterly alien
- Maori elder woman's DNA (identity unknown) — thus the HGP connection
- Objective: maternal feelings toward humanity
- Healer thought of her as his daughter (he had no human children)
- Year of conception (1999) = same year as Bruce's daughter Gillian
- This is WHY she is "she" — not arbitrary pronoun choice
