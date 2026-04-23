# Plan 0075: Longmem Implicit Task Tracking (Structure as a Service)

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Add two task tracking layers below the existing explicit PTL, so longmem works for the ~75% of users who won't maintain a structured task list. The system reconstructs task state from behavioral signals and presents it naturally. Users interact conversationally; the system handles structure.

## Working directory: `~/software/longmem/`

## Context: read `~/software/relinquishment/plans/0075-longmem-implicit-task-tracking.md` (this file)

---

## Design: Three-Layer Task Tracking

```
Layer 3: Explicit PTL       ← ~20-25% of users (current system, unchanged)
Layer 2: Narrative Summary   ← system-generated "where you are" briefing
Layer 1: Implicit Signals    ← zero-maintenance behavioral extraction
```

**Key principle:** Each layer feeds the one above. Implicit signals inform the narrative. The narrative can be promoted to explicit PTL items. Users enter at whatever layer feels natural. The system adapts to the user's style, not the other way around.

**DN constraint:** Mirror the user's natural style. If they use PTL, support PTL. If they work conversationally, generate narrative summaries. Never force a layer transition. Level 0 (mirror) default. Level 1 (friction) only for: "You mentioned X in 4 sessions but it's not tracked anywhere — want me to note it?"

---

## Phase 1: Implicit Signal Extraction — protocol.md Section 14

**File:** `.longmem/memory/protocol.md`

**Problem:** protocol.md is at ~197 lines (hard cap 200). We cannot add a new section without removing content.

**Solution:** Compress Sections 12-13 (Tutorials + Self-Limiting) into a single section. Current Section 12 (Tutorials) is ~12 lines with a table. Current Section 13 (Self-Limiting) is ~2 lines. Combine into 8 lines by making the tutorial table more compact. This frees ~6 lines for Section 14.

**Replace Sections 12-13 with:**

```markdown
## 12. Tutorials & Progressive Disclosure

At session start, if no tutorial items are ACTIVE in ptl.yaml, check triggers:

| Sessions ≥ | + Condition | Adds | Pattern |
|-----------|-------------|------|---------|
| 3 | no plan written | PTL-T01 | Planning |
| 5 | corrections exist | PTL-T02 | Red-team |
| 8 | >3 PTL items | PTL-T03 | Role separation |
| 10 | — | PTL-T04 | Structure > behavior |
| 3+ health vectors | — | PTL-T05 | Inform not optimize |
| 12 | corrections ≥3 | PTL-T06 | Finding your edge |
| 6 | PTL items exist | PTL-T07 | Specs first |

Max ONE per session. Skip if user said "no tutorials." Templates in ptl.yaml (commented). Reference: `.longmem/docs/patterns.md`.

---

## 13. Open Threads (Implicit Task Tracking)

At session end, after writing the session summary, extract open threads:

1. **Scan** the current session for topics mentioned as incomplete, deferred, or "next time"
2. **Compare** against MEMORY.md Active Sessions — topics in ≥3 of last 5 sessions are high-signal
3. **Update** the `## Open Threads` section in MEMORY.md (max 5 items, one line each)
4. **Promote** — if user says "PTL add" for a thread, move it to ptl.yaml with proper ID

Format: `- [topic] (sessions: N, last: YYYY-MM-DD)` — one line per thread, max 5.

If user says "no tracking" or never references threads, skip this step. Zero-maintenance: threads appear and decay automatically. Stale threads (>3 sessions without mention) drop off.

---

## 14. Protocol Self-Limiting

This file stays under 200 lines. Compress edge cases into general principles.
```

**Line budget check:** Sections 12-14 total ~28 lines. Current sections 12-13 are ~16 lines. Net addition: ~12 lines. Protocol at 197 → ~209. TOO MANY.

**Mitigation:** Compress Section 8 (System Review, currently 9 lines) to 5 lines by removing the numbered sub-steps (they're obvious — "review file map for orphans" doesn't need stating). This saves 4 lines. Also compress Section 11 (Mid-Session Checkpoints, currently 3 lines) to 2 lines. Total savings: 5 lines. Net addition: ~7 lines → protocol at ~204. Still over.

**Further mitigation:** Remove Section 6 header's "Canonical file" line (redundant with directives.md). Remove Section 7 item 7 (Index growth) — it's a future feature, not current protocol. That's 3 more lines saved. Net: protocol at ~201. Close enough — the Generator can tighten further to hit exactly 200 or under.

**IMPORTANT for Generator:** You MUST keep protocol.md under 200 lines. Count carefully. Compress aggressively. Every word must earn its place. If you can't fit Section 13 (Open Threads), reduce it to 4 lines: the scan-compare-update-promote steps as a single paragraph.

---

## Phase 2: MEMORY.md Template — Add Open Threads Section

**File:** `.longmem/memory/MEMORY.md`
**Where:** Add between `## Active Sessions` and `## File Map`.

```markdown
## Open Threads

<!-- Auto-maintained. Topics from recent sessions that remain unresolved. Max 5. -->
<!-- Threads appear when mentioned in 2+ sessions. Drop off after 3 sessions without mention. -->
<!-- Say "PTL add: [thread]" to promote to explicit task tracking. -->

<!-- No threads yet. They'll appear after 2-3 sessions. -->
```

This adds ~5 lines to the template. Template is currently 84 lines → 89 lines. Well under cap.

---

## Phase 3: directives.md — Open Threads Command

**File:** `.longmem/directives.md`
**Where:** After the PTL Commands section (line ~57), add:

```markdown
### Open Threads (Implicit Task Tracking)

Longmem automatically tracks topics that recur across sessions. No user action required.

When the user says:
- **"threads"** — Show current open threads from MEMORY.md
- **"PTL add: [thread topic]"** — Promote a thread to an explicit PTL item
- **"no tracking"** — Disable open threads (remove the section from MEMORY.md)

Open threads are extracted at session end from topics mentioned as incomplete or deferred. They appear when mentioned in 2+ sessions and decay after 3 sessions without mention. Max 5 active threads.
```

---

## Phase 4: architecture.md — Document the Three-Layer Model

**File:** `.longmem/docs/architecture.md`
**Where:** After the PTL section (~line 199), add a new section:

```markdown
## Three-Layer Task Tracking

Not everyone works with structured task lists. longmem offers three layers — users naturally settle into whatever feels right:

**Layer 1 — Implicit (Open Threads):**
Zero maintenance. The system extracts "open threads" from session summaries — topics mentioned as incomplete across multiple sessions. Threads appear in MEMORY.md, decay automatically when no longer discussed. Based on Zeigarnik effect: unfinished tasks persist in attention.

**Layer 2 — Narrative:**
At session start, MEMORY.md's Active Sessions section provides a natural "where was I?" briefing. The system maintains this; the user reads and corrects. No structured input required.

**Layer 3 — Explicit PTL:**
Structured YAML with stable IDs, tiers, decay rules. For users who want full control. ~20-25% of developers voluntarily maintain systems like this (RescueTime 2019, triangulated).

Each layer feeds upward: threads can be promoted to PTL items. PTL items reference threads. The system adapts to the user, not the reverse.

**Design principle:** Structure as a service. The system maintains structure from behavioral signals. Users interact naturally. Forcing structured approaches on unstructured thinkers reduces both satisfaction and output (Czerwinski et al. 2004, Kirton Adaption-Innovation theory).
```

---

## Phase 5: README.md — Update Feature Description

**File:** `README.md`

### 5a. Update "What Is This?" section

**Where:** In the bullet list (~line 13), change the task continuity bullet:

**Old:** `- **Task continuity** — Stable task IDs, five-tier prioritization, automatic decay for stale items`
**New:** `- **Task continuity** — Three layers: implicit thread tracking (zero maintenance), narrative summaries, and optional structured task lists`

### 5b. Update "What's Included" section

**Where:** (~line 144), change the PTL bullet:

**Old:** `- **PTL (Prioritized Task List)** — YAML-based, stable IDs, five tiers, natural language commands`
**New:** `- **Task tracking** — Implicit open threads (zero maintenance) + optional PTL (YAML, stable IDs, five tiers)`

### 5c. Update "Talking to Your AI" section

**Where:** After the Tasks commands (~line 126), add:

```markdown
**Threads:**
- `threads` — Show topics that keep coming up across sessions (auto-tracked)
- `PTL add: [thread]` — Promote a recurring thread to a formal task
```

### 5d. Update "What Changes" table

**Where:** (~line 158), change the task continuity row:

**Old:** `| No task continuity | Stable task IDs, five-tier prioritization |`
**New:** `| No task continuity | Auto-tracked threads + optional structured tasks |`

---

## Phase 6: Update File Map References

### 6a. patterns.md reference to layers

**File:** `.longmem/docs/patterns.md` (created by Plan 0074)

**NOTE:** If Plan 0074 has not been executed yet, skip this sub-phase. The Generator should check whether patterns.md exists before editing it.

**Where:** At the end of Pattern 4 (Structure Over Behavior), add:

```markdown
**See also:** Open threads (implicit task tracking) — a structural approach to task continuity that requires zero user maintenance. Protocol.md Section 13.
```

### 6b. CONTRIBUTING.md acknowledgment

**File:** `CONTRIBUTING.md`
**Where:** In "What's welcome" section, add:

```markdown
- **Task tracking improvements** — Better thread extraction, narrative summaries, PTL integration
```

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| G1 | protocol.md has Section 13 Open Threads | `grep 'Open Threads.*Implicit' .longmem/memory/protocol.md` |
| G2 | protocol.md has scan-compare-update-promote | `grep -c 'Scan\|Compare\|Update\|Promote' .longmem/memory/protocol.md` returns ≥3 |
| G3 | protocol.md under 200 lines | `[ $(wc -l < .longmem/memory/protocol.md) -lt 200 ]` |
| G4 | MEMORY.md template has Open Threads section | `grep 'Open Threads' .longmem/memory/MEMORY.md` |
| G5 | MEMORY.md template under 100 lines | `[ $(wc -l < .longmem/memory/MEMORY.md) -lt 100 ]` |
| G6 | directives.md has "threads" command | `grep '"threads"' .longmem/directives.md` |
| G7 | directives.md has "no tracking" option | `grep 'no tracking' .longmem/directives.md` |
| G8 | architecture.md has Three-Layer section | `grep 'Three-Layer Task Tracking' .longmem/docs/architecture.md` |
| G9 | architecture.md mentions Zeigarnik | `grep -i 'zeigarnik' .longmem/docs/architecture.md` |
| G10 | architecture.md mentions structure as a service | `grep -i 'structure as a service' .longmem/docs/architecture.md` |
| G11 | README.md updated task continuity bullet | `grep -i 'implicit thread\|zero maintenance' README.md` |
| G12 | README.md has "threads" command | `grep 'threads.*auto-tracked\|threads.*coming up' README.md` |
| G13 | README.md "What Changes" updated | `grep -i 'auto-tracked threads' README.md` |
| G14 | Open threads max 5 items documented | `grep 'max 5\|Max 5' .longmem/memory/protocol.md` |
| G15 | Thread decay rule documented | `grep -i '3 sessions.*without\|without mention.*drop\|decay' .longmem/memory/protocol.md` |
| G16 | PTL promotion path documented | `grep -i 'PTL add.*thread\|promote.*PTL' .longmem/directives.md` |
| G17 | DN constraint in architecture.md | `grep -i 'adapts to the user\|mirror.*style\|not the reverse' .longmem/docs/architecture.md` |
| G18 | CONTRIBUTING.md mentions task tracking | `grep -i 'task tracking' CONTRIBUTING.md` |
| G19 | No "threads" without "no tracking" escape | Both present in directives.md |
| G20 | Test suite passes | `bash /tmp/longmem-tests/test-longmem.sh ~/software/longmem` — all pass |

One commit: "Add implicit task tracking: open threads, three-layer model, structure as a service"

---

## Notes for Generator

- **protocol.md line budget is CRITICAL. Coordinated with Plan 0074.** After Plan 0074, protocol.md should be at ~196 lines (it compressed Sections 5 and 7). This plan adds Section 13 (Open Threads, ~12 lines) and renumbers Self-Limiting to Section 14 (2 lines). Net: +12 lines → 208. To fit under 200, compress these sections:
  - **Section 3 (Compression):** Merge steps 1-7 into a compact numbered list (drop "BEFORE doing anything else" — self-evident). Merge "Never compress" + "Overflow" into one line. Target: 12 lines (save 6).
  - **Section 8 (System Review):** Remove numbered sub-steps 2-4 (obvious — "review for orphans/outdated/stalled"). Keep only: trigger condition, ask user, reset counter. Target: 6 lines (save 4).
  - **Section 11 (Checkpoints):** Compress to 2 content lines. Target: 3 lines (save 2).
  - Total savings: 12 lines. 208 - 12 = 196. Fits.
- **PREREQUISITE: Plan 0074 must be executed first.** This plan assumes Sections 12 (Tutorials) and 13 (Self-Limiting) already exist from Plan 0074. If not, include the tutorial trigger table from Plan 0074 in Section 12.
- **Check Plan 0074 status:** Read protocol.md — if Section 12 is "Tutorials," Plan 0074 ran. If Section 12 is "Protocol Self-Limiting," it didn't — include tutorial content.
- **Open Threads is deliberately minimal.** 5 items max, one line each, auto-decay. Don't over-engineer. The value is in the signal extraction, not the data structure.
- **"no tracking" is an escape hatch, not a default.** Most users should get threads automatically. The opt-out exists for users who find it noisy.
- **Thread format:** `- [topic] (sessions: N, last: YYYY-MM-DD)` — compact, scannable, includes recency signal.
- Run the test suite AFTER all changes.

---

## Dependency Note

This plan can be executed independently of Plan 0074 (tutorials). The tutorial trigger table in protocol.md Section 12 is specified in both plans — if 0074 runs first, 0075 preserves its content. If 0075 runs first, it includes the tutorial table from 0074's spec.

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0075-longmem-implicit-task-tracking.md`. Apply Phases 1-6 to `~/software/longmem/`. Verify G1-G20. One commit.
