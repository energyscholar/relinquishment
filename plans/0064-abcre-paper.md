# Plan 0064: ABCRE Paper — Nonlinear Bandpass Filter for Critical Transitions

*Auditor: Argus (Session 35, red-teamed same session). Origin: Phases 1-3 validated ABCRE operators as a criticality detector. Bruce decided: publish openly, no patent, free the math. Target: Chaos (AIP) primary, arXiv (nlin.CD + physics.data-an) simultaneous. JRSI is free (zero APC, 2026 S2O) but requires biological data we don't have — deferred to separate paper if ECoG validation added.*

---

## Red-Team Findings (Session 35)

Three critical tests run before plan finalization:

1. **Spearman AC₁ test (PASSED):** Spearman AC₁ perfectly survives heavy tails (retention 1.00 on t(df=3) vs Pearson's 0.00). BUT E-var still beats Spearman on real data: 16W-3L, **p=0.016** — stronger than vs Pearson (p=0.073). E's advantage is NOT an artifact of Pearson's fragility.

2. **Decomposition test:** C-only gets 82-91% of E-var Fisher on non-Gaussian data. ABR-only collapses to ~1%. C is the dominant mechanism; ABR adds ~15-20% on top. Paper must frame C as the key innovation with ABR as spatial refinement.

3. **Null model test (PASSED):** False positive rate < 10% across all null models (AR(1), pink noise, white noise). E-var has the best real-vs-null separation (+0.283). 14/19 thermoacoustic series significant above matched surrogates.

**Key reframe:** Primary comparison is E-var vs **Spearman AC₁** (p=0.016, significant), not Pearson AC₁ (p=0.073, marginal). This is the paper's headline result.

**Publication route:** Chaos (AIP) = $0 subscription access, perfect scope match for nonlinear dynamics methods. arXiv in nlin.CD + physics.data-an for open access. JRSI deferred (requires biological validation). Proc. R. Soc. A and SciPost Physics as alternatives (both potentially free).

**Authorship:** Robin qualifies via ICMJE criterion 1 (operator conception) but MUST review, approve, and accept accountability (criteria 2-4). AI (Claude) acknowledged in Methods, not listed as author. Data license (CC BY-NC-SA 4.0) is clean — academic use is non-commercial, analysis is "collection" not "adaptation."

---

## Paper Summary

**Title:** A nonlinear bandpass filter for detecting critical transitions: robustness advantages of bounded compression on non-Gaussian spatially-extended data

**Authors:** Bruce Stephenson, Robin Macomber
**AI disclosure:** "Computational analysis assisted by Claude (Anthropic). All results verified and approved by human authors."

**Repo:** `~/software/abcre-paper/`
**Validation code:** `~/software/abcre-validation/` (all results reproducible)

**Core claim:** A composition of four operators — gradient extraction (A), local coupling (B), circulation (R), and bounded compression (C) — forms a nonlinear bandpass filter whose robustness to non-Gaussianity is primarily due to C's bounded compression, with A/B/R providing spatial frequency refinement. E-var significantly outperforms Spearman-robust AC₁ on 19 thermoacoustic experiments (p=0.016) and has lower false positive rates on null models. Discriminability scales as n^1.04 with system size.

**What this is NOT:** A claim that E beats all existing methods. E ties raw variance on thermoacoustic data (p=0.83). The contribution is: (1) mechanism analysis showing C is the dominant robustness factor, (2) significant advantage over robust AC₁ on real data, (3) scaling result, (4) specificity analysis.

---

## Structure

### Section 1: Introduction (~500 words)
- Critical transitions in spatially-extended systems
- Existing EWS indicators (variance, AC₁, DFA) and their limitations
- The gap: non-Gaussian data degrades AC₁ even with rank-based robustification
- This paper: a nonlinear filter with demonstrable robustness and specificity

### Section 2: Operator Definitions and Transfer Function (~800 words)
- Define A, B, R, C with explicit formulas
- Derive H_E(k,ρ) = H_B(k)·H_R(k,ρ) analytically
- Prove all 24 orderings equivalent in linear regime (scalar commutation)
- Show bandpass shape, DC kill, and ρ as selectivity parameter
- Note: transfer function describes spectral selectivity (WHERE E looks); C's nonlinearity (Section 3) describes amplitude handling (HOW it processes)
- Figure 1: Transfer function |H_E|² for several ρ, overlaid with Ising S(k)

### Section 3: C's Nonlinearity and Operator Decomposition (~800 words)
- Three filters compared: E (nonlinear BCAR), linear-exact (BAR), linear-magnitude (|H|)
- Gaussian fields: E provides 3.5× Fisher improvement over linear filters
- Binary (Ising) data: all three identical. C can't compress ±1.
- **NEW: Decomposition analysis** — C-only vs ABR-only vs E-var:
  - C-only gets 82-91% of E-var Fisher on non-Gaussian data
  - ABR-only collapses to ~1% under heavy tails
  - E-var outperforms both — composition matters, but C dominates
- Conclusion: C is the key innovation; ABR provides spatial refinement
- Figure 2: Fisher bar chart (3 filters × 2 data types) + decomposition bars (E vs C-only vs ABR-only)

### Section 4: Comparison with Established Indicators (~700 words)
- Indicators: E-var (BCAR), raw variance, **AC₁ (Pearson)**, **AC₁ (Spearman)**, spectral β
- Gaussian fields: E-var Fisher=5.05, raw variance=1.73, Pearson AC₁=5.34, Spearman AC₁=5.2
- Ising: raw variance dominates (Fisher=358). E adds nothing on binary data.
- **NEW: Spearman AC₁ as the fair comparison.** Spearman is rank-based and survives heavy tails (retention 1.00 on t(df=3)). E-var still beats Spearman by ~10% on synthetic and significantly on real data.
- Honest comparison: E is competitive with robust AC₁ on continuous data, inferior on binary data.
- Figure 3: Fisher bars (5+ indicators × 2 data types) with Spearman prominently included

### Section 5: Size Scaling (~500 words)
- F ~ n^α from n=32 to 8192
- E-var α=1.04 [0.98, 1.11], R²=0.995
- Raw variance α=0.73 [0.63, 0.84]
- AC₁ α=1.21 [1.09, 1.34]
- Multi-seed stability: α=1.07 ± 0.02
- Breakpoint analysis: smooth drift, no sharp break
- E scales faster than variance, slower than AC₁ on clean Gaussian data
- Figure 4: Log-log Fisher vs n with power-law fits + sliding-window α

### Section 6: Robustness Mechanisms (~700 words)
- **Non-Gaussianity:** Heavy tails (t, df=3): E Fisher=5.7, **Spearman AC₁=5.2**, Pearson AC₁=0.0. Bursts: E=5.2, Spearman=4.6.
- **Colored noise:** E/AC₁ ratio increases monotonically with spectral slope β. Crossover at pink noise (β≈1). Real-world data lives at β=1-2.
- **Synthesis:** On clean Gaussian data, Spearman AC₁ matches E. On non-Gaussian data with colored noise (i.e., real data), E's advantage emerges — and survives even against rank-robust alternatives.
- Figure 5: Non-Gaussianity bar chart (including Spearman) + colored noise crossover curve

### Section 7: Real Data Validation + Specificity (~800 words)
- 19 thermoacoustic Hopf bifurcation experiments (Bury et al. 2021)
- Sliding window Kendall τ: E-var median=0.888, Spearman AC₁ median=0.835, variance median=0.866
- **E wins 16/19 vs Spearman AC₁ (Wilcoxon p=0.016)**
- E ties variance (p=0.83)
- The 3 series where AC₁ wins: most Gaussian-like (higher roughness p=0.014, lower kurtosis p=0.064)
- **NEW: Null model specificity.** FPR < 10% on AR(1), pink noise, white noise nulls. E-var has largest real-vs-null separation (+0.283 above worst-case null P95). 14/19 series significant above matched AR(1) surrogates.
- Figure 6: Sliding window plot + Kendall τ box plot + null model comparison panel

### Section 8: Discussion (~600 words)
- E is a purpose-built filter for continuous, non-Gaussian, spatially-extended data approaching criticality
- **C's bounded compression is the dominant mechanism** — provides ~85% of the robustness. ABR adds spatial frequency refinement.
- The operators are simple (O(n), one hyperparameter ρ) — a feature, not a limitation
- Applicable domains: thermoacoustic instability, potentially neural/structural/geophysical
- Limitations: 1D only, nearest-neighbor coupling assumed, doesn't work on binary data, ties variance on this dataset, only one empirical domain tested
- The scaling result suggests E's advantage grows with sensor array size — relevant for high-density monitoring

### Section 9: Methods (~400 words)
- Gaussian random field generation (FFT-based, Lorentzian spectrum)
- Ising sampler (Metropolis-Hastings, burn-in, thinning)
- Fisher discriminant ratio definition
- Sliding window protocol (detrending, window size, Kendall τ)
- Null model generation (AR(1), colored noise, matched surrogates)
- AI disclosure statement
- All code available at [GitHub repo URL]

### References (~30 citations)
Key: Scheffer 2009, Dakos 2012, Bury 2020, Bury 2021, Ghanavati 2014, Maturana 2020

---

## Figures (7 total)

1. Transfer function |H_E|² + Ising S(k) overlay
2. Nonlinearity + decomposition: E vs linear filters + C-only vs ABR-only
3. EWS comparison: Fisher bars (5+ indicators × 2 data types, Spearman included)
4. Size scaling: log-log with power-law fits
5. Robustness mechanisms: non-Gaussianity (with Spearman) + colored noise
6. Real data: sliding window + 19-series box plot
7. **NEW:** Null model specificity: null τ distributions + real vs null separation

Figures 1-6 already generated in `~/software/abcre-validation/figures/`. Fig 2 and 5 need reformatting to include decomposition and Spearman. Fig 7 generated as `null_model_test.png`. All will need reformatting for publication (single-column, colorblind-safe palette, consistent font sizes).

---

## Implementation Plan

### Part 1: Paper scaffold
**File:** `paper.tex` (LaTeX, Chaos/AIP template or REVTeX)
- Download REVTeX4 template (AIP/Chaos uses REVTeX)
- Set up sections, bibliography, figure placeholders
- Write abstract (~200 words)

### Part 2: Sections 1-2 (intro + operators)
- Write introduction (frame for nonlinear dynamics audience)
- Write operator definitions with equations
- Transfer function derivation
- Generate publication-quality Figure 1

### Part 3: Sections 3-5 (core results)
- Nonlinearity + decomposition writeup + Figure 2 (include C-only/ABR-only)
- EWS comparison writeup + Figure 3 (include Spearman AC₁)
- Size scaling writeup + Figure 4

### Part 4: Sections 6-7 (mechanisms + real data + specificity)
- Robustness mechanisms writeup + Figure 5 (include Spearman)
- Real data validation writeup + Figure 6
- Null model specificity writeup + Figure 7

### Part 5: Sections 8-9 (discussion + methods)
- Discussion (honest limitations, C-dominant framing)
- Methods (include AI disclosure)
- References
- Final proofreading pass

### Part 6: Supplementary material
- All 24 orderings comparison table
- C-position grouping analysis
- ρ optimization curves
- Full 19-series Kendall τ table (all indicators including Spearman)
- Noise sweep extended results
- Full null model results (all thresholds, all models)
- Matched surrogate details per series

---

## File Structure

```
~/software/abcre-paper/
├── paper.tex           # Main manuscript (REVTeX4)
├── supplement.tex      # Supplementary material
├── references.bib      # Bibliography
├── figures/            # Publication-quality figures
│   ├── fig1_transfer_function.pdf
│   ├── fig2_decomposition.pdf
│   ├── fig3_ews_comparison.pdf
│   ├── fig4_scaling.pdf
│   ├── fig5_robustness.pdf
│   ├── fig6_real_data.pdf
│   └── fig7_null_model.pdf
├── scripts/            # Figure-generation scripts (import from abcre-validation)
│   └── make_figures.py
└── .gitignore
```

---

## Acceptance Criteria

- T64.1: Paper compiles without errors (REVTeX4/pdflatex)
- T64.2: All 7 figures render correctly
- T64.3: Abstract ≤ 200 words
- T64.4: Total word count 4000-6000 (Chaos typical length)
- T64.5: Every numerical claim traceable to a specific test in abcre-validation
- T64.6: Limitations section explicitly states: ties variance on thermoacoustic, loses on binary data, 1D only, single empirical domain
- T64.7: Primary AC₁ comparison uses Spearman (rank-robust), not Pearson. Pearson included for context only.
- T64.8: Decomposition analysis (C-only vs ABR-only) is presented honestly — C gets 82-91%, ABR adds 15-20%
- T64.9: Null model specificity results included (FPR, separation, matched surrogates)
- T64.10: References include all key EWS papers (Scheffer, Dakos, Bury ×2, Ghanavati)
- T64.11: Code availability statement with repo URL
- T64.12: AI disclosure statement in Methods
- T64.13: All figures colorblind-safe
- T64.14: No overclaiming — "significantly outperforms robust AC₁" (p=0.016) but "ties raw variance" (p=0.83)

---

## Style Notes

- Write for nonlinear dynamics / signal processing audience (Chaos readership)
- Assume reader knows Fourier analysis, bifurcation theory, basic statistics
- Don't assume reader knows ABCRE operators or their origin
- Present operators as new constructions motivated by signal processing principles
- No reference to the book, Healer, QRR, or Relational Relativity
- Honest, understated tone — let the numbers speak
- Frame C as the key insight, not the four-operator composition
- Anticipate reviewer objections (Spearman, decomposition, specificity) — address them in the text

---

## Pre-Submission Checklist

- [ ] Robin has reviewed manuscript and approved (ICMJE criteria 2-4)
- [ ] AI disclosure statement included
- [ ] Data attribution to Bury et al. (2021) and Pavithran & Sujith with license noted
- [ ] arXiv submission prepared (nlin.CD primary, physics.data-an cross-list)
- [ ] Chaos submission package prepared (REVTeX, figures as separate EPS/PDF)
- [ ] Code repository public and linked

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0064-abcre-paper.md

Working directory: ~/software/abcre-paper/
Six parts, one commit per part. Message format: "Plan 0064 part N: description"
Validation code is in ~/software/abcre-validation/ — import/reference but don't copy.
LaTeX paper (REVTeX4). Generate publication-quality figures.
Key data files for figures:
- ~/software/abcre-validation/robustness_redteam.py (Spearman + decomposition results)
- ~/software/abcre-validation/null_model_test.py (specificity results)
- ~/software/abcre-validation/FINDINGS.md (all Phase 3 results)
```
