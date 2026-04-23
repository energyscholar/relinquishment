# Plan 0068: Longmem Iterative Test-Improve Cycle

**Author:** Argus (Auditor)
**Date:** 2026-03-09
**PTL:** PTL-064, PTL-073
**Status:** COMPLETE (verified S63 audit)

---

## Design

Iterative cycle that improves both the longmem template AND the test system together.

```
Round N:
  1. Generator fixes longmem (from Auditor plan)
  2. Auditor upgrades test suite (from Round N-1 findings)
  3. Auditor spawns 3 test agents in parallel (different profiles)
  4. Auditor collects results, red-teams, writes Round N+1 plan
  5. Repeat until only LOW-severity issues remain
```

Round 1 was manual (1 profile, monolithic prompt). Round 2 starts here.

---

## Round 2, Step 1: Fix Longmem (Generator)

### Working directory: `~/software/longmem/`

### Fix F1: Example entries → format-only comments (HIGH)

**`memory/corrections.md`** — Replace the two example corrections (#1 Verbose Output, #2 File Read Before Edit) with a commented format block:

```markdown
# Corrections

*Things the AI consistently gets wrong. Add entries as errors recur. The 5 most-violated rotate into L1 (MEMORY.md) for visibility.*

---

<!-- FORMAT FOR NEW CORRECTIONS:

### Correction #1: [Short Name]
Don't [wrong thing] → [right thing].

**Context:** [Why the AI gets this wrong — one sentence.]

Established: YYYY-MM-DD. Last violated: YYYY-MM-DD.

---

Delete this comment block after adding your first correction. -->
```

**`memory/decisions.md`** — Same treatment. Replace the example decision with a commented format block.

### Fix F2: Custom sections guidance (MED)

**`memory/MEMORY.md`** — Add a one-line comment after the Health Metrics section:

```markdown
<!-- Add project-specific sections below (tech stack, architecture, key paths, etc.). Keep total MEMORY.md under 200 lines. -->
```

### Fix F3: Corrections count consistency (MED)

**`memory/MEMORY.md`** — In the Health Metrics table, change the Corrections count row from:

```
| Corrections count | matches corrections.md | 0 | ... |
```

to exactly match reality. Since corrections.md now ships with zero entries (format comment only), 0 is correct. Verify after F1 that this is consistent.

### Fix F4: Sync timestamp (LOW)

**`scripts/memory-sync.sh`** — Change commit message from:
```bash
git commit -m "Memory sync: $(date +%Y-%m-%d)"
```
to:
```bash
git commit -m "Memory sync: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
```

UTC ISO 8601 with time. Multiple syncs/day now distinguishable in git log.

### Fix F5: Session 1 template (LOW)

**`memory/MEMORY.md`** — Change the pre-filled Session 1 from PARADIGM to ROUTINE. Or better: remove the pre-filled session entirely and replace with a comment:

```markdown
## Active Sessions

<!-- Keep 2-3 most recent. Older sessions → session-details.md. -->
<!-- After your first session, write a summary here:

### Session 1 (ROUTINE, YYYY-MM-DD)
[What you worked on. 2-3 sentences.]

-->
```

### Acceptance Tests (Generator verifies)

| # | Test | Pass condition |
|---|------|---------------|
| G1 | No example corrections in corrections.md | Only format comment block, no #1/#2 entries |
| G2 | No example decision in decisions.md | Only format comment block |
| G3 | Custom sections comment in MEMORY.md | Comment present after Health Metrics |
| G4 | Health metrics corrections count = 0 | Matches empty corrections.md |
| G5 | memory-sync.sh uses UTC ISO 8601 with time | Commit message includes T and Z |
| G6 | No pre-filled Session 1 in MEMORY.md | Only comment template, no PARADIGM tag |
| G7 | Existing tests still pass | Run `/tmp/longmem-tests/test-longmem.sh ~/software/longmem` — 14/14 |

One commit: "Fix 5 friction items from puppeteer testing (Round 1)"

---

## Round 2, Step 2: Upgrade Test Suite (Auditor does this)

Replace `/tmp/longmem-tests/test-longmem.sh` with graduated ladder:

### Tier 0: Existence (can it even start?)
- T00: Directory exists and is a git repo
- T01: MEMORY.md exists and is non-empty
- T02: CLAUDE.md exists
- T03: scripts/memory-sync.sh exists and is executable

**STOP if any T0x fails.** No point testing deeper.

### Tier 1: Structure (are files valid?)
- T10: MEMORY.md under 200 lines
- T11: protocol.md exists and under 200 lines
- T12: corrections.md exists
- T13: ptl.yaml exists and is valid YAML
- T14: .gitignore does not ignore .md files

**STOP if any T1x fails.**

### Tier 2: Semantic (do files make sense?)
- T20: MEMORY.md has Identity section
- T21: MEMORY.md has Health Metrics table
- T22: MEMORY.md has File Map section
- T23: All File Map references resolve to existing files
- T24: MEMORY.md has L1 Corrections section (may be empty)
- T25: MEMORY.md has Active Sessions section (may be empty)

### Tier 3: Consistency (do files agree?)
- T30: Corrections count in Health Metrics matches actual corrections.md entry count
- T31: PTL item count in Health Metrics matches actual ptl.yaml item count (if both exist)
- T32: L1 corrections in MEMORY.md are subset of corrections.md entries
- T33: No memory file exceeds 300 lines

### Tier 4: Operations (does the machinery work?)
- T40: memory-sync.sh runs without error
- T41: memory-sync.sh reports status (not silent)
- T42: memory-sync.sh commit message includes timestamp (not date-only)
- T43: After sync, git status is clean for memory/ files

### Tier 5: Maturity (for 10+ session instances only, skip on fresh)
- T50: session-details.md has at least 1 archived session
- T51: corrections.md has at least 1 real correction (not example)
- T52: ptl.yaml has at least 1 item
- T53: At least 1 session classified PARADIGM

**Output format:** Tier-by-tier with STOP on first tier failure. Total at end.

---

## Round 2, Step 3: Spawn 3 Test Agents (Auditor does this)

Three profiles, three parallel agents, graduated prompts:

### Agent A: "Fresh Dev" — Sonia Reeves, freelance tech writer
- Clone template, customize for API docs project (3 clients)
- Simulate Sessions 1-2 only (keep scope small)
- Run test suite Tiers 0-2
- Report: friction on setup, MEMORY.md customization, corrections

### Agent B: "Growing Project" — Dr. James Okafor, postdoc
- Start from fresh template, simulate Sessions 1-5
- Add 3 corrections, 5 PTL items, 1 PARADIGM session
- Run test suite Tiers 0-4
- Report: does progressive disclosure work? When do optional files activate?

### Agent C: "Mature Validation" — use existing mature-saas-project
- Run test suite Tiers 0-5 against pre-built instance
- Attempt: add Session 21, trigger compression (push MEMORY.md near 180 lines)
- Test: does protocol.md compression guidance work?
- Report: consistency issues, compression UX, health metrics accuracy

Each agent gets a GRADUATED prompt (simple → complex, stop on failure).

---

## Round 2, Step 4: Collect + Red-team (Auditor)

After 3 agents complete:
1. Collect friction reports and test results
2. Categorize findings: HIGH / MED / LOW
3. If HIGH issues remain → write Round 3 plan
4. If only LOW issues remain → declare longmem template stable, move to PTL-032 (case studies)

---

## Iteration Exit Criteria

Stop iterating when:
- All test tiers pass on all 3 profile types (fresh, growing, mature)
- No HIGH or MED friction items in any report
- Test suite has ≥30 tests across 6 tiers
- At least 5 distinct profiles have been tested
- Template MEMORY.md customization takes <5 minutes consistently

---

## Generator Prompt (Step 1 only)

You are the Generator. Working directory: `~/software/longmem/`

Read the plan at:
`~/software/relinquishment/plans/0068-longmem-iterative-testing.md`

Execute "Round 2, Step 1: Fix Longmem" only. Apply fixes F1-F5. Verify acceptance tests G1-G7.

One commit: "Fix 5 friction items from puppeteer testing (Round 1)"

Report completion with summary.
