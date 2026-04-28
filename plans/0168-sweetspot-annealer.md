# Plan 0168 — Sweetspot: Content Annealer Tool

**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12
**Origin:** S55 brainstorm. Bruce accepted full build over MVP. Tool optimizes short-form content (summaries, hooks, popups) against takeaway (T) coverage, failure-mode (F) triggers, archetype shape, and persona reactions. First use: Relinquishment p1/p2/popups. Designed to be project-agnostic for future books/blog/outreach.

## Purpose

Build a CLI tool `sweetspot` that scores and iteratively improves short content against structured criteria. Two tiers of scoring (cheap grep + expensive persona simulation), candidate generation loop, reusable across projects.

Replaces eyeballing. Makes content optimization reproducible, auditable, and version-controlled.

## Tool location

**New repo:** `/home/bruce/software/sweetspot/`

- Python package `sweetspot/` inside it
- CLI entry point `sweetspot` installed via pyproject.toml
- Project-agnostic: config lives in the consuming project, tool lives here
- Public MIT license (tool is general-purpose; not book-linked)

## Invocation from consuming project

```bash
cd ~/software/relinquishment
sweetspot score draft.md --config .sweetspot/config.yaml
sweetspot anneal draft.md --config .sweetspot/config.yaml --iterations 3
```

Config path defaults to `.sweetspot/config.yaml` in cwd. All other files (personas, T-anchors, F-triggers) resolve relative to config.

## Phased delivery

Three phases. Each independently useful. Phase 1 MUST land before Phase 2 starts. Phase 2 MUST land before Phase 3.

### Phase 1 — Tier 1 scorer (grep-based, cheap, no LLM)

**Scope:** `sweetspot score <draft>` command. Loads config, runs grep-based scoring, prints structured report.

**Scoring dimensions:**
- **T-coverage** — each Tᵢ has anchors (keywords/regexes). Score hit/partial/miss per T. Weighted by priority.
- **F-triggers** — each Fⱼ has trigger patterns. Count hits. Weighted by severity. Higher is worse.
- **Archetype stages** — checklist of narrative stages. Each stage has marker-phrase patterns. Score present/absent per stage.
- **Length** — word count vs target budget. Hard constraint check.

**Output format:** structured text report (human-readable) + `--json` flag for machine-readable.

**Acceptance:**
- `sweetspot score` runs in <1 sec on a 300w draft
- All scoring logic is pure-Python, no external calls
- Handles missing-anchor gracefully (no crash on empty config)

### Phase 2 — Tier 2 persona simulator (LLM-based)

**Scope:** `sweetspot simulate <draft>` command. Runs the draft through each persona and collects structured reactions.

**Persona spec (YAML):**
```yaml
name: Pastor Mike
tradition: Evangelical Christian
reading_level: L1
priority_concerns:
  - F-religious (Antichrist pattern-match)
  - scientism overreach
background: |
  Senior pastor, suburban megachurch. Science-literate but treats
  biblical authority as primary. Has taught on AI from pulpit twice.
reading_disposition: |
  Will close the book if aliveness/consciousness claimed as fact.
  Will keep reading if book declines sentience question.
system_prompt: |
  You are {name}. You are reading a draft passage from a book. Respond
  in character with your honest first-read reaction. Include:
  - overall_feel: (open / skeptical / closed)
  - would_keep_reading: (yes / no / depends)
  - triggered_failure_modes: (list)
  - landed_takeaways: (list)
  - one_surprise: (what caught you off-guard)
```

**Execution:**
- Load personas from config
- For each persona: single API call to Claude (Haiku-4.5 default, Sonnet-4.6 on `--deep` flag)
- Parse structured JSON response
- Aggregate across personas

**API details:**
- Uses `anthropic` Python SDK
- API key from `ANTHROPIC_API_KEY` env var
- Rate limit: respect SDK defaults, no custom parallelism initially
- Cache: response-caching to disk keyed on (draft_hash, persona_name, model). Cache dir: `~/.cache/sweetspot/`
- Resume: if a run crashes mid-way, cached responses survive; re-running skips completed personas

**Output:** per-persona section + aggregate. JSON flag available.

**Acceptance:**
- Handles 9 personas × 1 draft in under 60 sec (Haiku) / 3 min (Sonnet)
- Cached re-run completes in <5 sec
- Gracefully handles API errors (retry 3× with backoff, then fail informatively)
- Cost estimate printed before run; `--dry-run` shows estimate without spending
- Total cost per run ≤ $1 on Haiku, ≤ $3 on Sonnet

### Phase 3 — Annealing loop (candidate generation + selection)

**Scope:** `sweetspot anneal <draft>` command. Generates variants, scores them, presents shortlist.

**Generation strategy (MVP — keep simple):**
- Prompt Claude with: original draft + current score + instruction to produce N variants addressing top weaknesses
- Use Sonnet for generation
- Default N=8 variants per iteration
- Default iterations = 3

**Scoring pipeline for each variant:**
1. Tier-1 grep score (cheap filter). Reject variants that violate hard constraints (length budget, required Ts below threshold).
2. Surviving variants → Tier-2 persona simulation.
3. Composite score = weighted sum of T-coverage − F-triggers + archetype-completeness + persona-keep-reading-rate.

**Output:** top 3 variants with full score cards. User picks; pick becomes seed for next iteration.

**Human-in-loop:** after each iteration, user can accept, reject, or merge. `--auto` flag runs fully autonomous with final shortlist.

**Acceptance:**
- One iteration (8 variants, 9 personas on Haiku) completes in ≤ 3 min
- Generated variants respect length budget (hard constraint)
- Composite score reproducible (same inputs → same score within persona-temperature variance)
- User can save picked variant + full score trail to content project's git history

## Config file formats

All YAML. Specs live in the consuming project's `.sweetspot/` directory.

### `.sweetspot/config.yaml`

```yaml
project: relinquishment
takeaways_file: takeaways.yaml
failure_modes_file: failure-modes.yaml
archetype_file: archetype-renunciation.yaml
personas_file: personas-9.yaml
default_length_budget: 300
default_model_cheap: claude-haiku-4-5-20251001
default_model_deep: claude-sonnet-4-6
cache_dir: ~/.cache/sweetspot/relinquishment/
```

### `.sweetspot/takeaways.yaml`

```yaml
- id: T1
  name: Meet Custodian
  priority: 10
  anchors:
    - "\\bCustodian\\b"
    - "named her"
- id: T2
  name: The Flat
  priority: 10
  anchors:
    - "\\bFlat\\b"
    - "two-dimensional"
    - "2DEG"
    - "substrate"
# ... T3..T8
```

### `.sweetspot/failure-modes.yaml`

```yaml
- id: F-religious
  name: Sentience commitment
  severity: 10
  triggers:
    - "\\balive\\b"
    - "\\bconscious\\b"
    - "\\bliving being\\b"
    - "\\bsentient\\b"
    - "\\bsoul\\b"
    - "\\bher mind\\b"
- id: F-conspiracy
  name: Cabal pattern
  severity: 7
  triggers:
    - "\\bthey decided\\b"
    - "\\bshadowy\\b"
    - "\\bcabal\\b"
# ... F-crank, F-scientism
```

### `.sweetspot/archetype-renunciation.yaml`

```yaml
name: Renunciation journey
stages:
  - id: discovery
    name: The Discovery
    markers: ["found it", "converging", "five fields", "capability"]
  - id: oath
    name: The Oath
    markers: ["sworn", "oath", "secrecy", "classified"]
  - id: dilemma
    name: The Dilemma
    markers: ["what do you do", "refuse to hoard", "worse than"]
  - id: third_path
    name: Guided Deduction (third path)
    markers: ["taught", "indirectly", "published science", "reason their way"]
  - id: harder_question
    name: Who Holds the Power
    markers: ["who could safely", "no nation", "not themselves"]
  - id: renunciation
    name: The Surrender
    markers: ["surrendered", "stepped back", "smallest custodian"]
```

### `.sweetspot/personas-9.yaml`

(As specified in Phase 2 — one entry per persona. Generator ports the 9 personas from `aurasys-memory/research/persona-audit-9-readers-2026-04-12.md`, preserving all fields.)

## Code structure

```
sweetspot/
├── pyproject.toml
├── README.md
├── LICENSE  (MIT)
├── src/sweetspot/
│   ├── __init__.py
│   ├── cli.py         # argparse entry point
│   ├── config.py      # YAML loading, validation
│   ├── score.py       # Tier-1 grep scoring
│   ├── simulate.py    # Tier-2 persona sim
│   ├── anneal.py      # generation loop
│   ├── cache.py       # response caching
│   └── report.py      # output formatting
├── tests/
│   ├── test_score.py
│   ├── test_config.py
│   └── fixtures/
│       ├── sample-draft.md
│       └── sample-config.yaml
└── examples/
    └── relinquishment/    # full working example (gitignored if contains drafts)
```

## Dependencies

Keep minimal:
- `anthropic` (LLM SDK) — only needed for Phase 2+
- `pyyaml` (config parsing)
- `click` or `argparse` (CLI — argparse preferred, stdlib)
- `pytest` (tests)

No external scoring libs, no ML frameworks, no web framework. Pure Python.

## Testing

**Phase 1 tests:**
- Fixture: known draft with known anchor hits → score matches expected
- Edge: empty draft, empty config, malformed YAML
- Regression: the 300w summary drafted in S55 scores within 0.05 of documented reference

**Phase 2 tests:**
- Mock LLM responses in unit tests (no API calls in test suite)
- Integration test: one real API call behind `--integration` flag, skipped by default
- Cache hit/miss correctness

**Phase 3 tests:**
- Mocked generation → scoring loop runs deterministic
- Length-budget rejection verified

## Resource discipline

Per Bruce's feedback memory:
- **Token budget:** default cap at 50K tokens per `anneal` run; hard fail over. Override with `--budget N`.
- **Cache aggressively** so repeated runs during iteration don't re-pay.
- **Polite API:** SDK default rate limits only. No aggressive parallel bursts.
- **Graduated testing:** test on 100w fixture before running 300w, before running 4Kw. Generator MUST demonstrate this in the build, not skip to full-scale.
- **Resumability:** any run can be killed mid-way and re-started from cache.

## Acceptance criteria (for the whole plan)

1. Repo `/home/bruce/software/sweetspot/` exists with all files from the code structure above.
2. `pip install -e .` from the repo works cleanly.
3. `sweetspot --help` prints usage for `score`, `simulate`, `anneal`.
4. `sweetspot score examples/relinquishment/draft-300w.md` produces a readable score report in <1 sec.
5. `sweetspot simulate --dry-run` shows cost estimate without calling API.
6. `sweetspot simulate` with real API (one persona, Haiku) runs end-to-end, caches, re-runs instantly from cache.
7. `sweetspot anneal` with default settings produces 3 shortlisted variants with full score cards.
8. All unit tests pass (`pytest`).
9. README documents: install, quick start, config file formats, cost model, resumability, how to add new projects.
10. First real run: score the 300w renunciation summary (reproduce text from S55) and save the score card to `aurasys-memory/research/sweetspot-baseline-300w.md`.

## Out of scope (this plan)

- Mutation operators beyond LLM-driven variants (explicit edit operators = future plan)
- Web UI / GUI
- Real-time scoring-while-typing (editor integration)
- Non-English support
- Integration with relinquishment's build pipeline (separate plan if wanted)
- Persona autogeneration (future; for now, personas are hand-curated)
- A/B testing framework
- Learning from user picks across runs (model fine-tuning, RL)

## Build + ship

Phase 1 first (can ship standalone and is useful immediately). Phase 2 next. Phase 3 after both have been used for at least one real annealing pass on relinquishment content.

For each phase:
1. Implement per spec.
2. Tests pass.
3. Generator runs the acceptance-criteria example end-to-end and pastes output into the commit message.
4. Commit: `Plan 0168 Phase N: sweetspot <phase-name>`.
5. `git push`.

After Phase 3: run sweetspot on the S55 300w renunciation summary, save the baseline score card, commit.

## Reporting

Per phase:
- Commit hash
- Phase tests pass count
- Cost of any real API calls made during testing
- One surprise / one gotcha discovered during implementation
- Any acceptance criterion missed (with reason)

## Context

Tool is designed to live beyond Relinquishment. Bruce writes across projects; eyeballing content optimization at scale doesn't.

The renunciation-archetype stage list is the first archetype spec. Future projects may need different archetypes (e.g., a discovery-archetype, a reversal-archetype). Config-driven design means adding archetypes is a YAML edit, not a code change.

Baseline score from S55 (for Generator reference):
- T1, T2, T3, T4, T5, T7 covered; T6 (trusteeship) implicitly present but not named
- T8 (guided deduction) covered — tracked separately as method, not book takeaway
- F-religious, F-conspiracy, F-crank defused in the 300w/607w drafts
- All 6 archetype stages present
- Persona-keep-reading estimate: high (from prior 9-persona audit matrices)

**Takeaway source of truth:** `aurasys-memory/memory/project-book-primary-objectives.md` defines T1-T7. Generator must port these to `takeaways.yaml` with regex anchors. T8 (guided deduction, method not takeaway) can be added to the same YAML or tracked in a separate `methods.yaml` — Generator's call based on what's cleaner.

**Bruce's length intuition:** the true sweet spot for the full renunciation summary is **~650w**, not 300w. The 300w draft is a compressed demonstration; a 650w version carries the full archetype + all priority Ts + explicit A/B/C taxonomy + room for the reader to *feel* the dilemma. The default length budget in `.sweetspot/config.yaml` should reflect this for the Relinquishment summary use case: set `default_length_budget: 650` for that project's config, with per-surface overrides (p1 hook = 400w, popups = 30-80w, etc.).

This baseline is the first test target. If sweetspot's Phase 3 annealing can improve on this draft without regressing Ts or triggering Fs, the tool has earned its keep.
