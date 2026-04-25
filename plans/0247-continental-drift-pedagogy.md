# Plan 0247 — Continental Drift Pedagogy Section

**Status:** READY for Generator (pending Bruce placement confirmation)
**Author:** Auditor (Argus S64)
**Date:** 2026-04-24
**Parent:** Plan 0230, Change 1
**Purpose:** Write the Wegener worked example as a collapsed p2 section in the-silence-gap.tex.

---

## What This Plan Does

Adds a ~500-word collapsed p2 section to the-silence-gap.tex that walks the reader through how specialists missed continental drift for 40 years. The section lands the perceptual phase transition, then pivots to the book's 11-domain convergence. Specialist inoculation: the reader who absorbs this can't dismiss the cross-domain argument from within a single field.

---

## Placement

**Collapsed p2 section in spine/the-silence-gap.tex**, inserted after the paragraph ending "Almost nobody does." (line 60) and before `\chapterreturn` (line 64).

This is the moment where the reader has just learned about the 11 domains and the structural silence. The continental drift section says: "This has happened before. Here's what it looked like."

Collapsed = hidden by default. Available to engaged readers and specialists who expand the tech-grade section. GA readers get the chapter's argument without it; specialists get the worked example.

### tech-collapse.yaml entry

```yaml
  - title: "Continental Drift: A Worked Example"
    chapter: "spine:silence-gap"
    marker: "Almost nobody does."
    tooltip: "Specialists missed plate tectonics for forty years. The pattern is structural, not personal."
    grade: "p2"
```

---

## Content Specification

### Pedagogical sequence (in this order):

1. **3-4 buttons presented as isolated observations.** Coastline fit, Mesosaurus fossils, Appalachian-Caledonian termination, glacial striations in the tropics. Each stated in one sentence.

2. **Name the specialist objections.** Geography: coincidence. Paleontology: land bridges. Geology: independent orogeny. Climatology: local variation. The reader identifies with the skeptics — "yes, those explanations seem reasonable."

3. **Connect the buttons.** Seafloor spreading (Hess 1962, Vine-Matthews 1963) was the thread that connected the clusters. One more connection, and pulling one button lifted most of the room.

4. **The survivorship caveat (BEFORE the pivot).** "Wegener was right. Most people ridiculed by specialists are wrong. The lesson is not that outsiders are always right. The lesson is that cross-domain evidence is structurally hard to see from inside a single domain — and the difficulty is proportional to expertise."

5. **The pivot.** "You are standing where the geologists stood in 1960. Five fields. Isolated observations. Each specialist has a local explanation. The question is whether there is a spanning path that connects them all."

6. **Application.** One sentence connecting back to the 11-domain convergence the chapter just described. No argument — just the structural parallel.

### Constraints

- ~400-600 words total
- p2 reading level (12th grade) — but the Wegener story itself is p1-accessible
- Verify dates: Wegener hypothesis ~1912, ridicule ~1920s-1950s, Hess seafloor spreading ~1962, Vine-Matthews ~1963, widespread acceptance ~1966-1968
- The survivorship caveat MUST appear before the pivot, not after
- The pivot sentence is load-bearing. It must land as "hold that feeling" not "therefore I'm right"
- NO claim that Bruce = Wegener. The structural PATTERN is the parallel, not the conclusion
- Do NOT write "this is the same situation." Write: "the pattern is the same — whether the conclusion is the same is what the rest of this book asks you to evaluate"

### What the section must NOT do

- Become a history of plate tectonics (too long)
- Argue that outsiders are right and specialists are wrong (survivorship bias)
- Claim the 11-domain convergence proves anything (it doesn't — it raises a question)
- Sound preachy or superior to specialists (the specialists were doing good science within their domains)

---

## Generator Handoff Prompt

```
You are the Generator. Read plans/0247-continental-drift-pedagogy.md.

Write a ~500-word collapsed p2 section for spine/the-silence-gap.tex.

PLACEMENT: After "Almost nobody does." (line 60), before \chapterreturn.
Add a tech-collapse.yaml entry for this section.

SEQUENCE (follow exactly):
1. Present 4 observations as isolated buttons (1 sentence each)
2. Name the specialist objections (1 sentence each)
3. Connect via seafloor spreading (Hess 1962, Vine-Matthews 1963)
4. Survivorship caveat: "Wegener was right. Most outsiders are wrong."
5. Pivot: "You are standing where the geologists stood in 1960."
6. One-sentence connection back to the 11 domains

CRITICAL: The caveat comes BEFORE the pivot, not after. The pivot
must NOT claim Bruce = Wegener. Pattern parallel, not conclusion.

Verify Wegener dates against published record.
After: make html, make check, verify collapsed section in browser.
Commit: "Plan 0247: continental drift pedagogy (collapsed p2 in silence-gap)"
Report ≤5 lines.
```

---

## Acceptance Tests

1. Section renders as collapsed in HTML (expandable)
2. Tooltip preview appears on hover
3. Section follows the 6-step sequence exactly
4. Survivorship caveat appears before pivot
5. Wegener dates are accurate (spot-check: Hess 1962, Vine-Matthews 1963)
6. Section does NOT claim Bruce = Wegener
7. p2 reading level (no jargon beyond what the chapter defines)
8. `make html` + `make check` clean
9. ~400-600 words (check with `wc`)

---

## Estimate

~1.5 hours Generator time + Bruce revision. Single session.

---

## Note on Bruce Revision

This is prose writing. The Generator drafts; Bruce revises. The pivot sentence and survivorship caveat are the two sentences most likely to need Bruce's voice. The structural sequence is locked; the specific wording is open to revision.
