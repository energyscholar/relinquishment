# ewstools Architecture Specification v0.2

**Status:** Draft (for Bury review)
**Authors:** Bruce Stephenson, Robin Macomber
**Date:** 2026-05-09
**Converts to:** Polished HTML architecture proposal

---

## 1. Design Goals

| Priority | Goal | Constraint |
|----------|------|-----------|
| 1 | A domain scientist with 20 lines of math can contribute a new indicator | No touching core.py, no understanding the framework |
| 2 | Existing code continues to work unchanged | Zero breaking changes in v3.0 |
| 3 | One place to fix bugs, add features | DRY: harness owns all boilerplate |
| 4 | Cross-domain universality is visible in the structure | Domain packs make the math's universality tangible |
| 5 | Self-maintaining: CI enforces quality without human gatekeeping | Status promotion rules, auto-generated docs, regression tests |

**Non-goals:** Web framework, REST API, real-time streaming (Year 2+), GUI, database integration.

---

## 2. Current Architecture (Problems)

```
ewstools/                     ~2,900 lines total
├── __init__.py         11    Bare imports
├── core.py          1,837    God-class: TimeSeries + 14 compute_* + make_plotly
├── helpers.py       1,053    Spectral fitting, DFA, autocovariance, utilities
└── models.py            0    Empty (never used)
```

### 2.1 The Boilerplate Problem

Every `compute_*` method repeats the same ~13 lines:

```python
def compute_var(self, rolling_window=0.25, band_width=0.2):
    # --- BOILERPLATE (repeated 14×) ---
    if self.transition is not None:
        series = self.state[self.state.index <= self.transition]
    else:
        series = self.state
    
    if self.residuals is not None:
        eval_series = self.residuals
    else:
        eval_series = series
    
    rw = int(np.floor(rolling_window * len(series)))
    
    # --- ACTUAL MATH (1-2 lines) ---
    roll = eval_series.rolling(window=rw).var()
    
    # --- STORAGE (repeated 14×) ---
    self.ews['Variance'] = roll
    return self
```

**Impact:** A bug in window calculation requires fixing 14 methods. Adding weighted windows requires modifying 14 methods. Adding a new indicator requires understanding 1,837 lines to know where to put it and what boilerplate to copy.

### 2.2 Coupling Failures

| Component | Coupled to | Should be independent |
|-----------|-----------|----------------------|
| `make_plotly()` (260 lines) | TimeSeries class | Visualization backend |
| TensorFlow classifier | Import-time `try/except` | Optional dependency |
| `compute_*` methods | Internal state mutation | Pure functions |
| Detrending | Hardcoded in `TimeSeries.__init__` | Composable preprocessing |

---

## 3. Proposed Architecture

```
ewstools/
├── __init__.py                 Public API (thin re-exports)
├── core.py                     TimeSeries orchestrator (thin: delegates to harness)
├── harness.py                  Rolling-window engine (THE shared function)
├── registry.py                 Plugin discovery + metadata catalog
├── _compat.py                  Deprecation shims (v3 only, removed v4)
├── indicators/
│   ├── __init__.py             Package marker + discovery entry point
│   ├── _protocol.py            Indicator Protocol definition
│   ├── core/                   PRODUCTION: universal criticality indicators
│   │   ├── __init__.py         Domain metadata declaration
│   │   ├── variance.py         Variance, std, coefficient of variation
│   │   ├── autocorrelation.py  Lag-1 AC, lag-k AC, autocovariance function
│   │   ├── moments.py          Skewness, kurtosis
│   │   ├── spectral.py         Power spectrum, Smax, spectral exponent
│   │   ├── dfa.py              Detrended fluctuation analysis
│   │   └── entropy.py          Sample entropy, spectral entropy
│   ├── ecology/                BETA: domain-specific ecology indicators
│   ├── climate/                BETA: climate-specific indicators
│   ├── cardiac/                BETA: HRV and arrhythmia precursors
│   └── [domain]/               Additional domain packs
├── classifiers/
│   ├── _base.py                Classifier Protocol
│   └── dl_classifier.py        TensorFlow/PyTorch (lazy import)
├── viz/
│   ├── _backend.py             Visualization Protocol
│   └── plotly_backend.py       Default backend (extracted from core.py)
├── detrend.py                  Detrending methods (Gaussian, Lowess, polynomial)
└── cross_domain/               Research-grade cross-domain analysis (Year 2+)
    ├── compare.py              Run indicators across domain benchmarks
    └── convergence.py          Domain correlation matrix
```

---

## 4. Indicator Protocol

### 4.1 Definition

```python
# ewstools/indicators/_protocol.py
from __future__ import annotations
from typing import Protocol, runtime_checkable, Literal
import numpy as np

Status = Literal["unverified", "beta", "production"]

@runtime_checkable
class Indicator(Protocol):
    """Structural type for EWS indicators.
    
    Any object with these attributes and methods is an indicator.
    No inheritance required. No base class. Just implement the interface.
    """
    
    name: str
    """Short identifier, unique within domain. e.g. 'variance', 'lag1_ac'."""
    
    domain: str
    """Which domain pack this belongs to. e.g. 'core', 'ecology', 'climate'."""
    
    status: Status
    """Maturity level. CI enforces promotion rules."""
    
    is_rolling: bool
    """True: harness calls compute() per window. False: compute() receives full series."""
    
    def compute(self, data: np.ndarray, **kwargs) -> float | np.ndarray:
        """Compute the indicator.
        
        Parameters
        ----------
        data : np.ndarray
            If is_rolling=True: a single window (1D array of length window_size).
            If is_rolling=False: the full pre-processed series.
        **kwargs
            Indicator-specific parameters (e.g., lag=1 for autocorrelation).
        
        Returns
        -------
        float
            For rolling indicators: single scalar per window.
        np.ndarray
            For full-series indicators: array of values.
        """
        ...
```

### 4.2 Design Pattern: Strategy

The Indicator Protocol implements the **Strategy pattern**. The harness is the Context; each indicator is a concrete Strategy. Strategies are interchangeable at runtime without modifying the Context.

### 4.3 Why Protocol, Not ABC

| Approach | Requires inheritance | Works with dataclasses | Validates at runtime | Supports duck typing |
|----------|---------------------|--------------------------|---------------------|---------------------|
| ABC | Yes | No | Yes | No |
| **Protocol** | **No** | **Yes** | **Yes (`runtime_checkable`)** | **Yes** |
| Convention only | No | Yes | No | Yes |

Protocol (PEP 544) gives us structural subtyping: if an object has `name`, `domain`, `status`, `is_rolling`, and `compute()`, it IS an indicator. No registration ceremony. No inheritance tax. A domain scientist doesn't need to know what a Protocol is — they just write a class with the right shape.

### 4.4 Minimal Indicator Example

```python
# ewstools/indicators/core/variance.py
"""Variance indicator — simplest possible rolling EWS."""
import numpy as np

class Variance:
    name = "variance"
    domain = "core"
    status = "production"
    is_rolling = True
    
    def compute(self, data: np.ndarray, **kwargs) -> float:
        return np.var(data, ddof=1)
```

A contributor copies this template, changes the class name and `compute()` body, drops it in their domain directory.

### 4.5 Parametric Indicator Example

```python
# ewstools/indicators/core/autocorrelation.py
"""Lag-k autocorrelation indicator."""
import numpy as np

class Autocorrelation:
    name = "autocorrelation"
    domain = "core"
    status = "production"
    is_rolling = True
    
    def compute(self, data: np.ndarray, *, lag: int = 1) -> float:
        """Pearson autocorrelation at specified lag."""
        n = len(data)
        if n <= lag:
            return np.nan
        x = data[:n - lag]
        y = data[lag:]
        return np.corrcoef(x, y)[0, 1]
```

Parameters are kwargs with defaults. Users override at call time: `ts.compute("autocorrelation", lag=3)`.

### 4.6 Full-Series Indicator Example (DFA)

```python
# ewstools/indicators/core/dfa.py
"""Detrended Fluctuation Analysis — requires full series, not rolling window."""
import numpy as np

class DFA:
    name = "dfa"
    domain = "core"
    status = "production"
    is_rolling = False  # <-- harness passes full series, not windows
    
    def compute(self, data: np.ndarray, *, 
                scales: np.ndarray | None = None,
                order: int = 1) -> float:
        """Compute DFA scaling exponent alpha.
        
        Returns single float: the scaling exponent.
        """
        y = np.cumsum(data - np.mean(data))
        
        if scales is None:
            scales = np.unique(np.logspace(
                np.log10(4), np.log10(len(data) // 4), num=20
            ).astype(int))
        
        fluctuations = np.zeros(len(scales))
        for i, s in enumerate(scales):
            n_segments = len(y) // s
            if n_segments == 0:
                fluctuations[i] = np.nan
                continue
            segments = y[:n_segments * s].reshape(n_segments, s)
            # Detrend each segment
            x = np.arange(s)
            for j in range(n_segments):
                coeffs = np.polyfit(x, segments[j], order)
                segments[j] -= np.polyval(coeffs, x)
            fluctuations[i] = np.sqrt(np.mean(segments ** 2))
        
        # Log-log regression for scaling exponent
        valid = ~np.isnan(fluctuations) & (fluctuations > 0)
        if np.sum(valid) < 3:
            return np.nan
        coeffs = np.polyfit(np.log(scales[valid]), np.log(fluctuations[valid]), 1)
        return coeffs[0]  # alpha (scaling exponent)
```

---

## 5. Rolling-Window Harness

### 5.1 The Single Shared Function

```python
# ewstools/harness.py
"""Rolling-window computation engine.

This module contains the ONE function that replaces 14× duplicated boilerplate.
All rolling-window logic lives here. All indicators benefit from improvements here.
"""
from __future__ import annotations
import warnings
import numpy as np
import pandas as pd
from .indicators._protocol import Indicator

def apply_indicator(
    series: pd.Series,
    indicator: Indicator,
    *,
    rolling_window: int | float = 0.25,
    transition: float | None = None,
    use_residuals: bool = True,
    residuals: pd.Series | None = None,
    **indicator_kwargs,
) -> pd.Series:
    """Apply an indicator to a time series.
    
    Handles ALL shared logic:
    - Pre-transition truncation
    - Rolling window resolution (fraction → absolute)
    - Residuals selection
    - NaN propagation
    - Error isolation (indicator crash → NaN, not exception)
    
    Parameters
    ----------
    series : pd.Series
        Raw time series data.
    indicator : Indicator
        Any object satisfying the Indicator protocol.
    rolling_window : int or float
        If 0 < x < 1: fraction of series length.
        If x >= 1: absolute window size (integer).
    transition : float or None
        If set, truncate series to index <= transition.
    use_residuals : bool
        If True and residuals provided, compute on residuals.
    residuals : pd.Series or None
        Pre-computed residuals (from detrending).
    **indicator_kwargs
        Passed to indicator.compute(). e.g., lag=3.
    
    Returns
    -------
    pd.Series
        Indicator values. Same index as input (leading NaNs for rolling window).
    
    Raises
    ------
    ValueError
        If rolling_window resolves to < 2 or > len(series).
    TypeError
        If indicator does not satisfy the Indicator protocol.
    """
    # --- PROTOCOL VALIDATION ---
    if not isinstance(indicator, Indicator):
        raise TypeError(
            f"{type(indicator).__name__} does not satisfy the Indicator protocol. "
            f"Required: name, domain, status, is_rolling, compute()"
        )
    
    # --- PRE-TRANSITION TRUNCATION ---
    if transition is not None:
        eval_series = series[series.index <= transition]
    else:
        eval_series = series
    
    # --- RESIDUALS SELECTION (truncated to same range) ---
    if use_residuals and residuals is not None:
        eval_series = residuals[residuals.index.isin(eval_series.index)]
    
    # --- WINDOW RESOLUTION ---
    n = len(eval_series)
    if isinstance(rolling_window, float) and 0 < rolling_window <= 1.0:
        rw = max(2, int(np.floor(rolling_window * n)))
    elif isinstance(rolling_window, int) or rolling_window > 1.0:
        rw = int(rolling_window)
    else:
        raise ValueError(f"rolling_window must be > 0, got {rolling_window}")
    
    if rw < 2:
        raise ValueError(f"Resolved window size {rw} < 2. Series length: {n}")
    if rw > n:
        raise ValueError(f"Window size {rw} > series length {n}")
    
    # --- DISPATCH ---
    if indicator.is_rolling:
        return _apply_rolling(eval_series, indicator, rw, **indicator_kwargs)
    else:
        return _apply_full(eval_series, indicator, **indicator_kwargs)


def _apply_rolling(
    series: pd.Series, 
    indicator: Indicator, 
    window: int,
    **kwargs
) -> pd.Series:
    """Apply a rolling-window indicator with error isolation."""
    _error_count = [0]
    
    def _safe_compute(window_data: np.ndarray) -> float:
        try:
            result = indicator.compute(window_data, **kwargs)
            if not np.isfinite(result):
                return np.nan
            return float(result)
        except Exception as e:
            if _error_count[0] == 0:
                warnings.warn(
                    f"Indicator '{indicator.name}' raised {type(e).__name__}: {e} "
                    f"(further errors suppressed)",
                    RuntimeWarning, stacklevel=4
                )
            _error_count[0] += 1
            return np.nan
    
    result = series.rolling(window=window).apply(_safe_compute, raw=True)
    if _error_count[0] > 1:
        warnings.warn(
            f"Indicator '{indicator.name}' failed on {_error_count[0]} of "
            f"{len(series) - window + 1} windows",
            RuntimeWarning, stacklevel=2
        )
    return result


def _apply_full(
    series: pd.Series,
    indicator: Indicator,
    **kwargs
) -> pd.Series:
    """Apply a full-series indicator."""
    try:
        result = indicator.compute(series.values, **kwargs)
    except Exception as e:
        warnings.warn(
            f"Indicator '{indicator.name}' raised {type(e).__name__}: {e}",
            RuntimeWarning, stacklevel=3
        )
        return pd.Series(np.nan, index=series.index)
    
    if isinstance(result, (int, float)):
        # Single value: broadcast to series length (constant line)
        return pd.Series(result, index=series.index)
    else:
        return pd.Series(result, index=series.index[:len(result)])
```

### 5.2 Design Pattern: Strategy + Fixed Pipeline

The harness implements a **fixed pipeline** that accepts **Strategy** objects (indicators). The invariant algorithm (truncate → select residuals → resolve window → dispatch → store) is fixed. The variable step (`compute()`) is supplied by the indicator. This inverts the dependency: indicators don't know about the harness; the harness calls indicators through a stable interface.

### 5.3 Error Isolation

Indicators run inside a try/except boundary. A crashing indicator produces `NaN` for that window and a `RuntimeWarning`, not a stack trace that kills the entire computation. This is critical for:
- Third-party plugins with bugs
- Numerical edge cases (zero-variance windows, degenerate data)
- Interactive use in Jupyter (don't crash the notebook)

### 5.4 Future Harness Features (One Place to Add)

| Feature | Implementation location | Benefit |
|---------|------------------------|---------|
| Weighted windows | `_apply_rolling()` | Exponential/Gaussian weighting for all indicators |
| Adaptive windows | `apply_indicator()` | Window size varies with local dynamics |
| Parallelism | `_apply_rolling()` | Numba/multiprocessing for large datasets |
| Progress bar | `_apply_rolling()` | tqdm integration for long series |
| Caching | `apply_indicator()` | Memoize results for repeated calls |

Every indicator gets these improvements for free. Zero indicator code changes required.

---

## 6. Registry

### 6.1 Discovery Mechanism

Two-tier discovery (standard Python pattern: pytest, Flask, Sphinx):

**Tier 1 — Internal indicators (shipped with ewstools):**
Scanned from `ewstools/indicators/` subdirectories via `importlib`.

**Tier 2 — External plugins (third-party packages):**
Discovered via `importlib.metadata.entry_points(group="ewstools.indicators")`.

```python
# ewstools/registry.py
"""Indicator registry with lazy discovery and metadata catalog."""
from __future__ import annotations
import importlib
import importlib.metadata
import pkgutil
import threading
from typing import Iterator
from .indicators._protocol import Indicator, Status

class Registry:
    """Singleton registry for all discovered indicators.
    
    Thread-safe. Lazy-loaded on first access. Cached after discovery.
    """
    
    _instance: Registry | None = None
    _lock = threading.Lock()
    
    def __new__(cls) -> Registry:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._indicators = {}
                    cls._instance._discovered = False
        return cls._instance
    
    def _discover(self) -> None:
        """Discover all indicators (internal + external). Called once."""
        if self._discovered:
            return
        with self._lock:
            if self._discovered:
                return
            self._discover_internal()
            self._discover_external()
            self._discovered = True
    
    def _discover_internal(self) -> None:
        """Scan ewstools/indicators/ subdirectories."""
        import inspect
        import ewstools.indicators as pkg
        for importer, modname, ispkg in pkgutil.walk_packages(
            pkg.__path__, prefix="ewstools.indicators."
        ):
            if modname.endswith("_protocol") or modname.endswith("__init__"):
                continue
            try:
                module = importlib.import_module(modname)
            except ImportError:
                continue
            for attr_name in dir(module):
                obj = getattr(module, attr_name)
                if not isinstance(obj, type) or inspect.isabstract(obj):
                    continue
                try:
                    instance = obj()
                except (TypeError, Exception):
                    continue
                if isinstance(instance, Indicator):
                    key = f"{instance.domain}.{instance.name}"
                    self._indicators[key] = instance
    
    def _discover_external(self) -> None:
        """Discover third-party plugins via entry_points."""
        try:
            eps = importlib.metadata.entry_points(group="ewstools.indicators")
        except TypeError:
            # Python 3.9 compatibility
            eps = importlib.metadata.entry_points().get("ewstools.indicators", [])
        
        for ep in eps:
            try:
                indicator_class = ep.load()
                instance = indicator_class()
                if isinstance(instance, Indicator):
                    # External plugins forced to 'unverified' unless allow-listed
                    if not self._is_promoted(instance):
                        instance.status = "unverified"
                    key = f"{instance.domain}.{instance.name}"
                    self._indicators[key] = instance
            except Exception:
                continue  # Bad plugin → skip silently
    
    def _is_promoted(self, indicator: Indicator) -> bool:
        """Check if an external indicator has been explicitly promoted.
        
        Promotion list maintained in ewstools package data.
        Prevents external packages from self-declaring 'production' status.
        """
        # Future: read from ewstools/data/promoted_plugins.toml
        return False
    
    # --- PUBLIC API ---
    
    def get(self, name: str) -> Indicator:
        """Get indicator by name. Supports 'variance' or 'core.variance'."""
        self._discover()
        if "." in name:
            return self._indicators[name]
        # Search all domains for unqualified name
        matches = [v for k, v in self._indicators.items() if k.endswith(f".{name}")]
        if len(matches) == 1:
            return matches[0]
        if len(matches) == 0:
            raise KeyError(f"No indicator named '{name}'. Use registry.list() to see available.")
        raise KeyError(
            f"Ambiguous: '{name}' exists in domains: "
            f"{[m.domain for m in matches]}. Use 'domain.{name}' to disambiguate."
        )
    
    def list(self, *, domain: str | None = None, status: Status | None = None) -> list[str]:
        """List available indicators, optionally filtered."""
        self._discover()
        results = []
        for key, ind in sorted(self._indicators.items()):
            if domain and ind.domain != domain:
                continue
            if status and ind.status != status:
                continue
            results.append(key)
        return results
    
    def domains(self) -> list[str]:
        """List all registered domains."""
        self._discover()
        return sorted(set(ind.domain for ind in self._indicators.values()))
    
    def info(self, name: str) -> dict:
        """Get metadata for an indicator."""
        ind = self.get(name)
        return {
            "name": ind.name,
            "domain": ind.domain,
            "status": ind.status,
            "is_rolling": ind.is_rolling,
            "doc": ind.compute.__doc__ or "(no docstring)",
        }
    
    def __iter__(self) -> Iterator[Indicator]:
        self._discover()
        return iter(self._indicators.values())
    
    def __len__(self) -> int:
        self._discover()
        return len(self._indicators)
```

### 6.2 Design Patterns

- **Singleton** (one registry per process, thread-safe double-checked locking)
- **Lazy Initialization** (no import-time scanning; discovery on first `.get()` or `.list()`)

Note: The double-checked locking pattern is correct under CPython's GIL. For free-threaded Python (PEP 703, 3.13+), this would need revision to use `threading.Lock` unconditionally — negligible cost for a once-per-process operation.

### 6.3 External Plugin Registration

A third-party package registers indicators via standard Python packaging:

```toml
# pyproject.toml of a third-party plugin
[project.entry-points."ewstools.indicators"]
hurst = "ewstools_finance:HurstExponent"
flash_crash = "ewstools_finance:FlashCrashEWS"
```

After `pip install ewstools-finance`, the indicators appear automatically:
```python
>>> import ewstools
>>> ewstools.registry.list(domain="finance")
['finance.hurst', 'finance.flash_crash']
```

---

## 7. Public API (User-Facing)

### 7.1 New API

```python
import ewstools

# Load data
ts = ewstools.TimeSeries(data, transition=460)
ts.detrend(method='Gaussian', bandwidth=20)

# New unified interface
ts.compute("variance")                          # Rolling variance
ts.compute("autocorrelation", lag=1)            # Lag-1 AC
ts.compute("dfa")                               # Full-series DFA
ts.compute("core.spectral", method="welch")     # Qualified name

# Query available indicators
ewstools.registry.list()                         # All indicators
ewstools.registry.list(domain="ecology")         # Domain filter
ewstools.registry.list(status="production")      # Status filter
ewstools.registry.info("dfa")                    # Metadata

# Compute multiple at once
ts.compute_all(["variance", "autocorrelation", "skewness"])

# Visualization (unchanged but decoupled)
ts.make_plotly()
```

### 7.2 Deprecated API (v3.0 shims, removed in v4.0)

```python
# Still works, emits FutureWarning:
ts.compute_var()          # → ts.compute("variance")
ts.compute_auto()         # → ts.compute("autocorrelation")
ts.compute_skew()         # → ts.compute("skewness")
ts.compute_kurt()         # → ts.compute("kurtosis")
# ... all 14 methods shimmed
```

### 7.3 Shim Implementation

```python
# ewstools/_compat.py
"""Backward-compatibility shims. Removed in v4.0."""
import warnings
import functools

_SHIM_MAP = {
    "compute_var": "variance",
    "compute_auto": "autocorrelation",
    "compute_skew": "skewness",
    "compute_kurt": "kurtosis",
    "compute_cv": "cv",
    "compute_std": "std",
    # ... complete mapping
}

def make_shim(old_name: str, new_name: str):
    """Generate a deprecation shim method."""
    def shim(self, rolling_window=0.25, **kwargs):
        warnings.warn(
            f"{old_name}() is deprecated since v3.0. "
            f"Use ts.compute('{new_name}') instead. "
            f"Will be removed in v4.0.",
            FutureWarning, stacklevel=2
        )
        return self.compute(new_name, rolling_window=rolling_window, **kwargs)
    shim.__name__ = old_name
    return shim
```

---

## 8. Domain Pack Structure

### 8.1 Domain Metadata

```python
# ewstools/indicators/ecology/__init__.py
"""Ecology domain pack — indicators specific to ecological tipping points."""

DOMAIN_METADATA = {
    "name": "ecology",
    "status": "beta",
    "description": "Indicators for ecological regime shifts and critical transitions",
    "citation": "Scheffer et al. (2009) Nature 461:53-59",
    "maintainer": "ewstools contributors",
    "min_ewstools_version": "3.0",
}
```

### 8.2 Status Lifecycle

```
UNVERIFIED ──────────────────────► BETA ─────────────────────────► PRODUCTION
    │                                  │                                 │
    │ Requirements:                    │ Requirements:                   │ Guarantees:
    │ • compute() runs without error   │ • Tested on ≥2 real datasets   │ • Numerically validated
    │ • Has docstring                  │ • Reviewed by domain expert    │ • Benchmarked vs reference
    │ • Passes type checking           │ • Performance baseline set     │ • Stable API ≥6 months
    │                                  │ • Citation provided            │ • Used in publication
    │                                  │                                │ • Regression tests
```

**CI enforcement:** A PR that changes `status = "production"` triggers a CI check requiring:
- All benchmark datasets pass
- Numerical equivalence test against reference implementation
- No performance regression beyond 10%
- Changelog entry

### 8.3 Contributor Workflow

```
1. Fork ewstools
2. Create file: indicators/[domain]/my_indicator.py
3. Implement: name, domain, status="unverified", is_rolling, compute()
4. Add test: tests/indicators/test_my_indicator.py
5. Submit PR
6. CI validates: Protocol compliance, tests pass, type checks pass
7. Maintainer reviews → merge as "unverified"
8. Later: benchmarking + domain expert review → promote to "beta"
```

---

## 9. Security Analysis

### 9.1 Threat Model

ewstools is scientific computing software used in research environments. The trust boundary is `pip install` — once a package is installed, its code runs with full process privileges. This is standard for the scientific Python ecosystem (numpy, scipy, pandas all operate this way).

| Threat | Risk | Mitigation |
|--------|------|-----------|
| Malicious external plugin (supply chain) | Medium | External plugins forced to "unverified". Users see status. Promotion requires explicit allow-listing. |
| Plugin infinite loop / memory exhaustion | Low | Optional `timeout` parameter on `apply_indicator()`. Default: no timeout (scientific workflows may be long). |
| Plugin writing to filesystem / network | Low | Convention: indicators SHOULD be pure functions. Enforced by code review, not runtime sandbox. |
| Malicious input data (crafted series) | Very Low | numpy operations are bounds-checked. No buffer overflow risk in pure Python. |
| Dependency confusion (typosquatting) | Low | Entry point group is `ewstools.indicators` — only packages explicitly declaring this group are scanned. |

### 9.2 Design Decisions

- **No runtime sandboxing.** Python cannot meaningfully sandbox code in-process. Attempting it (e.g., restricted exec) provides false security and breaks legitimate use.
- **No pickle/eval in plugin loading.** Discovery uses `importlib` only — modules are imported, not deserialized.
- **No network access in harness.** The harness never fetches data, downloads models, or phones home.
- **External plugins default to "unverified".** Users can see at a glance which indicators are vetted vs. third-party.
- **Input validation at the harness boundary.** Window size, series length, and NaN density checked before calling indicators.

### 9.3 Dependency Policy

```
# Core (required):
numpy >= 1.22
pandas >= 1.4

# Optional per domain:
[ecology]  # no additional deps
[climate]  # no additional deps  
[cardiac]  # no additional deps (pure numpy math)

# Optional visualization:
[viz]
plotly >= 5.0

# Optional classifiers:
[dl]
tensorflow >= 2.10  # or torch >= 2.0

# Development:
[dev]
pytest >= 7.0
mypy >= 1.0
```

Minimal dependency footprint. Domain packs use numpy only unless explicitly documented otherwise.

---

## 10. Testing Strategy

### 10.1 Test Pyramid

```
                    ┌────────────────┐
                    │  Integration   │  Few: full TimeSeries workflow
                    │   (5-10)       │  (compute → store → visualize)
                    ├────────────────┤
                    │  Harness Tests │  Medium: window resolution, edge cases,
                    │   (20-30)      │  error isolation, NaN handling
                    ├────────────────┤
                    │ Indicator Unit │  Many: one test per indicator,
                    │  Tests (50+)   │  known-input → known-output
                    └────────────────┘
```

### 10.2 Numerical Equivalence Tests

Every converted indicator has a test proving numerical equivalence with the old `compute_*` method:

```python
def test_variance_equivalence():
    """New plugin produces identical results to old compute_var()."""
    ts_old = ewstools.TimeSeries(DATA)
    ts_old.compute_var(rolling_window=0.25)  # Old method
    
    ts_new = ewstools.TimeSeries(DATA)
    ts_new.compute("variance", rolling_window=0.25)  # New method
    
    # Old API stores as 'Variance'; new stores as indicator.name ('variance')
    np.testing.assert_array_almost_equal(
        ts_old.ews['Variance'].values,
        ts_new.ews['variance'].values,
        decimal=10
    )
    # NOTE: v3 shim also populates legacy key 'Variance' for compat
```

### 10.3 Property-Based Tests

```python
from hypothesis import given, strategies as st

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=50, max_size=1000))
def test_variance_non_negative(data):
    """Variance is always >= 0 for any input."""
    series = pd.Series(data)
    result = apply_indicator(series, Variance(), rolling_window=20)
    assert (result.dropna() >= 0).all()
```

---

## 11. Backward Compatibility Contract

### 11.1 Migration Path

| Version | State | User action required |
|---------|-------|---------------------|
| v2.x (current) | Monolithic `compute_*` methods | None |
| **v3.0** | Plugin system added. Shims preserve old API. | None (FutureWarnings appear) |
| v3.x | Both APIs coexist. New features via plugin system only. | Migrate at own pace |
| **v4.0** | Shims removed. Old `compute_*` methods gone. | Update calls to `ts.compute("name")` |

### 11.2 Guarantees

- `ts.compute_var()` works identically in v3.x as in v2.x (same results, same return type)
- `ts.ews` dictionary populated by both old and new API
- `ts.make_plotly()` works with results from either API
- Test suite runs BOTH old and new code paths until v4.0

### 11.3 Migration Script (shipped with v3.0)

```bash
# Automated migration tool
ewstools-migrate path/to/your/script.py
# Rewrites: ts.compute_var() → ts.compute("variance")
# Uses lib2to3 AST transformation — safe, reversible
```

---

## 12. Performance Considerations

### 12.1 Baseline (Current)

Current `compute_*` methods use `pd.Series.rolling().apply()` which calls Python for each window. This is the performance floor. The new system cannot be slower.

### 12.2 Optimization Path (Future)

| Optimization | Where | Speedup | Complexity |
|-------------|-------|---------|-----------|
| `raw=True` in `.apply()` | Harness | 2-5× | Already implemented |
| Numba JIT for indicators | Indicator | 10-100× | Optional decorator |
| Vectorized indicators | Indicator | 5-50× | Where math permits |
| Parallel windows | Harness | N× cores | `concurrent.futures` |

**Design constraint:** Optimizations are opt-in. A plain Python `compute()` always works. Numba is never required.

### 12.3 Numba-Compatible Indicator (Optional)

```python
# Indicators can optionally provide a numba-jitted version
import numpy as np
try:
    from numba import njit
    
    @njit
    def _variance_fast(data):
        # Manual ddof=1: Numba doesn't support np.var(ddof=) in all versions
        n = len(data)
        mean = np.sum(data) / n
        return np.sum((data - mean) ** 2) / (n - 1)
    
    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False

class Variance:
    name = "variance"
    domain = "core"
    status = "production"
    is_rolling = True
    
    def compute(self, data: np.ndarray, **kwargs) -> float:
        if HAS_NUMBA:
            return _variance_fast(data)
        return np.var(data, ddof=1)
```

---

## 13. Documentation Architecture

### 13.1 Auto-Generated Catalog

The registry produces a live indicator catalog:

```python
ewstools.registry.catalog()  # Returns markdown table of all indicators
```

Output:
```
| Name | Domain | Status | Rolling | Description |
|------|--------|--------|---------|-------------|
| variance | core | production | Yes | Sample variance (ddof=1) |
| autocorrelation | core | production | Yes | Lag-k Pearson autocorrelation |
| dfa | core | production | No | Detrended fluctuation analysis |
| spectral_reddening | climate | beta | Yes | Spectral exponent trend |
| ...  | ... | ... | ... | ... |
```

CI generates this on every release → published to docs site.

### 13.2 Plugin Author Guide (Shipped with Package)

```
docs/
├── user_guide.md              Using ewstools (unchanged)
├── indicator_authoring.md     "Add a new indicator in 10 minutes"
├── domain_pack_guide.md       "Create a new domain pack"
├── api_reference/             Auto-generated from docstrings
└── architecture.html          THIS DOCUMENT (polished)
```

### 13.3 Indicator Docstring Convention (NumPy Style)

```python
class MyIndicator:
    """One-line summary.
    
    Extended description if needed. Include the mathematical
    definition in LaTeX-compatible notation.
    
    Parameters (via compute kwargs)
    ----------
    param_name : type
        Description. Default: value.
    
    Returns
    -------
    float
        Description of what the number means.
    
    References
    ----------
    [1] Author (Year). "Title." Journal. DOI.
    
    Examples
    --------
    >>> ts.compute("my_indicator", param_name=value)
    """
```

---

## 14. Self-Maintaining Features

### 14.1 CI Pipeline

```yaml
# .github/workflows/ci.yml
jobs:
  test:
    strategy:
      matrix:
        python: ["3.9", "3.10", "3.11", "3.12"]
        numpy: ["1.22", "1.26", "2.0", "2.1"]
    steps:
      - run: pytest tests/ --strict-markers
      - run: mypy ewstools/ --strict
      - run: python -m ewstools.registry validate  # Protocol compliance check
  
  catalog:
    steps:
      - run: python -m ewstools.registry catalog > docs/indicator_catalog.md
      - run: git diff --exit-code docs/  # Fail if catalog changed (needs commit)
  
  benchmarks:
    steps:
      - run: pytest tests/benchmarks/ --benchmark-compare
      # Fails if any indicator regresses > 10% vs baseline
  
  status-audit:
    steps:
      - run: python -m ewstools.registry audit
      # Checks: no "production" indicator without benchmark test
      # Checks: no "beta" indicator without citation in docstring
      # Checks: no external plugin claiming non-"unverified" status
```

### 14.2 Registry Self-Validation

```python
# ewstools/registry.py (addition)
def validate(self) -> list[str]:
    """Validate all registered indicators. Used by CI."""
    self._discover()
    errors = []
    for key, ind in self._indicators.items():
        if not hasattr(ind, 'compute') or not callable(ind.compute):
            errors.append(f"{key}: missing compute() method")
        if ind.status not in ("unverified", "beta", "production"):
            errors.append(f"{key}: invalid status '{ind.status}'")
        if ind.status == "production" and not ind.compute.__doc__:
            errors.append(f"{key}: production indicator lacks docstring")
    return errors

def audit(self) -> list[str]:
    """Audit status claims against evidence. Used by CI."""
    self._discover()
    warnings = []
    for key, ind in self._indicators.items():
        if ind.status == "production":
            test_file = f"tests/indicators/test_{ind.name}.py"
            # Check test exists (CI will verify content)
            warnings.append(f"AUDIT: {key} claims production — verify {test_file} exists")
    return warnings
```

### 14.3 Deprecation Lifecycle (Automated)

```python
# _compat.py tracks when shims were introduced
_SHIM_INTRODUCED = "3.0.0"
_SHIM_REMOVAL_TARGET = "4.0.0"

# CI check: if current version >= 4.0.0, _compat.py must not exist
```

---

## 15. Cross-Domain Module (Year 2-3, Grant-Funded)

*API sketch — signals architectural intent, not implementation-ready specification. Full design requires domain expert input during grant execution.*

### 15.1 Compare

```python
# ewstools/cross_domain/compare.py
def compare(
    indicator: str,
    datasets: dict[str, pd.Series],
    rolling_window: float = 0.25,
) -> pd.DataFrame:
    """Run the same indicator across domain-labeled datasets.
    
    Parameters
    ----------
    indicator : str
        Indicator name (e.g., "variance", "autocorrelation").
    datasets : dict
        Keys are domain labels, values are time series.
    
    Returns
    -------
    pd.DataFrame
        Columns: domain, kendall_tau, p_value, lead_time
        One row per dataset showing the indicator's performance.
    """
```

### 15.2 Convergence Matrix

```python
def convergence_matrix(
    indicators: list[str],
    datasets: dict[str, pd.Series],
) -> pd.DataFrame:
    """Compute cross-domain indicator performance correlation.
    
    Shows which indicators behave similarly across which domains.
    High correlation = mathematical universality of that indicator.
    Low correlation = domain-specific behavior.
    """
```

### 15.3 RAF Analysis (Research-Grade)

```python
def method_graph(registry: Registry) -> dict:
    """Construct the citation/derivation graph of indicators.
    
    Edges: indicator A in domain X was derived from / inspired by
    indicator B in domain Y (from citation metadata in docstrings).
    
    Returns graph suitable for RAF analysis: which subsets of the
    indicator ecosystem are reflexively autocatalytic?
    """
```

---

## 16. Versioning and Release Strategy

| Version | Content | Timeline |
|---------|---------|----------|
| 3.0.0-alpha | Harness + registry + 3 core indicators converted + shims | Phase 2 (pre-grant) |
| 3.0.0-beta | All 14 core indicators converted + 1 domain pack | Phase 2 complete |
| 3.0.0 | Full release: all indicators, docs, migration script | Grant Year 1 |
| 3.1.0 | First domain packs (ecology, climate) | Grant Year 1-2 |
| 3.2.0 | Cross-domain module, benchmarking suite | Grant Year 2 |
| 4.0.0 | Shims removed, old API gone | Grant Year 3 |

**SemVer commitment:** Minor versions add features. Major versions may break API. Patch versions fix bugs only.

---

## 17. Design Decisions Log

| Decision | Alternatives Considered | Rationale |
|----------|------------------------|-----------|
| Protocol over ABC | ABC, plain dict, dataclass | Structural typing: no inheritance burden on contributors |
| Singleton Registry | Module-level dict, class method | Thread safety, lazy loading, single source of truth. Acceptable overhead for single init. |
| Entry points for external plugins | Config file, explicit registration | Standard Python mechanism, zero config for users |
| Mutable status override on external plugins | Separate allow-list file, wrapper class | Direct attribute set is simplest; documented constraint that `status` must be writable |
| Error isolation (NaN on crash) | Propagate exceptions, skip silently | Jupyter-friendly, non-destructive, still warns |
| No runtime sandboxing | RestrictedPython, subprocess | False security, incompatible with numpy/pandas |
| `raw=True` in rolling.apply | Custom loop, strided windows | pandas-native, proven, correct |
| Fractional window (0.25) | Always absolute | Backwards compatible with existing API |
| Domain directories (not tags) | Flat indicators/ with domain attribute | Filesystem structure IS the domain organization — visible |
| Status as Protocol field | Separate metadata file, decorator | Self-documenting: status lives WITH the indicator |
| Shims via method generation | Manual wrappers, `__getattr__` | DRY, complete coverage, easy to remove |

---

## 18. Public API Contract

### 18.1 `ts.compute()` Return Value

`ts.compute(name, **kwargs)` returns `self` (for method chaining). The result is stored in `ts.ews[indicator.name]` using the indicator's lowercase `name` field. The v3 shims additionally populate the legacy capitalized key (e.g., both `'variance'` and `'Variance'`).

Re-computation overwrites the previous result for that indicator name.

### 18.2 `ts.compute_all()` Specification

```python
def compute_all(
    self,
    indicators: list[str | tuple[str, dict]],
    rolling_window: float = 0.25,
) -> Self:
    """Compute multiple indicators.
    
    Each element is either a name (uses default kwargs) or
    a (name, kwargs_dict) tuple for per-indicator parameters.
    
    Example:
        ts.compute_all([
            "variance",
            ("autocorrelation", {"lag": 3}),
            "skewness",
        ])
    """
```

### 18.3 Column Naming in `ts.ews`

| API | Storage key | Example |
|-----|-------------|---------|
| `ts.compute("variance")` | `indicator.name` | `"variance"` |
| `ts.compute("autocorrelation", lag=3)` | `indicator.name` | `"autocorrelation"` |
| `ts.compute("core.variance")` | `indicator.name` (unqualified) | `"variance"` |
| v3 shim `ts.compute_var()` | Both legacy AND new | `"Variance"` + `"variance"` |

### 18.4 Indicator Constraints

Indicators MUST be pure functions of their input data:
- `compute()` MUST NOT mutate the `data` array (harness passes `raw=True` buffer)
- `compute()` MUST NOT access filesystem, network, or global mutable state
- `compute()` SHOULD be deterministic for the same input

These are enforced by code review and documented convention, not runtime sandbox.

---

## 19. Configuration

### 19.1 Defaults

```python
# ewstools/config.py
DEFAULTS = {
    "rolling_window": 0.25,
    "log_level": "WARNING",
    "enable_numba": True,
    "max_window_fraction": 0.9,
}
```

Users override via:
```python
ewstools.config.rolling_window = 0.5          # Session-wide
ts.compute("variance", rolling_window=0.4)     # Per-call (always wins)
```

### 19.2 Logging

```python
import logging
logger = logging.getLogger("ewstools")
# Default: WARNING (matches scientific Python convention)
# Users: logging.getLogger("ewstools").setLevel(logging.DEBUG)
```

RuntimeWarnings for indicator failures. Structured logging for batch processing.

---

## 20. Protocol Versioning

The Indicator Protocol is versioned. Current: `protocol_version = 1`.

| Version | Fields | Backward compat |
|---------|--------|-----------------|
| 1 (v3.0) | name, domain, status, is_rolling, compute() | — |
| 2 (future) | + citation, + parameters_schema | v1 indicators still work; new fields optional with defaults |

Rule: new Protocol fields are ALWAYS optional with sensible defaults. Existing plugins never break from a Protocol version bump. The registry checks `getattr(ind, 'protocol_version', 1)` and handles accordingly.

---

## 21. What This Architecture Enables

1. **For domain scientists:** 8-20 lines of math. No framework knowledge required.
2. **For Bury:** Reviewable design. Clear upgrade path. No risk to existing users.
3. **For the grant:** "Plugin architecture = community multiplier" is a concrete deliverable.
4. **For benchmarking:** Any indicator × any domain's datasets with one function call.
5. **For the field:** First standardized, extensible EWS computation framework. Fills the gap left by earlywarnings (R, CRAN-removed June 2025).
6. **For cross-domain science:** Domain packs make universality visible and computable.

1. **For domain scientists:** Write 8-20 lines of math. Contribute an indicator. No framework knowledge required.
2. **For Bury:** Reviewable, approvable design. Clear upgrade path. No risk to existing users.
3. **For the grant:** "Plugin architecture = community multiplier" is a concrete deliverable, not a vague promise.
4. **For benchmarking:** Run any indicator across any domain's datasets with one function call.
5. **For the field:** The first standardized, extensible EWS computation framework. Fills the gap left by earlywarnings (R, CRAN-removed June 2025).
6. **For cross-domain science:** The structure SHOWS that the same math works across domains. Domain packs make universality visible and computable.
