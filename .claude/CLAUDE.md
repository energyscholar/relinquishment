# Relinquishment — Output Repository

## This Repo Is OUTPUT ONLY

This repo contains ONLY manuscript content and build artifacts. No research, no plans, no working documents.

**Root policy:** Only `README.md`, `*.tex`, `*.pdf`, `.gitignore` in root.

## Architecture

- **aurasys-memory** (`~/software/aurasys-memory/`) = workshop. Research, evidence, plans, requirements, session notes. Auditor and Generator RUN there.
- **relinquishment** (this repo) = gallery. Generator WRITES here. Only finished manuscript content.

## What Belongs Here

- `manuscript/` — chapter markdown files (Generator output)
- `build/` — LaTeX templates, build scripts
- `*.tex` — main LaTeX document (root)
- `*.pdf` — compiled output (root)

## What Does NOT Belong Here

- Research notes, session transcripts, evidence files
- Plans, requirements, auditor documents
- Working drafts, TODO lists, scratch files

## Generator Instructions

When writing chapters, the Generator runs from aurasys-memory (full research context) and writes output files to this repo at `/home/bruce/software/relinquishment/manuscript/`.

## Key Rules

- Author maintains cognitive dissonance — does not claim to know which possibility is correct
- All predictions must be falsifiable
- Science must be accurate
- No fabricated evidence; speculation labeled as speculation
