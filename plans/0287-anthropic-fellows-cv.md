# Plan 0287: CV for Anthropic Fellows Program (AI Safety Track)

**Auditor:** Argus (S64)
**Status:** READY FOR GENERATOR (annealed: 4 passes, 8.5/10)
**Deadline:** 2026-05-03 EOD PST (TOMORROW)
**Output:** `/home/bruce/software/bruce_stephenson_cv/cv-anthropic-fellows.md` → PDF
**Application portal:** Greenhouse (step 1) → Constellation (step 2, real application)
**Workstream dropdown:** Select "AI Safety Fellows"
**Cohort start:** July 20, 2026

## Context

Anthropic Fellows Program, July 2026 cohort. 4-month paid fellowship ($3,850/week), compute ($15K/month), mentorship, 40%+ conversion to full-time. Track: **AI Safety Fellows.**

What they want (verbatim from posting):
- "You can code well in Python"
- "You can take ambiguous problems and make concrete progress"
- "You think clearly about hard technical questions"
- "You're excited about reducing catastrophic risks from advanced AI systems"
- "You want to transition into empirical AI safety research"
- "You don't need a PhD, prior ML experience, or published papers"
- Strong candidates from: physics, mathematics, CS, cybersecurity

Research areas: scalable oversight, adversarial robustness, model organisms, mechanistic interpretability, AI security, **model welfare**.

## CV Structure

Use `cv-prompt-engineer.md` as formatting template (tight margins, LaTeX header). One page maximum.

### Header

```
BRUCE STEPHENSON
Albany, OR 97321 | bruce@freethemath.org | (541) 250-0662
linkedin.com/in/stephensonbruce | github.com/energyscholar
AI Safety Researcher | Empirical AI Governance | Physics
```

### Section 1: AI SAFETY RESEARCH (lead section — this is what they're buying)

**Dignity Net — Empirical Sycophancy Reduction** (2026, 64 multi-hour sessions over 4 months)

Designed and deployed a three-layer governance system for Claude Code (Anthropic) agents operating under persistent memory across 64 working sessions. System comprises three orthogonal boundary conditions:

- **Triad Protocol** — execution integrity (prevents unauthorized action, scope drift, role collapse)
- **Dignity Net** — epistemic integrity (prevents sycophancy, truth erosion under social pressure). Designed by collaborator Genevieve Prentice. Five governance escalation levels with proportional response.
- **Longmem** — continuity (persistent corrections, accumulated governance decisions, cross-session learning)

**Empirical observations:** Agent shows observably reduced sycophancy compared to baseline Claude Code instances. 23 accumulated corrections persist across sessions. Governance decisions survive context window compaction. System self-maintains via health metrics and decay protocols.

**Research hypothesis (testable):** Structured epistemic governance (DN) reduces sycophancy in LLM agents more effectively than RLHF alone. Proposed test: controlled comparison of DN-governed vs ungoverned Claude Code instances on sycophancy benchmarks.

**Relevant to:** scalable oversight, model welfare (DN treats AI agents as having governance rights — not just tools), adversarial robustness.

**Available to start:** July 20, 2026.

### Section 2: PUBLICATIONS & RESEARCH

**Stephenson, B. & Macomber, R.** (2026). "Convergent Discovery of Critical Phenomena Mathematics Across Disciplines." arXiv:2601.22389. Submitted to FACETS (Royal Society of Canada), in peer review.

- Cross-domain analysis of criticality mathematics across 12 scientific fields
- Endorsed by Didier Sornette (ETH Zürich)

**Cognitive Exoskeleton Architecture** (2026). 5,500-word technical document describing AI-orchestrated workflow: plan annealing, correction-driven learning, memory with decay, OPSEC filtering, verification checklists, predictive calibration. Available on request.

### Section 3: TECHNICAL COMPETENCIES

**Python:** NumPy, SciPy, matplotlib, signal processing, Monte Carlo methods, time series analysis, statistical hypothesis testing, automated evaluation pipelines

**AI/LLM:** Claude (Opus/Sonnet/Haiku) via Claude Code CLI. Prompt engineering (chain-of-thought, few-shot, structured output). Custom agent governance protocols. 64-session production deployment.

**Security:** Former CISSP (#319668). Enterprise security training (IBM, Fortune 500). Cryptographic systems, vulnerability analysis. Cypherpunk community (1990s–2000s).

**Systems:** Python, Rust, Java, JavaScript/TypeScript, C/C++, SQL, AWS, Docker, Linux (51 years CLI, DEC-10 onwards). Git.

### Section 4: EDUCATION

**Bachelor of Arts in Physics** — Reed College, Portland, Oregon (1991)
National Merit Scholar. Quantum mechanics (Richard Crandall), statistical mechanics, computational methods.

### Section 5: PROFESSIONAL BACKGROUND (compressed)

25+ years software engineering. Six-time CTO (Symantec, FiServ, startups). Current: CTO, Metatron Dynamics Inc. Expertise: algorithm design, performance optimization, translating mathematical frameworks into production software.

- Symantec (2006–2008): Technical Lead, J2EE e-commerce, ~$1B annual revenue
- FiServ (2001–2003): Sr. Software Engineer, CUNA Best of Breed award
- Multiple CTOs (1996–2006): Enterprise and startup environments

*2016–2019: Full-time family caregiver.*

## Acceptance Criteria

1. Single page PDF
2. AI safety research section leads (not buried)
3. Dignity Net / Triad / Longmem described concretely, not abstractly
4. Testable hypothesis stated explicitly
5. Physics + cybersecurity + Python all visible in first scan
6. No mention of TQNN, Healer, guided deduction, the book, the Flat, Custodian, Aurora, Guardian, three possibilities, relinquishment, magnetosphere-as-habitat (OPSEC)
7. Email: bruce@freethemath.org (NOT energyscholar@gmail.com)
8. Build with `pandoc` + `xelatex` to PDF

## Generator Instructions

1. Read this plan
2. Create `/home/bruce/software/bruce_stephenson_cv/cv-anthropic-fellows.md`
3. Use formatting from `cv-prompt-engineer.md` (LaTeX header, tight margins)
4. Build to PDF: `cd /home/bruce/software/bruce_stephenson_cv && pandoc cv-anthropic-fellows.md -o Bruce_Stephenson_CV_anthropic_fellows_2026.pdf --pdf-engine=xelatex`
5. Report completion

## Anneal Notes

- Pass 1: Added Constellation portal note, expanded OPSEC list, specified workstream dropdown
- Pass 2: "measurably" → "observably" (honest about evidence level); added "64 multi-hour sessions over 4 months" for context; added model welfare framing; arXiv paper framed as research capability not safety research
- Pass 3: Company = Metatron Dynamics Inc. (not Relational Relativity). Sornette endorsement verifiable. Cypherpunk kept vague for OPSEC.
- Pass 4: Main risk is one-page compression. Prioritize research section, compress professional background aggressively. If space is tight, cut Cognitive Exoskeleton item — the DN description carries the weight.

## Backup: Motivation Blurb (for Constellation free-text field, if present)

"I built a working AI governance system on Claude Code and ran it for 64 sessions. The system's epistemic integrity layer (Dignity Net) observably reduces sycophancy — but I don't have the controlled experimental data to prove it. I want to design and run that experiment. The Fellows program gives me the compute, mentorship, and institutional context to turn an empirical observation into a publishable result."

## Handoff

Generator: read plan 0287 at `~/software/relinquishment/plans/0287-anthropic-fellows-cv.md`. Create the CV variant and build to PDF. One page. OPSEC: no TQNN/Healer/book/Flat/Custodian/Aurora/Guardian/relinquishment content. If Constellation portal has a free-text motivation field, use the backup blurb from this plan.
