#!/bin/bash
# Generate build/manifest.json from git ls-files ONLY (never walks the filesystem).
cd "$(git rev-parse --show-toplevel)" || exit 1
out=build/manifest.json
{
  echo '{'
  echo '  "generated": "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'",'
  echo '  "files": ['
  git ls-files -- manuscript build \
    | grep -E '\.(tex|sty|cls)$' | grep -v '^build/epub[-]tmp/' | LC_ALL=C sort \
    | sed 's/.*/    "&",/' | sed '$ s/,$//'
  echo '  ]'
  echo '}'
} > "$out"
echo "Manifest written to $out"
