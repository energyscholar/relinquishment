# Plan 0316: Idempotent PDF Optimization

**Created:** 2026-05-09 (Session 71)
**Purpose:** Repeatable, idempotent PDF quality pass. Run after any content change.
**Depends on:** Plan 0315 (P2 items), PDF QA audit (Plan 0314 / S71)
**Scope:** Build-system fixes only. No content changes.

## Principle

Every fix is a build-system transformation, not a manual edit. The script reads source, applies corrections, generates PDF. Safe to re-run after any content drift.

## Systematic Issues (apply globally via CSS/LaTeX conditionals)

### S1: Navigation Arrows
**Problem:** `◁` `▷` arrows appear on every page (HTML nav elements bleeding into PDF).
**Fix:** CSS `@media print { .nav-arrow, .page-nav { display: none !important; } }` or equivalent LaTeX conditional `\ifpdf`.
**Idempotent:** Yes -- CSS rule is additive.

### S2: Section Tab Labels
**Problem:** BRIDGE / AWAKENING / CONFESSION / CONVERGENCE / TESTAMENT labels in right margin.
**Fix:** CSS `@media print { .section-tab, .margin-label { display: none !important; } }` or LaTeX margin suppression.
**Idempotent:** Yes.

### S3: TOC Return Links
**Problem:** "Return to Table of Contents" links appear at chapter boundaries. "TOC" text at page footer.
**Fix:** CSS `@media print { .toc-return, .toc-link { display: none !important; } }`.
**Idempotent:** Yes.

## Local Defects (apply via source correction)

### L1: "Hspent" Typo (p.224 Acknowledgements)
**Problem:** "Hspent his last years" should be "He spent his last years."
**Fix:** Grep source for "Hspent" and correct. 
**Idempotent:** Grep finds nothing if already fixed.
**Verify:** `grep -r "Hspent" manuscript/`

### L2: Missing Macron (p.203 Timeline)
**Problem:** "Maori" without macron. Should be "Maori" with macron on the a.
**Fix:** Search source for unaccented "Maori" instances, replace with macron version.
**Caution:** Some instances may be intentional (e.g., in quoted material). Check each.
**Idempotent:** Already-macronned text won't match the search.
**Verify:** `grep -rn 'Maori' manuscript/ | grep -v 'Maori'` (with macron in the exclusion pattern)

## Verification Script

```bash
#!/bin/bash
# post-pdf-check.sh — run after every PDF build
set -euo pipefail
PDF="${1:-Relinquishment.pdf}"

echo "=== PDF QA Check ==="

# Check for systematic issues in extracted text
pdftotext "$PDF" - | {
    echo -n "Nav arrows: "
    grep -c '◁\|▷' || echo "0 (PASS)"
    
    echo -n "Tab labels: "
    grep -c 'BRIDGE\|AWAKENING\|CONFESSION\|CONVERGENCE\|TESTAMENT' || echo "0 (PASS)"
    
    echo -n "TOC links: "
    grep -c 'Return to Table of Contents' || echo "0 (PASS)"
    
    echo -n "Hspent typo: "
    grep -c 'Hspent' || echo "0 (PASS)"
}

echo "=== Done ==="
```

## Execution

**Generator work.** Auditor provides this plan; Generator implements the CSS/LaTeX fixes and verification script.

### Phase 1: CSS/LaTeX conditionals for S1-S3
### Phase 2: Source corrections for L1-L2
### Phase 3: Verification script integration into build pipeline
### Phase 4: Rebuild PDF + visual spot-check (3 pages: early, middle, late)

## Re-run Protocol

After any content change:
1. Run build
2. Run `post-pdf-check.sh`
3. If any check fails, diagnose and fix
4. Rebuild and re-check

This cycle is the idempotent loop. Content authors never need to think about PDF rendering issues.
