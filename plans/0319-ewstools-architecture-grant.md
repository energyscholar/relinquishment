# Plan 0319 — ewstools Architecture + Grant + Outreach Campaign

**Status:** Active
**Priority:** High (income pathway)
**Owner:** Bruce + Robin
**Stakeholder:** Thomas Bury (PI, UCR)
**PTL:** PTL-145 (grant), PTL-120 (job search)

## Strategic Frame

This is not three separate projects. It is one coordinated campaign with four outputs:

1. **Architecture document** — demonstrates competence, gives Bury something to approve
2. **User outreach** — surfaces feature requests, builds relationships, generates user statements for grant, identifies contract opportunities
3. **Grant application** — wraps (1) + (2) into funding. Even if rejected, (1) and (2) already paid off.
4. **Contract pipeline** — every outreach conversation is a potential client. "We're building this anyway — would your group benefit from custom integration?"

The grant is the *excuse* for the outreach. The outreach builds the network regardless of grant outcome. Bury's endorsement converts cold emails to warm introductions. This is enterprise sales methodology applied to academic scientific software.

**Key insight:** The same work serves all four goals simultaneously. No wasted motion.

## Grant Target: NSF CSSI Elements

**Amount:** $600,000 / 3 years
**Fit:** Excellent. Domain-agnostic, explicitly multi-directorate, values cross-domain tools.
**PI:** Thomas Bury (Assistant Professor, Mathematics, UC Riverside — R1, tenure-track, qualifies)
**Named contributors:** Bruce Stephenson, Robin Macomber
**Solicitation:** NSF 22-632 (still active, annual cycle)
**Deadline:** December 1, 2026 (confirmed via FY26 webinar Nov 2025 + Duke tracker)
**Page limit:** 15-page Project Description + 2-page Community Usage Metrics + 2-page CI Mentoring Plan
**Contact:** CSSIQueries@nsf.gov (confirmed active)
**Requirement:** Must budget PI meeting travel. Must show demonstrated community need.

**Why CSSI over CZI EOSS:**
- EOSS is dead (last cycle Oct 2023, CZI restructured Feb 2026)
- CSSI is 3× the money ($600K vs $200K)
- CSSI is domain-agnostic (ewstools' cross-domain reach is a *strength*)
- CSSI is 3 years (vs 2) — sustainable development timeline
- CSSI funds development + benchmarking + community (not just maintenance)

**Secondary targets:**
- **CZI EOSS Cycle 7:** Possibly Oct 18, 2026 LOI (UNCONFIRMED — Cycle 6 closed Oct 2023, no C7 announced). $100K–$400K / 2yr. Monitor chanzuckerberg.com/rfa/. Life-sciences scope.
- **NSF PESOSE Phase I (NSF 26-506):** Supersedes POSE. $300K/2yr. ~Sept 2026 deadline (verify). Community-building + security focus. Requires existing user base. Good fit after Phase 2 implementation proves community uptake.
- **NSF PESOSE Phase II:** $750K/3yr. ~Mar 2027. Requires Phase I or equivalent.

**Note:** "OS4LS" label appears to be informal/unconfirmed programme name. The actual EOSS successor mechanism is unclear. CZI restructured Feb 2026. Monitor but don't plan around.

## Phase 1: Architecture Proposal

**Format:** Polished HTML document with diagrams. Like the existing ewstools tutorials but for architecture.
**Audience:** Bury first (approval), then outreach contacts (credibility), then grant reviewers.
**Bundled with:** numpy2-compat PR (maintenance credibility, already on branch).

### Current Architecture (Problems)

```
ewstools/
├── core.py        1,837 lines — god-class TimeSeries with 14 compute_* methods
├── helpers.py     1,053 lines — spectral fitting, DFA, autocovariance
├── models.py      0 lines — empty
└── __init__.py    11 lines
```

**Problem 1: Monolithic compute methods.**
14 `compute_*` methods on one class. Each contains ~13 lines of identical harness (pre-transition cut, window conversion, residuals selection) wrapping 1-2 lines of actual math. Adding a new EWS method requires editing the god-class.

**Problem 2: Visualization coupled to computation.**
`make_plotly()` is 260 lines on TimeSeries. Cannot swap backends. Cannot compute without importing plotly.

**Problem 3: No plugin pattern.**
Adding a new method (Hurst, transfer entropy, etc.) requires understanding 1,837 lines. Domain scientists with 20 lines of math cannot contribute.

**Problem 4: Univariate/multivariate split.**
Separate classes duplicating concepts. No shared interface.

**Problem 5: Deep learning special-cased.**
TensorFlow is the only optional dep pattern. No general mechanism for heavy optional deps.

### Proposed Architecture

```
ewstools/
├── __init__.py              Public API
├── core.py                  TimeSeries + MultiTimeSeries (thin orchestrator)
├── harness.py               Rolling-window engine (extracted, shared)
├── registry.py              Indicator plugin registry (auto-discovery, status metadata)
├── indicators/
│   ├── __init__.py          Auto-discovers plugins across all domain packs
│   ├── _base.py             Protocol class (name, domain, status, compute)
│   ├── core/                PRODUCTION — universal criticality indicators
│   │   ├── variance.py      Variance, std, CV
│   │   ├── autocorrelation.py  Lag-1 AC, autocovariance
│   │   ├── moments.py       Skewness, kurtosis
│   │   ├── entropy.py       Sample, spectral, permutation entropy
│   │   ├── spectral.py      Power spectrum, Smax, spectral reddening
│   │   └── dfa.py           Detrended fluctuation analysis
│   ├── ecology/             Domain pack — BETA
│   ├── climate/             Domain pack — BETA
│   ├── cardiac/             Domain pack — BETA
│   ├── thermoacoustic/      Domain pack — UNVERIFIED
│   ├── finance/             Domain pack — UNVERIFIED
│   └── [domain]/            ← new domain = new directory, done
├── multivariate/
│   ├── covariance.py        Eigenvalue-based EWS
│   ├── correlation.py       Cross-correlation EWS
│   └── [new_method].py
├── classifiers/
│   ├── dl_base.py           Base for DL classifiers (optional deps)
│   └── tf_classifier.py     TensorFlow implementation
├── viz/
│   ├── plotly_backend.py    Current visualization (decoupled)
│   └── [alt_backend].py     Matplotlib, altair, etc.
├── cross_domain/            Cross-domain analysis (Year 2-3)
│   ├── compare.py           Run indicators across domain benchmarks
│   ├── convergence.py       Domain correlation matrix
│   └── raf.py               Reflexive autocatalytic structure in method space
└── detrend.py               Detrending methods
```

### Plugin Protocol — Domain-Organized Criticality Math

```python
class Indicator(Protocol):
    name: str
    domain: str                    # "core" | "ecology" | "climate" | "cardiac" | ...
    status: Literal["unverified", "beta", "production"]
    is_rolling: bool

    def compute(self, series: np.ndarray, **kwargs) -> np.ndarray:
        ...

    @property
    def citation(self) -> str:     # Paper where this method was introduced/validated
        ...
```

**Domain packs:** Each domain is a plugin directory with its own maturity status:

```
indicators/
├── core/              # status: PRODUCTION (variance, AC, skewness — universal)
├── ecology/           # status: BETA (spatial EWS, flickering, body-size shifts)
├── climate/           # status: BETA (DFA, spectral reddening, AMOC-specific)
├── cardiac/           # status: BETA (HRV indicators, arrhythmia precursors)
├── thermoacoustic/    # status: UNVERIFIED (Sujith's combustor metrics)
├── finance/           # status: UNVERIFIED (volatility regimes, flash crash EWS)
├── epidemiology/      # status: UNVERIFIED (R0 divergence, pandemic EWS)
├── neuroscience/      # status: UNVERIFIED (seizure precursors, criticality markers)
├── power_grid/        # status: UNVERIFIED (frequency deviation, cascading failure EWS)
├── materials/         # status: UNVERIFIED (fatigue/fracture precursors)
└── paleoclimate/      # status: UNVERIFIED (proxy-based EWS, D-O event detection)
```

**Status lifecycle:** UNVERIFIED → BETA (tested on ≥2 datasets, reviewed by domain expert) → PRODUCTION (benchmarked, published, 1+ year stable). Status is per-indicator, visible in registry metadata.

**The deeper architecture:** This isn't just "EWS tools organized by domain." It's a **general-purpose criticality mathematics plugin system**. The core indicators (variance, autocorrelation, spectral metrics) work universally because critical slowing down is a mathematical theorem, not a domain fact. Domain packs add domain-specific signatures that ALSO exhibit universal structure when you look across domains.

**Cross-domain features (grant Year 2-3):**
- `ewstools.compare(indicator, domains=["ecology", "climate", "cardiac"])` — run same indicator across domain benchmark datasets, visualize convergence
- Domain correlation matrix — which indicators are structurally equivalent across domains?
- RAF-inspired analysis (optional, research-grade): measure how methods developed in one domain catalyze discoveries in others — reflexive autocatalytic structure in the method space itself

A contributor writes one file, implements `compute()`, declares their domain and status, drops it in the right directory. Registry auto-discovers. No touching core.py. A domain scientist with 20 lines of math can contribute a new EWS method to their domain pack.

### Rolling-Window Harness (extracted)

One function replaces 14× duplicated boilerplate:
```python
def apply_rolling(ts_data, indicator, rolling_window=0.25, use_residuals=True):
    series = _select_series(ts_data, use_residuals)
    rw_abs = _resolve_window(series, rolling_window)
    return series.rolling(window=rw_abs).apply(indicator.compute)
```

One place to fix bugs. One place to add features (weighted windows, adaptive windows, parallelism). Every indicator gets improvements for free.

### Backwards Compatibility

Non-breaking. All `ts.compute_var()` calls become thin wrappers delegating to new system. Deprecation warnings guide users to `ts.compute("variance")`. v3.0 adds new system + shims, v4.0 removes old methods.

## Phase 1b: User Outreach Campaign (parallel with Phase 1)

**Purpose:** Surface feature requests. Build relationships. Generate user statements for grant. Identify contract opportunities.

**Timing:** Launch once architecture document is ready to share. The document IS the outreach artifact — "here's what we're proposing, what would be most valuable to your work?"

### Target Summary (Full Details in Plan 0319b)

| Priority | Contacts | Combined accessible budget | Mechanism |
|----------|----------|---------------------------|-----------|
| $$$ | Boettiger, Lenton, Thornalley, Gommenginger | $12.6M + £5M + £5M + £11M | Contract/subaward |
| $$ | Bauch (→Kutz/Brunton), Ditlevsen | NSERC + $20M (indirect) + EU | Referral chain |
| $ (endorsement) | Scheffer, Dakos, Sujith, O'Brien | Low direct $ | Letters/statements for grant |
| Community | GitHub users, JOSS reviewers, Dylewsky | — | Feature data, user base proof |

**Key insight:** The four $$$ targets alone control >£30M in EWS-relevant funding. The architecture doc + Bury intro opens those doors. Every conversation is dual-purpose: grant material AND contract pipeline.

### Outreach Approach

Templates, per-contact strategies, tracking table, and decision tree are in **Plan 0319b** (outreach comms plan). This section covers strategic intent only.

**What We're Listening For:**
1. **Feature requests** → grant deliverables
2. **Pain points** → architecture decisions
3. **"We'd use that if..."** → user statements
4. **"We need someone to build..."** → contract opportunities
5. **"Our grant could fund..."** → subcontract slots

## Phase 2: Implementation (Pre-Grant, Unpaid)

What Bruce + Robin deliver to prove competence:

1. **Extract harness.py** — rolling-window engine
2. **Extract registry.py** — plugin discovery
3. **Convert 3-4 existing indicators** to plugin pattern
4. **One new domain plugin** — proof of concept (candidate: Hurst/R-S, or domain-specific from outreach findings)
5. **Backwards-compat shims** — existing tests pass unchanged
6. **Submit as PR(s)** — visible public contribution

**NOT in Phase 2:** Full multivariate refactor, viz separation, benchmarking suite, all domain packs. Those are what the grant funds.

## Phase 3: NSF CSSI Elements Application

### Narrative Structure

1. **What ewstools does** — universal criticality mathematics computation across 11+ domains
2. **The insight** — critical slowing down is a mathematical theorem. The same indicators work everywhere because the math is universal. But domain-specific signatures exist and nobody has systematized them.
3. **The problem** — monolithic architecture limits contribution + no benchmarking standard + no way to see cross-domain structure
4. **What we've already done** — architecture refactor working, N indicators converted, user outreach findings from 5+ domain experts
5. **What funding enables:**
   - Complete domain-organized plugin migration (11 domain packs with maturity tracking)
   - Multivariate EWS suite
   - Benchmarking framework ("ImageNet for tipping points") with per-domain datasets
   - Cross-domain analysis tools (which indicators converge across domains?)
   - Community infrastructure (contributor guide, domain-pack template, status promotion protocol)
6. **User statements** — sourced from outreach campaign (Tier 1 contacts across 5+ domains)
7. **Cross-domain impact** — one package serving ecology, climate, cardiology, finance, thermoacoustics, epidemiology, neuroscience, power grids, materials, paleoclimate. The domain-organized structure makes cross-fertilization VISIBLE and MEASURABLE.
8. **Team:** Bury (PI, PNAS/Nature Comms, cross-domain expertise), Bruce (architecture, 6 startups/4 CTO), Robin (DFA, math validation)
9. **Budget:** ~$200K/yr: Bury overhead + Bruce/Robin stipends. Specific with Bury.

### Key Selling Points

- Cross-domain is THE strength for CSSI (multi-directorate program). We don't just serve multiple domains — we make the cross-domain mathematical structure COMPUTABLE.
- "Show up with work half done" — Phase 2 proves the team can deliver
- User statements prove demand across multiple NSF directorates (BIO, GEO, MPS, ENG)
- Plugin architecture = community multiplier (domain scientists become contributors without touching core)
- Maturity status (UNVERIFIED/BETA/PROD) = responsible science. We don't oversell unvalidated methods.
- Benchmarking suite fills a gap nobody else is filling — VERIFY (£5M ARIA) is literally funded to answer "do EWS methods work?" and has no standardized evaluation infrastructure
- £81M ARIA context: UK is spending heavily on tipping point forecasting. ewstools positions US researchers to be the software standard. Fund now, be the infrastructure.
- Cross-domain convergence analysis (optional RAF-inspired tools) = novel research output FROM the infrastructure, not just infrastructure serving existing research. This is a CSSI differentiator: most proposals are pure service. Ours enables new science.

## Phase 3b: Secondary Grant Applications (Parallel)

See "Fallback + Parallel Grant Targets" section below for full table. Key parallel submissions:
- **PESOSE Phase I (~Sept 2026):** Community-building. Compatible with CSSI. Can submit both.
- **CZI EOSS Cycle 7 (~Oct 2026, if announced):** Life-sciences, cardiology-forward. Low effort if it materializes.
- **NumFOCUS Small Grant (NOW):** $5-15K for compute/travel. Apply immediately after Phase 2 starts.

## Contract Pipeline (Ongoing)

Every outreach conversation is dual-purpose. Track separately:

| Signal | Follow-up |
|--------|-----------|
| "We need someone to implement X" | "We could do that on contract. Here's our rate." |
| "Our grant has budget for software" | "We'd be happy to discuss a scope of work." |
| "We're hiring scientific programmers" | "Here's my CV. Tom Bury can speak to our work." |
| "We'd use ewstools if it had Y" | "That's on our roadmap. Want a user statement quote for the grant?" |

## Deliverables & Timeline (Anchored to Dec 1, 2026 CSSI Deadline)

| Date | Deliverable | Serves | Gate? |
|------|-------------|--------|-------|
| May 9-16 | Architecture HTML document (polished, with diagrams) | All four goals | — |
| May 16 | numpy2-compat PR resubmitted (bundled with doc link) | Credibility | — |
| May 19 | Bury call: approve architecture, discuss intros, budget, grants office | All | **GATE 1** |
| May 19-23 | Bury sends Tier 1 intros (Boettiger, Bauch first — NA timezone) | Relationships + contracts | — |
| May 26-30 | Tier 2 cold outreach (Thornalley, Gommenginger, Dakos, O'Brien) | Grant + £ contacts | — |
| June 1-20 | Calls with respondents. Feature requests. Contract signals. | Grant narrative + income | — |
| June 23-July 4 | Phase 2 implementation (harness + registry + 3-4 domain plugins) | Competence proof | — |
| July 1-15 | Collect user statements + Letters of Collaboration | Grant supplementary | **GATE 2** (need 3+) |
| July 15 | NumFOCUS Small Grant application (fund compute/travel) | Immediate $ | — |
| Aug 1 | Begin CSSI draft (Project Description) | Funding | — |
| Aug-Sept | PESOSE Phase I application (~Sept deadline, verify) | Parallel funding | — |
| Sept 22 | Full CSSI draft complete | Funding | — |
| Oct 6 | Budget finalized with UCR grants office | Funding | — |
| Nov 3 | Final draft to Bury | Funding | **GATE 3** |
| Nov 17 | UCR grants office submits | Funding | — |
| **Dec 1** | **NSF CSSI Elements submitted** | **PRIMARY GOAL** | — |
| Ongoing | Contract conversations from every outreach touch | Income | — |

## Competing Landscape (Grant Reviewers Will Ask)

| Tool | Language | Status | ewstools advantage |
|------|----------|--------|-------------------|
| earlywarnings (Dakos) | R | **DEAD.** CRAN archived+removed June 2025. Last commit Oct 2022. | ewstools is the successor. Dakos reportedly directs users here. |
| EWSmethods (O'Brien) | R | Active on CRAN | Python, DL classifiers, cross-domain. EWSmethods is R-only, ecology-focused. |
| resilience (CRAN) | R | Minimal maintenance | Active development, modern API |
| CSD Toolkit (Lever et al.) | MATLAB | Unmaintained since 2020 | Open source, free, community-driven |
| ewstools (current) | Python | Active but monolithic | We're fixing the monolithic problem |
| Custom scripts (most labs) | Various | Per-lab, unreproducible | Standardization + benchmarking |

**Key argument:** The original R earlywarnings package is now defunct (CRAN-removed). EWSmethods fills part of that gap for R users, but Python users have only ewstools. No existing tool combines (a) Python, (b) cross-domain, (c) DL classifiers, (d) plugin extensibility, (e) benchmarking suite. ewstools already has (a-c). We're adding (d-e).

**Grant framing:** ewstools is positioned to be THE standard Python EWS toolkit — a role that's vacant now that earlywarnings is dead and no Python alternative with comparable scope exists. The plugin architecture makes it the natural home for community methods. The benchmarking suite makes it the evaluation standard.

## NSF Required Sections (CSSI-Specific)

These sections are MANDATORY for CSSI Elements. Each needs content:

| Section | Status | Notes |
|---------|--------|-------|
| Project Description (15 pages max) | Planned (Phase 3) | Narrative structure above covers this |
| Broader Impacts | **NOT YET PLANNED** | See below |
| Data Management Plan (2 pages) | **NOT YET PLANNED** | See below |
| Letters of Collaboration | **NOT YET PLANNED** | Different from user statements |
| Facilities/Equipment | Trivial (Bury drafts) | UCR compute cluster |
| Budget Justification | Requires Bury input | UCR indirect rate needed |
| Current & Pending Support | Bury's responsibility | He lists his grants |
| Biographical Sketches | Bruce + Robin + Bury | NSF format, 3 pages each max |

### Broader Impacts (required, often under-developed)

- **Workforce development:** Plugin system lowers barrier → domain scientists learn software engineering patterns by contributing. Train-the-contributor model.
- **Cross-domain knowledge transfer:** Tipping point methods developed in ecology become accessible to climate scientists, cardiologists, engineers. ewstools is the Rosetta Stone.
- **Reproducibility:** Benchmarking suite → reproducible EWS research. Currently every lab reimplements from scratch, results aren't comparable.
- **Underrepresented institutions:** UCR is a Hispanic-Serving Institution (HSI). Bury's position there strengthens BI argument.
- **Open source community:** MIT license, contributor-friendly architecture, documented plugin protocol = sustainable open science infrastructure.

### Data Management Plan

- All code: MIT license, GitHub, archived on Zenodo at each release.
- Benchmarking datasets: curated from published sources, DOI'd on Figshare/Zenodo.
- No new human subjects data. No PII. No export-controlled data.
- Metadata standards: DataCite schema for datasets, CITATION.cff for software.

### Letters of Collaboration vs. User Statements

| Type | Source | Content | Format |
|------|--------|---------|--------|
| Letter of Collaboration | Active research collaborator | "I will contribute X, test Y, provide Z" | Formal letterhead, NSF boilerplate |
| User Statement | End user | "My group would benefit from X" | Informal, quoted in Project Description |

**We need BOTH.** User statements go in the narrative. Letters go in Supplementary Documents.
Target: 2-3 letters (Boettiger, Lenton, Bauch) + 3-5 user statements (broader).

## Budget Framework (Preliminary — Bury Confirms)

| Category | Year 1 | Year 2 | Year 3 | Notes |
|----------|--------|--------|--------|-------|
| PI summer salary (Bury, 1 month) | ~$15K | ~$15K | ~$15K | UCR determines |
| Senior personnel (Bruce) | ~$80K | ~$80K | ~$80K | Contractor/subaward structure TBD |
| Senior personnel (Robin) | ~$40K | ~$40K | ~$40K | Part-time, math/validation |
| Travel (conferences, user meetings) | $8K | $8K | $8K | SciPy, domain conferences |
| Computing (CI, cloud benchmarks) | $5K | $5K | $5K | GitHub Actions, AWS spot |
| Indirect costs (UCR MTDC rate ~54%) | ~$52K | ~$52K | ~$52K | Applied to modified total |
| **Total** | **~$200K** | **~$200K** | **~$200K** | Fits $600K cap |

**Critical question for Bury:** Is Bruce/Robin paid as (a) UCR employees, (b) subaward to a small entity, or (c) direct consultants? Each has different overhead implications. Option (b) may be cleanest — Bruce forms LLC, subaward has its own indirect rate (lower).

## Sustainability Plan (CSSI Requires This)

Post-funding (Year 4+), ewstools survives via:
1. **Plugin architecture = distributed maintenance.** Core is small; domain packs maintained by domain communities.
2. **Benchmarking suite becomes community standard.** Once adopted, community maintains datasets.
3. **PyOpenSci / NumFOCUS affiliation.** Apply during Year 2. Provides governance + fiscal sponsorship.
4. **Contract revenue.** Custom integrations fund continued development (the pipeline this plan builds).
5. **Bury's ongoing role.** Tenured faculty maintaining open-source tool = long-term steward.

## Technical Risks in Plugin Architecture

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Indicators needing cross-window state (e.g., DFA) | Can't use simple `.apply()` | Harness supports `compute_full(series)` path for non-rolling indicators |
| Indicators needing multiple time series (multivariate) | Single-series Protocol insufficient | Separate `MultivariateIndicator` protocol with `compute(matrix)` |
| Performance regression from indirection | Users notice slowdown | Benchmark suite catches this; tight inner loop in harness, not per-indicator |
| Plugin discovery too slow at import | Startup time increases | Lazy loading — discover on first `compute()` call, not on `import ewstools` |
| Third-party plugins with incompatible deps | Dependency hell | Entry-point based discovery (setuptools); plugins are separate packages |
| Backwards-compat shims mask bugs | Silent behavior change | Shims emit FutureWarning; test suite runs BOTH old and new paths |

## Robin's Role (Specific)

| Phase | Robin's deliverables | Hours/week |
|-------|---------------------|-----------|
| Phase 1 (Architecture) | Review math correctness of protocol. Verify DFA fits plugin pattern. | 3-5 |
| Phase 2 (Implementation) | Implement DFA plugin. Validate numerical equivalence of all converted indicators vs originals. | 8-10 |
| Phase 3 (Grant) | Write "Mathematical Validation" subsection. Review technical claims. | 3-5 |
| Post-grant (Year 1) | New indicator development. Multivariate math. Benchmarking dataset curation. | 15-20 |

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| CSSI deadline already passed | Verify immediately. If so, target next cycle (annual). Typical deadline: October. |
| Bury doesn't like architecture | It's a proposal — he reviews before implementation. Adjust to his vision. He's PI. |
| Grant rejected | Outreach + contracts + Bury recommendation already in hand. Network built regardless. Resubmit next cycle with reviewer feedback. |
| Outreach gets no responses | Bury warms Tier 1 first. Architecture doc is the credential. If 0/5 Tier 1, reassess framing with Bury. |
| Scope creep | Phase 2 is deliberately 3-4 plugins + harness only. Grant funds the rest. |
| UCR grants office slow/unresponsive | Start early. Bury identifies contact in Week 3. 6-week minimum lead time for submission. |
| Bruce/Robin payment structure unclear | Resolve in Bury call. If UCR can't pay contractors directly, form LLC for subaward. |
| Plugin architecture doesn't fit all indicators | DFA already tests this — it's non-rolling. Dual protocol (rolling + full-series) handles all cases. |
| Reviewer says "just use R earlywarnings" | Competing landscape section + DL classifiers + multivariate + benchmarking = clear differentiation. |
| Key contact (Boettiger/Lenton) declines | 10 targets across 3 tiers. Need 3 statements minimum. Redundancy built in. |

## Bury's Grant Experience

Bury has never been PI on a CSSI grant before. He's been peripheral to colleagues' CSSI applications and knows the program well, but this would be his first time leading. He's excited about it.

**Implications:**
- Bruce does the heavy lifting on grant writing (which was the plan anyway)
- Bury's colleagues who've done CSSI can advise on process and review drafts
- "Early-career PI" framing is a PLUS for NSF (shows investment developing faculty)
- UCR grants office will need lead time — don't surprise them last minute
- Bury's elite pedigree (Cambridge → Waterloo → McGill → PNAS/Nature Comms) compensates for first-time-PI concern

**Bury's specific PI responsibilities (cannot delegate):**
1. Submit through FastLane/Research.gov (UCR credentials required)
2. Budget justification sign-off (institutional authority)
3. Current & Pending Support disclosure
4. Facilities description (UCR resources)
5. Biographical Sketch (his CV in NSF format)
6. Sign-off on Data Management Plan
7. Final review authority on all sections

**What Bruce drafts for Bury's review:**
1. Project Description (15 pages) — full draft
2. Broader Impacts — full draft
3. Data Management Plan — full draft
4. Budget narrative — proposed structure, Bury adjusts rates
5. Supplementary Documents — collect and organize letters

## Architecture Doc Production Plan

**Tool:** Static HTML with embedded CSS. No framework. Served from GitHub Pages or raw link.
**Diagrams:** Mermaid (renders in GitHub markdown) + SVG exports for HTML version.
**Template model:** ewstools existing tutorials (Jupyter → HTML style, but hand-crafted for architecture).
**Length:** ~2000 words + 3-4 diagrams. NOT a paper. A proposal document.

**Structure of the HTML document:**

1. **Header:** ewstools Architecture Modernization Proposal (v0.1 — Request for Comment)
2. **Problem statement:** 4 paragraphs, with code examples showing the pain (actual snippets from core.py)
3. **Proposed architecture:** Diagram (tree structure) + plugin protocol + harness extraction
4. **Migration plan:** Versioning strategy, backwards compat guarantees
5. **Contribution guide:** "How to add a new EWS method in 20 lines"
6. **Benchmarking vision:** Brief (3 paragraphs) — detailed in grant
7. **Call to action:** "What methods does your group need? Contact us."

**Production timeline (5 working days):**
- Day 1: Structure + problem statement + code examples from actual core.py
- Day 2: Architecture diagrams (Mermaid → SVG) + proposed structure
- Day 3: Plugin protocol + harness extraction + contribution guide section
- Day 4: Benchmarking vision + migration plan + call to action
- Day 5: Polish, responsive CSS, test on mobile, spell-check, Bury-ready

## CSSI Deadline — CONFIRMED

**Deadline: December 1, 2026.** (NSF 22-632, annual cycle, confirmed via FY26 webinar Nov 18, 2025.)

**Timeline working backwards from Dec 1:**
| Date | Milestone | Days before deadline |
|------|-----------|---------------------|
| Dec 1, 2026 | **SUBMIT** | 0 |
| Nov 17 | Final Bury review + UCR grants office submission | 14 |
| Nov 3 | Complete draft to Bury for final review | 28 |
| Oct 20 | All letters of collaboration in hand | 42 |
| Oct 6 | Budget finalized with UCR grants office | 56 |
| Sept 22 | Full draft complete (all sections) | 70 |
| Sept 1 | User statements + letters collected | 91 |
| Aug 1 | Draft writing begins (Project Description) | 122 |
| July 1 | Phase 2 implementation complete (proof of competence) | 153 |
| June 1 | Outreach calls complete, feature data collected | 183 |
| May 19 | Architecture doc approved by Bury, outreach launches | 196 |
| **TODAY (May 9)** | Architecture doc in production | **206 days** |

**We have 206 days.** This is comfortable but not slack. The critical path is: architecture doc → Bury approval → outreach → statements → draft. Each depends on the prior.

## Fallback + Parallel Grant Targets

| Program | Solicitation | Amount | Deadline | Fit | Strategy |
|---------|-------------|--------|----------|-----|----------|
| **NSF PESOSE Phase I** | NSF 26-506 | $300K/2yr | ~Sept 2026 (verify) | Good | Community-building + security. Submit AFTER Phase 2 proves uptake. Complementary to CSSI (different focus). Could do BOTH. |
| **NSF PESOSE Phase II** | NSF 26-506 | $750K/3yr | ~Mar 2027 | Excellent (later) | After Phase I or equivalent demonstration |
| **CZI EOSS Cycle 7** | Unannounced | $100K-$400K/2yr | ~Oct 2026 (unverified) | Medium | Life-sciences. Cardiology framing. Monitor chanzuckerberg.com/rfa/. LOW EFFORT if it materializes. |
| NumFOCUS Small Grant | Rolling | $5K-$15K | Rolling | Easy | Funds travel/compute for Phase 2. Apply NOW. |
| NSF EAGER | Via PO | $300K/2yr | No deadline | Speculative | "High-risk, high-reward" benchmarking angle. Requires PO relationship. |
| Sloan Foundation | By invitation | Varies | N/A | Long shot | Only if Scheffer/Boettiger advocate. Don't pursue directly. |

**Dual-submission strategy:** CSSI (Dec 1) and PESOSE Phase I (~Sept) are COMPATIBLE — different programmes, different focus (development vs. community). Can submit both. This is standard NSF practice. Bury confirms with grants office.

## Open Questions (for Bury call)

**Priority A (must resolve before proceeding):**
1. Next CSSI deadline — ask his colleagues who've submitted. Also email CSSIQueries@nsf.gov.
2. Budget: what range is UCR comfortable with? What's the MTDC indirect rate? How are Bruce/Robin paid (employee vs. subaward vs. consultant)?
3. UCR grants office: what's their lead time? Who's the contact? Do they have a CSSI template?

**Priority B (inform outreach strategy):**
4. Outreach: which Tier 1 contacts should he introduce us to first? Order matters.
5. Who in his network would provide (a) Letters of Collaboration and (b) user statements? These are different.
6. OS4LS: worth a shot? Can he help frame the cardiology angle? Does he know anyone on the review panel?

**Priority C (inform implementation):**
7. Which new indicator/domain for the proof-of-concept plugin? What do HIS students need?
8. Has he seen a successful CSSI Elements application he can share as a model?
9. Does he want co-PI(s) or is solo-PI stronger for this? (Early-career = solo may be better.)
10. What's his publication pipeline? Anything forthcoming that strengthens the application?

## Intellectual Property & Licensing

- ewstools is MIT licensed. Grant-funded work remains MIT. This is a CSSI strength (open by design).
- UCR may have IP policies for grant-funded work. Bury confirms whether MIT license is compatible with UCR policy (it almost certainly is for NSF-funded open source, but verify).
- Bruce/Robin contributions pre-grant are MIT regardless. No assignment to UCR.
- If subaward structure: Bruce's LLC retains no IP. All code goes to the public repo.

## Benchmarking Framework ("ImageNet for Tipping Points")

**Why this matters:** Currently there is NO standard way to compare EWS methods. Every paper uses its own synthetic data + 1-2 real datasets. Results are not comparable across papers. This is the biggest gap in the field.

**Components:**
1. **Curated dataset collection** — real transitions from 5+ domains (ecology regime shifts, climate transitions, cardiac arrhythmia onset, market crashes, thermoacoustic instability)
2. **Synthetic data generators** — parameterized models (fold, Hopf, transcritical) with known transition points + configurable noise
3. **Standard metrics** — AUC, Kendall τ trend, lead time, false positive rate
4. **Leaderboard infrastructure** — submit a new indicator, get ranked against all others on all datasets
5. **Reproducibility guarantee** — pinned random seeds, containerized evaluation, CI-validated

**Grant deliverable framing:** "We will create the first cross-domain benchmarking suite for early warning signal methods, enabling reproducible comparison across indicators, parameters, and noise regimes."

## OS4LS LOI Specifics (June 8 Deadline)

**What an LOI contains (1-2 pages):**
- Project title
- Applicant name, institution, role
- Brief description of the project (500 words)
- Relevance to life sciences (THIS IS THE CONSTRAINT)
- Requested funding amount and duration

**Cardiology-forward framing:**
- Bury's Nature Comms 2023 paper used ewstools for cardiac arrhythmia EWS detection
- The DL classifier was literally trained on cardiac + ecological + climate data
- Reframe: "ewstools for real-time patient monitoring" — streaming API + validated classifiers
- Secondary angle: pandemic EWS (epidemiological tipping points, R0 early detection)

**Low-cost to produce:** Same architecture doc, different intro framing. 2-3 hours of Bruce's time.
**Expected outcome:** Likely rejection (life-sci framing is secondary for us). But: (a) practice writing to reviewers, (b) learn what OS4LS values, (c) if invited to full proposal, reassess.

## PR Strategy (numpy2-compat Bundle)

**Current state:** Branch `maintenance/numpy2-compat`, 3 commits ahead of upstream/main. PR #469 closed.
**Additional QC before resubmission:**
1. Run full test suite against numpy 2.0, 2.1, 2.2 (matrix in CI)
2. Verify no deprecation warnings from numpy 2.x
3. Run ewstools tutorials end-to-end (they're the real integration tests)
4. Check that codecov v4 action works (was v3 → v4 upgrade in our branch)

**Bundle strategy:**
- PR title: "Maintenance: numpy 2.x compatibility + CI modernization"
- PR description links to architecture doc: "See also: architecture modernization proposal [link]"
- This signals: "We maintain AND we design. We're serious contributors."
- Submit SAME DAY as architecture doc goes to Bury. Double signal.
