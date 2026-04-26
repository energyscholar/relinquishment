#!/usr/bin/env python3
"""Verify every manifest entry resolves to an anchor in the built HTML,
and no HTML anchor is orphan (not in manifest).

Manifest IDs are stored with their namespace prefix after Plan 0209
(dl:X and custodian:X). HTML anchors are id="dl:X" or id="custodian:X".
SVG figures use id="fig-X". Puzzles and eggs are registered but may not
be in the main HTML yet (skipped categories).
"""
import re, sys, yaml
from pathlib import Path

repo = Path(__file__).parent.parent
manifest = yaml.safe_load((repo / 'build/deep-links.yaml').read_text())
html = (repo / 'docs/downloads/Relinquishment.html').read_text()

# Categories not yet placed in main HTML — skip verification, don't error
SKIP_CATEGORIES = {'egg', 'puzzle'}

skip_ids = {e['id'] for e in manifest if e.get('category') in SKIP_CATEGORIES}
manifest_ids = {e['id'] for e in manifest}
check_ids = manifest_ids - skip_ids

missing = [mid for mid in check_ids if f'id="{mid}"' not in html]
if missing:
    print(f'MISSING: {len(missing)} manifest entries have no anchor in HTML:', file=sys.stderr)
    for m in sorted(missing):
        print(f'  {m}', file=sys.stderr)
    sys.exit(1)

html_ids = set(re.findall(r'id="(dl:[^"]+|custodian:[^"]+|fig-[^"]+)"', html))
orphans = html_ids - manifest_ids
if orphans:
    print(f'ORPHANS: {len(orphans)} HTML anchors absent from manifest:', file=sys.stderr)
    for o in sorted(orphans):
        print(f'  {o}', file=sys.stderr)
    sys.exit(1)

checked = len(check_ids)
skipped = len(skip_ids)
print(f'OK: {checked} manifest entries verified, {skipped} skipped (not yet in HTML); no orphans.')

egg_manifest_path = repo / 'build' / 'easter-egg-manifest.yaml'
if egg_manifest_path.exists():
    egg_manifest = yaml.safe_load(egg_manifest_path.read_text())
    for egg in egg_manifest.get('eggs', []):
        slug = egg['slug']
        built = repo / 'docs' / 'downloads' / 'eggs' / slug / 'index.html'
        if not built.exists():
            print(f'  WARNING: egg \'{slug}\' in manifest but not built (run \'make eggs\')')
