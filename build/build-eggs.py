#!/usr/bin/env python3
"""Build standalone easter egg pages from manifest (Plan 0246)."""

import yaml
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent
MANIFEST = REPO / 'build' / 'easter-egg-manifest.yaml'
CSS_FILES = [REPO / 'build' / 'epub.css', REPO / 'build' / 'html.css']
READER_JS = REPO / 'build' / 'reader.js'
OUT_DIR = REPO / 'docs' / 'downloads' / 'eggs'


def build():
    with open(MANIFEST) as f:
        manifest = yaml.safe_load(f)

    css = ''
    for css_file in CSS_FILES:
        css += css_file.read_text() + '\n'
    reader_js = READER_JS.read_text()

    count = 0
    for egg in manifest.get('eggs', []):
        slug = egg['slug']
        source = REPO / egg['source']
        title = egg.get('title', slug)

        if not source.exists():
            print(f"  WARNING: source not found for egg '{slug}': {source}")
            continue

        result = subprocess.run(
            ['pandoc', str(source), '-f', 'latex', '-t', 'html5', '--mathml'],
            capture_output=True, text=True, check=True
        )
        content_html = result.stdout

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
        count += 1
        print(f"  Egg: {slug} -> {out_path}")

    print(f"Built {count} easter egg page(s).")


if __name__ == '__main__':
    build()
