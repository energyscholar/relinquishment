# Plan 0246 — Easter Egg Infrastructure

**Status:** READY for Generator
**Author:** Auditor (Argus S64, annealed S65)
**Date:** 2026-04-24 (annealed 2026-04-25)
**Parent:** Plan 0233 (Easter Egg Architecture), Phase 2a
**Purpose:** Build the /eggs/ directory, build pipeline, manifest, and make target. Infrastructure only — no ULTRA II content yet.

---

## What This Plan Does

Creates the build infrastructure for easter egg pages: standalone HTML files that share the book's styling but are not linked from navigation or TOC. One test egg validates the pipeline. Content migration (ULTRA II) is a separate phase (Plan 0233 Phase 2b).

---

## Architecture Decision: Standalone Script

**Implementation: `build/build-eggs.py`** (standalone script, NOT a function in preprocess.py).

Rationale:
- Pattern established by `build/build-puzzles.py` — another standalone page builder
- preprocess.py is 3100+ lines and handles the main build; eggs are independent
- The `make eggs` target is independent of `make html`
- Decoupled: egg pages can be rebuilt without rebuilding the main book

The script reads the manifest, converts each .tex source to HTML via pandoc, wraps it in a template with inlined CSS and reader.js, and writes the output.

---

## Files to Create

### 1. `manuscript/eggs/test-egg.tex`

Minimal test content — no custom commands (\hovertip, \deeplink, etc.):

```latex
\chapter*{Test Easter Egg}

This is a test page. If you can read this, the easter egg pipeline works.

The styling should match the main book: same fonts, same colors, same hover definitions.
```

### 2. `build/easter-egg-manifest.yaml`

```yaml
eggs:
  - slug: "test"
    source: "manuscript/eggs/test-egg.tex"
    title: "Test Easter Egg"
    status: "test"
    description: "Pipeline validation — delete before ship"
```

### 3. `build/build-eggs.py`

Structure (follow `build-puzzles.py` pattern):

```python
#!/usr/bin/env python3
"""Build standalone easter egg pages from manifest (Plan 0246)."""

import yaml
import subprocess
import os
from pathlib import Path

REPO = Path(__file__).parent.parent
MANIFEST = REPO / 'build' / 'easter-egg-manifest.yaml'
CSS_FILES = [REPO / 'build' / 'epub.css', REPO / 'build' / 'html.css']
READER_JS = REPO / 'build' / 'reader.js'
OUT_DIR = REPO / 'docs' / 'downloads' / 'eggs'

def build():
    with open(MANIFEST) as f:
        manifest = yaml.safe_load(f)

    # Read shared assets once
    css = ''
    for css_file in CSS_FILES:
        css += css_file.read_text() + '\n'
    reader_js = READER_JS.read_text()

    for egg in manifest['eggs']:
        slug = egg['slug']
        source = REPO / egg['source']
        title = egg.get('title', slug)

        # Convert .tex → HTML fragment via pandoc
        result = subprocess.run(
            ['pandoc', str(source), '-f', 'latex', '-t', 'html5', '--mathml'],
            capture_output=True, text=True, check=True
        )
        content_html = result.stdout

        # Assemble self-contained page
        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<main class="egg-content" style="max-width:42em;margin:2em auto;padding:0 1em;">
{content_html}
</main>
<p style="margin-top:3em;text-align:center;font-size:0.85em;">
<a href="../../Relinquishment.html">&larr; Return to book</a>
</p>
<script>
{reader_js}
</script>
</body>
</html>"""

        out_path = OUT_DIR / slug / 'index.html'
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page)
        print(f"  Egg: {slug} -> {out_path}")

if __name__ == '__main__':
    build()
```

Key details:
- pandoc converts .tex to HTML fragment (no --standalone) — the Python template provides structure
- CSS from epub.css + html.css is inlined in `<style>` (same files the main build uses)
- reader.js is inlined in `<script>` (provides hover term handling for future eggs)
- `max-width:42em` matches the main book's reading width
- "Return to book" link uses relative path `../../Relinquishment.html`
- No hover-data JSON injected for MVP — test egg has no \hovertip commands. When ULTRA II content arrives (Plan 0233 Phase 2b), add hover-data injection by reading `build/hover-definitions.yaml` and serializing to JSON, following the pattern in preprocess.py lines 2256-2285.

### 4. Makefile additions

Add to `.PHONY` line (after `puzzles`): `eggs`

Add target (after the `puzzles:` target block, ~line 142):

```makefile
# --- Easter egg pages (standalone, Plan 0246) ---
eggs:
	python3 build/build-eggs.py
	@echo "Egg pages built. Check docs/downloads/eggs/."
```

### 5. `make check` additions

Add to `build/verify-deep-links.py` (at end of script, before final exit):

```python
# Verify easter egg manifest ↔ built files
egg_manifest_path = REPO / 'build' / 'easter-egg-manifest.yaml'
if egg_manifest_path.exists():
    with open(egg_manifest_path) as f:
        egg_manifest = yaml.safe_load(f)
    for egg in egg_manifest.get('eggs', []):
        slug = egg['slug']
        built = REPO / 'docs' / 'downloads' / 'eggs' / slug / 'index.html'
        if not built.exists():
            print(f"  WARNING: egg '{slug}' in manifest but not built (run 'make eggs')")
```

Do NOT add to `check-strict` — egg pages are optional artifacts, not part of the main build integrity contract. Warning-only in `check`.

---

## Scope Boundary: What This Plan Does NOT Do

- **No hover-data injection.** Test egg doesn't use \hovertip. Add when ULTRA II content migrates (0233 Phase 2b).
- **No custom LaTeX command support.** Test egg uses only standard LaTeX. Future eggs using \hovertip, \deeplink, \collapse need a preamble file (`build/egg-preamble.tex`) that defines these commands as pandoc-compatible stubs. Create that file in Phase 2b, not now.
- **No discovery mechanism.** How readers find egg pages (puzzle unlock, hidden link, etc.) is a content-level decision in Plan 0233. The infrastructure just builds them.
- **No .gitignore changes.** The `docs/downloads/eggs/` output is git-tracked (same as `docs/downloads/puzzles.html`).

---

## Generator Handoff Prompt

```
You are the Generator. Read plans/0246-egg-infrastructure.md.

Build the easter egg infrastructure:

1. Create manuscript/eggs/test-egg.tex with the test content from the plan.
2. Create build/easter-egg-manifest.yaml with the test entry from the plan.
3. Create build/build-eggs.py following the plan's specification exactly.
   Key: pandoc converts .tex to HTML fragment. Python template wraps it
   with inlined CSS (epub.css + html.css) and reader.js. Output goes to
   docs/downloads/eggs/{slug}/index.html.
4. Add "eggs" to the .PHONY line and add the make target per the plan.
5. Add egg manifest verification to build/verify-deep-links.py per plan.
   Warning-only, not error.
6. Run: make eggs. Verify docs/downloads/eggs/test/index.html exists and
   renders with book styling (open in browser with xdg-open). Verify
   main HTML has no link to test egg:
   grep -c 'eggs/test' docs/downloads/Relinquishment.html  # should be 0
   Run: make check. Verify no new warnings.

Commit: "Plan 0246: easter egg build infrastructure"
Report ≤5 lines.
```

---

## Acceptance Tests

1. `make eggs` exits 0 and produces `docs/downloads/eggs/test/index.html`
2. Test egg page renders with book CSS — same fonts, colors, and reading width as main book
3. reader.js is present in the page source (for future hover support)
4. `grep -c 'eggs/test' docs/downloads/Relinquishment.html` returns 0 (no main-book link)
5. `make check` passes with no new errors (egg manifest warning OK if eggs haven't been built yet)
6. `make html` still clean (main book unaffected)
7. Return-to-book link (`../../Relinquishment.html`) resolves correctly from the egg page

---

## Annealing Log (S65: HIGH HIGH MED LOW LOW MED LOW)

### HIGH 1 — Architecture
- LOCKED: standalone `build/build-eggs.py`, not preprocess.py function
- LOCKED: pandoc fragment conversion + Python template wrapping
- LOCKED: CSS inlined from epub.css + html.css (same files as main build)
- LOCKED: reader.js inlined (future hover support without rebuild dependency)
- Found: test egg must NOT use \hovertip or other custom LaTeX — pandoc won't recognize them without a preamble. Test content already clean.

### HIGH 2 — Risks
- The main book uses `--standalone --self-contained` pandoc flags with template. Eggs use fragment mode + Python template. Visual consistency depends on CSS being sufficient without the pandoc template's HTML structure. **Mitigation:** The `egg-content` wrapper with `max-width:42em` provides the reading-width constraint. epub.css + html.css handle typography and colors. If visual delta appears in testing, Generator should adjust the wrapper styling to match — halt-and-report if styling can't converge.
- pandoc subprocess call may fail if pandoc not installed. **Mitigation:** the Makefile already depends on pandoc (the `html:` target uses it). If it's missing, `make html` would have already failed.
- reader.js initialization: it looks for `#hover-data` JSON block. Without one, the hover system initializes but does nothing. This is correct — no errors, no functionality, no harm. Verified by reading reader.js IIFE structure.

### MED — Load-bearing test
- Every piece serves the MVP: manifest (tracking), script (build), test egg (validation), make target (integration), check addition (drift prevention). Nothing to cut.
- Hover-data injection explicitly deferred — correct for MVP. Document the hook point (preprocess.py lines 2256-2285) for Phase 2b.

### LOW 1 — File paths and markers
- `build/easter-egg-manifest.yaml`: no collision with existing files ✓
- `build/build-eggs.py`: no collision ✓
- `manuscript/eggs/`: directory doesn't exist yet ✓
- `docs/downloads/eggs/`: directory doesn't exist yet ✓
- Makefile `eggs` not in .PHONY line yet (line 13 has `puzzles` but not `eggs`) ✓

### LOW 2 — Interaction with other plans
- No interaction with Plan 0249 (puzzle catalog — different pipeline, different output dir) ✓
- No interaction with Plan 0247 (continental drift — main book content) ✓
- No interaction with Plan 0248 (phonon sentence — main book content) ✓
- No interaction with Plan 0249-gen (structural mapping — read-only analysis) ✓
- Future interaction: Plan 0233 Phase 2b will migrate ULTRA II content into eggs. That plan will need to add hover-data injection to build-eggs.py and create egg-preamble.tex. Note this in 0233 when it's drafted.

### MED 2 — Generator prompt audit
- All judgment calls eliminated (implementation path locked, template specified, scope bounded)
- Six concrete verification steps
- Build-then-check pattern matches established workflow
- xdg-open for browser verification matches Bruce's VM→Chrome workflow ✓

### LOW 3 — Acceptance test audit
- 7 tests cover: existence, styling, JS presence, isolation, manifest check, regression, navigation
- Missing: no test for pandoc fragment conversion specifically. **Added:** if pandoc fails, subprocess.run with check=True will raise CalledProcessError — Generator will see it immediately.

**Rating: 9/10.** All decisions locked. No Generator judgment calls. Clean scope boundary. Hover-data hook point documented for Phase 2b. The 1-point gap: visual consistency between egg page and main book can only be fully verified at runtime. Generator should compare side-by-side.

---

## Estimate

~1 hour Generator time. Single session.
