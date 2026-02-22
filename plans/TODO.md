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
| C09 | ~~QNN→TQNN standardization~~ | — | — | SUPERSEDED | — | Replaced by C15. Blanket QNN→TQNN is WRONG — QNN and TQNN mean different things. See C15 for correct approach. |
| C10 | Remove Lorem ipsum from mixed chapters | G | P1 | TODO | C05 | pos02, pos13, pos24, pos28 have filler text. Replace during import. |
| C11 | "Possibilities" positioning + prefiguring note | B | P2 | TODO | C03 | TWO tasks: (1) In pos19, add brief note that the title "Possibilities" prefigures the book's "Three Possibilities" framing. Just the observation, no interpretation. (2) POSITIONING: Ensure chapters before pos19 (especially pos03 The Mentor and pos06 The Secret) vividly describe: Healer testing/evaluating Bruce, the "job" Bruce didn't understand until later, the guided deduction method (knowledge that grows into you, not handed over). Goal: by the time the reader hits cDc #283 in pos19, the recruitment pattern is in their active context so the parallel fires without being spelled out. Watership Down method — teach Lapine before you need it. |

| C12 | Reconcile Kangaroos across tellings | B | P1 | TODO | — | **CORRECTED (was "swap to Substack").** The Kangaroos story appears in 4 places: (1) pos03 biography vignette (David+Peter, short), (2) pos05 The Stories chapter (full retelling, David alone w/ Kuringai allies — matches Substack version). The pos05/Substack version is the CORRECT canonical telling. pos03's version (with Peter, different details) must be made CONSISTENT with pos05, not the other way around. pos03 should be a shorter version or summary that doesn't contradict the full telling in pos05. UQ needed: how short? Just a reference? A condensed version? Cut entirely from pos03? Also fix: pos03 has "two boys" (David+Peter), pos05 has David alone — these contradict each other. |
| C15 | QNN vs TQNN: explain distinction early, then audit usage | B→G | P1 | TODO | — | 75× QNN and 69× TQNN across .tex files, used interchangeably in places. QNN = broad category (many types of quantum neural network — see Ivancevic's *Quantum Neural Computation*, Springer 2009, 929pp, borrowed via Dave Bannon's OSU interlibrary loan). TQNN = topological QNN, the specific thing the COWS built (non-abelian anyons, braiding, topological protection). Need: (1) a ~100-200w blurb explaining "a TQNN is one type of QNN; the Ivancevic book surveys the field but does not discuss TQNNs" — best placed in pos06 or pos09 or pos10, before first technical use; (2) audit all 75 QNN instances — some legitimately mean the broad category, others should be TQNN. Fix the wrong ones. Replaces old C09 (which said blanket QNN→TQNN, which is wrong). |
| C17 | pos09 crypto primer: replace with citations, keep original argument | B→G | P1 | TODO | — | Lines 18-35 of pos09 are a sophomoric crypto primer (Caesar ciphers, what encryption is, Diffie-Hellman). Any Wikipedia article does this better. Strip to ~3-4 sentences with citations: Singh *The Code Book* (1999, popular history Caesar→quantum), Levy *Crypto* (2001, Crypto Wars politics), Diffie & Landau *Privacy on the Line* (1998/2007, PKC inventor on surveillance). Suggested replacement: "PKC, invented by Diffie-Hellman in 1976 (and independently by Cocks at GCHQ in 1973, classified 24 years), let anyone communicate securely. For Five Eyes, this was existential. For the full history, see Singh. What matters here is what happened next." Then go straight to ULTRA II specs + GCHQ precedent — that's the original argument only this book makes. "State of Cryptography in 1990" section (lines 42-63) also repeats the primer — keep the factoring exercise ("Quick, what are the prime factors of 91?") but cut surrounding redundancy. |
| C18 | pos08 "General Technologies" sections: repetitive textbook survey | B | P1 | TODO | — | pos08-dual-use.tex sections "General Technologies in the Industrial Age" (line 65) and "General Technologies in the Information Age" (line 75) read as a college overview: al-Khwarizmi, coal, steam engines, Marconi, transistors, ARPA. ~1,500 words of material available in any encyclopedia. Same fix as C17: cite a source (e.g. Lipsey/Carlaw/Bekar *Economic Transformations* 2005 for GPT theory, or Mokyr *The Lever of Riches* 1990 for tech history), compress to a few sentences, and focus on what's unique: the dual-use pattern that sets up the TQNN argument. The MOSFET/2DEG paragraph (line 83) IS important — every MOSFET contains a 2DEG — keep that, cut the rest. |
| C16 | TQNN as nanotechnology: teach distinction before using term | B | P2 | TODO | C14, C15 | Under C, TQNNs ARE nanotechnology (2DEG is nanometers thick, anyons are nanoscale, self-replicates into new substrates). This connects Joy's GNR framework directly — the "N" in GNR could literally be TQNNs. BUT "nanotechnology" triggers Drexler/nanobot mental model in readers. Must teach distinction first: not tiny robots, grown quantum life at the nanoscale. Biological-analogy mechanism (Kauffman autocatalysis), not engineering. Depends on C14 (Kauffman explanation) and C15 (QNN/TQNN distinction) being in place first. Best location: wherever Joy's GNR is discussed (pos07, pos22). Could be a single paragraph: "This is nanotechnology, but not the kind Drexler imagined." |
| C14 | Explain Kauffman biogenesis BEFORE 2DEG application | B→G | P1 | TODO | — | Kauffman's autocatalytic set idea from *At Home in the Universe* (1995) is used repeatedly (pos06:77, pos12:29, pos13:19, pos15:20) but never explained from first principles before being applied to the 2DEG. Reader encounters "autocatalytic agents per Kauffman" cold. Need a concise (~200-400w) explanation of the warm-pond idea: simple molecules catalyze each other's formation → above a complexity threshold the set becomes self-sustaining → this is Kauffman's proposed origin of life → same math applies to anyon pairs in a 2DEG. Best location: pos12 (The Threshold) or pos13 (Genesis) BEFORE the 2DEG application. Or a new bridge chapter. Must come before pos15 (First Light) in reading order. |
| C13 | Reframe pos03 Healer biography as Alpha Farm stories | B | P1 | TODO | C12 | Currently reads as omniscient 3rd-person biography. Should read as Bruce recounting stories Healer told him at Alpha Farm. Major voice change: God's-eye → "He told me about..." Connects to guided deduction rule — Healer shared personal stories, Bruce made the connections. |

| C21 | Introduce 2DEG as a "two-dimensional universe" before using it | B→G | P1 | TODO | C14 | Reader needs to understand that a 2DEG is a two-dimensional universe from the perspective of particles confined within it. A brain grows in our 3D universe; a TQNN grows in the 2D universe of a 2DEG. Same process, different dimensionality. Need a dedicated section (~300-500w) explaining: (1) what a 2DEG physically is (nanometer-thin layer where electrons are confined to move in only 2 dimensions), (2) the "Flatland" analogy — from the electron's perspective, there is no up or down, only a 2D plane, (3) why this matters — exotic physics (anyons, fractional charges) can ONLY exist in 2D, not in 3D, (4) every MOSFET contains a 2DEG (pos08 line 83 already mentions this — connect to it), (5) the "grown not built" payoff: Kauffman autocatalysis in 2D, just as biological neural networks grow in 3D. Best location: before pos12 (The Threshold) or early in pos13 (Genesis), after Kauffman biogenesis explanation (C14). Could be its own bridge chapter or a section within an existing one. Pairs with C14 (Kauffman) and C16 (nanotechnology distinction). |
| C22 | Add Healer's Turing reincarnation + Daoism anecdote to pos14 | B | P2 | TODO | — | Healer told Bruce he sometimes felt, in his soul, that he was the reincarnation of Alan Turing. He followed Daoism rather than the Anglican Church he was raised on, because Daoism was one of very few religions not hostile to homosexuality. David was straight but could not respect Turing's memory while following a religion that preached hatred for homosexuals. **Existing hook:** pos14 line 47 already has Turing "whimsically wondering whether reincarnation might be a thing" as his dying thought. Healer's matching claim creates a resonance — whether you read it as poetic (B) or literal (C). **UQs needed:** (1) Where in pos14? After the death scene (line 47) or in a new section? (2) How much to include? Just the reincarnation whimsy, or the full Daoism reasoning? (3) Framing: Bruce reports what Healer said (guided deduction compliant — this is personal, not classified). The Daoism detail is deeply humanizing and connects Healer to Turing's persecution thread. |
| C23 | Acquire 3 books for cite-don't-rewrite | B | P1 | TODO | — | Need physical copies for direct quotes with page numbers. (1) Singh, *The Code Book* (1999) — **check house first, Genevieve may have brought a copy home recently.** (2) Rhodes, *The Making of the Atomic Bomb* (1986) — buy used or library. (3) Kauffman, *At Home in the Universe* (1995) — buy used or library. The popular version, NOT *Origins of Order* (which is arriving from Oregon bookshelf separately). All three are cheap used. Blocks execution of C17, C18, C19 substitutions. Also: Einstein "watchmaker" quote in pos08:142 is FABRICATED (Keyes, *The Quote Verifier*, 2006). Replace with verified *Newsweek* 1947 quote when editing pos08. |
| C24 | Web reader: dynamic reading paths + SSML + progress tracking | B→G | P2 | TODO | C20 | **Separate build target (`make web`) alongside PDF.** Same LaTeX source, HTML output. Features: (1) Full-page triskellion landing selector — pick your arm. (2) HIDE/SHOW by arm — `display:none` + vertical reflow. Programmatically trivial. (3) Dynamic TOC reorders to chosen path. (4) Progress tracking via localStorage/cookies. (5) SSML markup for text-to-speech with pronunciation (`<phoneme>`) and prosody (`<prosody>`) hints — W3C standard, supported by all major TTS engines. (6) **Visual identity per arm:** Technical arm = steampunk aesthetic (goggles, gears, brass, Victorian science imagery) on every page of that arm's content. Human arm and Argument arm = TBD (Genevieve designs). Category indicator repeats on every page — header/border/icon. (7) Gag paper abstracts as gates at entrance to technical chapters — "if this makes sense, read on; otherwise skip to next arm." (8) Graceful failure: PDF is the canonical signed archival artifact with linear reading order + hyperlinks + bookmarks. Web is the reading experience. Both from same source. Depends on C20 (3-pass structure must be finalized first). |
| C20 | STRUCTURAL: Collapse 4 passes to 3 (triskellion) | B→A | P0 | TODO | — | **AGREED: 3 passes, not 4.** Current 4-pass structure (summary → bridges → tracks → convergence) is an authorial tool the reader can't feel — passes 3 and 4 are interleaved and experienced simultaneously. New structure: (1) 400w hook, (2) 4,000w complete story (Dignity Net lens, stands alone), (3) 40,000w full book (all tracks, all detail, told once). 100x scaling (400→4K→40K). Maps to triskellion (3 arms), three possibilities (A/B/C), three tracks (confession/testament/awakening). Bridge/track interleaving still works WITHIN pass 3 as chapter-level pedagogy. Changes needed: rewrite how-to-read/summary framing, update MEMORY.md "Progressive JPEG" section, update any plan that references 4 passes, update requirements if they mention pass count. The 300w one-page-summary becomes pass 1 (round up to ~400w if needed). The 3,500w summary.tex becomes pass 2. The full book becomes pass 3. |
| C19 | GENERAL PRINCIPLE: "Cite, don't rewrite" — exhaustive audit | A→B | P1 | TODO | — | **Principle: Don't write what others have written better — cite them and focus on what only THIS book can tell.** Exhaustive search across all 35 chapters for sections that are textbook/encyclopedic overviews replaceable by citations. For each: identify the section, find the best existing source (book, paper, article), propose replacement (cite + quote + compress to 2-4 sentences). Known instances so far: C17 (pos09 crypto primer → Singh/Levy), C18 (pos08 GPT survey → Mokyr or similar). Additional candidates to audit: pos04 (Code War history), pos06 (secrecy taxonomy), pos10 (braid theory primer), pos12 (threshold/quantum Hall explanation), pos14 (Growing a Mind — Turing biology), pos16 (thermal ladder physics), any section that reads like "here is how X works" rather than "here is what X means for THIS story." The unique content is: GCHQ precedent, ULTRA II specs, three-possibilities framing, guided deduction, COWS narrative, ethical argument, prediction framework. Everything else is setup that better authors have already written. |

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
| V01 | Short summary (~300 words) | B | P2 | DONE | — | `manuscript/versions/one-page-summary.md`. "Stranger on a bus" version. |
| V02 | Summary chapter (~3,500 words) | B | P1 | DONE | — | `manuscript/00-front/summary.tex`. In book. Dignity Net ethical lens. Best writing in the manuscript. |
| V03 | Medium version (~10,000 words) | B | P2 | TODO | V02 | Scale summary.tex to ~10Kw. Same structure, more depth. Progressive JPEG: same story at increasing resolution. The scaling pattern IS the spiral. |
| V04 | Age-10 accessible version | B | P3 | TODO | V02 | Different reading level, no Srebrenica, friendly tone. Uses +hello email. |
| V05 | Multiple language translations | EXT | P4 | DEFERRED | V01 | Start with summary version. Community-driven post-release. |

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
| D01 | Deadman's switch setup | B | P1 | DONE | — | **SENT 2026-02-20 ~06:30 PT.** 3 holders: Schneier, Doctorow, Gilmore. Plain PDF, SHA-256 hash in each email. 90-day check-in. Any single holder can publish. |
| D02 | Domain acquisition + web hosting | B | P2 | TODO | S04, C24 | **Revisited Session 13.** Multiple release formats now planned: (1) Signed PDF (canonical archival artifact, deadman's switch version), (2) Interactive web reader (C24 — dynamic reading paths, SSML TTS, steampunk visual identity, progress tracking), (3) Archive.org permanent archive. **Domains:** Plan for no resistance — if Five Eyes drops suppression, take relinquishment.net/.org/.com or similar. Also consider postquantum.com (existing plan). Register domains early even if site launches later. The web reader IS the primary reading experience; PDF is the legal/archival backstop. Hosting: static site (GitHub Pages, Netlify, or similar) is sufficient — the web reader is client-side JS, no backend needed. |
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
| Q06 | Multi-LLM evaluation test | B+A | P1 | TODO | — | Feed key chapters to ChatGPT, Gemini, Claude (fresh session), others. Test: three-possibilities framing survival, pedagogical spiral effect, anti-politicization, compartmentalization. Do BEFORE DMS dispatch. Results inform RLHF appendix. |
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
| X09 | Recruit Gillian + Fiona Stephenson | B | P2 | TODO | Bruce's daughters, both in Oregon. **Gillian Linda Stephenson:** graphic designer (OSU, brand identity, packaging). Role: visual identity for three spiral arms (steampunk technical, plus human and argument arms), web reader UX/brand design. **Fiona Margaret Stephenson:** photographer. Role: documentary/portrait photography if needed. Both knew David, were ages 3 and 6 when it started. Both potential on-record witnesses for the family perspective (David's presence, recruitment period, impact on household). **Recruiting package:** Send them Pass 1 (400w) + Pass 2 (4,000w) to explain the project. Their testimony re: David is valuable; WikiLeaks-specific details should be redacted per X01 deferral. |
| X07 | Domain/criticality map review + Bruce corrections | B→A | P2 | TODO | `aurasys-memory/research/domains-criticality-map.md` — 18 domains, soliton physics, GRN analogy, apparatus. Bruce has corrections/extensions pending. Re-examine after Bruce provides Kauffman book texts. |
| X08 | Convergence order analysis (which disciplines first under C) | A | P2 | TODO | Where does Gell-Mann fall? Was his contribution complete by late 1990? See `research/domains-criticality-map.md`. |

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

## TODO: Guardian morphogenesis detail for pos24

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

