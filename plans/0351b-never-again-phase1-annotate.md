# Plan 0351b: Never Again — Phase 1 (Annotate Only)

**Status:** READY FOR GENERATOR (after 0351a passes)
**Difficulty:** EASY — adds comments only, no text moves
**Purpose:** Mark each section with its destination. This is a planning step that makes the actual moves easier later.
**File:** `manuscript/record/never-again.tex`

---

## Instructions

Add a comment line ABOVE each `\section*{...}` heading. The comment states where that section will eventually move. Use exactly this format:

```
% DISASSEMBLY 0351: [DESTINATION] | priority=[HIGH/MEDIUM/LOW]
```

Here are the 5 annotations to add. Find each `\section*` by searching for the exact string shown, then insert the comment on the line immediately ABOVE it:

### Before `\section*{The Question}`:
```
% DISASSEMBLY 0351: STAYS as transition line | priority=LOW
```

### Before `\section*{The Enforcement Mechanism}`:
```
% DISASSEMBLY 0351: RELOCATE to late chapter (after moral ground) | priority=HIGH
```

### Before `\section*{The Ethical Framework}`:
```
% DISASSEMBLY 0351: SPLIT — see plan for sub-destinations | priority=HIGH
```

### Before `\section*{What Could Go Wrong}`:
```
% DISASSEMBLY 0351: TRAVELS WITH enforcement mechanism | priority=MEDIUM
```

### Before `\section*{The Cost}`:
```
% DISASSEMBLY 0351: RELOCATE to cost/consequence movement | priority=MEDIUM
```

---

## What NOT To Do

- Do NOT move any text
- Do NOT delete anything
- Do NOT change any existing lines
- ONLY add the 5 comment lines described above

---

## Verification

After adding the comments, the file should be 80 lines (75 original + 5 new comment lines). Each `\section*` should have a `% DISASSEMBLY` comment on the line immediately above it.

## Success

If Slate added 5 comment lines in the right places and nothing else changed, Phase 1 is complete. Proceed to Plan 0351c.
