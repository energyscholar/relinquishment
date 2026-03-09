# Plan 0061: ABCRE Phase 3 — Practical Validation

*Auditor: Argus (Session 35). Origin: Phase 2 showed E is a nonlinear bandpass filter matched to critical fluctuations. Phase 3 answers: does it matter? Four tests: (A) does C's nonlinearity help vs a linear filter, (B) does E outperform established EWS indicators, (C) does discriminability scale with system size, (D) does E detect known transitions in real/realistic data.*

*If A and B both come back negative, the operators are an intellectual curiosity. If either is positive, there's a tool worth developing. D provides ground truth validation.*

---

## Background

**Phase 2 results (Plan 0060):**
- E = C(R(B(A(x)))) is a nonlinear bandpass filter. |H_E|² peaks at low-to-mid spatial frequencies.
- C-last orderings have 2× Fisher discriminability (225.8 vs 113.8). Best composite: BCAR, BCRA.
- ρ monotonically increases spectral concentration (no interior optimum).
- Efficiency region (high gain × flat group delay) overlaps Ising S(k) for large ξ.
- All 24 orderings identical in linear regime. Only C's nonlinearity differentiates.

**The open question:** Phase 2 showed E *can* distinguish correlation regimes on synthetic Ising data. Phase 3 tests whether E does this *better* than simpler methods, and whether C's nonlinearity is the reason.

**Repo:** `~/software/abcre-validation/`
**Primary ordering:** BCAR (Phase 2 top composite, C-last). Run ABRC (canonical) as secondary comparison in all parts.

**Critical design note:** Phase 2 used ±1 Ising spins exclusively. On binary data, raw variance = 1 - m² is a sufficient statistic for the order parameter — no filter can beat it. This biases comparisons against E. Phase 3 uses TWO data sources:

1. **Ising (binary ±1):** Retained for continuity with Phase 2. Raw statistics have an inherent advantage here.
2. **Gaussian random fields (continuous):** Generated with tunable correlation length ξ. Same correlation physics as Ising, but continuous values where raw variance is NOT a sufficient statistic. More representative of real-world data.

**Fisher information caveat:** For the Lorentzian spectrum P(k) = 1/(k² + 1/ξ²), the optimal linear discriminant weight w_opt(k) ∝ (dP/dξ)/P² = 2ξ⁻³ — constant across frequencies. This means raw variance (equal weighting) IS the optimal linear estimator for ξ. E's bandpass weighting is provably suboptimal in the linear regime. E can only win via C's nonlinear compression effects. If E loses on Gaussian fields, that's consistent with this analysis — and it would explain why raw variance is such a robust EWS indicator in practice.

**Kernel note:** E is defined as ABRC (canonical composition, per kernel). BCAR is a research variant tested for comparison — not a redefinition of E. operator_e() in operators.py remains ABRC.

---

## Shared Utility: Gaussian Random Field Generator

**Add to `ising.py`** (keep filename — renaming breaks Phase 1+2 imports):

```python
def correlated_gaussian_field(n, xi, n_samples=200, rng=None):
    """1D Gaussian random field with correlation length xi.

    Power spectrum: P(k) ~ 1/(k² + 1/xi²), DC removed.
    Generated via spectral method: white noise → FFT → shape → IFFT.
    Returns array of shape (n_samples, n) with continuous real values.

    Unlike Ising, raw variance here is NOT a sufficient statistic.
    E's bandpass filtering can potentially extract information that
    raw variance misses.
    """
    white = rng.standard_normal((n_samples, n))
    W = np.fft.fft(white, axis=-1)
    k = np.fft.fftfreq(n, d=1.0)
    P = 1.0 / ((2 * np.pi * k)**2 + 1.0 / xi**2)
    P[0] = 0  # kill DC (same as operator A)
    shaped = W * np.sqrt(P)
    return np.fft.ifft(shaped, axis=-1).real
```

**ξ values mapping to Ising temperatures:**
- ξ = 1 (uncorrelated, like T → ∞)
- ξ = 2, 5, 10, 20, 50 (increasing correlation)
- For Fisher ratio: compare ξ=2 ("high T") vs ξ=50 ("low T", near critical)

---

## Part A: Does C's Nonlinearity Help?

**File:** `nonlinearity_test.py`

This is the critical test. If a linear filter matches E's performance, C is cosmetic.

### A1. Three filters to compare

1. **E (nonlinear):** BCAR(x, ρ) via `ALL_ORDERINGS_4['BCAR']`. C applied elementwise in position 2.

2. **Linear-exact (BAR):** Compose B, A, R without C. Since A, B, R are all linear, this applies the same frequency response as BCAR's linear regime, but without C's compression. Output is unbounded.
   ```python
   def linear_exact(x, rho):
       return operator_r(operator_a(operator_b(x)), rho)
   ```

3. **Linear-magnitude (zero-phase):** Apply |H_BAR(k)| in Fourier space with zero phase. Tests whether phase response matters.
   ```python
   def linear_magnitude(x, rho):
       X = np.fft.fft(x, axis=-1)
       k_norm = np.fft.fftfreq(x.shape[-1])
       H = transfer_function_H(k_norm, rho)  # from transfer_function.py
       H[..., 0] = 0  # DC kill
       return np.fft.ifft(X * np.abs(H), axis=-1).real
   ```

### A2. Discriminant scalar

For each config and each filter: compute **var(output)**. This is the scalar fed to the Fisher ratio, matching Phase 2's metric.

Fisher ratio: F = (mean_var_group1 - mean_var_group2)² / (std_var_group1² + std_var_group2²)

### A3. Test conditions

**On Ising data:**
- T_low=0.5, T_high=5.0, n=64, ρ ∈ {0.3, 0.7}
- 200 configs per temperature, 10 RNG seeds (seeds 0-9) → mean ± std of Fisher

**On Gaussian random fields:**
- ξ_high=50 ("near critical"), ξ_low=2 ("far from critical"), n=64, ρ ∈ {0.3, 0.7}
- 200 fields per ξ, 10 RNG seeds → mean ± std of Fisher

**Robustness tests (on Gaussian fields only — noise on binary data is a different problem):**
- **Additive noise:** Add N(0, σ²) with σ ∈ {0.1, 0.5, 1.0, 2.0} to fields before filtering
- **Amplitude outliers:** Replace 5% of values with draws from N(0, 10)

### A4. Output

- `figures/nonlinearity_comparison.png` — 2×3 panel:
  - Row 1: Ising. Row 2: Gaussian fields.
  - Col 1: Fisher ratio (3 filters × 2 ρ) on clean data
  - Col 2: Fisher ratio vs noise level σ (Gaussian only; Ising shows clean comparison)
  - Col 3: Example outputs of all 3 filters on same input

- `results/nonlinearity_test.npz` — all Fisher ratios, noise sweep data

### A5. Acceptance criteria

**On Gaussian fields (the fair test):**
- E's Fisher ratio exceeds linear-exact by > 20% on clean data OR > 50% on noisy data → **C helps**
- E matches linear-exact within 10% on all conditions → **C is cosmetic**
- Linear-magnitude significantly underperforms linear-exact → **phase matters**

**On Ising (expected: linear-exact matches E because raw stats are sufficient):**
- Document result. If E wins even on binary data, that's a stronger finding.

---

## Part B: Head-to-Head Against EWS Indicators

**File:** `ews_comparison.py`

**Note:** This tests *spatial* discriminability — can each indicator distinguish correlation regimes from single spatial snapshots? Part D below tests *temporal* EWS detection (sliding windows on time series approaching known transitions).

### B1. Indicators to compare

All computed on single spatial snapshots:

1. **E-variance (BCAR):** var(BCAR(x, ρ=0.3))
2. **E-variance (ABRC):** var(ABRC(x, ρ=0.3)) — canonical ordering comparison
3. **E-concentration:** Spectral concentration of BCAR output (power fraction in k/n ∈ [0.05, 0.25])
4. **Raw variance:** var(x)
5. **Lag-1 autocorrelation (AC₁):** corr(x[:-1], x[1:])
6. **Spectral exponent β:** Linear regression of log(P(k)) vs log(k) over k/n ∈ [0.02, 0.45]
7. **DFA exponent α:** (Optional, n ≥ 256 only.) Detrended fluctuation analysis. Box sizes from 4 to n/4. If n < 256, skip — too few scaling points for reliable exponent.

### B2. Test protocol

**On Ising:** T ∈ {0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0}, n=64, 200 configs per T.

**On Gaussian fields:** ξ ∈ {1, 2, 5, 10, 20, 50}, n=64, 200 fields per ξ.

For each dataset, compute:
- **Fisher ratio:** F(low vs high) for each indicator. Ising: T=0.5 vs T=5.0. Gaussian: ξ=50 vs ξ=2.
- **Monotonicity:** Spearman rank correlation between indicator mean and control parameter (T or ξ). A good detector is monotonic.
- **Coefficient of variation:** std(indicator) / |mean(indicator)| at each condition. Lower = more reliable per-sample.

### B3. Output

- `figures/ews_comparison_ising.png` — 3-panel: indicators vs T, Fisher bar chart, monotonicity bar chart
- `figures/ews_comparison_gaussian.png` — same layout for Gaussian fields
- `figures/ews_sensitivity.png` — d(indicator)/d(control parameter) for both datasets. Shows WHERE each indicator is most sensitive.
- `results/ews_comparison.npz` — all data

### B4. Acceptance criteria

**On Gaussian fields (primary):**
- E-variance has higher Fisher ratio than raw variance → E adds value
- E-variance monotonicity > 0.9 (Spearman) → reliable ordering
- At least one E indicator in top 3 → E is competitive
- If raw variance or AC₁ beats all E indicators → E is not useful (honest result)

**On Ising (secondary — expected: raw stats win):**
- Document results. E winning on binary data would be surprising and significant.

---

## Part C: Size Scaling

**File:** `size_scaling.py`

### C1. Parameters

- n ∈ {32, 64, 128, 256, 512}
- **Ising:** T ∈ {0.5, 1.0, 2.0, 5.0}
- **Gaussian:** ξ ∈ {2, 10, 20, 50}
- ρ = 0.3
- 200 configs/fields per (n, condition)
- Indicators: E-variance (BCAR), E-variance (ABRC), raw variance, AC₁, spectral exponent β

### C2. Scaling analysis

For each indicator and dataset, compute Fisher ratio (low vs high condition) at each n.

Plot F(n) for each indicator. Fit power law: F ~ n^α (log-log linear regression, report α ± 95% CI).

- α_E > α_variance → E has better scaling (advantage grows with system size)
- α_E ≈ α_variance → no structural scaling advantage
- α_E < α_variance → E is worse at scale

Also: minimum n where F > 10 for each indicator (practical threshold for reliable discrimination).

### C3. Output

- `figures/size_scaling_ising.png` — Fisher ratio vs n (log-log), power-law fits
- `figures/size_scaling_gaussian.png` — same for Gaussian fields
- `results/size_scaling.npz` — all data, fit parameters

### C4. Acceptance criteria

- Fisher increases with n for all indicators (sanity)
- Power-law exponents reported with 95% CI
- Clear statement per dataset: "E scales [better/same/worse] than variance"

---

## Part D: Real Data Validation

**File:** `real_data_test.py`

Parts A-C use synthetic data with exact ground truth. Part D tests E on time series with known transitions, using standard sliding-window EWS methodology.

**Key adaptation:** E was validated on spatial snapshots. For time series, treat each sliding window as a 1D spatial array. "Nearest neighbor" in B and R becomes "adjacent time points." Temporal autocorrelation maps to spatial nearest-neighbor correlation. The physics is identical.

### D0. Pre-condition: data must be in place before Generator runs

All datasets must be downloaded, format-verified, and integrity-tested by the Auditor BEFORE handoff. The Generator reads from `data/` — it does not download or debug data formats.

Verification checklist (Auditor completes before handoff):
- [ ] `data/ricker_simulation.csv` — generated and verified (or Ricker model code tested)
- [ ] `data/thermoacoustic.csv` — downloaded, columns identified, no NaN, expected size
- [ ] `data/gisp2.csv` (optional) — downloaded, interpolated to regular spacing, transition region identified
- [ ] Each dataset has a companion `data/README_datasets.txt` with column descriptions, source URLs, transition indices

### D1. Datasets (3 sources, increasing complexity)

**Dataset 1: ewstools Ricker model (synthetic control)**
- Source: `ewstools.models.simulate_ricker()` — already installed at `~/repos/ewstools/`
- Type: fold bifurcation (population collapse via harvesting)
- Size: ~500 time steps
- Ground truth: known bifurcation point
- Access: `import ewstools` or copy the model function (3 lines of code: x_{t+1} = x_t * exp(r*(1 - x_t/K)) + harvest + noise)
- **Implementation note:** If ewstools import fails, implement the Ricker model directly:
  ```python
  def simulate_ricker(r=0.75, K=10, h_values=np.linspace(0, 0.75, 500),
                      sigma=0.02, x0=None, rng=None):
      """Ricker model with linearly increasing harvest rate.
      x_{t+1} = x_t * exp(r * (1 - x_t/K)) - h_t + sigma * noise
      Clamp x to max(x, 0) — population can't go negative.
      Fold bifurcation when h approaches critical value.
      """
  ```

**Dataset 2: Thermoacoustic Rijke tube (real, engineering)**
- Source: Bury et al. (2021) PNAS GitHub repo
- URL: `https://github.com/ThomasMBury/deep-early-warnings-pnas`
- File: `test_empirical/data/thermoacoustic.csv` (or similar path in repo)
- Type: subcritical Hopf bifurcation (transition to oscillatory combustion instability)
- Size: ~tens of thousands of pressure measurements
- Ground truth: known transition point from experimental setup
- **Access protocol:** Download CSV to `data/thermoacoustic.csv` in repo. Inspect CSV format and adapt column selection as needed. If download fails or format is unclear, skip with warning and document why — don't block the rest of Phase 3.

**Dataset 3: GISP2 Younger Dryas (real, paleoclimate) — OPTIONAL**
- Source: NOAA NCEI Paleoclimatology
- URL: `https://www.ncei.noaa.gov/access/paleo-search/study/2475`
- Type: abrupt warming (~11,700 yr b2k), canonical EWS benchmark (Dakos 2008)
- Size: ~1500 data points over ~100Kyr
- Complication: irregularly spaced → needs interpolation
- **If data prep exceeds 50 lines of code, skip.** This is a stretch goal. The Ricker and thermoacoustic datasets are sufficient for Phase 3.

### D2. Sliding window protocol

For each dataset:

1. **Identify pre-transition region:** manually specify start and end indices (or timestamps). The transition point is known for all datasets.

2. **Detrend:** Remove linear or Gaussian-kernel trend from pre-transition data. Standard EWS preprocessing. Bandwidth = 50% of series length (Dakos convention).

3. **Sliding window:** Window size = 25% of pre-transition length. Step size = 1. For each window position:
   - Compute E-variance: var(BCAR(window, ρ=0.3))
   - Compute E-variance (ABRC): var(ABRC(window, ρ=0.3))
   - Compute raw variance: var(window)
   - Compute AC₁: corr(window[:-1], window[1:])
   - Compute spectral exponent β: linear regression of log(P(k)) vs log(k)

4. **Trend test:** For each indicator, compute Kendall τ correlation with time index over the pre-transition region. τ > 0 means increasing trend (expected for CSD). Higher |τ| = stronger trend = better early warning.

### D3. Output

- `figures/real_data_ricker.png` — 2-panel:
  - Top: time series with transition point marked
  - Bottom: all indicators vs time (sliding window), Kendall τ annotated per indicator

- `figures/real_data_thermoacoustic.png` — same layout

- `figures/real_data_gisp2.png` — same layout (if GISP2 attempted)

- `figures/real_data_summary.png` — bar chart: Kendall τ per indicator across all datasets. Shows which indicator detects the approaching transition most reliably.

- `results/real_data_test.npz` — all indicator time series, Kendall τ values

### D4. Acceptance criteria

- Ricker model: all indicators show positive Kendall τ (CSD detected). This is a control — if indicators fail here, the implementation is wrong.
- Thermoacoustic: E-variance Kendall τ > 0 (E detects the approaching instability)
- E-variance Kendall τ ≥ variance Kendall τ on at least one dataset → E adds value on real data
- If variance and AC₁ consistently beat E-variance → E doesn't translate to practical use (honest result)
- GISP2 (if attempted): any positive Kendall τ from E is a bonus

---

## Implementation Notes

- Add `scipy` to `requirements.txt` (curve fitting, detrending)
- Add `correlated_gaussian_field()` to `ising.py` (keep filename — renaming breaks Phase 1+2 imports)
- Create `data/` directory for downloaded real datasets (add `data/` to `.gitignore` if datasets are large)
- All files import from `operators.py`, `ising.py`, `transfer_function.py`
- BCAR primary, ABRC secondary — both run in Parts B, C, D
- Tests in `tests/test_phase3.py`
- One commit per Part (A, B, C, D)
- Figures to `figures/`, results to `results/`

## Test Cases for `tests/test_phase3.py`

- T3.1: Linear-exact (BAR) produces output with max |value| > 1 on Ising data — confirms C bounds
- T3.2: Linear-magnitude filter output has correct power spectrum shape (matches |H_BAR|² within 10% at sampled frequencies)
- T3.3: Gaussian field at ξ=10, n=64 has measured autocorrelation length within 30% of 10 (fit exp decay to C(r)). Note: ξ >> n/4 will show finite-size effects — that's physics, not a bug.
- T3.4: Gaussian field at ξ=50 has higher AC₁ than at ξ=2
- T3.5: All indicators computed without error for n=64 on both data types
- T3.6: Raw variance on Ising increases with decreasing T
- T3.7: AC₁ on Ising increases with decreasing T
- T3.8: E-variance differs from raw variance (E is not a no-op)
- T3.9: Fisher ratio > 0 for all indicators on Gaussian fields
- T3.10: Size scaling — Fisher at n=256 > Fisher at n=32 for E-variance on Gaussian data
- T3.11: Ricker model simulation runs without error and produces ~500 time points
- T3.12: Sliding window on Ricker produces indicator time series with no NaN values
- T3.13: Kendall τ for raw variance on Ricker is positive (CSD detected — sanity check)

---

## Execution Order

A first (answers the most fundamental question). Then B, then C, then D.

```
A (nonlinearity) → B (EWS comparison) → C (scaling) → D (real data)
```

If Part A shows C is cosmetic, Parts B-D still run — the story changes from "nonlinear filter" to "this bandpass shape," but the comparison is still valuable.

Part D depends on B's indicator computation functions. Generator should reuse/import indicator functions from `ews_comparison.py` rather than reimplementing.

Shared data generation: implement `correlated_gaussian_field()` in Part A's commit. Parts B and C import it.

---

## Possible Outcomes and Implications

**Outcome 1: C helps, E beats EWS on Gaussian fields.** The operators are a genuinely novel criticality detector. C's nonlinear compression provides advantage on continuous data. Worth developing.

**Outcome 2: C helps on noisy data only, E matches EWS on clean data.** C provides robustness (noise rejection) but not superior discrimination. E is an alternative for noisy/nonstationary settings, not a replacement.

**Outcome 3: C is cosmetic, bandpass shape beats EWS.** The value is in A+B+R's spectral properties. You could replace E with a tuned linear bandpass and get the same result. Still useful — the operator composition naturally produces a good criticality filter shape.

**Outcome 4: C is cosmetic, E matches or loses to EWS.** The operators add no practical value for criticality detection on either data type. Variance and AC₁ capture the same information. Honest result — the operators are a mathematical curiosity, not a tool.

**Outcome 5 (bonus): E wins on Ising too.** Would mean C's nonlinearity helps even on binary data where raw stats should be sufficient. Surprising and publishable.

**Part D cross-reference:** Real data results may match or diverge from synthetic findings. If E wins on Gaussian fields (Outcome 1/3) AND shows strong Kendall τ on real data, that's convergent evidence. If E wins synthetic but fails real, the synthetic setup is too clean. If E fails synthetic but shows signal on real, something unexpected is happening.

All outcomes are valid. The plan distinguishes between them.

---

## Idempotency Statement

All metrics, data generation, test conditions, and acceptance criteria are fully specified. Discriminant scalar = var(output), matching Phase 2. RNG seeds: 42 for primary runs, 0-9 for repeats. Gaussian field generation via spectral method is deterministic given seed. A second Generator produces equivalent code.

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0061-abcre-phase3-validation.md

Working directory: ~/software/abcre-validation/
Four parts (A-D), each a separate .py file. One commit per part.
Message format: "Plan 0061 part X: description"
Run tests after each part. All existing Phase 1+2 tests must continue to pass.
Also read: operators.py, ising.py, transfer_function.py (existing code to build on).
Part D imports indicator functions from Part B's ews_comparison.py.
For thermoacoustic data: download CSV to data/ directory, skip gracefully if unavailable.
```
