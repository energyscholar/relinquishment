# Relinquishment — Requirements & Acceptance Criteria

*This document defines TEST PASS requirements for the book project. Each requirement is binary: PASS or FAIL. The Auditor writes plans referencing these requirements. The Generator implements to spec. The Auditor verifies.*

---

## R0: Root Directory Cleanliness

**PASS if:** Root contains ONLY:
- `README.md`
- `main.tex` (root LaTeX document)
- `Makefile` (build orchestration — must be at root for `make` convention)
- `*.pdf` output file(s) (gitignored)
- `.gitignore`
- Standard hidden dirs (`.git/`, `.claude/`)

**FAIL if:** Any working documents, research files, or subdirectory READMEs appear in root. All working content lives in subdirectories.

**Subdirectory layout:**
- `plans/` — Serial-numbered generator plans (0001-name.md), requirements.md, verification reports. Auditor territory.
- `manuscript/` — All chapter content (LaTeX .tex source). Generator territory.
- `build/` — .latexmkrc, Dockerfile, preamble, palette, geometry configs, images, validation scripts, toolchain. Generator territory.
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
- The three possibilities appear in the preface (brief) and as the full opening chapter (Pos 1 per Plan 0007)

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
- Surmise is labeled as surmise (e.g., ninja missions → Custodian setup)
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
- OCG layers: at minimum, toggle prediction tables, toggle abstracts (see also R19 for graphics toggle)
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
- All appendix sections complete (predictions, abstracts, glossary, timeline, sources)
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

## R13: Cover — Interactive Triskellion

**PASS if:**
- Cover page features a colorful triskellion design incorporating words and images
- The three spiral arms of the triskellion correspond to the three tracks (Confession/Testament/Awakening)
- Each spiral arm is a clickable link that navigates to the start of that track
- In PDF viewers that support link annotations, the cover functions as a navigation hub
- In older/basic PDF viewers, the cover renders as a static visual — no broken elements, no invisible text
- Cover art is fully embedded (no external image dependencies)
- Design is visually compelling as a standalone image (printable, shareable as screenshot)

**FAIL if:** Cover is text-only, triskellion is absent, links break the visual in old viewers, or any spiral arm is not clickable in capable viewers.

---

## R14: Multi-Route Navigation

**PASS if:**
- **Linear path (default):** Reader can read front-to-back in the spiral interleave order (R12). This is the default experience.
- **Track standalone:** Each of the 3 tracks can be read independently as a coherent narrative. PDF bookmarks and/or link pages provide per-track reading order.
- **Chronological timeline:** A cross-track index orders all events by historical date, with links to the relevant chapter/section. Reader can follow the timeline rather than the spiral.
- **Hyperlinks:** Dense internal cross-referencing — chapters link to related chapters, predictions link to evidence, abstracts link to their mirrored chapters, and vice versa.
- **Popup definitions/annotations:** Key terms, people, and acronyms have PDF popup annotations (tooltip text). In viewers that support annotations, these appear on hover/tap. In older viewers, they are invisible (graceful absence, not broken rendering).
- All navigation mechanisms coexist without interfering with each other
- A "How to Read This Book" page explains the available routes

**FAIL if:** Only linear reading is supported, per-track paths are missing or incoherent, chronological index is absent, or popups break rendering in basic viewers.

---

## R15: Embedded Verification

**PASS if:**
- A **visible verification page** inside the PDF displays:
  - SHA-256 hash of the PDF content (excluding the verification page itself, or of a canonical content extract)
  - PGP signature block (ASCII-armored)
  - Publication timestamp
  - Brief instructions for independent verification
- **Machine-readable attachments** are embedded in the PDF (PDF 1.4+ embedded files):
  - `SHA256SUMS.txt` — hash file
  - `signature.asc` — detached PGP signature
  - `README.txt` — verification instructions and public key fingerprint
- The PDF remains a single self-contained file with all verification material inside it
- Older viewers that don't surface attachments still show the visible verification page
- Digital signature with trusted timestamp (as per R9) remains a separate mechanism from the PGP layer

**FAIL if:** Verification requires external files, the visible page is missing, attachments are absent, or the PDF is no longer a single file.

---

## R16: Distribution — Darknet Torrent

**PASS if:**
- The PDF is distributed as a single file via BitTorrent on darknet/anonymous networks
- Torrent metadata includes: title, author pseudonym, description, content hash
- The PDF stands alone — no companion files required (all verification is embedded per R15)
- A clearnet fallback distribution method exists (e.g., IPFS, Substack, or direct download)
- No DRM or access restrictions on the PDF itself
- The torrent is seeded from infrastructure Bruce controls or trusts

**FAIL if:** Distribution requires multiple files, DRM is present, or no darknet distribution channel exists.

---

## R17: Page Layout — Screen-First, Conditional Compilation

**PASS if:**
- Two build targets from the same LaTeX source: `make screen` (landscape) and `make print` (portrait)
- Screen: landscape-oriented single page, single reading column, optimized for laptop at fit-width
- Print: portrait, book margins (inner/outer gutter), optimized for standard paper
- Both outputs generated via conditional compilation flags (`\ifdefined\SCREEN` / `\ifdefined\PRINT`)
- Blank pages inserted as needed for clean chapter starts
- Margins are generous and comfortable for extended screen reading
- Both outputs maintain all content, hyperlinks, and structure — only geometry and pagination differ
- Each chapter tested in both modes for layout quality (no orphan lines, no awkward float placement)

**FAIL if:** Screen and print require separate source files, either output loses content or structure, or layout testing is skipped.

---

## R18: Visual Design — Typography & Color

**PASS if:**
- Full color interior: track-colored margins, headings, hyperlinks, figure accents
- Color palette is easy on the eyes for extended screen reading (no high-saturation primaries for large areas)
- Three distinct track colors applied to margin stripes AND running headers (per R14 track differentiation)
- Clean B&W degradation: when printed in grayscale, track differentiation remains distinguishable (pattern/weight variation, not color alone)
- Typography choices are isolated in a swappable style configuration (LaTeX class/style file), not hardcoded throughout
- Default font selection: mixed family (serif body, sans-serif headings, monospace for abstracts/technical content)
- All fonts are open-source and freely embeddable — embedding permission verified per font license before use
- **NOTE:** Typography and color choices require human aesthetic review before finalization. Defaults are placeholders pending review.

**FAIL if:** Color causes eye strain, B&W print loses track differentiation, font changes require editing every chapter file, proprietary fonts create licensing issues, or font embedding permission is unverified.

---

## R19: Graphics & Multimedia Toggle

**PASS if:**
- OCG (Optional Content Group) layer controls allow toggling between:
  - **Full mode (default):** All graphics, illustrations, figures, and multimedia visible
  - **Text mode:** Plain text only — graphics hidden via OCG. Empty space remains where figures were (OCG is visibility toggle, not layout reflow — this is a PDF limitation). All text remains readable.
- Toggle is accessible from PDF viewer's layer panel (supported in Acrobat, Evince, Okular, PDF.js)
- Text mode is the effective "audiobook source" — clean prose without figure references that point to invisible images
- In viewers that don't support OCG, full mode displays (graceful default)

**FAIL if:** Toggle breaks layout, text mode references invisible figures, or full mode is not the default in non-OCG viewers.

---

## R20: Rich Illustration

**PASS if:**
- Interior includes diagrams, archival photographs, and generated visualizations where they serve the narrative
- Minimum illustration types: timeline visualization, people/organization network, at least one technical diagram (e.g., topological protection, magnetosphere schematic)
- All images embedded in PDF (no external references)
- All images have alt text for accessibility (per R21)
- Illustrations are placed contextually near relevant text, not in a separate plate section
- Image resolution sufficient for both screen viewing (150+ DPI at display size) and print (300+ DPI at print size)
- Licensing: all images are either original, public domain, Creative Commons, or fair use with attribution

**FAIL if:** No illustrations present, images lack alt text, images are external references, or licensing is unresolved.

---

## R21: Accessibility, TTS & Archival Longevity

**PASS if:**
- **Standards compliance:**
  - PDF/A-4 (ISO 19005-4) for archival longevity — all fonts embedded, no external dependencies, no encryption that blocks access
  - PDF/UA-2 (ISO 14289-2) for universal accessibility
  - WCAG 2.1 Level AA equivalent
- **Tagged PDF structure:**
  - Complete tag tree with logical reading order
  - Proper heading hierarchy (H1–H6)
  - All tables tagged with header associations
  - All lists tagged as lists
  - Figure tags with alt text on every image
- **TTS optimization:**
  - Document language set (`en-US`)
  - Abbreviation expansion via `/E` entries on first occurrence (TQNN, COWS, FQH, UDHR, SAS, GCHQ, DARPA, cDc, ICTY, etc.)
  - `/ActualText` entries for symbols, abbreviations that should be read differently than displayed
  - Correct Unicode/ligature handling (LuaLaTeX + fontspec handles this natively; `cmap` is pdfLaTeX-only and NOT used)
  - Clean reading order verified by screen reader testing (NVDA or equivalent)
  - Mixed-language passages tagged with appropriate `/Lang` entries
- **Archival intent:**
  - Document must remain fully functional and readable with no external dependencies for 50+ years
  - No features that depend on external services, web APIs, or cloud resources
  - All interactive features degrade to readable static content
  - Metadata includes creation date, author, subject, keywords, and preservation intent
- **Degradation testing:** PDF opened in a viewer 10+ years old (or PDF.js with limited feature support) must be fully readable. Interactive features absent but content intact.
- **Validation:** Passes PAC (PDF Accessibility Checker) and Adobe Acrobat accessibility checker

**FAIL if:** PDF/A-4 validation fails, tag tree is missing or incomplete, screen reader cannot navigate the document coherently, any external dependency exists, or degradation testing is skipped.

---

## R22: Front & Back Matter

**PASS if:**
- **Front matter (in order):**
  1. Cover page (per R13)
  2. Title page
  3. Copyright / license notice
  4. "How to Read This Book" — explains navigation routes, track structure, graphics toggle
  5. Table of Contents (clickable, per R9)
  6. Preface (author's voice, three possibilities introduced)
- **Back matter (in order):**
  1. Appendix A: Predictive Framework (full table, per R5)
  2. Appendix B: Spiral Abstracts (all 15, per R3)
  3. Appendix C: Glossary — definitions of all technical terms, acronyms, people. Popup annotations (R14) link here.
  4. Appendix D: Chronological Timeline — all events in date order across all tracks (the TIME navigation route from R14)
  5. Appendix E: Sources & References
  7. Verification page (per R15)
  8. Colophon (toolchain, build date, version, archival statement)
- All front/back matter sections are bookmarked and appear in TOC
- Glossary entries are cross-referenced from popup annotations in body text

**FAIL if:** Any listed section is missing, ordering is wrong, or sections are not navigable from TOC/bookmarks.

---

## R23: File Size Optimization

**PASS if:**
- Build process actively minimizes PDF file size at every stage
- **Image optimization:** All images compressed to optimal quality/size ratio (JPEG for photos, PNG for diagrams with transparency, WebP where PDF version supports). No uncompressed raster data.
- **Font subsetting:** Only used glyphs embedded, not full font files
- **Stream compression:** All PDF content streams use maximum Flate (zlib) compression
- **Duplicate elimination:** Identical resources (images, fonts, color profiles) stored once and referenced, not duplicated
- **Object stream compression:** Cross-reference and object streams compressed (PDF 1.5+)
- **Build pipeline:** Automated size audit step reports final file size and per-component breakdown (fonts, images, content, metadata)
- **Triad Protocol shrinkage:** Auditor defines size budget targets; Generator implements; Auditor verifies. Iterative compression until diminishing returns.
- **Size target:** Final PDF should be as small as possible while meeting all other requirements. No absolute number — the target is "smallest achievable given R13–R22 constraints."
- Linearized PDF ("Fast Web View") for efficient partial download and streaming

**FAIL if:** Build process includes no compression step, fonts are fully embedded (not subsetted), images are uncompressed, or file contains duplicate resources. Also FAIL if no size audit report is generated during build.

---

## R24: Build System

**PASS if:**
- `Makefile` exists with targets: `dev`, `final`, `screen`, `print`, `images`, `validate`, `clean`, `clean-cache`, `manifest`, `size-report`, `gitinfo`
- `make dev` compiles in < 30 seconds for incremental/cached builds (full cold builds may be slower)
- `make final` compiles with no errors and no unresolved references
- `make screen` and `make print` produce distinct PDFs from the same source
- `make validate` runs automated validation pipeline (PDF/A, links, size, manifest)
- `Dockerfile` pins TeX Live version and produces reproducible builds via `SOURCE_DATE_EPOCH`
- Docker build produces PDF verifiable against host build (when host has matching TeX Live)
- `.latexmkrc` configures LuaLaTeX, shell-escape, glossary build step
- TikZ externalization caches compiled images; second build is faster than first
- Build generates machine-readable validation report (JSON)
- One git commit per plan phase, commit message references plan number

**FAIL if:** No Makefile, no Docker, build has unresolved references, validation pipeline absent, or TikZ caching broken.

**Note:** Host system (TeX Live 2022) supports dev builds only. Final/tagged builds require Docker (TeX Live 2025+). This is by design — `\ifdefined\FINAL` flag controls tagging activation.

---

## R25: Suppression Resilience

**PASS if:**
- **Incremental hashing:** Each chapter hashed at draft completion; hash published externally (Substack) with timestamp. Creates temporal proof chain.
- **Signed git commits:** All commits to relinquishment repo are GPG-signed.
- **Multiple git remotes:** Repo pushed to at least 2 independent hosting services.
- **Reproducible build:** Docker ensures anyone with the source can verify the PDF matches.
- **Multi-channel distribution:** Torrent (multiple trackers + DHT) + IPFS + clearnet fallback. Magnet link and IPFS hash printed inside the PDF.
- **No JavaScript in PDF:** PDF/A-4 prohibits it. No tracking beacons, no phone-home URLs.
- **Content integrity:** PGP signature + SHA-256 (per R15) + OpenTimestamps registration.
- **Repo is private until publication.** Plans describe structure and strategy — OPSEC until release.

**FAIL if:** No incremental hashing, single distribution channel, unsigned commits, or repo publicly accessible before release.

---

## R26: Rollback & Error Correction

**PASS if:**
- When a Generator produces incorrect output, the Auditor writes a corrective plan (new serial number, references original plan and specific failures)
- Corrective plans specify: which files to modify, what's wrong, what "correct" looks like
- Git history preserves incorrect output (no force-push, no rebase) — the error and its correction are both auditable
- If an entire plan's output is wrong, the corrective plan may specify `git revert` of the original plan's commits
- Partial corrections are the norm; full reverts are the exception

**FAIL if:** Errors are fixed by ad-hoc editing without a plan, git history is rewritten to hide errors, or the error/correction cycle is not auditable.

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

*Requirements v1.7 — 2026-02-14 — R0-R26. Updated R19 (OCG gaps), R21 (cmap→fontspec), R24 (images/gitinfo targets, 30s→incremental). Prior: v1.6 R0/R19; v1.5 R0; v1.4 R24-R26.*
