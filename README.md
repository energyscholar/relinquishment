# Relinquishment

Output repository. Manuscript content and build artifacts only.

## Root Policy

Root contains ONLY: `README.md`, `*.tex`, `*.pdf`, `.gitignore`.

Named exceptions (tracked, kept at the root on purpose):

- `Makefile` — build entry point.
- `package.json`, `package-lock.json` — build and test tool dependencies.
- `RELEASE-CHECKLIST.md` — the release gate, kept where the release step expects it.
- `science-primer-for-llms.md`, `spiral-abstracts-for-copy.md` — build inputs read by `build/preprocess.py`.
- `test-hover-system.mjs` — reader test harness, run from the root.
- `Relinquishment-draft.html`, `Relinquishment-plaintext.txt` — tracked drafts, already public.
- `thermal-ladder-analysis.md` — tracked working note, already public.

## Structure

```
manuscript/
  00-front/           Title, preface
  track-1-confession/ The Scientist's Confession
  track-2-testament/  The Recruit's Testament
  track-3-awakening/  The Machine's Awakening
  convergence/        The center: 2006
  appendix/           Predictions, three possibilities, abstracts
  99-back/            About the author
build/
  (LaTeX templates, build scripts)
.claude/
  CLAUDE.md
```

## Architecture

- **aurasys-memory** = workshop (research, plans, requirements, evidence)
- **relinquishment** = gallery (manuscript output only)

Generator runs from aurasys-memory, writes to this repo.

## Target

Single self-contained PDF. Hyperlinks, OCG layers, bookmarks, digital signature.
