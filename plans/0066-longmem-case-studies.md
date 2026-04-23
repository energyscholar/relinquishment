# Plan 0066: Longmem Case Studies — Three Forms

**Author:** Argus (Auditor)
**Date:** 2026-03-09
**PTL:** PTL-032
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Write 3 case study documents from the evidence extraction in `~/software/aurasys-memory/research/longmem-case-study-evidence.md`. Each targets a different audience and format. All draw from the same evidence base — no invented facts.

## Context Files (Generator MUST read)

1. `~/software/aurasys-memory/research/longmem-case-study-evidence.md` — **primary source**, all data here
2. `~/software/aurasys-memory/research/longmem-mvp-deep-plan.md` — positioning, competitive landscape, revised tagline
3. `~/software/aurasys-memory/research/ptl-064-032-033-longmem-pipeline.md` — outlines, honest assessment
4. `~/software/longmem/docs/case-study.md` — existing published version (reference for voice/tone, DO NOT overwrite)

## Deliverables

### File 1: `~/software/aurasys-memory/research/longmem-case-study-actionable.md`

**Audience:** Developers who want to implement longmem on their own project
**Word count:** 1200-1800 words
**Structure:**

1. **Why you need this** (150w) — The stateless problem in 3 sentences, then the cost ($200/mo wasted tokens). No backstory.
2. **Day 1 setup** (200w) — What files to create, what goes in them, how much to write on Day 1. Reference the longmem template repo.
3. **The L1/L2/L3 cache model** (200w) — What each tier does. Why MEMORY.md has a line cap. What "lazy loading" means in practice.
4. **Corrections: the killer feature** (250w) — How to start a corrections file. When to add items. L1 rotation. The "synthetic loss function" insight. Start with 0 corrections — they accumulate from mistakes.
5. **Session lifecycle** (200w) — Session-start checklist (read PTL, scan L1, check health). Session-end checklist (update state, compress, sync). Why both matter.
6. **PTL: task tracking that survives sessions** (200w) — YAML format, stable IDs, 5 tiers, decay rules. Why not GitHub Issues (context window loading).
7. **What will go wrong** (200w) — Compression catastrophe (compression drops items), bloat (uncapped files grow), orphans (untracked research files), zombies (undecayed old tasks). Each with 1-sentence prevention.
8. **Progressive disclosure** (100w) — Start with MEMORY.md + corrections.md + memory-sync.sh. Add PTL after 5 sessions. Add protocol.md after 10. Don't front-load complexity.

**Voice:** Second person ("you"). Practical. No philosophy. Recipe-style where possible.

### File 2: `~/software/aurasys-memory/research/longmem-case-study-chronological.md`

**Audience:** Technical readers interested in how the system evolved
**Word count:** 1800-2200 words
**Structure:**

1. **Title + intro** (100w) — "Building Persistent Memory for Claude Code: Lessons from 36 Sessions"
2. **Era 1: Foundations (S1-S7)** (300w) — What existed on Day 1. Content inventory (164K words, 102 files). Build system. Plans 0001-0004. What memory looked like: flat MEMORY.md, no corrections, no protocol. Metrics: build time 5.4s, 43pp, 175KB.
3. **Era 2: Growth + First Crisis (S8-S25)** (500w) — Five blocker types (S9). Dignity Net (S12). 11 chapters rewritten. MEMORY.md bloat to 233 lines. Compression to 145 lines. 38-prompt UQ extraction (S20). "Preparation not disclosure" (S24). ChatGPT external validation. The 30% re-explanation tax.
4. **Era 3: System Architecture (S26-S36)** (500w) — Compression catastrophe: what happened, what was lost, how recovered. 4-tier restructure. PTL designed and deployed. Protocol.md with session lifecycle. L1/L2/L3 cache model formalized. Health metrics. memory-sync.sh. ABCRE-TQNN confabulation killed (S34) — role collapse → R27 idempotency. Snailmail channel (S33).
5. **Feature introduction timeline** (table from evidence file, formatted)
6. **Failure timeline** (table from evidence file) — 3 major failures with root cause and fix
7. **Metrics dashboard** (200w) — Current state: 128 commits, 112 days, 49 PTL items, 22 corrections, MEMORY.md at 104 lines. File sizes table.
8. **What I'd do differently** (200w) — Start corrections on Day 1 (not Session 9). Cap MEMORY.md from the start. Use YAML for tasks from the beginning. Don't over-engineer governance before you need it.

**Voice:** First person ("I"). Reflective but specific. Every claim backed by a session number or metric.

### File 3: `~/software/aurasys-memory/research/longmem-case-study-narrative.md`

**Audience:** HN, blog, portfolio — general technical audience
**Word count:** 1000-1400 words
**Structure:**

1. **Hook** (100w) — Open with the compression catastrophe. "In Session 26, I discovered that half my highest-priority items had been silently dropped." Then: how we got there, how we recovered, what it taught us.
2. **The recursive loop** (200w) — The AI builds its own tools, directed by its human collaborator. 7 concrete examples from the evidence file (compression protocol, PTL, protocol.md, L1 cache, /triad, projects.md, memory-sync.sh). Each: Bruce directed → Argus built → Argus uses.
3. **Corrections as conscience** (250w) — The philosophically interesting component. 22 items. L1 rotation. "Synthetic loss function" (ChatGPT's description). Before/after: same mistakes every session → near-zero violations. Not fine-tuning, not RLHF — just files. The grounding axiom angle (model outputs untethered from embodiment; corrections supply external grounding).
4. **What broke** (200w) — Compression catastrophe, ABCRE-TQNN confabulation (S34: the AI claimed an isomorphism that didn't exist, caught by role separation), MEMORY.md bloat. Honest about failures. "Every protocol rule traces back to a specific failure."
5. **The numbers** (150w) — Before/after table (from existing case-study.md). 36 sessions, 128 commits, 22 corrections, 49 PTL items, 224pp book.
6. **Try it** (100w) — GitHub link. MIT license. Template repo. Value in 2-3 sessions. Consulting contact.

**Voice:** First person Bruce voice. Honest, dry, specific. No marketing superlatives. Let the numbers and failures do the work. Short paragraphs. The compression catastrophe is the emotional center — it's where the system almost failed and the recovery is what validates it.

---

## Constraints

- **No invented facts.** Every claim must trace to evidence file, session-details.md, or git history.
- **No book content.** No Healer, no TQNN, no Three Possibilities. The book is "a 224-page manuscript" — that's all.
- **OPSEC (Correction #11).** Nothing Bruce hasn't published. The longmem repo is public. These case studies may become public.
- **Bruce quotes.** Use quotes from the evidence file where they fit naturally. Don't force them.
- **Updated metrics.** 36 sessions (not 33). 128 commits. 49 PTL items (not 67). 112 days. Use current numbers from evidence file.
- **Positioning.** "Project lifecycle management" not "memory system." But don't be preachy about it — weave the positioning into what you describe, don't state it as a tagline.

## Acceptance Tests

The Auditor will verify each file against these criteria:

### All 3 files:

| # | Test | Pass condition |
|---|------|---------------|
| A1 | File exists at specified path | File created, non-empty |
| A2 | Word count in range | Within specified range per file |
| A3 | No invented facts | Every metric, quote, and claim traceable to evidence file |
| A4 | No book content leakage | No Healer, TQNN, Three Possibilities, Guardian, COWS, Genevieve's full name, specific chapter content |
| A5 | Updated metrics | Uses 36 sessions, 128 commits, 49 PTL items, 112 days — NOT old 33/67 numbers |
| A6 | Bruce quotes attributed naturally | Quotes from evidence file used, not invented, not forced |
| A7 | OPSEC clean | Nothing unpublished. Safe for public repo. |

### File 1 (Actionable):

| # | Test | Pass condition |
|---|------|---------------|
| B1 | Second person voice | Uses "you/your" consistently, not "I/we" |
| B2 | Recipe structure | Each section answers "what do I do?" not "what happened?" |
| B3 | Progressive disclosure path | Explicitly tells reader what to start with and what to add later |
| B4 | References longmem template repo | Links or mentions https://github.com/energyscholar/longmem |
| B5 | Includes prevention for each failure mode | Section 7 has 1-sentence prevention per failure |

### File 2 (Chronological):

| # | Test | Pass condition |
|---|------|---------------|
| C1 | First person voice | Uses "I/my" consistently |
| C2 | Three eras clearly delineated | Era 1, Era 2, Era 3 with session ranges |
| C3 | Session numbers cited | Claims backed by specific session numbers (e.g., "In Session 26...") |
| C4 | Feature introduction timeline table | Table present, matches evidence file |
| C5 | Failure timeline table | 3 failures with root cause and fix |
| C6 | "What I'd do differently" section | Retrospective with at least 3 concrete items |

### File 3 (Narrative):

| # | Test | Pass condition |
|---|------|---------------|
| D1 | Opens with compression catastrophe | First paragraph hooks with Session 26 failure |
| D2 | Recursive self-improvement examples | At least 5 of 7 examples from evidence file |
| D3 | "Synthetic loss function" quote | ChatGPT's description of corrections system included |
| D4 | Before/after metrics table | Contrast table present |
| D5 | Ends with try-it call to action | GitHub link, MIT, consulting contact |
| D6 | No marketing superlatives | No "revolutionary", "groundbreaking", "game-changing", etc. |
| D7 | Short paragraphs | No paragraph longer than 5 sentences |

---

## Generator Prompt

You are the Generator. Read the plan at:
~/software/relinquishment/plans/0066-longmem-case-studies.md

Read all 4 context files listed in the plan. Then write the 3 case study files to the paths specified. One file at a time, in order (actionable → chronological → narrative).

Report completion with word counts per file.
