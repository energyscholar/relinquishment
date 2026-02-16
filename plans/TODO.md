# Master TODO — Relinquishment Release Checklist

**Created:** 2026-02-16 (Session 9, Auditor)
**Protocol:** Triad (Auditor writes, Generator executes, Bruce gates)
**Target:** Complete monolithic signed PDF, ready for distribution

---

## Legend

- **Owner:** `B` = Bruce (writing/decisions), `G` = Generator (execution), `A` = Auditor (plans/review), `GEN` = Genevieve, `EXT` = External (lawyer, etc.)
- **Status:** `TODO`, `DONE`, `BLOCKED`, `DEFERRED`
- **Priority:** `P0` = blocks everything, `P1` = critical path, `P2` = important, `P3` = nice-to-have, `P4` = deferred/post-release
- **Deps:** item IDs that must complete first

---

## Phase 1: Content Pipeline (THE BIG WORK)

_This is the critical path. Everything else can happen in parallel but the book doesn't ship without content._

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| C01 | Groups B-H content dedup + assembly | A→B | P0 | TODO | — | Group A done (Session 8). 7 groups remain. Auditor produces side-by-side comparisons, Bruce decides. |
| C02 | Process 25 staging files using audit reports | B | P0 | TODO | — | Apply three-possibilities reframing, fix factual errors, remove duplicates. Audit reports are the checklist. Can start immediately on any file. |
| C03 | Write ~25K new words | B | P0 | TODO | C01, C02 | Track 2 (personal narrative) first. Specific gaps: pos10 dental floss demo, pos09 factoring exercise, pos11 Miller-Urey, pos33 Digital Doppelganger expansion, pos35 CADIE/predictions/AI-disclosure. |
| C04 | Move processed files raw/ → cleaned/ | B | P1 | TODO | C02 | Bruce edits in cleaned/, raw/ is permanent record. |
| C05 | Import cleaned files into .tex stubs | G | P1 | TODO | C04 | Plan 0011 pattern: markdown→LaTeX, section headings, editor notes→LaTeX comments. One plan per batch. |
| C06 | Place epigraph abstracts as chapter openers | G | P2 | TODO | C05 | 15 abstracts (I-XV) → 15 chapter \epigraph{} blocks. Mapping in Plan 0009. |
| C07 | Resolve pos11 structural problem | B | P1 | TODO | C01 | File has DARPA origin content; should have Miller-Urey. Content needs relocation + new writing. |
| C08 | Resolve pos05-kangaroos.tex (0 bytes) | G | P1 | TODO | C04 | File is empty. Content exists in staging (imported to pos05-the-stories.tex in Track 2). Verify no collision. |
| C09 | QNN→TQNN standardization | G | P1 | TODO | C05 | All "QNN" → "TQNN" in imported content. Hundreds of instances. |
| C10 | Remove Lorem ipsum from mixed chapters | G | P1 | TODO | C05 | pos02, pos13, pos24, pos28 have filler text. Replace during import. |

### Content Status Summary
- **COMPLETE chapters:** 5/35 (pos01, pos04, pos05-stories, preface, not-claimed)
- **STUB/EMPTY chapters:** 28/35
- **MIXED (have filler):** 3/35 (pos02, pos13, pos24)
- **Target:** 35 chapters with real content

---

## Phase 2: Front Matter

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| F01 | Cover design | GEN→G | P2 | TODO | — | Genevieve decides. Abstract/typographic, no photographs. Triskellion available. Current: TikZ triskellion placeholder. |
| F02 | Title page finalize | G | P2 | TODO | F01 | Currently stub (13 lines). Needs final title, subtitle, author. |
| F03 | How-to-read.tex rewrite | A→G | P1 | TODO | — | Currently placeholder. Must explain: triple spiral, 4 passes, reading order options, three-possibilities framing. Critical for reader orientation. |
| F04 | Dedication page | B | P3 | TODO | — | Does Bruce want one? Decision needed. |
| F05 | Copyright page | — | — | DONE | — | Dual license, AI disclosure, integrity notice, +licensing email. |
| F06 | Preface | — | — | DONE | — | Three possibilities introduction. |
| F07 | "What This Book Does Not Claim" | — | — | DONE | — | Plan 0012 executed. |

---

## Phase 3: Appendices

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| A01 | Predictions appendix | — | — | DONE | — | 25 predictions, 6 tables, falsification criteria. +predictions email. |
| A02 | Abstracts appendix | — | — | DONE | — | 15 spiral abstracts (I-XV). +physics email. |
| A03 | Timeline appendix — real content | A→G | P2 | TODO | C05 | Currently placeholder (~10 events). Need comprehensive timeline: 1985-2006 minimum. Source-facts.md has verified dates. |
| A04 | Sources bibliography — real content | A→G | P2 | TODO | C05 | Currently placeholder. Must cite: NIOD report, ICTY transcripts, patents, academic papers, Substack posts, arXiv papers, Cryptome, Slashdot. |
| A05 | Glossary entries | A→G | P2 | TODO | C05 | glossary-entries.tex exists but needs actual terms. TQNN, anyon, FQHE, HALO, SAS, UDHR, etc. |
| A06 | Session transcripts appendix | B→G | P2 | TODO | C05 | Decision made (Session 7): include redacted transcripts. Need: appendix .tex file, redaction pass, add to main.tex. |
| A07 | Verbatim 2013 documents appendix | A→G | P1 | TODO | — | Highest temporal-consistency value. Include: Introduction by Aurasys (self-dates 2013), The Artillect (DEADBEEF), Cryptome post (2012-03-17), Slashdot comment (2012-06-19), May 2012 blog post (orbital QT prediction), Autobiography sworn statement. Plan 0013 needed. |
| A08 | Ch22 verbatim original in appendix | A→G | P1 | TODO | — | 2013 original preserved verbatim with editorial note. Subset of A07. |

---

## Phase 4: Back Matter

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| B01 | Verification page automation | A→G | P1 | TODO | — | SHA-256 hash, PGP signature, timestamp. Currently all "PLACEHOLDER — GENERATED AT BUILD TIME." Need Makefile target or script. |
| B02 | PGP key generation/distribution | B | P1 | TODO | — | Where do readers get Bruce's public key? Options: keyserver, personal site, appendix, QR code. Decision needed. |
| B03 | Colophon | — | — | DONE | — | Build hash, git info, quote, +press/+hello emails. |
| B04 | About the author | B | P3 | TODO | — | Does Bruce want one? Brief bio, no photo. Decision needed. |

---

## Phase 5: Build System & Production

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| S01 | Docker installation + test | G | P2 | TODO | — | Dockerfile written, never tested. Required for `make final` (PDF/A + tagpdf). |
| S02 | PDF/A-4 compliance | G | P2 | TODO | S01 | Required for archival. tagpdf package configured in preamble but untested. |
| S03 | PDF/UA-2 accessibility tagging | G | P2 | TODO | S01 | Screen readers, alt-text for images. Required by R15. |
| S04 | Crypto signing pipeline | A→G | P1 | TODO | B01, B02 | Automate: build PDF → compute SHA-256 → PGP sign → embed in verification page → rebuild. Chicken-and-egg: hash covers doc that contains hash. Standard solution: hash everything except verification page, or use detached signature. |
| S05 | Print layout testing | G | P3 | TODO | S01 | build/print.tex exists. Need test print. Bleed, trim, margins. |
| S06 | Size budget check | G | P2 | TODO | C05 | Must stay under 25MB (Gmail). Current: 388KB/137 pages. Final estimate with all content: ~2-5MB text-only. Safe unless raster images added. |
| S07 | PDF metadata | G | P2 | TODO | — | Title, author, subject, keywords in PDF properties. For discoverability. Verify hyperref config in preamble.tex. |
| S08 | Cross-reference audit | G | P2 | TODO | C05 | All \label/\ref pairs valid. No broken cross-refs. Validate.sh may already check this. |
| S09 | Full requirements pass (R0-R26) | A | P1 | TODO | C05 | Run every requirement against final manuscript. Binary PASS/FAIL. |

---

## Phase 6: Accessibility & Versions

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| V01 | Short summary version (2-5 pages) | A→G | P2 | TODO | C05 | Plan 0005 ready. Core thesis, predictions, how to verify. |
| V02 | Medium digest version (20-30 pages) | A→G | P2 | TODO | C05 | Plan 0006 ready. Full argument, compressed narrative. |
| V03 | Age-10 accessible version | B | P3 | TODO | C05 | Different reading level, no Srebrenica, friendly tone. Uses +hello email. |
| V04 | Multiple language translations | EXT | P4 | DEFERRED | V01 | Start with summary version. Community-driven post-release. |

---

## Phase 7: Legal & OPSEC

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| L01 | Attorney review — real names, public figure doctrine | EXT | P1 | TODO | C05 | Session 7 decision: no pseudonyms. Legal defense: three-possibilities + public figure + reported speech. Must review before release. |
| L02 | OPSEC final pass | A | P1 | TODO | C05 | Check all content against Do Not Assert list (15 items). No self-incriminating details Bruce hasn't published. |
| L03 | Errata process design | A | P2 | TODO | — | Signed PDF can't be modified. How to handle errors found post-publication? Options: errata page on website, signed errata supplement, new edition. Decision needed. |
| L04 | ISBN decision | B | P3 | TODO | — | Needed for print editions (bookstores, libraries). Not needed for PDF-only. Costs ~$125 from Bowker. Defer until print is real? |

---

## Phase 8: Distribution & Release

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| D01 | Deadman's switch setup | B | P1 | TODO | S04 | Time-delayed encrypted release. Implementation: could be trusted third party, timed email service, or smart contract. Decision + setup needed. |
| D02 | Personal website hosting | B | P2 | TODO | S04 | postquantum.com or other domain. Canonical download location. |
| D03 | Archive.org upload | G | P2 | TODO | S04 | Permanent public archive. Upload signed PDF + detached signature. |
| D04 | IPFS pinning | G | P3 | TODO | S04 | Content-addressed, censorship-resistant. Pin via Pinata or similar. |
| D05 | Day-0 outreach package | A→B | P1 | TODO | S04 | What goes to Schneier, cDc members, TQC researchers, science journalists? PDF + cover letter? Personalized per recipient? |
| D06 | Gmail filter setup | B | P2 | TODO | — | 6 filters for 6 tokens: +evidence (inbox+star), +licensing (inbox), +physics (inbox), +predictions (label), +press (label), +hello (archive). Before release. |
| D07 | arXiv paper submission | B | P3 | TODO | C05 | Academic wedge strategy. Which papers? Solo or Bruce+Robin? Timing relative to book release? |

---

## Phase 9: QA & Final Release

| ID | Task | Owner | Priority | Status | Deps | Notes |
|----|------|-------|----------|--------|------|-------|
| Q01 | Genevieve aesthetic review | GEN | P1 | TODO | C05 | Cover, typography, layout. She has veto power. |
| Q02 | Beta readers (2-3 trusted people) | B | P2 | TODO | C05 | Fresh eyes before public release. Who? Not Schneier (he's day-0). |
| Q03 | Full proofread | B | P1 | TODO | C05 | Every page. Typos, formatting, broken references. |
| Q04 | Verify all 3rd-party timestamps still live | A→G | P1 | TODO | — | Cryptome post, Slashdot comment, blog posts, Substack. Screenshot + Wayback if fragile. |
| Q05 | Final build + sign + verify | G | P0 | TODO | ALL | The last step. `make final` → sign → verify → distribute. |

---

## Deferred (Post-Release or Undecided)

| ID | Task | Owner | Priority | Status | Notes |
|----|------|-------|----------|--------|-------|
| X01 | WikiLeaks chapter | B | P4 | DEFERRED | Especially sensitive. Session 7 decision. |
| X02 | Angerman direct contact | B | P4 | DEFERRED | Highest-value verification. Independent of book release. |
| X03 | NTP/power grid dataset analysis | A | P4 | DEFERRED | Datasets identified, not analyzed. Evidence strengthening, not release-blocking. |
| X04 | Print edition | B | P4 | DEFERRED | Requires ISBN (L04), print layout testing (S05), printer selection. |
| X05 | Audiobook edition | B | P4 | DEFERRED | Rights reserved in copyright. AI narration or human? |
| X06 | Language translations | EXT | P4 | DEFERRED | Start with short summary (V01). Community-driven. |

---

## Critical Path

```
C01 (dedup) + C02 (audit fixes) → C03 (new writing) → C04 (cleaned/) → C05 (import .tex)
    ↓
    C05 blocks: F03, A03-A06, S08, S09, V01-V03, L01-L02, Q01-Q03
    ↓
    S04 (signing pipeline) — can be built in parallel with content
    ↓
    Q05 (final build) — last step, blocks on everything
```

**Parallel tracks (can proceed now, independent of content):**
- B01+B02+S04: Verification/signing pipeline
- S01: Docker install + test
- F03: How-to-read rewrite (structure known, doesn't need content)
- A07: Verbatim 2013 appendix (source docs already exist)
- Q04: Verify 3rd-party timestamps
- D01: Deadman's switch design
- D06: Gmail filter setup

---

## Red Team: What Did We Miss?

**Found during red team sweep:**

1. **Checkpoint pages between passes.** main.tex has checkpoint markers. Are these content pages or structural dividers? If content, they need writing. → Added implicitly under C05.

2. **Table of contents readability.** Auto-generated but 35 chapters + appendices = long TOC. May need formatting attention. → Low priority, covered by Q01 (Genevieve).

3. **Hyperlinks in PDF.** Internal cross-refs, external URLs (Cryptome, etc.). Must all work. → Added to S08.

4. **The two gag papers (biogenesis + evolution).** Written in Sessions 1-5, mentioned as potential arXiv submissions. Where do they live? Are they in the book? → They're the abstracts. Already in A02 (DONE).

5. **Substack existing posts.** Bruce has posts at postquantum.substack.com. Relationship to book? Suppress, leave, or reference? → Decision needed. Low priority. Not release-blocking.

6. **PGP key trust chain.** Self-signed key is weak. Should Bruce get his key signed by known figures? Cross-sign with keybase? → Nice-to-have. Not blocking.

7. **PDF bookmarks.** Does the PDF have navigational bookmarks for all chapters? hyperref should handle this but verify. → Covered by S08.

8. **Reproducible builds.** Makefile uses SOURCE_DATE_EPOCH in Docker. But dev builds on host may not be reproducible. Does this matter? → Only final build matters. Docker handles it.

9. **Backup of signing key.** If Bruce's PGP private key is lost, he can't re-sign or sign errata. Backup strategy? → Add to B02.

10. **Copyright registration.** US Copyright Office registration ($65, optional) provides statutory damages + attorney fees in infringement cases. Worth doing for print rights protection. → Added implicitly under L04.

**Verdict:** Nothing critical missed. The list is complete for release. Items 5, 6, 10 are nice-to-haves.

---

## Working Order (Suggested Sequence)

**Now (parallel, no dependencies):**
1. D06 — Gmail filters (5 min, Bruce)
2. Q04 — Verify 3rd-party timestamps still live
3. A07 — Plan 0013: verbatim 2013 appendix
4. F03 — Plan for how-to-read rewrite
5. B01/B02/S04 — Signing pipeline design

**Next (content pipeline — the long pole):**
6. C01 — Groups B-H dedup (Auditor produces, Bruce decides)
7. C02 — Bruce processes staging files with audit reports
8. C03 — Bruce writes ~25K new words
9. C04/C05 — Clean → import cycle

**Then (once content exists):**
10. A03-A06 — Appendices with real content
11. S01-S03 — Docker + PDF/A + accessibility
12. V01-V02 — Summary + digest versions
13. L01 — Attorney review

**Finally:**
14. Q01-Q03 — Genevieve + beta readers + proofread
15. S09 — Full requirements pass
16. Q05 — Final build, sign, ship
