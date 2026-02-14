# Relinquishment

Private repository. Book project.

## Root Policy

Root contains ONLY: `README.md`, `*.tex`, `*.pdf`, `.gitignore`. Everything else in subdirectories.

## Structure

```
plans/              Auditor plans, requirements, generator prompts
manuscript/         Chapter content (markdown source)
  00-front/           Title, preface
  track-1-confession/ The Scientist's Confession
  track-2-testament/  The Recruit's Testament
  track-3-awakening/  The Machine's Awakening
  convergence/        The center: 2006
  appendix/           Predictions, three possibilities, abstracts
  99-back/            About the author
research/           Reconstruction document, gag papers, notes
build/              LaTeX templates, build scripts, toolchain
.claude/            Claude configuration
```

## Workflow (Triad Protocol)

1. Auditor writes plan in `plans/` referencing `plans/requirements.md`
2. User copies plan to Generator shell
3. Generator implements to spec
4. Auditor verifies PASS/FAIL against requirements
5. Repeat until all requirements PASS

## Target

Single self-contained PDF. Hyperlinks, OCG layers, bookmarks, digital signature for timestamping.
