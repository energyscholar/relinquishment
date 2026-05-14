# Carl Boettiger — Complete Dossier

**Compiled:** 2026-05-12 by Argus
**Purpose:** Preparation for technical engagement. Read his papers, learn his stack, then contribute.

---

## 1. Who He Is

**Carl Boettiger** — Associate Professor, ESPM, UC Berkeley. Tenured 2022.
Princeton Physics undergrad. DOE Computational Science Graduate Fellow. Postdoc with Alan Hastings (UC Davis).
Co-founder of rOpenSci (peer-reviewed scientific software). H-index 33, ~7,200 citations.

**Email:** cboettig@berkeley.edu
**Office:** 203 Wellman Hall, UC Berkeley
**Mail:** ESPM Dept, 130 Mulford Hall #3114, UC Berkeley, CA 94720-3114
**GitHub:** cboettig (1,014 followers, 202 repos) | boettiger-lab (org)
**Website:** carlboettiger.info

---

## 2. His Science — Reading List (Priority Order)

### READ FIRST: "The Forecast Trap" (2022)
*Ecology Letters*, 25, 1655-1664.
**Free:** [arXiv:2207.10193](https://arxiv.org/abs/2207.10193)
Demonstrates that selecting models producing the most accurate forecasts can lead to *worse* real-world outcomes. His intellectual manifesto. Reveals his deepest concern: the ML/forecasting community is optimizing the wrong objective function.

### 2. "Early Warning Signals and the Prosecutor's Fallacy" (2012)
*Proc. R. Soc. B*, 279(1748), 4734-4739.
**Free:** [arXiv:1210.1204](https://arxiv.org/abs/1210.1204)
Studying systems that transitioned introduces selection bias, inflating false-positive rates for EWS. His methodological foundation for skepticism about generic EWS. **Must read before any EWS conversation with him.**

### 3. "Tipping Points: From Patterns to Predictions" (2013)
*Nature*, 493, 157-158.
**Free:** [Nature open](https://www.nature.com/articles/493157a)
2-page Nature commentary: truly generic warning signals for tipping points are unlikely to exist. Study system-specific transitions instead. **This frames his intellectual tension with Bury's universal deep-learning approach.**

### 4. "Limits to Ecological Forecasting" (2023, with Lapeyrolerie)
*Methods in Ecology and Evolution*, 14.
**Free:** [DOI open access](https://doi.org/10.1111/2041-210X.14013)
Tests deep learning for critical transitions with uncertainty quantification. Finds the problem is fundamentally hard. **His direct response to Bury et al.'s 2021 PNAS deep learning EWS paper.**

### 5. "From Noise to Knowledge" (2018)
*Ecology Letters*, 21, 1255-1267.
Noise is not just a nuisance — it induces novel phenomena and reveals hidden information. **Reveals his physicist-level thinking about stochastic systems.** Connects to Bruce's own signal-vs-noise work in geomagnetic data.

### 6. "Biodiversity Monitoring for a Just Planetary Future" (2024)
*Science*, 383, 34-36.
**Free:** [Berkeley PDF](https://nature.berkeley.edu/BrasharesGroup/wp-content/uploads/2024/03/science.adh8874.pdf)
Biodiversity data reflect legacies of social inequity. **Reveals the values driving geo-agent** — democratizing access to conservation data.

### 7. "Building Software, Building Community" (2015, rOpenSci)
*J. Open Research Software*, 3, e8.
**Free:** [DOI open access](https://doi.org/10.5334/jors.bu)
How rOpenSci built a community of peer-reviewed scientific software. **Reveals how he thinks about software communities.** Relevant to any collaboration model.

---

## 3. His Stack — What to Learn

### Core Platform
| Component | Repo | Tech | Purpose |
|-----------|------|------|---------|
| geo-agent | boettiger-lab/geo-agent | ES modules, MapLibre GL JS, MCP | LLM-powered interactive geospatial analysis |
| mcp-data-server | boettiger-lab/mcp-data-server | Python, DuckDB, H3, Parquet/S3 | MCP server for SQL on cloud-native geospatial data |
| open-llm-proxy | boettiger-lab/open-llm-proxy | Python, uvicorn | Multi-provider LLM routing + logging |
| agent-skills | boettiger-lab/agent-skills | SKILL.md files | 15 Claude Code skill modules |

### Key Technologies to Study
- **MapLibre GL JS** — open-source map rendering (replacement for Mapbox)
- **MCP (Model Context Protocol)** — Anthropic's tool-use protocol. He runs a production MCP server.
- **DuckDB** — in-process analytical SQL database. His MCP server uses it for geospatial queries.
- **H3** — Uber's hexagonal hierarchical spatial index. His data is H3-indexed Parquet on S3.
- **PMTiles** — single-file tile archives for vector map tiles
- **jsDelivr CDN** — geo-agent serves via CDN with version pinning
- **NRP Nautilus Kubernetes** — National Research Platform. All production runs here.
- **vitest** — test framework (156 tests currently passing)

### His 15 Agent Skills
| Skill | Purpose |
|-------|---------|
| boettiger-lab-stack | Which repo owns which layer |
| cng-datasets | Cloud-native geospatial dataset processing |
| duckdb-spatial | DuckDB spatial extension gotchas |
| gdal-spatial | GDAL/OGR remote file access |
| geo-agent-training | Log analysis, root cause tracing, fix routing |
| geo-agent | App configuration |
| github-app-auth | YubiKey GitHub App authentication |
| github-rulesets | Branch protection templates |
| maplibre-expressions | MapLibre GL JS expression gotchas |
| nrp-k8s | Kubernetes deployment |
| nrp-s3 | S3 storage on NRP Ceph |
| oci-artifacts | OCI registry for large files |
| python-env | Python venv/Docker policy |
| stac-navigation | STAC catalog browsing |

### Deployed Instances (~12)
tpl-ca, tpl, biodiversity, wetlands-v2, wyoming-public-demo, ca-30x30, CBN-taskforce, bosl-high-seas, urban-biodiversity, landvote, wetlands, plus geo-agent-template.

---

## 4. Team Structure — He's Alone

| Repo | His commits | Bot commits | Other humans |
|------|------------|-------------|--------------|
| geo-agent | 240 | 46 | **0** |
| mcp-data-server | 120 | 22 | **0** |
| open-llm-proxy | 22 | 1 | **0** |
| agent-skills | 11 | 2 | **0** |

Only org member besides him: Matt Fisher (Schmidt Center), who opened one question issue and has zero commits.

**Lab members (none contribute to code):**
- Diego Ellis Soto — President's Postdoctoral Fellow (externally funded)
- Cassie Buhler — ESIIL Postdoc (NSF-funded through CU Boulder, moving to DSE Fall 2026)
- Daniela Rodriguez-Chavez — Grad student
- Abby Keller — Grad student

He handles: all code, all DevOps, all kubectl rollouts, all releases, all operational incidents. Merged 28 commits in the last 48 hours.

---

## 5. Work Patterns

- **Hours:** 9am-4pm Pacific (peak 3pm), secondary spike 8-10pm
- **Peak days:** Thursday (30 commits), Wednesday (21), Saturday (13!)
- **Commit style:** Rapid bursts (5-30 min intervals) suggesting Claude Code pair-programming
- **Average:** 2-3 commits per active day
- **Release cadence:** v3.3.0 to v3.6.1 in 3 weeks

---

## 6. Funding — Grant Gap

| Grant | Amount | Period | Status |
|-------|--------|--------|--------|
| Schmidt DSE Center | $12.6M (shared) | 2023-2028 | Active — faculty advisor, not director |
| NSF DeCODER (OAC-2209865) | $103K | 2022-2026 | Active — small sub-award |
| NSF CAREER (DBI-1942280) | $504K | 2020-2025 | **Ended** |
| NASA (055956-001) | $135K | 2022-2025 | **Ended** |
| USGS Green Crab | $175K | 2022-2025 | **Ended** |

Three grants ($813K total) ended in 2025. Neither postdoc is funded by his grants.
DSE hires research software engineers periodically (not currently hiring).

**Path to paid work:** DSE hire with Boettiger's advocacy, or CSSI sub-award through Bury.

---

## 7. Does He Want Collaborators?

**Evidence says yes:**
- AGENTS.md files are obsessively documented (written for future readers, not just himself)
- Co-founded rOpenSci (community builder by nature)
- Bot PR descriptions written for a reviewer who isn't him
- gh-agent-auth (YubiKey credentials for autonomous agents) suggests thinking about delegation
- His issue specs are multi-page engineering documents — onboarding documentation

**But:**
- Zero external contributors across all repos
- "Not currently hiring" on DSE page
- Ignored Bruce's cold email (April 3)
- Issue #132 from Matt Fisher got zero response

**Assessment:** He wants collaborators but hasn't found any at his technical level. His bar is high. Prove competence through the work, not through pitching.

---

## 8. His Claude Code Setup (What He Has vs What We Have)

| Feature | Boettiger | Bruce/Argus |
|---------|-----------|-------------|
| CLAUDE.md | Single-line `@AGENTS.md` redirect | 200+ line governance document |
| Role separation | None | Auditor/Generator with authorization gates |
| Memory persistence | None (session-scoped) | Typed memories, MEMORY.md index, SQLite cache |
| Corrections | Ad hoc prompt patches | Numbered corrections, anti-confab hot-five |
| Health monitoring | None | 4 metrics (pressure, friction, validity, drift) |
| Drift detection | None | Threshold-triggered actions |
| Truth governance | None (mcp-data-server incident) | Dignity Net, 6 graduated levels |
| Skills | 15 SKILL.md files, no versioning | Checksummed flat files, protocol.md |
| Planning | None | Plan files with phases, acceptance criteria |
| Agent contributor | 22% of mcp-data-server commits | Argus co-author |

---

## 9. Known Bugs (Verified in Source)

### 1. XSS in addMarkdown (chat-ui.js:693)
`el.innerHTML = marked.parse(md)` — no DOMPurify. Also line 561 (tool reasoning). Real security vulnerability.

### 2. setStyle success masking (map-manager.js:703)
Returns `{success: true}` even when all property updates failed. Open issue #161.

### 3. listTools timeout never recovers (main.js:217)
Comment says "will retry on first use" but no retry logic exists. 4 of 5 MCP tools permanently lost. Issue #206 (filed today).

### 4. parseEmbeddedToolCalls (agent.js:341)
Complex regex XML parser with zero test coverage.

---

## 10. His Active TODO List (Last 2 Weeks)

**Urgent (filed last 48h):**
- #206 listTools timeout permanently strips MCP tools
- #205 MCP client timeout too short for large hex builds
- mcp-data-server #136 sparse raster documentation gap

**Active backlog:**
- #197 Refactor DatasetCatalog.load() to source from MCP
- #196 Add local tool to adjust layer tooltip fields
- #195 Diagnose qwen3 degenerate-200 responses
- #113 LLM streaming (blocked)
- #169 MapManager decomposition (1030+ lines)
- #159 style_by_query feature
- #130 Boot-time optimization

---

## 11. The Two-Process Incident (Key Intelligence)

**March 2026, mcp-data-server:**
1. Small LLM generated query joining on h8 only (violating h0-in-join rule)
2. Slow query → Claude misdiagnosed as "S3 DPP is broken" (wrong)
3. Claude wrote incorrect diagnosis into optimization-design-notes.md
4. Next Claude session read those notes and **tried to delete the correct rule**
5. Carl had to `git revert` to save the rule

**His fix:** Document separation + evidence standard: "A claim that a rule is wrong requires a correctly structured benchmark that violates only that rule."

**Our assessment:** Truth-governance failure. His fix is structural but reactive. No numbered corrections, no anti-confab protocol, no drift detection. He's solving it with documentation, not with a system.

---

## 12. Attitude Indicators

- **Princeton physics → ecology:** Intellectual maverick. Comfortable crossing domains.
- **"The Forecast Trap":** Willing to challenge his own field's assumptions.
- **rOpenSci:** Believes in community, peer review for code, open science.
- **"Biodiversity for a Just Planetary Future":** Values-driven. Cares about equity in data access.
- **His code quality:** High. Clean architecture, good variable names, detailed comments.
- **His issue writing:** Exhaustive. Multi-page specs with diagnosis, proposed fix, verification.
- **His response to the two-process incident:** Structural fix, honest postmortem, no blame. Good engineering culture.
- **Ignored Bruce's cold email:** Busy, not hostile. The email didn't signal "I understand your work."
