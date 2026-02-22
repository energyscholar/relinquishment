# SE Improvement — Generator Chain Index

**Created:** 2026-02-21
**Total chains:** 9 (A through I)
**Total estimated time:** 70-110 hours at 10% allocation
**Review gates:** 3 (after B, F, G)

---

## Dependency Graph

```
Chain A (quick wins, 75 min)
  ├──→ Chain B (c8 spike, 15 min)  ⛔ REVIEW GATE
  │      └──→ Chain E (coverage, 2-3 hrs)
  │             └──→ Chain F (framework eval, 4-8 hrs)  ⛔ REVIEW GATE
  └──→ Chain C (npc-persona linting, 3 hrs)
         ├──→ Chain D (traveller linting, 2-3 hrs)  [can parallel with E]
         └──→ Chain G (restructure recon, 2 hrs)  ⛔ REVIEW GATE
                └──→ Chain H (restructure execute, 6-10 hrs)
                       └──→ Chain I (TypeScript, 2-4 hrs)
```

**Parallelizable:** After Chain C, Chains D and E can run simultaneously (different repos / independent concerns). Chain F can start after E completes.

---

## Chain Execution Order

| Chain | Plan | Plans covered | Repo | Time | Gate? |
|-------|------|--------------|------|------|-------|
| **A** | 0026 | 006A + 007 | npc + traveller | 75 min | No |
| **B** | 0027 | 003 Phase 0 | npc | 15 min | **YES** |
| **C** | 0028 | 002.1 + 006B | npc | 3 hrs | No |
| **D** | 0029 | 002.2 | traveller | 2-3 hrs | No |
| **E** | 0030 | 004 | npc | 2-3 hrs | No |
| **F** | 0031 | 003 Phases 1-4 | npc + traveller | 4-8 hrs | **YES** |
| **G** | 0032 | 005 Phase 0 | npc | 2 hrs | **YES** |
| **H** | 0033 | 005 Phases 1-3 | npc | 6-10 hrs | No |
| **I** | 0034 | 001 Phase 1 | npc | 2-4 hrs | No |

---

## Handoff Prompts

### Chain A
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0026-se-chain-A-quick-wins.md
Two tasks: (1) commitlint + .gitmessage in npc-persona,
(2) package-lock tracking in traveller.
Report per format at end of plan.
```

### Chain B
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0027-se-chain-B-c8-spike.md
One task: test c8 coverage with npc-persona's custom test runner.
This is a decision gate. Report the binary result.
```

### Chain C
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0028-se-chain-C-npc-linting.md
Two tasks: (1) ESLint 9 + Prettier in npc-persona,
(2) husky + lint-staged + commitlint hook.
Report per format at end of plan.
```

### Chain D
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0029-se-chain-D-traveller-linting.md
One task: ESLint 9 + Prettier for traveller backend.
Two config blocks: Node.js (lib/) + browser (public/).
Report per format at end of plan.
```

### Chain E
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0030-se-chain-E-coverage.md
One task: c8 coverage with ratchet threshold in npc-persona.
Prerequisite: Chain B confirmed c8 works.
Report per format at end of plan.
```

### Chain F
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0031-se-chain-F-framework-eval.md
Evaluation task: benchmark runners, triage orphaned tests,
produce decision document. This is a decision gate.
Report per format at end of plan.
```

### Chain G
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0032-se-chain-G-restructure-recon.md
Reconnaissance: import graph, __dirname audit, chat-tui analysis.
This is a decision gate. Report the blueprint.
```

### Chain H
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0033-se-chain-H-restructure-execute.md
Execute the restructure per the approved blueprint from Chain G.
9 batches, each atomic. All-or-nothing rollback if needed.
Report per format at end of plan.
```

### Chain I
```
You are the Generator. Read and execute
~/software/relinquishment/plans/0034-se-chain-I-typescript.md
One task: TypeScript setup (allowJs + checkJs) in npc-persona.
No file renames. JSDoc-only. Establish error baseline.
Report per format at end of plan.
```

---

## Review Gate Decisions

### After Chain B (c8 spike):
- If c8 WORKS → proceed to Chains C/D/E as planned
- If c8 DOESN'T WORK → replanning needed for Plans 003/004

### After Chain F (framework eval):
- If recommendation is Option A (keep runner) → proceed to Chain G
- If recommendation is Option B or C → new chain needed for migration before Chain G

### After Chain G (restructure recon):
- Bruce decides: PROJECT_ROOT vs per-file fixup
- Bruce decides: src/data/ naming
- Bruce decides: chat-tui.js placement
- Then Chain H can proceed

---

## What Happens After Chain I?

Plan 001 Phase 2+ (JSDoc annotations) is ongoing work, not a Generator chain. It happens file-by-file alongside normal development. No plan file needed.

Traveller-specific items (coverage, TypeScript, framework consolidation) can be planned as separate chains once npc-persona is complete.
