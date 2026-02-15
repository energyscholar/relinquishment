#!/bin/bash
# Validation pipeline for Relinquishment build
# Run from repo root: make validate

set -euo pipefail

echo "=== Relinquishment Build Validation ==="
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

PASS=0
FAIL=0
WARN=0

check() {
    local name="$1"
    local result="$2"
    if [ "$result" = "PASS" ]; then
        echo "  [PASS] $name"
        PASS=$((PASS + 1))
    elif [ "$result" = "WARN" ]; then
        echo "  [WARN] $name"
        WARN=$((WARN + 1))
    else
        echo "  [FAIL] $name"
        FAIL=$((FAIL + 1))
    fi
}

# 1. PDF exists
echo "--- Output checks ---"
if [ -f main.pdf ]; then
    check "main.pdf exists" "PASS"
    PDF_SIZE=$(ls -lh main.pdf | awk '{print $5}')
    echo "         Size: $PDF_SIZE"
    if command -v pdfinfo >/dev/null 2>&1; then
        PAGE_COUNT=$(pdfinfo main.pdf 2>/dev/null | grep "^Pages:" | awk '{print $2}')
        echo "         Pages: $PAGE_COUNT"
    fi
else
    check "main.pdf exists" "FAIL"
fi

# 2. LaTeX log checks
echo ""
echo "--- LaTeX log checks ---"
if [ -f main.log ]; then
    UNDEF_REFS=$(grep -c "undefined" main.log 2>/dev/null) || UNDEF_REFS=0
    if [ "$UNDEF_REFS" -gt 0 ]; then
        check "Undefined references ($UNDEF_REFS)" "WARN"
    else
        check "No undefined references" "PASS"
    fi

    WARNINGS=$(grep -c "Warning" main.log 2>/dev/null) || WARNINGS=0
    if [ "$WARNINGS" -gt 0 ]; then
        check "LaTeX warnings ($WARNINGS total)" "WARN"
    else
        check "No LaTeX warnings" "PASS"
    fi

    OVERFULL=$(grep -c "Overfull" main.log 2>/dev/null) || OVERFULL=0
    UNDERFULL=$(grep -c "Underfull" main.log 2>/dev/null) || UNDERFULL=0
    if [ "$OVERFULL" -gt 0 ] || [ "$UNDERFULL" -gt 0 ]; then
        check "Box warnings (overfull: $OVERFULL, underfull: $UNDERFULL)" "WARN"
    else
        check "No box warnings" "PASS"
    fi
else
    check "main.log exists" "FAIL"
fi

# 3. Manifest check
echo ""
echo "--- Manifest check ---"
if [ -f build/manifest.json ]; then
    check "build/manifest.json exists" "PASS"
else
    check "build/manifest.json exists" "WARN"
    echo "         Run 'make manifest' to generate"
fi

# 4. makeglossaries check
echo ""
echo "--- Tool checks ---"
if command -v makeglossaries >/dev/null 2>&1; then
    check "makeglossaries installed" "PASS"
else
    check "makeglossaries installed" "WARN"
    echo "         WARNING: makeglossaries not found"
fi

# 5. veraPDF (Docker only)
if command -v verapdf >/dev/null 2>&1; then
    check "veraPDF available" "PASS"
else
    check "veraPDF available (Docker only)" "WARN"
    echo "         Skipped — only available in Docker builds"
fi

# 6. gitinfo check
echo ""
echo "--- Build metadata ---"
if [ -f build/gitinfo.tex ]; then
    check "build/gitinfo.tex exists" "PASS"
else
    check "build/gitinfo.tex exists" "FAIL"
fi

# Summary
echo ""
echo "=== Summary ==="
echo "  PASS: $PASS"
echo "  WARN: $WARN"
echo "  FAIL: $FAIL"

# JSON output
cat > build/validation.json <<EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "pass": $PASS,
  "warn": $WARN,
  "fail": $FAIL,
  "pdf_exists": $([ -f main.pdf ] && echo true || echo false),
  "pdf_size": "${PDF_SIZE:-N/A}",
  "page_count": ${PAGE_COUNT:-0},
  "undefined_refs": ${UNDEF_REFS:-0},
  "latex_warnings": ${WARNINGS:-0}
}
EOF
echo ""
echo "JSON report written to build/validation.json"

if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
