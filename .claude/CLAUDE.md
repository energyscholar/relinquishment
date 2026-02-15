# Relinquishment — Self-Contained Project Repository

## Architecture

- **relinquishment** (this repo) = the project. Plans, requirements, build system, manuscript, output.
- **aurasys-memory** (`~/software/aurasys-memory/`) = workshop. Research, evidence, session notes. Reference material, not build input.

## What Belongs Here

- `plans/` — Serial-numbered generator plans (0001-name.md), requirements.md
- `manuscript/` — Chapter `.tex` files (LaTeX source, Generator output)
- `build/` — Makefile, preamble, Dockerfile, images, validation scripts
- `main.tex` — Root LaTeX document (root)
- `*.pdf` — Compiled output (root, .gitignore'd)

## What Does NOT Belong Here

- Research notes, session transcripts, evidence files (those live in aurasys-memory)
- Working drafts, TODO lists, scratch files

## Write Permissions

- **Auditor** writes to: `plans/` only
- **Generator** writes to: `manuscript/`, `build/`, `main.tex`, root `.tex` files
- Neither modifies the other's territory without a plan

## Plan Convention

Plans are serial-numbered: `plans/0001-name.md`, `plans/0002-name.md`, etc.
Running all non-superseded plans sequentially from an empty directory reproduces the project.
Each plan is self-contained — no external dependencies.

## Key Rules

- Author maintains cognitive dissonance — does not claim to know which possibility is correct
- All predictions must be falsifiable
- Science must be accurate
- No fabricated evidence; speculation labeled as speculation
