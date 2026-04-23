# Plan 0060: ABCRE Validation Framework

**Status:** DRAFT v4 — Deeper questions: Fourier analysis, visual evolution, ρ-as-subject
**Project:** `~/software/abcre-validation/` (local git repo)
**Reference:** `~/software/Invariant_Relational_Kernel_ABRCE/operators.rs` (canonical spec)
**Scope:** Systematic empirical validation of ABCRE operators as critical transition detectors
**Idempotency:** A second Generator given only this plan would produce the same code.

---

## 0. What We're Testing and Why

The ABCRE operators define a fixed signal-processing pipeline:

```
E(x, ρ) = C(R(B(A(x)), ρ))

A(x)[i] = x[i] - mean(x)          # mean-centering
B(x)[i] = x[i] + x[(i+1) mod n]   # neighbor coupling
R(x,ρ)[i] = x[i] + ρ·(x[i+1] - x[i-1])  # circulation
C(x)[i] = x[i] / (1 + |x[i]|)     # soft saturation
```

### The five questions (in order of depth)

**Q0: What does E do to a signal, mathematically?**
Before any simulation, understand the operator chain analytically. In Fourier
space (for small amplitudes where C ≈ identity): A kills the DC component
(k=0). B multiplies each mode by (1 + e^{-2πik/n}) — a low-pass filter with
nulls. R adds ρ times a pure imaginary term i·sin(2πk/n) — a phase shift,
which IS circulation in frequency space. We can compute E's transfer function
H(k, ρ) exactly in the linear regime. If H's passband overlaps with the range
where the Ising correlation function C(k) ~ 1/(k² + ξ⁻²) changes most near
Tc, then ABCRE detects Tc FOR MATHEMATICAL REASONS and simulations just
confirm. If not, we know in advance it won't work, and we know why.

**Q1: What structures persist under iterated E?**
Rather than "does it detect Tc" (a goal-directed frame the kernel's philosophy
rejects), ask: what does the operator chain PRESERVE? Feed it configurations
at different T. Iterate E. What survives? If the structures that persist are
correlated with proximity to criticality, that's a detection mechanism — but
discovered through observation, not imposed through a detection frame.

**Q2: Does ρ encode information about the input?**
The ρ at which iterated E transitions from convergent to non-convergent is
unique to ABCRE — no other method has a tunable parameter with this property.
If ρ_critical(input) varies systematically with system properties (temperature,
proximity to bifurcation), then ρ IS the detection mechanism. This reframes
ABCRE from "a tool for detecting transitions in the system" to "a system
that itself undergoes transitions, and the transition point encodes information
about the input." This is the most novel potential finding.

**Q3: Does E(x,ρ) produce observable signatures at known critical points?**
The standard detection question. Apply E to Ising configurations at various T.
Do scalar statistics (variance, correlation length ratio) peak near Tc?
Does the signal scale with system size?

**Q4: Is the composition A→B→R→C special?**
Among all orderings and subsets, does the canonical chain produce richer
dynamics, better detection, or unique behavior? Does removing R (the only
antisymmetric operator) collapse the dynamics, as the canonical spec claims?

### What changes our minds

- E's Fourier transfer function has structure that selectively amplifies
  modes near the correlation length scale (Q0 positive)
- Iterated E preserves spatial structure that correlates with T (Q1 positive)
- ρ_critical encodes proximity to phase transition (Q2 positive)
- I1 or I6 peaks at Tc and scales with L (Q3 positive)
- A→B→R→C is empirically special among orderings (Q4 positive)

### What a negative result looks like

- Transfer function is essentially flat — E is a uniform smoother (Q0 negative)
- Iterated E erases all input-dependent structure within ~5 iterations (Q1 neg.)
- ρ_critical is input-independent (Q2 negative)
- No indicator peaks at Tc, or signal is weaker than raw spatial variance (Q3 neg.)
- Many orderings work equally well (Q4 negative)

**Both outcomes are publishable and valuable.** A negative result with clear
analytical explanation (Q0) is more valuable than a positive result without one.

### Exploration-First Principle

We do NOT build a framework and then run experiments. We run the simplest
possible experiment first, LOOK at the output, then build infrastructure
only as warranted by what we see. Each phase produces a visible result
(a plot, a number, a yes/no) before the next phase begins.

Sampling starts sparse (5 temperatures, 10 ρ values, 30 samples) and
increases only after code is debugged and results are directional. Dense
sampling is for publication, not exploration.

---

## 1. Project Structure

Start flat. No package structure. Refactor into packages in Phase 6+ if
the project grows enough to need it.

```
abcre-validation/
├── requirements.txt              # Phase 1
├── operators.py                  # Phase 1
├── ising.py                      # Phase 2
├── explore.py                    # Phase 1-2 (the main exploration script)
├── indicators.py                 # Phase 3 (when we need more than I1)
├── classical.py                  # Phase 3 (magnetization, susceptibility)
├── experiment.py                 # Phase 5 (config-driven runner)
├── analysis.py                   # Phase 5
├── tests/
│   ├── test_operators.py         # Phase 1
│   ├── test_ising.py             # Phase 2
│   └── test_indicators.py        # Phase 3
├── configs/                      # Phase 5+
├── results/                      # .gitignored
├── figures/                      # Generated plots, git-tracked
└── .gitignore
```

### Design philosophy

- **No abstract base classes.** Plain classes, plain functions.
  If polymorphism becomes needed, add it then.
- **No YAML configs until Phase 5.** Parameters are constants at the top
  of each script. Copy-paste to change. This is faster to debug and read.
- **No Numba until Phase 5.** Pure NumPy is fast enough through L=64.
  Numba adds compilation delay and debugging complexity. Add it when
  profiling shows it's needed.
- **Tests exist from Phase 1** but are simple pytest functions, not a
  test framework. Test what matters: operator correctness, not infrastructure.

### Dependencies (requirements.txt)

```
numpy>=1.24
scipy>=1.10
matplotlib>=3.7
pytest>=7.0
```

That's it. Add numba, pyyaml, h5py WHEN NEEDED (Phase 5+).

### Git setup (Phase 1)

```bash
cd ~/software
mkdir abcre-validation && cd abcre-validation
git init
# Initial commit: requirements.txt, .gitignore, operators.py, tests/
```

`.gitignore`:
```
results/
__pycache__/
*.pyc
.pytest_cache/
```

---

## 2. ABCRE Indicators — What Numbers We Extract

### Critical design constraint: C is a contraction

C maps everything to (-1,1). After 2-3 iterations of E, the output is
dominated by the operator chain's dynamics, not the input configuration.
**All useful information is in the transient (first 1-10 iterations), not
the asymptote.** Indicator design accounts for this.

Iterated E can never "diverge" — C bounds all outputs. The meaningful
transition is convergent (fixed point) vs non-convergent (oscillatory/chaotic
within (-1,1)).

### Batch processing requirement (CRITICAL for performance)

ALL operators MUST process 2D arrays where axis=-1 is the spatial dimension
(length L) and axis=0 is the batch dimension (all rows of the lattice).
Use `np.mean(x, axis=-1, keepdims=True)` for A, `np.roll(x, -1, axis=-1)`
for B, etc. A Python loop over rows is unacceptable — it introduces a 256×
overhead for L=256.

### Indicator introduction schedule (maps to questions)

**Phase 1 (analytical):** Transfer function H(k,ρ). Answers Q0 before any
simulation. No configurations needed — just math + FFT.

**Phase 2 (visual exploration):** Spatiotemporal heatmaps + I1. Answers Q1
visually. I1 is one line — compute it alongside the heatmaps.

**Phase 3 (ρ as subject):** I3 (ρ-convergence). Answers Q2 — the most novel
potential finding. Also I1 with more temperatures for Q3.

**Phase 4 (physical mechanism):** I6 (correlation length ratio). Explains
WHY ABCRE sees or doesn't see Tc. Connects to transfer function from Phase 1.

**Phase 5+ (scaling/publication):** I2, I4, I5 if warranted.

### H(k,ρ): Transfer function (Phase 1 — ANALYTICAL, no simulation)

For small amplitudes (|x| ≪ 1, so C(x) ≈ x), E is approximately linear.
Compute the transfer function:

    H(k, ρ) = [1 + e^{-2πik/n}] · [1 + 2iρ·sin(2πk/n)]

where the first factor is B's transfer function (applied after A kills k=0)
and the second is R's. A removes DC. C ≈ identity for small amplitudes.

Plot |H(k,ρ)|² for several ρ values. This tells us EXACTLY which spatial
frequencies E amplifies or suppresses. Compare to the Ising correlation
function in k-space: S(k) ~ 1/(k² + ξ⁻²). Near Tc, ξ → ∞ so S(k) ~ 1/k²
(power concentrates at low k). If H amplifies low-k modes, ABCRE will be
sensitive to the diverging correlation length. If H is flat or high-pass,
it won't.

This analysis costs zero CPU time and answers Q0 definitively.

### V: Spatiotemporal evolution heatmap (Phase 2 — VISUAL)

For a single Ising row at temperature T, iterate E:
x₀ = row, x₁ = E(x₀, ρ), ..., x₂₀ = E(x₁₉, ρ).

Plot as heatmap: x-axis = spatial position (0 to L-1), y-axis = iteration
(0 to 20), color = value. Generate three panels: T = 1.5 (ordered),
T = 2.27 (critical), T = 3.5 (disordered).

This is the Wolfram approach: LOOK at the evolution before extracting
numbers. Patterns visible in these heatmaps (persistent structures, wave-like
propagation, rapid convergence to uniform) answer Q1 visually and guide which
scalar indicators to compute.

### I1: E-variance

`Var(E(rows, ρ), axis=-1).mean()` — variance of the transformed signal.
Single E application, no iteration. Quick sanity check alongside the
visual exploration.

### I3: ρ-convergence (PROMOTED — answers the most novel question Q2)

For fixed ρ, iterate E up to 20 times. A row "converges" if
‖xₙ - xₙ₋₁‖₂ < 1e-6 by iteration 20. Compute fraction of rows that
converge. Sweep ρ to find ρ₅₀ (the ρ at 50% convergence).

**The key question:** Does ρ₅₀ vary with temperature? If ρ₅₀(T) has a
feature at Tc, then ρ encodes information about the input's proximity to
criticality. This is the most unique potential finding — no other EWS
method has an analogous tunable parameter whose critical value carries
information.

Reframes ABCRE: not "a tool that detects transitions" but "a system that
itself undergoes a transition, parameterized by ρ, where the transition
point encodes input properties."

### I6: Correlation length transformation (explains mechanism)

Autocorrelation of E(row, ρ) vs autocorrelation of raw row. Ratio
ξ_E / ξ_raw. Connects directly to the transfer function H(k,ρ) from
Phase 1: if H amplifies modes near k ~ 1/ξ, then ξ_E > ξ_raw when ξ is
large (near Tc). This indicator EXPLAINS why ABCRE does or doesn't work,
by connecting the analytical prediction (H) to the empirical observation.

### I2: Transient sensitivity (LATER)

Variance of E^n(rows, ρ) at checkpoints n=1,3,5,10. Rate of change over
transient. MAX 20 iterations.

### I4: Fixed-point norm (LATER)

If iteration converges within 20 steps, ‖x*‖₂. NaN otherwise.

### I5: Spectral ratio (LATER)

Power in lowest 10% of frequency bins for FFT(E(x,ρ)) vs FFT(x).

### Statistical notes

- Error bars: bootstrap resampling of per-configuration indicator values
  (NOT recomputation from raw configs). 1000 bootstrap samples for
  publication; 200 for exploration.
- For ρ-dependent indicators: bootstrap gives POINTWISE CIs at each ρ.
  Plot CIs at every 5th ρ value to avoid false visual structure from
  independent fluctuations. If a feature at Tc is claimed, verify it's
  significant under Bonferroni correction for n_rho multiple comparisons.
- ρ scan: start with 10 values (exploration), increase to 50 (publication).

---

## 3. Systems Under Test

### Tier 0: Negative Control — 1D Random Correlated Spins

Generate 1D spin arrays (±1) with tunable correlation length using a Markov
chain with transition probability p. Correlation length ξ = -1/ln(1-2p).
Sweep p from 0 (random) to 0.49 (strongly correlated).

These are NOT near any phase transition. ABCRE should show NO features.
If it does, we have false positives and must understand why before proceeding.

### Tier 1: 2D Ising Model

Exact Tc = 2/ln(1+√2) ≈ 2.2692 (Onsager 1944).

**Phase 2:** Simple Metropolis algorithm in NumPy. Adequate for L≤32.
Single-spin-flip, no JIT. Each configuration: L² attempted flips = 1 sweep.
Equilibration: 500 sweeps. Decorrelation: 20 sweeps.

**Phase 5:** Wolff cluster algorithm (Numba JIT) for L≥64. Necessary because
Metropolis has critical slowing down z≈2.17 — at L=128 near Tc, decorrelation
requires ~10⁴ sweeps vs ~10 Wolff steps.

**ABCRE application:** The L×L lattice is treated as L row vectors of
length L, each with periodic boundaries. Apply E to the (L, L) array in
batch (axis=-1 is spatial). Average indicator over all rows.

**Known limitation:** Row-by-row discards inter-row correlations. If ABCRE
shows no signal, one explanation is that 1D slices lose too much 2D structure.
A 2D operator extension is a possible future direction but NOT in this plan.

**Classical benchmarks:**
- Magnetization: m = |Σ sᵢ| / N
- Susceptibility: χ = N(⟨m²⟩ − ⟨|m|⟩²) / T
- Binder cumulant: U = 1 − ⟨m⁴⟩/(3⟨m²⟩²) — size-independent crossing
  at Tc. **Preferred Tc extraction method** (no fitting needed).
- Specific heat: Cv = (⟨E²⟩ − ⟨E⟩²) / (NT²)

**Sampling progression:**

| Stage | L | n_temp | n_rho | n_samples | Purpose |
|-------|---|--------|-------|-----------|---------|
| Explore | 16 | 5 | 10 | 30 | See anything at all? |
| Quick | 16 | 15 | 20 | 100 | Confirm signal, check noise |
| Medium | 16,32 | 20 | 30 | 300 | Finite-size scaling begins |
| Full | 16,32,64 | 30 | 50 | 1000 | Publication-quality |
| Extra | 16,32,64,128 | 40 | 50 | 3000 | Final (needs Wolff) |

Explore config uses temperatures: [1.5, 2.0, 2.27, 2.5, 3.5]
(brackets Tc with one point right on it).

**Estimated times:** Explore: <2s. Quick: ~5s. Medium: ~1min. Full: ~15min.
Extra: ~2-4hr (Wolff required).

**Success criteria for Tier 1:**
- [ ] Classical indicators reproduce known Tc within 2% for L≥32
- [ ] Binder cumulant curves for different L cross within [2.20, 2.35]
- [ ] At least one ABCRE indicator shows a statistically significant feature
      at T within [2.1, 2.4]
- [ ] Feature sharpens with increasing L
- [ ] Feature location converges toward 2.269 with increasing L

**Failure criteria (stop here if all true):**
- No ABCRE indicator shows any feature near Tc for any ρ
- Or: ABCRE feature is weaker than raw spatial variance (no added value)

### Tier 2: Bifurcation Systems (Phase 6+)

Only if Tier 1 shows signal.

**Fold:** dx/dt = μ − x² + σ·dW. Bifurcation at μ=0.
**Pitchfork:** dx/dt = μx − x³ + σ·dW. Bifurcation at μ=0.
**Hopf:** dr/dt = μr − r³, dθ/dt = ω + br². Bifurcation at μ=0.
**Stommel 2-box:** Cessi (1994) parameterization:
  dT/dt = η₁ - T - |T-S|·T,  dS/dt = η₂ - η₃·S - |T-S|·S.
  η₂=1.0, η₃=0.3. Fold bifurcation in η₁.

**ABCRE for time series:** Sliding window of length w. Windows are NOT
periodic — use Tukey taper (α=0.1) to suppress edge discontinuity.
Test sensitivity to window length as a sanity check.

### Tier 3: Bury Benchmark (Phase 7)

Replicate Bury et al. (2021) test data. ROC/AUC comparison. ρ value for
ABCRE selected from Tier 1 results (no data snooping — Tier 1 is "training",
Tier 3 is "test"). Also report AUC distribution over all ρ values.

### Tier 4: Operator Ordering (Phase 7)

64 compositions: 24 four-op permutations + 24 three-op + 12 two-op + 4 single.
Run on Ising medium config. Measure both detection quality and ordering
richness (output variance, entropy, sensitivity to T). The question isn't
just "does ABRC detect Tc" but "does ABRC do more computation than other
orderings?"

---

## 4. Phase Specifications

### Phase 1: Operators + Transfer Function + Smoke Test

**Goal:** Port operators, understand E analytically, see first visual output.
Answers Q0 (what does E do mathematically?) before any simulation.

**Deliverables:**
- `operators.py` — ABCRE operators, compositions, iteration
- `transfer_function.py` — Fourier analysis of E in linear regime
- `explore.py` — smoke test: correlated vs uncorrelated arrays
- `tests/test_operators.py`
- `figures/transfer_function.png` — E's frequency response for several ρ
- `figures/smoke_test.png` — visual E output comparison
- `requirements.txt`, `.gitignore`
- Git repo initialized, first commit

**operators.py specification:**

ALL operators accept ndarray with spatial dimension along axis=-1.
1D input (shape (n,)) and 2D batch input (shape (batch, n)) must both work.

```python
import numpy as np
from itertools import permutations

def operator_a(x: np.ndarray) -> np.ndarray:
    """A(x)[i] = x[i] - mean(x). Vectorized along axis=-1."""
    return x - np.mean(x, axis=-1, keepdims=True)

def operator_b(x: np.ndarray) -> np.ndarray:
    """B(x)[i] = x[i] + x[(i+1) mod n]. Uses np.roll."""
    return x + np.roll(x, -1, axis=-1)

def operator_r(x: np.ndarray, rho: float) -> np.ndarray:
    """R(x,ρ)[i] = x[i] + ρ·(x[i+1] - x[i-1])."""
    return x + rho * (np.roll(x, -1, axis=-1) - np.roll(x, 1, axis=-1))

def operator_c(x: np.ndarray) -> np.ndarray:
    """C(x)[i] = x[i] / (1 + |x[i]|)."""
    return x / (1 + np.abs(x))

def operator_e(x: np.ndarray, rho: float) -> np.ndarray:
    """E(x,ρ) = C(R(B(A(x)), ρ)). Canonical composition."""
    return operator_c(operator_r(operator_b(operator_a(x)), rho))

def iterate_e(x: np.ndarray, rho: float, n_iter: int) -> list[np.ndarray]:
    """Apply E repeatedly, return list of states [E¹(x), ..., Eⁿ(x)].
    For transient analysis. Max n_iter ~20."""
    states = []
    current = x
    for _ in range(n_iter):
        current = operator_e(current, rho)
        states.append(current)
    return states

def make_composition(ordering: str):
    """Build composition from ordering string like 'ABRC'.
    Returns function (x, rho) -> ndarray."""
    ops = {
        'A': lambda x, _rho: operator_a(x),
        'B': lambda x, _rho: operator_b(x),
        'R': lambda x, rho: operator_r(x, rho),
        'C': lambda x, _rho: operator_c(x),
    }
    def composed(x, rho):
        result = x
        for char in ordering:
            result = ops[char](result, rho)
        return result
    return composed

ALL_ORDERINGS_4 = {
    ''.join(p): make_composition(''.join(p))
    for p in permutations('ABRC')
}  # 24 entries. 'ABRC' is the canonical ordering.
```

**transfer_function.py — THE MATH BEFORE THE SIMULATION:**

```python
"""Compute and plot E's transfer function in the linear regime.

For small amplitudes (|x| << 1), C(x) ≈ x, so E is approximately linear.
In Fourier space, each operator has a transfer function:

  A: H_A(k) = 1 for k ≠ 0, H_A(0) = 0   (kills DC)
  B: H_B(k) = 1 + exp(-2πik/n)            (low-pass with nulls)
  R: H_R(k,ρ) = 1 + 2iρ·sin(2πk/n)       (phase shift / circulation)

Combined (for k ≠ 0):
  H_E(k, ρ) = H_B(k) · H_R(k, ρ)
            = [1 + exp(-2πik/n)] · [1 + 2iρ·sin(2πk/n)]

Plot 1: |H_E(k,ρ)|² vs k/n for ρ = 0.0, 0.1, 0.3, 0.5, 0.7, 1.0
        → Shows which spatial frequencies E amplifies/suppresses.

Plot 2: Overlay Ising structure factor S(k) ~ 1/(k² + ξ⁻²) for
        ξ = 2, 5, 20, ∞ (spanning far-from-Tc to at-Tc).
        → Shows whether H_E's passband overlaps with where S(k) changes
        most as ξ → ∞.

Plot 3: Verify linearity assumption — apply E to small-amplitude (×0.01)
        random signal, compare to H_E prediction. Also apply to full-amplitude
        signal. How much does C's nonlinearity matter?

These three plots answer Q0 before any Ising simulation runs:
- If H_E is flat: E is a uniform smoother, won't detect Tc. KNOWN BEFORE SIMULATING.
- If H_E peaks at low k: E amplifies long-wavelength structure, WILL be
  sensitive to ξ → ∞ at Tc. Simulation confirms the prediction.
- If H_E peaks at high k: E amplifies short-wavelength noise, opposite of
  what we want. Negative result with clear explanation.
"""
```

**explore.py — smoke test:**

```python
"""Smoke test: does E(x, ρ) produce visually different output for
correlated vs uncorrelated 1D input?

1. Random uncorrelated ±1 spins (length 64)
2. Highly correlated ±1 spins (blocks of ~10 same spin)
3. Apply E at ρ = 0.0, 0.1, 0.3, 0.5, 0.7, 1.0
4. Plot: input vs E(input) for each ρ, two columns (uncorrelated | correlated)

If visually identical at all ρ → investigate before building anything else.
"""
```

**Test cases (test_operators.py):**

```
T1.1: A of constant array → all zeros
T1.2: A of [1,2,3] → [-1, 0, 1]
T1.3: B of [1,0,0] → [1, 0, 1] (wraps around)
T1.4: R of constant array → unchanged
T1.5: R of [0,1,0,-1] with ρ=0.5 → [1.0, 1.0, -1.0, -1.0]
       (R[0] = 0 + 0.5*(1-(-1)) = 1.0, R[1] = 1 + 0.5*(0-0) = 1.0,
        R[2] = 0 + 0.5*(-1-1) = -1.0, R[3] = -1 + 0.5*(0-0) = -1.0)
T1.6: C of [0] → [0]; C of [100] → 100/101; C of [-100] → -100/101
T1.7: C is odd: C(-x) == -C(x) for random input
T1.8: E output bounded: |E(x,ρ)[i]| < 1 for all i, any ρ, random input
T1.9: sum(A(x), axis=-1) ≈ 0 (atol=1e-10)
T1.10: 2D batch: operator_e(x_2d, rho)[i] == operator_e(x_2d[i], rho)
        for all rows i. Random (10, 64) array.
T1.11: ALL_ORDERINGS_4 has exactly 24 entries
T1.12: ALL_ORDERINGS_4['ABRC'] matches operator_e for random input
T1.13: Operators handle length-1 and length-2 arrays
T1.14: iterate_e returns list of length n_iter, all bounded
T1.15: Transfer function H_E matches empirical FFT(E(x))/FFT(x) for
        small-amplitude x (atol=0.01). Validates the linear analysis.
```

**Performance check (in smoke test):** operator_e on (256, 256) in <5ms.

**Commit:** `git add -A && git commit -m "Phase 1: operators + transfer function + smoke test"`

---

### Phase 2: Ising + Visual Exploration + ρ as Subject

**Goal:** Generate Ising configurations. LOOK at E's spatiotemporal evolution.
Compute I1 and I3 (ρ-convergence). Three outputs answer three questions:
heatmaps (Q1: what persists?), I1 vs T (Q3: signal at Tc?),
ρ₅₀ vs T (Q2: does ρ encode input properties?).

**Deliverables:**
- `ising.py` — simple Metropolis (NOT Wolff yet)
- `explore.py` updated — Tier 0 + spatiotemporal heatmaps + I1 + I3
- `tests/test_ising.py`
- `figures/tier0_negative_control.png`
- `figures/spatiotemporal_evolution.png` — THE WOLFRAM PLOT (heatmaps: iteration × position)
- `figures/tier1_I1_vs_T.png` — I1 vs T for multiple ρ
- `figures/tier1_rho50_vs_T.png` — ρ₅₀ convergence boundary vs T

**ising.py specification:**

```python
class IsingModel:
    """2D Ising model with simple Metropolis dynamics.
    No Numba, no JIT. Pure NumPy. Adequate for L ≤ 32."""

    def __init__(self, L: int, seed: int | None = None):
        self.L = L
        self.rng = np.random.default_rng(seed)
        self.spins = np.ones((L, L), dtype=np.int8)  # start all-up

    def metropolis_sweep(self, temperature: float):
        """One full sweep: L² random single-spin-flip attempts.
        Vectorized: generate all random numbers at once, compute
        ΔE for each site, accept/reject."""
        # Note: fully vectorized Metropolis is tricky (checkerboard
        # update avoids correlations). Use checkerboard pattern:
        # update even sites, then odd sites. Each half is independent.

    def equilibrate(self, temperature: float, n_sweeps: int = 500):
        """Run n_sweeps Metropolis sweeps. Reset from all-up first."""
        self.spins = np.ones((self.L, self.L), dtype=np.int8)
        for _ in range(n_sweeps):
            self.metropolis_sweep(temperature)

    def generate_configurations(self, temperature: float, n_samples: int,
                                 n_decorrelation: int = 20):
        """Generator: yield one (L, L) configuration at a time.
        n_decorrelation sweeps between samples."""
        self.equilibrate(temperature)
        for _ in range(n_samples):
            for _ in range(n_decorrelation):
                self.metropolis_sweep(temperature)
            yield self.spins.copy()

    TC = 2.0 / np.log(1 + np.sqrt(2))  # 2.2691853...
```

Checkerboard Metropolis: update all even-index sites simultaneously (their
neighbors are all odd, so no conflicts), then all odd sites. Two half-sweeps
= one full sweep. Fully vectorized in NumPy.

**explore.py — Tier 0 + Visual Exploration + I1 + I3:**

```python
# === Part A: Tier 0 Negative Control ===
# Generate correlated 1D spins (Markov chain, no phase transition)
# Apply E at 10 ρ values, compute I1 (variance of output)
# Plot I1 vs correlation_length for each ρ
# Expected: flat or monotonic. No peaks. If peaks → STOP.

# === Part B: Spatiotemporal Evolution (THE WOLFRAM PLOT) ===
# Generate ONE Ising config at each of T = 1.5, 2.27, 3.5
# Take one row from each. Iterate E for 20 iterations at ρ = 0.1, 0.3, 0.5
# Plot 3×3 heatmap grid: columns = T, rows = ρ
# Each cell: x-axis = spatial position (0 to L-1), y-axis = iteration (0 to 20)
# Color = value at that position and iteration.
#
# LOOK at these. Questions to answer visually:
# - Does the ordered row (T=1.5) converge to a uniform state?
# - Does the critical row (T=2.27) show persistent structure?
# - Does the disordered row (T=3.5) look different from critical?
# - How does ρ change the dynamics?
# This is Q1: what structures persist under iterated E?

# === Part C: I1 vs Temperature ===
# L=16, temperatures = [1.5, 2.0, 2.27, 2.5, 3.5], 30 samples each
# Apply E (single application) to all rows. Compute I1 at 10 ρ values.
# Also compute: magnetization, spatial_variance (baselines)
# Plot: I1 vs T for each ρ. Mark Tc.
# Q3: does I1 have a feature near Tc that spatial_variance does not?

# === Part D: ρ-Convergence (I3) ===
# Same configs as Part C.
# For each T: iterate E at 15 ρ values (0.0 to 1.0), 20 iterations each.
# For each (T, ρ): fraction of rows that converge (‖xₙ-xₙ₋₁‖ < 1e-6).
# Plot: convergence fraction vs ρ, one curve per T.
# Extract ρ₅₀ (ρ at 50% convergence) for each T.
# Plot: ρ₅₀ vs T. Mark Tc.
# Q2: does ρ₅₀ have a feature at Tc? THIS IS THE NOVEL QUESTION.
```

**Test cases (test_ising.py):**

```
T2.1: At T=0.5, |magnetization| > 0.95 (L=8, 50 samples avg)
T2.2: At T=5.0, |magnetization| < 0.2 (L=8, 50 samples avg)
T2.3: Configuration shape is (L, L) with values in {-1, +1}
T2.4: Deterministic with fixed seed
T2.5: generate_configurations yields correct count
T2.6: Energy per spin at T=0.5 ≈ -2.0 (within 0.05) for L=8
```

Note: L=8 for tests (fast). L=16 for exploration. Tests validate correctness,
not physics precision.

**Decision gate after Phase 2 — four figures, four verdicts:**

1. **`transfer_function.png` (from Phase 1):** Does H_E have structure?
   - Flat → E is a uniform smoother. Proceed anyway but expectations are low.
   - Peaked at low k → E amplifies long-wavelength modes. Promising.

2. **`tier0_negative_control.png`:** False positives?
   - Features present → STOP. Understand before proceeding.
   - Clean (flat/monotonic) → Continue.

3. **`spatiotemporal_evolution.png`:** Does iterated E look different near Tc?
   - All three T panels look the same → E doesn't distinguish. Negative for Q1.
   - Critical row shows distinct pattern (persistent structure, slower
     convergence, richer dynamics) → Positive for Q1. Worth quantifying.

4. **`tier1_I1_vs_T.png` and `tier1_rho50_vs_T.png`:** Signal at Tc?
   - I1 peaks near Tc AND differs from spatial_variance → Q3 positive.
   - I1 flat → try I6 in Phase 3.
   - ρ₅₀ has feature at Tc → Q2 positive. MOST NOVEL FINDING if true.
   - ρ₅₀ flat → ρ doesn't encode input properties. Q2 negative.

**Any positive answer → Phase 3. All negative → document, consider 2D extension.**

**Commit:** `git commit -m "Phase 2: Ising + visual exploration + rho-convergence"`

---

### Phase 3: Confirm + Explain Mechanism

**Goal:** Confirm Phase 2 signal with more data. Add I6 (correlation length
ratio) to explain WHY ABCRE sees or doesn't see Tc — connecting back to the
transfer function analysis from Phase 1. Add classical benchmarks for
comparison.

**Deliverables:**
- `indicators.py` — I1, I3, I6 (I2 only if I1/I3 showed signal)
- `classical.py` — magnetization, susceptibility, Binder cumulant
- `tests/test_indicators.py`
- `explore.py` updated — Tier 1 quick config
- `figures/tier1_quick_*.png` — multi-panel comparison plots
- `figures/mechanism_check.png` — I6 (ξ_E/ξ_raw) vs T, compared to
  transfer function prediction from Phase 1

**Sampling:** L=16, 15 temperatures (linspace 1.5–3.5), 20 ρ values, 100 samples.

**indicator introduction order:**
1. I1 (already working from Phase 2)
2. I6 (correlation length ratio — most physically motivated)
3. Classical (magnetization, susceptibility, Binder) for comparison
4. I2 (transient sensitivity) — only if I1/I6 show signal
5. I3 (ρ-convergence fraction) — only if I2 is interesting

**Classical indicators — simple functions, no class hierarchy:**

```python
def magnetization(config: np.ndarray) -> float:
    """m = |mean(spins)|"""
    return abs(config.mean())

def energy_per_spin(config: np.ndarray) -> float:
    """-Σ_{<i,j>} sᵢsⱼ / N"""

def susceptibility(m_values: np.ndarray, N: int, T: float) -> float:
    """χ = N(⟨m²⟩ − ⟨|m|⟩²) / T. Computed from array of m values."""

def binder_cumulant(m_values: np.ndarray) -> float:
    """U = 1 - ⟨m⁴⟩/(3⟨m²⟩²). Computed from array of m values."""
```

No base classes. Plain functions. If we need a class hierarchy later, refactor.

**Test cases (test_indicators.py):**

```
T3.1: magnetization of all-up lattice = 1.0
T3.2: magnetization of checkerboard = 0.0
T3.3: I1 of constant lattice = 0.0 (A zeros it)
T3.4: I6 of uncorrelated noise: ξ_raw ≈ 0 → handle gracefully (return NaN or 0)
T3.5: susceptibility of constant m_values = 0
T3.6: binder_cumulant of constant m_values = 2/3
```

**Commit:** `git commit -m "Phase 3: indicators + classical benchmarks"`

---

### Phase 4: Two-Size Finite-Size Check

**Goal:** Does the signal sharpen with increasing L? This separates real
physics from finite-size artifacts.

**Deliverables:**
- `explore.py` updated — L=16 AND L=32 comparison
- `figures/tier1_medium_*.png` — side-by-side L=16 vs L=32
- Binder cumulant crossing plot (Tc extraction)

**Sampling:** L=16,32. 20 temperatures. 30 ρ values. 300 samples.
Metropolis is still adequate at L=32 (each sweep: 1024 flips, ~1ms in NumPy).

**Key analysis:**
- Do ABCRE indicator features sharpen (narrower, taller) at L=32 vs L=16?
- Do Binder cumulant curves for L=16 and L=32 cross near Tc=2.269?
- If ABCRE features DON'T sharpen: the signal is a finite-size artifact, not
  real critical behavior. Negative result for scaling claim.

**Commit:** `git commit -m "Phase 4: two-size finite-size check"`

---

### Phase 5: Scale Up + Infrastructure

**Gate:** Only proceed here if Phases 2-4 show genuine signal that scales.

**Goal:** Add performance infrastructure. Scale to L=64+. Config system.

**Deliverables:**
- Wolff cluster algorithm (Numba JIT) in `ising.py`
- Config system (YAML) in `experiment.py`
- Welford accumulator for streaming statistics
- Generator pattern for configurations (memory-bounded)
- `analysis.py` — publication-quality plotting functions
- L=64 results

**Why now:** L=64 with Metropolis near Tc requires ~10⁴ sweeps for
decorrelation (critical slowing down). At 64² = 4096 flips/sweep, that's
~40M flips per sample. Still feasible in NumPy (~10s per sample) but Wolff
reduces this to ~10 cluster flips (~50ms per sample). For 1000 samples × 30
temperatures = 30,000 samples, the difference is 83 hours vs 25 minutes.

**Wolff in Numba:**

```python
@numba.njit
def _wolff_step(spins, p_add, rng_state):
    """Single Wolff cluster flip. BFS with pre-allocated stack.
    Modifies spins in-place."""
```

**Welford accumulator:**

```python
class WelfordAccumulator:
    """Online mean/variance. O(1) memory per statistic.
    Numerically stable (Welford 1962)."""
    def update(self, value): ...
    def mean(self): ...
    def variance(self): ...
```

**Memory budget:** Configurations yielded one at a time (generator pattern).
Per-config indicator values stored for bootstrap (n_samples floats, not
full configs). Peak memory for L=128, 3000 samples: ~200MB.

**Commit:** `git commit -m "Phase 5: Wolff + config system + L=64"`

---

### Phase 6: Full Tier 1 + Tier 2

**Goal:** Publication-quality Tier 1. Begin Tier 2 (bifurcation systems).

**Deliverables:**
- L=16,32,64 with 1000+ samples each. 30 temperatures. 50 ρ values.
- All 6 indicators (I1-I6).
- Finite-size scaling: Tc extraction from Binder crossing.
  If fitting T*(L) = Tc + a·L^(-1/ν), fix ν=1 (known for 2D Ising).
- Bifurcation systems: fold, pitchfork, Hopf, Stommel.
- CSD classical indicators (sliding variance, autocorrelation, DFA).

**Tier 2 specifics:**
- Sliding window with Tukey taper (α=0.1) for non-periodic boundary.
- Test sensitivity to window length (w = 50, 100, 200).
- ρ value from Tier 1 (no data snooping).

**Commit(s):** One per tier.

---

### Phase 7: Tier 3 + Tier 4

**Goal:** Head-to-head benchmark. Operator ordering exploration.

**Tier 3 (Bury benchmark):**
Bury's code: https://github.com/ThomasMBury/dl_detect. If available,
use their data generation. 500 approaching + 500 stationary per bifurcation
type. ROC/AUC.

**IMPORTANT:** ρ for ABCRE selected from Tier 1 (training). Tier 3 is the
test set. Also report AUC distribution over all ρ values (boxplot).

**Tier 4 (ordering exploration):**

64 compositions total:
- 24 four-operator permutations of {A,B,C,R}
- 24 three-operator compositions (4 subsets × 6 orderings each)
- 12 two-operator compositions (6 subsets × 2 orderings each)
- 4 single operators

For each: compute on Ising medium config. Measure:
- **Detection quality:** peak near Tc? How sharp? SNR?
  (baseline = indicator values at T < 1.8 and T > 2.8)
- **Richness:** output variance, Shannon entropy of binned output,
  sensitivity dI/dT at Tc.
  Answers: "does ABRC do more computation than other orderings?"
- **Tc detection:** binary — is there a peak within [2.1, 2.4]?

**Key questions:**
- Is ABRC the best? The richest? Both?
- Which operator is most important for detection?
- Does removing R destroy detection? (Tests the antisymmetric circulation claim)
- Does removing C cause numerical issues in iterated application?

**Visualizations:**
- 64-entry heatmap of detection quality
- Scatter: detection quality vs richness (if correlated → "more computation = better detection")
- Ablation bar chart: detection quality with each operator removed

**Commit(s):** One per tier.

---

### Phase 8: Publication Figures + Analysis

**Deliverables:**
- Publication-quality matplotlib figures (PDF output)
- Summary statistics
- Narrative writeup
- `notebooks/exploration.ipynb` — interactive walkthrough

**Figures:**
1. Transfer function |H_E(k,ρ)|² with Ising structure factor overlay
2. Spatiotemporal evolution heatmaps (3×3: T × ρ)
3. Tier 0: negative control (should be flat)
4. Classical Ising phase diagram (validation)
5. ABCRE heatmap: T vs ρ for I1 and I6
6. ρ₅₀ vs T (the novel finding, if it exists)
7. Comparison: classical vs ABCRE peaks, normalized
8. Binder cumulant crossing (Tc extraction)
9. Finite-size scaling
10. Tier 2: approaching bifurcation (4 panels)
11. Tier 3: ROC curves + AUC table
12. Tier 4: ordering landscape + richness scatter

---

## 5. Execution Order + Decision Gates

```
Phase 1 (operators + transfer function + smoke test)
    │
    ├─→ Q0: Transfer function H_E — does E have frequency selectivity?
    │    │
    │    ├─ H_E flat → E is a uniform smoother. Low expectations. Proceed anyway.
    │    └─ H_E structured → Prediction: E will be sensitive to correlation length.
    │
    └─→ Smoke test: does E output differ for correlated vs uncorrelated?
         │
         ├─ Identical → Investigate. (If H_E predicted this, we understand why.)
         └─ Different → Continue.

Phase 2 (Ising + visual exploration + ρ-convergence)
    │
    ├─→ Tier 0: false positives on random data?
    │    ├─ YES → STOP. Understand before proceeding.
    │    └─ NO → Continue.
    │
    ├─→ Q1: Spatiotemporal heatmaps — does iterated E look different near Tc?
    │    ├─ All panels look the same → Q1 negative. Continue with scalars anyway.
    │    └─ Critical row shows distinct pattern → Q1 positive. Worth quantifying.
    │
    ├─→ Q3: I1 feature near Tc?
    │    ├─ YES (and ≠ spatial_variance) → Signal exists. Phase 3.
    │    ├─ YES (but = spatial_variance) → No added value. Try I6 in Phase 3.
    │    └─ NO → Try I6 in Phase 3. If I6 also flat → Q3 negative.
    │
    └─→ Q2: ρ₅₀ feature near Tc?  ← THE NOVEL QUESTION
         ├─ YES → Most interesting finding. ρ encodes input properties. Phase 3.
         └─ NO → ρ doesn't carry information. Q2 negative.
    │
    └─→ Any Q positive → Phase 3.  All negative → document, consider 2D.

Phase 3 (confirm + explain mechanism) → Phase 4 (finite-size check)
    │
    └─→ Signal scales with L?
         │
         ├─ YES → Phase 5, 6, 7, 8
         │
         └─ NO → Finite-size artifact. Document.
```

---

## 6. Memory and Performance Budget

**Target machine:** 6GB RAM (Crostini), multi-core CPU, no GPU.

| Phase | Peak memory | CPU time | Bottleneck |
|-------|-------------|----------|------------|
| 1 (smoke test) | <50MB | <1s | Nothing |
| 2 (Tier 0+1 explore) | <100MB | ~10s | Metropolis at L=16 |
| 3 (Tier 1 quick) | <100MB | ~30s | ABCRE indicators |
| 4 (medium, L=32) | <200MB | ~2min | Metropolis decorrelation |
| 5 (L=64, Wolff) | <300MB | ~15min | Wolff JIT compile (one-time) |
| 6 (full) | <500MB | ~30min | ABCRE I2/I3 iteration |
| 7 (Tier 3+4) | <300MB | ~3hr | 64 compositions × medium |
| 8 (figures) | <200MB | ~5min | Plotting |

---

## 7. What the Generator Needs to Know

**Canonical operator definitions:** See `~/software/Invariant_Relational_Kernel_ABRCE/operators.rs`.
Port these EXACTLY. The Python implementations must produce identical outputs
to the Rust versions for identical inputs (within float precision).

**Critical performance rule:** ALL operators process 2D arrays (batch on
axis=0, spatial on axis=-1). No Python loops over rows. This is the
difference between minutes and hours.

**Key tension:** The canonical spec says A→B→R→C ordering is "non-negotiable."
Phase 7 tests alternative orderings. This is empirical science, not a
violation. Testing a claim doesn't violate it.

**Memory rule:** Never store all configurations. Use generators for configs,
Welford for running stats. The only list that grows is per-config indicator
values for bootstrap (floats, not configs).

**Style:** Clean, readable, minimal. Bruce reads code. No clever tricks.
No abstractions that don't earn their keep. A function is better than a class
until you need state. A constant at the top of a script is better than a
config file until you have multiple configs.

---

## Appendix: Red Team Issues Log (v4)

### Resolved in v4 (deeper questions / purpose alignment)

| # | Issue | Fix |
|---|-------|-----|
| Q0 | No analytical understanding before simulation | Transfer function analysis in Phase 1. Answers "what does E do?" with zero CPU. |
| Q1 | Jumped to scalar indicators without looking | Spatiotemporal heatmaps in Phase 2. Wolfram approach: LOOK first. |
| Q2 | ρ treated as nuisance parameter to sweep | ρ-convergence (I3) promoted to primary question. ρ₅₀ as novel indicator. |
| Q3 | "Does it detect Tc?" is the wrong first question | Reordered: Q0 (math) → Q1 (visual) → Q2 (ρ as subject) → Q3 (detection) → Q4 (ordering). |
| Q5 | Detection frame contradicts kernel's non-goal-directed philosophy | Reframed: "what persists under E?" rather than "what does E detect?" |

### Resolved in v3 (NEW issues from purpose/efficiency review)

| # | Issue | Fix |
|---|-------|-----|
| N1 | Premature infrastructure (ABCs, YAML, package structure) | Flat files, plain functions, refactor when warranted |
| N2 | Wolff in Phase 2 (over-engineered) | Metropolis for L≤32. Wolff deferred to Phase 5. |
| N3 | Six indicators designed blind | I1 first. Others added incrementally based on results. |
| N4 | 50 ρ values too dense for exploration | Start with 10, increase to 50 for publication. |
| N5 | 100 samples before seeing anything | Start with 30, increase as warranted. |
| N6 | pyproject.toml before code exists | requirements.txt until Phase 5+ |

### Resolved in v2 (from first two red teams)

| # | Issue | Fix |
|---|-------|-----|
| 1 | I2 measures asymptote dominated by C contraction | TransientSensitivity: first 10 iterations only |
| 2 | I3 "divergent" impossible with C | Convergence fraction (binary per-row) |
| 3 | Per-row Python loop 256× slow | Batch processing mandated |
| 4 | generate_batch OOMs at L=256 | Generator pattern + Welford |
| 5 | Time estimates 10-100× low | Revised upward |
| 6 | No negative control | Tier 0 added |
| 7 | Missing correlation length indicator | I6 added |
| 8 | Forced indicator hierarchy | Two base classes → now just functions |
| 9 | Finite-size scaling fit under-constrained | Fix ν=1, use Binder crossing |
| 10 | Time series windows not periodic | Tukey taper |
| 11 | Stommel under-specified | Cessi 1994 |
| 12 | Subset count wrong | Corrected to 64 |
| 13 | Bootstrap on ρ-dependent indicators | Bonferroni correction |
| 14 | "Best ρ" data snooping in Tier 3 | ρ from Tier 1, Tier 3 is test set |
| 15 | detection_quality baseline undefined | T < 1.8 and T > 2.8 |
| 16 | Ordering comparison lacks richness | ordering_richness added |

### Remaining (MEDIUM/LOW)

| # | Issue | Severity | Note |
|---|-------|----------|------|
| 16 | Row-by-row discards 2D correlations | MEDIUM | Documented. Possible Phase 9. |
| 17 | NKS analogy imprecise | LOW | Tempered in Tier 4 description. |
| 18 | Checkerboard Metropolis edge cases | LOW | Well-studied algorithm, standard implementation. |
