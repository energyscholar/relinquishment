# Plan 0074: Longmem Automated Tutorial System

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Build an automated tutorial system that teaches longmem methodology through the PTL system itself. Tutorials appear as PTL items at the right time based on session maturity, teach one concept each, and self-delete when the user acknowledges them. Progressive disclosure — users learn what they need when they need it.

## Working directory: `~/software/longmem/`

## Context: read `~/software/relinquishment/plans/0074-longmem-automated-tutorials.md` (this file)

---

## Design Principles

1. **Teach through the system, not about the system.** Each tutorial is a PTL item. Using it teaches PTL. Reading it teaches memory. Deleting it teaches decay. The medium is the message.

2. **Progressive disclosure by session count.** Don't dump everything on Day 1. Tutorials appear when the user's project has matured enough for the concept to be relevant.

3. **Inform, don't prescribe (DN Level 0).** Tutorials reveal patterns and offer techniques. They never pressure, never guilt, never optimize. User decides what to adopt. Storm Protocol applies: if the user is overwhelmed, tutorials should back off, not pile on.

4. **One concept per tutorial.** Each item teaches exactly one thing. Short enough to read in 30 seconds. Links to reference doc for depth.

5. **Self-deleting.** All tutorials are `decay_exempt: true` but include "PTL done: PTL-00N" instruction. They persist until acknowledged, but never block work.

6. **Failure-traced.** Every tutorial maps to a documented failure mode. "We teach this because we failed without it."

---

## Architecture

### New file: `.longmem/docs/patterns.md`

Reference document for methodology patterns. Tutorials point here for depth. Separate from architecture.md (which covers the cache model, not methodology). ~80-100 lines.

### Tutorial trigger: protocol.md Section 13

Add a section to protocol.md with trigger rules. At session start (after step 6 in the start checklist), check if any tutorial trigger has fired. If so, add the tutorial PTL item to ptl.yaml. Maximum ONE new tutorial per session (don't overwhelm).

### Tutorial items: ptl.yaml

Tutorials use IDs PTL-T01 through PTL-T06 (T prefix distinguishes from user items). They're decay_exempt, tier 5 ("Someday" — low visual priority), owner "longmem".

---

## Phase 1: Create `.longmem/docs/patterns.md`

**File:** `.longmem/docs/patterns.md` (NEW)

```markdown
# Methodology Patterns

*Reference for longmem tutorials. Each pattern was learned through documented failure.*

---

## Pattern 1: Plan Before You Build

**Failure:** Sessions 25-26 of the founding project attempted migrations without written plans. Half the active PTL items were dropped. Recovery took 3 sessions.

**Pattern:** Before implementing anything non-trivial, write a short plan:
1. What am I doing? (1-2 sentences)
2. What does "done" look like? (acceptance criteria)
3. What could go wrong? (risk scan)

For simple tasks, this takes 30 seconds in your head. For complex tasks, write it down — even a 5-line plan in the PTL note field catches issues before they cost implementation time.

**Scaling:** As tasks grow, the plan grows:
- Small task: mental checklist (criteria + risks)
- Medium task: PTL note with acceptance criteria
- Large task: separate plan document with red-team review

---

## Pattern 2: Red-Team Before You Ship

**Failure:** Multiple protocol rules were shipped with edge cases that caused failures in production (adaptive thresholds caused oscillation, compression rules had positive feedback loops).

**Pattern:** After planning, ask: "What would break this?" Specifically:
- Positive feedback loops (does the fix make the problem worse?)
- Edge cases at boundaries (empty files, maximum sizes, first/last items)
- Idempotency (can this run twice safely?)
- Recursion depth (can this trigger itself?)

Iterate until remaining issues are LOW severity. Don't ship with HIGH or MEDIUM open.

**Cost:** 2-5 minutes of thinking saves 2-5 sessions of rework.

---

## Pattern 3: Separate Planning from Implementation

**Failure:** When the same session plans and implements, scope creep is universal. The planner adds features mid-implementation. The implementer second-guesses the plan. Confabulation risk rises because there's no external check.

**Pattern (Triad):** The entity that plans should not implement.
- **Auditor role:** Defines objectives, writes acceptance criteria, reviews output
- **Generator role:** Reads the plan, implements exactly what's specified, reports completion

In Claude Code: run Auditor and Generator in separate shells. The plan document is the contract between them. Copy-paste is the authorization gate.

**When to use:** When specs are ambiguous, when scope exceeds one session, when you catch yourself adding "while I'm at it..." features. Start with Pattern 1 (planning). Graduate to Pattern 3 when you need enforcement.

---

## Pattern 4: Structure Over Behavior

**Failure:** "Remember to run the sync script" was forgotten 40% of the time. "Remember to check the line count" was forgotten 60% of the time. Behavioral rules have a half-life of about 3 sessions.

**Pattern:** If something needs to happen reliably, build it into data or scripts — not into instructions that say "remember to do X."

Examples:
- Health warnings in memory-sync.sh (structural) vs "check file sizes" in protocol (behavioral)
- PTL decay rules computed from dates (structural) vs "review old items" (behavioral)
- Dedup guard checking existing sessions (structural) vs "don't run session-end twice" (behavioral)
- Naming conventions: `abcre-criticality-operators.pdf` (structural) vs remembering what `paper.pdf` is (behavioral). Plan numbers scoped per project prevent cross-project collision.

**Test:** If the AI has a bad session and forgets half its instructions, does the thing still work? If yes, it's structural. If no, it's behavioral and fragile.

---

## Pattern 5: Inform, Don't Optimize

**Failure:** An adaptive compression threshold was designed that automatically tightened based on correction frequency. Analysis revealed a positive feedback loop: more compression triggered more corrections, which tightened the threshold further. The feature was killed before shipping.

**Pattern:** Systems that reveal state earn their cost. Systems that automate decisions reduce transparency and risk runaway.

- Health vector SHOWS you where you are → good (you decide what to do)
- Adaptive threshold MOVES you somewhere → dangerous (you lose visibility)
- Correction count displayed → good (you notice patterns)
- Auto-rotation based on count → questionable (removes human judgment)

**Rule of thumb:** If removing the feature would leave the user less informed, keep it. If removing it would leave the user less controlled, kill it.

---

## Pattern 6: Find Your Edge

**Failure:** Projects that stayed in comfortable territory (easy tasks, no corrections) learned nothing. Projects that overreached (too many tasks, too ambitious) crashed repeatedly. The productive zone is at the boundary.

**Pattern:** Your corrections tell you where your edge is. They cluster around the concepts you're still learning. The health vector tells you how much pressure you're under.

- **Too easy:** No corrections accumulating, health vector flat, sessions all ROUTINE. Try a harder tier.
- **Too hard:** Corrections piling up, p > 0.8, sessions crashing. Scale back, consolidate.
- **Productive edge:** 1-2 new corrections per 3 sessions, p around 0.5-0.7, mix of PARADIGM and ROUTINE.

This isn't about optimization. It's about noticing where you are so you can choose where to go.

---

## Pattern 7: Specs First, Then Tests, Then Code

**Failure:** Features built without specifications drifted during implementation. "I'll know it when I see it" led to three rounds of rework on the PTL migration because acceptance criteria were invented after the code was written.

**Pattern:** Write the specification. Then write failing tests that encode the spec. The gap between failing tests and passing tests IS your implementation plan.

1. Write spec (what does the feature do?)
2. Write failing acceptance tests (how do we know it works?)
3. Gap analysis (what's missing between current state and passing tests?)
4. Plan the feature to close the gap
5. Implement → iterate until tests pass
6. Red-team the result (Pattern 2)

**Why this ordering matters:** If you write code first, the tests get written to match the code (confirmation bias). If you write tests first, the code gets written to match the spec. The direction of causation determines whether you're testing what you built or building what you specified.

**Scaling:** For small tasks, the "spec" is a mental model and the "test" is checking the output. For large tasks, formal test files prevent specification drift.
```

---

## Phase 2: Add tutorial triggers to protocol.md

**File:** `.longmem/memory/protocol.md`
**Where:** Replace Section 12 (Protocol Self-Limiting). The self-limiting note moves to line 1 of the new section. Net: Section 12 becomes "Tutorials" and Section 13 becomes "Protocol Self-Limiting" (one line).

**IMPORTANT:** protocol.md is at 197 lines after Plan 0073. This section must replace existing content, not add. The self-limiting section is currently 4 lines (194-197). The tutorial section must fit in ~12 lines to stay under 200. If it doesn't fit, trim trigger descriptions to single-line format.

**Replace Section 12 content with:**

```markdown
## 12. Tutorials (Progressive Disclosure)

At session start, after startup checks, if ptl.yaml has no tutorial items with status ACTIVE:

| Trigger | Item | Teaches |
|---------|------|---------|
| Session ≥3, no plan written yet | PTL-T01 | Planning (Pattern 1) |
| Session ≥5, corrections exist | PTL-T02 | Red-team (Pattern 2) |
| Session ≥8, >3 PTL items | PTL-T03 | Role separation (Pattern 3) |
| Session ≥10 | PTL-T04 | Structure over behavior (Pattern 4) |
| Health vector computed 3+ times | PTL-T05 | Inform not optimize (Pattern 5) |
| Session ≥12, corrections ≥3 | PTL-T06 | Finding your edge (Pattern 6) |
| Session ≥6, PTL items exist | PTL-T07 | Specs first (Pattern 7) |

**Rules:** Max ONE new tutorial per session. Skip if user said "no tutorials." All tutorials are tier 5, decay_exempt, owner "longmem". Add to ptl.yaml only when trigger fires. Reference: `.longmem/docs/patterns.md`.

---

## 13. Protocol Self-Limiting

This file stays under 200 lines. No explanations — only triggers and actions. Compress edge cases into general principles. This is a living document.
```

---

## Phase 3: Create tutorial PTL item templates

**File:** `.longmem/memory/ptl.yaml`
**Action:** Add tutorial item definitions as YAML comments after PTL-000. These are templates — they get uncommented and activated when triggers fire. This avoids bloating the file with inactive items.

**Add after PTL-000 (after the example item comment block):**

```yaml
# ============================================================
# Tutorial items (activated by protocol.md Section 12 triggers)
# Copy, uncomment, and add to items[] when trigger fires.
# ============================================================
#
#  - id: PTL-T01
#    title: "Tutorial: Plan before you build"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      You've had a few sessions now. Before your next non-trivial task, try:
#      1. What am I doing? (1-2 sentences)
#      2. What does "done" look like?
#      3. What could go wrong?
#      Even a 5-line plan catches issues before they cost implementation time.
#      Details: .longmem/docs/patterns.md (Pattern 1)
#      Type "PTL done: PTL-T01" when you've tried it.
#
#  - id: PTL-T02
#    title: "Tutorial: Red-team your plans"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      You have corrections now — proof that mistakes happen. Before implementing,
#      ask: "What would break this?" Check for feedback loops, boundary cases,
#      idempotency, and recursion. Iterate until only LOW issues remain.
#      Details: .longmem/docs/patterns.md (Pattern 2)
#      Type "PTL done: PTL-T02" when you've tried it.
#
#  - id: PTL-T03
#    title: "Tutorial: Separate planning from implementation"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      If you catch yourself adding "while I'm at it..." features, or if tasks
#      keep growing beyond their original scope, try role separation:
#      - Plan in one session (or one shell). Define acceptance criteria.
#      - Implement in a separate session (or shell). Follow the plan exactly.
#      The plan document is the contract. Separation prevents scope creep.
#      Details: .longmem/docs/patterns.md (Pattern 3)
#      Type "PTL done: PTL-T03" when you've tried it.
#
#  - id: PTL-T04
#    title: "Tutorial: Build it into the system, not the instructions"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      If something needs to happen reliably, make it structural — built into
#      scripts or data — not behavioral ("remember to do X").
#      Test: if the AI has a bad session and forgets half its instructions,
#      does the thing still work? If not, it's fragile.
#      Details: .longmem/docs/patterns.md (Pattern 4)
#      Type "PTL done: PTL-T04" when you've tried it.
#
#  - id: PTL-T05
#    title: "Tutorial: Show state, don't automate decisions"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      Your health vector shows system state. That's good — it informs you.
#      Be cautious of features that automatically act on that state.
#      Systems that reveal earn their cost. Systems that decide reduce transparency.
#      Details: .longmem/docs/patterns.md (Pattern 5)
#      Type "PTL done: PTL-T05" when you've tried it.
#
#  - id: PTL-T06
#    title: "Tutorial: Find your productive edge"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      Your corrections tell you where your edge is — they cluster around
#      concepts you're still learning. Your health vector shows pressure.
#      Too easy: no corrections, all ROUTINE. Too hard: corrections piling up.
#      Productive: 1-2 new corrections per 3 sessions, p around 0.5-0.7.
#      This isn't optimization — it's noticing where you are.
#      Details: .longmem/docs/patterns.md (Pattern 6)
#      Type "PTL done: PTL-T06" when you've tried it.
#
#  - id: PTL-T07
#    title: "Tutorial: Write specs and tests before code"
#    tier: 5
#    status: ACTIVE
#    owner: longmem
#    blocked_by: null
#    detail: null
#    source: "tutorial"
#    created: YYYY-MM-DD
#    touched: YYYY-MM-DD
#    decay_exempt: true
#    note: |
#      Next time you have a feature to build, try this order:
#      1. Write what it should do (spec)
#      2. Write a test that fails (encodes the spec)
#      3. Gap analysis: what's missing?
#      4. Build to close the gap
#      Tests written BEFORE code test the spec. Tests written AFTER test the code.
#      Details: .longmem/docs/patterns.md (Pattern 7)
#      Type "PTL done: PTL-T07" when you've tried it.
```

---

## Phase 4: Update PTL-000 to reference tutorials

**File:** `.longmem/memory/ptl.yaml`
**Action:** Add "Planning Discipline" as a third optional layer in PTL-000, and add a note about tutorials.

**In PTL-000's note field, replace the OPTIONAL LAYERS block with:**

```yaml
    note: |
      Welcome! This item teaches you how longmem works. Type "PTL" anytime
      to see your task list. Delete this item when you're comfortable.

      KEY CONCEPTS:
      - Memory lives in .longmem/memory/. MEMORY.md is always loaded (L1 cache).
      - Corrections prevent repeat mistakes. Add them when you're corrected.
      - Sessions are classified PARADIGM (significant) or ROUTINE (incremental).
      - Health vector [p f v d] tracks system state. Computed at session end.
      - Run .longmem/scripts/memory-sync.sh to snapshot to git (L3 backup).

      FIRST STEPS:
      1. Fill in MEMORY.md Identity section with your project details
      2. Start working — longmem learns as you go
      3. After 2-3 sessions, check Health Metrics in MEMORY.md
      4. After 5+ sessions, corrections and PTL will be populated

      TUTORIALS: As your project matures, tutorial items will appear in your
      PTL (tier 5). Each teaches one methodology pattern — planning, red-teaming,
      role separation, and more. They appear when relevant, not all at once.
      Delete them when you've tried the technique. See .longmem/docs/patterns.md.

      OPTIONAL LAYERS (for complex/long projects):
      - Planning Discipline: Plan → red-team → iterate → implement → verify.
        Even simple tasks benefit from "what does done look like?" before starting.
        See .longmem/docs/patterns.md for the full pattern set.
      - Triad (Auditor/Generator role discipline): Auditor plans, Generator
        executes. Separation prevents scope creep and confabulation. Most valuable
        when specs are ambiguous or project exceeds 10 sessions.
      - Dignity Net (governance): Relational health monitoring. Detects
        divergence between stated goals and observable actions. Optional.

      Type "PTL done: PTL-000" to archive this item when ready.
```

---

## Phase 5: Update architecture.md and File Map

### 5a. architecture.md — add patterns.md to "Extending longmem"

**File:** `.longmem/docs/architecture.md`
**Where:** In the "Good extensions" list (line ~279), add:

```markdown
- Methodology patterns (`.longmem/docs/patterns.md`) — planning, red-teaming, role separation
```

### 5b. MEMORY.md template — update File Map

**File:** `.longmem/memory/MEMORY.md`
**Where:** File Map section, add:

```markdown
- `.longmem/docs/patterns.md` — Methodology patterns (planning, red-team, role separation)
```

### 5c. directives.md — add tutorial suppression escape hatch

**File:** `.longmem/directives.md`
**Where:** User Escape Hatches section (line ~116), add:

```markdown
- **"no tutorials"** — Suppress tutorial PTL items from appearing
```

---

## Phase 6: Update README.md

**File:** `README.md`
**Where:** In the "What's Included" section (line ~140), add to the list:

```markdown
- **Progressive tutorials** — Methodology patterns appear as PTL items when your project is ready for them
```

**Where:** In the Stage 2 section (line ~40), add after the corrections paragraph:

```markdown
- Around session 3-5, tutorial items start appearing in your PTL (tier 5). Each teaches one methodology pattern. They're gentle suggestions, not requirements — delete them anytime.
```

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| G1 | patterns.md exists | `[ -f .longmem/docs/patterns.md ]` |
| G2 | patterns.md has 7 patterns | `grep -c '^## Pattern' .longmem/docs/patterns.md` returns 7 |
| G3 | Pattern 1 references failure | `grep -i 'failure\|failure mode\|sessions 25' .longmem/docs/patterns.md` |
| G4 | Pattern 5 mentions feedback loop | `grep -i 'feedback loop\|oscillation' .longmem/docs/patterns.md` |
| G5 | Pattern 6 mentions corrections cluster | `grep -i 'corrections.*cluster\|cluster.*corrections' .longmem/docs/patterns.md` |
| G6 | protocol.md has Section 12 Tutorials | `grep 'Tutorials.*Progressive' .longmem/memory/protocol.md` |
| G7 | protocol.md has trigger table | `grep 'PTL-T01' .longmem/memory/protocol.md` |
| G8 | protocol.md has "no tutorials" suppression | `grep -i 'no tutorials' .longmem/memory/protocol.md` |
| G9 | protocol.md under 200 lines | `[ $(wc -l < .longmem/memory/protocol.md) -lt 200 ]` |
| G10 | ptl.yaml has PTL-T01 template (commented) | `grep 'PTL-T01' .longmem/memory/ptl.yaml` |
| G11 | ptl.yaml has all 7 tutorial templates | `grep -c 'PTL-T0[1-7]' .longmem/memory/ptl.yaml` returns 7 (or 14 for id + title) |
| G12 | PTL-T06 mentions productive edge | `grep -i 'productive edge\|find your.*edge' .longmem/memory/ptl.yaml` |
| G26 | Pattern 7 mentions specs/tests | `grep -i 'spec.*test\|failing test\|gap analysis' .longmem/docs/patterns.md` |
| G27 | PTL-T07 template exists | `grep 'PTL-T07' .longmem/memory/ptl.yaml` |
| G13 | PTL-000 mentions tutorials | `grep -i 'tutorial' .longmem/memory/ptl.yaml` (in PTL-000 note) |
| G14 | PTL-000 mentions Planning Discipline | `grep 'Planning Discipline' .longmem/memory/ptl.yaml` |
| G15 | PTL-000 mentions patterns.md | `grep 'patterns.md' .longmem/memory/ptl.yaml` |
| G16 | architecture.md references patterns.md | `grep 'patterns.md' .longmem/docs/architecture.md` |
| G17 | MEMORY.md template has patterns.md in File Map | `grep 'patterns.md' .longmem/memory/MEMORY.md` |
| G18 | directives.md has "no tutorials" escape hatch | `grep 'no tutorials' .longmem/directives.md` |
| G19 | README.md mentions tutorials | `grep -i 'tutorial' README.md` |
| G20 | README.md Stage 2 mentions tutorial items | `grep -i 'tutorial items\|tutorial.*PTL' README.md` |
| G21 | Each tutorial note references patterns.md | `grep -c 'patterns.md' .longmem/memory/ptl.yaml` returns ≥7 |
| G22 | Each tutorial has "PTL done" instruction | `grep -c 'PTL done.*PTL-T0' .longmem/memory/ptl.yaml` returns 7 |
| G23 | Tutorials are tier 5 | `! grep -A2 'PTL-T0[1-7]' .longmem/memory/ptl.yaml \| grep 'tier: [1-4]'` |
| G24 | Test suite passes | `bash /tmp/longmem-tests/test-longmem.sh ~/software/longmem` — all pass |
| G25 | DN constraint documented | `grep -i 'inform.*not.*prescribe\|inform.*not.*optimize\|Level 0' .longmem/docs/patterns.md` |

One commit: "Add automated tutorial system: 7 progressive methodology patterns"

---

## Notes for Generator

- **protocol.md is at 197 lines. Coordinated compression required (shared with Plan 0075).** This plan adds Section 12 (Tutorials, ~14 lines) and Section 13 (Self-Limiting, 2 lines), replacing current Section 12 (6 lines). Net: +10 lines → 207. To fit under 200, compress these sections:
  - **Section 5 (Corrections):** Remove the code block example (lines 83-87, redundant with directives.md). Merge "L1 (Hot Five)" and "On violation" into one line. Target: 11 lines (save 6).
  - **Section 7 (Integrity):** Remove item 7 (Index growth — future feature, not current). Merge items 4+5 (orphans + broken links → "Orphan/broken: flag files in .longmem/memory/ not in File Map, or linked but missing"). Target: 13 lines (save 5).
  - Total savings: 11 lines. 207 - 11 = 196. Fits.
  - **Leave Sections 3, 8, 11 alone** — Plan 0075 will compress those if needed.
- **Tutorial templates in ptl.yaml are COMMENTS.** They're activated by uncommenting when triggers fire. Don't add them as active items.
- **patterns.md should be ~80-100 lines.** It's reference material, not a textbook. Each pattern: failure (2-3 lines), pattern (3-5 lines), practical guidance (2-3 lines).
- **PTL-000 note field formatting:** YAML multiline (`|`). Preserve exact indentation. The TUTORIALS paragraph goes between FIRST STEPS and OPTIONAL LAYERS.
- **DN constraint:** Pattern 6 (Find Your Edge) must use "noticing" language, not "optimizing" language. "Notice where you are so you can choose" not "push yourself to the boundary."
- **Failure tracing:** Every pattern in patterns.md traces to a real failure. Don't invent failures. The ones listed are documented in architecture.md and session history.
- **Execution order:** Run Plan 0074 BEFORE Plan 0075. Plan 0075 depends on this plan's protocol.md layout.
- Run the test suite AFTER all changes.

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0074-longmem-automated-tutorials.md`. Apply Phases 1-6 to `~/software/longmem/`. Verify G1-G27. One commit.
