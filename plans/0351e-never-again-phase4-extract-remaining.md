# Plan 0351e: Never Again — Phase 4 (Extract Remaining Sections)

**Status:** BLOCKED — awaiting Gen's confirmation of destinations from Phase 3
**Difficulty:** MODERATE — moves sub-topics to staging files
**Purpose:** Extract the labeled sub-topics and "The Cost" to their staging files.
**Files:**
- Source: `manuscript/record/never-again.tex`
- Destinations:
  - `manuscript/staging/never-again-srebrenica-motivation.tex` (NEW)
  - `manuscript/staging/never-again-hacktivismo.tex` (NEW)
  - `manuscript/staging/never-again-cost.tex` (NEW)

---

## Instructions

### Step 1: Extract Srebrenica motivation

Copy the paragraph(s) labeled `% SUB-TOPIC: Srebrenica motivation` to a new file:
`manuscript/staging/never-again-srebrenica-motivation.tex`

Header:
```latex
% Extracted from never-again.tex by Plan 0351e
% Destination: What Healer Said, near Srebrenica testimony (search for "Srebrenica" in what-healer-said.tex)
% Insert BEFORE the Srebrenica section as motivating context
```

Replace the original with:
```latex
% RELOCATED: Plan 0351e — moved to staging/never-again-srebrenica-motivation.tex
```

### Step 2: Extract Hacktivismo connection

Copy the paragraph(s) labeled `% SUB-TOPIC: Hacktivismo connection` to a new file:
`manuscript/staging/never-again-hacktivismo.tex`

Header:
```latex
% Extracted from never-again.tex by Plan 0351e
% Destination: What Healer Said, near Patrick Ball nexus (search for "Patrick Ball" in what-healer-said.tex)
% Insert AFTER the Patrick Ball nexus as connective tissue
```

Replace the original with:
```latex
% RELOCATED: Plan 0351e — moved to staging/never-again-hacktivismo.tex
```

### Step 3: Extract "The Cost"

Copy the entire "The Cost" section (heading + text) to a new file:
`manuscript/staging/never-again-cost.tex`

Header:
```latex
% Extracted from never-again.tex by Plan 0351e
% Destination: Late in book — cost/consequence movement (after enforcement + ethics)
% Exact insertion point TBD by Auditor
```

Replace the original with:
```latex
% RELOCATED: Plan 0351e — moved to staging/never-again-cost.tex
```

### Step 4: Do NOT extract UDHR-as-skeleton or UDHR adequacy

These two sub-topics STAY in place. They remain in never-again.tex (or wherever the ethical framework ultimately lives). Do not move them.

---

## What NOT To Do

- Do NOT modify extracted text
- Do NOT touch the UDHR-as-skeleton or UDHR-adequacy sub-topics
- Do NOT decide where the staging files ultimately go (that's the Auditor's job)
- Do NOT remove "The Question" section (2 lines, stays as transition)

---

## Verification

After this phase:
- 3 new staging files exist
- `never-again.tex` contains only: chapter declaration, "The Question" (2 lines), UDHR-as-skeleton, UDHR-adequacy, and several `% RELOCATED` markers
- No text was modified, only moved

## What Remains

After Phase 4, `never-again.tex` is a shell containing only:
- Chapter header + epigraph
- "The Question" (2-line transition)
- UDHR-as-skeleton + UDHR-adequacy paragraphs
- Relocation markers

A final phase (0351f) will either:
- Merge the remaining UDHR material into its destination (e.g., Letting Go chapter)
- Or keep it as a short standalone section

That decision belongs to Gen + Bruce after reviewing the extracted pieces in staging.
