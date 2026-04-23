# Plan 0179 — Two surgical edits (hook wordcount tooltip + stratosphere preposition)

**Type:** Two one-line edits. One commit. Different files.

## Edit 1 — Intro tooltip wordcount (reader.js)

**File:** `build/reader.js`

**Line 119, current:**

```
introLink.setAttribute('data-hover', 'Start here. 400 words, then the full story in 4,000. Most readers never need more.');
```

**Issue:** "400 words" is wrong. `detex manuscript/00-front/hook.tex | wc -w` = **764 words**. The "400 words" figure predates post-0163/0178 hook growth.

**Replace `400 words` with `~750 words`.** (Round down slightly; matches reader-perceived length, not exact source count.)

**New line:**

```
introLink.setAttribute('data-hover', 'Start here. ~750 words, then the full story in 4,000. Most readers never need more.');
```

**Verification:**

```
grep -n "400 words" build/reader.js
```

returns zero hits after edit.

## Edit 2 — "falls through" → "falls from" (hook.tex)

**File:** `manuscript/00-front/hook.tex`

**Line 11, current:**

> [REDACTED]. A man falls through the stratosphere. The air is thin enough to kill in minutes.

**Replace:** `falls through the stratosphere` → `falls from the stratosphere`

**One word change.** "Through" implies passage across; "from" correctly marks the stratosphere as the origin point of the fall.

**Verification:**

```
grep -n "falls through the stratosphere" manuscript/
grep -n "falls from the stratosphere" manuscript/00-front/hook.tex
```

First returns zero hits; second returns one.

## Other "400 words" references (out of scope — flag only)

Also surfaced in grep:

- `build/chapter-hover-descriptions.yaml:16` — `"START HERE. A man falls from the sky over Bosnia. ... ~400 words."` (this tooltip is separately stale — uses pre-redaction "sky over Bosnia" wording AND includes "one of the most important people who ever lived" phrasing that was softened in Plan 0177-era work). **Not in 0179.** Flag for a follow-up hygiene plan alongside the hover-definitions.yaml audit findings.
- `manuscript/versions/one-page-summary.md:4` — target spec for p1 pass (400w = the one-page summary target, not the hook). Not stale; leave.

## Acceptance

1. `grep -n "400 words" build/reader.js` returns zero hits.
2. `grep -n "~750 words" build/reader.js` returns one hit.
3. `grep -n "falls through the stratosphere" manuscript/` returns zero hits.
4. `grep -n "falls from the stratosphere" manuscript/00-front/hook.tex` returns one hit.
5. `make` HTML build clean.
6. No other content changes.

## Commit

One commit: `Plan 0179: correct hook wordcount tooltip + "falls through"→"falls from" stratosphere`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit.

## Handoff report (Generator, 3 lines)

1. Commit SHA.
2. Acceptance grep results (criteria 1-4).
3. Build + push result.
