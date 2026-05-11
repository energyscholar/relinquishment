# Plan 0317: Multi-Reader Feedback Integration Protocol

**Created:** 2026-05-09 (Session 71)
**Purpose:** Gated process for integrating feedback from Plans 0314 (audit) and 0315 (fix plan).
**Depends on:** Plan 0314, Plan 0315, Plan 0316 (PDF fixes separate track)
**Scope:** Content changes only. PDF rendering handled by Plan 0316.

## Principle

Bruce gates each priority tier. No tier executes until Bruce approves it. Each tier is a self-contained Generator prompt. The ACCENTUATE list protects passages that must not be degraded during editing.

## Feedback Inventory

| Priority | Count | Character | Gate |
|----------|-------|-----------|------|
| P0 (must-fix) | 9 | Physics errors, credibility threats | Bruce reviews each individually |
| P1 (should-fix) | 13 | Redundancy, missing qualifiers, structural | Bruce reviews as batch |
| P2 (PDF-only) | 6 | Rendering artifacts | Handled by Plan 0316 (separate track) |
| P3 (polish) | 7 | Tightening, word choice | Bruce reviews as batch |
| ACCENTUATE | ~19 | Passages to protect | Read-only reference for all generators |

## Gating Protocol

### Step 1: Bruce Reviews P0 List
**Input:** Plan 0315 P0 items (9 items)
**Bruce decides for each:**
- ACCEPT (proceed as described)
- MODIFY (change the fix approach)
- REJECT (leave as-is, with reason)
- QQQ (needs more information before deciding)

**Output:** Approved P0 fix list with Bruce's annotations.

### Step 2: Generator Executes Approved P0s
**Input:** Approved P0 list + ACCENTUATE reference
**Constraint:** Generator MUST check each edit against ACCENTUATE list. If an edit would modify an ACCENTUATE passage, STOP and flag for Bruce.
**Output:** One commit per P0 fix. Message format: `Plan 0317 P0-N: description`

### Step 3: Bruce Reviews P0 Results
Verify each fix is correct. If any need revision, loop back to Step 2.

### Step 4: Repeat for P1, P3
Same ACCEPT/MODIFY/REJECT/QQQ protocol. P1 and P3 can be batched more aggressively since they're lower risk.

### P2 Handled Separately
P2 items (PDF-only) are addressed by Plan 0316. No content changes needed.

## ACCENTUATE Protection Protocol

The ACCENTUATE list in Plan 0315 identifies ~19 passages that are the book's strongest material. During any edit:

1. Generator loads ACCENTUATE list before starting
2. Before each edit, check: does this change touch an ACCENTUATE passage?
3. If yes: STOP. Show Bruce the proposed change alongside the original. Bruce decides.
4. If no: proceed with edit.

This prevents the common failure mode where fixing a weakness inadvertently damages a strength.

## P0 Items (from Plan 0315, for Bruce's review)

1. **P0-1:** 2DEG room-temperature conflation ("The Punchline") — every pHEMT claimed as topologically ordered
2. **P0-2:** Non-abelian qualifier missing from anyon discussions
3. **P0-3:** Factoring-as-brute-force error
4. **P0-4:** 1991 anachronism
5. **P0-5:** "Infinitely thin" claim (should be ~10nm)
6. **P0-6:** "3D computation" should be "classical computation" (Interlude 03)
7. **P0-7:** Missing AI confabulation steelman (TODO line 95 — already flagged HIGH PRIORITY)
8. **P0-8:** Kauffman-to-2DEG bridge undefined (CH reader credibility collapse point)
9. **P0-9:** Spiral Abstracts count error ("Fifteen" but has 16: I-XVI)

## Cross-Reference: Previous Audits

Plan 0158 (earlier audit) findings should be compared to Plan 0314 to identify:
- Issues found in both audits (persistent problems, high priority)
- Issues found only in 0158 (may have been fixed, verify)
- Issues found only in 0314 (new findings from deeper read)

This comparison is a separate task (not blocking P0 execution).

## Execution Notes

- Each P0 fix is a separate commit for clean revert capability
- Generator reads source files, not PDF (PDF is a build artifact)
- UQ-gated workflow from Plan 0312 applies: uncertain physics claims get QQQ markers
- Bruce's editor is `subl` — he may want to review diffs there before committing
