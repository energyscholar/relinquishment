# Plan 0351c: Never Again — Phase 2 (Extract Enforcement Mechanism)

**Status:** READY FOR GENERATOR (after 0351b passes)
**Difficulty:** MODERATE — moves one section to a staging file
**Purpose:** Extract the enforcement mechanism section into a staging file. This is the single highest-priority extraction.
**Files:**
- Source: `manuscript/record/never-again.tex`
- Destination: `manuscript/staging/never-again-enforcement.tex` (NEW FILE)

---

## Instructions

### Step 1: Create the staging file

Create a new file at `manuscript/staging/never-again-enforcement.tex` with:
- A comment header explaining what this is
- The content of "The Enforcement Mechanism" section (the `\section*` heading + all text until the next `\section*`)
- The content of "What Could Go Wrong" section (these travel together)

The file should look like this:

```latex
% Extracted from never-again.tex by Plan 0351c
% These sections relocate to a late chapter (after moral ground is established)
% Do not re-insert here — destination TBD by Auditor

\section*{The Enforcement Mechanism}
[... all text from \section*{The Enforcement Mechanism} up to (not including) \section*{The Ethical Framework} ...]

\section*{What Could Go Wrong}
[... all text from \section*{What Could Go Wrong} up to (not including) \section*{The Cost} ...]
```

Copy the EXACT text. Do not modify, rewrite, or improve it.

### Step 2: Replace those sections in the source file

In `never-again.tex`, replace the enforcement mechanism section (from its `% DISASSEMBLY` comment through to just before `\section*{The Ethical Framework}`) with:

```latex
% RELOCATED: Plan 0351c — moved to staging/never-again-enforcement.tex
```

Replace the "What Could Go Wrong" section (from its `% DISASSEMBLY` comment through to just before `\section*{The Cost}`) with:

```latex
% RELOCATED: Plan 0351c — moved to staging/never-again-enforcement.tex
```

---

## What NOT To Do

- Do NOT modify the extracted text (copy verbatim)
- Do NOT touch "The Question", "The Ethical Framework", or "The Cost" sections
- Do NOT delete any `\srcnote` or `\label` commands — they travel with their text
- Do NOT run the build system (that's a separate verification step)

---

## Verification

After this phase:
- `manuscript/staging/never-again-enforcement.tex` exists with 2 sections
- `never-again.tex` is shorter (2 sections replaced by single-line comments)
- The remaining sections (The Question, The Ethical Framework, The Cost) are untouched

## Success

Two sections cleanly extracted. The staging file preserves all text verbatim. Proceed to Plan 0351d.
