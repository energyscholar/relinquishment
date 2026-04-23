# Plan 0070: Longmem Dotdir Restructure

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**PTL:** PTL-064
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Move all longmem files into a `.longmem/` dotdir. The project root gets ONE block appended to CLAUDE.md — nothing else. Standard Unix convention: guests don't scatter luggage across every room.

## Working directory: `~/software/longmem/`

## Context: read `~/software/relinquishment/plans/0070-longmem-dotdir-restructure.md` (this file)

---

## Current Structure (RUDE)

```
project-root/
├── CLAUDE.md              ← longmem owns this entirely
├── memory/                ← in project root
├── scripts/               ← in project root
├── docs/                  ← in project root
├── CONTRIBUTING.md        ← in project root
├── feedback.md            ← in project root
└── README.md
```

## Target Structure (POLITE)

```
longmem-repo/                    ← the GitHub repo
├── README.md                    ← repo-level docs
├── CONTRIBUTING.md              ← repo-level
├── LICENSE                      ← repo-level
├── .longmem/                    ← everything that gets installed
│   ├── directives.md            ← full Claude Code directives (NOT named CLAUDE.md)
│   ├── memory/
│   │   ├── MEMORY.md
│   │   ├── corrections.md
│   │   ├── protocol.md
│   │   ├── ptl.yaml
│   │   ├── decisions.md
│   │   ├── session-details.md
│   │   └── people.md
│   ├── scripts/
│   │   └── memory-sync.sh
│   └── docs/
│       ├── architecture.md
│       └── case-study.md
├── install.md                   ← install prompt (plain text)
├── uninstall.md                 ← uninstall prompt (plain text)
├── feedback.md                  ← stays at repo level
└── .gitignore
```

When installed into a user's project:
```
my-project/
├── CLAUDE.md              ← user's own file, longmem block appended
├── .longmem/              ← copied from repo
│   ├── directives.md      ← full protocol (read at session start)
│   ├── memory/
│   ├── scripts/
│   └── docs/
└── ... user's project files ...
```

**Key naming decision:** The directives file is `.longmem/directives.md`, NOT `.longmem/CLAUDE.md`. Two files named CLAUDE.md (root + dotdir) creates ambiguity in every reference. `directives.md` is unambiguous.

---

## Phases

### Phase 1: Move files into .longmem/

Use `git mv` to preserve history (NOT plain `mv`):

1. `mkdir -p .longmem`
2. `git mv CLAUDE.md .longmem/directives.md` (rename + move in one step)
3. `git mv memory .longmem/memory`
4. `git mv scripts .longmem/scripts`
5. `git mv docs .longmem/docs`
6. Do NOT move: `README.md`, `CONTRIBUTING.md`, `LICENSE`, `feedback.md`, `.gitignore`, `.github/`
7. Create new root `CLAUDE.md` with activation block (see below)
8. Add `!.longmem/` to `.gitignore` (prevents common `.*` patterns from excluding the memory system)

**Root CLAUDE.md content (entire file):**

```markdown
<!-- LONGMEM START — do not edit this block manually -->
## Longmem Persistent Memory

Full directives: `.longmem/directives.md` — read at session start for complete protocol.

**Minimum session loop:**
- **Start:** Read `.longmem/memory/MEMORY.md`, then `.longmem/memory/corrections.md`
- **End:** Update `.longmem/memory/MEMORY.md`, run `.longmem/scripts/memory-sync.sh`
<!-- LONGMEM END -->
```

This block is deliberately self-sufficient. Even if Claude never reads `directives.md`, the core read/write loop works. The full protocol provides depth but isn't a single point of failure.

### Phase 2: Update all internal path references

Every file inside `.longmem/` that references paths must use `.longmem/`-prefixed paths, because Claude's working directory is the project root.

**Path vs Name conversion rules** (Generator must follow these exactly):
- **Convert** if: backticked AND could be a file argument to a tool; inside a shell command (wc, git, cat, grep); after "Read"/"Open"/"Check" as an instruction to Claude
- **Leave** if: bare name in prose describing what the file IS (e.g., "MEMORY.md is the L1 cache"); in a heading; in a description (e.g., "the corrections system")
- **Test:** Could this string be copy-pasted as a path into a terminal or editor? If yes → convert. If no → leave.

**`.longmem/directives.md`** (was CLAUDE.md) — change ALL path occurrences:
- `memory/MEMORY.md` → `.longmem/memory/MEMORY.md`
- `memory/corrections.md` → `.longmem/memory/corrections.md`
- `memory/protocol.md` → `.longmem/memory/protocol.md`
- `memory/ptl.yaml` → `.longmem/memory/ptl.yaml`
- `memory/decisions.md` → `.longmem/memory/decisions.md`
- `memory/session-details.md` → `.longmem/memory/session-details.md`
- `memory/people.md` → `.longmem/memory/people.md`
- `scripts/memory-sync.sh` → `.longmem/scripts/memory-sync.sh`
- `memory/` (directory reference in paths) → `.longmem/memory/`

Also update the Memory System header:
```markdown
You have a persistent memory directory at `.longmem/memory/`. Its contents persist across conversations.
```

**`.longmem/memory/MEMORY.md`** — File Map section:
- All `memory/X` paths → `.longmem/memory/X`

**`.longmem/memory/protocol.md`** — change ALL path occurrences per the conversion rules above. Key instances:
- `Read `MEMORY.md`` → `Read `.longmem/memory/MEMORY.md``
- `corrections.md` (in "Read `corrections.md`" instructions) → `.longmem/memory/corrections.md`
- `session-details.md` (in move/archive instructions) → `.longmem/memory/session-details.md`
- `ptl.yaml` (in "read `ptl.yaml`" instructions) → `.longmem/memory/ptl.yaml`
- `scripts/memory-sync.sh` → `.longmem/scripts/memory-sync.sh`
- `wc -l memory/MEMORY.md` → `wc -l .longmem/memory/MEMORY.md`
- `memory/` in git commands → `.longmem/memory/`
- Leave prose like "MEMORY.md line cap: 200 lines" unchanged (that's a name, not a path)
- Leave headings unchanged

**`.longmem/scripts/memory-sync.sh`** — change:
- `git add memory/ CLAUDE.md` → `git add .longmem/`

**Verification step after Phase 2:** Run these checks before proceeding:
```bash
# Should return 0 — no backtick-quoted bare memory/ paths remain in directives
grep -cP '`memory/' .longmem/directives.md || true
# Should return 0 — no backtick-quoted bare memory/ paths remain in protocol
grep -cP '`memory/' .longmem/memory/protocol.md || true
# Should return matches — .longmem/ paths are present
grep -c '.longmem/' .longmem/directives.md
grep -c '.longmem/' .longmem/memory/protocol.md
```

### Phase 3: Create install.md and uninstall.md

**`install.md`** — a prompt users paste into Claude Code:

```markdown
# Longmem Install Prompt

Paste this into Claude Code in your project directory:

---

Set up longmem persistent memory in this project. Steps:

1. If `.longmem/` already exists, stop and ask me what to do (might be an existing install)
2. Clone https://github.com/energyscholar/longmem.git to /tmp/longmem-install
3. Copy the `.longmem/` directory from the clone into this project root
4. If this project has no CLAUDE.md, create one. Append this block to CLAUDE.md:

<!-- LONGMEM START — do not edit this block manually -->
## Longmem Persistent Memory

Full directives: `.longmem/directives.md` — read at session start for complete protocol.

**Minimum session loop:**
- **Start:** Read `.longmem/memory/MEMORY.md`, then `.longmem/memory/corrections.md`
- **End:** Update `.longmem/memory/MEMORY.md`, run `.longmem/scripts/memory-sync.sh`
<!-- LONGMEM END -->

5. Run: chmod +x .longmem/scripts/memory-sync.sh
6. Run: git init (if not already a git repo)
7. If .gitignore has a `.*` pattern, add `!.longmem/` to prevent exclusion
8. Open `.longmem/memory/MEMORY.md` and ask me to fill in: project name, start date, goal, and key people.
9. Delete /tmp/longmem-install

---
```

**`uninstall.md`** — a prompt users paste into Claude Code:

```markdown
# Longmem Uninstall Prompt

Paste this into Claude Code in your project directory:

---

Remove longmem from this project. Steps:

1. Run `.longmem/scripts/memory-sync.sh` to create a final git snapshot
2. Show me what will be deleted (list files in .longmem/)
3. Ask for confirmation
4. After confirmation: rm -rf .longmem/
5. Remove the block between <!-- LONGMEM START --> and <!-- LONGMEM END --> from CLAUDE.md
6. If CLAUDE.md is now empty, delete it
7. Confirm removal is complete. Note: memory history is preserved in git — recoverable via `git log --all -- .longmem/`

---
```

### Phase 4: Update README.md

- Update file tree diagram to show `.longmem/` structure with `directives.md` (not CLAUDE.md)
- Update Quickstart:
  - **New project:** `git clone https://github.com/energyscholar/longmem.git my-project` still works (repo has root CLAUDE.md)
  - **Existing project:** Paste the install prompt (reference install.md)
- Update "Why is there no setup script?" to reference install prompt
- Add "Uninstall" section referencing uninstall.md
- Update all path references in body text (`memory/` → `.longmem/memory/`, `scripts/` → `.longmem/scripts/`, etc.)
- Update Troubleshooting paths
- Change all references from "CLAUDE.md" (meaning longmem's directives) to `.longmem/directives.md`
- **Add "How It Works — Quick Reference" section** (for confused Claude Code instances). This section is the recovery path — if Claude loses context, it can read README.md and understand the system. Include:
  - Where memory lives: `.longmem/memory/`
  - What to read first: `.longmem/directives.md` → `.longmem/memory/MEMORY.md`
  - How to recover from context loss: read `.longmem/directives.md`, then `.longmem/memory/MEMORY.md`, then continue
  - How to sync: `.longmem/scripts/memory-sync.sh`
  - Key file purposes: 1-line each for MEMORY.md, corrections.md, protocol.md, ptl.yaml
  - Keep this section under 20 lines — it's a map, not a manual

### Phase 5: Update docs/

- **`.longmem/docs/architecture.md`** — update all path references; change "CLAUDE.md" references (meaning longmem's directives) to `directives.md`
- **`.longmem/docs/case-study.md`** — update all path references; same CLAUDE.md → directives.md rename

### Phase 6: Update test suite

- Update `/tmp/longmem-tests/test-longmem.sh` — all path references change:
  - `$DIR/memory/` → `$DIR/.longmem/memory/`
  - `$DIR/scripts/` → `$DIR/.longmem/scripts/`
  - `$DIR/CLAUDE.md` (for longmem's directives) → `$DIR/.longmem/directives.md`
  - Root `$DIR/CLAUDE.md` check → verify activation block exists (T02 becomes: root CLAUDE.md has LONGMEM START marker)
- Add T04: Root CLAUDE.md contains LONGMEM START activation block
- Verify test suite passes on restructured repo

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| G1 | `.longmem/` directory exists | `[ -d .longmem ]` |
| G2 | No `memory/` in project root | `[ ! -d memory ]` |
| G3 | No `scripts/` in project root | `[ ! -d scripts ]` |
| G4 | No `docs/` in project root | `[ ! -d docs ]` |
| G5 | Root CLAUDE.md has activation block | `grep "LONGMEM START" CLAUDE.md` |
| G6 | Root CLAUDE.md references directives.md | `grep ".longmem/directives.md" CLAUDE.md` |
| G7 | `.longmem/directives.md` exists (NOT .longmem/CLAUDE.md) | `[ -f .longmem/directives.md ] && [ ! -f .longmem/CLAUDE.md ]` |
| G8 | No backtick-quoted bare `memory/` paths in directives.md | `` grep -cP '`memory/' .longmem/directives.md `` returns 0 |
| G9 | directives.md uses .longmem/ prefix paths | `grep ".longmem/memory/MEMORY.md" .longmem/directives.md` matches |
| G10 | MEMORY.md File Map uses .longmem/ paths | `grep ".longmem/memory/" .longmem/memory/MEMORY.md` matches |
| G11 | protocol.md uses .longmem/ paths | `grep ".longmem/" .longmem/memory/protocol.md` matches |
| G12 | No backtick-quoted bare `memory/` paths in protocol.md | `` grep -cP '`memory/' .longmem/memory/protocol.md `` returns 0 |
| G13 | memory-sync.sh adds .longmem/ | `grep "git add .longmem/" .longmem/scripts/memory-sync.sh` matches |
| G14 | install.md exists and references .longmem/ | `[ -f install.md ] && grep ".longmem/" install.md` |
| G15 | uninstall.md exists and references LONGMEM START | `[ -f uninstall.md ] && grep "LONGMEM START" uninstall.md` |
| G16 | README.md file tree shows .longmem/ | `grep ".longmem/" README.md` matches |
| G17 | README.md file tree shows directives.md | `grep "directives.md" README.md` matches |
| G18 | README has recovery reference section | `grep -q "Quick Reference\|How It Works" README.md` |
| G19 | .gitignore has !.longmem/ | `grep "!.longmem/" .gitignore` matches |
| G20 | Root CLAUDE.md has inline bootstrap (minimum session loop) | `grep "Minimum session loop" CLAUDE.md` matches |
| G21 | install.md block matches root CLAUDE.md block | Both contain "directives.md" reference — manually verify identical |
| G22 | Test suite updated for .longmem/ paths | `grep ".longmem/memory/" /tmp/longmem-tests/test-longmem.sh` matches |
| G23 | Test suite passes on restructured repo | `bash /tmp/longmem-tests/test-longmem.sh ~/software/longmem` — all tiers pass |

One commit: "Restructure: move all files into .longmem/ dotdir, rename CLAUDE.md→directives.md, add install/uninstall prompts"

---

## Notes for Generator

- Use `git mv` for ALL moves. Do NOT use plain `mv`. History preservation matters.
- The `.longmem/` directory will be hidden by default in most file browsers. This is intentional — it's infrastructure, not content.
- The `.github/` directory stays at repo root (it's GitHub infrastructure, not longmem infrastructure).
- Follow the **path vs name conversion rules** in Phase 2 exactly. When in doubt: "Could I paste this into a terminal?" If yes → convert. If no → leave.
- Run the Phase 2 verification greps before moving to Phase 3. Fix any remaining bare `memory/` paths.
- The install.md and uninstall.md activation blocks must be IDENTICAL to the root CLAUDE.md block. Copy-paste, don't retype.

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0070-longmem-dotdir-restructure.md`. Apply Phases 1-6 to `~/software/longmem/`. Verify G1-G23. One commit.
