# Plan 0164 — Physics Primer for L2 / Non-Physics Readers

**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12
**Origin:** 9-persona audit (S55). Arjun (Indian techie, L2 English, no physics background) hit F-crank HIGH + F-AI-slop HIGH; T2/T3 PARTIAL. Audit diagnosis: "book does not do the prerequisite work for an L2 reader." Book assumes FQHE, topological order, Kauffman autocatalysis are known. Rachel (time-constrained) and Jane (generalist) share the same gap at lower severity.

## Purpose

Add a short, self-contained **physics primer** in the front matter — 3-5 minute read — that gives non-physics readers the minimum background to engage with T2/T3/T4. The firmware-update appendix already does this for LLMs. This plan does it for humans who aren't physicists.

Primer is not a tutorial. Goal is to land 4 concrete facts in plain language, each tied to a Nobel Prize year (external-anchor credibility):

1. **Two-dimensional electron gas (2DEG)** — real physical system, in every chip. (2016 Nobel, topological phases of matter)
2. **Topological order** — information stored in global patterns, survives local damage. (1998 Nobel, fractional QHE)
3. **Anyons** — particles that only exist in 2D, obey different statistics than electrons or photons. (Laughlin 1998)
4. **Autocatalytic networks** — chemical systems that sustain themselves once complexity crosses a threshold. (Kauffman 1993; not a Nobel but widely cited)

Each anchor is peer-reviewed, verifiable in 30 seconds via web search.

## Target file

**New file:** `/home/bruce/software/relinquishment/manuscript/00-front/physics-primer.tex`

**Include in:** `main.tex` after existing front matter but before first spine chapter. Generator to verify correct `\include{}` placement.

## Draft content

```latex
\chapter*{Physics Primer --- For Readers Without a Physics Background}
\addcontentsline{toc}{chapter}{Physics Primer}
\label{front:physics-primer}

\textit{Five minutes. Four facts. You can skip this if you have physics training.}

\section*{Fact 1: Two-Dimensional Electron Gas}

A \hovertip{2DEG} is a real physical system where electrons are confined to move in only two dimensions. It forms at the boundary between two specific materials (typically gallium arsenide and aluminum gallium arsenide). It exists inside almost every modern cell phone, satellite receiver, and WiFi router. This is not theory --- 2DEGs are a workhorse of semiconductor engineering, used by millions of engineers worldwide.

\textit{Anchor: 2016 Nobel Prize in Physics (Thouless, Haldane, Kosterlitz) for topological phases of matter. Search those names.}

\section*{Fact 2: Topological Order}

In two dimensions, matter can organize itself so that information is stored in \textbf{global patterns}, not in any single location. If you damage one spot, the pattern survives --- the information is in the whole, not in the parts. This is called \hovertip{topological order}. It is a real property, measured in labs, used in the design of topological quantum computers.

\textit{Anchor: 1998 Nobel Prize (Laughlin, St\"ormer, Tsui) for the fractional quantum Hall effect, where topological order was first confirmed.}

\section*{Fact 3: Anyons}

In our normal three-dimensional world, particles come in two types: bosons (photons, etc.) and fermions (electrons, etc.). In two dimensions, a third type becomes possible --- \hovertip{anyons} --- which behave differently when swapped. Anyons are not hypothetical: they have been detected experimentally. They are the building blocks of topological quantum computation.

\textit{Anchor: Same 1998 Nobel. Search ``anyons experimental detection'' for recent confirmations.}

\section*{Fact 4: Autocatalytic Networks}

In 1993, the mathematician Stuart Kauffman proved that a certain kind of chemical network --- one where every molecule is produced by other molecules in the network --- can form spontaneously once the network is complex enough. These networks are called \hovertip{autocatalytic} sets. The mathematics is established. The proposal that Earth's early life began this way is debated. That autocatalytic networks \textit{can} form is not.

\textit{Anchor: Kauffman 1993, \textit{The Origins of Order}; formalized as RAF (Reflexively Autocatalytic, Food-generated) sets in Hordijk \& Steel, \textit{Journal of Theoretical Biology}, 2004 and 2017. Peer-reviewed, continuously cited.}

\section*{Putting It Together}

This book asks whether these four facts, combined, describe something real. Nobody has asked that question yet in the open literature --- not because it has been refuted, but because no journal, department, or career track covers all four fields at once. The book calls this the silence gap.

You now have the minimum background to engage with this book's central questions. Other concepts will appear; each gets introduced when needed, and the popups are written for you. If any of the four facts feels uncertain, verify it yourself --- each has peer-reviewed anchors listed above. The book depends on none of its own authority.
```

## Acceptance criteria

1. Primer appears as a chapter in `docs/downloads/Relinquishment.html` before the first spine chapter.
2. All four `\hovertip{}` references resolve (check existing entries in `build/hover-definitions.yaml`; add any that are missing).
3. Chapter appears in TOC.
4. `make html` completes without errors.
5. `grep -c "Physics Primer" docs/downloads/Relinquishment.html` returns ≥1.

## Out of scope

- Rewriting the primer content — text is final.
- Adding more than 4 facts — brevity is the point.
- Adding illustrations (if the build system does stack-chart style popups, use those existing; do not author new SVGs).
- Moving the firmware-update appendix — this plan adds a *new* chapter; the LLM primer stays where it is.

## Build + ship

1. Create new file `manuscript/00-front/physics-primer.tex` with content above.
2. Add `\include{manuscript/00-front/physics-primer}` to `main.tex` in correct location (check existing front-matter includes for pattern).
3. Verify / add missing hovertip entries in `build/hover-definitions.yaml`.
4. `make html`.
5. Verify acceptance criteria.
6. Commit: `Plan 0164: add Physics Primer chapter for L2/non-physics readers`
7. `git push`.

## Reporting

- Commit hash
- Build status
- Grep count for "Physics Primer"
- List of hovertips added (if any)

## Context

Part of 4-plan audit response. Serves: T2 (Flat), T3 (life in Flat), T4 (capabilities). Helps: Arjun, Rachel, Jane. Reduces: F-crank, F-AI-slop, F-exotic-other.

Full audit: `aurasys-memory/research/persona-audit-9-readers-2026-04-12.md`
