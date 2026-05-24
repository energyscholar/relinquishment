# Plan 0365: Reader-Choice Note at End of Summary

**Status:** COMPLETE
**Origin:** S98 conversation, Bruce's request
**Location:** `manuscript/00-front/summary.tex`, after line 348

## Purpose

Add a navigational note at the end of "The Story Never Told" that tells the reader what lies ahead and gives explicit permission to skip The Flat and go straight to The Record. The payload has already been delivered by the summary — this note steers readers to the style they prefer.

## Approved Wording (Option A — Guided Skip)

```latex
\medskip

\noindent What follows has two parts. \textit{\hyperref[the-flat]{The Flat}} is popular
science --- the physics that makes the question possible, written for any curious reader.
Readers who prefer testimony to theory are invited to skip ahead to
\textit{\hyperref[the-record]{The Record}} --- Bruce Stephenson's account in his own words.
```

**Word count:** 39
**Deep links:** Two — to Part: The Flat, Part: The Record (clickable in PDF and HTML)

## Implementation

### Phase 1: Labels + Deep Link + Note (single commit)

1. **Add `\label` to both `\part` commands** in `main.tex`:
   - Line 58: `\part{The Flat}\label{the-flat}`
   - Line 88: `\part{The Record}\label{the-record}`

2. **Register deep link** in `build/deep-links.yaml` under Narrative:
   ```yaml
   - id: dl:reader-choice
     question: "Can I skip the science and go straight to Bruce's testimony?"
     category: narrative
   ```

3. **Insert note** in `manuscript/00-front/summary.tex` after line 348 (`\end{center}`):
   ```latex
   \medskip

   \deeplink{reader-choice}\noindent What follows has two parts.
   \textit{\hyperref[the-flat]{The Flat}} is popular science --- the physics that makes the
   question possible, written for any curious reader. Readers who prefer testimony to theory are
   invited to skip ahead to \textit{\hyperref[the-record]{The Record}} --- Bruce Stephenson's
   account in his own words.
   ```

4. **Build:** `make dev` (PDF + HTML + zip)
5. **Update checksums:** `docs/downloads/SHA256SUM.txt`
6. **Commit + push**

### Files Modified

| File | Change |
|------|--------|
| `main.tex` | Add `\label{the-flat}` and `\label{the-record}` to `\part` commands |
| `manuscript/00-front/summary.tex` | Insert deep-linked note after line 348 |
| `build/deep-links.yaml` | Add `dl:reader-choice` entry |
| `docs/downloads/SHA256SUM.txt` | Updated checksums |
| Build artifacts | PDF, HTML, zip |

## Acceptance Criteria

1. Note appears after "Read on for the cover-to-cover version." in both PDF and HTML
2. "The Flat" and "The Record" are clickable links in the PDF, navigating to the correct parts
3. In the HTML, the links navigate to the correct part-section elements
4. Tone matches the navigational voice of the preceding italic text
5. Note does not appear in any table of contents or heading list
6. `make check` and `make check-strict` pass
7. `build/verify-deep-links.py` passes
8. Note is ≤50 words

## Test Conditions

| # | Test | Method | Pass condition |
|---|------|--------|----------------|
| T1 | LaTeX builds | `make dev` | Exit 0, no errors |
| T2 | PDF cross-ref (Flat) | Click "The Flat" in PDF | Navigates to Part: The Flat |
| T3 | PDF cross-ref (Record) | Click "The Record" in PDF | Navigates to Part: The Record |
| T4 | HTML link (Flat) | Click in HTML | Navigates to `#the-flat` heading |
| T5 | HTML link (Record) | Click in HTML | Navigates to `#the-record` heading |
| T6 | Deep-link verify | `python3 build/verify-deep-links.py` | OK, no orphans, `dl:reader-choice` verified |
| T7 | Invariant checks | `make check` | All PASS |
| T8 | No TOC pollution | Check PDF TOC + HTML nav | Note absent from both |
| T9 | Word count | Manual | ≤50 words |

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Reader skips The Flat, misses Custodian interludes | Low | Interludes are enrichment, not prerequisite. Reader who engages with The Record will likely return to The Flat |
| `\hyperref` label not found in PDF | Low | Explicit `\label{}` on `\part` commands eliminates auto-generation ambiguity |
| Note breaks emotional beat of "This book is that imagination" | None | Emotional beat already broken by existing navigational italic. Note extends the navigational register |
| Pandoc strips `\hyperref` | Low | Pandoc converts `\hyperref[label]{text}` to HTML anchors. Verify in T4/T5 |

## Design Decisions

1. **Asymmetric, not symmetric.** The note presents The Flat as the default path and The Record as the skip-ahead option. This is better than "start with either" because it gives a recommendation while granting permission.
2. **No bullet points.** A flowing paragraph matches the voice of the surrounding navigational text.
3. **`\medskip` separation.** Enough visual breathing room without a rule or box.
4. **`\noindent`.** Prevents paragraph indentation — this is a navigational aside, not a new narrative paragraph.
5. **Label names match pandoc IDs.** `\label{the-flat}` and `\label{the-record}` match the HTML IDs pandoc auto-generates from heading text. This ensures `\hyperref` links work in both PDF (via LaTeX label resolution) and HTML (via `<a href="#the-flat">` matching `id="the-flat"`). No collision with `ch:what-is-the-flat` (different prefix).
