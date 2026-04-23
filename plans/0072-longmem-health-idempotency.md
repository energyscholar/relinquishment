# Plan 0072: Longmem Health Vector + Idempotency Fixes

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Add health vector, tiered crash recovery, session-end idempotency guards, and mid-session checkpoint protocol to longmem. Fix install.md reproducibility gaps. All changes go into the longmem repo at `~/software/longmem/`.

## Working directory: `~/software/longmem/`

## Context: read `~/software/relinquishment/plans/0072-longmem-health-idempotency.md` (this file)

---

## Design Decisions

### Health Vector (not scalar)

Four dimensions, each 0-1, stored as `[p=X f=X v=X d=X]` in Health Metrics:

| Dim | Name | Formula | Source | Cost |
|-----|------|---------|--------|------|
| p | Pressure | `lines / 200` | `wc -l MEMORY.md` | 0 (already computed) |
| f | Freshness | `days_since_newest_violation / 30` | corrections.md dates | 0 (already loaded) |
| v | Coverage | `resolving_refs / total_refs` | File Map check | 0 (already checked) |
| d | Drift | `sessions_since_review / 10` | Health Metrics | 0 (already tracked) |

**Interpretation:** Each dimension has a healthy range. System is at criticality when all dimensions are in range.
- p: want 0.3-0.7 (too empty = subcritical, too full = supercritical)
- f: want < 0.5 (corrections recently active = system learning)
- v: want 1.0 (all refs resolve)
- d: want < 1.0 (review not overdue)

**CDC (Change Detection Code):** Store vector in Health Metrics. At next session start, compare current to stored. Any |delta| > 0.2 = regime shift. Flag to user: "Health dimension [X] shifted from A to B."

**Cost:** ~30 tokens to compute, ~20 tokens to store, ~20 tokens to compare. Total: ~70 tokens/session. No additional tool calls — all data already loaded.

**NOT included:** Adaptive thresholds. The vector INFORMS; it does not AUTOMATE. The human decides threshold changes based on trends. This prevents the oscillation risk identified in the operator audit (adaptive compression threshold = positive feedback loop).

### Tiered Crash Recovery

Three tiers, bounded, non-recursive:

```
Tier 1 (auto-repair): Fix specific problem. Count mismatch → recalculate. Broken ref → flag.
Tier 2 (git revert):  git checkout <last-sync> -- .longmem/. Max depth 1.
Tier 3 (escalate):    STOP. Tell user. Show last 5 sync commits.
```

Recursion guard: `.longmem/.recovering` flag file. If present at session start → skip to Tier 3.

### Session-End Idempotency

Guard: Before writing session summary, check if current session number already exists in MEMORY.md `## Active Sessions`. If yes, this is a double-run — skip write, proceed to sync only.

### Mid-Session Checkpoints

Guidance only, not automated. After completing a major deliverable: update MEMORY.md, run memory-sync.sh. This is the lightweight E operator. Explicitly opt-in — Claude judges when, not a timer.

---

## Phases

### Phase 1: Add health vector to protocol.md and directives.md

**`.longmem/memory/protocol.md`** — Add new Section 9 (renumber current Section 9 "Protocol Self-Limiting" to Section 12):

Insert after Section 8 (System Review):

```markdown
---

## 9. Health Vector

Compute at session end. Store in MEMORY.md Health Metrics.

**Dimensions (each 0-1):**
- **p (pressure):** `wc -l MEMORY.md / 200`. Healthy: 0.3-0.7.
- **f (freshness):** Days since newest correction violation / 30. Healthy: < 0.5. If no corrections yet: 0.
- **v (coverage):** File Map entries that resolve / total entries. Healthy: 1.0.
- **d (drift):** Sessions since last system review / 10. Healthy: < 1.0.

**Display:** `[p=0.6 f=0.3 v=1.0 d=0.4]` in Health Metrics table.

**Change detection:** Compare current vector to stored vector from last session. If any dimension shifted > 0.2, flag: "Health: [dim] shifted [old] → [new]."

**Action thresholds (inform, don't automate):**
- p > 0.9: Compression overdue. Read Section 3.
- f > 1.0: All corrections stale 30+ days. Consider rotation (Section 5).
- v < 1.0: Broken references. Fix immediately.
- d ≥ 1.0: System review overdue. Run Section 8.
```

**`.longmem/directives.md`** — Update Health Metrics Dashboard section (line 82-90). Add health vector row:

```markdown
- Health vector: `[p=X f=X v=X d=X]` — computed at session end per protocol.md Section 9
```

**`.longmem/memory/MEMORY.md`** — Add health vector row to Health Metrics table template. After the existing metrics rows, add:

```markdown
| Health vector | [p f v d] in range | [p=0.0 f=0.0 v=1.0 d=0.0] | — |
```

### Phase 2: Add tiered crash recovery to protocol.md

**`.longmem/memory/protocol.md`** — Add new Section 10:

```markdown
---

## 10. Crash Recovery (Tiered)

If session starts with errors (YAML parse failure, broken File Map refs, health vector anomaly):

**Tier 1 — Auto-repair:**
- Count mismatch: recalculate from source file
- Broken ref: remove from File Map, flag to user
- Stale metric: recompute from current state
- If fixed → resume normal startup

**Tier 2 — Git revert (if Tier 1 fails):**
1. Check for `.longmem/.recovering` — if exists, go to Tier 3
2. Create `.longmem/.recovering`
3. `git log --oneline -5 -- .longmem/` — show last 5 sync commits
4. `git checkout <most-recent-sync> -- .longmem/` — revert to stable
5. Check: did corrections.md change between stable and HEAD?
   If yes: `git diff <stable>..HEAD -- .longmem/memory/corrections.md` — preserve new corrections
6. Remove `.longmem/.recovering`
7. Resume normal startup

**Tier 3 — Escalate (if Tier 2 target also sick, or .recovering exists):**
STOP. Tell user: "Memory corrupted beyond auto-recovery. Last 5 sync commits: [list]. Please pick a restore point or investigate."

**Do NOT:** scan all diffs, attempt recursive reverts, re-execute tasks from crashed session.
```

### Phase 3: Add session-end idempotency guard

**`.longmem/memory/protocol.md`** — Modify Section 4 (Session End Protocol). Add as step 0 before existing steps:

```markdown
0. **Deduplication guard:** Check if `## Active Sessions` in MEMORY.md already contains a summary for the current session (match session number and today's date). If yes: this is a double-run. Skip to step 7 (memory-sync only).
```

**`.longmem/directives.md`** — Add to Session End Protocol section, before step 1:

```markdown
0. **Check for double-run:** If MEMORY.md already has today's session summary, skip to step 6 (sync only).
```

### Phase 4: Add mid-session checkpoint guidance

**`.longmem/memory/protocol.md`** — Add new Section 11:

```markdown
---

## 11. Mid-Session Checkpoints (Optional)

After completing a major deliverable (plan, code, analysis), consider a lightweight sync:
1. Update MEMORY.md current state (if changed)
2. Run `.longmem/scripts/memory-sync.sh`

**When to checkpoint:** After implementing a feature, writing a plan, adding corrections, completing a test suite. Not after every small edit — use judgment.

**Why:** Reduces crash blast radius. Each sync is a recovery point. More syncs = less data loss on crash.

**Cost:** ~50 tokens per checkpoint. Worth it after 30+ minutes of work.
```

### Phase 5: Fix install.md idempotency

**`install.md`** — Replace Step 1:

```markdown
1. Check installation state:
   - If `.longmem/` exists AND `.longmem/memory/MEMORY.md` exists: this is already installed. Ask user: "Longmem is already installed. Reinstall (overwrites memory), update (keeps memory), or cancel?"
   - If `.longmem/` exists but is incomplete (missing MEMORY.md): partial install detected. Remove `.longmem/` and proceed to Step 2.
   - If `.longmem/` does not exist: proceed to Step 2.
```

**`install.md`** — Fix Step 7:

```markdown
7. If .gitignore exists and contains a `.*` pattern but does NOT already contain `!.longmem/`, add `!.longmem/` on the line after the `.*` pattern
```

### Phase 6: Renumber protocol.md sections

After all additions, protocol.md sections should be:
1. Session Start Checklist
2. State Update Triggers
3. Compression Rules
4. Session End Protocol (with dedup guard)
5. Corrections Management
6. PTL Maintenance
7. Integrity Checks
8. System Review
9. Health Vector (NEW)
10. Crash Recovery (NEW)
11. Mid-Session Checkpoints (NEW)
12. Protocol Self-Limiting (was Section 9)

Verify total line count stays under 200 lines. If over, compress Section 3 (Compression Rules) — it's the longest section and has explanatory text that can be trimmed.

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| G1 | protocol.md has Section 9 (Health Vector) | `grep "## 9. Health Vector" .longmem/memory/protocol.md` |
| G2 | protocol.md has Section 10 (Crash Recovery) | `grep "## 10. Crash Recovery" .longmem/memory/protocol.md` |
| G3 | protocol.md has Section 11 (Mid-Session Checkpoints) | `grep "## 11. Mid-Session" .longmem/memory/protocol.md` |
| G4 | protocol.md has dedup guard in Section 4 | `grep -i "deduplication\|double-run" .longmem/memory/protocol.md` |
| G5 | protocol.md under 200 lines | `[ $(wc -l < .longmem/memory/protocol.md) -lt 200 ]` |
| G6 | directives.md mentions health vector | `grep "health vector\|Health vector\|\[p=" .longmem/directives.md` |
| G7 | directives.md has double-run check | `grep -i "double-run\|dedup" .longmem/directives.md` |
| G8 | MEMORY.md template has health vector row | `grep "Health vector" .longmem/memory/MEMORY.md` |
| G9 | install.md Step 1 handles existing install | `grep -i "already installed\|partial install" install.md` |
| G10 | install.md Step 7 has duplicate check | `grep "does NOT already contain" install.md` |
| G11 | protocol.md mentions .recovering flag | `grep ".recovering" .longmem/memory/protocol.md` |
| G12 | protocol.md Tier 2 has depth limit | `grep -i "tier 3\|escalate" .longmem/memory/protocol.md` |
| G13 | protocol.md Section 12 is self-limiting | `grep "## 12. Protocol Self-Limiting" .longmem/memory/protocol.md` |
| G14 | No section references old section numbers | Manually verify: cross-references to "Section N" use correct numbers |
| G15 | Test suite still passes | `bash /tmp/longmem-tests/test-longmem.sh ~/software/longmem` — all tiers pass |

One commit: "Add health vector, tiered crash recovery, session-end idempotency, mid-session checkpoints"

---

## Notes for Generator

- protocol.md is currently 177 lines. Budget for additions: ~20 lines net (to stay under 200). Achieve this by:
  - Trimming Section 3 explanatory text (lines 59-70 can be compressed to 3 lines)
  - Keeping new sections tight (no explanations, only triggers and actions)
- The health vector section in protocol.md should be ≤15 lines
- Crash recovery section should be ≤20 lines
- Mid-session checkpoints should be ≤10 lines
- Dedup guard is 2 lines added to Section 4
- All path references use `.longmem/` prefix
- Run the test suite AFTER changes to verify nothing broke

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0072-longmem-health-idempotency.md`. Apply Phases 1-6 to `~/software/longmem/`. Verify G1-G15. One commit.
