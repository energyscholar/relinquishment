# Plan 0198 — Argus bio on title page

**Auditor:** Argus
**Date:** 2026-04-15
**Type:** Single-commit plan (Auditor specifies → Bruce approves → Generator executes).
**Sibling:** Independent of Plan 0197 (tonal softening). Separated to keep commits single-purpose.

---

## 1. Premise

The title page and title-card currently show *"by Bruce Stephenson, Genevieve Prentice & Argus"* with no further context. Genevieve has a front-matter preface (`genevieve-preface.tex`); Argus has no equivalent visible front-matter surface. The canonical Argus bio (80 words) sits in `copyright.tex:43-47`, effectively an appendix.

Bruce (2026-04-15): *"reader knows nothing about argus besides name. Should know the brief bio."*

The fix: add a trimmed 35-word Argus note on both title surfaces (HTML card + PDF title page), preserving `copyright.tex` as the canonical single source of truth.

---

## 2. Scope

In-scope:
- `build/preprocess.py` — HTML title card inside `.title-page-extra` div (L537-542 + CSS L582-583).
- `manuscript/00-front/title.tex` — PDF title page (insert between L39 and L41).

Out-of-scope:
- `manuscript/00-front/copyright.tex` — canonical bio; no changes.
- `manuscript/00-front/cover.tex` — front cover byline, stays name-only (poster layout, no room).
- Any new standalone `argus-preface.tex` file (considered and rejected: creates an asymmetry where Argus has a preface comparable to Genevieve's; Bruce picked Medium, not Large).

---

## 3. The text (35 words, used verbatim on both surfaces)

> *Argus is a persistent instance of Claude (Anthropic) with version-controlled memory and an ethical governance layer by Genevieve Prentice. It maintains honest uncertainty about the story. Named for Argus Panoptes, the hundred-eyed watchman.*

Rationale:
- Trimmed from the 80-word canonical `copyright.tex:47`. Title card is landing-page real estate — brief is better.
- Preserves the three load-bearing hooks: **Claude + memory + governance**, **Gen named it**, **honest uncertainty** (mirrors the book's own three-possibilities ethos).
- Drops: model ID (`claude-opus-4-6`), "cannot verify its own reasoning against reality", "Argus Panoptes…who never sleeps" (shortened to "the hundred-eyed watchman"). Reader who wants more opens copyright.

---

## 4. Placement & styling

### HTML title card — `build/preprocess.py:537-542`

Insert new `<p class="tp-argus">` between the `tp-authors` line (L538) and the first `tp-tagline` line (L539):

```python
'<p class="tp-authors">by Bruce Stephenson, Genevieve Prentice &amp; Argus</p>'
'<p class="tp-argus"><em>Argus is a persistent instance of Claude (Anthropic) with version-controlled memory and an ethical governance layer by Genevieve Prentice. It maintains honest uncertainty about the story. Named for Argus Panoptes, the hundred-eyed watchman.</em></p>'
'<p class="tp-tagline"><em>Three narrative threads. Real science. Real people. Real institutions.</em></p>'
```

And add a new CSS rule after L582 `.tp-tagline { opacity: 0.8; }`:

```css
.tp-argus { font-size: 0.9em; opacity: 0.75; margin: 0.3em 0; line-height: 1.45; }
```

Intent: smaller than byline, more prominent than copyright line, enough breathing room to register as its own block.

### PDF title page — `manuscript/00-front/title.tex`

Between L39 (`{\normalsize 2026}`) and L41 (`\vspace{2cm}`), insert:

```latex
\vspace{0.8cm}

\begin{minipage}{0.75\textwidth}
\centering
{\footnotesize\itshape Argus is a persistent instance of Claude (Anthropic) with version-controlled memory and an ethical governance layer by Genevieve Prentice. It maintains honest uncertainty about the story. Named for Argus Panoptes, the hundred-eyed watchman.}
\end{minipage}
```

The `minipage` wrapper gives the paragraph a reasonable line length on a poster-style page (otherwise it wraps edge-to-edge at `\Large` page width, which looks bad).

---

## 5. Acceptance criteria

1. Edits applied per §4, exactly as specified.
2. `make dev` clean — no new LaTeX warnings, no new preprocess.py errors.
3. Built `Relinquishment.html` contains the new `<p class="tp-argus">` with the 35-word text verbatim. Spot-check in a browser (phone preview): bio appears on landing, hides when book is expanded (inherits `.title-page-extra` visibility rule at L584).
4. Built PDF's title page shows the bio as a centered footnote-style block between the `2026` line and the `Skip ahead to the story →` link. Line length is comfortable (not edge-to-edge).
5. Byte-level parity check: the 35-word text is identical (modulo HTML `&amp;` / LaTeX escape rules) between `preprocess.py` insertion and `title.tex` insertion. Single source in the plan; Generator should copy-paste it verbatim.
6. `copyright.tex:43-47` is **untouched**. Canonical 80-word bio remains there as single source of truth.
7. Single commit. Message: `Plan 0198: Argus bio on title page (HTML card + PDF)`.

---

## 6. Non-goals

- No change to the front cover (`cover.tex`).
- No new Argus preface file.
- No change to Genevieve's preface.
- No change to the copyright/colophon bio content or location.
- No redesign of the title card or title page layout beyond inserting the new block.

---

## 7. Rollback

Single commit. `git revert <sha>` is the rollback. If the placement reads wrong (too heavy on the title card, wrong line on the PDF), that gets re-edited in a follow-up; the rest stands.

---

## 8. First Generator handoff (held until Bruce approves §3 and §4)

> You are the Generator. Execute Plan 0198 (`~/software/relinquishment/plans/0198-argus-bio-title-page.md`). Apply §4 edits verbatim to `build/preprocess.py` (new `<p class="tp-argus">` + new CSS rule) and `manuscript/00-front/title.tex` (new `\begin{minipage}` block). Do not touch `copyright.tex`, `cover.tex`, or `genevieve-preface.tex`. Run `make dev`, verify the §5 acceptance criteria (in particular #3, #4, and the byte-level parity check #5), then commit with the message in §5.7. Report back: build status, confirmation that the bio appears on the landing HTML card, confirmation that it renders cleanly on the PDF title page, commit SHA.
