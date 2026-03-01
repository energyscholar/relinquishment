#!/usr/bin/env bash
# release.sh — Push-button release for Relinquishment
# Usage: ./scripts/release.sh
#        DRY_RUN=1 ./scripts/release.sh   (print steps without executing)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

DRY_RUN="${DRY_RUN:-0}"
MAILING_LIST="scripts/mailing-list.txt"
MAIN_TEX="main.tex"
DOCS_DIR="docs"
DOWNLOADS_DIR="docs/downloads"
DMS_LINE_ACTIVE='\include{manuscript/appendix/dms-note}'
DMS_LINE_COMMENTED='%\include{manuscript/appendix/dms-note}'

# --- Helpers ---

run() {
    if [[ "$DRY_RUN" == "1" ]]; then
        echo "  [DRY RUN] $*"
    else
        "$@"
    fi
}

step() {
    echo ""
    echo "=== $1 ==="
}

die() {
    echo "ERROR: $1" >&2
    exit 1
}

# --- Preflight checks ---

step "Preflight checks"

# Verify we're in the right repo
[[ -f "$MAIN_TEX" ]] || die "Not in repo root (no main.tex)"
[[ -d "$DOCS_DIR" ]] || die "No docs/ directory"

# Verify DMS line exists and is not already commented out
if ! grep -qF "$DMS_LINE_ACTIVE" "$MAIN_TEX"; then
    if grep -qF "$DMS_LINE_COMMENTED" "$MAIN_TEX"; then
        die "DMS appendix already commented out in main.tex — restore it first"
    else
        die "Cannot find DMS appendix line in main.tex"
    fi
fi

# Check for uncommitted changes
if [[ "$DRY_RUN" != "1" ]] && ! git diff --quiet; then
    die "Uncommitted changes in working tree. Commit or stash first."
fi

echo "All preflight checks passed."

# --- Step 1: Strip DMS appendix ---

step "Step 1: Strip DMS appendix from public build"

if [[ "$DRY_RUN" == "1" ]]; then
    echo "  [DRY RUN] Comment out \\include{manuscript/appendix/dms-note} in main.tex"
else
    sed -i 's|^\\include{manuscript/appendix/dms-note}|%\\include{manuscript/appendix/dms-note}|' "$MAIN_TEX"
fi

echo "DMS appendix commented out."

# --- Step 2: Build all formats ---

step "Step 2: Build PDF, HTML, EPUB"

if [[ "$DRY_RUN" == "1" ]]; then
    echo "  [DRY RUN] make clean && make dev && make html && make epub"
else
    make clean
    make dev
    make html
    make epub
fi

# --- Step 3: Restore DMS appendix ---

step "Step 3: Restore DMS appendix"

if [[ "$DRY_RUN" == "1" ]]; then
    echo "  [DRY RUN] Restore \\include{manuscript/appendix/dms-note} in main.tex"
else
    sed -i 's|^%\\include{manuscript/appendix/dms-note}|\\include{manuscript/appendix/dms-note}|' "$MAIN_TEX"
fi

echo "DMS appendix restored."

# --- Step 4: Generate checksums ---

step "Step 4: Generate SHA-256 checksums"

if [[ "$DRY_RUN" != "1" ]]; then
    sha256sum Relinquishment.pdf Relinquishment.html Relinquishment.epub | tee checksums.sha256
else
    echo "  [DRY RUN] sha256sum Relinquishment.{pdf,html,epub} > checksums.sha256"
fi

# --- Step 5: Copy builds to website ---

step "Step 5: Copy builds to docs/downloads/"

run cp Relinquishment.pdf "$DOWNLOADS_DIR/"
run cp Relinquishment.html "$DOWNLOADS_DIR/"
run cp Relinquishment.epub "$DOWNLOADS_DIR/"
run cp checksums.sha256 "$DOWNLOADS_DIR/"

echo "Builds deployed to $DOWNLOADS_DIR/"

# --- Step 6: Swap Under Construction → Live ---

step "Step 6: Swap to live site"

if [[ -f "$DOCS_DIR/index-live.html" ]]; then
    run cp "$DOCS_DIR/index-live.html" "$DOCS_DIR/index.html"
    echo "Live site activated."
else
    echo "WARNING: No index-live.html found. Site remains in Under Construction mode."
fi

# --- Step 7: Git commit + push ---

step "Step 7: Git commit + push"

if [[ "$DRY_RUN" != "1" ]]; then
    git add docs/ checksums.sha256
    git commit -m "Release: public build deployed to website

Stripped DMS appendix, rebuilt all formats, deployed to docs/.
Site swapped from Under Construction to live."
    git push
    echo "Pushed to remote. GitHub Pages will deploy."
else
    echo "  [DRY RUN] git add docs/ checksums.sha256"
    echo "  [DRY RUN] git commit -m 'Release: public build deployed to website'"
    echo "  [DRY RUN] git push"
fi

# --- Step 8: Create torrent (optional) ---

step "Step 8: Create torrent"

if command -v mktorrent &>/dev/null; then
    if [[ "$DRY_RUN" != "1" ]]; then
        mktorrent -a udp://tracker.opentrackr.org:1337/announce \
                  -a udp://open.stealth.si:80/announce \
                  -c "Relinquishment by Bruce Stephenson, Genevieve Prentice & Argus — CC BY-ND 4.0" \
                  -n Relinquishment \
                  -o Relinquishment.torrent \
                  Relinquishment.pdf Relinquishment.epub Relinquishment.html checksums.sha256
        echo "Torrent created: Relinquishment.torrent"
    else
        echo "  [DRY RUN] mktorrent ... -o Relinquishment.torrent"
    fi
else
    echo "mktorrent not installed — skipping. Install: sudo apt install mktorrent"
fi

# --- Step 9: Print mailing checklist ---

step "Step 9: Mailing checklist"

echo ""
echo "=== MAILING LIST ==="
echo "Send Relinquishment.pdf + cover letter to:"
echo ""

if [[ -f "$MAILING_LIST" ]]; then
    n=0
    while IFS= read -r line; do
        # Skip comments and blank lines
        [[ "$line" =~ ^[[:space:]]*# ]] && continue
        [[ -z "${line// /}" ]] && continue
        n=$((n + 1))
        echo "  $n. $line"
    done < "$MAILING_LIST"
    echo ""
else
    echo "  (No mailing list found at $MAILING_LIST)"
    echo "  Create it with one entry per line: Name <email> — relationship"
    echo ""
fi

echo "Website: https://relinquishment.ai"

if [[ -f Relinquishment.torrent ]]; then
    echo "Torrent: Relinquishment.torrent (seed with transmission-cli)"
fi

echo ""
echo "Checksums in checksums.sha256 — include in cover letter."

# --- Step 10: Seeding reminder ---

step "Step 10: START SEEDING"

if [[ -f Relinquishment.torrent ]]; then
    echo ""
    echo "Run:  transmission-cli Relinquishment.torrent"
    echo "Leave running. The more seeds, the harder to suppress."
else
    echo "No torrent file. Create one after installing mktorrent."
fi

echo ""
echo "=== RELEASE COMPLETE ==="
