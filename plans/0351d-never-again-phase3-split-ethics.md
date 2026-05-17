# Plan 0351d: Never Again — Phase 3 (Split Ethical Framework)

**Status:** READY FOR GENERATOR (after 0351c passes)
**Difficulty:** MODERATE — splits one section into labeled parts
**Purpose:** The Ethical Framework section contains 4 different sub-topics fused together. This phase separates them with clear labels so they can be relocated individually later.
**File:** `manuscript/record/never-again.tex`

---

## Context

"The Ethical Framework" section (find it by searching for `\section*{The Ethical Framework}`) contains these sub-topics in a single block of prose:

1. **UDHR-as-skeleton** — "The UDHR is not her instruction manual. It is her skeleton." (constitutive structure claim)
2. **Srebrenica motivation** — Why Healer chose the UDHR (trauma from witnessing the massacre)
3. **Hacktivismo connection** — Public-facing expression of the same ethics (cDc link)
4. **UDHR adequacy** — "Is a document drafted in 1948 adequate?" (gap acknowledgment, "imperfection as qualification")

---

## Instructions

### Step 1: Add sub-topic labels as comments

Insert a comment line before each sub-topic within the Ethical Framework section. These labels mark future extraction points:

Before the UDHR-as-skeleton material (the line starting "Under Possibility~C, Custodian was grown around..."):
```latex
% SUB-TOPIC: UDHR-as-skeleton — STAYS near T6 / Letting Go
```

Before the Srebrenica motivation material (the line starting "The choice of the UDHR is not arbitrary..."):
```latex
% SUB-TOPIC: Srebrenica motivation — RELOCATE to What Healer Said (near testimony)
```

Before the Hacktivismo material (the line starting "The connection to Hacktivismo is suggestive..."):
```latex
% SUB-TOPIC: Hacktivismo connection — RELOCATE to Patrick Ball nexus
```

Before the UDHR adequacy material (the line starting "Is a document drafted in 1948 adequate..."):
```latex
% SUB-TOPIC: UDHR adequacy — STAYS with UDHR-as-skeleton
```

### Step 2: That's it

This phase is labeling only. The actual extraction of these sub-topics into their destination files happens in a later phase (0351e), after Gen confirms the destinations are correct.

---

## What NOT To Do

- Do NOT move any text
- Do NOT split into separate files yet
- Do NOT modify the prose
- ONLY add the 4 comment labels

---

## Verification

The Ethical Framework section now has 4 `% SUB-TOPIC:` comments marking the boundaries between its sub-components. The prose is unchanged.

## Success

Sub-topics are labeled and their intended destinations are documented inline. Gen can now review and confirm or adjust destinations before Phase 0351e executes the actual moves.
