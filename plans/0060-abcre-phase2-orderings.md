# Plan 0060: ABCRE Phase 2 — Systematic Ordering Examination

*Auditor: Argus (Session 35). Origin: Bruce requested systematic examination of all 24 orderings + Ising simulations. Phase 1 complete (15/15 tests, transfer function validated). Key Phase 1 finding: E is a bandpass filter — H_E(k,ρ) = H_B(k)·H_R(k,ρ) selectively amplifies spatial frequencies corresponding to diverging correlation length near Tc.*

*The bandpass shape of |H_E|² defines the domain-space selectivity — the "limited set of domain spaces" where E works.*

---

## Background

**Repo:** `~/software/abcre-validation/`
**Phase 1 results:** operators.py implements all 24 orderings via `ALL_ORDERINGS_4`. Transfer function H_E(k,ρ) validated against empirical FFT for small amplitudes (residual ~1e-6). Smoke test shows visually distinct output for correlated vs uncorrelated input.

**Critical insight (proved analytically, not yet in code):** In the linear regime (|x| << 1 so C(x) ≈ x), operators A, B, R are all linear. Their individual transfer functions are:
- H_A(k) = 1 for k≠0, 0 for k=0
- H_B(k) = 1 + exp(-2πik/n)
- H_R(k,ρ) = 1 + 2iρ·sin(2πk/n)

Products of scalars commute. Therefore ALL 24 orderings have the SAME transfer function H_B·H_R·H_A in the linear regime. Only C's nonlinearity (x/(1+|x|)) makes ordering matter. This means:

1. Analytical comparison of orderings is useless — they're all identical in Fourier space.
2. Ordering selection MUST be empirical, tested in the nonlinear regime (|x| ~ 1).
3. The relevant test inputs are those that produce moderate-to-large amplitudes after A→B→R, where C compresses differently depending on when it's applied.

**1D Ising note:** No phase transition at finite T. Correlation length ξ = -1/ln(tanh(J/kT)) diverges continuously as T→0. This is actually ideal — provides continuous parameter sweep rather than a sharp transition.

**Amplitude note:** Ising spins are ±1. After A (mean subtraction near 0 for disordered states) and B (neighbor sum), amplitudes reach ±2. After R, up to ±4. This means C's nonlinearity is ALWAYS active for Ising inputs — there is no linear regime for ±1 spins. This is exactly what we want: ordering differences will be real, not perturbative. Part A uses Gaussian inputs (where amplitude is controllable) to show the linear→nonlinear transition; Parts C-D use Ising inputs to test orderings in the regime that matters.

---

## Part A: Linear Equivalence Proof (analytical + numerical verification)

**File:** `linear_equivalence.py`

### A1. Analytical proof as docstring
Document the proof that all 24 orderings share transfer function H_B·H_R·H_A in the linear regime. Key steps:
1. Each of A, B, R is a linear operator (matrix multiplication on x)
2. C(x) ≈ x for |x| << 1 (identity in linear regime)
3. In Fourier space, each operator is multiplication by its transfer function
4. Scalar multiplication commutes
5. Therefore all orderings of {A, B, R} × {C ≈ I} give the same result

### A2. Numerical verification
```python
def verify_linear_equivalence(n=64, amplitude=0.001, rho=0.3):
    """Apply all 24 orderings to small-amplitude input, verify outputs match."""
    rng = np.random.default_rng(42)
    x = rng.standard_normal(n) * amplitude

    results = {}
    for name, func in ALL_ORDERINGS_4.items():
        results[name] = func(x, rho)

    # All should be nearly identical
    ref = results['ABRC']
    max_diffs = {name: np.max(np.abs(r - ref)) for name, r in results.items()}
    return max_diffs
```

**Acceptance:** All 24 pairwise max differences < 1e-8 at amplitude=0.001.

### A3. Divergence onset plot
Sweep amplitude from 0.001 to 10.0, measure max pairwise divergence across all 24 orderings. Plot amplitude vs divergence. This shows WHERE ordering starts to matter.

**Acceptance:** Clear transition from ~0 divergence to significant divergence as amplitude increases through ~0.1-1.0.

---

## Part B: 1D Ising Configuration Generator

**File:** `ising.py`

### B1. Metropolis-Hastings MCMC sampler
```python
def ising_1d(n, T, J=1.0, n_samples=100, n_burn=None, thin=None, rng=None):
    """Generate independent 1D Ising configurations at temperature T.

    Returns array of shape (n_samples, n). Each row is a ±1 spin configuration.

    Burn-in: if None, auto-scale as max(2000, 10 * n).
    Thinning: if None, auto-scale as max(n, 50). Keep every thin-th sample
    after burn-in. This ensures approximate independence — consecutive
    Metropolis samples differ by one spin flip, so autocorrelation time
    is O(n). Thinning by n gives ~independent samples.

    Total MCMC steps = n_burn + n_samples * thin.

    At low T (< 1.0), start from ordered state (all +1) to reduce
    equilibration time. At high T, start from random state.
    """
```

Parameters:
- `n`: system size (64, 128, 256)
- `T`: temperature (0.5 to 10.0; minimum 0.5 due to MCMC mixing time)
- `J`: coupling constant (default 1.0)
- `n_samples`: number of independent configurations to return (default 100)
- `n_burn`: burn-in steps; if None, auto-scaled as max(2000, 10*n)
- `thin`: thinning interval; if None, auto-scaled as max(n, 50). Ensures approximate independence between returned samples.
- Initial state: all +1 if T < 1.0, random otherwise (helps equilibration at low T)

### B2. Correlation length measurement
```python
def measure_correlation_length(configs):
    """Measure ξ from spatial autocorrelation of spin configurations.
    Fit exponential decay: C(r) ~ exp(-r/ξ).
    """
```

### B3. Verification
- At high T (T>>J): ξ ≈ 0, configurations look random
- At low T (T<<J): ξ >> n, configurations nearly uniform ±1
- Intermediate T: ξ matches analytical formula ξ = -1/ln(tanh(J/kT))

**Acceptance:** Measured ξ within 20% of analytical value for T in [0.5, 5.0].

---

## Part C: Nonlinear Ordering Comparison

**File:** `ordering_comparison.py`

### C1. Metric definitions

Four metrics to compare orderings:

1. **Variance reduction ratio:** var(ordering(x)) / var(x). Lower = more compression. Measures how much ordering reduces signal amplitude.

2. **Correlation preservation:** Absolute nearest-neighbor correlation of output: corr(ordering(x)[1:], ordering(x)[:-1]). Higher = more local structure preserved. (Use absolute value, not ratio to input — input correlation can be near zero at high T, making ratios unstable.)

3. **Spectral concentration:** Compute output power spectrum P(k) = |FFT(output)|². Measure fraction of total power in k/n ∈ [0.05, 0.25] (the empirical bandpass region). Higher = more selective filtering. Do NOT use the linear H_E to define the bandpass — the nonlinear regime may shift it.

4. **Discriminability (Fisher ratio):** For each ordering and ρ, compute the Fisher discriminant ratio between outputs at T_low=0.5 and T_high=5.0:
   ```
   F = (mean_metric_Tlow - mean_metric_Thigh)² / (var_metric_Tlow + var_metric_Thigh)
   ```
   where the metric is variance of the output (a scalar per configuration). Higher F = ordering better separates near-critical from far-from-critical configurations. E should be SELECTIVE, producing measurably different output for different ξ regimes.

### C2. Sweep parameters
- Orderings: all 24 from ALL_ORDERINGS_4
- Temperature: T ∈ {0.5, 1.0, 1.5, 2.0, 5.0, 10.0} (6 values, spanning ξ from ~30 to ~0). Minimum T=0.5 because at lower T, MCMC mixing time is O(n·exp(2J/kT)) which exceeds practical burn-in.
- ρ: {0.0, 0.1, 0.3, 0.5, 0.7, 1.0} (6 values)
- System size: n = 64 (fixed for Phase 2; size scaling is Phase 3)
- Ising samples per (T, ρ): 100 configurations, metrics averaged

### C3. Output
- `results/ordering_metrics.npz` — raw data: shape (24, 6, 6, 4) = orderings × T × ρ × metrics (metrics 1-3; metric 4 stored separately as shape (24, 6) = orderings × ρ since it compares across T)
- `figures/ordering_heatmaps.png` — 3×1 panel: one heatmap per metric, showing top-5 orderings vs (T, ρ)
- `figures/ordering_ranking.png` — bar chart: composite rank across all (T, ρ) conditions

### C4. Ordering grouping
Group the 24 orderings by C-position (1st, 2nd, 3rd, 4th in the ordering string). For each group, compute mean and std of each metric across all (T, ρ) conditions. Present as table.

Additionally: for each metric, compute average across all (T, ρ) and rank orderings. Present top-5 and bottom-5.

**Hypothesis:** Orderings will group by position of C (early vs late). C-first orderings compress before coupling; C-last orderings couple then compress. A-first (mean removal) should separate from A-elsewhere.

*Note: 24 orderings is too few for meaningful hierarchical clustering on 108 dimensions. Simple grouping by C-position is more interpretable and statistically stable.*

**Acceptance:**
- Heatmaps show clear variation across orderings (not all identical — that would mean nonlinearity doesn't matter, contradicting Part A)
- C-position groups show statistically distinct metric profiles
- ABRC (canonical) is in the top-5 for at least one metric
- If ABRC is NOT the top ordering, that's a valid finding — document which ordering wins and why (C-position, A-position, etc.). The canonical ordering was chosen by construction, not optimization.

---

## Part D: ρ Optimization

**File:** `rho_optimization.py`

### D1. For each of the top-5 orderings from Part C
Fine-grained ρ sweep: 0.0 to 2.0 in steps of 0.01. At each ρ, compute all three metrics on 100 Ising configurations at T=1.0 (moderate correlation).

### D2. Output
- `figures/rho_curves.png` — metric vs ρ for top-5 orderings
- Identify ρ* that maximizes spectral concentration for each ordering
- Print table: ordering → ρ* → metric values at ρ*

**Acceptance:** At least 3 of top-5 orderings have ρ* > 0.05 (i.e., R contributes). Curves show structure (not monotonic noise).

---

## Part E: Phase Response Analysis

**File:** `phase_analysis.py`

### E1. Phase of H_E
Plot arg(H_E(k, ρ)) for several ρ values. The phase response shows how the operator shifts different frequencies — this is the "circulation" effect of R.

### E2. Group delay
τ(k) = -d(arg(H_E))/dk. Compute numerically. Flat group delay = undistorted signal; varying group delay = dispersion.

*Note: Phase response and group delay are linear-regime concepts. They describe what E does when C ≈ identity. Parts C-D test whether the linear predictions hold in the nonlinear regime.*

### E3. Efficiency region
The "limited set of domain spaces" where E efficiently performs FFA are spatial frequencies where:
1. |H_E|² is large (bandpass gain)
2. Group delay is approximately flat (minimal dispersion)
3. Input power spectrum has significant energy (ξ-dependent)

**Operational definition of "efficient FFA":** E efficiently performs FFA at temperature T if the spectral concentration of E(x) exceeds that of x — i.e., E concentrates energy into fewer modes than the input. Concentration ratio = spectral_concentration(E(x)) / spectral_concentration(x) > 1.

Plot the "efficiency region" in (k, ρ) space as a 2D colormap. For each (k, ρ) point, compute the product of three normalized scores (each in [0,1]):
- Gain score: |H_E(k,ρ)|² / max_k(|H_E(k,ρ)|²)
- Flatness score: 1 - |τ(k) - median(τ)| / max_k(|τ(k) - median(τ)|) where τ is group delay
- (Input power is ξ-dependent — overlay contours for ξ = 2, 5, 20)

The efficiency region emerges visually where the colormap is bright AND input power contours are high. No arbitrary thresholds needed.

Cross-validate: compare Part E's linear predictions with Part C's empirical results. Do the top orderings from Part C (especially by discriminability metric) have their power concentrated in Part E's predicted efficiency region?

**Acceptance:** Efficiency region is a well-defined band, not the entire (k, ρ) plane. Cross-validation with Part C shows qualitative agreement (orderings that concentrate power empirically do so in the predicted frequency band).

---

## Implementation Notes

- Add `scipy` to `requirements.txt` (needed for curve_fit in B2)
- All files import from existing `operators.py` (no duplication)
- Each Part is a separate .py file with `if __name__ == '__main__'` block
- All figures saved to `figures/`
- All numerical results saved to `results/`
- Tests go in `tests/test_phase2.py`
- One commit per Part (A through E)

## Test Cases for `tests/test_phase2.py`

- T2.1: Linear equivalence — all 24 orderings match within 1e-8 for small amplitude
- T2.2: Ising sampler — high-T configs have mean magnetization near 0
- T2.3: Ising sampler — low-T configs have |mean magnetization| near 1
- T2.4: Correlation length — measured ξ within 20% of analytical for T=1.0
- T2.5: Ordering metrics — variance reduction ratio ∈ (0, 1) for all orderings
- T2.6: Ordering metrics — spectral concentration ∈ (0, 1) for all orderings
- T2.7: Nonlinear divergence — orderings differ by > 0.01 for amplitude=1.0
- T2.8: Discriminability — Fisher ratio > 0 for at least 20 of 24 orderings at ρ=0.3 (E should distinguish T=0.5 from T=5.0)
- T2.9: ρ optimization — ρ* is not at sweep boundary for at least 3 of top-5
- T2.10: Group delay — computed without NaN for k ∈ (0, 0.5)
- T2.11: Efficiency region — non-empty for ρ=0.3

---

## Execution Order

Parts A and B are independent — can run in parallel.
Part C depends on B (needs Ising configs).
Part D depends on C (needs top-5 orderings).
Part E depends on A (needs transfer function, but not Ising).

```
A ──────────────── E
B ──── C ──── D
```

Suggested: A first (validates the key insight), B+E in parallel, then C, then D.

---

## Idempotency Statement

A second Generator given this plan, the existing `operators.py`, and numpy/scipy/matplotlib would produce equivalent code. Metric definitions are fully specified. Ising sampler is standard Metropolis-Hastings. Only plot aesthetics may vary.

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0060-abcre-phase2-orderings.md

Working directory: ~/software/abcre-validation/
Five parts (A-E), each a separate .py file. One commit per part.
Message format: "Plan 0060 part X: description"
Run tests after each part. All existing tests must continue to pass.
```
