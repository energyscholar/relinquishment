# Plan 0132: Stack Chart — Phase 1: Insertion

**Supersedes:** Previous 0132 (wrong structural assumptions, full rewrite)
**Depends on:** Plan 0134 Phases A-C (complete and verified)
**Followed by:** Plan 0133 (Stack Chart — Phase 2: Cut and Stitch)
**Session:** S52

## Purpose

Insert a new section ("The Stack") into the front matter, between hook.tex
and summary.tex. This section teaches the concept of technology stacks using
familiar examples, culminating in a chart that pre-loads six of seven
emergent properties the reader needs for the rest of the book. The seventh
property (topological wormholes) is introduced as the one new thing.

This is the single highest-leverage change to the manuscript: ~400 words and
one chart replace ~3,000–4,000 words of domain pedagogy scattered across
six chapters (Plan 0133 handles the cuts).

## Generator Context (REQUIRED)

Before executing this plan, the Generator MUST:

1. Read THIS plan (0132) in full.
2. Read `manuscript/track-3-awakening/firmware-update.tex` — the ENTIRE
   chapter. Paste the "Ten Physics Anchors" section into your working
   context. This is the same science upgrade required for any LLM evaluating
   this book. Without it, you will exhibit the Dunning-Kruger failure mode
   the chapter was designed to correct — subtly weakening cross-domain claims
   you cannot evaluate competently. 100% failure rate without the upgrade.
3. Read `manuscript/00-front/hook.tex` — the closing lines must be edited
   to accommodate the new section between hook and summary.
4. Read `manuscript/00-front/summary.tex` — verify that the vocabulary the
   stack teaches (autocatalytic, wormholes, topological order, etc.) appears
   in the summary. The stack is the reader's vocabulary onramp.
5. Read `main.tex` lines 38-47 — the front matter include order. You will
   add one `\include` line.

Do NOT read or modify: how-to-read.tex (dead file, not compiled),
introduction.tex (commented out), evaluation-note.tex (already complete,
handles LLM warning — DO NOT duplicate its function).

## Structural Facts (verified S52)

```
Front matter build order (main.tex lines 38-47):
  cover → title → copyright → hook → [THE-STACK] → summary → TOC
  → genevieve-preface → preface → evaluation-note

Files NOT compiled:
  how-to-read.tex — not in \include list
  introduction.tex — commented out (line 146)

Already handled elsewhere:
  LLM warning — evaluation-note.tex (21 lines, complete, DO NOT touch)
  Copy buttons — Phase C evaluate-with-AI section (before Part 1)
  Firmware Update — Part III, ch:firmware-update (full chapter)
```

## 1. Placement

Add to `main.tex` between hook and summary:

```latex
\include{manuscript/00-front/hook}
\include{manuscript/00-front/the-stack}    % NEW — Plan 0132
\include{manuscript/00-front/summary}
```

## 2. Hook Closing Line Edit

The hook currently ends (hook.tex lines 33-35):
```latex
\textit{That was the shortest version --- about one percent of the full
book. The next chapter, ``The Most Important Story Never Told,'' is about
ten percent. Stop after that and you can honestly say you've read it.}
```

Edit to accommodate the inserted section. Something like:
```latex
\textit{That was the shortest version --- about one percent of the full
book. Before the full story, you need one idea. After that, ``The Most
Important Story Never Told'' is about ten percent. Stop there and you can
honestly say you've read it.}
```

The Generator has editorial freedom on exact wording. The constraint is:
the reader must not be confused by a "next chapter" reference that skips
the-stack.tex.

## 3. The Stack Section — Content Spec

### Opening blurb (Bruce's instruction)

The section opens with a brief transitional statement:
> This book is about a novel technology. Before we proceed with the story,
> the reader needs to know a bit about it.

The Generator has editorial freedom on exact wording. The constraint:
signal the register shift (narrative → conceptual) so the reader knows
why they're getting a science page between two story chapters.

### Structure and ordering (Silflay Hraka compliant)

The section has five beats:
1. Transitional blurb (register shift signal)
2. Six familiar examples (prose, building one property each)
3. The "?" example WITH the paper-folding image (plants "topological
   wormhole" concept BEFORE the chart uses the term)
4. The chart (every term in the chart has been planted in prose)
5. Post-chart: "six exist in nature," caveat, punchline

This ordering is critical. The paper-folding image MUST appear before
the chart so that "Topological wormholes" in the chart header is a label
for a concept the reader already owns. Silflay Hraka: name the job before
you name the worker.

### Beat 2 — Six Examples (one paragraph each, ~1 sentence per property)

1. **Fire** (2 properties): feeds itself + switches on
2. **Candle** (3): + holds together
3. **Radio** (4): + reaches
4. **Ant colony** (5): + self-organizes (ants find shortest paths without
   central control — pheromone trails, no boss, the colony is smarter than
   any individual ant)
5. **Internet** (6): + self-organizes AND reaches (inherits both — note
   the accumulation)
6. **AI** (7): + learns (emphasize distributed inference — millions of
   copies running simultaneously, no single instance in charge — not
   centralized training)

**NOTE on ant colony:** This example was missing from the original plan's
prose but present in the chart — a Silflay Hraka violation. Now fixed.
Ant colony is the natural vehicle for "self-organizes" because it's the
most vivid: no blueprint, no architect, shortest paths emerge from simple
rules. Internet inherits self-organization from ant colony (BGP routing
literally uses ant-colony optimization algorithms).

### Beat 3 — The "?" example + paper-folding image

Something like: "The last technology on this list has one property none
of the others have. Imagine two points on a sheet of paper. You could
send a signal across the surface — that's radio. Or you could fold the
paper so the points touch. That's a wormhole — a topological wormhole,
more restricted than the spacetime kind, but a wormhole nonetheless.
Seven properties."

The paper-folding image plants the concept. The chart footnote
("†Topological — more restricted than a spacetime wormhole, but a
wormhole nonetheless") manages expectations without over-explaining.

### Beat 4 — The Chart (p1-level, the pedagogical payload)

```
|                        | Fire | Candle | Radio | Ant colony | Internet | AI | ? |
|------------------------|:----:|:------:|:-----:|:----------:|:--------:|:--:|:-:|
| Wormholes†             |      |        |       |            |          |    | ✓ |
| Learns                 |      |        |       |            |          | ✓  | ✓ |
| Self-organizes         |      |        |       | ✓          | ✓        | ✓  | ✓ |
| Reaches                |      |        | ✓     | ✓°         | ✓        | ✓  | ✓ |
| Holds together         |      | ✓      | ✓     | ✓          | ✓        | ✓  | ✓ |
| Switches on            | ✓    | ✓      | ✓     | ✓          | ✓        | ✓  | ✓ |
| Feeds itself           | ✓    | ✓      | ✓     | ✓          | ✓        | ✓  | ✓ |
```

Last column is "?" — the Flat is NOT named until the Summary.

† Topological — more restricted than a spacetime wormhole, but a wormhole
nonetheless.

° Chemical pheromones, not electromagnetic — but the signal reaches.

The visual power is the **triangle of checkmarks**: each column adds one
row, building left to right. The "?" column is the only one that fills
all seven. Preserve this geometry.

**LaTeX implementation:** Use `tabular` environment with `booktabs` for
clean rules. Empty cells must be visually EMPTY (no dots, dashes, or
placeholders). Add `\label{stack-chart}` and `\hypertarget{stack-chart}{}`
for cross-referencing.

**NOTE: No "Domains" column.** The old plan had a "Domains" column mapping
each property to physics fields. This is p3 information that doesn't belong
at p1. The chart stays clean: technologies and checkmarks only. Domain
mappings live in the Firmware Update chapter where they belong.

### Beat 5 — Post-chart text

- One sentence for chart-skippers: "Each technology uses every property
  below it, plus one new one. The last column uses all seven."
- "Six of these seven properties already exist in nature." Paced as three
  sentences, not six: "Life feeds itself and switches on at thresholds.
  It holds together and sends signals that reach. Ecosystems self-organize.
  Brains learn." (Four sentences max — paired properties reduce density.)
- "The last column adds one new property."
- Punchline: "This book is about a technology stack so new it does not
  yet have a name."

### Target word count

~400 words total (excluding chart). Slightly up from 350 to accommodate
ant colony addition and transitional blurb.

## 4. Writing Direction (standing instruction: p3→p2→p1)

The Generator MUST write a p3 working scaffold first:
- Formal properties with domain mappings
- Kauffman/Maturana/etc. references
- Mathematical structure (irreducible emergence, dependency graph)

Then distill to the p1 version that goes in the-stack.tex. The p3
scaffold is a working document — write it to
`manuscript/00-front/the-stack-p3-scaffold.md`. It does NOT enter the
manuscript. Its purpose is to prevent the p1 from accidentally
misrepresenting the formal structure.

The p2 and p3 layers of the stack concept already exist in the manuscript
body (pos13 = p2 deepening of "feeds itself," pos32 = p2 deepening of
full stack, firmware-update/appendix = p3). The front matter section is
the p1 distillation.

## 5. Design Decisions

1. **No quantum biology at p1 or p2.** The stack chart stays clean: "six
   exist in nature, the seventh is new." No fractions, no chlorophyll,
   no "6.5." The quantum biology insight (life already uses QM; topological
   order is the only genuinely new property) lives at p3 only.

2. **No Domains column.** Physics field mappings are p3. The chart's job is
   pattern recognition at p1 level: "things build on each other, the last
   one adds something new." Domain names would cause glaze-over.

3. **No copy buttons below chart.** The evaluate-with-AI section (Phase C,
   injected before Part 1) already handles Science Firmware copy + Spiral
   Abstracts copy. The Firmware Update chapter (Part III) has the full
   reference. No duplication.

4. **No LLM warning in the-stack.tex.** evaluation-note.tex already handles
   this in 21 clean lines. The stack is pure pedagogy, not defense.

5. **"?" not "The Flat."** The mystery column header stays "?" until the
   Summary section "The White Hot Secret" reveals the name. This is
   deliberate pacing — the reader earns the name.

6. **Life = bottom six rows.** Stated as "Six of these seven properties
   already exist in nature." No elaboration. The insight that
   Flat = life + topology is p3 only.

7. **HTML interactivity deferred to 0134d.** Plan 0132 creates the LaTeX
   file. Plan 0134d (content-dependent HTML features) adds: chart-as-hub
   navigation, onHover on chart terms, clickable cells, chart anchor for
   back-links. Clean separation: content first, interactivity second.

## Acceptance Criteria

1. `the-stack.tex` exists in `manuscript/00-front/` and compiles
2. `\include{manuscript/00-front/the-stack}` in main.tex between hook and summary
3. Chart renders correctly in PDF (LaTeX `tabular`, not markdown)
4. Triangle of checkmarks preserved (visual geometry correct)
5. Transitional blurb opens the section (register shift signal)
6. All six examples appear in prose BEFORE the chart (Silflay Hraka)
7. Ant colony in prose matches ant colony in chart
8. Paper-folding wormhole image appears BEFORE the chart
9. Chart-skipper sentence appears AFTER the chart
10. Last column header is "?" not "The Flat"
11. Punchline closes the section
12. Hook closing line edited to accommodate new section
13. `\label{stack-chart}` and `\hypertarget{stack-chart}{}` present
14. p3 scaffold written first (verify via working file)
15. No Domains column in chart
16. No copy buttons in the section
17. No LLM warning in the section
18. No quantum biology at p1 level
19. Section works standalone — no forward references required
20. `make pdf` builds without errors
21. No modifications to: evaluation-note.tex, how-to-read.tex, introduction.tex, any file in build/

## Files Modified

| File | Change |
|---|---|
| manuscript/00-front/the-stack.tex | NEW — ~400 words + chart |
| manuscript/00-front/the-stack-p3-scaffold.md | NEW — working document, not compiled |
| manuscript/00-front/hook.tex | Edit closing line (1-2 lines) |
| main.tex | Add one `\include` line (line 42) |

## Files NOT Modified

| File | Why |
|---|---|
| manuscript/00-front/evaluation-note.tex | Already handles LLM warning — DO NOT touch |
| manuscript/00-front/how-to-read.tex | Dead file — not compiled |
| manuscript/00-front/introduction.tex | Commented out — not compiled |
| manuscript/00-front/summary.tex | Phase 2 (Plan 0133) handles cuts |
| Any file in build/ | Content plan, not infrastructure |
| Any file in build/test-* | Auditor's test suites |

## Build Verification

```bash
cd ~/software/relinquishment && make pdf
```

Confirm: no LaTeX errors, section appears between hook and summary,
chart renders with correct triangle geometry, "?" column header visible.
