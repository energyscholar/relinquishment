# Plan 0229 — ewstools Grant Application

**Status:** DRAFT — awaiting Bruce review
**Created:** 2026-04-20
**Author:** Argus (Auditor)
**PI:** Thomas Bury (UC Riverside)
**Lead writer:** Bruce Stephenson

---

## Background

Bury confirmed grant partnership in 40-min phone call (2026-04-07). Key quote: "wants to pay Bruce+Robin for ewstools work, will provide recommendations, open to grant writing." Bruce as lead writer, Bury as PI through UC Riverside.

### Prior Research (all in aurasys-memory)

| Resource | Path |
|----------|------|
| CZI EOSS dossier | `dossiers/czi-eoss.md` |
| Bury network assessment | `research/bury-network-unlocks-2026-04-07.md` |
| EWS field landscape | `ewstools/research/ews-field-landscape.md` |
| Bury correspondence | `research/bury-correspondence.md` |
| ewstools plans 0001-0008 | `ewstools/plans/` |
| Field dependency audit | `ewstools/research/dependency-compat-audit.md` |
| User base audit | `ewstools/research/user-base-audit.md` |

---

## Target Programs (ranked by fit)

### Primary: CZI Essential Open Source Software for Science (EOSS)

- **Amount:** $100K–$400K over 2 years
- **Status:** Cycle 7 NOT yet announced. CZI restructured Feb 2026 (layoffs, Biohub consolidation). Program page active but no open deadlines.
- **Action required:** Email sciencegrants@chanzuckerberg.com to ask about Cycle 7 timeline.
- **PI path:** Bury at UC Riverside. UCR Office of Research signs off. 15% overhead cap.
- **Fit:** Excellent — JOSS-published, Python, no competing EWS package funded. Gap: biomedical framing required (CZI is biomedically focused).

### Backup: NSF CSSI Elements

- **Amount:** ~$600K over 3 years
- **PI path:** Same — Bury at UCR (US institution required)
- **Fit:** Excellent — broader scope than CZI, any science domain, no biomedical framing needed
- **Timeline:** Check current solicitation (NSF 22-632 or successor)

### Supplementary: NumFOCUS Small Development Grants

- **Amount:** Up to $10K, 3 rounds/year
- **Prerequisite:** ewstools must be NumFOCUS affiliated project
- **Value:** Stepping stone, strengthens CZI/NSF applications

---

## Phase 1: Groundwork (before any deadline opens)

**Objective:** Prepare everything that doesn't depend on a specific program deadline.

### 1.1 Program Status Inquiry

**Owner:** Bruce
**Action:** Email sciencegrants@chanzuckerberg.com asking:
1. Is a Cycle 7 planned?
2. Expected timeline?
3. Has the Biohub restructuring affected EOSS?

Also check NSF CSSI Elements current solicitation status.

### 1.2 NumFOCUS Affiliated Project Application

**Owner:** Bruce + Bury
**Action:** Apply for NumFOCUS affiliated project status for ewstools.
**Why:** Strengthens any grant application. Unlocks Small Development Grants. Signals community legitimacy.
**Requirements:** Open governance, open source (MIT — check), community engagement.

### 1.3 Metrics Snapshot

**Owner:** Bruce (Argus assists)
**Action:** Document current ewstools metrics for the application:
- GitHub: stars, forks, contributors, open/closed issues, commit frequency
- PyPI: downloads/month trend (currently ~5,200/month)
- Citations: JOSS paper (currently 11 ADS citations), PNAS 2021 citations
- Dependents: who imports ewstools?
- User geography/domain spread if available

### 1.4 Biomedical Framing Document

**Owner:** Bruce + Bury
**Action:** Write a 1-page framing of ewstools for biomedical audiences. Must-cover:
- **Clinical EWS:** ICU monitoring (sepsis onset, cardiac arrest prediction), post-surgical recovery trajectories
- **Neuroscience:** Epileptic seizure prediction, depression relapse, anesthesia transitions
- **Epidemiology:** Epidemic tipping points, vaccine hesitancy thresholds (Bauch's work)
- **Cell biology:** Cell fate decisions, differentiation tipping points
- **Cancer:** Tumor microenvironment phase transitions

This is the #1 weakness in ewstools' CZI pitch. Bury's cardiac modeling background (Glass, Bub, McGill) makes him the perfect person to co-write this.

### 1.5 Confirm Team Roles and Rates

**Owner:** Bruce + Bury
**Action:** Agree on:
- Bury: PI, % effort, salary line
- Bruce: role (contractor/consultant), rate, deliverables
- Robin: role, availability (currently in financial emergency / moving — status check needed)
- Any additional personnel (grad student? postdoc?)

---

## Phase 2: LOI Preparation (when deadline is known)

CZI EOSS uses a two-stage process. LOI first, then full application by invitation only.

### 2.1 LOI Components (CZI format)

| Component | Limit | Status |
|-----------|-------|--------|
| Work summary | 500 words | Not started |
| Value to biomedical community | 250 words | Phase 1.4 feeds this |
| Software project details | Up to 5 projects, repo URLs | ewstools GitHub ready |
| Landscape analysis | 250 words | `ews-field-landscape.md` + `earlywarnings-and-dakos.md` drafted |
| Category selection | 2 categories | TBD — likely "data analysis" + "machine learning" |
| Previous funding | list | Bury's grants at UCR |

### 2.2 Proposed Deliverables (2-year scope)

Based on Bury's 4 stated priorities + CZI evaluation criteria:

**Year 1:**
1. **Architecture modernization** — Modular plugin pattern, test coverage >80%, CI/CD pipeline
2. **Deep learning backend migration** — TensorFlow 2.x → PyTorch (broader compatibility, active development)
3. **Multivariate EWS** — Covariance eigenvalues, PCA-based indicators
4. **Documentation overhaul** — Biomedical tutorials, Jupyter notebooks, integration guides

**Year 2:**
5. **Benchmarking framework** — Standard datasets, reproducible baselines across domains (ecology, climate, cardiac, neural)
6. **Additional univariate methods** — DFA (already developed by Robin), spectral EWS, spatial indicators
7. **Cross-package interoperability** — scipy, statsmodels, scikit-learn pipeline compatibility
8. **Community building** — Contributor onboarding docs, DEI plan, annual virtual sprint

### 2.3 Budget Estimate

| Line | Year 1 | Year 2 | Total |
|------|--------|--------|-------|
| PI (Bury, 20% effort) | $35K | $35K | $70K |
| Developer/contractor (Bruce, 50% effort) | $50K | $50K | $100K |
| Contributor (Robin, 25% effort) | $25K | $25K | $50K |
| Cloud/CI/storage | $5K | $5K | $10K |
| Conference travel (2/yr) | $8K | $8K | $16K |
| UCR overhead (15%) | $18.5K | $18.5K | $37K |
| **Total** | **$141.5K** | **$141.5K** | **$283K** |

Notes:
- Within CZI range ($100K–$400K total)
- Bruce and Robin as contractors through UCR subcontract
- Rates are placeholder — need Bury's input on UCR salary scales and overhead calculation
- Could scale up to ~$350K with higher effort percentages or a grad student

---

## Phase 3: Full Application (by invitation only)

If LOI is accepted (~40-60% of LOIs advance):

### 3.1 Additional Components Required

- Detailed activities, milestones, deliverables (expand Phase 2.2)
- Complete budget with justification
- Key personnel biosketches (Bury, Bruce, Robin)
- DEI statement
- Software project metrics (Phase 1.3)
- Expected outcomes with evaluation strategies
- Institutional approval from UCR Office of Research

### 3.2 Biosketches Needed

**Bury:** Academic CV, publications, grants, teaching. Standard NSF-style biosketch.
**Bruce:** Non-standard path. Frame around: 51 years CLI experience, 6 startups (4 as CTO), arXiv paper (2601.22389), open-source contributions to ewstools (merged PRs), Reed College quantum physics.
**Robin:** Mathematical background, ABCRE work, ewstools contributions (DFA implementation).

---

## Phase 4: NSF CSSI Elements (parallel or backup)

If CZI Cycle 7 doesn't materialize, pivot to NSF CSSI Elements:

- Broader scope (any science domain — no biomedical framing needed)
- Larger budget (~$600K / 3 years)
- More formal proposal process
- Bury at UCR is perfectly positioned
- ewstools' cross-domain universality is a *strength* here, not a weakness to frame around

Key difference: NSF wants intellectual merit + broader impacts framing, not biomedical value. The arXiv paper's cross-domain convergence thesis becomes the intellectual merit argument.

---

## Acceptance Criteria

- [ ] Phase 1.1: CZI and NSF program status confirmed
- [ ] Phase 1.2: NumFOCUS application submitted
- [ ] Phase 1.3: Metrics snapshot documented
- [ ] Phase 1.4: Biomedical framing document reviewed by Bury
- [ ] Phase 1.5: Team roles, rates, and availability confirmed
- [ ] LOI drafted and reviewed by Bury before submission
- [ ] Full application completed (if invited)
- [ ] UCR Office of Research sign-off obtained

---

## Risks

| Risk | Mitigation |
|------|------------|
| CZI EOSS Cycle 7 doesn't happen | Pivot to NSF CSSI Elements (backup) |
| Robin unavailable (financial emergency) | Budget for Bruce at higher effort %; recruit Bury grad student |
| ewstools metrics too small (94 stars, 11 citations) | Emphasize growth trajectory, niche specificity, no competitor |
| Biomedical framing feels forced | Bury's cardiac modeling background makes it authentic |
| UCR overhead exceeds 15% | CZI caps at 15% — UCR must agree to reduced rate |

---

## Immediate Next Actions (for Bruce)

1. **Email CZI** — sciencegrants@chanzuckerberg.com asking about Cycle 7
2. **Email Bury** — "Ready to start on the grant. Here's my plan. What's your timeline?"
3. **Check Robin's availability** — is he able to commit to a 2-year grant?
4. **Check NSF CSSI Elements** — current solicitation status and next deadline
