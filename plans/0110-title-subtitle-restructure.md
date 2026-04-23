# Plan 0110: Title/Subtitle Restructure + Part III Rename

**Status:** OBSOLETE (subtitle changed again; Part III eliminated by Z-restructure, verified S63 audit)
**Source:** Genevieve's feedback, implemented via Bruce (S48)
**Scope:** Metadata, front matter, build system, two manuscript passages. Narrative uses of the phrase unchanged.

---

## Changes

1. **Subtitle:** "It is easier to get forgiveness than permission" → "Life in Two Dimensions"
2. **Part III title:** "Agency And Restraint" → "It is Easier to Get Forgiveness than Permission"
3. **Two in-text passages** (pos18, pos35) that call the phrase "the book's subtitle" → update structural reference

Narrative/thematic uses of "it is easier to get forgiveness than permission" throughout the manuscript are UNCHANGED. Verified: all SPIRAL-REPEAT instances use the phrase as Healer's/COWS' line in narrative context. None reference "subtitle." Only pos18 line 71 and pos35 lines 117+ call it "the subtitle."

---

## Phase 1: Subtitle Change (metadata + front matter + build)

### LaTeX files:

| File | Line | Current | New |
|------|------|---------|-----|
| `manuscript/00-front/title.tex` | 16 | `{\Large\textit{It is easier to get forgiveness than permission}}` | `{\Large\textit{Life in Two Dimensions}}` |
| `manuscript/00-front/cover.tex` | 28 | `{\Large\color{textprimary}\textit{It is easier to get forgiveness than permission}}` | `{\Large\color{textprimary}\textit{Life in Two Dimensions}}` |
| `manuscript/00-front/copyright.tex` | 12 | `\textbf{Relinquishment: It is easier to get forgiveness than permission}` | `\textbf{Relinquishment: Life in Two Dimensions}` |
| `build/preamble.tex` | 62 | `pdftitle={Relinquishment: It is easier to get forgiveness than permission},` | `pdftitle={Relinquishment: Life in Two Dimensions},` |
| `build/metadata.yaml` | 2 | `title: "Relinquishment: It is easier to get forgiveness than permission"` | `title: "Relinquishment: Life in Two Dimensions"` |

### Build system (preprocess.py):

**Line 441** — book-section summary:
```
Current: 'It is easier to get forgiveness than permission</span></summary>\n'
New:     'Life in Two Dimensions</span></summary>\n'
```

**Lines 769-770** — regex matching Pandoc's HTML title block (first occurrence):
```
Current: r'<p><span><em>It is easier to get forgiveness than\s*'
         r'permission</em></span></p>\s*'
New:     r'<p><span><em>Life in Two Dimensions</em></span></p>\s*'
```

**Lines 776-777** — same regex (second occurrence in the title block):
```
Current: r'<p><span><em>It is easier to get forgiveness than\s*'
         r'permission</em></span></p>\s*'
New:     r'<p><span><em>Life in Two Dimensions</em></span></p>\s*'
```

**Line 790** — replacement HTML:
```
Current: <p class="book-subtitle">It is easier to get forgiveness than permission</p>
New:     <p class="book-subtitle">Life in Two Dimensions</p>
```

**Regex warning:** The old subtitle was long enough that Pandoc sometimes line-wrapped it, hence the `\s*` in the original regex. "Life in Two Dimensions" is short enough that Pandoc should emit it on one line, so collapsing to a single regex line is correct. However: after making these changes, run `make html` and check whether the title block was replaced. If it wasn't (regex didn't match), run `make html 2>&1 | grep "title block"` — preprocess.py prints a status line. If no title block message appears, do a raw Pandoc build (`make html` without preprocess), inspect the raw HTML title block output, and adjust the regex to match exactly.

## Phase 2: Part III Rename

### main.tex:

```
Current (line 98): \part{Agency And Restraint}
New:               \part{It is Easier to Get Forgiveness than Permission}
                   \label{forgiveness-and-permission}
```

The `\label{}` is REQUIRED (not a recommendation). It controls the HTML anchor ID. Without it, Pandoc would generate `it-is-easier-to-get-forgiveness-than-permission` (36 characters). With it: `forgiveness-and-permission` (clean, stable, won't break if title is tweaked).

### Anchor ID updates (all instances of the old ID):

| File | Line | Current | New |
|------|------|---------|-----|
| `build/chapter-hover-descriptions.yaml` | 13 | `"agency-and-restraint": "They built something..."` | `"forgiveness-and-permission": "They built something..."` |
| `build/chapter-hover-descriptions.yaml` | 47 | `# Agency And Restraint (Part III)` | `# It is Easier to Get Forgiveness than Permission (Part III)` |
| `build/preprocess.py` | 354 | `'agency-and-restraint'` | `'forgiveness-and-permission'` |
| `build/preprocess.py` | 606 | `"agency-and-restraint"` | `"forgiveness-and-permission"` |
| `build/reader.js` | 99 | `{label: 'Agency', id: 'agency-and-restraint'}` | `{label: 'Forgiveness', id: 'forgiveness-and-permission'}` |

### Verify: after `make html`, confirm the Part III heading in the output has `id="forgiveness-and-permission"`. If Pandoc ignored the `\label{}` and used the auto-slug instead, grep for both IDs in the HTML and update the build references to match what Pandoc actually emitted.

## Phase 3: pos18 reference update

**File:** `manuscript/track-1-confession/pos18-the-walk-out.tex`

**Line 70** (SPIRAL-REPEAT comment) — update to note the phrase is now a part title:
```
Current: % SPIRAL-REPEAT: "forgiveness than permission" — subtitle through-line, also in title.tex, cover.tex, copyright.tex, colophon.tex, summary.tex, timeline.tex, abstracts.tex
New:     % SPIRAL-REPEAT: "forgiveness than permission" — Part III title through-line, also in colophon.tex, summary.tex, timeline.tex, abstracts.tex
```

**Line 71** — change "subtitle" to Part III reference:
```
Current: This is the book's subtitle and the COWS' dispositional stance
New:     This is the title of Part~III and the COWS' dispositional stance
```

## Phase 4: pos35 convergence chapter

**File:** `manuscript/convergence/pos35-the-question.tex`

**Line 117:**
```
Current: There is one thing left. The subtitle: \textit{It is easier to get forgiveness than permission.}
New:     There is one thing left. The title of Part~III: \textit{It is easier to get forgiveness than permission.}
```

The rest of the passage (lines 118-149) is unchanged. The mathematical proof, the equation, and the final large italic appearance of the phrase all stand as-is. Only the word "subtitle" on line 117 changes to "the title of Part~III."

---

## DO NOT CHANGE (verified)

All of the following are narrative uses of Healer's/COWS' phrase. None reference "subtitle." Leave them exactly as-is:

- `manuscript/00-front/summary.tex` line 141 — "That was their philosophy..."
- `manuscript/track-1-confession/pos34b-the-engine.tex` line 86 — "The COWS knew that..."
- `manuscript/99-back/colophon.tex` line 28 — standalone italic quote
- `manuscript/99-back/afterword.tex` line 89 — "The COWS knew that..."
- `manuscript/appendix/abstracts.tex` line 123 — Subject D's stated motivation
- `manuscript/appendix/abstracts.tex` line 235 — team's stated justification
- `manuscript/appendix/timeline.tex` line 209 — COWS get right with DARPA

These SPIRAL-REPEAT comments in these files still reference "subtitle through-line" in their comment text. Optionally update the comments to say "Part III title through-line" for accuracy, but this is cosmetic and low priority.

---

## Acceptance Criteria

1. `make pdf` produces a PDF with subtitle "Life in Two Dimensions" on title page and cover.
2. `make html` produces HTML with subtitle "Life in Two Dimensions" in the title block and book-section summary.
3. Part III heading reads "It is Easier to Get Forgiveness than Permission" in both PDF and HTML.
4. Part III heading in HTML has `id="forgiveness-and-permission"`.
5. The quick-jump bar in the HTML reader shows "Forgiveness" for Part III and navigates correctly.
6. `pos18-the-walk-out.tex` says "the title of Part III" not "the book's subtitle."
7. `pos35-the-question.tex` says "The title of Part III:" not "The subtitle:".
8. All 7 narrative SPIRAL-REPEAT uses of the phrase are unchanged.
9. No broken links or missing title-block replacement in `make html` output.
10. `make pdf` compiles without errors.

## Execution Order

1. Phase 1 (subtitle in LaTeX files + build metadata + preprocess.py).
2. Phase 2 (Part III rename in main.tex with `\label` + all anchor ID references).
3. `make html` — verify title block replacement worked, verify Part III ID is correct. If either fails, fix regex/ID before proceeding.
4. Phase 3 (pos18 update).
5. Phase 4 (pos35 update).
6. Final `make html` + `make pdf` — verify all 10 acceptance criteria.

**Commit:** `Plan 0110 phase 1: subtitle "Life in Two Dimensions", Part III rename`
