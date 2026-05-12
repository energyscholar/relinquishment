# Subtask: Add Deep-Link Anchors to Scientific Revolutions .tex

**Output:** Add four `\deeplink{}` macros to
`manuscript/spine/scientific-revolutions.tex`
**Commit:** `Plan 0321: add deep-link anchors to Scientific Revolutions`
**Read first:** This spec, then the .tex file.

## Context

Four deep-link IDs are registered in `build/deep-links.yaml` but have no
corresponding `\deeplink{}` anchors in the .tex. The `\deeplink{id}` macro
expands to `\hypertarget{dl:id}{}`, which pandoc converts to an anchor that
preprocess.py transforms into `<span class="share-anchor" id="dl:id">`.
Without these, the questions index links to `#dl:kuhn-framework` etc. point
to nowhere.

## Changes

Add one `\deeplink{}` call at the start of each target section's first
paragraph. This is the existing pattern used throughout the book (see
`the-flat.tex` lines 19, 21, 25, 67, 73 for examples).

### 1. `dl:kuhn-framework` → Section 1 "The Pattern"

Line 19 currently starts:
```
Thomas Kuhn identified a recurring structure
```
Change to:
```
\deeplink{kuhn-framework}Thomas Kuhn identified a recurring structure
```

### 2. `dl:anomaly-accumulation` → Section 3 "Anomaly Accumulation"

Line 51 currently starts:
```
Kuhn's anomalies are not errors.
```
Change to:
```
\deeplink{anomaly-accumulation}Kuhn's anomalies are not errors.
```

### 3. `dl:a1-a2-fork` → Section 4 "Life in the Flat"

Line 75 currently starts:
```
What emerges from a sufficiently complex
```
Change to:
```
\deeplink{a1-a2-fork}What emerges from a sufficiently complex
```

### 4. `dl:ninth-pattern` → Section 7 "The Reader's Position"

Line 159 currently starts:
```
The preceding chapter
```
Change to:
```
\deeplink{ninth-pattern}The preceding chapter
```

## Idempotency

Each `\deeplink{}` call is a no-op if already present. Grep for
`\deeplink{kuhn-framework}` etc. — if found, skip that insertion.
The macro itself is idempotent (produces an empty hypertarget).

## Do NOT

- Modify any other file
- Change any prose text
- Add or remove any other macros
- Run `make`

## Report

Confirm: four `\deeplink{}` calls added, grep shows all four present,
no other changes to the file.
