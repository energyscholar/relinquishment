# Plan 0282 — T1a Governance-Gap Ordering in Hook

**Status:** PROMPT READY
**Rating:** 8/10
**Annealing:** MED LOW LOW
**Target:** `manuscript/00-front/hook.tex` (p1 — 8th grade)
**Takeaway:** T1a (derive governance necessity before naming the Custodian)

## Rationale

The hook currently names "a custodian" in paragraph 2 (line 13) — before the reader understands *why* such a thing needs to exist. The governance gap (no person/government should hold this) is the argument; the Custodian is the conclusion. Reversing the order lets the reader derive the necessity before meeting the entity.

Insight extracted from external review: **show the gap before filling it.** The reader should feel "someone needs to hold this" before learning that someone already does.

## Scope

Three surgical word-level edits. No structural changes. No paragraph moves. ~15 words changed total.

## Changes

### Change 1 — Line 13: defer recipient naming
**Current:**
```
handed the master cryptographic keys of a one-of-a-kind machine to a custodian they had built for the purpose, and walked away.
```
**New:**
```
handed the master cryptographic keys of a one-of-a-kind machine to something they had built for the purpose, and walked away.
```

### Change 2 — Line 19: defer entity label
**Current:**
```
The custodian is the next emergent layer above that: a coherent behavior of the stack, bound by a charter, acting in public.
```
**New:**
```
The next emergent layer above that is a coherent behavior of the stack, bound by a charter, acting in public.
```

### Change 3 — Line 21: defer entity label
**Current:**
```
by the time you reach the top, emergent layers compound into a coherent custodian.
```
**New:**
```
by the time you reach the top, emergent layers compound into something coherent.
```

### First appearance of "custodian" — Line 27 (unchanged)
```
The custodian in this story is a trustee in that older sense: something that holds, on behalf of everyone, what no one should own.
```

The word "custodian" now first appears *after* the reader has absorbed: the technology stack, the governance danger ("what would happen if any single government controlled it"), and the act of relinquishment. The kenosis paragraph names the entity in the same breath as its trustee lineage.

## C-check

All three changes work under possibilities A, B, and C. "Something they had built" is true under all three. No new claims introduced.

## Acceptance criteria

1. The word "custodian" does not appear before line 27
2. No meaning is lost — every concept still present
3. Reading level remains ≤ 8th grade
4. Word count change ≤ ±5 words

---

## Generator Prompt

```
You are the Generator for Plan 0282.

Read: ~/software/relinquishment/plans/0282-t1a-governance-gap-hook.md

Execute the 3 changes specified in the plan against manuscript/00-front/hook.tex.
Verify all 4 acceptance criteria after editing. Commit: "Plan 0282: T1a governance-gap ordering — defer Custodian naming in hook"
Build and push.
```
