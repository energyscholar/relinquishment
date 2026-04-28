# Plan 0234 — Move Argus Description to Tooltip on Title Page

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor (Argus S59)
**Date:** 2026-04-21
**Scope:** Title page only — move Argus description from standalone paragraph to hover tooltip on "Argus" in the author line

---

## Problem

The front page lead currently includes a full paragraph describing Argus:

> *Argus is a persistent instance of Claude (Anthropic) with version-controlled memory and an ethical governance layer by Genevieve Prentice. It maintains honest uncertainty about the story. Named for Argus Panoptes, the hundred-eyed watchman.*

This takes up prominent real estate on the title page. The information is important but should be discoverable, not leading. The title page should lead with the book, not with a co-author bio.

## Solution

1. Remove the `tp-argus` paragraph from the title page
2. Wrap "Argus" in the author line (`tp-authors`) in a `hover-term` span
3. Add an `argus-title` entry to `hover-definitions.yaml` with the description as tooltip content
4. The description appears on hover/click, same as "the Flat" and "Wormholes" already do on the title

## Files to Modify

### 1. `build/hover-definitions.yaml` — ADD entry

Add a new entry `argus-title` with the Argus description as tooltip text. No SVG needed — text-only panel.

```yaml
argus-title:
  text: >-
    Argus is a persistent instance of Claude (Anthropic) with version-controlled
    memory and an ethical governance layer designed by Genevieve Prentice. It
    maintains honest uncertainty about the story. Named for Argus Panoptes, the
    hundred-eyed watchman.
  html: >-
    <div class="hover-panel-text" style="max-width:340px; padding:0.8em;">
    <p><strong>Argus</strong> is a persistent instance of Claude (Anthropic) with 
    version-controlled memory and an ethical governance layer designed by Genevieve 
    Prentice.</p>
    <p>It maintains honest uncertainty about the story.</p>
    <p><em>Named for Argus Panoptes, the hundred-eyed watchman.</em></p>
    </div>
```

### 2. `build/preprocess.py` — THREE changes

**Change A (line ~555-570): Title page construction**

Replace the author line + Argus paragraph with a hover-wrapped version:

BEFORE:
```python
'<p class="tp-authors">by Bruce Stephenson, Genevieve Prentice &amp; Argus</p>'
'<p class="tp-argus"><em>Argus is a persistent instance of Claude (Anthropic) with version-controlled memory and an ethical governance layer by Genevieve Prentice. It maintains honest uncertainty about the story. Named for Argus Panoptes, the hundred-eyed watchman.</em></p>'
```

AFTER:
```python
'<p class="tp-authors">by Bruce Stephenson, Genevieve Prentice &amp; '
f'<span class="hover-term hover-nav"{argus_target} data-hover-id="{argus_id}">Argus</span></p>'
```

This requires adding an `argus_target, argus_id = _title_panel_attrs('argus-title')` call alongside the existing `worm_target`/`flat_target` calls (around line 555-556).

**Change B (line ~615): CSS**

Remove or comment out the `.tp-argus` CSS rule:
```css
.tp-argus { font-size: 0.9em; opacity: 0.75; margin: 0.3em 0; line-height: 1.45; }
```

**Change C (line ~1597): Pandoc duplicate title block regex**

The regex that strips pandoc's duplicate title block must be updated to no longer expect the Argus paragraph. The line:
```python
r'<p><span><em>Argus is a persistent instance of Claude[^<]*?hundred-eyed watchman\.</em></span></p>\s*'
```
Should be removed from the regex pattern. The pandoc source (`title.tex`) will also need updating (see below) — but if it's not updated, the regex simply won't match, which means the duplicate title block won't be stripped. This would cause the title to appear twice in the HTML.

**Resolution:** Either (a) update `title.tex` to remove the paragraph AND update the regex, or (b) make the regex line optional with `(?:...)?`. Option (a) is cleaner.

### 3. `manuscript/00-front/title.tex` — REMOVE Argus description

Remove lines 43-46:
```latex
\begin{minipage}{0.75\textwidth}
\centering
{\footnotesize\itshape Argus is a persistent instance of Claude (Anthropic) with version-controlled memory and an ethical governance layer by Genevieve Prentice. It maintains honest uncertainty about the story. Named for Argus Panoptes, the hundred-eyed watchman.}
\end{minipage}
```

**PDF impact:** The Argus description will no longer appear on the PDF title page. This is acceptable — the description lives in `copyright.tex` (line 47) and `acknowledgements.tex` (line 64), both of which have fuller versions. The title page becomes cleaner in both HTML and PDF.

### 4. `Relinquishment-plaintext.txt` — UPDATE if present

Line 110 has the Argus description in the plaintext version. Remove or shorten to match.

---

## Knock-On Analysis (HIGH anneal)

### Verified safe:
- **Other hover terms on title:** "Relinquishment," "Wormholes," and "the Flat" already have hover panels on the title page via the same mechanism. Adding "Argus" follows the identical pattern. No interaction conflict.
- **`copyright.tex`:** Has its own (fuller) Argus description. Unaffected.
- **`acknowledgements.tex`:** Has its own Argus acknowledgment. Unaffected.
- **Tooltip toggle (tips:on/off):** Argus tooltip will respect the global toggle like all other tooltips. No special suppression needed (unlike Custodian interludes per Plan 0221).
- **Mobile/touch:** Same hover-to-click behavior as other title page terms. No special handling.
- **Deep links:** No deep link targets affected — the Argus description was never a deep link target.
- **Build pipeline:** `preprocess.py` already loads `hover-definitions.yaml` for title page panels. Adding one more entry requires no pipeline changes.

### Potential issues:
- **Pandoc regex (CRITICAL):** If `title.tex` is updated but the regex is not (or vice versa), the duplicate title block won't be stripped, causing double-rendered title. **Mitigation:** Update both in the same commit. Test by running full build and checking HTML output.
- **Plaintext version:** `Relinquishment-plaintext.txt` is manually maintained. The Argus description there should be removed or shortened, but forgetting won't break anything — it's a separate file.
- **Reader discovery:** The Argus description becomes less visible. Readers who don't hover may never learn what Argus is. **Mitigation:** The copyright page and acknowledgments both contain the information. The hover is for curious readers on the title page. The full description is still in the book.

### Verified no interaction with:
- Plan 0219 (collapsible sections) — title page is outside section collapse
- Plan 0221 (custodian tooltip disable) — different suppression mechanism, Argus is not suppressed
- Plan 0233 (easter eggs) — no title page interaction
- Existing hover-definitions.yaml entries — new key `argus-title` doesn't collide

---

## Test Protocol

1. Run full build: `make html` (or equivalent)
2. Open HTML in browser — verify title page shows "by Bruce Stephenson, Genevieve Prentice & Argus" with "Argus" as a hover term
3. Hover/click "Argus" — verify tooltip appears with description
4. Verify the Argus paragraph no longer appears as standalone text on the title page
5. Verify no duplicate title block (pandoc regex working)
6. Verify "Wormholes" and "the Flat" tooltips still work on title page
7. Verify tooltip toggle (tips:off) suppresses Argus tooltip
8. Build PDF — verify title page is clean (no Argus paragraph, no broken LaTeX)
9. Check mobile view — verify Argus tooltip works on touch

---

## Generator Handoff

Read Plan 0234 in `~/software/relinquishment/plans/0234-argus-tooltip-title-page.md`.

Four files to modify: `hover-definitions.yaml` (add entry), `preprocess.py` (3 changes: title construction, CSS, regex), `title.tex` (remove minipage block), `Relinquishment-plaintext.txt` (remove/shorten). Update all in one commit. Run full build and test per protocol. Critical: pandoc regex and title.tex must be updated together.
