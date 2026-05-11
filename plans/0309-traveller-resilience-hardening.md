# Plan 0309: Traveller Reference System — Resilience Hardening

**Status:** READY FOR GENERATOR  
**Priority:** HIGH — blocks Plan 0308 unblock (Bruce can't validate a system with known resilience gaps).  
**Prerequisite:** Plan 0299 complete (it is).  
**Source:** S68 stress test, ISSUES.md (ISSUE-001 through ISSUE-009).  
**Estimated effort:** Single Generator session, ~45 min.  
**Branch:** `traveller-ref-phase1` (current)

---

## Why This Plan Exists

The Plan 0299 stress test (S68) found 9 issues — 2 moderate data-loss risks, 5 resilience gaps, 2 cosmetic. The system works for happy-path operations but has no protection against DB corruption, rebuild failure, concurrent access, or graceful degradation. These must be fixed before Bruce validates the system for Plan 0308 migration.

**Key principle:** The Traveller DB is a testbed for Argus's memory. Every resilience pattern we prove here gets baked into Plan 0308. Fix it cheap here or fix it expensive there.

---

## Phase 1: Fix load.sh FK Enforcement [ISSUE-002]

**File:** `traveller-reference/scripts/load.sh`

**Change:** Replace the per-script sqlite3 invocation so PRAGMA and data share the same connection.

Current (broken):
```bash
sqlite3 "$DB" "PRAGMA foreign_keys = ON;"
sqlite3 "$DB" < "$full_path"
```

Fixed:
```bash
(echo "PRAGMA foreign_keys=ON;" && cat "$full_path") | sqlite3 "$DB"
```

**Test:** Add `test-12-fk-during-load.sh`: creates a temp data script with a bad `species_id` FK reference, attempts to load it through `load.sh`'s mechanism (piped PRAGMA+script), verifies it fails with exit code ≠ 0. Clean up temp file.

**Gate:** `test-02-constraints.sh` still passes. New `test-12-fk-during-load.sh` passes. `run-tests.sh` 12/12.

---

## Phase 2: Fix rebuild-db.sh Safety [ISSUE-006]

**File:** `traveller-reference/scripts/rebuild-db.sh`

**Changes:**
1. Before dropping the DB, copy to `${DB}.bak`
2. After rebuild + verification passes, remove the backup
3. If rebuild fails, restore from backup

```bash
# Before rm
if [ -f "$DB" ]; then
    cp "$DB" "${DB}.bak"
    echo "  Backed up to ${DB}.bak"
    rm "$DB"
fi

# After RESULT: REBUILD CLEAN
if [ -f "${DB}.bak" ]; then
    rm "${DB}.bak"
    echo "  Removed backup (rebuild successful)"
fi

# On failure
if [ "$integrity" != "ok" ] || [ "$fk_errors" -ne 0 ]; then
    if [ -f "${DB}.bak" ]; then
        mv "${DB}.bak" "$DB"
        echo "  RESTORED from backup"
    fi
    exit 1
fi
```

**Gate:** Rebuild still completes clean. Backup file created and removed. Simulate rebuild failure (corrupt a setup script, attempt rebuild, verify backup restores).

---

## Phase 3: Capture Stellar Bodies as Data Script [ISSUE-001]

**Goal:** Make rebuild fully self-contained — no external dependency on VTT-private repo.

**Steps:**
1. Run the Python importer and capture its SQL output (verified: outputs valid INSERT statements to stdout):
   ```bash
   python3 ~/software/traveller-VTT-private/import-enriched-systems.py > scripts/db-data/013-stellar-bodies.sql
   ```
2. Verify the captured SQL reproduces the same 474 rows and 37 systems
3. Add `013-stellar-bodies.sql` to `scripts/db-data/MANIFEST.md` (between 012-canon-systems and 014-canon-cultures) with sha hash
4. Update `reference-landmarks.md` db-data MANIFEST hash
5. Run full rebuild — stellar_bodies should now be 474 without manual reimport
6. **Ordering note:** The importer outputs INSERT OR IGNORE for systems (preserves canon data scripts) and INSERT OR REPLACE for stellar_bodies. It must run AFTER 012-canon-systems.sql (which creates the canon system rows that stellar_bodies FK-references). The manifest ordering handles this.

**Gate:** `rebuild-db.sh` produces 474 stellar bodies with NO manual step. Before/after counts identical. test-04 passes.

---

## Phase 4: Session-Start Health Check Script [ISSUE-005]

**New file:** `traveller-reference/scripts/health-check.sh`

Purpose: Fast integrity check, callable at session start or by a hook.

```bash
#!/bin/bash
# health-check.sh — Quick DB integrity check with auto-repair
set -uo pipefail
BASE="$(cd "$(dirname "$0")/.." && pwd)"
DB="$BASE/campaign.db"

if [ ! -f "$DB" ]; then
    echo "[DB MISSING — rebuilding]"
    bash "$BASE/scripts/rebuild-db.sh"
    exit $?
fi

integrity=$(sqlite3 "$DB" "PRAGMA integrity_check;" 2>/dev/null)
if [ "$integrity" != "ok" ]; then
    echo "[DB CORRUPT — integrity=$integrity — rebuilding]"
    bash "$BASE/scripts/rebuild-db.sh"
    exit $?
fi

fk_errors=$(sqlite3 "$DB" "PRAGMA foreign_keys=ON; PRAGMA foreign_key_check;" 2>/dev/null | wc -l)
if [ "$fk_errors" -ne 0 ]; then
    echo "[FK VIOLATIONS: $fk_errors — rebuilding]"
    bash "$BASE/scripts/rebuild-db.sh"
    exit $?
fi

# Quick count verification (detect data loss without full test suite)
npc_count=$(sqlite3 "$DB" "SELECT count(*) FROM npcs;")
if [ "$npc_count" -lt 80 ]; then
    echo "[DATA LOSS: only $npc_count NPCs (expected 90+) — rebuilding]"
    bash "$BASE/scripts/rebuild-db.sh"
    exit $?
fi

echo "[DB OK: integrity=ok, FK=clean, NPCs=$npc_count]"
exit 0
```

**Integration:** Add to `scripts/tests/MANIFEST.md` as a utility (not a test). Document in ISSUES.md that this should be called at session start. A session-start hook is a future enhancement (not this plan).

**Gate:** Script detects all three failure modes (missing, corrupt, data loss). Auto-rebuilds successfully in each case. Returns exit 0 on healthy DB.

---

## Phase 5: DR Protocol Update [ISSUE-007, ISSUE-008]

**File:** `~/software/aurasys-memory/disaster/recovery-protocol.md`

**Add between Tier 2 and Tier 3:**

```markdown
## Tier 2.5: Database Corruption or Loss

**Applies to:** campaign.db (Traveller), argus.db (when built)

**Symptoms:** SQLite errors on query, PRAGMA integrity_check ≠ ok, .db file missing, data count anomalies.

**Recovery:**
1. Detect: health-check.sh (auto-runs at session start) or manual `PRAGMA integrity_check`
2. If corrupt/missing: `bash scripts/rebuild-db.sh` (~1.3s for Traveller, TBD for Argus)
3. Verify: `run-tests.sh` passes
4. If rebuild fails: `git checkout -- campaign.db` (committed snapshot — may be stale but functional)
5. If scripts are also corrupt: `git checkout -- scripts/` then rebuild
6. If git is intact, everything is recoverable. Zero-data-loss ceiling.

**Degradation (Traveller):**
DB loss = loss of structured queries (views, cross-entity joins, confab ordering).
Prose files (.md) still work. L1 index still loads. Session prep proceeds with manual lookups.

**Degradation (Argus — when built):**
DB loss = loss of structured queries. Falls back to pre-retrofit behavior.
All memory/*.md files still load normally through Claude Code's auto-memory system.
MEMORY.md still loaded at session start. System functions at pre-Plan-0308 capability.

**Prevention:**
- health-check.sh at session start
- rebuild-db.sh creates backup before drop
- DB file committed to git (snapshot recovery)
- Scripts in git (deterministic rebuild)
```

**Gate:** DR protocol covers DB scenarios. Degradation path documented for both systems.

---

## Phase 6: NPC Fixed Locations [ISSUE-003] (OPTIONAL)

**Only if Bruce wants this.** Add `current_system` for NPCs with known fixed locations.

| NPC | Location |
|-----|----------|
| Telenn Gha | Binges (1234) |
| Htasea'a Ora | Raschev (1436) |
| Voss-Hallen | Binges (1234) |
| Hagen Stross | Forine (1533) |
| Senator Koss | Collace (1237) |

**File:** Add UPDATE statements to `020-campaign-npcs.sql` or a new `025-npc-locations.sql`.

**Gate:** `SELECT n.name, s.name FROM npcs n JOIN systems s ON n.current_system = s.hex WHERE n.current_system IS NOT NULL;` returns the expected list.

---

## Phase 7: Verify + Update ISSUES.md

1. Run full test suite: all pass
2. Run health-check.sh: OK
3. Simulate each failure mode:
   - Delete DB → health-check detects, rebuilds, 474 stellar bodies preserved
   - Corrupt DB → health-check detects, rebuilds from backup
   - Bad FK in test data → load.sh rejects at load time
4. Update `ISSUES.md`: mark fixed issues with date and commit
5. Update performance/resilience baselines with new numbers

**Gate:** All 9 issues addressed (7 FIXED, 1 WONTFIX if ISSUE-004 accepted, ISSUE-003 pending decision). ISSUES.md updated. run-tests.sh 12/12+ (new tests added).

---

## Generator Prompt

```
You are the Generator for Plan 0309.
Read: ~/software/relinquishment/plans/0309-traveller-resilience-hardening.md
Execute Phases 1-5, 7 in order. Phase 6 is OPTIONAL — skip unless the plan says otherwise.
Each phase has a Gate — verify before proceeding to next.
Commit after each phase: "Plan 0309 Phase N: description"
Report: phases completed, tests passing, issues fixed.
```

---

## Constraints

- All scripts must be idempotent (re-runnable, same result)
- All tests must pass after each phase
- No changes to schema or data content — this plan fixes infrastructure only
- Git tag `pre-0309` before starting
- Traveller-reference.md (L1) should not need changes for this plan
