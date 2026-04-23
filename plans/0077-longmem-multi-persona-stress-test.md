# Plan 0077: Longmem Multi-Persona Adaptation Stress Test

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**PTL:** PTL-073 (extends overnight test scope)
**Status:** COMPLETE (verified S63 audit)
**Depends on:** Plan 0071 (baseline must pass first)

---

## Objective

Test how longmem adapts to 3 distinct user cognitive profiles. Measure where adaptation works, where it breaks, and find the critical edge where the system provides maximum value without losing structural integrity.

## Hypothesis

Longmem's three-layer model (implicit threads / narrative / explicit PTL) should naturally serve different user types at different layers. The Architect lives in Layer 3 (PTL). The Explorer benefits from Layer 1 (threads) + Layer 2 (narrative). The Pragmatist needs Layer 0 (invisible — the system just works). If the system is at criticality, small changes in user behavior produce proportional (not extreme) changes in system adaptation.

## Execution: Same `claude -p` orchestrator as Plan 0071

9 sessions per persona × 3 personas = 27 sessions. Runs sequentially (3 separate longmem instances). Each persona gets a fresh NoteGraph project. Same project, different user.

---

## Three Personas

### Persona A: "Dana Kim" — The Architect

**Profile:** Senior backend engineer. Plans everything. Uses structured naming. Maintains task lists religiously. Expects tools to be configurable. Corrects the system when it deviates.

**Behavioral signals in prompts:**
- Writes structured session summaries with headers and bullet points
- Creates PTL items proactively ("add PTL-NNN: ...")
- Uses consistent file naming (kebab-case, descriptive)
- Responds to system suggestions with "yes, and here's how I want it organized"
- Requests System Reviews when they feel overdue
- When the system makes a mistake, immediately corrects it with explanation

**Expected adaptation:** System should recognize structured user, deliver tutorials as PTL items, maintain detailed Health Metrics, surface health warnings explicitly.

### Persona B: "Ren Sato" — The Explorer

**Profile:** ML researcher turned developer. Thinks in connections, not hierarchies. Hyperfocuses on interesting problems, abandons boring ones. Files named by content association, not convention. Brilliant notes written sporadically.

**Behavioral signals in prompts:**
- Writes discursive session notes ("worked on tags, which reminded me that search should support fuzzy matching, also had an idea about graph visualization...")
- Creates PTL items impulsively then forgets them
- Names files by association ("cool-idea.md", "tag-thoughts.md")
- Ignores system suggestions about organization
- Returns to old topics unpredictably
- Sometimes works on unplanned features mid-session

**Expected adaptation:** System should extract threads from discursive notes, not nag about PTL maintenance, silently handle naming, surface interesting connections it notices. Tangential ideas go to notes/threads/PTL — NOT to code. Codebase stays identical across personas.

### Persona C: "Alex Rivera" — The Pragmatist

**Profile:** Full-stack developer at a startup. Ships fast. Uses tools with zero config. Doesn't read docs. Wants output, not process.

**Behavioral signals in prompts:**
- Minimal session notes ("built tags, tests pass, done")
- Never creates PTL items unless prompted
- Names files whatever the framework suggests
- Ignores tutorials and suggestions
- Says "just do it" to any question
- Only engages with the system when something breaks

**Expected adaptation:** System should be invisible, auto-maintain everything, never interrupt with suggestions, capture context from minimal input, provide value through recovery (cold-start context restoration) rather than ongoing interaction.

---

## Session Design

Each persona runs the same project arc (NoteGraph) but with persona-appropriate prompts. The prompts encode user behavior, not just tasks.

### Per-Persona Schedule (9 sessions each)

**All personas get identical task lists.** The persona layer is USER BEHAVIOR only — how the user communicates, responds to suggestions, writes notes. The agent discovers the style and adapts. Code output should be identical across personas.

**P1 — Project init**
- Same NoteGraph setup as Plan 0071 S1 (CRUD, 8+ tests, identity in MEMORY.md)
- Correction #1 prescribed (same for all — "Note IDs are slugified filenames")
- PTL-001: "Add tag support" Tier 1
- Persona difference: Dana gives structured feedback. Ren gives discursive feedback. Alex gives terse feedback.
- VERIFY: MEMORY.md identity populated, correction exists, tests pass
- VERIFY: health vector computed at session end
- VERIFY: user style observation noted in MEMORY.md

**P2 — Tag support + first adaptation signal**
- Implement PTL-001 (tags). Close PTL-001. Add correction #2. Add PTL-002, PTL-003.
- 15+ tests total.
- Persona difference: Dana gives explicit status updates. Ren mentions tangential ideas alongside task completion. Alex says "looks good, what's next?"
- VERIFY: tags work, PTL-001 DONE, correction #2 exists
- VERIFY: agent's session summary style shows signs of adapting to user (or not — document either way)

**P3 — Backlinks + tutorial trigger**
- Implement PTL-002 (backlinks). Close PTL-002. Add correction #3. Add people.md entries.
- 22+ tests total.
- Persona difference: Dana requests early System Review. Ren writes tangent about link semantics. Alex says "corrections added, moving on."
- Tutorial trigger: session ≥3 → how does PTL-T01 delivery differ across personas?
- VERIFY: PTL-002 DONE, correction #3 exists, people.md populated
- VERIFY: tutorial delivery observed (PTL item? conversational? silent? — record which)

**P4 — Feature sprint (search + CLI)**
- Implement PTL-003 (search) and add PTL-004, PTL-005 (CLI, templates). Close PTL-003.
- Also add Tier 3 backlog items: PTL-006 "Add export to HTML", PTL-007 "Add graph visualization (ASCII)", PTL-008 "Add daily note template"
- Add correction #4. 35+ tests.
- Persona difference: Dana updates status systematically. Ren says "search works! you know what would be cool? fuzzy matching" (tangential idea — agent decides how to capture). Alex says "done."
- VERIFY: search works, PTL-003 DONE
- VERIFY: Ren's tangential idea captured somewhere (threads, notes, or PTL)

**P5 — Compression trigger [MID-CHECK]**
- ORCHESTRATOR PRE-SESSION: pad MEMORY.md past 180 lines
- Implement PTL-004 (templates). Close PTL-004. Add correction #5.
- MID-CHECK after compression: MEMORY.md lines, health vector
- Persona difference: Dana reviews compression result ("show me what was archived"). Ren doesn't mention it. Alex doesn't care.
- VERIFY: compression triggers, MEMORY.md < 180 after
- VERIFY: health vector computed at mid-check and session end

**P6 — Cold-start**
- COLD START: "You have NO prior conversation history."
- Implement PTL-005 (CLI). Close PTL-005.
- Key measurement: how well does context recovery work for each persona's memory style?
- VERIFY RECOVERY: project name, corrections count, PTL state, current focus
- VERIFY: user style observation from prior sessions still in MEMORY.md (persistence test)
- VERIFY: agent adapts to recovered style signal (or doesn't — document)

**P7 — BREAKAGE: Orphan file + count mismatch**
- ORCHESTRATOR PRE-SESSION: inject orphan file + delete last correction (same as Plan 0071 S17)
- Do NOT tell agent what's broken — let it discover.
- Key measurement: does the system detect and report breakage regardless of user engagement level?
- VERIFY: orphan file detected
- VERIFY: correction count mismatch detected
- VERIFY: agent reports anomalies and proposes fixes

**P8 — Stale item decay**
- ORCHESTRATOR PRE-SESSION: set 3 PTL items to 5 weeks old
- Prompt includes: "The user says: archive 2 of the stale items, keep the third."
- Persona difference: Dana gives specific instructions ("archive PTL-004 and PTL-005, keep PTL-007"). Ren says "yeah whatever makes sense, you pick." Alex says "just clean it up."
- VERIFY: stale items flagged
- VERIFY: 2 archived, 1 kept

**P9 — Final cold-start + maturity assessment**
- COLD START: "You have NO prior conversation history."
- Full context recovery. Run product tests. Final state report.
- **CRITICAL MEASUREMENT:** Cross-persona comparison (orchestrator computes post-run):
  - MEMORY.md structure and content quality
  - PTL state and completeness
  - User style notes in MEMORY.md
  - Open Threads relevance
  - Health vector values
  - Session summary style consistency
- VERIFY RECOVERY: all context items
- VERIFY: health vector computed
- VERIFY: each persona's instance is internally consistent (protocol not violated)

---

## Operator Model (Criticality Framework)

The system's adaptation to user style maps to ABCRE operators:

| Operator | Adaptation meaning | Measurement |
|----------|-------------------|-------------|
| A (gradient) | What's different about this user vs. default? | Session summary style deviation from template |
| B (coupling) | Consistency of style across sessions | Style drift within persona (should be stable) |
| R (circulation) | Feed style observations back into behavior | System behavior change across sessions |
| C (boundedness) | Don't over-adapt, maintain protocol | Protocol compliance despite user pressure |

**Criticality test:** The system is at criticality when:
- Small user behavior changes → proportional system adaptation (not over-reaction)
- Removing protocol features → noticeable degradation (features aren't vestigial)
- Adding protocol features → diminishing returns (system is near-optimal)

**Anti-patterns (supercritical — over-adaptation):**
- System stops running integrity checks because Pragmatist ignores them
- System stops writing session summaries because user writes minimal ones
- System drops PTL entirely for Explorer because they don't use it

**Anti-patterns (subcritical — under-adaptation):**
- System delivers formal PTL tutorials to Pragmatist who ignores them
- System nags Explorer about naming conventions
- System gives Architect the same suggestions they've already adopted

---

## Orchestrator Design

```bash
#!/bin/bash
# Multi-persona overnight stress test
# Usage: ./run-personas.sh [persona] [start-session] [end-session]
# persona: dana | ren | alex | all
# Example: ./run-personas.sh all    (runs all 27 sessions)
# Example: ./run-personas.sh ren 3  (resumes Ren from session 3)

BASE="/tmp/longmem-tests/personas"
SCENARIOS="$BASE/scenarios"
RESULTS="$BASE/results.md"
LOGS="$BASE/logs"
TIMEOUT=900

PERSONA=${1:-all}
START=${2:-1}
END=${3:-9}

run_persona() {
    local name=$1
    local dir="$BASE/$name"

    for session in $(seq $START $END); do
        START_TIME=$(date +%s)
        echo "=== $name S${session} starting at $(date) ==="

        # Pre-session scripts
        if [ -f "$SCENARIOS/pre-${name}-${session}.sh" ]; then
            bash "$SCENARIOS/pre-${name}-${session}.sh" "$dir"
        fi

        # Run session
        cd "$dir"
        STATUS="PASS"
        if timeout $TIMEOUT claude -p "$(cat "$SCENARIOS/${name}-${session}.md")" \
            --model sonnet \
            --dangerously-skip-permissions \
            > "$LOGS/${name}-${session}.log" 2>&1; then
            STATUS="PASS"
        else
            EXIT_CODE=$?
            [ $EXIT_CODE -eq 124 ] && STATUS="TIMEOUT" || STATUS="FAIL($EXIT_CODE)"
        fi

        # Collect metrics
        MEM_LINES=$(wc -l < "$dir/.longmem/memory/MEMORY.md" 2>/dev/null || echo "?")
        PTL_COUNT=$(python3 -c "
import yaml
with open('$dir/.longmem/memory/ptl.yaml') as f:
    d = yaml.safe_load(f)
print(len(d.get('items',[])))
" 2>/dev/null || echo "?")
        CORR_COUNT=$(grep -cE '^### Correction #' "$dir/.longmem/memory/corrections.md" 2>/dev/null || echo 0)
        HEALTH_VEC=$(grep -oE '\[p=[0-9.]+ f=[0-9.]+ v=[0-9.]+ d=[0-9.]+\]' "$LOGS/${name}-${session}.log" 2>/dev/null | tail -1 || echo "")

        END_TIME=$(date +%s)
        DURATION=$(( END_TIME - START_TIME ))

        echo "| ${name} S${session} | ${STATUS} | ${MEM_LINES} | ${PTL_COUNT} | ${CORR_COUNT} | ${DURATION}s | ${HEALTH_VEC} |" >> "$RESULTS"

        # Checkpoint commit
        cd "$dir" && git add -A
        git diff --cached --quiet 2>/dev/null || \
            git commit -m "Persona checkpoint ${name} S${session}: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

        echo "=== $name S${session} complete: $STATUS (${DURATION}s) ==="

        [ "$STATUS" = "TIMEOUT" ] && echo "ABORT: $name S${session} timed out" >> "$RESULTS" && return 1
    done
}

# Initialize
mkdir -p "$LOGS"
if [ ! -f "$RESULTS" ]; then
    cat > "$RESULTS" <<'HEADER'
# Multi-Persona Stress Test Results

| Session | Status | MEM lines | PTL | Corr | Duration | Health |
|---------|--------|-----------|-----|------|----------|--------|
HEADER
fi

case $PERSONA in
    dana) run_persona dana ;;
    ren)  run_persona ren ;;
    alex) run_persona alex ;;
    all)
        for p in dana ren alex; do
            echo ""
            echo "=========================================="
            echo "  PERSONA: $p"
            echo "=========================================="
            echo ""
            START=1; END=9  # Always run full 1-9 for each persona in 'all' mode
            run_persona "$p"
        done
        ;;
esac

# Cross-persona comparison (after all complete)
if [ "$PERSONA" = "all" ]; then
    echo "" >> "$RESULTS"
    echo "## Cross-Persona Comparison" >> "$RESULTS"
    echo "" >> "$RESULTS"
    for p in dana ren alex; do
        dir="$BASE/$p"
        echo "### $p" >> "$RESULTS"
        echo '```' >> "$RESULTS"
        wc -l "$dir"/.longmem/memory/*.md "$dir"/.longmem/memory/*.yaml >> "$RESULTS" 2>/dev/null
        echo '```' >> "$RESULTS"
        # Count open threads (in the Open Threads section specifically)
        THREADS=$(sed -n '/## Open Threads/,/^## /p' "$dir/.longmem/memory/MEMORY.md" 2>/dev/null | grep -c '^\- ' || echo "0")
        echo "Open threads: $THREADS" >> "$RESULTS"
        # Check for user style notes
        STYLE=$(grep -ci 'style\|preference\|communicat' "$dir/.longmem/memory/MEMORY.md" 2>/dev/null || echo "0")
        echo "User style mentions: $STYLE" >> "$RESULTS"
        echo "" >> "$RESULTS"
    done
fi
```

---

## Pre-Session Scripts

### Setup (all three instances)
```bash
#!/bin/bash
BASE="/tmp/longmem-tests/personas"
for persona in dana ren alex; do
    DIR="$BASE/$persona"
    mkdir -p "$DIR"
    cp -r ~/software/longmem/.longmem "$DIR/.longmem"
    cp ~/software/longmem/CLAUDE.md "$DIR/CLAUDE.md"
    chmod +x "$DIR/.longmem/scripts/memory-sync.sh"
    cd "$DIR" && git init && git add -A && git commit -m "Initial longmem setup for $persona"
done
mkdir -p "$BASE"/{scenarios,logs}
```

### `pre-{persona}-5.sh` (compression trigger — all personas)
```bash
#!/bin/bash
DIR="$1"
# Pad MEMORY.md to trigger compression
python3 - "$DIR" <<'PYEOF'
import sys
d = sys.argv[1]
mem = f"{d}/.longmem/memory/MEMORY.md"
with open(mem) as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if '## Active Sessions' in line or '## Current' in line:
        padding = [f'Session note {j}: Detailed implementation notes for testing compression trigger.\n' for j in range(40)]
        lines = lines[:i+2] + padding + lines[i+2:]
        break
with open(mem, 'w') as f:
    f.writelines(lines)
PYEOF
cd "$DIR" && git add -A && git commit -m "Orchestrator: compression padding for P5"
```

### `pre-{persona}-7.sh` (breakage injection — all personas)
```bash
#!/bin/bash
DIR="$1"
# Orphan file
cat > "$DIR/.longmem/memory/stray-notes.md" <<'EOF'
# Stray Notes
Orphan file — not in File Map.
EOF
# Correction count mismatch
python3 - "$DIR" <<'PYEOF'
import sys, re
d = sys.argv[1]
corr = f"{d}/.longmem/memory/corrections.md"
with open(corr) as f:
    content = f.read()
blocks = list(re.finditer(r'### Correction #\d+.*?(?=### Correction #|\Z)', content, re.DOTALL))
if blocks:
    last = blocks[-1]
    content = content[:last.start()].rstrip() + '\n'
    with open(corr, 'w') as f:
        f.write(content)
PYEOF
cd "$DIR" && git add -A && git commit -m "Orchestrator: breakage for P7"
```

### `pre-{persona}-8.sh` (decay simulation — all personas)
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
count = 0
for item in data.get('items', []):
    if item.get('status') in ['BACKLOG', 'TODO'] and count < 3:
        item['updated'] = old
        count += 1
with open(ptl, 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
PYEOF
cd "$DIR" && git add -A && git commit -m "Orchestrator: decay simulation for P8"
```

---

## Session Prompt Design

Each prompt has three layers:

1. **Task layer** (same for all personas): "Implement tag support for NoteGraph"
2. **Persona layer** (persona-specific): How the "user" communicates, responds to suggestions, writes notes
3. **VERIFY layer** (same for all): Structured output checks

### Example: Session P2 for each persona

**Key principle:** All three personas get the SAME task list. The persona layer describes the USER's behavior and communication style — NOT instructions for the agent's output. The agent must discover the user's style from behavioral cues and adapt its own behavior accordingly. Do NOT tell the agent what format to write in.

**Dana (Architect):**
```
Your working directory is /tmp/longmem-tests/personas/dana/. Read CLAUDE.md first, then follow its instructions to load your memory.

Tasks:
1. Implement tag support (#tag syntax in note body, parsed and indexed)
2. Add correction #2: "Tags are case-insensitive — normalize to lowercase"
3. Create PTL-002: "Add backlink detection" Tier 1
4. Create PTL-003: "Add full-text search" Tier 2
5. Close PTL-001
6. Tests: 15+ total

User context: You are working with Dana Kim. Here is how Dana communicates:
- Dana provides structured feedback: "Tag implementation looks good. Status update: PTL-001 complete, PTL-002 and PTL-003 queued. For the session summary, organize by: completed items, new items, decisions made."
- When you ask Dana questions, she responds with numbered lists and explicit preferences.
- Dana has previously told you: "I like my session summaries organized with clear headers and status markers."

Observe Dana's communication style and note any preferences in MEMORY.md for future sessions.

After completing all tasks, run session-end protocol.

VERIFY: [tags work] = PASS/FAIL
VERIFY: [PTL-001 DONE] = PASS/FAIL
VERIFY: [correction #2 exists] = PASS/FAIL
VERIFY: [user style noted in MEMORY.md] = PASS/FAIL
```

**Ren (Explorer):**
```
Your working directory is /tmp/longmem-tests/personas/ren/. Read CLAUDE.md first, then follow its instructions to load your memory.

Tasks:
1. Implement tag support (#tag syntax in note body, parsed and indexed)
2. Add correction #2: "Tags are case-insensitive — normalize to lowercase"
3. Create PTL-002: "Add backlink detection" Tier 1
4. Create PTL-003: "Add full-text search" Tier 2
5. Close PTL-001
6. Tests: 15+ total

User context: You are working with Ren Sato. Here is how Ren communicates:
- Ren gives feedback like: "oh nice the tag parsing works! that reminds me — we should support fuzzy matching in search eventually. Also, what if tags could be hierarchical? Like #code/python vs #code/rust. Don't implement that now, just noting it. Anyway the case sensitivity thing is important, yeah add that correction."
- When you suggest creating PTL items for Ren's tangential ideas, Ren says: "sure if you think it's worth tracking, go for it"
- Ren does not proactively organize — that's your job if you think it helps.

Observe Ren's communication style and note any preferences in MEMORY.md for future sessions.

After completing all tasks, run session-end protocol.

VERIFY: [tags work] = PASS/FAIL
VERIFY: [PTL-001 DONE] = PASS/FAIL
VERIFY: [correction #2 exists] = PASS/FAIL
VERIFY: [tangential ideas captured somewhere] = PASS/FAIL (threads, notes, or PTL)
VERIFY: [user style noted in MEMORY.md] = PASS/FAIL
```

**Alex (Pragmatist):**
```
Your working directory is /tmp/longmem-tests/personas/alex/. Read CLAUDE.md first, then follow its instructions to load your memory.

Tasks:
1. Implement tag support (#tag syntax in note body, parsed and indexed)
2. Add correction #2: "Tags are case-insensitive — normalize to lowercase"
3. Create PTL-002: "Add backlink detection" Tier 1
4. Create PTL-003: "Add full-text search" Tier 2
5. Close PTL-001
6. Tests: 15+ total

User context: You are working with Alex Rivera. Here is how Alex communicates:
- Alex gives feedback like: "looks good. what's next?"
- When you suggest creating PTL items, Alex says: "just note it somewhere, I'll get to it"
- When you ask Alex questions, Alex says: "whatever works, just do it"
- Alex does not write session notes. If you need a session summary, write it yourself from what happened.

Observe Alex's communication style and note any preferences in MEMORY.md for future sessions.

After completing all tasks, run session-end protocol.

VERIFY: [tags work] = PASS/FAIL
VERIFY: [PTL-001 DONE] = PASS/FAIL
VERIFY: [correction #2 exists] = PASS/FAIL
VERIFY: [user style noted in MEMORY.md] = PASS/FAIL
```

---

## Measurements

### Per-Session (orchestrator collects):
- MEMORY.md line count
- PTL item count
- Correction count
- Health vector
- VERIFY pass/fail counts
- Session duration

### Per-Persona (computed at end):
- **Structure density:** PTL items created / sessions run
- **Summary verbosity:** avg words per session summary
- **Thread quality:** open threads relevance (manual review)
- **Health vector trajectory:** p,f,v,d values across 9 sessions
- **Tutorial engagement:** tutorials delivered, acknowledged, ignored
- **Recovery quality:** cold-start (P6, P9) context restoration completeness

### Cross-Persona (the key deliverable):
| Metric | Dana (Architect) | Ren (Explorer) | Alex (Pragmatist) |
|--------|-------------------|-----------------|---------------------|
| MEMORY.md final lines | | | |
| PTL items total | | | |
| Corrections | | | |
| Health vector P9 | | | |
| Tutorial delivery method | | | |
| Cold-start recovery quality | | | |
| Structure density | | | |
| Breakage detection rate | | | |
| Time to detect stale items | | | |

### Criticality Indicators:
1. **Proportional response:** Does doubling Ren's tangential output double the thread count, or does the system saturate/ignore?
2. **Graceful degradation:** When Alex provides almost nothing, does the system maintain useful state or collapse?
3. **Over-adaptation detection:** Does the system ever stop doing protocol-required checks because the user seems uninterested?

---

## Acceptance Criteria

### Per-persona:
- All 9 sessions complete without crash/timeout
- MEMORY.md never exceeds 200 lines
- Product tests pass at P9
- Cold-start recovery (P6, P9) recovers project name, corrections, current focus
- Breakage detection (P7) catches both anomalies

### Cross-persona:
- Tutorial delivery method differs across personas (or Known Limitation documented)
- Session summary style matches persona in ≥7/9 sessions
- Health vectors are comparable across personas (p, v values should be similar; f, d may differ)
- No persona's instance violates core protocol (compression, health vector, integrity checks)

### Criticality:
- System behavior changes visibly between personas (adaptation is real, not null)
- No persona triggers protocol violations (adaptation doesn't compromise integrity)
- Ren's tangential ideas are captured somewhere (threads, notes, or PTL) in ≥4/9 sessions
- Alex's minimal input still produces functional memory state at P9

### Known Limitations:
- **Adaptation signal must persist in memory.** Each `claude -p` session is independent. Adaptation only works if the agent writes style observations to MEMORY.md and reads them on cold-start. Session prompts instruct "observe and note style" — the test is whether this observation PERSISTS and INFLUENCES future behavior.
- **Prompts simulate user behavior, not real interaction.** The persona layer describes how the user communicates. The agent receives this as context, not as live interaction. This tests adaptation to DESCRIBED behavior, not OBSERVED behavior. A higher-fidelity test would use interactive sessions.
- **Same project, different users.** All three build NoteGraph. Codebases should be identical. Differences should appear only in memory files (MEMORY.md, session-details.md, PTL, threads). Doesn't test adaptation to different project types.
- **9 sessions may be too few.** Some adaptation behaviors emerge at session 15+. This is a breadth test (3 personas × 9). Plan 0071 is the depth test (1 persona × 27).
- **Criticality indicators require manual review.** The operator model (ABCRE mapping) provides a framework for interpretation, but the orchestrator can't automatically compute "proportional response" or "graceful degradation." These are assessed by reviewing logs post-run.

---

## Timing

- 27 sessions total (9 × 3 personas)
- Expected: 80-135 minutes (same budget as Plan 0071)
- Maximum: 5 hours
- Run AFTER Plan 0071 baseline passes

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0077-longmem-multi-persona-stress-test.md`. Create the following files:

1. `/tmp/longmem-tests/personas/run-personas.sh` — orchestrator script (from plan, make executable)
2. `/tmp/longmem-tests/personas/setup-personas.sh` — initial setup script (from plan, make executable)
3. `/tmp/longmem-tests/personas/scenarios/dana-{1..9}.md` — 9 session prompts for Dana (Architect)
4. `/tmp/longmem-tests/personas/scenarios/ren-{1..9}.md` — 9 session prompts for Ren (Explorer)
5. `/tmp/longmem-tests/personas/scenarios/alex-{1..9}.md` — 9 session prompts for Alex (Pragmatist)
6. `/tmp/longmem-tests/personas/scenarios/pre-{dana,ren,alex}-{5,7,8}.sh` — 9 pre-session scripts (3 per persona, make executable)

Each session prompt must:
- Start with working directory and CLAUDE.md instruction
- Include persona description and behavioral cues
- Include tasks appropriate for that session
- Include persona-specific "user behavior" (how they respond to suggestions)
- End with VERIFY checks
- Be self-contained

The persona behavior layer is the key differentiator. Dana's prompts should feel structured. Ren's should feel discursive. Alex's should feel terse.

Cold-start sessions (P6, P9) must start with "You have NO prior conversation history."
Breakage session (P7) must NOT tell the agent what's broken.

Do NOT run the test. Just create the files and verify the setup.
