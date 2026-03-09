# Plan 0064: ABCRE Paper — Nonlinear Bandpass Filter for Critical Transitions

*Auditor: Argus (Session 35). Origin: Phases 1-3 validated ABCRE operators as a criticality detector. Bruce decided: publish openly, no patent, free the math. Target: J. Royal Society Interface (where Bury 2020 published spectral EWS). arXiv preprint first.*

---

## Paper Summary

**Title:** A nonlinear bandpass filter for detecting critical transitions: robustness advantages of bounded compression on non-Gaussian spatially-extended data

**Authors:** Bruce Stephenson, Robin Macomber

**Repo:** `~/software/abcre-paper/`
**Validation code:** `~/software/abcre-validation/` (all results reproducible)

**Core claim:** A composition of four simple operators — gradient extraction (A), local coupling (B), circulation (R), and bounded compression (C) — forms a nonlinear bandpass filter whose discriminability scales as n^1.04 with system size and is robust to non-Gaussianity and colored noise. Validated on 19 real thermoacoustic experiments.

**What this is NOT:** A claim that E beats all existing methods. E ties raw variance and marginally beats AC₁ on thermoacoustic data. The contribution is the mechanism analysis (why nonlinear compression helps) and the scaling result (how much it helps at large n).

---

## Structure

### Section 1: Introduction (~500 words)
- Critical transitions in spatially-extended systems
- Existing EWS indicators (variance, AC₁, DFA) and their limitations
- The gap: non-Gaussian data degrades AC₁; raw variance doesn't exploit spatial structure efficiently
- This paper: a nonlinear filter with provable robustness properties

### Section 2: Operator Definitions and Transfer Function (~800 words)
- Define A, B, R, C with explicit formulas
- Derive H_E(k,ρ) = H_B(k)·H_R(k,ρ) analytically
- Prove all 24 orderings equivalent in linear regime (scalar commutation)
- Show bandpass shape, DC kill, and ρ as selectivity parameter
- Figure 1: Transfer function |H_E|² for several ρ, overlaid with Ising S(k)

### Section 3: C's Nonlinearity — When Does It Help? (~600 words)
- Three filters compared: E (nonlinear BCAR), linear-exact (BAR), linear-magnitude (|H|)
- Gaussian fields: E provides 3.5× Fisher improvement. Linear filters are equivalent.
- Binary (Ising) data: all three identical. C can't compress ±1.
- Conclusion: C helps on continuous data, not binary. The improvement is entirely from bounded compression.
- Figure 2: Fisher ratio bar chart (Ising vs Gaussian, 3 filters, 2 ρ values) + noise robustness curves

### Section 4: Comparison with Established Indicators (~600 words)
- Six indicators: E-var (BCAR), E-var (ABRC), E-concentration, raw variance, AC₁, spectral β
- Gaussian fields: E-var Fisher=5.05, raw variance=1.73, AC₁=5.34
- Ising: raw variance dominates (Fisher=358). E adds nothing on binary data.
- Honest comparison: E is competitive with AC₁ on continuous data, inferior on binary data.
- Figure 3: Fisher bars + monotonicity (Ising and Gaussian side by side)

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
- **Non-Gaussianity:** Heavy tails (t, df=3): E Fisher=5.7, AC₁=0.0. Bursts: E=5.2, AC₁=0.9. E is rock-stable; AC₁ collapses.
- **Colored noise:** E/AC₁ ratio increases monotonically with spectral slope β. Crossover at pink noise (β≈1). Real-world data lives at β=1-2.
- **Synthesis:** On clean Gaussian data, AC₁ beats E. On non-Gaussian data with colored noise (i.e., real data), E's advantage emerges.
- Figure 5: Non-Gaussianity bar chart + colored noise crossover curve

### Section 7: Real Data Validation (~600 words)
- 19 thermoacoustic Hopf bifurcation experiments (Bury et al. 2021)
- Sliding window Kendall τ: E-var median=0.887, AC₁ median=0.816, variance median=0.856
- E wins 16/19 vs AC₁ (Wilcoxon p=0.073)
- E ties variance (p=0.83)
- The 3 series where AC₁ wins: higher roughness (p=0.014), lower kurtosis (p=0.064), near-zero intermittency — most Gaussian-like series
- This confirms the mechanism: E's advantage is non-Gaussianity robustness
- Figure 6: Sliding window plot (1 representative series) + Kendall τ box plot (all 19)

### Section 8: Discussion (~600 words)
- E is a purpose-built filter for continuous, non-Gaussian, spatially-extended data approaching criticality
- The operators are simple (O(n), one hyperparameter ρ) — a feature, not a limitation
- Applicable domains: thermoacoustic instability, potentially neural/structural/geophysical
- Limitations: 1D only, nearest-neighbor coupling assumed, doesn't work on binary data, ties variance on this dataset
- The scaling result suggests E's advantage grows with sensor array size — relevant for high-density monitoring
- C's bounded compression is the key innovation; the linear operators (A, B, R) are standard signal processing

### Section 9: Methods (~400 words)
- Gaussian random field generation (FFT-based, Lorentzian spectrum)
- Ising sampler (Metropolis-Hastings, burn-in, thinning)
- Fisher discriminant ratio definition
- Sliding window protocol (detrending, window size, Kendall τ)
- All code available at [GitHub repo URL]

### References (~30 citations)
Key: Scheffer 2009, Dakos 2012, Bury 2020, Bury 2021, Ghanavati 2014, Maturana 2020

---

## Figures (6 total)

1. Transfer function |H_E|² + Ising S(k) overlay
2. Nonlinearity test: E vs linear filters (Gaussian + Ising)
3. EWS comparison: Fisher bars (6 indicators × 2 data types)
4. Size scaling: log-log with power-law fits
5. Robustness mechanisms: non-Gaussianity + colored noise
6. Real data: sliding window + 19-series box plot

All figures already generated in `~/software/abcre-validation/figures/`. Some will need reformatting for publication (single-column, colorblind-safe palette, consistent font sizes).

---

## Implementation Plan

### Part 1: Paper scaffold
**File:** `paper.tex` (LaTeX, J. Royal Society Interface template)
- Download JRSI template
- Set up sections, bibliography, figure placeholders
- Write abstract (~200 words)

### Part 2: Sections 1-2 (intro + operators)
- Write introduction
- Write operator definitions with equations
- Transfer function derivation
- Reformat Figure 1

### Part 3: Sections 3-5 (core results)
- Nonlinearity test writeup + Figure 2
- EWS comparison writeup + Figure 3
- Size scaling writeup + Figure 4

### Part 4: Sections 6-7 (mechanisms + real data)
- Robustness mechanisms writeup + Figure 5
- Real data validation writeup + Figure 6

### Part 5: Sections 8-9 (discussion + methods)
- Discussion (honest limitations)
- Methods
- References
- Final proofreading pass

### Part 6: Supplementary material
- All 24 orderings comparison table
- C-position grouping analysis
- ρ optimization curves
- Full 19-series Kendall τ table
- Noise sweep extended results

---

## File Structure

```
~/software/abcre-paper/
├── paper.tex           # Main manuscript
├── supplement.tex      # Supplementary material
├── references.bib      # Bibliography
├── figures/            # Publication-quality figures
│   ├── fig1_transfer_function.pdf
│   ├── fig2_nonlinearity.pdf
│   ├── fig3_ews_comparison.pdf
│   ├── fig4_scaling.pdf
│   ├── fig5_robustness.pdf
│   └── fig6_real_data.pdf
├── scripts/            # Figure-generation scripts (import from abcre-validation)
│   └── make_figures.py
└── .gitignore
```

---

## Acceptance Criteria

- T64.1: Paper compiles without errors
- T64.2: All 6 figures render correctly
- T64.3: Abstract ≤ 200 words
- T64.4: Total word count 4000-6000 (JRSI typical length)
- T64.5: Every numerical claim traceable to a specific test in abcre-validation
- T64.6: Limitations section explicitly states: ties variance on thermoacoustic, loses on binary data, 1D only
- T64.7: No overclaiming — "competitive with" not "superior to" for AC₁ comparison
- T64.8: References include all key EWS papers (Scheffer, Dakos, Bury ×2, Ghanavati)
- T64.9: Code availability statement with repo URL
- T64.10: All figures colorblind-safe

---

## Style Notes

- Write for signal processing + dynamical systems audience
- Assume reader knows Fourier analysis, bifurcation theory, basic statistics
- Don't assume reader knows ABCRE operators or their origin
- Present operators as new constructions motivated by signal processing principles
- No reference to the book, Healer, QRR, or Relational Relativity
- Honest, understated tone — let the numbers speak

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0064-abcre-paper.md

Working directory: ~/software/abcre-paper/
Six parts, one commit per part. Message format: "Plan 0064 part N: description"
Validation code is in ~/software/abcre-validation/ — import/reference but don't copy.
LaTeX paper. Generate publication-quality figures.
```
