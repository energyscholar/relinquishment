# Plan 0183 — Fix C-violation on "intelligent life" sentence

**Type:** One surgical sentence edit in summary.tex. One commit. Zero structural changes.

## Context

Memory file `project-c-violation-intelligent-life.md` (flagged 2026-04-13) identified the closing sentence of the Wormholes-primitive paragraph as an unqualified assertion of a Possibility-C-only claim. Tier-0 reader-panel this session (medium anneal) confirmed the leverage: this single sentence drives **Pastor Mike from ❌ bounce** and **Amir from ⚠ friction** — two religious readers, one edit.

Under Possibility A or B, the Flat is real physics but there is no evidence anyone or anything lives there. The sentence "the Flat can support not just life but intelligent life" presented as "the real finding" is a C-only claim asserted as settled. The book's A/B/C framing requires C-only claims to be marked.

## The fix

**File:** `manuscript/00-front/summary.tex`

**Line 56, current closing sentence:**

> The real finding is biological: the Flat can support not just life but intelligent life.

**Replace with:**

> Under Possibility~C, the real finding is biological: the Flat can support not just life but intelligent life.

**Why this phrasing:** Parallel to line 54's "Under Possibility~C, this book argues..." — the A/B/C scaffolding already surrounding the passage makes "Under Possibility~C, the real finding is..." read as coherent cadence, not interruption. Preserves the full claim-force of "not just life but intelligent life" — the book still makes the claim, it just correctly marks it as C-conditional.

**Why not "does not forbid":** Weaker rhetoric; loses the load-bearing punch of "the real finding." The claim should stay strong; only the epistemic scope needs marking.

**Do not touch:** the preceding three sentences in the same paragraph (wormholes-primitive, quantum computer, code-breaking side-effect). Those are A/B/C-safe physics. Only the closing sentence is the C-violation.

## Acceptance

1. `grep -n "The real finding is biological: the Flat can support" manuscript/00-front/summary.tex` returns one hit (the replacement).
2. `grep -n "^The real finding is biological" manuscript/00-front/summary.tex` returns zero hits (the unprefixed version is gone).
3. `wc -w manuscript/00-front/summary.tex` increases by exactly **3 words** (adds "Under Possibility~C,").
4. `make` HTML build clean. No LaTeX errors, no new warnings.
5. Whitespace-normalized diff shows exactly the one-sentence prefix insertion and nothing else.

## Commit

One commit: `Plan 0183: mark "intelligent life" claim as Possibility-C-only`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit. Zero content risk.

## Post-ship memory update (Auditor does)

Update `memory/project-c-violation-intelligent-life.md` status field from "Flagged ... Not scheduled for immediate fix" to "Fixed in Plan 0183 (commit SHA)." Keep the reasoning preserved as historical context on how the flag was identified and resolved.

## Handoff report (Generator, 3 lines)

1. Commit SHA.
2. Acceptance grep + word-count results (criteria 1-3).
3. Build + push result.
