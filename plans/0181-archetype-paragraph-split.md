# Plan 0181 — Split archetype paragraph (phone pacing)

**Type:** Two `\n\n` insertions in summary.tex. Zero word changes. One commit. Mirrors Plan 0175 mechanics.

## Context

Reader-test (this session, 9 personas × phone/browser, 2 rounds annealed) surfaced Jane bouncing on summary.tex's archetype paragraph when reading on phone. The paragraph is load-bearing (Plan 0162 / renunciation-archetype — what converts Mike/Amir/Arjun/Wei from theological-collision bounce to recognition). Cannot cut content. Can fix geometry: 170 words of unbroken grey block in a narrow phone column triggers skim-past before Jane starts reading.

This plan splits that one paragraph into three at natural seams. Zero word changes. Same mechanic as Plan 0175 (wormholes-established standalone).

## File

`manuscript/00-front/summary.tex`, line 196 (one long source line).

## Current (line 196, single paragraph)

> The UDHR is not an answer to the older and deeper questions --- about dignity, restraint, what we owe each other --- that every tradition has asked in its own language. It is a modern attempt, offered here as a working constraint, not as a replacement for anything older. The traditions already have names for what the team did with their discovery. Christians call it \textit{kenosis} --- self-emptying. Muslims call it \textit{tawakkul} --- entrusting what you cannot carry. Jews call it \textit{tzimtzum} --- making room by stepping back. Hindus and Jains call it \textit{aparigraha} --- non-grasping. Buddhists recognize the bodhisattva's refusal to keep what others need. Indigenous traditions across the Americas and the Pacific know the pattern as trusteeship of a commons --- and the 1948 Declaration itself drew in part on the Haudenosaunee Great Law of Peace, whose authors understood that some powers must be held, not owned. The book claims none of these traditions. It notices that they all noticed the same thing.

## Two splits

### Split A — setup | list

**Insert `\n\n` between:**

> ...not as a replacement for anything older.

and

> The traditions already have names for what the team did with their discovery.

### Split B — list | closer

**Insert `\n\n` between:**

> ...whose authors understood that some powers must be held, not owned.

and

> The book claims none of these traditions. It notices that they all noticed the same thing.

**Why standalone closer:** `"The book claims none of these traditions. It notices that they all noticed the same thing."` is the load-bearing sentence of the whole passage. Standalone paragraph = maximum phone-scroll impact (direct parallel to 0175's wormholes-established treatment).

## LaTeX mechanics

Blank line in source = `\par` = new paragraph. The target paragraph is currently one long source line. Generator finds each anchor string in the line, replaces the inter-sentence space with `\n\n`, producing three source lines separated by blank lines.

## Do not touch

- Any `\textit{...}` italic macro or its argument.
- Any em-dash (`---`), comma, or word.
- Any file other than summary.tex.
- The interior of any sentence.
- Any other paragraph in summary.tex.

## Acceptance

1. `wc -w manuscript/00-front/summary.tex` unchanged (±0 words).
2. `grep -c '^$' manuscript/00-front/summary.tex` increased by exactly **2**.
3. `make` HTML build clean. No LaTeX errors, no new warnings.
4. Whitespace-normalized content regression check: `diff <(tr -s '[:space:]' ' ' < before.tex) <(tr -s '[:space:]' ' ' < after.tex)` empty.
5. On phone (Bruce verifies post-push): three distinct paragraph blocks visible; closer sentence ("noticed the same thing") stands alone as punchline.

## Commit

One commit: `Plan 0181: split archetype paragraph 3 ways (phone pacing, zero word changes)`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit. Zero content risk.

## Handoff report (Generator, 4 lines)

1. Commit SHA.
2. Word-count diff for summary.tex (target: 0).
3. Blank-line count diff for summary.tex (target: +2).
4. Build + push result.
