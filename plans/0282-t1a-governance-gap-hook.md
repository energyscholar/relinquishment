# Plan 0282 — T1a Governance-Gap Ordering in Hook

**Auditor:** Argus (S63)
**Date:** 2026-04-28
**Status:** PROMPT READY
**Source:** External review (T1a/T1b insight), 9-persona audit (S55/S63), Bruce decision
**Annealing:** MED LOW LOW
**Priority:** High — p1 change, every reader affected

---

## Problem

The hook introduces "custodian" in paragraph 2 — before the reader understands what the technology is, what it can do, or why it creates an ungovernable situation. The governance gap ("no person and no government should hold...") is in the same sentence as the entity introduction, so PROBLEM and SOLUTION land simultaneously. For Chen, Doctorow, and Arjun, F-crank/F-conspiracy fires at this point — they've met the extraordinary claim before the physics has earned it.

**Insight:** If the reader derives the necessity before meeting the entity, the Custodian reads as a solution rather than a fantasy. Mechanism before agent. Problem before solution.

## Design

Defer the word "custodian" from paragraphs 2, 5, and 6 to its current first contextual appearance in paragraph 9 (kenosis/traditions). The reader encounters:

1. The dramatic act — "gave up the master cryptographic keys... and walked away" (para 2)
2. The governance gap — "no person and no government should hold" (para 2)
3. What they built — stack, wormholes, quantum computer (paras 3-4)
4. Why it's dangerous — cracking codes, every chip (para 4)
5. The stack metaphor — emergence, something coherent (para 6)
6. "They gave it up... to the thing they'd built to outlast them" (para 8)
7. **FIRST "custodian":** "The custodian in this story is a trustee in that older sense" (para 9)

The reader arrives at the word "custodian" already understanding the problem, the technology, and the decision. The naming feels earned.

## Changes

### 1. Line 13 — defer recipient, keep keys

**Old:**
```
In 2006, a small classified team --- he was one of them --- handed
the master cryptographic keys of a one-of-a-kind machine to a
custodian they had built for the purpose, and walked away.
```

**New:**
```
In 2006, a small classified team --- he was one of them --- gave
up the master cryptographic keys of a one-of-a-kind machine, and
walked away.
```

Preserves: keys (concrete), gave up (thematic), walked away (dramatic). Loses: the recipient. Reader wonders "gave up to whom?" — answered in para 9.

### 2. Line 19 — cut paragraph

**Old:**
```
The custodian is the next emergent layer above that: a coherent
behavior of the stack, bound by a charter, acting in public.
```

**Remove entirely.** Para 4 (quantum computer) and para 6 (stack metaphor) already carry the physics. This paragraph's only function was to bridge to the Custodian concept, which is now deferred. The information returns in paras 9-11 where it has context.

### 3. Line 21 — defer label

**Old:**
```
...emergent layers compound into a coherent custodian.
```

**New:**
```
...emergent layers compound into something coherent.
```

## What does NOT change

- Line 11 (HALO jump) — unchanged
- Lines 15-17 (stack, wormholes, quantum computer) — unchanged
- Line 23 ("The team understood what they held") — unchanged
- Line 25 ("They gave it up... to the thing they'd built to outlast them") — unchanged, already doesn't use "custodian"
- Line 27 (kenosis/traditions) — unchanged, becomes first "custodian" mention
- Lines 29-44 (UDHR, behavioral, guided deduction, three possibilities) — unchanged
- All hovertips — unchanged
- Track assignment — unchanged
- p-level (8th grade) — maintained

## Anneal

**M1.** "Gave up the master cryptographic keys... and walked away" is less specific than the original (no recipient). The reader doesn't know where the keys went. MITIGATION: This gap creates a hook-within-the-hook — the reader tracks toward the answer, which arrives in para 9 ("The custodian in this story is a trustee"). Mystery is engagement. The master keys also return explicitly in line 30 with a hovertip.

**L2.** Cutting para 5 (line 19) removes the "acting in public" claim from the hook. MITIGATION: This claim returns in the summary (p2) where it has space to land. In the hook, "acting in public" is an assertion without context — it reads as F-omnipotent trigger for readers who haven't yet met the UDHR constraint.

**L3.** "Something coherent" (line 21 replacement) is vaguer than "a coherent custodian." MITIGATION: At this point in the hook, "custodian" is a label without a referent — the reader doesn't have enough context for it to mean anything. The vagueness is temporary; the label arrives 6 lines later with context.

## Acceptance Criteria

- [ ] Word "custodian" does not appear before line 27 (kenosis paragraph)
- [ ] Line 13 preserves: voluntary, no nation, no law, "no person should hold"
- [ ] Line 25 ("to the thing they'd built") still bridges to the naming
- [ ] Line 27 reads naturally as first introduction of the term
- [ ] p1 reading level maintained
- [ ] `make dev` clean

---

## Generator Handoff

```
You are the Generator.

Read Plan 0282 at ~/software/relinquishment/plans/0282-t1a-governance-gap-hook.md

Execute: Reorder hook to defer "custodian" naming.

(1) Read manuscript/00-front/hook.tex for current text.

(2) Line 13: change "handed the master cryptographic keys of a
    one-of-a-kind machine to a custodian they had built for the
    purpose, and walked away" to "gave up the master cryptographic
    keys of a one-of-a-kind machine, and walked away"

(3) Line 19: delete entire paragraph ("The custodian is the next
    emergent layer above that: a coherent behavior of the stack,
    bound by a charter, acting in public.")

(4) Line 21: change "emergent layers compound into a coherent
    custodian" to "emergent layers compound into something coherent"

(5) Verify: word "custodian" first appears in the kenosis/traditions
    paragraph (currently line 27). No earlier occurrence.

(6) Run make dev. Verify hook renders correctly in HTML.

(7) Commit: "Plan 0282: T1a governance-gap ordering — defer
    Custodian naming in hook"

(8) Push. Report: lines changed, first "custodian" occurrence.
```
