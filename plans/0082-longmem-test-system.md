# Plan 0082: Longmem Test System

*Auditor: Argus (Session 42). Origin: Robin will evaluate longmem. No tests exist. Need at minimum: integrity checks, CRC/hash verification, and a smoke test that proves the system activates correctly.*

---

## Background (Generator: read this section for context)

**Longmem** is a persistent memory system for Claude Code at `~/software/longmem/`. It's a template repo users clone. The installed system lives in `.longmem/` with memory files, a protocol, and a sync script.

**Current state:** Zero tests. The system has been validated manually over 40+ sessions on one project (N=1). Before sharing with collaborators, we need automated verification that the template is internally consistent and the core mechanisms work.

**Design constraint:** Tests must be runnable with `bash` only. No test framework dependencies. No npm, no pytest, no jest. A user who clones the repo should be able to run `bash tests/run-all.sh` and see pass/fail output. This matches longmem's zero-dependency philosophy.

**Test location:** `~/software/longmem/tests/` (new directory at repo root, NOT inside `.longmem/`).

**Files to read before writing:**
- `~/software/longmem/.longmem/directives.md` — what the system promises
- `~/software/longmem/.longmem/memory/MEMORY.md` — template L1 cache
- `~/software/longmem/.longmem/memory/protocol.md` — session lifecycle rules
- `~/software/longmem/.longmem/scripts/memory-sync.sh` — sync script
- `~/software/longmem/README.md` — file structure diagram, quickstart
- `~/software/longmem/install.md` — install flow
- `~/software/longmem/CLAUDE.md` — activation block

---

## Phase 1: Test Runner and Integrity Tests

### File: `tests/run-all.sh`

**Spec:** Bash test runner. Finds and runs all `test-*.sh` files in `tests/`. For each: runs it, captures exit code, prints PASS/FAIL with test name. At end: summary line ("N passed, M failed"). Exit 0 if all pass, exit 1 if any fail. Color output (green/red) if terminal supports it, plain text otherwise.

```bash
#!/bin/bash
# run-all.sh — Run all longmem tests
# Usage: bash tests/run-all.sh [from repo root]
```

### File: `tests/test-integrity.sh`

**Spec:** Verify the template is internally consistent. Each check prints a one-line result.

Checks:
1. **All File Map entries resolve.** Parse MEMORY.md File Map section, extract paths (lines matching `- \`.longmem/...`), verify each file exists.
2. **No orphan memory files.** Every `.md` and `.yaml` file in `.longmem/memory/` should appear in the File Map.
3. **directives.md references exist.** Extract file paths mentioned in directives.md, verify they exist.
4. **protocol.md section references valid.** Extract "Section N" references, verify those section numbers exist as `## N.` headings in protocol.md.
5. **README file structure matches reality.** Parse the file tree from README.md, verify each listed path exists. Flag files that exist but aren't in the tree.
6. **CLAUDE.md activation block present.** Check for `<!-- LONGMEM START` and `<!-- LONGMEM END -->` markers.
7. **memory-sync.sh is executable.** Check file permissions.
8. **No broken markdown links.** Scan all `.md` files for `[text](path)` links where path is a relative file reference (not http), verify the target exists.

### File: `tests/test-hashes.sh`

**Spec:** CRC/hash verification of template files. Ensures template hasn't been accidentally modified.

1. **Generate baseline hashes.** On first run (no `.test-baseline` file), compute SHA256 of all files in `.longmem/` and save to `tests/.test-baseline`. Print "Baseline created."
2. **Verify against baseline.** On subsequent runs, recompute hashes and compare. Report any changed files. Exit 1 if changes detected (indicates template drift).
3. **Reset command.** If `tests/test-hashes.sh --reset` is passed, regenerate baseline.
4. **Exclude `.file-hashes`** (generated artifact, expected to change).

Note: `.test-baseline` should be in `tests/.gitignore` — it's local to each clone, not committed.

---

## Phase 2: Smoke Test

### File: `tests/test-smoke.sh`

**Spec:** Verify the system can activate in a fresh environment. Does NOT require Claude Code — tests the file structure and script execution only.

1. **Create temp clone.** `cp -r` the repo to a temp directory. Init fresh git repo there.
2. **Verify CLAUDE.md loads.** Check that CLAUDE.md exists and contains the longmem activation block.
3. **Verify directives.md is readable.** Check file exists and is non-empty.
4. **Verify MEMORY.md is readable.** Check exists, non-empty, contains expected sections: Identity, Current State, L1 Corrections, Active Sessions, File Map, Health Metrics.
5. **Run memory-sync.sh.** Execute in the temp clone. Verify it creates a git commit (check `git log --oneline -1` output contains "Memory sync").
6. **Run memory-sync.sh again (idempotency).** Execute again with no changes. Verify it prints "no changes to commit" and does NOT create a duplicate commit.
7. **Simulate MEMORY.md growth.** Append 190 lines to MEMORY.md. Run `wc -l` and verify the health warning triggers in memory-sync.sh output (should print WARNING about line count).
8. **Clean up.** Remove temp directory.

---

## Phase 3: Documentation and Runner Integration

### File: `tests/.gitignore`

**Content:**
```
.test-baseline
```

### File: `tests/README.md`

**Content (brief, ~15 lines):**
- What: automated tests for longmem template integrity
- How: `bash tests/run-all.sh` from repo root
- Tests: integrity (cross-references), hashes (template drift), smoke (activation)
- Requirements: bash, git. No other dependencies.
- When to run: before committing changes, before releases

### Updates to existing files:

**`README.md`:** Add to file structure diagram:
```
├── tests/
│   ├── run-all.sh                  # Test runner
│   ├── test-integrity.sh           # Cross-reference and consistency checks
│   ├── test-hashes.sh              # Template drift detection
│   ├── test-smoke.sh               # Activation and sync verification
│   └── README.md                   # Test documentation
```

**`CONTRIBUTING.md`:** Add after "How to contribute" section:
```markdown
## Running tests

Before submitting a PR, run the test suite:

```bash
bash tests/run-all.sh
```

All tests must pass. If you've intentionally changed template files, run `bash tests/test-hashes.sh --reset` to update the baseline.
```

---

## Acceptance Criteria

1. `bash tests/run-all.sh` exits 0 on an unmodified clone of the repo
2. `test-integrity.sh` catches a deliberately broken File Map entry (rename a file, run test, see FAIL)
3. `test-hashes.sh` detects a modified template file after baseline is set
4. `test-smoke.sh` creates and cleans up temp directory without leaving artifacts
5. `test-smoke.sh` memory-sync.sh idempotency check passes (no duplicate commits)
6. All test scripts are executable (`chmod +x`)
7. `tests/.gitignore` excludes `.test-baseline`
8. README.md file tree updated
9. CONTRIBUTING.md includes test instructions
10. Zero dependencies beyond bash + git
11. **No existing content modified** beyond the specified additions to README.md and CONTRIBUTING.md

---

## Idempotency Statement

A second Generator given only this plan file would produce the same test structure, the same checks, and the same pass/fail logic. The exact wording of test output messages may vary, but the checks performed and their pass/fail criteria are fully specified. File structure additions to README.md and CONTRIBUTING.md are specified precisely.

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0082-longmem-test-system.md

3 phases: (1) test runner + integrity tests + hash tests, (2) smoke test,
(3) docs + README/CONTRIBUTING updates. Read all referenced longmem files
BEFORE writing tests. Commit per phase: "Plan 0082 phase N: description"
```
