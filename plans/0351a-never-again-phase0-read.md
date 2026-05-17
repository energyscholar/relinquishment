# Plan 0351a: Never Again — Phase 0 (Read & Confirm)

**Status:** READY FOR GENERATOR
**Difficulty:** TRIVIAL — no file changes
**Purpose:** Verify Slate can read the manuscript file and understand its structure.
**File:** `manuscript/record/never-again.tex`

---

## Instructions

Read the file `manuscript/record/never-again.tex`.

Then confirm the following by listing them back:

1. How many lines is the file?
2. What are the 5 section headings (look for `\section*{...}` commands)?
3. What line number does each section start on?
4. What is the first sentence of the chapter (after the italic epigraph)?
5. What is the last line before `\chapterreturn`?

---

## Expected Answers

(For the Auditor to verify against)

1. 75 lines
2. The Question, The Enforcement Mechanism, The Ethical Framework, What Could Go Wrong, The Cost
3. Line 15, Line 22, Line 35, Line 49, Line 64
4. "If relinquishment is the answer, what enforces it?"
5. "Under Possibility~C, this is an act of restraint of unusual scale. Under any possibility, it is worth asking: would you have the courage to let go?"

---

## Success

If Slate can list these correctly, it has manuscript access and can parse LaTeX structure. Proceed to Plan 0351b.

## If It Fails

If Slate cannot read the file, the access path needs to be resolved before any further plans run. Report back what error occurred.
