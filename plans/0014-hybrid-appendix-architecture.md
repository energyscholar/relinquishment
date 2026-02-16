# Plan 0014: Hybrid Appendix Architecture

**Author:** Auditor (Session 9)
**Status:** READY FOR REVIEW
**Depends:** 0002, 0013
**TODO ref:** A07, A08, A06
**Supersedes/extends:** Plan 0013 (visible appendix) remains unchanged. This plan adds the embedded attachment layer.

---

## Problem

Bruce has ~174 files (32MB) of historical source material spanning 2011-2021, plus session transcripts from 2025-2026. All of this is evidence. All of it should be in the signed PDF for provenance. But 99% of readers should never see it — it's messy, repetitive, and would destroy the reading experience.

## Solution: Three-Layer Architecture

```
Layer 1: VISIBLE APPENDIX (Plan 0013)
    8 key documents, editorially formatted, with provenance headers.
    The reader encounters these naturally if they read the appendices.

Layer 2: EMBEDDED ORIGINALS (this plan)
    Original .docx/.txt/.pdf files for the 8 key documents PLUS
    web page screenshots PLUS session transcripts (redacted).
    Invisible in normal reading. Accessible via PDF Attachments panel.
    Covered by the cryptographic hash.

Layer 3: MANIFEST ONLY (not embedded)
    The full cloudCrypt archive (32MB) is too large to embed.
    A manifest (filename, size, date, description) is printed in
    the visible appendix. The full archive available on request
    to energyscholar+evidence@gmail.com.
```

### Why This Works

- **Layer 1** serves the reader. Clean, formatted, editorial framing.
- **Layer 2** serves the researcher/verifier. Original files, bit-for-bit. The hash proves they haven't been modified since signing.
- **Layer 3** serves the investigator. Full archive available but not bloating the PDF.

---

## Layer 2 Implementation: Embedded Files

### Package

Use `embedfile` (already installed). Works with LuaLaTeX and PDF 2.0. Compatible with PDF/A-4 (which permits embedded files per PDF/A-3+ spec).

### Preamble Addition

```latex
\usepackage{embedfile}
\embedfilesetup{
  mimetype=application/octet-stream,
  desc={Source document for Relinquishment historical appendix}
}
```

### Files to Embed

**Tier A: Key Documents (original .docx/.txt files)**

| # | File | Source Path | Est. Size | Timestamp |
|---|------|------------|-----------|-----------|
| 1 | Introduction by Aurasys.docx | cloudCrypt/novel_variant/ | ~15KB | Google Docs ~2013-2016 |
| 2 | The Artillect.docx | cloudCrypt/Relinquishment/pure_fiction/ | ~10KB | Google Docs ~2013-2017 |
| 3 | Autobiography of an Accidental Conspirator by Bruce.docx | cloudCrypt/Relinquishment/autobiographical/ | ~20KB | Google Docs ~2013 |
| 4 | Relinquishment_ It is Easier to get Forgiveness than Permission.docx | cloudCrypt/Relinquishment/ | ~15KB | Google Docs ~2013 |
| 5 | forJoe.txt | cloudCrypt/Relinquishment/temp/ | ~5KB | Google Docs ~2013 |
| 6 | biography_D_Lane.docx | cloudCrypt/CC_book/ | ~17KB | Google Docs 2012-07-02 |
| 7 | Speculative Fiction_ Unlikely Possibilities.docx | cloudCrypt/CC_book/ | ~13KB | Google Docs 2016-01-09 |
| 8 | Journalistic Source Protection in the Age of Leaks.docx | cloudCrypt/Relinquishment/autobiographical/ | ~10KB | Google Docs ~2013 |

**Tier B: Web Page Evidence (screenshots + saved HTML)**

| # | File | Content | Est. Size |
|---|------|---------|-----------|
| 9 | cryptome-2012-03-17.png | Screenshot of Cryptome post, captured [date] | ~200KB |
| 10 | slashdot-2012-06-19.png | Screenshot of Slashdot comment, captured [date] | ~200KB |
| 11 | blogspot-2012-05-13.png | Screenshot of blog post with orbital QT prediction, captured [date] | ~200KB |
| 12 | blogspot-full-archive.png | Screenshot of full blogspot page showing all posts + dates | ~300KB |

**Tier C: Session Transcripts (redacted)**

| # | File | Content | Est. Size |
|---|------|---------|-----------|
| 13 | session-transcripts-redacted.txt | All AI-assisted sessions, redacted for OPSEC | ~500KB-2MB |

**Tier D: Archive Metadata**

| # | File | Content | Est. Size |
|---|------|---------|-----------|
| 14 | cloudcrypt-manifest.txt | Complete file listing: name, size, modified date, SHA-256 hash for every file in the 32MB archive | ~20KB |

**Estimated total embedded size: ~1.5-3.5MB**

Current PDF: 388KB. With full content: ~2-5MB. With attachments: ~4-8MB. Well under 25MB.

### Embedding Locations

Each embedded file is attached at the point where its visible-appendix counterpart appears. The `\embedfile` command can be placed inline:

```latex
\section{Introduction by Aurasys (2013)}
\embedfile[
  filespec={Introduction_by_Aurasys.docx},
  desc={Original Google Docs export of Introduction by Aurasys, circa 2013},
  mimetype={application/vnd.openxmlformats-officedocument.wordprocessingml.document}
]{path/to/Introduction by Aurasys.docx}

\begin{quote}
\small
\textbf{Source:} Google Drive archive (cloudCrypt) ...
```

### Reader Instructions

Add to the visible appendix introduction:

```latex
\subsection*{Accessing Original Source Files}

The original source documents --- unmodified Google Docs exports, screenshots
of third-party web pages, and redacted session transcripts --- are embedded
in this PDF as file attachments. They are covered by the cryptographic
signature on the Verification page.

\begin{description}
\item[Adobe Acrobat / Acrobat Reader:] Click the paperclip icon in the
left panel, or navigate to View $\to$ Show/Hide $\to$ Navigation Panes
$\to$ Attachments.
\item[Foxit Reader:] View $\to$ Navigation Panels $\to$ Attachments.
\item[Evince (Linux):] Side panel $\to$ Attachments.
\item[Apple Preview:] \textit{Does not support PDF attachments.} Use an
alternative viewer or extract with the command: \texttt{pdftk file.pdf
unpack\_files}
\item[Command line:] \texttt{pdftk Relinquishment*.pdf unpack\_files}
or \texttt{pdfdetach -saveall Relinquishment*.pdf}
\end{description}

A manifest of the complete cloudCrypt archive (174 files, 32MB) is included
as an attachment. The full archive is available on request to
\texttt{energyscholar+evidence@gmail.com}.
```

---

## Layer 3: Archive Manifest

Generate `cloudcrypt-manifest.txt` by running:

```bash
find /path/to/cloudCrypt -type f -exec sh -c \
  'echo "$(stat -c "%Y %s" "$1") $(sha256sum "$1" | cut -d" " -f1) $1"' \
  _ {} \; | sort -n > cloudcrypt-manifest.txt
```

This gives: timestamp, size, SHA-256, filename for every file. Embed this file. A researcher can request the full archive and verify each file against the manifest hashes.

Print a summary table in the visible appendix:

```latex
\subsection*{cloudCrypt Archive Summary}

The author's Google Drive archive, exported November 15, 2025, contains
174 files spanning 2011--2021. A complete manifest with SHA-256 hashes
is embedded as an attachment. Key statistics:

\begin{center}
\small
\begin{tabular}{l r r}
\hline
\textbf{Directory} & \textbf{Files} & \textbf{Date Range} \\
\hline
CC\_book/ & 27 & 2011--2016 \\
novel\_variant/ & 12 & 2012--2016 \\
Relinquishment/ & 45+ & 2012--2021 \\
docs/ (reference papers) & 15 & collected 2012--2013 \\
images/ (screenshots) & 10 & 2012 \\
\ldots & & \\
\hline
\textbf{Total} & \textbf{174} & \textbf{2011--2021} \\
\hline
\end{tabular}
\end{center}
```

---

## Session Transcripts (Tier C)

### What to Include

All sessions (1-9+) between Bruce and Claude. These document:
- The discovery process (how claims were investigated)
- Red-team methodology
- Evidence assessment evolution
- Probability calibration
- Bruce's real-time reactions and corrections

### Redaction Protocol

Before embedding, redact:
1. **OPSEC items** — anything Bruce hasn't published that could be self-incriminating
2. **Personal details** — phone numbers, physical addresses, non-public-figure real names
3. **API keys, credentials** — any accidentally pasted credentials
4. **System prompts** — Claude system instructions (they add noise, not signal)

Preserve:
- All substantive exchanges about the story, evidence, and claims
- Bruce's corrections of AI errors (demonstrates epistemic honesty)
- Red-team challenges and Bruce's responses
- Probability assessments and their evolution
- Moments where Bruce says "I don't know" or "that's wrong"

### Format

Single text file: `session-transcripts-redacted.txt`
Sections separated by session number and date.
Each redaction marked: `[REDACTED: category]`

---

## File Preparation Workflow

### Step 1: Copy Source Files (Generator)

Copy the 8 Tier A files from cloudCrypt to `relinquishment/attachments/originals/`.
Rename to clean, descriptive filenames (no spaces, no special chars):

```
attachments/originals/
├── 01-introduction-by-aurasys.docx
├── 02-the-artillect.docx
├── 03-autobiography-accidental-conspirator.docx
├── 04-relinquishment-forgiveness-permission.docx
├── 05-for-joe.txt
├── 06-biography-d-lane.docx
├── 07-speculative-fiction-unlikely-possibilities.docx
└── 08-journalistic-source-protection.docx
```

**CRITICAL:** Files must be BIT-FOR-BIT copies. No conversion, no re-saving, no opening in Word. `cp` only. The .docx metadata IS the evidence.

### Step 2: Capture Screenshots (Generator or Bruce)

Use a browser to visit each live URL. Full-page screenshot at high resolution.
Include the URL bar in the screenshot (proves the domain).
Save as PNG.

```
attachments/screenshots/
├── 09-cryptome-2012-03-17.png
├── 10-slashdot-2012-06-19.png
├── 11-blogspot-2012-05-13-orbital-qt.png
└── 12-blogspot-full-archive.png
```

### Step 3: Generate Manifest (Generator)

Run the manifest generation command. Save to `attachments/cloudcrypt-manifest.txt`.

### Step 4: Session Transcripts (Bruce)

Bruce redacts. Generator formats. Save to `attachments/session-transcripts-redacted.txt`.

### Step 5: Embed in LaTeX (Generator)

Add `\embedfile` commands to `historical-documents.tex` (from Plan 0013).
Add preamble changes.
Verify `make dev` compiles.

---

## Acceptance Criteria

1. `\usepackage{embedfile}` added to preamble.tex
2. All Tier A files (8) embedded as PDF attachments
3. All Tier B files (4 screenshots) embedded — OR flagged as pending capture
4. Tier C (transcripts) embedded — OR flagged as pending Bruce's redaction
5. Tier D (manifest) embedded
6. Reader instructions for accessing attachments included in visible appendix
7. Archive summary table printed in visible appendix
8. `make dev` succeeds with 0 errors
9. Embedded files verifiable: `pdfdetach -list output.pdf` shows all expected files
10. Total PDF size remains under 25MB
11. PDF/A-4 compliance maintained (verify with `make final` when Docker available)
12. All attached files are bit-for-bit identical to their sources (SHA-256 verification)

---

## Red Team

### 1. Apple Preview doesn't show attachments
**Severity: MEDIUM.** ~30% of readers may use Preview. Mitigation: clear instructions in the appendix for command-line extraction (`pdftk`, `pdfdetach`). This is a researcher feature, not a reader feature — researchers can handle a terminal command.

### 2. File size creep
**Severity: LOW.** Estimated 1.5-3.5MB of attachments. Current PDF is 388KB. Even with full chapter content (est. 2-5MB), total would be ~4-8MB. Well under 25MB. However: session transcripts are the wildcard. If they're 10MB+, they should be compressed before embedding. `embedfile` can embed .gz files.

### 3. .docx metadata exposure
**Severity: LOW-POSITIVE.** The .docx files contain Google Docs export metadata: author, timestamps, revision counts. This is EVIDENCE, not a leak. A forensic examiner can verify the files came from Google's export system. However: Bruce should review the files for any unexpected metadata (e.g., if he ever opened them on a shared computer). Run `python-docx` or `zipinfo` on each .docx to inspect metadata before embedding.

### 4. Modification after embedding
**Severity: NONE.** The whole point is that the SHA-256 hash covers the entire PDF including attachments. Any modification to any attachment changes the hash. This is exactly the provenance guarantee we want.

### 5. Viewer compatibility for `embedfile` vs `attachfile2`
**Severity: LOW.** `embedfile` produces standard PDF attachment annotations. `attachfile2` adds visible icons inline. `embedfile` is cleaner for our use case (invisible by default). Both produce standard-compliant PDFs. Use `embedfile`.

### 6. Copyright on embedded reference papers
**Severity: MEDIUM.** The cloudCrypt `docs/` directory contains academic papers (arXiv PDFs, BULLRUN docs). We are NOT embedding these — only Bruce's own writing. The manifest lists them by filename but doesn't include the files. If a researcher wants the Kitaev paper, they get it from arXiv.

### 7. Session transcript size and sensitivity
**Severity: HIGH.** This is the highest-risk embedded item. Transcripts are large and contain our full working process. Risks: (a) accidental OPSEC leak, (b) size bloat, (c) embarrassing AI errors preserved forever. Mitigations: (a) Bruce does manual redaction, (b) compress to .gz before embedding, (c) this is actually a feature — showing the AI making mistakes and Bruce correcting them demonstrates epistemic honesty. The redaction pass is non-negotiable. **This item should be the LAST thing embedded, after everything else is done.**

### 8. Embedded files not indexed by search engines
**Severity: NONE.** This is correct behavior. The visible appendix text IS indexable. The embedded files are for verification, not discovery.

### 9. `make dev` vs `make final` behavior
**Severity: LOW.** `embedfile` works in both dev (host) and final (Docker) builds. File paths must be relative to the build directory or absolute. Use relative paths from repo root. Test with `make dev` first; verify attachment listing.

### 10. Can the embedded .docx files carry macros/malware?
**Severity: LOW.** Google Docs exports are clean OOXML. No macros. But a paranoid reader might be concerned. Mitigation: note in the appendix that all .docx files are Google Docs exports (OOXML format, no macros). Researchers can verify with `zipinfo`.

### 11. What if a .docx file's internal metadata says "last modified 2025" because it was re-exported?
**Severity: MEDIUM.** If Bruce exported the archive in November 2025, the file modification dates on disk are 2025, but the INTERNAL Google Docs metadata (revision history) reflects the original edit dates. The .docx files in CC_book/ show filesystem dates from 2011-2016 — these appear to be the original Google Drive sync timestamps, NOT re-export timestamps. This is strong evidence. The plan should note this distinction and recommend that Bruce verify the file timestamps are original (not re-export).

**FINDING: The CC_book/ filesystem timestamps (2011-2016) are themselves evidence. They should be preserved in the manifest.**

### 12. What happens if Bruce adds more content to the appendix later?
**Severity: NONE.** New edition, new hash. The signed PDF is a point-in-time snapshot. This is by design.

---

## Red Team Verdict

**No blocking issues found.** The highest-risk item is session transcript redaction (Red Team #7), which is mitigated by making it the last step and requiring Bruce's manual redaction pass. All other risks are LOW or mitigated by existing architecture.

**One finding to add:** The CC_book/ filesystem timestamps should be explicitly noted as original Google Drive sync timestamps in the manifest and appendix text.

---

## Handoff Prompt

```
You are the Generator. Read plans/0014-hybrid-appendix-architecture.md.

Phase 1: File preparation
- Create relinquishment/attachments/originals/ directory
- Copy the 8 Tier A files (bit-for-bit, cp only) from the cloudCrypt
  archive paths listed in the plan. Use the clean filenames specified.
- Generate cloudcrypt-manifest.txt per the plan's command.
- DO NOT capture screenshots yet (requires browser + manual verification).
- DO NOT create session transcripts (requires Bruce's redaction).

Phase 2: LaTeX integration
- Add \usepackage{embedfile} to build/preamble.tex
- Add \embedfile commands to manuscript/appendix/historical-documents.tex
  (created by Plan 0013) for all Tier A files and the manifest.
- Add reader instructions and archive summary table per plan.
- Add placeholder \embedfile commands for Tier B (screenshots) and Tier C
  (transcripts) with comments noting they're pending.

Phase 3: Verification
- make dev succeeds with 0 errors
- pdfdetach -list on output PDF shows all embedded files
- Total PDF size check

Report: completion status, embedded file count, PDF size, any issues.
Flag: screenshots (Tier B) and transcripts (Tier C) as pending Bruce's action.
```
