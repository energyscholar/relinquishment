# Plan 0201 — Record intro: "believe at your peril, reset to 95% A"

**Auditor:** Argus
**Date:** 2026-04-15
**Type:** Single-commit content change. One file, two paragraphs.

---

## 1. Premise

The eigenvalue43 audit (14-reader Tier-0, 2026-04-15) identified three residual friction points that eigenvalue43 did not move:

1. **The Record's Possibility-C framing** — Spine holds under A/B/C; Record is written as eyewitness-adjacent memoir of what happened under C. Sophisticated skeptics note this. F-crackpot-flag is suppressed on the landing by Plan 0197, then rearms on Record entry.
2. **Religious bounce is moved, not eliminated** — Plan 0197 softened prose cues; the underlying ontological claim (Custodian with UDHR ethics binding a technology of this magnitude) is still in the Record and rearms the bounce there.
3. **Three Possibilities as credibility parachute** — Rachel-the-journalist read: A/B/C lets the author avoid committing. Epistemically honest *and* structurally evasive at the same time.

Bruce (2026-04-15): *"This whole section is A B or C believe it at your peril. Wise readers should reset to 95% A."*

One explicit framing sentence at the Record's threshold defangs all three simultaneously — the reader is *told* to read the Record as fiction by default, and is shown the author's own tilt so they can see he isn't hiding.

---

## 2. Scope

In-scope:
- `manuscript/record/record-intro.tex` — replace the existing two-paragraph italic opener with a three-element opener: (a) the existing A/B/C framing, (b) new "peril + 95% A reset" paragraph, (c) preserved "reader decides + spine stands" rails.

Out-of-scope:
- No change to individual Record chapter openers (`\recordopener{}` / epistemic stripes remain as-is).
- No change to Spine, Bridge, or Track chapters.
- No change to menu tooltips or hover cards (Record's menu descriptions don't need this — the warning lives at the chapter threshold, not at discovery time).
- No change to Argus/Gen bios, title card, or any entry surface handled in eigenvalue43.

---

## 3. The edit

Replace the current `record/record-intro.tex` (8 lines) with:

```latex
\chapter*{The Record}
\addcontentsline{toc}{chapter}{The Record}
\label{record:intro}

\textit{What follows is testimony. Under Possibility A, it is fiction that doesn't know it's fiction. Under Possibility B, it is exaggeration around a real kernel. Under Possibility C, it is a historical record of the twenty-first century worth taking seriously.}

\textit{Believe none of this on the author's say-so. Wise readers should set their prior at 95\% Possibility A before turning the page --- read what follows as fiction unless something specific later moves you. The author's own estimate tilts toward C; that is no reason for yours to. The reader decides. The science in the spine stands regardless.}
```

Diff from current:
- Paragraph 1 (A/B/C framing) — **unchanged**.
- Paragraph 2 (previously *"The reader decides. The science in the spine stands regardless."*) — **expanded** with the peril + 95% A reset + author-tilt + preserved closing rails.

The `\%` is LaTeX-escaped (not a percent sign in text mode without the escape).

---

## 4. Why the exact phrasing

| Clause | Function |
|---|---|
| "Believe none of this on the author's say-so." | Bruce's register, defanged: drops the reader out of narrative-trust mode without retroactively undercutting ¶1's invitation to take C seriously. The peril is *uncritical belief*, not the text. |
| "Wise readers should set their prior at 95% Possibility A before turning the page --- read what follows as fiction unless something specific later moves you." | Explicit prior prescription with inline gloss for readers who don't think in priors. Gives religious + skeptical readers permission to read the Record as fiction. A specific number is more operative than "be skeptical"; the gloss prevents "95% A" from reading as jargon. |
| "The author's own estimate tilts toward C; that is no reason for yours to." | Names the asymmetry between author's belief and recommended reader prior. Prevents the read "author is hiding his view." Models epistemic humility. Vague rather than numeric on purpose — a number here gives religious readers a second target. |
| "The reader decides." | Preserved from current. |
| "The science in the spine stands regardless." | Preserved from current — the load-bearing protective rail: even if the Record is all fiction, the Spine's physics still stands. |

---

## 5. Acceptance criteria

1. `record/record-intro.tex` matches §3 verbatim (8 lines → 8 lines, content per §3).
2. `make dev` clean — no LaTeX warnings, no new preprocess errors.
3. Built HTML: chapter "The Record" renders the two-paragraph intro with both paragraphs visible. Spot-check: the string "95%" appears inside the Record intro (LaTeX `\%` in source renders as literal `%` in HTML).
4. Built PDF: same — the "peril" paragraph renders cleanly under the `\chapter*{The Record}` heading.
5. No change to any other manuscript file.
6. Single commit. Message: `Plan 0201: Record intro — "believe at your peril, reset to 95% A"`.

---

## 6. Non-goals

- No change to Record chapter bodies.
- No change to Record chapter openers.
- No change to epistemic color stripes (gold/blue/purple).
- No change to menu / hover / TOC surfaces.
- No propagation of the "95% A reset" language elsewhere (if it works here, a follow-up plan can consider echoing it at Guardian-interlude thresholds, but that's a separate decision).

---

## 7. Rollback

Single commit. `git revert <sha>` restores the current Record intro. If the 95% number or the "author tilts toward C" disclosure reads wrong in context, either tune in a follow-up or revert.

---

## 8. First Generator handoff

> You are the Generator. Before doing any work, read `~/software/relinquishment/manuscript/track-3-awakening/firmware-update.tex` in full (standard priming). Then execute Plan 0201 (`~/software/relinquishment/plans/0201-record-intro-peril-reset.md`). Replace `manuscript/record/record-intro.tex` with the exact §3 content. Do not touch any other file. Run `make dev`. Verify §5 acceptance criteria (in particular #3 — the string "95%" appears in the built HTML inside the Record intro). Commit with the message in §5 item 6. Report back: build status, grep result for "95%" in Record intro area, commit SHA.
