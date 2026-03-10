# Plan 0073: Criticality Paper — Polish Pass (Pre-Robin)

**Repo:** `~/software/criticality-paper/`
**Scope:** 6 targeted edits to the current 22-page paper. No structural changes.
**Estimated effort:** Single generator session, <30 minutes.

---

## Context

The paper (`Stephenson_CrossDomainCriticality_2026.tex`) has been through a deep red-team pass. All CRITICAL and MODERATE issues are fixed. Citation data (Table 2) updated to 15-seed analysis. This plan addresses 3 remaining red-team LOWs + 3 cheap FACETS compliance fixes.

Key files:
- `Stephenson_CrossDomainCriticality_2026.tex` — main paper
- `Stephenson_CrossDomainCriticality_2026.bib` — bibliography
- `analysis/data/processed/analysis_report_15seed.md` — 15-seed analysis report (sensitivity data here)
- `analysis/data/processed/sensitivity.json` — sensitivity analysis data

---

## Phase 1: Red-Team LOWs (3 items)

### 1A. Sensitivity analysis text

The table footnote (Table 2, `tab:citations`) says "see sensitivity analysis in text" but no sensitivity data appears inline.

**Action:** Add 2-3 sentences after the null model paragraph (the one starting "This null model assumes unrestricted mixing...") presenting sensitivity bounds. Use data from `analysis/data/processed/analysis_report_15seed.md`, section "Sensitivity Analysis."

Content to convey:
- Worst/best case bounds for unknown classifications (what if all unknowns are same-domain? all cross-domain?)
- Merged Biology+Biomedical robustness check (does the siloing conclusion hold if these two are one domain?)
- Key message: core finding (siloed in all periods) is robust to both perturbations

Keep it tight — 2-3 sentences, no new table. The conclusion shouldn't change, just show you checked.

### 1B. Table 3 (functional correspondence, `tab:equiv`) — add new domain rows

Three domains discussed in Section 2 have no entries in Table 3: seismology, linguistics, urban science.

**Action:** Add rows to Table 3:

| Domain | Parameter | Common name | Meaning | Critical Value |
|--------|-----------|-------------|---------|----------------|
| Seismology | $b$ | $b$-value (Gutenberg-Richter) | Frequency-magnitude scaling exponent | $b \approx 1$ |
| Linguistics | $\gamma$ | Zipf exponent | Word rank-frequency scaling | $\gamma \approx 1$ |
| Urban | $\beta$ | City scaling exponent | Superlinear scaling with population | $\beta > 1$ (innovation) |

Note: These are empirical scaling exponents, not correlation-length diagnostics. Add a brief note after the table distinguishing them from the correlation-decay parameters: something like "The last three entries are empirical scaling exponents from power-law distributions rather than correlation-decay diagnostics; they are included to show the breadth of critical-point mathematics across domains."

Generator discretion on exact wording and whether to fold this into the existing "Note on parameter types" paragraph below the table.

### 1C. Float placement

All five tables use `[h]` which LaTeX overrides to `[ht]`, producing warnings.

**Action:** Change all `\begin{table}[h]` to `\begin{table}[ht]` throughout the file.

---

## Phase 2: FACETS Quick Fixes (3 items)

### 2A. Remove citation from abstract

Line 48 contains `\cite{sornette2004}` inside the abstract. FACETS prohibits citations in abstracts.

**Action:** Replace `Sornette (2004) \cite{sornette2004}` with `Sornette's 2004 textbook` (or similar phrasing that removes the `\cite{}`). The full citation appears multiple times in the body; no information is lost.

### 2B. Trim keywords from 8 to 6

Line 51: currently 8 keywords. FACETS allows max 6.

**Action:** Remove the two least distinctive keywords. Recommended cuts: "self-organized criticality" (subset of "critical phenomena") and "edge of chaos" (subset of "phase transitions"). Keep: critical phenomena, phase transitions, convergent discovery, correlation analysis, detrended fluctuation analysis, Hurst exponent.

Generator discretion on which two to cut.

### 2C. Data availability statement

FACETS requires a data availability statement.

**Action:** Add after Acknowledgments, before `\bibliographystyle`:

```latex
\subsection*{Data Availability}

Citation data were retrieved from the Semantic Scholar API (public tier). Analysis code and processed data are available at [repository URL to be added prior to submission].
```

Use `\subsection*` (unnumbered) or `\section*` depending on what looks right in context. The bracketed placeholder is intentional — Bruce will fill in the repo URL before submission.

---

## Acceptance Criteria

1. Paper compiles clean (`pdflatex` + `bibtex` + 2x `pdflatex`): no errors, no undefined references
2. No `\cite{}` commands inside `\begin{abstract}...\end{abstract}`
3. Keywords ≤ 6
4. All `\begin{table}` use `[ht]` not `[h]`
5. Sensitivity analysis text present near Table 2
6. Table 3 has ≥ 10 rows (was 7, adding 3)
7. Data availability statement present
8. No new content beyond what this plan specifies — surgical edits only
9. Page count remains 21-23 pages (no structural bloat)

---

## What NOT to Do

- Do not restructure sections or move content between sections
- Do not touch appendices (deferred to compression phase)
- Do not switch to natbib/author-year (deferred)
- Do not add double-spacing or line numbers (submission formatting, deferred)
- Do not modify the citation analysis data or re-run scripts
- Do not add new references to the .bib file
