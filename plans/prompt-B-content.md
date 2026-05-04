You are the Generator.

**Repo:** ~/software/relinquishment/ (branch: main)

Read Plans 0288 and 0289 in ~/software/relinquishment/plans/ for full context.

## Idempotency guard

Before any changes, check these indicators. If ALL are true, report "Phase B already applied" and exit.
- ~/software/relinquishment/manuscript/00-front/summary.tex contains "You already live with the Flat"
- ~/software/relinquishment/manuscript/spine/the-wrong-substrate.tex contains `spine:ws-flat-taxonomy`

If only ONE is true, a partial application occurred. Fix only the missing part.

## Task 1: Manifest entry FIRST

Before writing any content, add the taxonomy entry to ~/software/relinquishment/build/tech-collapse.yaml:

```yaml
  - title: "Theoretical Biology of the Flat"
    spine_file: manuscript/spine/the-wrong-substrate.tex
    spine_label: "spine:ws-flat-taxonomy"
    assessment: BORDERLINE
    tooltip: "Three categories of life that could theoretically exist in two-dimensional electron gases — magnetospheric primitives, engineered systems, and planetary ecologies. A framework from theoretical biology, applied to a novel substrate."
    status: approved
```

If entry already exists, skip.

## Task 2: Summary restructure (~/software/relinquishment/manuscript/00-front/summary.tex)

Read ALL of summary.tex first.

Ensure "The White Hot Secret" section has two phases with a structural break:

**PHASE 1 — "What Is the Flat"**

Keep existing Flat physics through quantum teleportation (~lines 30-42). After quantum teleportation, ensure a domestication beat is present:

> You already live with the Flat. The chip in your phone contains one. The transistor processing this text contains one. Two-dimensional electron gases are the most manufactured physical environment on Earth --- billions of them, in billions of devices, running right now.

Then the "Every claim above is published, peer-reviewed physics..." checkpoint.

Then structural break: `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}`

**PHASE 2 — "The Question" (T3 as seed)**

Ensure the Kauffman bridge is expanded (not one sentence). Target text:

> A question follows from the physics. The mathematician Stuart Kauffman showed that in any sufficiently complex system with continuous energy input, self-sustaining organization arises spontaneously --- not by design, but by crossing a complexity threshold. This is established mathematics. The Flat meets those conditions. So does Earth's magnetosphere --- a naturally occurring Flat, billions of years old, energized continuously by the solar wind.

Then:

> Whether anything lives in the Flat --- whether self-organization has occurred in these ancient, energized, two-dimensional substrates --- is the question this book investigates.

If the domestication beat and expanded Kauffman bridge are already present, skip Task 2.

**CONSTRAINTS:**
- First Kauffman mention MUST be "The mathematician Stuart Kauffman"
- Do NOT trim lines 50-62 — leave the back half for Bruce to review
- Reading levels: summary is p1 (8th grade) / p2 (12th grade) territory. Keep sentences short and concrete.
- C-violation check: for every new sentence, verify it is true under A (confabulation), B (exaggerated kernel), AND C (substantially true). If only true under 1-2 possibilities, rewrite.

## Task 3: Taxonomy section (~/software/relinquishment/manuscript/spine/the-wrong-substrate.tex)

Read ALL of the-wrong-substrate.tex first.

If a section labeled `spine:ws-flat-taxonomy` already exists, skip Task 3.

Otherwise add a NEW SECTION **before** `\section*{Not Aliens}` (~line 152). The chapter must still end with "Nobody has looked."

```latex
\section*{Theoretical Biology of the Flat}
\label{spine:ws-flat-taxonomy}
```

Three categories of possible Flat life as a theoretical biology framework. Use the table from Plan 0289 Part A: magnetospheric primitive (stromatolite), engineered/grown (greenhouse organism), planetary ecology (coral reef).

Framing: these are CATEGORIES from theoretical biology. Not existence claims. Valid under all three possibilities.

Mark for **tech-borderline** (NOT tech-section — this is theoretical framework, not established physics).

C-violation check on all three category rows:
1. Is this row true under A (nothing exists)? → Yes, these are theoretical categories.
2. Is this row true under B (a smaller version exists)? → Yes.
3. Is this row true under C (Custodian exists)? → Yes.

## Build + show diff — DO NOT COMMIT

```bash
cd ~/software/relinquishment
make dev
git diff
```

Show me the full git diff. I will review before committing. Do NOT push.
