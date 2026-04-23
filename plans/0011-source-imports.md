# Plan 0011: Import Cleaned Source Files into Chapter Stubs

**Auditor:** Nightstalker, Session 9
**Date:** 2026-02-15
**Prerequisite:** Source pool cleaned (Session 9, ~115 corrections across 6 files + ultra-bridge)
**Builds on:** Plans 0002 (placeholder content), 0007 (pedagogical spiral), 0010 (structural scaffolding)

---

## Objective

Import the 6 cleaned source files into their designated chapter positions. Convert markdown to LaTeX. Preserve existing stub structure. Do not write new prose — import only.

---

## Imports (5 operations)

### Import 1: ultra-bridge.md → Pos4 (The Code War)

- **Source:** `manuscript/versions/ultra-bridge.md` (149 lines)
- **Target:** `manuscript/bridge/pos04-the-code-war.tex`
- **Track:** Bridge (`\settrack{trackbridge}`)
- **Current stub:** Empty (placeholder text only)

**Instructions:**
1. Read the source file. Skip the markdown title line (`# You Know This Story Already`).
2. Replace the placeholder line `\textit{[Content to be written per Plan 0007, Position 4.]}` with the converted content.
3. Convert markdown to LaTeX:
   - `---` horizontal rules → `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}` (use sparingly — only for major section breaks)
   - `## Heading` → `\section*{Heading}`
   - `### Heading` → `\subsection*{Heading}`
   - `**bold**` → `\textbf{bold}`
   - `*italic*` → `\textit{italic}`
   - Straight quotes → LaTeX quotes (`` `` `` and `''`)
   - `—` em dashes → `---`
   - Preserve paragraph breaks (blank lines between paragraphs = normal LaTeX paragraph separation)
4. The source has section structure: opener → "What the Movie Didn't Tell You" (3 subsections) → "The Work He Never Finished" → "Now Imagine It Happened Again" → closer. Preserve this structure.
5. Keep existing: comment header, `\settrack`, `\chapter`, `\label`, `\chapterreturn`.
6. Update the comment to: `% Source: manuscript/versions/ultra-bridge.md (imported Plan 0011)`

**Acceptance:** File compiles. Content matches source. No markdown artifacts remain.

---

### Import 2: srebrenica-witness.md → Pos5 (The Stories)

- **Source:** `manuscript/sources/srebrenica-witness.md` (58 lines)
- **Target:** `manuscript/track-2-testament/pos05-the-stories.tex`
- **Track:** T2 (`\settrack{tracktwo}`)
- **Current stub:** Contains full Kangaroos narrative (lines 19-58). DO NOT replace — APPEND after it.

**Instructions:**
1. Read the source file. Skip the header block (lines 1-7: title, source note, generator warning, `---`).
2. Insert a section break and the Srebrenica content AFTER the Kangaroos narrative, BEFORE `\chapterreturn`.
3. Add a section break: `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}`
4. The HALO jump opening paragraph (source line 11, beginning "I fall out of the moonlit night sky...") is ALREADY used as the epigraph at Pos2. Do NOT duplicate it as an opener here. Instead, begin with a brief transition sentence in Bruce's narrator voice, something like:

   ```latex
   \section*{Srebrenica, July 1995}

   Healer told this story only once. What follows is his account, as close to his words as memory allows.
   ```

   Then continue with the HALO paragraph and the rest of the source content. The reader has already seen the HALO excerpt at Pos2 — seeing it again here in full context is the spiral callback, not a duplication error. Keep it.

5. Convert markdown to LaTeX (same rules as Import 1).
6. The source includes Healer's first-person voice throughout — this is correct. It's reported speech within Bruce's narrative frame.
7. The Epstein/Dyncorp section (source lines 41-49) and the pub conversation (lines 41-49): keep as-is. This is Healer's reported speech of Sergeant Doe's reported speech. Triple-nested attribution provides legal cover.
8. The bibliography section at the end (source lines 51-58): convert to a footnote or endnote, not inline.
9. Update the file's comment header to note both sources:
   ```
   % Content: Kangaroos (from HealerStories archive) + Srebrenica Witness (imported Plan 0011)
   ```

**Acceptance:** File compiles. Kangaroos content unchanged. Srebrenica appended. No markdown artifacts.

---

### Import 3: gpt-history.md + unintended-consequences.md → Pos8 (Dual-Use)

- **Source 1:** `manuscript/sources/gpt-history.md` (204 lines)
- **Source 2:** `manuscript/sources/unintended-consequences.md` (44 lines)
- **Target:** `manuscript/bridge/pos08-dual-use.tex`
- **Track:** Bridge (`\settrack{trackbridge}`)
- **Current stub:** Empty (placeholder text only)

**Instructions:**
1. Read both source files. Skip header blocks (title, source notes, generator warnings, `---` separators).
2. Replace the placeholder line with the merged content.
3. Structure the chapter as follows:

   **Part A — General Purpose Technologies** (from gpt-history.md):
   - Opening section: What is a GPT? (source paragraphs on definition + fire + boating + agriculture)
   - `\section*{General Technologies in Prehistory}` — fire, boating, agriculture, metallurgy, wheel
   - The GPT timeline table: convert the What/When/Who entries (source lines 27-148) into a LaTeX table:
     ```latex
     \begin{tabular}{lll}
     \textbf{Technology} & \textbf{When} & \textbf{Who} \\
     \hline
     Stone toolmaking & $\sim$3 million years ago & Unknown \\
     ...
     \end{tabular}
     ```
   - `\section*{General Technologies in Early History}` — writing, Library of Alexandria, al-Khwarizmi, fossil fuel
   - `\section*{General Technologies in the Industrial Age}` — steam, electricity, radio, atomic power
   - `\section*{General Technologies in the Information Age}` — Lovelace, Turing, Ultra, transistor, Internet, DARPA, AI, genetic engineering, nanotechnology
   - The DARPA description block (source lines 181-185): keep, but trim to essentials. The ch3-relinquishment.md at Pos22 covers DARPA in more depth.

   **Part B — Unintended Consequences** (from unintended-consequences.md):
   - `\section*{Unintended Consequences}`
   - Whitney + cotton gin
   - Nobel + dynamite + Nobel Prize
   - Einstein + E=mc² + atomic weapons
   - The source's closing line about Einstein: "had he known in advance the unintended consequences... he would not have made those discoveries" — this is the thematic bridge to the COWS' relinquishment decision. End the chapter on this note.

4. Convert markdown to LaTeX (same rules).
5. The bibliography (gpt-history lines 197-204): convert to footnotes or a `\section*{Sources}` at chapter end.
6. Update comment: `% Source: gpt-history.md + unintended-consequences.md (imported Plan 0011)`

**Acceptance:** File compiles. Both sources represented. Table renders. No markdown artifacts.

---

### Import 4: turing-death.md → Pos14 (Growing a Mind)

- **Source:** `manuscript/sources/turing-death.md` (46 lines)
- **Target:** `manuscript/bridge/pos14-growing-a-mind.tex`
- **Track:** Bridge (`\settrack{trackbridge}`)
- **Current stub:** Empty (placeholder text only)

**Instructions:**
1. Read the source file. Skip the header block (lines 1-5: title, source note, `---`).
2. Replace the placeholder line with the converted content.
3. The source opens with a Turing quote — convert to epigraph:
   ```latex
   \begin{quote}
   \textit{``A computer would deserve to be called intelligent if it could deceive a human into believing that it was human.''}

   \hfill --- Alan Turing
   \end{quote}
   \vspace{0.5cm}
   ```
4. Convert markdown to LaTeX (same rules).
5. Note the inline editor notes in brackets:
   - Line 16: `[NOTE FOR GENERATOR: The apple was never tested...]` — convert to a LaTeX comment: `% NOTE: The apple was never tested for cyanide...`
   - Line 43: `[NOTE FOR GENERATOR: This Apple/Turing connection...]` — convert to LaTeX comment: `% NOTE: Apple/Turing connection is folklore, denied by Rob Janoff. Do not assert.`
6. The content has a natural dramatic arc: setting → Turing's suffering → his morphogenesis work → his death → legacy (Winterbotham, Apple, pardon, Kauffman/Wolfram continuation). Preserve this arc.
7. Update comment: `% Source: manuscript/sources/turing-death.md (imported Plan 0011)`

**Acceptance:** File compiles. Editor notes converted to comments. Epigraph renders. No markdown artifacts.

---

### Import 5: ch3-relinquishment.md → Pos22 (Why Give It Up)

- **Source:** `manuscript/sources/ch3-relinquishment.md` (212 lines)
- **Target:** `manuscript/bridge/pos22-why-give-it-up.tex`
- **Track:** Bridge (`\settrack{trackbridge}`)
- **Current stub:** Empty (placeholder text only)

**Instructions:**
1. Read the source file. Skip the header block (lines 1-16: title, source note, generator warning with bullet list of known issues, `---`).
2. **IMPORTANT:** The GENERATOR WARNING header lists known issues. These have ALL been fixed during Session 9 cleanup. The warning header is for pre-cleanup reference only. Do not apply the warning's corrections again — they are already in the text.
3. Replace the placeholder line with the converted content starting from line 18 ("Practical Cryptography and Project ULTRA II").
4. Section structure from the source — convert headings to LaTeX:
   - "Practical Cryptography and Project ULTRA II" → chapter intro (no section heading needed, the `\chapter{Why Give It Up}` title covers it)
   - "Project ULTRA II Origins" / "Why would DARPA conduct the ULTRA II project?" (lines 26-30) — these are alternate headings. Use: `\section*{Why Would DARPA Conduct Project ULTRA II?}`
   - "The state of Cryptography in 1990" → `\section*{The State of Cryptography in 1990}`
   - Line 58 `[GENERATOR TODO: Insert PKC technical section...]` → Keep as LaTeX comment: `% GENERATOR TODO: Insert PKC technical section here. [full text of the TODO]`
   - "One-way Arms Race" → `\section*{One-Way Arms Race}`
   - "Multi-way Arms race" → `\section*{Multi-Way Arms Race}`
   - "Total Relinquishment" → `\section*{Total Relinquishment}`
   - "Powerful Artificial Intelligence" → `\section*{Powerful Artificial Intelligence}`
   - "Partial Relinquishment" → `\section*{Partial Relinquishment}`
   - "What the ULTRA II COWS actually did" → `\section*{What the ULTRA II COWS Actually Did}`
5. Line 28-29 ("or") between two heading variants — delete. Use only the second heading.
6. The DARPA bullet list (lines 42-53): convert to LaTeX itemize:
   ```latex
   \begin{itemize}
   \item DARPA invented the Internet --- ...
   \item Small and flexible: ...
   ...
   \end{itemize}
   ```
7. The `[encrypted]` on line 113 ("reading other peoples' [encrypted] mail") — keep as-is in the text. It's inline, not an editor note.
8. URLs in the text (lines 195, 205-207): convert to `\url{}` or footnotes. The Bill Joy Wired article URLs should become footnotes.
9. Convert markdown to LaTeX (same rules as other imports).
10. Update comment: `% Source: manuscript/sources/ch3-relinquishment.md (imported Plan 0011)`

**Acceptance:** File compiles. GENERATOR TODO preserved as comment. Section structure matches source. URLs as footnotes. No markdown artifacts.

---

## General Rules for All Imports

1. **LaTeX compilation must succeed.** After all imports, run `make pdf` from the repo root. Fix any compilation errors.
2. **No new prose.** Import existing content only. Minor transition sentences (like the Srebrenica intro at Import 2) are allowed but should be minimal.
3. **Preserve all existing labels.** Do not modify `\label{}` tags or `\settrack{}` commands.
4. **Double-space between paragraphs** in the LaTeX source for readability. LaTeX ignores extra whitespace.
5. **Special characters:** Escape `&` → `\&`, `%` → `\%`, `#` → `\#`, `$` → `\$`, `_` → `\_` in body text. The `~` character → `\textasciitilde{}`. Watch for these in source files.
6. **Smart quotes:** Use ``` `` ``` and `''` for double quotes. Use `` ` `` and `'` for single quotes.
7. **Commit after each import** with message format: `Plan 0011 import N: [source] → pos[NN]`

---

## Verification

After all 5 imports:
1. `make pdf` compiles with 0 errors, 0 undefined references
2. PDF page count increases substantially (estimate: 43 → ~80-90 pages)
3. Each imported chapter appears in the PDF at its correct spiral position
4. No markdown formatting artifacts (`##`, `**`, `---` as literal text) visible in PDF
5. Table of contents shows all 5 new chapter titles
6. All `\chapterreturn` markers present (navigation works)

---

## Files Modified

| File | Action |
|------|--------|
| `manuscript/bridge/pos04-the-code-war.tex` | Replace placeholder with ultra-bridge content |
| `manuscript/track-2-testament/pos05-the-stories.tex` | Append srebrenica-witness after Kangaroos |
| `manuscript/bridge/pos08-dual-use.tex` | Replace placeholder with gpt-history + unintended-consequences |
| `manuscript/bridge/pos14-growing-a-mind.tex` | Replace placeholder with turing-death content |
| `manuscript/bridge/pos22-why-give-it-up.tex` | Replace placeholder with ch3-relinquishment content |

## Files Read (not modified)

| File | Purpose |
|------|---------|
| `manuscript/versions/ultra-bridge.md` | Source for Import 1 |
| `manuscript/sources/srebrenica-witness.md` | Source for Import 2 |
| `manuscript/sources/gpt-history.md` | Source for Import 3 |
| `manuscript/sources/unintended-consequences.md` | Source for Import 3 |
| `manuscript/sources/turing-death.md` | Source for Import 4 |
| `manuscript/sources/ch3-relinquishment.md` | Source for Import 5 |
| `plans/source-facts.md` | Cross-reference (do not modify) |
