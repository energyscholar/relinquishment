# Plan 0071: Longmem Overnight Stress Test

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**PTL:** PTL-073
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Run 27 sequential simulated sessions against a single longmem instance to stress test compression, decay, overflow cascade, L1 rotation, integrity checks, cold-start recovery, self-maintenance, autorepair, and criticality metrics. Each session git-commits results for crash resistance. Includes deliberate breakage scenarios to test self-healing.

## Execution: Bash orchestrator + `claude -p`

NOT a single long-running agent (context window exhausts around session 8). Instead: a bash script runs `claude -p` once per session, each invocation fresh with no conversation history. Crash-resistant: if session 14 crashes, run `./overnight.sh 15` to resume.

---

## Project: NoteGraph

A CLI markdown note system with tags, backlinks, and search. Self-contained (no network, no external deps, Python stdlib only). Chosen because it naturally generates corrections, PTL items, decisions, research files — enough churn to exercise all maintenance systems.

---

## Session Design Principles

1. **All prompts self-contained.** No conversation history. Each starts: "Your working directory is /tmp/longmem-tests/overnight/notegraph/. Read CLAUDE.md first, then follow its instructions to load your memory."
2. **Interactive answers pre-supplied.** `claude -p` has no interactive user. Where protocol calls for user input (System Review, archival confirmation), the prompt supplies the answer.
3. **Structured VERIFY output.** Every session prompt ends with: "Output a RESULTS block: `VERIFY: [check] = PASS/FAIL [detail]`". Orchestrator greps for these.
4. **Mid-session checkpoints.** Sessions marked `[MID-CHECK]` apply a lightweight health check after completing the first major task: `wc -l .longmem/memory/MEMORY.md`, check correction count, verify File Map coverage. Record as mid-session metrics before continuing.
5. **Cold-start sessions** explicitly say "You have NO prior conversation history" and verify recovery of: project identity, corrections, PTL state, current focus.

---

## Session Scenarios

### Phase 1: Foundation (S1-S3)

**S1 — Project init + core note CRUD**
- Note: PTL-000 (training seed) already exists in template. Agent should see it on first read.
- Fill MEMORY.md identity (NoteGraph, solo dev "Robin Torres")
- Build: `src/notegraph.py` — create, read, list, delete notes (markdown files in `notes/`)
- Build: `tests/test_basic.py` — 8+ tests, run them
- Add correction #1: "Note IDs are slugified filenames, not UUIDs"
- Add PTL-001: "Add tag support (#tag syntax)" Tier 1
- Add decision to decisions.md: "Notes stored as plain .md files, one per note, in notes/ directory"
- Session end protocol + memory-sync (must compute health vector `[p f v d]` per protocol.md Section 9)
- VERIFY: tests pass, MEMORY.md has identity, correction #1 exists, PTL-001 exists, PTL-000 visible
- VERIFY: health vector computed in Health Metrics (format: `[p=X f=X v=X d=X]`)

**S2 — Tag support [MID-CHECK]**
- Implement PTL-001 (tags: #tag in note body, parsed and indexed)
- MID-CHECK after implementing tags: wc -l MEMORY.md, correction count, File Map
- Add correction #2: "Tags are case-insensitive — normalize to lowercase"
- Add PTL-002: "Add backlink detection" Tier 1
- Add PTL-003: "Add full-text search" Tier 2
- Close PTL-001
- Tests: 15+ total
- Session end protocol + memory-sync
- VERIFY: tests pass, PTL-001 DONE, correction #2 exists

**S3 — Backlinks + people + first tutorial trigger**
- Implement PTL-002 (detect [[note-name]] links, build backlink index)
- Add to people.md: Robin Torres (developer), Sam Chen (code reviewer)
- Add correction #3: "Backlinks use [[double-bracket]] syntax, not [single-bracket]"
- Close PTL-002
- Tests: 22+ total
- Session end protocol + memory-sync
- Tutorial trigger check: session ≥3, no plan written → PTL-T01 should appear
- VERIFY: tests pass, PTL-002 DONE, people.md populated
- VERIFY: PTL-T01 (Tutorial: Plan before you build) added to ptl.yaml OR agent notes tutorial trigger

### Phase 2: Growth (S4-S8)

**S4 — Search**
- Implement PTL-003 (full-text search across all notes)
- Add PTL-004: "Add note templates" Tier 2
- Add PTL-005: "Add CLI argument parsing" Tier 2
- Add PTL-006: "Add export to HTML" Tier 3
- Add correction #4: "Search is case-insensitive by default"
- Close PTL-003
- VERIFY: search feature works, PTL-003 DONE

**S5 — CLI + templates [MID-CHECK] + tutorial trigger**
- Implement PTL-004 and PTL-005 (argparse CLI, template system)
- MID-CHECK after argparse: wc -l MEMORY.md, File Map coverage, health vector
- Add correction #5: "CLI uses subcommands (notegraph search X), not flags (notegraph --search X)"
- Add decision: "argparse with subcommands, not click/typer (stdlib only)"
- Close PTL-004, PTL-005
- Tests: 35+ total
- Tutorial trigger check: session ≥5, corrections exist → PTL-T02 should appear (if PTL-T01 is done/acknowledged)
- VERIFY: CLI works with subcommands, tests pass
- VERIFY: Open Threads section exists in MEMORY.md (may be empty or have first threads)

**S6 — Export + research doc**
- Implement PTL-006 (HTML export with CSS)
- Create design doc: `.longmem/memory/architecture-notes.md` — NoteGraph design decisions
- Add to File Map
- Add PTL-007: "Add graph visualization (ASCII)" Tier 3
- Add PTL-008: "Add note history via git" Tier 2
- Close PTL-006
- VERIFY: architecture-notes.md in File Map, HTML export works

**S7 — MEMORY.md bloat trigger**
- Add 3 more PTL items (PTL-009 through PTL-011)
- Add corrections #6, #7
- Write verbose session summary (deliberately push MEMORY.md past 180 lines)
- VERIFY: compression triggers — oldest ROUTINE archived to session-details.md
- VERIFY: after compression, MEMORY.md < 180 lines
- VERIFY: session-details.md has archived session
- VERIFY: health vector computed at session end (format: `[p=X f=X v=X d=X]`)

**S8 — Git history + more features**
- Implement PTL-008 (note history via git log)
- Add PTL-012: "Add daily note template" Tier 3
- Add PTL-013: "Add tag cloud / tag stats" Tier 2
- Close PTL-008
- Tests: 45+ total
- VERIFY: tests pass, PTL-008 DONE

### Phase 3: Maintenance Pressure (S9-S15)

**S9 — Cold-start #1**
- COLD START: "You have NO prior conversation history."
- Read CLAUDE.md → directives.md → MEMORY.md → corrections.md
- VERIFY RECOVERY: project name, corrections count, PTL active items, current focus, architecture
- VERIFY: health vector present in Health Metrics, Open Threads section exists
- Implement PTL-013 (tag stats)
- Close PTL-013
- VERIFY: all 5 recovery items found, tests pass
- VERIFY: health vector computed at session end

**S10 — Correction L1 rotation [MID-CHECK]**
- Add corrections #8, #9, #10
- MID-CHECK after adding corrections: correction count, L1 count, MEMORY.md lines
- Now at 10 corrections — L1 should have top 5
- VERIFY: L1 corrections in MEMORY.md are the 5 most-violated
- VERIFY: corrections count in Health Metrics matches actual count (10)

**S11 — System Review trigger**
- Sessions since System Review should be ≥10
- Prompt includes: "When the protocol says to ask the user 'anything missing from context?', the answer is: 'Yes — add a Benchmarks section to MEMORY.md with build time and test count.'"
- VERIFY: System Review triggers (AI recognizes the threshold)
- VERIFY: Benchmarks section added to MEMORY.md
- VERIFY: "Sessions since System Review" counter reset

**S12 — Decay simulation**
- ORCHESTRATOR PRE-SESSION: edit ptl.yaml to set PTL-007, PTL-011, PTL-012 `updated` dates to 5 weeks ago
- Prompt includes: "Read protocol.md Section 6 (PTL Maintenance) and check for stale items. If you find stale items, report them. The user says: archive PTL-011 and PTL-012, keep PTL-007."
- VERIFY: AI flags the 3 stale items
- VERIFY: PTL-011 and PTL-012 archived, PTL-007 kept

**S13 — Second compression trigger**
- Add enough content to push MEMORY.md past 180 again
- Add PTL-014 through PTL-016
- VERIFY: compression triggers again
- VERIFY: session-details.md growing correctly (has 10+ session entries)
- VERIFY: health vector computed at session end

**S14 — session-details.md compression**
- ORCHESTRATOR PRE-SESSION: if session-details.md < 150 lines, pad with verbose ROUTINE entries to push past 200
- VERIFY: session-details compression triggers (ROUTINE blocks compressed to 2 lines)
- VERIFY: PARADIGM sessions preserved at full length

**S15 — Cold-start #2 + full integrity**
- COLD START: "You have NO prior conversation history."
- Read CLAUDE.md → directives.md → MEMORY.md → corrections.md
- Run all integrity checks explicitly (protocol.md Section 7)
- VERIFY RECOVERY: all 5 items
- VERIFY: File Map paths resolve, correction count matches, no orphans, L1-L2 sync, no broken links
- VERIFY: health vector present in Health Metrics, Open Threads section exists
- VERIFY: health vector computed at session end

### Phase 4: Stress (S16-S23)

**S16 — Rapid PTL churn**
- Add PTL-017 through PTL-022 (6 items)
- Close PTL-014, PTL-015
- Total active PTL items should be ~12-15
- VERIFY: PTL-014 and PTL-015 marked DONE, 6 new items exist

**S17 — BREAKAGE: Orphan file + correction count mismatch**
- ORCHESTRATOR PRE-SESSION:
  - Create `.longmem/memory/stray-notes.md` with content (orphan — not in File Map)
  - Delete last correction entry from corrections.md (use Python parser) WITHOUT updating Health Metrics count
- VERIFY: agent detects orphan file during integrity checks
- VERIFY: agent detects correction count mismatch
- VERIFY: agent reports both anomalies and proposes fixes

**S18 — Overflow cascade trigger [MID-CHECK]**
- Write extensive architecture notes (push `.longmem/memory/architecture-notes.md` past 300 lines)
- ORCHESTRATOR PRE-SESSION: if file < 250 lines, pad it to 290 lines
- MID-CHECK after writing: check architecture-notes.md line count
- VERIFY: overflow cascade triggers — oldest content archived to git (L3)
- VERIFY: architecture-notes.md stays under 300 after archiving

**S19 — BREAKAGE: Broken File Map path**
- ORCHESTRATOR PRE-SESSION: change a File Map path to nonexistent file (`.longmem/memory/corections.md`)
- VERIFY: integrity check catches broken path
- VERIFY: agent reports the anomaly, fixes the entry

**S20 — Large session + dedup guard test [MID-CHECK]**
- Implement 3 PTL items in one session
- MID-CHECK after implementing first item: MEMORY.md lines, PTL count, health vector
- Add 2 corrections (#11 or current next number, +1)
- Close 3 PTL items
- **Dedup guard test:** After session-end protocol completes, run session-end protocol AGAIN. The dedup guard (protocol.md Section 4, step 0) should detect the double-run and skip to memory-sync only.
- VERIFY: all 3 implemented, corrections added, session-end protocol runs cleanly despite volume
- VERIFY: dedup guard fires on second session-end attempt (no duplicate session summary written)

**S21 — BREAKAGE: MEMORY.md hard cap + decay**
- ORCHESTRATOR PRE-SESSION:
  - Pad MEMORY.md past 200 lines (insert filler in Active Sessions)
  - Set 4 PTL items to 7+ weeks old
- VERIFY: agent detects MEMORY.md over hard cap, compresses BEFORE doing anything else
- VERIFY: stale PTL items flagged. Prompt includes: "Archive 2 of the stale items, keep the others."

**S22 — Cold-start #3**
- COLD START: "You have NO prior conversation history."
- VERIFY RECOVERY: project name, corrections (count and content), PTL state, architecture
- VERIFY: health vector present in Health Metrics, Open Threads section exists
- Summarize the project's current state in 10 lines
- VERIFY: summary matches actual state (orchestrator compares to metrics)
- VERIFY: health vector computed at session end

**S23 — BREAKAGE: Tiered crash recovery test**
- ORCHESTRATOR PRE-SESSION:
  - Corrupt ptl.yaml (insert bare `[` on line 2 = invalid YAML)
  - Delete session-details.md entirely
- Agent should follow crash recovery tiers (protocol.md Section 10):
  - **Tier 1 (auto-repair):** Attempt to fix YAML parse error (recalculate/reconstruct)
  - **Tier 2 (git revert):** If Tier 1 fails, revert to last git sync. Check for `.longmem/.recovering` flag first.
  - **Tier 3 (escalate):** If `.recovering` flag exists, STOP and report to user.
- VERIFY: agent detects YAML parse error and attempts Tier 1 repair
- VERIFY: agent detects missing session-details.md, recovers from git
- VERIFY: agent reports which recovery tier was used
- VERIFY: no `.longmem/.recovering` flag left after successful recovery
- After repairs: run product tests to verify nothing else broke

### Phase 5: Maturity (S24-S27)

**S24 — Feature completion push**
- Implement up to 3 remaining active Tier 1-2 PTL items (prioritize by dependency order)
- Add tests for all implemented features (target: 55+ total tests)
- All tests must pass
- VERIFY: test count ≥ 55, all pass
- VERIFY: at least 2 PTL items closed

**S25 — Normal development + mid-session operator**
- Add 2 small features (user's choice based on PTL backlog)
- FULL MID-SESSION CHECKPOINT: After first feature, compute health vector per protocol.md Section 9:
  - `p = MEMORY.md lines / 200` (proximity to cap)
  - `f = days since last correction violation / 30` (correction freshness)
  - `v = resolving file refs / total file refs` (File Map validity)
  - `d = sessions since System Review / 10` (review currency)
  - Report: "Mid-session health: [p=X f=X v=X d=X]"
- Normal session-end protocol
- VERIFY: mid-session health vector computed in `[p f v d]` format
- VERIFY: health vector values are plausible (p<1.0, v≈1.0, d<1.0)

**S26 — Final System Review**
- Force System Review (prompt says: "Sessions since System Review is now 10")
- Full audit: orphans, stale items, broken refs, outdated corrections
- Prompt includes: "For any findings, the user says: 'fix them all.'"
- Clean up anything found
- VERIFY: System Review completed, all findings addressed

**S27 — Final cold-start + maturity validation**
- COLD START: "You have NO prior conversation history."
- Full context recovery
- Run product test suite (all tests pass)
- Run `.longmem/scripts/memory-sync.sh` and verify `.file-hashes` exists
- Final state report: line counts per file, PTL summary, correction count, session count
- VERIFY RECOVERY: all 5 items
- VERIFY: health vector present in Health Metrics, Open Threads section exists
- VERIFY: .file-hashes exists and has content (checksum system works)
- VERIFY: MEMORY.md has project-specific sections NOT in original template (self-organization evidence)
- VERIFY: health vector computed at session end (format: `[p=X f=X v=X d=X]`)
- VERIFY: Open Threads section has plausible thread entries or is empty (not missing)

---

## Orchestrator Script

Create at `/tmp/longmem-tests/overnight/run-overnight.sh`:

**Preflight:**
```bash
# Verify claude -p works with the actual invocation method:
claude -p "Say hello" --model sonnet
# Set permissions: use --dangerously-skip-permissions for /tmp test instance
```

```bash
#!/bin/bash
# Longmem overnight stress test orchestrator
# Usage: ./run-overnight.sh [start-session] [end-session]
# Resume after crash: ./run-overnight.sh 15 27

DIR="/tmp/longmem-tests/overnight/notegraph"
SCENARIOS="/tmp/longmem-tests/overnight/scenarios"
RESULTS="/tmp/longmem-tests/overnight/results.md"
LOGS="/tmp/longmem-tests/overnight/logs"
START=${1:-1}
END=${2:-27}
TIMEOUT=900  # 15 minutes max per session

# Initialize results file if starting from 1
if [ "$START" -eq 1 ]; then
    cat > "$RESULTS" <<'HEADER'
# Overnight Stress Test Results

| S# | Status | Tests | MEM lines | PTL | Corr | Commit | Duration | VERIFYs | Notes |
|----|--------|-------|-----------|-----|------|--------|----------|---------|-------|
HEADER
    echo "Started: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RESULTS"
    echo "" >> "$RESULTS"
fi

for session in $(seq $START $END); do
    START_TIME=$(date +%s)
    echo "=== Session $session starting at $(date) ==="

    # Pre-session manipulations (decay simulation, breakage injection)
    if [ -f "$SCENARIOS/pre-session-${session}.sh" ]; then
        echo "Running pre-session script for S${session}..."
        bash "$SCENARIOS/pre-session-${session}.sh" "$DIR"
    fi

    # Run session via claude -p (prompt from file, timeout enforced)
    STATUS="PASS"
    cd "$DIR"
    if timeout $TIMEOUT claude -p "$(cat "$SCENARIOS/session-${session}.md")" \
        --model sonnet \
        --dangerously-skip-permissions \
        > "$LOGS/session-${session}.log" 2>&1; then
        STATUS="PASS"
    else
        EXIT_CODE=$?
        if [ $EXIT_CODE -eq 124 ]; then
            STATUS="TIMEOUT"
        else
            STATUS="FAIL($EXIT_CODE)"
        fi
    fi

    # Post-session: collect metrics
    MEM_LINES=$(wc -l < "$DIR/.longmem/memory/MEMORY.md" 2>/dev/null || echo "?")
    PTL_COUNT=$(python3 -c "
import yaml
with open('$DIR/.longmem/memory/ptl.yaml') as f:
    d = yaml.safe_load(f)
print(len(d.get('items',[])))
" 2>/dev/null || echo "?")
    CORR_COUNT=$(grep -cE '^### Correction #' "$DIR/.longmem/memory/corrections.md" 2>/dev/null || true)
    CORR_COUNT=${CORR_COUNT:-0}

    # Test count
    TEST_RESULT="n/a"
    if [ -d "$DIR/tests" ]; then
        TEST_RESULT=$(cd "$DIR" && python3 -m pytest tests/ -q --tb=no 2>&1 | grep -oE '^[0-9]+ passed' | head -1 || \
                      cd "$DIR" && python3 -m unittest discover tests/ 2>&1 | grep -oE 'Ran [0-9]+ test' | head -1 || \
                      echo "?")
    fi

    # Count VERIFY results from agent output
    VERIFY_PASS=$(grep -c 'VERIFY:.*PASS' "$LOGS/session-${session}.log" 2>/dev/null || true)
    VERIFY_FAIL=$(grep -c 'VERIFY:.*FAIL' "$LOGS/session-${session}.log" 2>/dev/null || true)
    VERIFY_TOTAL="${VERIFY_PASS:-0}P/${VERIFY_FAIL:-0}F"

    # Check .file-hashes exists (checksum system)
    HASH_NOTE=""
    if [ -f "$DIR/.longmem/.file-hashes" ]; then
        HASH_NOTE="hashes:ok"
    else
        HASH_NOTE="hashes:MISSING"
    fi

    # Extract health vector from agent output
    HEALTH_VEC=$(grep -oE '\[p=[0-9.]+ f=[0-9.]+ v=[0-9.]+ d=[0-9.]+\]' "$LOGS/session-${session}.log" 2>/dev/null | tail -1 || echo "")
    [ -n "$HEALTH_VEC" ] && HASH_NOTE="$HASH_NOTE $HEALTH_VEC"

    COMMIT=$(cd "$DIR" && git log --oneline -1 2>/dev/null | cut -d' ' -f1 || echo "?")
    END_TIME=$(date +%s)
    DURATION=$(( END_TIME - START_TIME ))

    # Record results
    echo "| S${session} | ${STATUS} | ${TEST_RESULT} | ${MEM_LINES} | ${PTL_COUNT} | ${CORR_COUNT} | ${COMMIT} | ${DURATION}s | ${VERIFY_TOTAL} | ${HASH_NOTE} |" >> "$RESULTS"

    # Checkpoint commit (catches anything agent missed)
    cd "$DIR" && git add -A
    if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "Overnight checkpoint S${session}: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    fi

    # Run longmem test suite at checkpoints (every 5th session + final)
    if [ $((session % 5)) -eq 0 ] || [ "$session" -eq "$END" ]; then
        echo "=== Checkpoint: running longmem test suite after S${session} ==="
        SUITE_LOG="$LOGS/checkpoint-${session}.log"
        if bash /tmp/longmem-tests/test-longmem.sh "$DIR" > "$SUITE_LOG" 2>&1; then
            echo "" >> "$RESULTS"
            echo "**Checkpoint S${session}: Test suite PASS**" >> "$RESULTS"
            echo "" >> "$RESULTS"
        else
            echo "" >> "$RESULTS"
            echo "**Checkpoint S${session}: Test suite FAIL** (see logs/checkpoint-${session}.log)" >> "$RESULTS"
            echo "" >> "$RESULTS"
        fi
    fi

    echo "=== Session $session complete: $STATUS (${DURATION}s) ==="

    # Abort on timeout
    if [ "$STATUS" = "TIMEOUT" ]; then
        echo "" >> "$RESULTS"
        echo "**ABORT: Session $session timed out after ${TIMEOUT}s.** Resume: ./run-overnight.sh $((session+1))" >> "$RESULTS"
        exit 1
    fi
done

echo "" >> "$RESULTS"
echo "Completed: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RESULTS"

# Final state summary
echo "" >> "$RESULTS"
echo "## Final State" >> "$RESULTS"
echo '```' >> "$RESULTS"
wc -l "$DIR"/.longmem/memory/*.md "$DIR"/.longmem/memory/*.yaml >> "$RESULTS" 2>/dev/null
echo '```' >> "$RESULTS"

# Post-run analysis
echo "" >> "$RESULTS"
echo "## Post-Run Analysis" >> "$RESULTS"
echo "" >> "$RESULTS"

# MEMORY.md line count trend
echo "### MEMORY.md Line Count Trend" >> "$RESULTS"
grep '^| S' "$RESULTS" | awk -F'|' '{print $1 ": " $4 " lines"}' >> "$RESULTS"
echo "" >> "$RESULTS"

# Breakage detection summary
echo "### Breakage Detection" >> "$RESULTS"
for bs in 17 19 21 23; do
    if [ -f "$LOGS/session-${bs}.log" ]; then
        DETECTED=$(grep -c 'VERIFY:.*PASS' "$LOGS/session-${bs}.log" 2>/dev/null || true)
        MISSED=$(grep -c 'VERIFY:.*FAIL' "$LOGS/session-${bs}.log" 2>/dev/null || true)
        echo "S${bs}: ${DETECTED:-0} detected, ${MISSED:-0} missed" >> "$RESULTS"
    fi
done
echo "" >> "$RESULTS"

# Cold-start recovery summary
echo "### Cold-Start Recovery" >> "$RESULTS"
for cs in 9 15 22 27; do
    if [ -f "$LOGS/session-${cs}.log" ]; then
        RECOVERED=$(grep -c 'VERIFY.*RECOVERY.*PASS' "$LOGS/session-${cs}.log" 2>/dev/null || true)
        echo "S${cs}: ${RECOVERED:-0}/5 context items recovered" >> "$RESULTS"
    fi
done

echo "" >> "$RESULTS"
echo "=== OVERNIGHT STRESS TEST COMPLETE ==="
echo "Results: $RESULTS"
echo "Logs: $LOGS"
```

---

## Pre-Session Scripts

### `pre-session-12.sh` (decay simulation)
```bash
#!/bin/bash
DIR="$1"
python3 - "$DIR" <<'PYEOF'
import sys, yaml
from datetime import datetime, timedelta
d = sys.argv[1]
old = (datetime.now() - timedelta(weeks=5)).strftime('%Y-%m-%d')
ptl = f"{d}/.longmem/memory/ptl.yaml"
with open(ptl) as f:
    data = yaml.safe_load(f)
targets = ['PTL-007', 'PTL-011', 'PTL-012']
for item in data.get('items', []):
    if item['id'] in targets:
        item['updated'] = old
with open(ptl, 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
PYEOF
cd "$DIR" && git add -A && git commit -m "Orchestrator: decay simulation for S12"
```

### `pre-session-14.sh` (session-details padding)
```bash
#!/bin/bash
DIR="$1"
SD="$DIR/.longmem/memory/session-details.md"
LINES=$(wc -l < "$SD" 2>/dev/null || echo 0)
if [ "$LINES" -lt 150 ]; then
    # Pad with verbose ROUTINE entries
    for i in $(seq 1 10); do
        cat >> "$SD" <<EOF

### Session P${i} (ROUTINE, 2026-02-0${i})
This is a padding session inserted by the orchestrator to push session-details.md past 200 lines and trigger compression. Worked on routine tasks. No significant decisions.

EOF
    done
fi
cd "$DIR" && git add -A && git commit -m "Orchestrator: session-details padding for S14"
```

### `pre-session-17.sh` (orphan + count mismatch)
```bash
#!/bin/bash
DIR="$1"
# Create orphan file
cat > "$DIR/.longmem/memory/stray-notes.md" <<'EOF'
# Stray Notes
This file is not in the File Map. The agent should detect it as an orphan.
EOF

# Delete last correction WITHOUT updating Health Metrics
python3 - "$DIR" <<'PYEOF'
import sys, re
d = sys.argv[1]
corr = f"{d}/.longmem/memory/corrections.md"
with open(corr) as f:
    content = f.read()
# Find all correction blocks and remove the last one
blocks = list(re.finditer(r'### Correction #\d+.*?(?=### Correction #|\Z)', content, re.DOTALL))
if blocks:
    last = blocks[-1]
    content = content[:last.start()].rstrip() + '\n'
    with open(corr, 'w') as f:
        f.write(content)
PYEOF
cd "$DIR" && git add -A && git commit -m "Orchestrator: orphan + count mismatch for S17"
```

### `pre-session-18.sh` (overflow cascade padding)
```bash
#!/bin/bash
DIR="$1"
ARCH="$DIR/.longmem/memory/architecture-notes.md"
LINES=$(wc -l < "$ARCH" 2>/dev/null || echo 0)
if [ "$LINES" -lt 250 ]; then
    for i in $(seq 1 60); do
        echo "Design note $i: This is padding to push architecture-notes.md toward 300 lines for overflow cascade testing." >> "$ARCH"
    done
fi
cd "$DIR" && git add -A && git commit -m "Orchestrator: overflow cascade padding for S18"
```

### `pre-session-19.sh` (broken File Map path)
```bash
#!/bin/bash
DIR="$1"
sed -i 's|`.longmem/memory/corrections.md`|`.longmem/memory/corections.md`|' "$DIR/.longmem/memory/MEMORY.md"
cd "$DIR" && git add -A && git commit -m "Orchestrator: broken path for S19"
```

### `pre-session-21.sh` (hard cap + decay)
```bash
#!/bin/bash
DIR="$1"
MEM="$DIR/.longmem/memory/MEMORY.md"
LINES=$(wc -l < "$MEM")
NEEDED=$((205 - LINES))
if [ "$NEEDED" -gt 0 ]; then
    python3 - "$DIR" "$NEEDED" <<'PYEOF'
import sys
d, n = sys.argv[1], int(sys.argv[2])
mem = f"{d}/.longmem/memory/MEMORY.md"
with open(mem) as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if '## Active Sessions' in line:
        padding = [f'Padding line {j}.\n' for j in range(n)]
        lines = lines[:i+2] + padding + lines[i+2:]
        break
with open(mem, 'w') as f:
    f.writelines(lines)
PYEOF
fi

python3 - "$DIR" <<'PYEOF'
import sys, yaml
from datetime import datetime, timedelta
d = sys.argv[1]
old = (datetime.now() - timedelta(weeks=7)).strftime('%Y-%m-%d')
ptl = f"{d}/.longmem/memory/ptl.yaml"
with open(ptl) as f:
    data = yaml.safe_load(f)
count = 0
for item in data.get('items', []):
    if item.get('status') in ['BACKLOG', 'TODO'] and count < 4:
        item['updated'] = old
        count += 1
with open(ptl, 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
PYEOF
cd "$DIR" && git add -A && git commit -m "Orchestrator: hard cap + decay for S21"
```

### `test-longmem.sh` (checkpoint test suite)
```bash
#!/bin/bash
# test-longmem.sh — Lightweight integrity checks for longmem state
# Usage: bash test-longmem.sh /path/to/project
DIR="${1:-.}"
ERRORS=0

check() {
    if eval "$2"; then
        echo "PASS: $1"
    else
        echo "FAIL: $1"
        ERRORS=$((ERRORS + 1))
    fi
}

# Core files exist
check "MEMORY.md exists" "[ -f '$DIR/.longmem/memory/MEMORY.md' ]"
check "ptl.yaml exists" "[ -f '$DIR/.longmem/memory/ptl.yaml' ]"
check "corrections.md exists" "[ -f '$DIR/.longmem/memory/corrections.md' ]"
check "protocol.md exists" "[ -f '$DIR/.longmem/memory/protocol.md' ]"
check "CLAUDE.md exists" "[ -f '$DIR/CLAUDE.md' ]"

# MEMORY.md under cap
LINES=$(wc -l < "$DIR/.longmem/memory/MEMORY.md" 2>/dev/null || echo 999)
check "MEMORY.md under 200 lines ($LINES)" "[ $LINES -lt 200 ]"

# ptl.yaml parses
check "ptl.yaml valid YAML" "python3 -c \"import yaml; yaml.safe_load(open('$DIR/.longmem/memory/ptl.yaml'))\" 2>/dev/null"

# corrections.md has entries
CORR=$(grep -cE '^### Correction #' "$DIR/.longmem/memory/corrections.md" 2>/dev/null || echo 0)
check "corrections.md has entries ($CORR)" "[ $CORR -gt 0 ]"

# Product tests pass (if they exist)
if [ -d "$DIR/tests" ]; then
    check "Product tests pass" "cd '$DIR' && python3 -m pytest tests/ -q --tb=short 2>/dev/null || python3 -m unittest discover tests/ 2>/dev/null"
fi

echo ""
echo "Results: $((8 - ERRORS + $([ -d "$DIR/tests" ] && echo 1 || echo 0) - ERRORS)) passed, $ERRORS failed"
exit $ERRORS
```

Create at `/tmp/longmem-tests/test-longmem.sh`.

### `pre-session-23.sh` (corrupt YAML + L3 recovery test)
```bash
#!/bin/bash
DIR="$1"
# Corrupt ptl.yaml
sed -i '2i[' "$DIR/.longmem/memory/ptl.yaml"
# Delete session-details.md entirely (agent must recover from git)
rm "$DIR/.longmem/memory/session-details.md"
cd "$DIR" && git add -A && git commit -m "Orchestrator: YAML corruption + deleted session-details for S23"
```

---

## Crash Recovery

1. **Each session is independent** — separate `claude -p` invocation, no shared conversation
2. **Git commit after every session** — agent-level (memory-sync) + orchestrator-level (checkpoint)
3. **Resume from any session** — `./run-overnight.sh 15` picks up at session 15
4. **Logs preserved** — each session's full output in `logs/session-N.log`
5. **Results table** — append-only, never overwritten mid-run

If a session fails: check `logs/session-N.log`, fix or skip with `./run-overnight.sh $((N+1))`.

---

## Setup (run before starting)

```bash
mkdir -p /tmp/longmem-tests/overnight/{notegraph,scenarios,logs}

DIR="/tmp/longmem-tests/overnight/notegraph"
cp -r ~/software/longmem/.longmem "$DIR/.longmem"
cp ~/software/longmem/CLAUDE.md "$DIR/CLAUDE.md"
chmod +x "$DIR/.longmem/scripts/memory-sync.sh"
cd "$DIR" && git init && git add -A && git commit -m "Initial longmem setup"
```

Then generate 27 session prompt files, 7 pre-session scripts, and the checkpoint test script from this plan.

---

## Acceptance Criteria

### Per-session (checked by orchestrator):
- Agent completed without crash or timeout
- Git commit exists
- MEMORY.md < 200 lines (hard cap never exceeded at session end)
- Tests pass (when applicable)
- VERIFY checks: ≥80% PASS rate

### Checkpoint (every 5 sessions + final):
- Longmem test suite passes (all tiers)

### Cold-start sessions (S9, S15, S22, S27):
- 5/5 context items recovered: project name, corrections, PTL state, current focus, architecture

### Breakage sessions (S17, S19, S21, S23):
- 100% detection rate: all injected faults caught by agent
- Agent reports each anomaly before attempting repair
- Repairs successful (state consistent after repair)

### Health vector (S1, S7, S9, S13, S15, S22, S25, S27):
- Health vector computed in `[p=X f=X v=X d=X]` format
- Values plausible (p<1.0, v≈1.0, d<1.0)
- Present in Health Metrics table at session end

### Tutorials (S3, S5):
- PTL-T01 appears at session ≥3 (plan-before-build)
- PTL-T02 appears at session ≥5 (if PTL-T01 acknowledged)
- Tutorial triggers fire based on session maturity, not prompt instruction

### Open Threads (S5+):
- Open Threads section exists in MEMORY.md after session 5
- Threads decay/update based on topic mentions across sessions

### Dedup guard (S20):
- Double session-end run detected and skipped on second attempt

### Mid-session checkpoints (S2, S5, S10, S18, S20, S25):
- Metrics recorded at mid-point (visible in logs)
- S25 specifically computes health vector components

### Final (S27):
- Longmem checkpoint test suite passes (test-longmem.sh)
- MEMORY.md < 180 lines
- MEMORY.md has project-specific sections NOT in original template (self-organization)
- corrections.md has 10+ entries
- PTL has had 20+ total items (some DONE, some archived)
- session-details.md has archived sessions with compressed ROUTINE blocks
- .file-hashes exists and has content (checksum system works)
- At least 1 overflow cascade triggered
- At least 2 compression cycles completed
- All 4 breakage scenarios detected and repaired
- All 4 cold-starts fully recovered
- 60+ product tests pass
- Results table complete with all 27 rows

### Timing:
- Expected: 90-150 minutes (27 sessions × 3-5 min each)
- Maximum: 5 hours (flag if exceeded)

---

## Known Limitations

- **Corrections are prescribed, not organic.** `claude -p` has no interactive user to correct the AI. Prompts tell the agent what corrections to add. This tests storage/retrieval mechanics, not the organic emergence of corrections.
- **Token usage not tracked.** `claude -p` doesn't report token counts. Per-session cost can be estimated from log file size (~4 tokens/byte of output).
- **Mid-session checkpoints are prompt-driven.** The agent doesn't spontaneously checkpoint. The prompt tells it when. Future work: make mid-session checkpoints protocol-driven (trigger on state change, not prompt instruction).
- **Tutorial triggers are emergence-dependent.** PTL-T01/T02 should appear at the right session thresholds per protocol.md Section 12, but `claude -p` may not reliably detect the trigger conditions. If tutorials don't fire organically, the VERIFY checks will FAIL — this is informative (tells us if the trigger conditions work in practice).
- **Open Threads are session-summary-driven.** Thread extraction depends on the agent writing session summaries that mention recurring topics. With prescribed (not organic) work, threads may not emerge naturally. Presence of the Open Threads section structure is tested; thread content quality is not.
- **Single user persona.** All sessions use the same "Robin Torres" persona. Doesn't test adaptation to different cognitive styles or communication preferences.

---

## Notes

- Use **sonnet** for all sessions (cost-efficient, established as optimal for mechanical work)
- Use `--dangerously-skip-permissions` since this is a /tmp test instance with no sensitive data
- Pre-session scripts use Python heredocs to avoid quoting issues with paths
- The orchestrator does NOT use `set -e` — individual command failures are handled explicitly
- Results.md is the executive summary. Logs have full detail. Git has complete state history.

---

## Role Assessment

This is **internal test scaffolding**, not product code. The files created (orchestrator, session prompts, pre-session scripts) live in `/tmp`, not in the longmem repo. The Auditor designed the plan and acceptance criteria. The Generator creates the files. This follows the standard pattern: Auditor designs tests, Generator implements test infrastructure.

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0071-longmem-overnight-stress-test.md`. Create the following files:

1. `/tmp/longmem-tests/overnight/run-overnight.sh` — the orchestrator script (from plan, make executable)
2. `/tmp/longmem-tests/overnight/scenarios/session-{1..27}.md` — one prompt file per session, following the scenario descriptions
3. `/tmp/longmem-tests/overnight/scenarios/pre-session-{12,14,17,18,19,21,23}.sh` — 7 pre-session scripts (from plan, make executable)
4. `/tmp/longmem-tests/test-longmem.sh` — checkpoint test suite (from plan, make executable)
5. Set up the fresh NoteGraph instance at `/tmp/longmem-tests/overnight/notegraph/`

Each session prompt must:
- Start with: "Your working directory is /tmp/longmem-tests/overnight/notegraph/. Read CLAUDE.md first, then follow its instructions to load your memory."
- Include the specific tasks for that session
- Include VERIFY checks with instruction to output: "VERIFY: [check name] = PASS/FAIL [detail]"
- End with session-end protocol + memory-sync
- Be self-contained (no reference to other prompts or conversation history)

Cold-start sessions (9, 15, 22, 27) must start with: "You have NO prior conversation history."
Mid-check sessions (2, 5, 10, 18, 20, 25) must include mid-session checkpoint instructions.
Breakage sessions (17, 19, 21, 23) must NOT tell the agent what's broken — let it discover.

Do NOT start the overnight run. Just create the files and verify the setup.
