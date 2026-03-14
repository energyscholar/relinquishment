# Plan 0075: Free The Math — Modular Rebuild

**Repo:** `~/software/freethemath/`
**Hosting:** GitHub Pages (energyscholar/freethemath, CNAME: freethemath.org)
**Current state:** Single monolithic `index.html`, advocacy/press-kit tone, references deleted paper structures (Appendix B), says "six to nine" (now twelve)
**Target:** Modular multi-page site. Educational tone. Picks up cut paper content. Extensible by generator. Hosts data.

---

## Design Principles

1. **Criticality is one instance.** FtM is about convergent mathematics — fields independently arriving at the same math. Criticality is the first documented case. The site should frame it that way, leaving room for future cases (Fourier analysis, Bayesian inference, information theory, etc.).

2. **No polemic.** Educational and informational. Not "it should be free" advocacy. The site earns attention by being genuinely useful, not by arguing. The paper makes the case; the site explains it.

3. **Modular.** Each page is a standalone file. Generator adds a new .md file → it appears on the site. No editing a monolithic index to add content. Navigation maintained via a simple data file.

4. **Data host.** FtM hosts data and supplementary material (Ising runs, citation analysis, operator test results) that the paper references but can't include. GitHub Pages serves static files; data goes in a `data/` directory as downloadable CSV/JSON.

5. **Matches paper.** Numbers, claims, domain counts must match the FACETS submission. Update simultaneously with arXiv v2.

---

## Technical Architecture

**Jekyll on GitHub Pages** (zero-config, built-in). Content in Markdown with YAML frontmatter. GitHub Pages compiles automatically on push.

```
freethemath/
├── _config.yml              ← Jekyll config (title, description, nav)
├── _layouts/
│   └── default.html         ← Single layout with dark terminal CSS
├── _includes/
│   └── nav.html             ← Navigation partial (auto from _data/nav.yml)
├── _data/
│   └── nav.yml              ← Navigation structure (generators update this)
├── assets/
│   └── style.css            ← Extracted from current index.html
├── data/                    ← Downloadable data files
│   ├── README.md            ← What's here and how to use it
│   ├── ising_correspondence.csv    ← Ising test results (from supplementary)
│   ├── citation_analysis/
│   │   ├── period_analysis_15seed.json
│   │   ├── per_paper_stats.json
│   │   ├── cross_matrix.json
│   │   └── README.md        ← Methodology + data dictionary
│   └── operators/
│       └── abcre_test_suite.json   ← (future: ABCRE validation data)
├── index.md                 ← Landing: "What is convergent mathematics?"
├── criticality/
│   ├── index.md             ← Plain-language criticality overview
│   ├── domains.md           ← Domain-by-domain walkthroughs
│   ├── rosetta.md           ← Notation Rosetta stone (big table + explanations)
│   ├── citations.md         ← Extended citation methodology + data links
│   └── faq.md               ← Updated FAQ (de-polemicized)
├── operators/
│   ├── index.md             ← MD v3: what the operators do, why, interpretation
│   ├── definitions.md       ← Formal definitions (from old Appendix C)
│   └── ising.md             ← Correspondence test + interpretation
├── about.md                 ← Authors, contact, license, paper link
└── CNAME                    ← freethemath.org (existing)
```

### How generators add content

1. Write a new .md file in the appropriate directory (e.g., `criticality/seismology.md`)
2. Add frontmatter: `layout: default`, `title:`, `description:`
3. Add an entry to `_data/nav.yml`
4. Push. Done.

No other files need editing. The layout renders the page. The nav partial picks up the new entry.

### Data hosting

The `data/` directory serves static files via GitHub Pages. The paper's Data Availability statement can reference `https://freethemath.org/data/`. Files are downloadable JSON/CSV. Each subdirectory has a README explaining the data format.

For the Ising correspondence test: include the raw data (temperature, κ_m values, sample counts) so anyone can reproduce the table. For citation analysis: include the 15-seed period analysis, per-paper stats, and cross-citation matrix.

---

## Phase 1: Infrastructure (Jekyll setup + CSS extraction)

### 1A. Create `_config.yml`

```yaml
title: Free The Math
description: "Convergent mathematics: when multiple fields independently discover the same math."
url: https://freethemath.org
baseurl: ""
markdown: kramdown
plugins:
  - jekyll-seo-tag
```

### 1B. Extract CSS to `assets/style.css`

Take the `<style>` block from current `index.html`, put it in `assets/style.css`. Keep the dark terminal aesthetic (it's good). Minor updates:
- Remove `.appendix-note` class (no longer relevant)
- Remove `.punchline` class (polemic removed)
- Add styles for multi-page nav
- Add styles for data tables and code blocks

### 1C. Create `_layouts/default.html`

Standard HTML5 boilerplate. Links to `style.css`. Includes `nav.html`. Renders `{{ content }}`. Includes footer with paper link and search bridge text. Preserves the existing meta tags (og:, twitter:) with Jekyll variables.

### 1D. Create `_data/nav.yml`

```yaml
- title: Home
  url: /
- title: Criticality
  url: /criticality/
  children:
    - title: Plain Language
      url: /criticality/
    - title: Domain Walkthroughs
      url: /criticality/domains
    - title: Notation Rosetta Stone
      url: /criticality/rosetta
    - title: Citation Analysis
      url: /criticality/citations
    - title: FAQ
      url: /criticality/faq
- title: Operators
  url: /operators/
  children:
    - title: Overview
      url: /operators/
    - title: Formal Definitions
      url: /operators/definitions
    - title: Ising Test
      url: /operators/ising
- title: Data
  url: /data/
- title: About
  url: /about
```

### 1E. Create `_includes/nav.html`

Simple nav partial that reads `_data/nav.yml` and renders links. Highlights current page. Uses the existing accent color scheme.

**Acceptance (Phase 1):** `bundle exec jekyll serve` renders the site locally. Navigation works. CSS matches current aesthetic. No content yet (placeholder pages OK).

---

## Phase 2: Landing Page + About

### 2A. `index.md` — "What is convergent mathematics?"

This is the new framing. NOT "criticality math should be free." Instead:

> When multiple scientific fields independently discover the same mathematics, that's convergent mathematics. It happens more often than you'd expect.

Content:
- 2-3 paragraphs explaining convergent math as a concept
- Criticality as the best-documented case (link to criticality section)
- Brief mention of other potential cases (Fourier analysis, Bayesian methods — future documentation)
- "This site explains the first case in plain language, hosts the supporting data, and provides tools for practitioners and educators."
- Link to the paper

Tone: curious, educational, clean. No advocacy. No "it should be free" punchline. The name "Free The Math" already makes the point; the content doesn't need to hammer it.

### 2B. `about.md`

- Authors (Bruce, Robin) with brief credentials
- Contact info (email, LinkedIn — generator discretion on phone number)
- Paper citation (arXiv link, FACETS status when applicable)
- License: CC BY 4.0 for site content (more permissive than paper's CC BY-ND for educational reuse)
- Acknowledgment of Genevieve (accessibility architecture)
- AI disclosure (same as paper: Claude assisted with writing, all science is human-originated)

**Acceptance (Phase 2):** Landing page renders. About page renders. No polemic language on either page. Convergent math framing clear.

---

## Phase 3: Criticality Content (paper cut material + new)

### 3A. `criticality/index.md` — Plain-language overview

This replaces old Appendix B. Content from the current site's sections 2-5 (What Is This Math, The Pattern, The Cost, The Open Question) — rewritten without polemic. Plus material from the deleted Appendix B.

Structure:
1. What criticality math detects (tipping points, phase transitions)
2. Why it matters (cardiac, grid, market, ecosystem applications)
3. The convergence pattern (timeline, 6-12 fields)
4. How it was discovered to be convergent (the paper's story, briefly)
5. "For the full technical analysis, see the paper. For domain-specific details, see the walkthroughs below."

~800-1200 words. Clear, jargon-free, but not dumbed down. A journalist should be able to read this and write an accurate article.

### 3B. `criticality/domains.md` — Domain walkthroughs

One section per domain with:
- What the domain studies
- What critical phenomenon they found
- What they call it (their notation)
- How it connects to the universal pattern
- Key paper(s)

Domains to cover (matching paper's Section 2):
Physics, Complexity/SOC, Biomedical/DFA, Finance, Machine Learning, Neuroscience, Power Grids, Traffic, Climate/Thermohaline, Seismology, Linguistics, Urban Scaling

This is where the cut detail goes: Mantegna/Stanley econophysics, Kerner three-phase model, batch normalization discussion, extended HRV/Mora-Bialek debate. Material that was too detailed for the paper lives here.

~2000-3000 words total. Each domain section self-contained (~150-250 words).

### 3C. `criticality/rosetta.md` — Notation Rosetta Stone

The big table from Table 3 in the paper, but expanded with:
- Full explanations of each parameter (not just one-line descriptions)
- "If you're in [domain], you call this [X]. In [other domain], it's [Y]. They measure the same thing."
- The equivalence chain (H = α for fGn, spectral relationship)
- Worked mapping: "Here's how to translate a DFA result to a Hurst exponent"

This is the most practically useful page on the site. A practitioner moving between fields would bookmark this.

### 3D. `criticality/citations.md` — Extended citation methodology

Material cut from the paper's methodological caveats paragraph:
- Full null model description (HHI, random mixing assumption)
- Sensitivity analysis details (worst/best case bounds, merged Bio/Biomedical)
- S2 classification limitations
- The artifact explanation (why seismology/materials/linguistics show 100%)
- Links to downloadable data in `data/`

### 3E. `criticality/faq.md` — Updated FAQ

Rewrite the current FAQ. Remove polemic framing. Update:
- "Six to nine" → "six to twelve"
- Remove Appendix B reference
- Update "Why arXiv?" to note FACETS submission
- Clarify Sornette endorsement (arXiv endorsement = vouching that the work is appropriate for the archive, not endorsement of conclusions)
- Add: "What domains are you missing?" — honest answer: probably several, see Limitations
- Add: "How were these domains found?" — manual survey + AI-assisted search (honest)
- Add: "What's Metatron Dynamics?" — brief, honest, links to operators section

**Acceptance (Phase 3):** All 5 criticality pages render. No polemic language. Domain count matches paper (six to twelve). FAQ updated. Rosetta stone table has ≥10 entries matching paper's Table 3.

---

## Phase 4: Operators Content (MD v3 material)

### 4A. `operators/index.md` — What the operators do and why

NOT a formal math dump. An explanation:
- What problem MD v3 solves (analyzing relational structure in discrete systems)
- The four operators in plain language: A extracts gradients, B couples neighbors, R creates circulation, C bounds everything
- Why the ABRC ordering matters (C-last: let linear operators build structure before compression)
- What κ_m measures and what the three regimes mean
- "This is the framework that accidentally led to the convergence paper"
- Link to formal definitions and the Ising test

~500-800 words. Accessible to someone with undergraduate math.

### 4B. `operators/definitions.md` — Formal definitions

The content from old Appendix C (now in supplementary), but with MORE explanation than the paper version:
- Each operator with its equation, properties, and intuition
- The composite E operator
- κ_m (spectral and geometric formulations)
- The three regimes with physical interpretation
- Links to downloadable test data

Can include LaTeX-rendered math via MathJax (add to layout).

### 4C. `operators/ising.md` — Correspondence test

The Ising test from old Appendix A, with honest discussion:
- What was tested (2D Ising, 32×32 lattice, 200 samples)
- Results table (all three κ_m candidates peak at T_c)
- Limitations (small lattice, no error bars, T=2.4 secondary peak)
- "This is illustrative, not proof. Full statistical characterization requires larger lattices."
- Link to raw data in `data/ising_correspondence.csv`

**Acceptance (Phase 4):** All 3 operator pages render. Math renders via MathJax. Ising test page links to downloadable data. Honest limitations stated.

---

## Phase 5: Data Directory

### 5A. `data/README.md`

Overview of all hosted data. For each dataset:
- What it is
- How it was generated
- File format
- How to cite it

### 5B. Copy data files

From `~/software/criticality-paper/analysis/data/processed/`:
- `period_analysis_15seed.json`
- `per_paper_stats.json` (from 15-seed run)
- `cross_matrix.json`

From `~/software/criticality-paper/Stephenson_CrossDomainCriticality_2026_supplementary.tex`:
- Extract Ising test data to `ising_correspondence.csv`

### 5C. Data dictionary

Each JSON file gets a brief data dictionary in the README: what each field means, units, methodology reference.

**Acceptance (Phase 5):** All data files accessible at `freethemath.org/data/`. README explains each file. Paper's Data Availability statement URL resolves.

---

## Phase 6: Cleanup + Deploy

### 6A. Delete old `index.html`

Replaced by `index.md` in Phase 2.

### 6B. Update meta tags

In `_layouts/default.html`:
- og:description → convergent mathematics framing (not advocacy)
- twitter:description → same
- keywords → update to match paper's 6 keywords + "convergent mathematics"

### 6C. Test all links

Every internal link resolves. Paper arXiv link works. Data downloads work. No broken references.

### 6D. Mobile test

Site renders correctly on mobile (current CSS already has `@media` rules — verify they still work with multi-page layout).

**Acceptance (Phase 6):** Old index.html deleted. Site deploys clean to GitHub Pages. All pages render. All links work. Mobile-friendly.

---

## Red-Team Fixes (applied during planning)

### RT1. Sornette endorsement language (MODERATE)

Current site says "endorsed by Didier Sornette." ArXiv endorsement means Sornette vouched that the work is appropriate for the archive — NOT that he endorses the conclusions. The FAQ must clarify this. The about page should say "arXiv-endorsed by" not just "endorsed by."

### RT2. Phone number on public site (LOW — conscious choice)

Bruce's phone number is on the current site. Flagged for awareness. Generator should include it in about.md only if Bruce has confirmed this is intentional. If unsure, use email only.

### RT3. arXiv version sync (MODERATE)

Site must match the paper version on arXiv. When arXiv v2 goes up (FACETS version), the site must be updated simultaneously: domain count, table data, structure references. Add a version note to about.md: "This site corresponds to v2 of the paper (March 2026)."

### RT4. MathJax dependency (LOW)

Operators section needs LaTeX rendering. MathJax loads from CDN — adds ~150KB. Acceptable for pages that need it. Add MathJax only to pages with math (use a frontmatter flag `math: true` that triggers MathJax loading in the layout). Don't load it on the landing page or FAQ.

### RT5. Jekyll build on GitHub Pages (LOW)

GitHub Pages supports Jekyll natively but only certain plugins. The `jekyll-seo-tag` plugin is supported. If using other plugins, verify they're on the [GitHub Pages whitelist](https://pages.github.com/versions/). If not, switch to GitHub Actions build.

### RT6. "Free The Math" name vs. educational framing (LOW — leave for Bruce)

The name "Free The Math" has advocacy connotation. The content is now educational. This tension is probably fine — the name is memorable, the content is measured. But if a reviewer or journalist reads the name as activist, the educational content should defuse that. Generator discretion on whether to address this explicitly on the about page.

---

## Content Tone Guide (for generators)

**Do:** Explain clearly. Use concrete examples. Link to the paper for technical claims. Acknowledge uncertainty honestly. Write for a smart non-specialist.

**Don't:** Advocate. Use "should" language. Claim ownership or priority. Overstate the paper's findings. Use jargon without definition. Sound like a press release.

**Voice model:** "Here's what was found. Here's what it means. Here's the data. Draw your own conclusions."

---

## What NOT to Do

- Do not host the full paper PDF (that's arXiv's job)
- Do not duplicate paper content verbatim — rewrite for web audience
- Do not add JavaScript beyond MathJax (keep it static, fast, accessible)
- Do not add analytics/tracking (privacy, and Bruce doesn't need it)
- Do not add comments/discussion (that's what the paper's venues are for)
- Do not promise future content that isn't planned — "coming soon" sections look abandoned

---

## Estimated Effort

| Phase | Content | Sessions |
|-------|---------|----------|
| 1 | Infrastructure (Jekyll, CSS, layout, nav) | 1 |
| 2 | Landing page + About | 0.5 |
| 3 | Criticality content (5 pages, ~5000 words) | 1-2 |
| 4 | Operators content (3 pages, ~2000 words) | 1 |
| 5 | Data directory | 0.5 |
| 6 | Cleanup + deploy | 0.5 |
| **Total** | | **4-5 sessions** |

Phases 1-2 are infrastructure and can be one session. Phase 3 is the bulk — the most writing. Phases 4-6 are mechanical. Could compress to 3 sessions with a fast generator.
