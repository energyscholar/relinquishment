# Plan 0058: Idempotency Requirement + Triad Protocol Hardening

*Auditor: Argus (Session 34). Origin: S34 confabulation incident — Auditor generated manuscript content directly, producing an incorrect ABCRE-TQNN isomorphism claim. Root cause: role collapse. This plan adds mechanical enforcement via idempotency.*

---

## Background (Generator: read this section for context)

The Triad Alignment Protocol separates Auditor (plans/verification) from Generator (implementation). On 2026-03-07, the Auditor violated role boundaries by generating manuscript content directly. The content contained a confabulated mathematical claim (ABCRE operators isomorphic to TQC operations) that was sent externally before verification. The claim was later disproven by independent testing.

The root cause: the Auditor had maximum context (ABCRE operators in persistent memory) and generated content without a plan or acceptance criteria. Pattern matching produced a plausible-sounding but incorrect cross-domain connection. No Generator plan existed to constrain the output. No acceptance criteria existed to catch the error.

**The fix:** Add an idempotency requirement that mechanically prevents this class of error. If all Generator plans must produce idempotent output (same plan → same claims regardless of which Generator runs it), then Generator-originated novel claims become structurally visible and must be flagged.

---

## Phase 1: Add Requirement R27 to requirements.md

**File:** `~/software/relinquishment/plans/requirements.md`

**Action:** Add the following new requirement section AFTER the existing R26 section and BEFORE the "Verification Protocol" section. Preserve all existing content exactly.

**Insert this text:**

```
## R27: Idempotency

**PASS if:**
- Every Generator plan includes an **idempotency statement** that reads: "A second Generator given only this plan file would produce the same claims, structure, and factual content. Style and phrasing may vary."
- Generator output contains ONLY claims, structure, and factual content that are **derivable from the plan file alone** — not from the Generator's training data, persistent context, or pattern matching
- If a Generator produces content not specified in the plan (novel claims, cross-domain connections, original research assertions), the Generator **flags it explicitly** in its completion report: "[NOT IN PLAN: description of unplanned content]"
- The Auditor's verification step includes an **idempotency check**: "Would a fresh Generator with no prior context produce the same claims from this plan?" If no → the divergent content requires independent verification before acceptance
- Plans that are inherently exploratory (research, literature search) state this explicitly and define **bounded output**: "Report findings from these sources. Do not draw conclusions beyond what sources state."

**FAIL if:** Plans lack idempotency statements. Generator produces unplanned novel claims without flagging them. Auditor accepts Generator output without idempotency check. Exploratory plans have unbounded output scope.

**Rationale (S34 incident):** The Auditor generated a novel mathematical claim (ABCRE-TQNN isomorphism) while writing manuscript content. The claim was incorrect. Had a Generator plan with idempotency constraints existed, the novel claim would either (a) not have been in the plan and therefore not generated, or (b) been flagged as "[NOT IN PLAN]" and routed to verification. Idempotency makes confabulation structurally visible.
```

**Update the version line** at the bottom of requirements.md:

Change: `*Requirements v1.7 — 2026-02-14 — R0-R26. Updated R19 (OCG gaps), R21 (cmap→fontspec), R24 (images/gitinfo targets, 30s→incremental). Prior: v1.6 R0/R19; v1.5 R0; v1.4 R24-R26.*`

To: `*Requirements v1.8 — 2026-03-08 — R0-R27. Added R27 (Idempotency). Prior: v1.7 R0-R26; v1.6 R0/R19; v1.5 R0; v1.4 R24-R26.*`

---

## Phase 2: Update Triad Protocol in CLAUDE.md

**File:** `~/.claude/CLAUDE.md`

**Action 1:** In the **Generator Role** section, add one item to the "You DO" list and one to the "You DO NOT" list.

Current "You DO" list:
```
**You DO:**
- Read the plan referenced in your prompt
- Implement exactly what the plan specifies
- Follow test cases as acceptance criteria
- Report completion (1–5 lines) with your Generator name if assigned
```

Change to:
```
**You DO:**
- Read the plan referenced in your prompt
- Implement exactly what the plan specifies
- Follow test cases as acceptance criteria
- Flag any content not derivable from the plan alone: "[NOT IN PLAN: description]"
- Report completion (1–5 lines) with your Generator name if assigned
```

Current "You DO NOT" list:
```
**You DO NOT:**
- Invent tests beyond plan spec
- Redefine purpose or scope
- Expand beyond what was requested
- Call EnterPlanMode or ExitPlanMode
```

Change to:
```
**You DO NOT:**
- Invent tests beyond plan spec
- Redefine purpose or scope
- Expand beyond what was requested
- Generate novel claims not specified in the plan without flagging them
- Call EnterPlanMode or ExitPlanMode
```

**Action 2:** In the **Auditor Role** section, add one item to the "You DO" list.

Current "You DO" list:
```
**You DO:**
- Define objectives and success criteria
- Write test cases that encode invariants
- Create audit plans in `~/software/relinquishment/plans/` (serial numbered: 0001-name.md)
- Write/update requirements in `~/software/relinquishment/plans/requirements.md`
- Review generator output against acceptance criteria
- Interpret failures structurally
- Output a handoff prompt (≤8 lines, references plan file) as plain text
```

Change to:
```
**You DO:**
- Define objectives and success criteria
- Write test cases that encode invariants
- Create audit plans in `~/software/relinquishment/plans/` (serial numbered: 0001-name.md)
- Include idempotency statement in every plan (R27): "A second Generator given only this plan file would produce the same claims, structure, and factual content."
- Write/update requirements in `~/software/relinquishment/plans/requirements.md`
- Review generator output against acceptance criteria
- Perform idempotency check: "Would a fresh Generator produce the same claims from this plan?"
- Interpret failures structurally
- Output a handoff prompt (≤8 lines, references plan file) as plain text
```

**Action 3:** In the **Handoff Rules** section, add one rule.

Current:
```
### Handoff Rules
- ≤8 lines. Full plan lives in `~/software/relinquishment/plans/`.
- Generator shell has NO conversation history — plan file must be self-contained.
- Generator may READ `~/software/relinquishment/` (plans, existing content). Generator may NOT read `~/software/aurasys-memory/` — all needed context must be in the plan.
- Bruce runs Auditor and Generator in SEPARATE shells. Copy-paste is the authorization gate.
- Git commits: one commit per plan phase, message format: `Plan NNNN phase N: description`
```

Change to:
```
### Handoff Rules
- ≤8 lines. Full plan lives in `~/software/relinquishment/plans/`.
- Generator shell has NO conversation history — plan file must be self-contained.
- Generator may READ `~/software/relinquishment/` (plans, existing content). Generator may NOT read `~/software/aurasys-memory/` — all needed context must be in the plan.
- Plans must be idempotent: the plan alone (not Generator context) determines what claims are made. See R27.
- Bruce runs Auditor and Generator in SEPARATE shells. Copy-paste is the authorization gate.
- Git commits: one commit per plan phase, message format: `Plan NNNN phase N: description`
```

---

## Phase 3: Update bruce-se-methodology.md

**File:** `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/bruce-se-methodology.md`

**Action:** Find the Triad Protocol section. Add a subsection on idempotency after the existing content. Keep it brief (≤10 lines). Content:

```
### Idempotency Discipline (Added S34, 2026-03-08)

All Generator plans include an idempotency statement: "A second Generator given only this plan would produce the same claims." This mechanically prevents confabulation by ensuring the plan — not the Generator's context — determines what claims are made. Generator flags unplanned content as "[NOT IN PLAN]". Auditor checks idempotency at review: "Would a different Generator produce the same claims?" Divergent content requires independent verification. See R27 in requirements.md. Origin: S34 ABCRE-TQNN confabulation incident.
```

---

## Acceptance Criteria

1. **R27 exists** in requirements.md with the exact text specified above
2. **Version line** updated to v1.8
3. **CLAUDE.md Generator "You DO"** contains "Flag any content not derivable from the plan alone"
4. **CLAUDE.md Generator "You DO NOT"** contains "Generate novel claims not specified in the plan without flagging them"
5. **CLAUDE.md Auditor "You DO"** contains idempotency statement and idempotency check items
6. **CLAUDE.md Handoff Rules** contains "Plans must be idempotent" rule
7. **bruce-se-methodology.md** contains Idempotency Discipline subsection
8. **No other content modified.** Existing text preserved exactly. Only additions.
9. **Idempotency self-test:** This plan itself satisfies R27. A second Generator given this plan would produce the same changes to the same files. The output is fully determined by the plan.

---

## Idempotency Statement

A second Generator given only this plan file would produce the same claims, structure, and factual content. Style and phrasing may vary only in the bruce-se-methodology.md addition, which specifies content but not exact wording. All other changes are exact text replacements with before/after specified.

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0058-idempotency-discipline.md

Three phases: (1) Add R27 to requirements.md, (2) Update Triad
Protocol in CLAUDE.md, (3) Add idempotency section to
bruce-se-methodology.md. All changes are additive — do not modify
existing content. Plan specifies exact before/after text for phases
1-2. Commit per phase: "Plan 0058 phase N: description"
```
