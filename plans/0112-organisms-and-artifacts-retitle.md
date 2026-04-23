# Plan 0112: Retitle pos27 "The Monopoly" → "Organisms and Artifacts"

**Status:** COMPLETE (verified S63 audit)
**Source:** S48 — Bruce's decision to reference Kauffman's *At Home in the Universe* Ch. 9 title. Triple reference: (1) Kauffman's published chapter on the organism/artifact boundary, (2) the chapter's actual content (is Guardian an organism or an artifact?), (3) sly breadcrumb for Kauffman's supposedly censored content Bruce remembers but can't prove.

---

## Changes

### 1. Chapter title + label (`pos27-extension.tex`)

**Line 3** — merge comment:
```
Current: % MERGE 6 (Plan 0093): Extension + Unipolar Condition → "The Monopoly"
New:     % MERGE 6 (Plan 0093): Extension + Unipolar Condition → "Organisms and Artifacts"
```

**Line 7** — chapter title:
```
Current: \chapter{The Monopoly}
New:     \chapter{Organisms and Artifacts}
```

**Line 8** — label:
```
Current: \label{pos27:the-monopoly}
New:     \label{pos27:organisms-and-artifacts}
```

The `\label` controls the HTML anchor ID. Pandoc will generate `id="organisms-and-artifacts"` from this label. Without the explicit label, Pandoc would auto-slug the chapter title to the same thing, so the label is technically redundant here — but keeping it explicit follows the convention established in Plan 0110 (Part III rename).

### 2. Hover description (`build/chapter-hover-descriptions.yaml`)

**Line 53:**
```
Current: "pos27:the-monopoly": "If Guardian is still running, what would twenty years look like?"
New:     "pos27:organisms-and-artifacts": "If Guardian is still running, what would twenty years look like?"
```

The hover text itself is still accurate — keep it.

### 3. Build comment in `main.tex`

**Line 95:**
```
Current: % Implications → habitat → monopoly → aftermath → convergence (Dual-Use moved to Part I)
New:     % Implications → habitat → organisms-and-artifacts → aftermath → convergence (Dual-Use moved to Part I)
```

### 4. Commented-out include in `main.tex`

**Line 157:**
```
Current: % \include{manuscript/track-3-awakening/pos30-unipolar-condition} % Merge 6: merged into pos27
New:     % \include{manuscript/track-3-awakening/pos30-unipolar-condition} % Merge 6: merged into pos27 (now "Organisms and Artifacts")
```

### 5. Build + verify

1. `make html` — verify the chapter heading in output has `id="organisms-and-artifacts"`
2. Verify hover tooltip still works on the chapter heading in the HTML reader
3. `make dev` — verify PDF compiles with new chapter title

---

## DO NOT CHANGE

- The `\include` path in `main.tex` line 106 stays `pos27-extension` — the filename is not being renamed. Only the chapter title changes.
- Section labels within pos27 (`pos27:the-biology-of-scale`, `pos27:vine-on-trellis`, `pos27:the-canopy`, `pos27:the-decisive-advantage`, `pos27:the-permanence`, `pos27:what-would-you-do`) are unchanged. The `hyperref` links in `topic-guide.tex` (lines 62, 170, 171) target these section labels, not the chapter label.
- SPIRAL-REPEAT comments referencing `pos27-extension.tex` are referencing the *filename*, not the chapter title. Leave them as-is.
- The word "monopoly" appears in the chapter's *body text* (lines 68, 106) as a concept. These are narrative uses, not titles. Leave them.

---

## Acceptance Criteria

1. Chapter title reads "Organisms and Artifacts" in both PDF and HTML output.
2. HTML chapter heading has `id="organisms-and-artifacts"`.
3. Hover tooltip appears on the chapter heading in the HTML reader.
4. All three `hyperref` links in `topic-guide.tex` still resolve (they target section labels, not the chapter label).
5. `make html` clean, no broken references.
6. `make dev` clean, no LaTeX errors.
7. No changes to section labels, filename, SPIRAL-REPEAT comments, or body text.

---

## Commit

`Plan 0112: retitle pos27 "The Monopoly" → "Organisms and Artifacts" (Kauffman AHitU Ch. 9)`
