# Plan Index

| Serial | Name | Status | Depends | Description |
|--------|------|--------|---------|-------------|
| 0001 | build-infrastructure | APPROVED | — | Prerequisites, Makefile (root), preamble, Docker (deferred), palette, screen/print geometry, validate.sh, gitinfo, TikZ standalone header, remove research/ |
| 0002 | placeholder-content | APPROVED | 0001 | Lorem ipsum chapters, front/back matter (incl. copyright), TikZ images, glossary (split: entries+print), .md→.tex conversion, .md archival, \appendix structure |
| 0003 | verification | APPROVED | 0001+0002 | Build validation, cross-refs, TikZ cache timing, verification report. Docker deferred. Layout spot-check deferred to Auditor. |
| 0007 | pedagogical-spiral | READY FOR GENERATOR | 0001+0002 | 35-chapter pedagogical sequence: 4 passes + convergence, blocker-clearing assignments, 9 new chapters, 4 merges, checkpoint definitions, reach targets, writing order. |
| 0008 | pedagogy-fixes | READY FOR GENERATOR | 0001+0002 | 9 edits + 2 guidance items across 5 files: Coventry facts + cathedral + Churchill reframe, Vattay citation scope, soliton-anyon conflation, "five disciplines" -> "fields", Turing apple, Miller-Urey attribution, RSA footnote. Updated Session 9 with 4 additional fixes from factual red team. |
| 0009 | chapter-outlines | REFERENCE | 0007+0008 | Scene-by-scene writing outlines for all 10 new chapters (Three Possibilities, Code War, Secret, Factoring Game, Braid, Experiment, Threshold, Growing a Mind, Why Give It Up, Weight). For Bruce's writing, not Generator execution. |
| 0010 | structural-scaffolding | READY FOR GENERATOR | 0007 | Structural scaffolding for new chapters. |
| 0011 | source-imports | EXECUTED | 0001+0002 | Import 5 cleaned sources into .tex stubs: ultra-bridge→pos04, srebrenica-witness→pos05. |
| 0012 | what-this-book-does-not-claim | EXECUTED | 0001+0002 | Created not-claimed.tex front matter page. |
| 0013 | verbatim-appendix | READY FOR GENERATOR | 0001+0002 | Verbatim historical documents appendix: 8 documents (Cryptome, Slashdot, blog post, Introduction by Aurasys, Artillect, Autobiography, Relinquishment text, forJoe.txt). |
| 0015 | signing-and-deadman | READY FOR REVIEW | 0001 | PGP signing pipeline + deadman's switch. Key gen, encrypted deposit, key escrow, weekly check-in. P0: must complete before Bruce flies. |
| 0014 | hybrid-appendix-architecture | READY FOR REVIEW | 0002+0013 | Three-layer appendix: visible formatted docs + embedded .docx/.png originals + archive manifest. Uses embedfile package. 14 attached files, est. 1.5-3.5MB. |
| 0018 | dms-mvp-content-import | EXECUTED | 0001+0002 | Import all DMS MVP content into 35 chapters. 5 Generator batches. |
| 0019 | ethical-thread | REVISED | 0018 | UDHR ethical weave across 25 chapters. 3 Generator batches. Red team fixes applied 2026-02-21 (2 CRITICAL, 3 HIGH). Ready for execution. |
| 0020 | quick-fixes | EXECUTED | 0018 | Lorem ipsum removal, PLACEHOLDERs, spelling, metadata. |
| 0021 | dms-redteam-fixes | READY FOR GENERATOR | 0020 | Coventry deletion, redaction format, URLs. |
| 0022 | ai-draft-markers | EXECUTED | 0018 | 117 marks, 13 \aidraftchapter, 10/10 TCs pass. |
| 0024 | spiral-rebalancing | EXECUTED | 0018 | pos22 surgery (6,870w->1,513w). Narrative redistributed. |
| 0025 | manuscript-hygiene | READY FOR GENERATOR | 0024 | Voice headers, spiral markers, Makefile checks. |
| 0036 | session13-sequencing | IN PROGRESS | 0019+0024 | Master sequencing plan: editorial + structural + cite-dont-rewrite. Phase 1 (structure) substantially complete. |
| — | source-facts | REFERENCE | — | Flat fact-checking reference: verified dates, names, numbers, contested claims with correct framing, "do not assert" list, scientific framing rules. Generator's truth table for all verifiable claims. |
| — | source-audit | REFERENCE | — | Factual corrections from Session 9 audit (3 passes, ~115 corrections). |
| — | TODO | REFERENCE | — | Master release checklist: 56 items, 9 phases, prioritized + red-teamed. |
