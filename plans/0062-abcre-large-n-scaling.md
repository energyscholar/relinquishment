# Plan 0062: ABCRE Large-n Scaling Test

*Auditor: Argus (Session 35). Origin: Phase 3 Part C showed E-var Fisher ~ n^1.13 vs raw variance ~ n^0.50 on Gaussian fields (n=32-512, R²=0.993). Bruce requested extension to n≈8192 to verify or falsify the power law.*

---

## Background

**Repo:** `~/software/abcre-validation/`
**Existing code:** `size_scaling.py` tests n=[32,64,128,256,512] on both Ising and Gaussian.
**Key result:** Gaussian scaling: E-var α=1.13 [0.96, 1.29], R²=0.993. Raw variance α=0.50 [0.41, 0.60].
**Ising result:** Flat (α≈0, R²<0.15). Binary data doesn't benefit from larger n. **Skip Ising entirely.**

## What This Tests

Does the n^1.13 scaling hold, flatten, or steepen at large n? The answer determines whether E's advantage over raw variance is:
- Structural and growing (α holds) → publishable asymptotic claim
- Bounded (α drops) → practical ceiling identified
- Accelerating (α increases) → stronger-than-expected result

## Implementation

**File:** `large_n_scaling.py` (new file, imports from existing modules)

### Step 1: Extended Gaussian scaling

```python
SIZES = [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
```

For each n, generate 200 Gaussian random fields at ξ_high=50 and ξ_low=2. Compute Fisher ratio for each indicator. Recompute all sizes (don't try to reuse cached results — clean run, single seed, ~2 minutes total).

Indicators (same as Part C, drop Ising-specific ones):
- E-var (BCAR)
- E-var (ABRC)
- Raw variance
- AC₁
- Spectral β

### Step 2: Robustness — multiple ξ pairs

Test three ξ pairs to verify the scaling isn't an artifact of ξ=50 vs ξ=2:
- (ξ_high=50, ξ_low=2) — original
- (ξ_high=20, ξ_low=2) — smaller contrast
- (ξ_high=50, ξ_low=5) — higher baseline

For each pair, compute Fisher at all 9 sizes. Fit power law. Report α and R².

### Step 3: Multi-seed stability

Run the primary (ξ=50 vs ξ=2) test across seeds 0-4. Report mean ± std of α for each indicator. This verifies the power-law exponent isn't seed-dependent.

### Step 4: Breakpoint detection

Fit power law on sliding 5-point windows: [32-512], [64-1024], ..., [512-8192]. If α changes significantly across windows, the power law is breaking. Report α per window.

### Output

- `figures/large_n_scaling.png` — 2×2 panel:
  - Top-left: log-log Fisher vs n (all indicators, primary ξ pair, full range)
  - Top-right: α vs ξ pair (bar chart, 3 pairs × 5 indicators)
  - Bottom-left: α stability across 5 seeds (error bars)
  - Bottom-right: sliding-window α (breakpoint detection)
- Print summary table: indicator → α → 95% CI → R² → verdict (holds/flattens/steepens)

### Acceptance Criteria

- T62.1: All 9 sizes compute without error or NaN
- T62.2: R² > 0.95 for E-var power-law fit on full range (if power law holds)
- T62.3: If R² drops below 0.90, report breakpoint (which n range α changes)
- T62.4: α consistent across 3 ξ pairs (within 0.2 of each other)
- T62.5: α consistent across 5 seeds (std < 0.15)
- T62.6: E-var α > raw variance α on all 3 ξ pairs (E scales faster)
- T62.7: Runtime < 10 minutes total

### Possible Outcomes

1. **α holds (1.0-1.3 across all tests):** Power law is real. E's advantage is structural. Publishable.
2. **α flattens to ~0.7-0.9 at large n:** Partial saturation. E still beats variance but advantage plateaus.
3. **α drops to ~0.5 at large n:** Full saturation. E converges to variance-like scaling. The nonlinear advantage is bounded.
4. **α increases (>1.3 at large n):** Superlinear acceleration. Strongest possible result.
5. **Inconsistent across ξ pairs or seeds:** The scaling exponent isn't robust. Report as such.

---

## Computational Notes

- Gaussian field generation: O(n log n) per sample via FFT. At n=8192, 200 samples = trivial.
- BCAR application: O(n) per sample. Trivial.
- Total: 9 sizes × 200 samples × 2 conditions × 5 indicators ≈ 18,000 FFTs + operator applications. Under 2 minutes.
- Multi-seed (5 seeds): 5× = under 10 minutes total.
- Memory: 200 × 8192 × 8 bytes = 13 MB per condition. Fine.

## Tests for `tests/test_large_n.py`

- T62.1: `compute_extended_scaling()` returns dict with 9 Fisher values per indicator, no NaN
- T62.2: E-var α > 0.9 on primary ξ pair (Phase 3 CI was [0.96, 1.29])
- T62.3: Raw variance α < E-var α (E scales faster)
- T62.4: All 3 ξ pairs produce E-var α > raw variance α
- T62.5: Multi-seed std of E-var α < 0.15

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0062-abcre-large-n-scaling.md

Working directory: ~/software/abcre-validation/
One new file: large_n_scaling.py. One test file: tests/test_large_n.py.
One commit. Message: "Plan 0062: large-n scaling test (n=32-8192)"
Run tests after implementation. All existing tests must continue to pass.
```
