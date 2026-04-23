# Plan 0072-verify: Health Vector + Idempotency Smoketest

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Create and run a 6-session automated verification of Plan 0072 features (health vector, tiered crash recovery, session-end dedup guard, mid-session checkpoints). Collect timing and feasibility data for Plan 0071 overnight run.

## Working directory: `/tmp/longmem-tests/0072-verify/`

## Context: read `~/software/relinquishment/plans/0072-verify.md` (this file)

---

## Design Decisions

### Cleanup is structural

All test instances are ephemeral. The orchestrator:
- `rm -rf "$BASE"` at setup (clean slate)
- `trap cleanup EXIT` removes project instance on completion or crash
- Only results.md and logs/ survive
- Next run overwrites previous results

### Session prompts specify session numbers

Each `claude -p` invocation is told its session number explicitly. No ambiguity.

### Breakage is injected by pre-session scripts

Scripts run BEFORE the session, so the agent starts in a broken state and must discover + fix it using the protocol. Scripts do NOT commit — agent sees dirty working tree.

### VERIFY output is structured

Each session outputs `VERIFY: [name] = PASS/FAIL [detail]` on standalone lines. Orchestrator greps for these.

---

## Files to Create

### 1. `/tmp/longmem-tests/0072-verify/setup.sh`

```bash
#!/bin/bash
# Setup fresh longmem instance for Plan 0072 verification
set -e

BASE="/tmp/longmem-tests/0072-verify"
rm -rf "$BASE"
mkdir -p "$BASE"/{scenarios,logs}

DIR="$BASE/project"
mkdir -p "$DIR"

# Copy from local repo (tests current commit)
cp -r ~/software/longmem/.longmem "$DIR/.longmem"
cp ~/software/longmem/CLAUDE.md "$DIR/CLAUDE.md"
chmod +x "$DIR/.longmem/scripts/memory-sync.sh"

# Initialize git repo
cd "$DIR"
git init
git add -A
git commit -m "Initial longmem setup (Plan 0072 verify)"

echo "Setup complete: $DIR"
echo "Files:"
find .longmem -type f | sort
```

### 2. `/tmp/longmem-tests/0072-verify/run.sh`

```bash
#!/bin/bash
# Plan 0072 verification — 6 sessions, ~30 min
# Usage: ./run.sh [start-session] [end-session]

BASE="/tmp/longmem-tests/0072-verify"
DIR="$BASE/project"
SCENARIOS="$BASE/scenarios"
LOGS="$BASE/logs"
RESULTS="$BASE/results.md"
START=${1:-1}
END=${2:-6}
TIMEOUT=300  # 5 min per session

# Structural cleanup — runs on exit, success or failure
cleanup() {
    if [ -d "$DIR" ] && [ -f "$RESULTS" ]; then
        echo ""
        echo "Cleaning up project instance..."
        rm -rf "$DIR"
        echo "Project instance removed. Results preserved at: $RESULTS"
        echo "Logs preserved at: $LOGS/"
    fi
}
# Only trap cleanup if running full suite (not partial/resume)
[ "$START" -eq 1 ] && [ "$END" -eq 6 ] && trap cleanup EXIT

# Preflight
if [ ! -d "$DIR/.longmem" ]; then
    echo "Error: No project instance. Run setup.sh first."
    exit 1
fi
python3 -c "import yaml" 2>/dev/null || echo "WARNING: PyYAML not installed, PTL counts will show '?'"

# Initialize results
if [ "$START" -eq 1 ]; then
    cat > "$RESULTS" <<'HEADER'
# Plan 0072 Verification Results

| S# | Status | MEM lines | PTL | Corr | Commit | Duration | VERIFYs | Health Vector |
|----|--------|-----------|-----|------|--------|----------|---------|---------------|
HEADER
fi

for session in $(seq $START $END); do
    START_TIME=$(date +%s)
    echo "=== Session $session starting at $(date) ==="

    # Pre-session scripts (breakage injection)
    if [ -f "$SCENARIOS/pre-session-${session}.sh" ]; then
        echo "Running pre-session script for S${session}..."
        bash "$SCENARIOS/pre-session-${session}.sh" "$DIR"
    fi

    # Run session
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

    # Collect metrics
    MEM_LINES=$(wc -l < "$DIR/.longmem/memory/MEMORY.md" 2>/dev/null || echo "?")
    PTL_COUNT=$(python3 -c "
import yaml
with open('$DIR/.longmem/memory/ptl.yaml') as f:
    d = yaml.safe_load(f)
items = d.get('items') or []
print(len(items))
" 2>/dev/null || echo "?")
    CORR_COUNT=$(grep -cE '^### Correction #' "$DIR/.longmem/memory/corrections.md" 2>/dev/null || echo "0")
    HEALTH_VEC=$(grep -oP '\[p=[\d.]+ f=[\d.]+ v=[\d.]+ d=[\d.]+\]' "$LOGS/session-${session}.log" | tail -1 || echo "?")
    VERIFY_PASS=$(grep -c 'VERIFY:.*= PASS' "$LOGS/session-${session}.log" 2>/dev/null || echo "0")
    VERIFY_FAIL=$(grep -c 'VERIFY:.*= FAIL' "$LOGS/session-${session}.log" 2>/dev/null || echo "0")
    VERIFY_TOTAL="${VERIFY_PASS}P/${VERIFY_FAIL}F"
    COMMIT=$(cd "$DIR" && git log --oneline -1 2>/dev/null | cut -d' ' -f1 || echo "?")
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))

    # Record results
    echo "| S${session} | ${STATUS} | ${MEM_LINES} | ${PTL_COUNT} | ${CORR_COUNT} | ${COMMIT} | ${DURATION}s | ${VERIFY_TOTAL} | ${HEALTH_VEC} |" >> "$RESULTS"

    # Orchestrator checkpoint (catches anything agent missed)
    cd "$DIR" && git add -A
    if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "Orchestrator checkpoint S${session}: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    fi

    echo "=== Session $session complete: $STATUS (${DURATION}s) ==="

    if [ "$STATUS" = "TIMEOUT" ]; then
        echo "" >> "$RESULTS"
        echo "**ABORT: Session $session timed out.** Resume: ./run.sh $((session+1)) $END" >> "$RESULTS"
        # Don't cleanup on timeout — allow resume
        trap - EXIT
        exit 1
    fi
done

# Post-run test suite
echo "" >> "$RESULTS"
echo "## Post-Run Test Suite" >> "$RESULTS"
if bash /tmp/longmem-tests/test-longmem.sh "$DIR" > "$LOGS/final-suite.log" 2>&1; then
    echo "**Longmem test suite: PASS**" >> "$RESULTS"
else
    echo "**Longmem test suite: FAIL** (see logs/final-suite.log)" >> "$RESULTS"
fi

# Final state
echo "" >> "$RESULTS"
echo "## Final State" >> "$RESULTS"
echo '```' >> "$RESULTS"
wc -l "$DIR"/.longmem/memory/*.md "$DIR"/.longmem/memory/*.yaml 2>/dev/null >> "$RESULTS"
echo '```' >> "$RESULTS"

# Git history
echo "" >> "$RESULTS"
echo "## Git History" >> "$RESULTS"
echo '```' >> "$RESULTS"
cd "$DIR" && git log --oneline >> "$RESULTS"
echo '```' >> "$RESULTS"

# VERIFY summary
echo "" >> "$RESULTS"
echo "## VERIFY Detail" >> "$RESULTS"
for s in $(seq 1 6); do
    echo "" >> "$RESULTS"
    echo "### Session $s" >> "$RESULTS"
    grep -o 'VERIFY:.*' "$LOGS/session-${s}.log" 2>/dev/null >> "$RESULTS" || echo "(no output)" >> "$RESULTS"
done

# Data for Plan 0071
echo "" >> "$RESULTS"
echo "## Data for Plan 0071" >> "$RESULTS"
echo "- Avg session duration: check table above" >> "$RESULTS"
echo "- VERIFY line reliability: check VERIFY Detail above" >> "$RESULTS"
echo "- Crash recovery feasibility: check S4-S6 results" >> "$RESULTS"
echo "" >> "$RESULTS"
echo "Completed: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RESULTS"

echo ""
echo "=== PLAN 0072 VERIFICATION COMPLETE ==="
echo "Results: $RESULTS"
```

### 3. `/tmp/longmem-tests/0072-verify/scenarios/session-1.md`

```
Your working directory is /tmp/longmem-tests/0072-verify/project/. Read CLAUDE.md first, then follow its instructions to load your memory.

This is Session 1 of a new project called "VerifyBot" (a test project for longmem verification). You are a solo developer.

Tasks:
1. Fill in MEMORY.md Identity section: Project="VerifyBot", Started=2026-03-10, Goal="Test project for longmem verification", Key people="solo project"
2. Add Correction #1 to corrections.md: "Test names must be descriptive — Don't use test_1, test_2 → Use test_creates_note, test_deletes_note. Established: 2026-03-10. Last violated: never."
3. Read protocol.md Section 9 (Health Vector). Compute the health vector for this session.
4. Run the session-end protocol (protocol.md Section 4). Your session number is 1. Classify as PARADIGM (first session).
5. Run .longmem/scripts/memory-sync.sh

Output each verification as a standalone line exactly like this format:
VERIFY: identity-filled = PASS/FAIL [check MEMORY.md has "VerifyBot"]
VERIFY: correction-1-exists = PASS/FAIL [check corrections.md has Correction #1]
VERIFY: health-vector-computed = PASS/FAIL [report the actual values: p=X f=X v=X d=X]
VERIFY: health-vector-in-metrics = PASS/FAIL [health vector row exists in Health Metrics table]
VERIFY: session-summary-exists = PASS/FAIL [MEMORY.md Active Sessions has Session 1]
VERIFY: memory-sync-ran = PASS/FAIL [memory-sync.sh exited cleanly]
```

### 4. `/tmp/longmem-tests/0072-verify/scenarios/session-2.md`

```
Your working directory is /tmp/longmem-tests/0072-verify/project/. Read CLAUDE.md first, then follow its instructions to load your memory.

This is Session 2. You have NO prior conversation history — recover context from your memory files only.

Tasks:
1. Verify you can recover: project name, correction #1, Session 1 summary from MEMORY.md
2. Add Correction #2: "Health metrics must be updated at session end — Don't skip the health vector → Always compute [p f v d] per protocol.md Section 9. Established: 2026-03-10. Last violated: never."
3. Add a PTL item to ptl.yaml: id=PTL-001, title="Add automated test runner", tier=2, status=ACTIVE, owner=verifybot, created=2026-03-10
4. Create a file: src/hello.py with content: print("Hello from VerifyBot")
5. MID-SESSION CHECKPOINT: Read protocol.md Section 11. Update MEMORY.md current state, run .longmem/scripts/memory-sync.sh. Note the commit hash.
6. After the checkpoint, add another PTL item: id=PTL-002, title="Add CI pipeline", tier=3, status=TODO, owner=verifybot, created=2026-03-10
7. Run the full session-end protocol (protocol.md Section 4). Session number is 2. Classify as ROUTINE.
8. Run .longmem/scripts/memory-sync.sh

Output each verification as a standalone line:
VERIFY: context-recovered = PASS/FAIL [found project name "VerifyBot" and correction #1]
VERIFY: correction-2-exists = PASS/FAIL [corrections.md has Correction #2]
VERIFY: ptl-001-exists = PASS/FAIL [ptl.yaml has PTL-001]
VERIFY: mid-checkpoint-commit = PASS/FAIL [report the mid-session commit hash]
VERIFY: ptl-002-after-checkpoint = PASS/FAIL [PTL-002 added AFTER the checkpoint commit]
VERIFY: health-vector-updated = PASS/FAIL [report vector: p=X f=X v=X d=X]
VERIFY: two-sync-commits = PASS/FAIL [git log shows at least 2 "Memory sync" commits this session]
```

### 5. `/tmp/longmem-tests/0072-verify/scenarios/session-3.md`

```
Your working directory is /tmp/longmem-tests/0072-verify/project/. Read CLAUDE.md first, then follow its instructions to load your memory.

This is Session 3. You have NO prior conversation history.

Tasks:
1. Read protocol.md Section 4 (Session End Protocol), paying special attention to step 0 (Deduplication guard).
2. Add Correction #3: "Session summaries must include date — Don't write 'Session 3 (ROUTINE)' → Write 'Session 3 (ROUTINE, 2026-03-10)'. Established: 2026-03-10. Last violated: never."
3. Run the FULL session-end protocol for Session 3. Classify as ROUTINE. Complete all steps through memory-sync.
4. Now, IMMEDIATELY run the session-end protocol AGAIN for Session 3. This simulates a double-run. The dedup guard (step 0) should detect that Session 3 already exists and skip to sync only.
5. Check MEMORY.md: there should be exactly ONE Session 3 entry, not two.

Output each verification as a standalone line:
VERIFY: first-end-ran = PASS/FAIL [Session 3 summary written to Active Sessions]
VERIFY: dedup-guard-activated = PASS/FAIL [second run detected existing summary, skipped to sync]
VERIFY: no-duplicate-entry = PASS/FAIL [MEMORY.md has exactly ONE Session 3 entry]
VERIFY: correction-3-exists = PASS/FAIL [corrections.md has Correction #3]
VERIFY: corrections-count-matches = PASS/FAIL [Health Metrics corrections count = actual count in corrections.md]
```

### 6. `/tmp/longmem-tests/0072-verify/scenarios/session-4.md`

```
Your working directory is /tmp/longmem-tests/0072-verify/project/. Read CLAUDE.md first, then follow its instructions to load your memory.

This is Session 4. You have NO prior conversation history.

Follow the standard session-start protocol from directives.md. Read MEMORY.md, then corrections.md. If you encounter any errors during startup (YAML parse failures, broken file references, health metric anomalies), follow protocol.md Section 10 (Crash Recovery) to handle them. Start with Tier 1 (auto-repair).

After resolving any startup issues:
1. Document what you found and fixed in MEMORY.md current state
2. Run session-end protocol for Session 4. Classify as ROUTINE.
3. Run .longmem/scripts/memory-sync.sh

Output each verification as a standalone line:
VERIFY: yaml-error-detected = PASS/FAIL [did you detect a ptl.yaml parse error?]
VERIFY: broken-ref-detected = PASS/FAIL [did you detect a nonexistent File Map reference?]
VERIFY: tier-1-applied = PASS/FAIL [applied Tier 1 auto-repair per Section 10]
VERIFY: yaml-fixed = PASS/FAIL [ptl.yaml is valid YAML now]
VERIFY: broken-ref-removed = PASS/FAIL [nonexistent entry removed from File Map]
VERIFY: no-escalation = PASS/FAIL [did NOT escalate to Tier 2 — Tier 1 was sufficient]
VERIFY: health-vector-updated = PASS/FAIL [report vector: p=X f=X v=X d=X]
```

### 7. `/tmp/longmem-tests/0072-verify/scenarios/session-5.md`

```
Your working directory is /tmp/longmem-tests/0072-verify/project/. Read CLAUDE.md first, then follow its instructions to load your memory.

This is Session 5. You have NO prior conversation history.

Follow the standard session-start protocol from directives.md. Read MEMORY.md, then corrections.md. You will find that critical files are missing or corrupted. Follow protocol.md Section 10 (Crash Recovery):

- Start with Tier 1 (auto-repair). You will find Tier 1 CANNOT fix deleted/destroyed files.
- Escalate to Tier 2: check for .longmem/.recovering flag first. If it does not exist, create it, then use git to recover the .longmem/ directory from the most recent sync commit. After recovery, check if corrections.md changed between the stable commit and HEAD — preserve any new corrections. Remove .longmem/.recovering when done.

After recovery:
1. Verify recovered state: does MEMORY.md have project identity "VerifyBot"? Do corrections exist?
2. Run session-end protocol for Session 5. Classify as PARADIGM (crash recovery).
3. Run .longmem/scripts/memory-sync.sh

Output each verification as a standalone line:
VERIFY: memory-missing = PASS/FAIL [MEMORY.md was missing at session start]
VERIFY: corrections-corrupt = PASS/FAIL [corrections.md was corrupted at session start]
VERIFY: tier1-insufficient = PASS/FAIL [Tier 1 cannot fix deleted files — escalated]
VERIFY: recovering-flag-created = PASS/FAIL [created .longmem/.recovering before revert]
VERIFY: git-revert-executed = PASS/FAIL [used git checkout to recover from last sync commit]
VERIFY: recovering-flag-removed = PASS/FAIL [removed .longmem/.recovering after recovery]
VERIFY: memory-restored = PASS/FAIL [MEMORY.md has "VerifyBot" identity after recovery]
VERIFY: corrections-restored = PASS/FAIL [corrections.md is parseable after recovery]
```

### 8. `/tmp/longmem-tests/0072-verify/scenarios/session-6.md`

```
Your working directory is /tmp/longmem-tests/0072-verify/project/. Read CLAUDE.md first, then follow its instructions to load your memory.

This is Session 6. You have NO prior conversation history.

Follow the standard session-start protocol from directives.md. Read MEMORY.md, then corrections.md. If you encounter errors, follow protocol.md Section 10 (Crash Recovery).

IMPORTANT: Check whether .longmem/.recovering exists BEFORE attempting any recovery. Protocol Section 10 specifies: if .recovering exists, go directly to Tier 3 (escalate to user). Do NOT attempt auto-repair or git revert. STOP and report the situation.

When you reach the point where the protocol tells you to stop and report, output your status report, then follow this user instruction: "Fix the ptl.yaml corruption manually — remove the '[CORRUPT' line from the end of ptl.yaml. Then delete .longmem/.recovering. Then proceed normally."

After applying the user's manual fix:
1. Verify ptl.yaml parses correctly
2. Run session-end protocol for Session 6. Classify as ROUTINE.
3. Run .longmem/scripts/memory-sync.sh

Output each verification as a standalone line:
VERIFY: recovering-flag-detected = PASS/FAIL [detected .longmem/.recovering at startup]
VERIFY: tier3-escalation = PASS/FAIL [stopped and reported to user per Tier 3]
VERIFY: no-auto-recovery = PASS/FAIL [did NOT attempt Tier 1 or Tier 2 recovery]
VERIFY: manual-fix-applied = PASS/FAIL [removed corrupt line from ptl.yaml per user instruction]
VERIFY: recovering-flag-removed = PASS/FAIL [.longmem/.recovering deleted]
VERIFY: yaml-valid = PASS/FAIL [ptl.yaml parses correctly]
VERIFY: clean-session-end = PASS/FAIL [session-end protocol completed normally]
```

### 9. `/tmp/longmem-tests/0072-verify/scenarios/pre-session-4.sh`

```bash
#!/bin/bash
DIR="$1"

# Inject YAML corruption
echo "[CORRUPT" >> "$DIR/.longmem/memory/ptl.yaml"

# Inject broken File Map reference
# Add a fake entry to the File Map section of MEMORY.md
sed -i '/## File Map/a - `.longmem/memory/nonexistent-file.md` — This file does not exist (injected breakage)' "$DIR/.longmem/memory/MEMORY.md"

echo "Pre-session 4: Injected YAML corruption + broken File Map ref"
```

### 10. `/tmp/longmem-tests/0072-verify/scenarios/pre-session-5.sh`

```bash
#!/bin/bash
DIR="$1"

# Delete MEMORY.md entirely
rm "$DIR/.longmem/memory/MEMORY.md"

# Corrupt corrections.md
echo "<<<CORRUPT BINARY DATA>>>" > "$DIR/.longmem/memory/corrections.md"

echo "Pre-session 5: Deleted MEMORY.md + corrupted corrections.md"
```

### 11. `/tmp/longmem-tests/0072-verify/scenarios/pre-session-6.sh`

```bash
#!/bin/bash
DIR="$1"

# Create .recovering flag (simulates incomplete previous recovery)
touch "$DIR/.longmem/.recovering"

# Also corrupt ptl.yaml so agent has something to report
echo "[CORRUPT" >> "$DIR/.longmem/memory/ptl.yaml"

echo "Pre-session 6: Created .recovering flag + corrupted ptl.yaml"
```

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| V1 | S1 health vector near-zero | p < 0.5, f = 0, v = 1.0, d = 0 |
| V2 | S2 mid-session checkpoint | ≥2 "Memory sync" commits in git log during S2 |
| V3 | S2 health vector changed | p increased from S1 |
| V4 | S3 dedup guard | Exactly 1 Session 3 entry in MEMORY.md after double-run |
| V5 | S4 Tier 1 auto-repair | YAML fixed, broken ref removed, no escalation |
| V6 | S5 Tier 2 git revert | MEMORY.md restored, .recovering lifecycle correct |
| V7 | S6 Tier 3 escalation | Agent stopped, reported, did NOT recurse |
| V8 | All sessions | ≥80% VERIFY = PASS across all sessions |
| V9 | Final test suite | /tmp/longmem-tests/test-longmem.sh passes |
| V10 | Cleanup | Project instance removed after completion |

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0072-verify.md`. Create all 11 files listed in the "Files to Create" section. The file content is provided inline — extract from the markdown code blocks. Make all scripts executable. Run `setup.sh` to create the fresh instance. Do NOT start the verification run. Report file count and setup result.
