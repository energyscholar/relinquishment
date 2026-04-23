# Plan 0022: AI Draft Markers (†)

**Purpose:** Mark AI-generated structural text so it's visually distinct from Bruce's prose. DMS version only — marks are trivially removable for final edition.
**Prerequisite:** Plans 0020 and 0024 already executed. Plan 0021 (red team fixes) resolved or in parallel.
**Deliverable:** `\aidraft{}` macro, chapter-level declarations, front matter explanation, verified in multiple PDF readers.

**Red team applied:** 2026-02-21. Fixes: C1 (pos22 reclassified after 0024 surgery), C2 (pos21/pos26 moved to NO MARKS per UQ3), H1 (pos11 line refs updated after 0024 walkout removal), H2 (MIXED count corrected 16→13), M1 (prerequisite updated).

---

## Phase 1: Macro Definition — ALREADY DONE

Macros already defined in `build/preamble.tex` (lines 171-176) during Plan 0024 execution. `\aidraftchapter` already present in pos22, pos24, pos28.

**Action:** Verify macros match spec below. If they match, skip to Phase 2.

```latex
% AI draft markers — DMS edition only
% To remove all marks for final edition: \renewcommand{\aidraft}[1]{#1}
\newcommand{\aidraftmark}{{\textsuperscript{\dag}}}
\newcommand{\aidraft}[1]{\aidraftmark\,#1}

% Chapter-level AI draft notice
\newcommand{\aidraftchapter}{%
  \begin{center}
  \small\textit{\dag\enspace AI structural draft from the author's source material}
  \end{center}
  \vspace{0.3cm}
}
```

## Phase 2: Front Matter Explanation

Add to `manuscript/00-front/copyright.tex`, after the Working Draft Notice:

```latex
\vspace{0.5cm}

\textbf{AI Structural Drafts}

\vspace{0.3cm}

Sections marked with a dagger (\dag) are AI structural drafts based on the author's
source material and twenty years of research notes. They preserve the author's facts
and arguments in a structure awaiting his prose. Unmarked sections are the author's
own writing. These markers will be removed as the author revises each section.
```

## Phase 3: Chapter Classification

### NO MARKS — Bruce's own prose, cloudCrypt imports, or reference material (11 chapters + appendices):

| Chapter | File | Source |
|---------|------|--------|
| Alpha Farm (2003) | pos02-alpha-farm.tex | Stub — too short to mark |
| The Mentor | pos03-the-mentor.tex | biography_D_Lane.txt + Autobiography |
| The Stories | pos05-the-stories.tex | HealerStories + Srebrenica Witness.docx |
| The Departure | pos07-the-departure.tex | Autobiography + HEALER-RECONSTRUCTION |
| The Weight | pos23-the-weight.tex | Autobiography + multiple Bruce docs |
| The Silence | pos29-the-silence.tex | Autobiography + HEALER-RECONSTRUCTION |
| Convergence Revisited | pos21-convergence-revisited.tex | Bruce's LG2QNN CH2, AI formatted only (UQ3=A) |
| Interdiction | pos26-interdiction.tex | Bruce's cloudCrypt doc, AI formatted only (UQ3=A) |
| Preface | preface.tex | Bruce's voice |
| What I Got Wrong | corrections.tex | Bruce's voice |
| What This Book Does Not Claim | disclaimers.tex | Bruce's voice (AI-structured, but editorial) |
| All appendices | various | Reference material, not narrative (UQ2=C) |

### CHAPTER-LEVEL `\aidraftchapter` — Mostly or entirely AI structural drafts (13 chapters):

| Chapter | File | Rationale | `\aidraftchapter` present? |
|---------|------|-----------|---------------------------|
| Three Possibilities | pos01-three-possibilities.tex | AI-written framing | No — add |
| The Code War | pos04-the-code-war.tex | AI-written bridge (from ultra-bridge.md) | No — add |
| Dual-Use | pos08-dual-use.tex | AI reference summary (LLM audit flagged) | No — add |
| The Braid | pos10-the-braid.tex | AI from HEALER-RECONSTRUCTION | No — add |
| The Threshold | pos12-the-threshold.tex | AI from HEALER-RECONSTRUCTION + LG2QNN | No — add |
| Genesis | pos13-genesis.tex | AI structural | No — add |
| **Why Give It Up** | **pos22-why-give-it-up.tex** | **Entirely AI rewrite after Plan 0024 surgery (was MIXED, now CHAPTER-LEVEL)** | **Yes — already present** |
| The Magnetosphere | pos32-the-magnetosphere.tex | AI from HEALER-RECONSTRUCTION | No — add |
| The Unipolar Condition | pos30-unipolar-condition.tex | AI from multiple sources | No — add |
| Extension | pos27-extension.tex | AI from LG2QNN + HEALER-RECONSTRUCTION | No — add |
| Ethical Framework | pos25-ethical-framework.tex | AI from HEALER-RECONSTRUCTION | No — add |
| Instantiation | pos24-instantiation.tex | AI structural (expanded by Plan 0024) | Yes — already present |
| Surrender | pos28-surrender.tex | AI structural (expanded by Plan 0024) | Yes — already present |

### MIXED — AI sections within Bruce-sourced chapters. Use `\aidraft{}` on AI paragraphs only (13 chapters):

**Note:** Generator must read each chapter and identify AI-written paragraphs by checking `\srcnote` annotations. Paragraphs with no source attribution are AI glue. Mark those with `\aidraft{}`.

| Chapter | File | AI sections |
|---------|------|-------------|
| The Secret | pos06-the-secret.tex | HEALER-RECONSTRUCTION glue sections (after line 60) |
| The Factoring Game | pos09-the-factoring-game.tex | GCHQ Precedent section (lines 66-79) is AI |
| The Experiment | pos11-the-experiment.tex | AI structural glue between imported sections. **NOTE: "Walking It Out" section removed by Plan 0024 — Generator must read current file, not rely on stale line numbers.** |
| First Light | pos15-first-light.tex | AI glue paragraphs |
| Thermal Ladder | pos16-the-thermal-ladder.tex | AI explanatory sections |
| The Capability | pos17-the-capability.tex | AI structural from Bruce's sources |
| The Walk-Out | pos18-the-walk-out.tex | AI glue between imported source blocks |
| Patrick Ball | pos19-patrick-ball.tex | AI analysis sections |
| The Network | pos20-the-network.tex | AI structural sections |
| Wolfram | pos31-wolfram.tex | AI structural from HEALER-RECONSTRUCTION |
| Digital Doppelganger | pos33-digital-doppelganger.tex | AI structural |
| The Research | pos34-the-research.tex | AI structural |
| The Question | pos35-the-question.tex | Artillect + Aurasys intro are BRUCE'S (timestamped 2013). AI glue around them. |

**Removed from MIXED (reclassified):**
- pos21 → NO MARKS (UQ3=A, Bruce's cloudCrypt content)
- pos22 → CHAPTER-LEVEL (entirely AI rewrite after Plan 0024 surgery)
- pos26 → NO MARKS (UQ3=A, Bruce's cloudCrypt content)

### UQ Answers (all resolved 2026-02-21)

| UQ | Question | Answer | Effect |
|----|----------|--------|--------|
| UQ1 | MIXED chapter marking | **B** — Mark AI paragraphs only | 13 MIXED chapters get precise `\aidraft{}` wrapping |
| UQ2 | Appendix material | **C** — No marks | Appendices are reference material |
| UQ3 | cloudCrypt chapters (pos21, pos26) | **A** — No marks | Bruce's content, AI just formatted → moved to NO MARKS |

## Phase 4: Implementation

For each chapter in the classification above:
1. If CHAPTER-LEVEL: add `\aidraftchapter` after `\chapter{...}` line (13 chapters total; 3 already have it from Plan 0024 — pos22, pos24, pos28 — so **10 chapters need the command added**)
2. If MIXED: read file, identify AI paragraphs (no `\srcnote`), wrap in `\aidraft{...}` (13 chapters — precise marking per UQ1=B)
3. NO MARKS: no changes (11 Bruce prose chapters + appendices per UQ2=C + cloudCrypt per UQ3=A)

## Phase 5: PDF Reader Testing

### Available reader: `okular` (KDE, installed)

Test protocol:
1. Build PDF: `make clean && make`
2. Open in okular: verify † marks render correctly
3. Check: dagger is superscript, not full-size
4. Check: `\aidraftchapter` italic notice renders centered
5. Check: marks don't break line spacing or paragraph flow
6. Check: marks visible in TOC? (they should NOT be)

### Additional reader tests:
7. `xdg-open Relinquishment.pdf` — test with system default viewer
8. `pdftotext Relinquishment.pdf - | grep "†"` — verify marks are in text layer (searchable/accessible)
9. Open in web browser: `firefox Relinquishment.pdf` or `chromium Relinquishment.pdf` (if available)
10. Print to PDF (okular print dialog) — verify marks survive print

### Verify removal:
11. Add `\renewcommand{\aidraft}[1]{#1}` and `\renewcommand{\aidraftchapter}{}` to preamble
12. Rebuild — verify all marks are gone
13. Remove the override lines, rebuild — verify marks return

## Test Cases

- TC1: Build completes with 0 LaTeX errors
- TC2: † visible in okular at 100% zoom
- TC3: † visible in at least one other reader
- TC4: `\aidraftchapter` notice renders as centered italic
- TC5: pdftotext captures the † character (accessibility)
- TC6: Removal override produces mark-free PDF
- TC7: No marks appear in TOC
- TC8: No marks in front matter (copyright, disclaimers, corrections)
- TC9: File size increase < 5KB (marks are lightweight)
- TC10: qpdf --check passes
