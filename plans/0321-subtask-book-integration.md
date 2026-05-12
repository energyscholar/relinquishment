# Subtask: Book Integration Plumbing for Scientific Revolutions

**Output:** Modify multiple build/config files to wire the new chapter into the
book's build system. Does NOT create the .tex file (that's a later step).
**Commit:** `Plan 0321: book integration plumbing — tooltips, deep links, concepts, accordions`
**Read first:** All files listed below. Understand each format before modifying.

## Overview

The chapter "The Structure of Scientific Revolutions" needs to be registered
in the book's build plumbing so that when the .tex file is eventually created,
all the automated injection systems (tooltips, deep links, concept symbols,
hover panels, chapter accordions, puzzle hooks) will work correctly.

This is config-only. No .tex file, no preprocess.py changes.

---

## 1. Hover Definitions — New Tooltips

**File:** `build/hover-definitions.yaml`

Add these entries (alphabetical placement, matching existing format):

```yaml
Possibility A1: "The A1 branch of Possibility A: autocatalytic dynamics do not produce computational structures in FQHE substrates. The silence gap is silence because there is nothing there. The distributed revolutions in condensed matter, complexity theory, and quantum information never converge into a single paradigm shift."

Possibility A2: "The A2 branch of Possibility A: the physics permits autocatalytic computation in quantum Hall substrates, but no one has looked. The anomalies exist but have not been recognized as anomalies because the question has not been framed. Structurally identical to Possibility C from a Kuhnian standpoint."

Kuhn cycle: "Thomas Kuhn's model of scientific progress (1962): Normal Science → Anomaly Accumulation → Crisis → Revolution → New Paradigm. Not gradual improvement but punctuated transformation — long periods of stability interrupted by sudden restructuring. The pattern has repeated in every major scientific field."

paradigm shift: "Kuhn's term for the replacement of one scientific framework by another. Not a gradual evolution but a structural break — the new paradigm is incommensurable with the old. Scientists on each side literally see different things when they look at the same data."

anomaly accumulation: "The Kuhnian phase where observations that don't fit the current paradigm pile up. Each is individually explicable or dismissible. The pattern — that they keep accumulating — is the signal. Precedes crisis."
```

These terms will be auto-detected by preprocess.py's hover-term injection
wherever they appear in the chapter text. "Possibility A1" and "Possibility A2"
are new vocabulary introduced in this chapter and should tooltip throughout
the book wherever they appear.

Note: "Possibility A", "Possibility B", "Possibility C" already exist in
hover-definitions.yaml. A1 and A2 are REFINEMENTS of A, introduced here.

## 2. Menu Tooltips — Chapter Hover Description

**File:** `build/menu-tooltips.yaml`

Add under the `chapters:` section, after `the-strongest-objection`:

```yaml
  "spine:scientific-revolutions":
    text: "Thomas Kuhn showed that science advances through revolutions, not increments. Eight historical examples. One animated map. A pattern that has repeated every time. An arrow showing where one open question sits on that map — if the physics permits what no one has checked."
    epistemic: A
    filter-group: A
```

## 3. Chapter Hover Description

**File:** `build/chapter-hover-descriptions.yaml`

Add entry matching format of existing entries:

```yaml
  scientific-revolutions: "Eight scientific revolutions mapped to Kuhn's framework, from Copernicus to DNA. One open question in quantum physics. A pattern the reader has seen before — if they've been watching."
```

## 4. Deep Links

**File:** `build/deep-links.yaml`

Add chapter-level deep links:

```yaml
# --- Scientific Revolutions chapter ---
- id: dl:kuhn-framework
  question: "What is Kuhn's framework and why does it matter here?"
  category: science

- id: dl:anomaly-accumulation
  question: "What are the anomalies in current quantum computing?"
  category: science

- id: dl:a1-a2-fork
  question: "What is the difference between A1 and A2?"
  category: science

- id: dl:ninth-pattern
  question: "Where does this open question sit in Kuhn's cycle?"
  category: science
```

## 5. Concept Symbols

**File:** `build/concept-symbols.yaml`

Add under `chapter_assignments:`, after `the-strongest-objection`:

```yaml
  scientific-revolutions:
    concepts: [emergence, silence]
    track: spine
    combination: true
```

Rationale: The chapter is about emergence (autocatalytic dynamics, Kauffman)
and silence (the unstudied question, the gap). Same combination as
the-silence-gap — the concepts carry through.

## 6. Accordion Sections for GA Readers

When the .tex file is eventually created, certain sections should become
collapsible `<details>` elements in the HTML build for GA readers who want
to skip physicist-level detail. These are noted here for the .tex author:

**Sections that should be GA-skippable (closed by default):**
- Section 3 deep dive into each of the four research programs (Kauffman,
  FQHE, TQC, the question) — the bullet summary stays visible, the detailed
  paragraphs collapse
- PhD seed boxes — always visible but could be in a `<details>` with
  summary "Research opportunity"

**Sections that should stay OPEN:**
- Section 4 "life" beat — this is the chapter's emotional core, don't hide it
- Section 6 conditional conclusion — the payoff, must be visible
- SVG-054 animation — already in `<details open>`
- SVG-055 spectrum — should also be `<details open>`

Implementation: Use the existing `tech-section` class pattern. In the .tex
source, wrap physicist-detail passages in a custom environment that pandoc
converts to `<details class="tech-section">`. This is the existing pattern
used 24 times in the current book.

No action required now — this is guidance for the .tex conversion subtask.

---

## Do NOT

- Create the .tex file (later step)
- Modify preprocess.py (existing injection handles everything)
- Modify main.tex
- Change any existing entries in any file
- Add the puzzle (separate subtask)

## Report

Confirm: each file modified, entry count before/after, no YAML syntax errors
(run `python3 -c "import yaml; yaml.safe_load(open('build/hover-definitions.yaml'))"` etc.
for each modified YAML file).
