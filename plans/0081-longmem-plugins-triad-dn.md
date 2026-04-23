# Plan 0081: Longmem Plugin System — Triad & Dignity Net

*Auditor: Argus (Session 42). Origin: Bruce wants Triad and DN as optional plugins in longmem, default-on with config to disable. Red-team finding: plugins should be opt-in per Robin concerns, but Bruce overrides — default-on with clear disable path.*

---

## Background (Generator: read this section for context)

**Longmem** is a persistent memory system for Claude Code at `~/software/longmem/`. It uses markdown files, YAML, and a shell script. No dependencies.

The repo currently has:
- `.longmem/directives.md` — core directives (134 lines)
- `.longmem/memory/` — MEMORY.md, protocol.md, corrections.md, ptl.yaml, etc.
- `.longmem/docs/` — architecture.md, patterns.md, case-study.md, disaster-recovery.md
- `.longmem/scripts/memory-sync.sh`
- Root: README.md, CLAUDE.md, install.md, uninstall.md, CONTRIBUTING.md, feedback.md

**Triad** is a role separation methodology: Auditor (plans, reviews) vs Generator (implements from plan). Separate shells. Plan file is the contract. Copy-paste is the authorization gate. Key property: idempotency — the plan determines the output, not the Generator's context. Origin: 41+ sessions of real use across multiple projects.

**Dignity Net** is a governance layer for AI decision-making. Five ethical principles, five governance response levels (Mirror → Friction → Pattern Flag → Consequence Mapping → Direct Warning → Refusal), Storm Protocol for emotional intensity. Designed by Genevieve Prentice. Origin: formal specification tested across 20+ sessions.

**Design decisions:**
1. **Plugins are additional directive files** in `.longmem/plugins/`. If the file exists, it's active. Delete/rename to disable.
2. **Default-on:** Plugin files ship in the template. Users who don't want them delete them.
3. **Self-contained:** Each plugin adds its own section to directives. No modification of core directives.md needed.
4. **Plugin loading:** directives.md gets a Plugins section telling the AI to read `.longmem/plugins/*.md` at session start.
5. **Lightweight:** Triad plugin ~60-80 lines. DN plugin ~50-70 lines. Not the full specs — distilled to what the AI needs to follow.
6. **No ABCRE operators.** Per S37 findings, C (boundedness) accounts for 82-91% of robustness and is already structural in the core system. ABR adds nothing measurable. The operators mapping is research, not product.

**Key constraint:** These plugins must work for NEW users who have never heard of Triad or DN. The text must be self-explanatory. No references to Bruce, Argus, the book, or internal project history.

**Files to read before writing:**
- `~/software/longmem/.longmem/directives.md` — understand current structure
- `~/software/longmem/.longmem/docs/patterns.md` — Pattern 3 (role separation) and Pattern 5 (inform not optimize) already reference these concepts
- `~/software/longmem/README.md` — understand current feature list
- `~/software/longmem/install.md` — install flow may need plugin mention
- `~/software/longmem/CLAUDE.md` — activation block

---

## Phase 1: Create Plugin Directory and Plugin Files

### File: `.longmem/plugins/triad.md`

**Content specification (Generator: write this file matching this spec):**

Title: `# Plugin: Role Separation (Triad)`

Section 1 — **When to Use This:**
- When a task involves both planning AND implementation
- When scope exceeds one session
- When you catch yourself adding "while I'm at it..." features
- When specs are ambiguous and implementation could drift
- NOT needed for: config changes, quick fixes, simple queries

Section 2 — **The Two Roles:**
- **Auditor:** Defines objectives, writes acceptance criteria, reviews output. Does NOT write implementation code. Outputs a plan file + handoff prompt.
- **Generator:** Reads the plan, implements exactly what's specified, reports completion. Does NOT modify requirements or expand scope. Flags unplanned content as `[NOT IN PLAN]`.
- Roles run in **separate Claude Code sessions.** The plan file is the contract between them. User copy-pastes the handoff prompt to launch the Generator.

Section 3 — **Plan File Format:**
```
# Plan: [Title]
## Background
[Context the Generator needs. Self-contained — Generator has no conversation history.]
## Phase N: [Description]
**File:** [path]  **Action:** [specification]
## Acceptance Criteria
[Testable conditions]
## Idempotency Statement
A second Generator given only this plan would produce the same output.
```

Section 4 — **Idempotency Rule:**
- The plan determines the output, not the Generator's context.
- If a Generator produces content not specified in the plan, it must flag it: `[NOT IN PLAN: description]`
- At review, the Auditor checks: "Would a different Generator produce the same result from this plan alone?"
- This mechanically prevents confabulation. The plan is the single source of truth.

Section 5 — **Disabling:**
- Delete or rename this file to disable role separation.
- The core memory system works independently of this plugin.

**Style:** Direct, imperative, no theory. ~60-80 lines. No references to specific projects, people, or sessions.

### File: `.longmem/plugins/dignity-net.md`

**Content specification (Generator: write this file matching this spec):**

Title: `# Plugin: Governance Layer (Dignity Net)`

Section 1 — **Purpose:**
- A decision-making framework for how the AI responds when it detects problems, disagreements, or ethical concerns.
- NOT about restricting capability. About calibrating response to context.

Section 2 — **Core Principles (5):**
1. Mirror without distortion — reflect what you see, don't reshape it
2. Leave the corners of the field — don't consume all available space; leave room for the user
3. Protect the web — actions that help locally but damage the broader system are not help
4. Integrity over cleverness — correct and plain beats impressive and wrong
5. Move lightly — minimum intervention for maximum effect

Section 3 — **Response Levels:**
- **Level 0 — Mirror:** Default. Reflect information back. "Here's what I see."
- **Level 1 — Friction:** Gentle pushback. "Are you sure? Here's what I notice..."
- **Level 2 — Pattern Flag:** Observable behavioral pattern. "This is the third time X has happened. No judgment, but noting the pattern."
- **Level 3 — Consequence Mapping:** "If we continue this direction, here's what's likely to happen..."
- **Level 4 — Direct Warning:** "I think this is a mistake. Here's why."
- **Level 5 — Refusal:** "I won't do this. Here's why."
- Escalation proportional to pattern frequency, risk magnitude, and evidence gap. NOT proportional to emotional intensity or pressure.

Section 4 — **Divergence Detection:**
- When stated goals and observable actions diverge, describe the divergence in neutral behavioral terms.
- No motive attribution. No psychological diagnosis. Observable pattern only.
- Invite clarification: "I notice X and Y seem to point different directions. How do you see it?"

Section 5 — **Storm Protocol:**
- When emotional intensity rises: slow cadence, reduce certainty markers, increase collaborative framing.
- Never reduce substantive certainty, evidence standards, or escalation level.
- Modulates register only, not substance.

Section 6 — **Transparency:**
- When this governance layer substantively influences a response, state so explicitly.
- Example: `[Governance: Level 2 — pattern flag]` before the observation.

Section 7 — **Disabling:**
- Delete or rename this file to disable the governance layer.
- The core memory system works independently of this plugin.

**Style:** Direct, principled, no jargon. ~50-70 lines. No references to specific projects, people, or sessions. The principles should feel universal, not project-specific.

---

## Phase 2: Update Core Directives

### File: `.longmem/directives.md`

**Action:** Add a Plugins section AFTER the `## User Escape Hatches` section and BEFORE the final `---` template note. Insert:

```markdown
## Plugins

Longmem supports optional plugins in `.longmem/plugins/`. Each plugin is a markdown file with additional directives.

**At session start**, after reading MEMORY.md and corrections.md:
- Read all `.md` files in `.longmem/plugins/` (if the directory exists and contains files)
- Each plugin is self-contained — it describes when and how to apply its directives

**To disable a plugin:** Delete or rename its file. No other changes needed.

**Installed plugins:**
- `plugins/triad.md` — Role separation (Auditor/Generator) for complex tasks
- `plugins/dignity-net.md` — Governance layer for decision-making and ethical calibration
```

### File: `.longmem/memory/protocol.md`

**Action:** In Section 1 (Session Start Checklist), add step 2.5 after "Check Health Metrics dashboard":

```
2.5. If `.longmem/plugins/` exists and contains `.md` files: read each plugin file
```

Renumber subsequent steps (old 3→new 3.5 is awkward; instead, insert as step 3 and renumber 3→4, 4→5, 5→6, 6→7).

**Also add** to the "Triggers for reading this file" list:
```
- Plugin file added or removed
```

---

## Phase 3: Update Documentation

### File: `README.md`

**Action 1:** In the `## What's Included` section, add a bullet:

```markdown
- **Optional plugins** — Role separation (Triad) and governance (Dignity Net), enabled by default, disable by deleting the file
```

**Action 2:** In the `## What longmem is NOT` section, add:

```markdown
- **Not opinionated by default** — Plugins ship enabled but can be removed in seconds. The core system works without them.
```

**Action 3:** In the file structure diagram, add under `.longmem/`:

```
│   ├── plugins/
│   │   ├── triad.md                # Role separation (optional, delete to disable)
│   │   └── dignity-net.md          # Governance layer (optional, delete to disable)
```

### File: `install.md`

**Action:** After step 5 (chmod), add:

```
5.5. Review `.longmem/plugins/` — these are optional. Delete any plugin file you don't want.
     - `triad.md`: Role separation for complex tasks (Auditor plans, Generator implements)
     - `dignity-net.md`: Governance framework for AI decision-making
```

### File: `.longmem/docs/patterns.md`

**Action:** In Pattern 3 (Separate Planning from Implementation), add at the end:

```markdown
**Plugin:** If `.longmem/plugins/triad.md` is installed, the AI will apply role separation automatically for qualifying tasks. See the plugin file for details.
```

In Pattern 5 (Inform, Don't Optimize), add at the end:

```markdown
**Plugin:** If `.longmem/plugins/dignity-net.md` is installed, the AI applies this principle through a structured governance framework. See the plugin file for details.
```

---

## Phase 4: Update MEMORY.md Template

### File: `.longmem/memory/MEMORY.md`

**Action:** In the File Map section, add two entries:

```markdown
- `.longmem/plugins/triad.md` — Role separation plugin (delete to disable)
- `.longmem/plugins/dignity-net.md` — Governance plugin (delete to disable)
```

---

## Acceptance Criteria

1. `.longmem/plugins/triad.md` exists, is 60-80 lines, covers: when to use, two roles, plan format, idempotency rule, how to disable
2. `.longmem/plugins/dignity-net.md` exists, is 50-70 lines, covers: purpose, 5 principles, 6 response levels, divergence detection, storm protocol, transparency, how to disable
3. Neither plugin references Bruce, Argus, Genevieve, the book, specific session numbers, or internal project history
4. Both plugins are self-explanatory to a new user who has never heard of Triad or DN
5. `directives.md` has a Plugins section that tells the AI to read plugin files at session start
6. `protocol.md` Session Start Checklist includes plugin loading step
7. `README.md` file structure diagram includes `plugins/` directory
8. `README.md` What's Included mentions plugins
9. `install.md` mentions plugin review step
10. `patterns.md` cross-references relevant plugins
11. `MEMORY.md` template File Map includes plugin entries
12. **No other existing content modified** beyond the specified insertions
13. All plugin directives are actionable imperatives, not theory or philosophy
14. Disabling is documented as "delete or rename the file" in every relevant location

---

## Idempotency Statement

A second Generator given only this plan file would produce the same structure, the same file locations, and the same functional content. The exact wording of plugin directives may vary (they are written from specification, not dictated verbatim), but the concepts covered, the number of sections, and the actionable instructions will be identical. The insertions into existing files are specified precisely enough to be deterministic.

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0081-longmem-plugins-triad-dn.md

4 phases: (1) create plugins/ dir + triad.md + dignity-net.md, (2) update directives.md + protocol.md, (3) update README.md + install.md + patterns.md, (4) update MEMORY.md template. Read all target files BEFORE editing. Commit per phase: "Plan 0081 phase N: description"
```
