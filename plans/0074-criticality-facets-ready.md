# Plan 0074: Criticality Paper — FACETS-Ready Conversion

**Repo:** `~/software/criticality-paper/`
**Input:** Current 22-page polished version (post Plan 0073)
**Target:** FACETS Perspectives submission-ready manuscript, ~16pp single-spaced
**Estimated effort:** Multi-phase, likely 2-3 generator sessions

---

## Overview

FACETS (Canadian Science Publishing) has specific requirements that differ from the current manuscript format. This plan restructures the paper for FACETS submission in four phases:

1. **Appendix restructuring** (FACETS doesn't publish appendices)
2. **Content compression** (22pp → ~16pp)
3. **natbib conversion** (numbered → author-year citations)
4. **Submission formatting** (double-spacing, line numbers)

Each phase should compile clean before proceeding to the next.

---

## Reference Files

- `analysis/compression_plan.md` — detailed section-by-section compression guide
- `analysis/facets_optimization_plan.md` — full FACETS compliance audit (Sections 1-19)
- `analysis/data/processed/analysis_report_15seed.md` — citation analysis data
- Current paper: `Stephenson_CrossDomainCriticality_2026.tex`
- Current bib: `Stephenson_CrossDomainCriticality_2026.bib`

---

## Phase 1: Appendix Restructuring

FACETS does not publish appendices. All three must be handled.

### 1A. Appendix C (Operator Definitions) → Supplementary Material

Create a new file `Stephenson_CrossDomainCriticality_2026_supplementary.tex` containing the full operator definitions (current lines 586-651). This becomes a standalone supplementary PDF uploaded to ScholarOne.

In the main paper, replace the `\section{Metatron Dynamics Operator Definitions}` appendix with a single sentence in Appendix A (or its replacement): "Operator definitions are provided in the Supplementary Material."

### 1B. Appendix A (Metatron Dynamics) → Main Text Section

Split current Appendix A into two parts:

**Keep in main text** (as a new section before Discussion, or as a subsection of Discussion):
- "How This Paper Originated" — compress to ~150 words. Keep: engineers derived operators → behavior resembled phase transitions → literature search → found convergence pattern. This is legitimate Perspectives content.
- "Disclosure" — keep verbatim (legally required).
- "Framework Summary" — compress to 2-3 sentences. The operator details are in supplementary now; just say what E does and what κ_m measures.

**Move to Supplementary Material:**
- The Ising correspondence test table and surrounding text. The 32×32 lattice with 200 samples and no error bars won't survive peer review as main-text evidence. In supplementary, it's illustrative and fine.

Update the COI paragraph to reference the new section location instead of "Appendix~\ref{app:correspondence}".

### 1C. Appendix B (Plain Language) → PLS + cut

Current state: 3-paragraph hook + URL (already compressed from earlier work).

**Action:** Move the first paragraph (the core plain-language description, ~80 words) to a new "Plain Language Summary" field after Keywords. This is the FACETS PLS slot. Keep it under 150 words.

Delete the remaining appendix section entirely. The URL to freethemath.org already appears in the abstract.

### 1D. Fix all cross-references

After restructuring:
- `\ref{app:correspondence}` → new section label
- `\ref{app:operators}` → "Supplementary Material"
- `\ref{app:plainlanguage}` → remove or update
- Remove `\appendix` command
- Update COI paragraph references
- Update the `\thanks` footnote if it references appendices

**Acceptance (Phase 1):** Clean compile. No `\appendix` command. No undefined references. Supplementary .tex file exists and compiles independently. Main paper is shorter by ~4-5 pages.

---

## Phase 2: Content Compression (target ~16pp)

Follow the disposition guide in `analysis/compression_plan.md`. Key cuts below, grouped by priority.

### 2A. Largest savings — already done
Appendix B replacement (Phase 1) saves ~3pp. This is the single biggest win.

### 2B. Section 2 (Cross-Domain Discoveries) — compress ~1.2pp

Currently the bulkiest section (~5.5pp). Per compression plan:

- **2.2 Complexity Science**: Cut to 1 tight paragraph. Keep Bak + Kauffman key facts only.
- **2.4 Finance**: Cut Mantegna/Stanley econophysics detail and Sornette 2003 log-periodic detail. Keep Hurst equation, Peters, Mandelbrot classification. (~0.8pp → 0.4pp)
- **2.5 Machine Learning**: Cut the batch normalization paragraph (lines ~208-209). Keep Jaeger/spectral radius, Saxe mention. (~0.8pp → 0.4pp)
- **2.8 Traffic Flow**: Cut Kerner three-phase itemized list. Compress to prose: keep Greenshields + Kerner classification note. (~0.6pp → 0.3pp)
- **Keep at current length**: 2.9 Thermohaline/Climate (bus anecdote, reviewer connection), 2.10-2.12 new domain subsections (already tight).

### 2C. Section 3 (Evidence) — compress ~0.9pp

- **Notation Divergence**: Cut the Newton/Leibniz calculus analogy paragraph (lines ~327-336). Move "Bury, personal communication" to a footnote. Keep core notation divergence argument. (~0.3pp saved)
- **Institutional Separation**: Compress conference program review to 1 sentence. (~0.2pp saved)
- **Methodological caveats paragraph** (line ~319): Compress. The detailed caveats about sampling, S2 classification, CS/ML dominance — tighten to 3 sentences max. Detail can go to supplementary. (~0.4pp saved)

### 2D. Section 5 (Convergence Analysis) — compress + merge ~0.8pp

- **Merge 5.2 + 5.3** into 5.1. One section "Convergence Analysis" with no subsections.
- Cut Newton/Leibniz/Wallace/Darwin (line ~468) — calculus analogy already used in (now-cut) Section 3 notation divergence.
- Keep "correlation scaling emerges... as Fourier analysis emerges for periodic signals."
- Keep timeline table.

### 2E. Section 6 (Discussion) — compress ~0.5pp

- Merge 6.1 Scientific Implications + 6.2 Knowledge Accessibility into one paragraph.
- Cut category theory future direction (line ~493, speculative).
- Compress limitations: keep scope limitation paragraph (broadening "criticality" risk), trim others.
- Keep "no institution can reasonably claim ownership" — softened to "the pattern of multiple independent derivations complicates any single claim of ownership" per FACETS tone guidance.

### 2F. Section 1 (Introduction) — minor trim ~0.2pp

- Historical Context: cut the Cvitanovic 1984 sentence (line 76). The point is already made by the preceding paragraph.
- Definitions: compress the five classification definitions to tighter wording (shorter `\item` descriptions).

### 2G. Section 4 (Functional Correspondence) — minor trim ~0.2pp

- HRV footnote: compress to 2 sentences. Cut the Mora/Bialek parenthetical debate.
- Merge "Clarification" and "Note on parameter types" into one combined note.

**Acceptance (Phase 2):** Clean compile. Page count 15-17 (single-spaced). No content removed that is listed as "MUST keep" in compression_plan.md Section 3 (bus anecdote, equivalence chain, tables 1-4, COI, thermohaline section). All new domain material (seismology, linguistics, urban) retained.

---

## Phase 3: natbib Conversion

### 3A. Package changes

In preamble:
- Remove `\usepackage{cite}`
- Add `\usepackage[authoryear,round]{natbib}`
- Change `\bibliographystyle{plain}` to `\bibliographystyle{apalike}`

### 3B. Convert all \cite commands (33 total)

Each `\cite{}` must become either:
- `\citep{}` — parenthetical: (Author Year). Use for most citations.
- `\citet{}` — textual: Author (Year). Use when the author name is part of the sentence.

**Decision rule:** If the sentence reads naturally with the author name inline (e.g., "Onsager's exact solution"), use `\citet{}`. If the citation is a parenthetical reference at the end of a clause, use `\citep{}`.

Examples from current text:
- `Onsager's exact Ising solution \cite{onsager1944}` → `Onsager's exact Ising solution \citep{onsager1944}` (already parenthetical)
- `Bak, Tang, and Wiesenfeld introduced SOC \cite{bak1987}` → `\citet{bak1987} introduced SOC` or keep as `introduced SOC \citep{bak1987}`
- `\cite{sornette2004}` standalone → `\citep{sornette2004}`
- Multi-cites like `\cite{sornette2009dragonking, sornette2012dragonking}` → `\citep{sornette2009dragonking, sornette2012dragonking}`

Generator discretion on each of the 33 calls. The goal is natural-reading author-year citations.

### 3C. Verify bib entries

Check that all .bib entries have complete `author` and `year` fields (required for author-year style). Current entries look complete based on earlier review, but verify after compile.

**Acceptance (Phase 3):** Clean compile. No numbered references anywhere. All citations render as (Author Year) or Author (Year). No LaTeX warnings about undefined citations. Reference list sorted by author name (apalike default).

---

## Phase 4: Submission Formatting

### 4A. Double-spacing

Add to preamble:
```latex
\usepackage{setspace}
```
Add after `\begin{document}`:
```latex
\doublespacing
```

### 4B. Line numbering

Add to preamble:
```latex
\usepackage{lineno}
```
Add after `\begin{document}`:
```latex
\linenumbers
```

### 4C. Title page numbering

Add after `\maketitle`:
```latex
\thispagestyle{plain}
```

### 4D. Plain Language Summary placement

If not already placed in Phase 1, ensure the PLS appears after Keywords and before the Introduction, per FACETS manuscript organization requirements.

**Acceptance (Phase 4):** Clean compile. Double-spaced throughout. Line numbers visible in left margin. Page numbers on all pages including title page. Expected page count ~30-35pp (double-spaced). PDF ready for ScholarOne upload.

---

## Red-Team Fixes (applied post-review)

### RT1. Saxe year mismatch (MODERATE)

The bib entry `saxe2013` has `year={2014}` (ICLR conference date) but the text says "Saxe et al. (2013)" on line ~206 and "2013" in the timeline table. After natbib conversion, the rendered citation will say "(Saxe et al., 2014)" contradicting the prose.

**Fix (Phase 3):** Change the bib entry to `year={2013}` and add `note={Presented at ICLR 2014}`. This matches the arXiv preprint date the text follows.

### RT2. Abstract references "Appendix~A" (MODERATE)

Line 46: "presented in Appendix~A" will be a broken reference after Phase 1 kills appendices.

**Fix (Phase 1, step 1D):** Update abstract to reference the new Discussion subsection instead.

### RT3. lineno + amsmath equation overlap (MODERATE)

`\usepackage{lineno}` produces overlapping/missing line numbers on `equation` environments. The paper has ~10 equations.

**Fix (Phase 4):** Use `\usepackage[mathlines]{lineno}` instead of plain `\usepackage{lineno}`. If that still has issues, add after loading both packages:
```latex
% Fix lineno + amsmath compatibility
\newcommand*\patchAmsMathEnvironmentForLineno[1]{%
  \expandafter\let\csname old#1\expandafter\endcsname\csname #1\endcsname
  \expandafter\let\csname oldend#1\expandafter\endcsname\csname end#1\endcsname
  \renewenvironment{#1}%
    {\linenomath\csname old#1\endcsname}%
    {\csname oldend#1\endcsname\endlinenomath}}%
\patchAmsMathEnvironmentForLineno{equation}
\patchAmsMathEnvironmentForLineno{align}
```

### RT4. AI-assisted search expansion — document honestly (NEW CONTENT)

The paper's Acknowledgments note AI-assisted literature search, but the paper doesn't document a key methodological finding: a single additional round of AI-assisted search (beyond the original manual survey) expanded the domain count from approximately nine to twelve. This suggests the survey is likely incomplete — further systematic search would probably find additional domains.

**Fix (Phase 2, during compression of Limitations):** Add 2-3 sentences to the Limitations subsection, something like:

> Our survey expanded from an initial nine domains to twelve after a single round of AI-assisted literature search beyond the original manual survey. That one additional pass yielded three new domains (seismology, linguistics, urban scaling) suggests the convergence pattern is broader than documented here. A systematic review — beyond this paper's scope — would likely identify further instances.

This is honest, strengthens the paper (the pattern is probably even bigger than we show), and pre-empts "why didn't you find X?" reviewer objections. It also documents the AI search methodology transparently.

Also update the Future Directions paragraph to reference this: the AI-assisted expansion is itself evidence that the convergence pattern invites further documentation.

### RT5. LOW issues (leave for generator discretion)

- **Cvitanovic cut**: Consider keeping — it preempts "didn't chaos community already know?" Generator's call.
- **Line numbers shifted**: Navigate by section/content descriptions, not line numbers from compression_plan.md.
- **MD section placement**: Recommend Discussion subsection titled "Genesis of This Investigation" or "Motivating Framework."

---

## What NOT to Do

- Do not modify the citation analysis data or scripts
- Do not add new references to the .bib (unless a cut creates an orphan that needs removal)
- Do not change the convergence thesis, classification taxonomy, or quantitative claims
- Do not soften honest hedging ("between six and twelve", "qualified independent")
- Do not remove the bus anecdote, equivalence chain, any of the four tables, or the COI disclosure
- Do not cut the thermohaline/climate subsection (reviewer connection)
- Do not create a .bst file — use `apalike` (standard, close enough for submission; production reformats)
- Do not add content beyond what this plan specifies (RT4 is the sole exception — 2-3 sentences in Limitations). Every other edit should reduce word count or be format-neutral

## Notes for Generator

- Phases are sequential. Complete each phase, verify clean compile, before starting the next.
- If page count after Phase 2 lands at 17pp, that's fine. Don't force cuts to reach exactly 16. The sweet spot is 15-17pp single-spaced.
- The Ising test table move to supplementary is the most structurally complex operation. Do it carefully — make sure the supplementary file compiles standalone with all necessary packages and the table renders correctly.
- For natbib, `apalike` may not perfectly match FACETS house style. That's acceptable — FACETS production reformats references. Close is good enough.
- The `\thanks` footnote currently references appendices. After Phase 1, it may need rewording if appendix labels are gone.
