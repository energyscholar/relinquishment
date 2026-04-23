# Plan 0118: Inline Hover Definitions — Build-Time Injection

**Status:** ANNEALED
**Affects:** build/preamble.tex, build/preprocess.py, build/hover-definitions.yaml (new), Makefile (minor)
**Principle:** Mark in the text, define in the data, inject on the build. Three concerns, three files.

---

## Architecture

```
.tex files          →  \hovertip{topological order}           (marker only, one argument)
hover-definitions.yaml  →  topological order: "A property..."    (definitions, single source of truth)
PDF build           →  preamble reads YAML-generated .tex     →  italic + footnote (first occurrence)
HTML build          →  preprocess.py reads YAML               →  <span title="def">term</span>
```

**Three files, three concerns:**
1. `manuscript/*.tex` — markers only: `\hovertip{term}`
2. `build/hover-definitions.yaml` — all definitions, one place, easy to edit
3. Build system — marries markers to definitions, produces format-appropriate output

---

## Data File: `build/hover-definitions.yaml`

```yaml
# Inline hover definitions — single source of truth
# Format: term: "definition (≤25 words, clear to 12th grade reader)"
# Used by: PDF (footnotes), HTML (tooltips)

two-dimensional electron gas: "A thin layer where electrons can only move in two directions — trapped on a sheet. Found inside every computer chip."
topological order: "A property where information is stored in global patterns, not in any single place. Extremely hard to destroy."
entanglement: "Two particles linked so that measuring one instantly reveals information about the other, no matter how far apart."
quantum teleportation: "Transferring quantum information from one place to another without it crossing the space between. Demonstrated in labs since 1997."
nonlocal: "Connected across distance. Distant points share quantum correlations — information about one place is encoded in another."
autocatalytic: "Self-sustaining chemical reactions where each reaction's products help catalyze other reactions in the set."
classical backchannel: "An ordinary communication channel — radio, light, electrical signal. Required to complete quantum teleportation."
magnetosphere: "Earth's magnetic field, extending thousands of kilometers into space. Contains thin layers where charged particles are trapped flat."
guided deduction: "Teaching someone to discover the answer from public information, rather than disclosing it directly. Legally distinct from disclosure."
topological protection: "Information stored in global patterns is shielded from local disturbances — including heat. The basis of topological quantum computing."
relinquishment: "Voluntarily surrendering power — not to another owner, but permanently. Not because you're forced to, but because holding it is more dangerous than letting go."
flat worlds: "Real two-dimensional layers inside computer chips and in Earth's magnetic field. Different physics applies there."
Special Air Service: "The most elite special forces unit shared by Britain and Australia."
grew: "The system organized itself, the way living things grow. Not engineered — emerged from the physics of the substrate."
```

Bruce edits this file directly. One place, plain text, version-controlled.

---

## PDF: Footnotes via Generated Macro File

**Build step:** Python script reads YAML, generates `build/hover-generated.tex`.

**Generated file:**
```latex
% AUTO-GENERATED from build/hover-definitions.yaml — do not edit
% Regenerate: python3 build/generate-hover.py
\usepackage{etoolbox}

% Definitions keyed by term
\csdef{hover@topological order}{A property where...}
\csdef{hover@quantum teleportation}{Transferring...}
% ... one per YAML entry

% The macro: italic + footnote on first occurrence, italic-only after
\newcommand{\hovertip}[1]{%
  \textit{#1}%
  \ifcsdef{hover@#1}{\footnote{\csuse{hover@#1}}\csundef{hover@#1}}{}%
}
```

The `\csundef` trick: after first use, the definition is removed. Subsequent `\hovertip{topological order}` renders as italic only — no duplicate footnotes. Automatic first-occurrence enforcement.

**Integration:** `\input{build/hover-generated}` in preamble. Makefile runs `python3 build/generate-hover.py` before latexmk.

---

## HTML: Tooltips via preprocess.py

In `patch()`, after existing Fix 7:

1. Load `build/hover-definitions.yaml`
2. Find all `\hovertip{term}` in .tex text (brace-matching for the single argument)
3. Look up term in YAML
4. Replace with raw HTML: `<span class="hover-term" title="definition">term</span>`
5. If term not in YAML: render as italic only (graceful fallback), print warning

First-occurrence tracking: use a set per file. After first replacement for a term, subsequent occurrences render as `<em>term</em>` only (no tooltip).

CSS in `collapse_chapters()`:
```css
.hover-term { font-style: italic; border-bottom: 1px dotted #888; cursor: help; }
.hover-term:hover { border-bottom-color: #2471a3; }
@media (prefers-color-scheme: dark) {
  .hover-term { border-bottom-color: #666; }
  .hover-term:hover { border-bottom-color: #5dade2; }
}
```

---

## Implementation Phases

### Phase 1: Build Infrastructure

1. Create `build/hover-definitions.yaml` with full term set above
2. Create `build/generate-hover.py` — reads YAML, writes `build/hover-generated.tex`
3. Add `\input{build/hover-generated}` to `build/preamble.tex`
4. Add `python3 build/generate-hover.py` to Makefile `dev:` target (before latexmk)
5. Add Fix 8 to `build/preprocess.py` patch() — YAML lookup + HTML replacement
6. Add CSS to `collapse_chapters()`
7. Test: add `\hovertip{encryption}` to one line of summary.tex. Run `make dev`. Verify: PDF has italic + footnote, HTML has tooltip span. Remove test markup. Commit infrastructure only.

### Phase 2: Install Markers

After all content work (Plans 0117 + 0119) is stable:
1. In summary.tex: wrap first occurrence of each term with `\hovertip{term}`
2. In hook.tex: wrap ≤3 terms
3. Run `make dev`. Verify PDF footnotes and HTML tooltips.

---

## Acceptance Criteria

- [ ] AC1: `\hovertip{term}` in .tex renders as italic + footnote in PDF (first occurrence only)
- [ ] AC2: `\hovertip{term}` in .tex renders as `<span class="hover-term" title="def">` in HTML
- [ ] AC3: Definitions live in YAML only — not in .tex files, not in preamble
- [ ] AC4: Second occurrence of same term: italic only, no footnote/tooltip
- [ ] AC5: Unknown term (not in YAML): italic only + build warning (no crash)
- [ ] AC6: `make dev` succeeds (PDF + HTML)
- [ ] AC7: Dotted underline + help cursor in HTML (light and dark mode)
- [ ] AC8: ≥ 10 terms in YAML, ≥ 8 markers in summary.tex, ≥ 2 in hook.tex

## Generator Notes

- Read `build/preprocess.py` and `build/preamble.tex` before implementing
- `generate-hover.py` is ~30 lines: load YAML, write .tex with `\csdef` per entry + the `\hovertip` command
- preprocess.py Fix 8: brace-matching for single argument (simpler than two-argument)
- The Makefile change is one line: add `python3 build/generate-hover.py` before the latexmk call in `dev:` target (and `dms:` target)
- etoolbox package: check if already in preamble. If not, add `\usepackage{etoolbox}` to hover-generated.tex
- Test with `make dev`, not just `make html` — must verify BOTH outputs
