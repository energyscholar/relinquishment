# Plan 0178 — Drop "first account" + Soften Pedagogy Question

**Type:** Two surgical edits (one delete, two word-drops for consistency). One commit. hook.tex + summary.tex.

## Status

- **Edit 1: LANDED** at commit `17acffd` (word-count -15, grep clean).
- **Edits 2 + 3: RESIDUAL** — executed by Generator on next handoff.

## Edit 1 — Delete "first account" line (hook.tex) [DONE]

**File:** `manuscript/00-front/hook.tex` (line 46 area)

**Delete the line:**

> This may be the first account of someone who faced that choice and let go.

Plus the blank line immediately below it (since the line is its own paragraph, the trailing blank becomes orphan).

**Verification:** `grep -n "first account" manuscript/00-front/hook.tex` returns zero hits after the edit.

## Edit 2 — Soften pedagogy question (hook.tex)

**File:** `manuscript/00-front/hook.tex`

**Current:**

> What could explain that, besides the obvious?

**Replace with:**

> What could explain that?

Delete ", besides the obvious" (comma, space, phrase). Trailing question mark stays.

**Rationale (Bruce, 2026-04-13):** less leading. The pure question is stronger — trusts the reader to infer without prompting.

## Edit 3 — Same softening in summary.tex (consistency)

**File:** `manuscript/00-front/summary.tex`

The same phrase `besides the obvious` appears in summary.tex line 253 in the pedagogy-as-evidence question. These two surfaces have been kept in rhetorical sync across prior plans (0163, 0174).

**Generator reads the exact current context at summary.tex:253 first**, then applies the same softening: delete `, besides the obvious` (or `--- besides the obvious ---` if it's em-dash flanked — Generator reports the exact punctuation context it finds, then applies the parallel softening).

**If the summary context differs meaningfully from the hook context** — e.g., the phrase is embedded in a longer sentence that would not read cleanly with the simple comma-phrase deletion — halt at Edit 3, report the current text, and wait for Auditor guidance. Do NOT invent phrasing.

**Verification:** `grep -n "besides the obvious" manuscript/` returns zero hits after the edit.

## Rationale

Flagged by Doctorow-read across every audit since the panel was established. Reads as self-positioning — the book elevating itself rather than letting the story speak. Bruce confirmed (2026-04-13): "I'm fine taking that out. No need to be obvious."

The surrounding flow strengthens without it:

- Line 44: "…someone, someday soon, will hold something too powerful for anyone to have."
- Line 48: "And a question to carry with you: why would a man with a [REDACTED] career spend two and a half years teaching a physicist public-domain science in a deliberate order?"

Deletion puts the question directly after the stakes sentence. Lands harder.

## Acceptance

1. `grep -n "first account" manuscript/` returns zero hits.
2. `wc -w manuscript/00-front/hook.tex` decreases by 14 words (sentence length).
3. `make` HTML build clean.
4. No other content changes.

## Commit

One commit: `Plan 0178: drop "first account" self-positioning line from hook`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit.

## Handoff report (Generator, 3 lines)

1. Commit SHA.
2. Word-count delta on hook.tex (target: -14).
3. Build + push result.
