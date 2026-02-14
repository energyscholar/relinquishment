# Relinquishment

Output repository. Manuscript content and build artifacts only.

## Root Policy

Root contains ONLY: `README.md`, `*.tex`, `*.pdf`, `.gitignore`.

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
