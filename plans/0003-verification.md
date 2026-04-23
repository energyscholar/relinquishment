# Plan 0003: Build Verification & Validation

**Author:** Auditor (Nightstalker)
**Date:** 2026-02-14
**Status:** APPROVED
**Serial:** 0003
**Requirements:** R9, R17, R21, R23, R24
**Depends on:** 0001 + 0002 (build system + content must exist)

---

## Context

Plans 0001 and 0002 created the build system and placeholder content. This plan verifies everything works: dev build compiles, validation pipeline runs, TikZ caching works, and size report generates. Docker verification is deferred (not installed on current host). Layout spot-check is an Auditor task (Generator cannot visually review PDFs).

---

## Deliverables

### 1. Run full validation suite

Execute and document results for:
- `make dev` — record wall-clock time
- `make validate` — run validation pipeline, save report
- `make size-report` — record per-component breakdown
- `make manifest` — verify manifest matches filesystem
- `make clean && make dev` — verify clean rebuild works
- Second `make dev` — verify TikZ cache makes it faster (compare wall-clock times)

### 2. Docker verification — DEFERRED

Docker is not installed on the current host. Record as "DEFERRED — Docker not available."

When Docker becomes available, the following should be tested:
- `docker build -t relinquishment-build build/`
- `docker run -v $(pwd):/src relinquishment-build make final`
- Docker build time and output comparison
- This will become a future plan (0004 or later)

### 3. Cross-reference verification

- Compile twice (latexmk handles this), check LaTeX log for "undefined reference" warnings
- All `\label{}` / `\ref{}` pairs resolve
- All `\hyperref{}` targets exist
- Glossary entries render correctly
- Check log location: `main.log` (in repo root — aux files not redirected)

### 4. Layout spot-check — AUDITOR TASK

**This step is performed by the Auditor (Bruce), not the Generator.**

The Generator cannot visually review PDFs. Instead, the Generator:
- Confirms `main.pdf` exists and reports file size and page count
- Reports any LaTeX warnings about overfull/underfull boxes

The Auditor (in a separate review) will check:
- Screen PDF: landscape orientation, single column, readable margins
- Cover triskellion colors match palette
- Track margin stripes show correct colors (teal/amber/violet)
- Placeholder images display correctly
- No layout catastrophes (pages overflowing, missing content)

### 5. Write verification report

Create `plans/verification-0003.md` (in plans/ directory, NOT build/output/ which is gitignored):
- Build times (dev first build, dev second build with cache)
- PDF page count and file size
- Validation pipeline results (pass/fail per check)
- TikZ cache effectiveness (first build vs second build time)
- LaTeX warnings summary (overfull boxes, undefined refs)
- makeglossaries status (installed/not installed)
- Docker status: "DEFERRED — not installed"
- Known issues and items for Auditor review

### 6. Update manifest

Run `make manifest` and include the updated `build/manifest.json` in the commit.

---

## Acceptance Criteria

1. `make dev` completes in < 60 seconds for full cold build; < 30 seconds for incremental (cached) rebuild
2. No "undefined reference" warnings in LaTeX log (on second pass)
3. Validation pipeline runs without script errors
4. Size report generates
5. Manifest is consistent with filesystem
6. Verification report written to `plans/verification-0003.md` with all sections filled
7. Layout spot-check explicitly marked as "DEFERRED TO AUDITOR"
8. Git commit: `Plan 0003: verification and validation`

---

## Generator Handoff

> You are the Generator. Read plan 0003 at `~/software/relinquishment/plans/0003-verification.md`. Plans 0001 and 0002 must already be implemented. Run all verification steps. You CANNOT visually review PDFs — report file size, page count, and warnings instead. Write the verification report to `plans/verification-0003.md`. Mark Docker testing as "DEFERRED." Mark layout spot-check as "DEFERRED TO AUDITOR." Commit with message `Plan 0003: verification and validation`. Report completion with build times, page count, file size, pass/fail summary.
