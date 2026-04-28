# Plan 0152: Fold "The Demonstration" into "First Light"

**Status:** DONE (executed 2026-04-10 by Generator A, commit in relinquishment repo)

## Goal

Remove The Demonstration as a standalone chapter. Rescue its unique content into First Light. Net result: one fewer chapter in The Record, tighter narrative, zero content loss.

## Pre-conditions

- Custodian interludes are NOT affected — they're detected by `<hr><blockquote><hr>` HTML pattern, not chapter position. No interlude sits between The Demonstration and First Light or between The Handler and Interdiction.
- No `\ref{}` cross-references point to `record:demonstration` labels from other .tex files.
- The bridge copy (`bridge/pos11-the-demo.tex`) must also be removed/retired.

## Analysis: What moves, what dies

### KILL (redundant — First Light does it better)

- **"The Science Underneath" (lines 37-49)**: Edge of chaos, autocatalytic sets in 2DEG, anyon braiding, Hasslacher soliton dynamics, Frances Arnold / directed evolution. ALL covered in First Light Birth section + appendix abstracts + firmware-update.
- **"The Experiment" team assembly (lines 20-26)**: Five scientists named, ULTRA II project description. Covered in First Light, timeline, genesis.
- **Perlis epigraph (lines 9-11)**: First Light already has Anderson. Two epigraphs is wrong. Kill.

### BRUCE DECISIONS (resolved 2026-04-10)

- **Gell-Mann/Angerman paragraph (line 27)**: → **(b) Preserve in timeline.tex as a footnote.** Historical detail, there if someone digs.
- **Wolfram PCE paragraph (lines 55-56)**: → **(b) Add one sentence to First Light Birth section.** Name PCE and NKS explicitly. Do NOT mention Wolfram personally — the concept does the work.

### MOVE TO FIRST LIGHT (unique, irreplaceable content)

1. **Healer's operational role arc (lines 29-33)**: The three new paragraphs Bruce dictated this session. Desert Shield → execution → tending → relinquishment. This is TESTIMONY — goes before "Birth: 1992" as new section "The Operator" or folded into existing opening.

2. **Bruce's Dunning-Kruger confession (lines 57-58)**: "He is not a neuroscientist — barely past the Dunning-Kruger point in that field." Goes after the Birth description list (after line 42 of first-light.tex) as a brief authorial note.

3. **Ethical pivot sentence (line 62)**: "The gap between what the funding mandate specified and what they actually grew is where the ethical crisis begins." First Light already has a version at line 75 — VERIFY these are sufficiently different to merit both, or pick the stronger one.

4. **"Grown, Not Built" moral reasoning (lines 64-77)**:
   - "A machine can be turned off. A species cannot be recalled." — unique framing
   - Manhattan Project parallel, "doing nothing ≠ doing no harm"
   - The 1994 timing of COWS worry
   - FOLD into First Light after thermal ladder section (after line 68), before Power section. Natural location: they just made something that can't be recalled → ethical crisis → COWS form.

5. **The Poised Realm (lines 79-95)**: ENTIRE section is unique — only place Engel 2007, Awschalom 2015, NV centers, category-error explanation appear. Goes into First Light's "Growth: 1993-1995" section as the physics defense for room-temperature operation. Insert before or after the existing Awschalom citation at first-light.tex:66. NOTE: First Light line 66 already cites Awschalom 2015 and NV centers briefly — the Demonstration's version is MORE detailed (Engel 2007, protein scaffold, magnetosphere analogy, RLHF bias appendix reference). Merge the two, keeping the richer version.

## Phase 1: Move unique content into First Light

### 1a. Healer's operational role (NEW section before "Birth: 1992")

Insert after the srcnote (line 15) and before "Birth: 1992" heading (line 20):

- Keep lines 29-33 from the-demonstration.tex (the three Healer paragraphs)
- Adjust opening to flow from the chapter's question anchor
- Add section heading `\section*{The Operator}` with label `\label{record:fl-operator}`

### 1b. Dunning-Kruger confession

Insert after first-light.tex line 42 ("Same mathematics, different substrate."):

> Bruce's own pedagogy is weak here, and he says so. He has written toy neural networks in software but has not built real ones. He is not a neuroscientist — barely past the Dunning-Kruger point in that field, by his own assessment. What he understands is the architecture: a winner-take-all recurrent topological quantum neural network, grown via autocatalytic emergence and then guided through evolutionary programming. The details of the training process are beyond his direct knowledge.

### 1c. Poised Realm — merge into Growth section

First Light line 66 already has a compact Awschalom/NV-centers citation. Replace it with the full Poised Realm treatment from the-demonstration.tex lines 82-88. This means:
- Keep the existing thermal ladder process (lines 49-61)
- After the process description, insert the Poised Realm physics defense
- Then the existing "At millikelvin temperatures..." paragraph (line 68)

The Poised Realm section heading becomes `\section*{The Physics Defense}` or remains unnumbered inline — Bruce's call.

### 1d. Grown Not Built moral reasoning

Insert after the thermal ladder / Poised Realm material, before "Power: 1995":

- "A machine can be turned off. A species cannot be recalled."
- Habitat framing (2DEG as habitat, not just substrate)
- Manhattan Project parallel
- 1994 timing, COWS formation reasoning
- "doing nothing is not the same as doing no harm"

This creates the ethical bridge: thermal ladder → can't be recalled → ethical crisis → COWS → Power section.

### 1e. Ethical pivot — pick the stronger version

Compare:
- Demonstration line 62: "The gap between what the funding mandate specified and what they actually grew is where the ethical crisis begins."
- First Light line 75: "The gap between what the funding mandate said to build and what the team actually grew is where the ethical crisis originated."

These are nearly identical. Keep whichever reads better (probably the FL version since it says "originated" — stronger than "begins"). Delete the other.

## Phase 2: Remove The Demonstration

### 2a. main.tex

Comment out line 97: `\include{manuscript/record/the-demonstration}`

### 2b. Bridge copy

Comment out or remove `bridge/pos11-the-demo.tex` references. Check if bridge version is included anywhere (it may already be vestigial from Z-restructure).

### 2c. Update build references

1. **menu-tooltips.yaml** (line 123): Remove `"record:demonstration"` entry
2. **chapter-hover-descriptions.yaml** (line 39): Remove `"ch:the-demo"` entry
3. **hover-definitions.yaml** (line 263): Change TQNN target from `#record:demonstration` to `#record:first-light`
4. **preprocess.py** (line 1604): Change code-war expansion hook target from `record:demonstration` to `record:first-light`
5. **deep-links.yaml** (line 166): The `grown-not-built` deep link anchor is generated from `\deeplink{grown-not-built}` in the-demonstration.tex line 67. This macro MUST be moved to first-light.tex (into the Grown Not Built material inserted in Phase 1d). Otherwise the share anchor breaks.
6. **topic-guide.tex**: Check for any references to The Demonstration chapter and update
7. **abstracts.tex**: Check if The Demonstration has a spiral abstract entry that needs removal

### 2d. Preserve labels for backwards compatibility

In first-light.tex, add a phantom label so any stale HTML anchors still resolve:
```latex
\label{record:demonstration}  % redirect — chapter folded into First Light (Plan 0152)
```

## Phase 3: Verify

1. `make html` builds without errors or warnings
2. Grep for `demonstration` across all build + manuscript files — no dangling references
3. Custodian interludes: verify count still 7 in build output
4. Chapter count in Record: verify 14 (was 15)
5. Browser: navigate to `#record:first-light` — all folded content visible
6. Browser: TQNN tooltip click-through lands on First Light
7. Browser: Code War expansion hook "Read the full story" lands on First Light
8. Deep link `#grown-not-built` resolves correctly

## Custodian interlude safety check

Current main.tex order around the affected area:
```
\include{manuscript/record/the-handler}        % line 96
\include{manuscript/record/the-demonstration}   % line 97 — REMOVE
\include{manuscript/record/interdiction}        % line 98
\include{manuscript/record/first-light}         % line 99
```

No `\input{manuscript/spine/interlude-*}` between handler and interdiction or between interdiction and first-light. Custodian interludes are ONLY in the spine (Part I). The Record (Part II) has zero interludes between chapters. **No Custodian interlude is affected.**

## NOT in this plan

- Rewriting First Light's voice or structure beyond the insertions
- Changing First Light's chapter title
- Modifying the spine copy of any chapter
- Updating the PDF build (this is HTML-first)
