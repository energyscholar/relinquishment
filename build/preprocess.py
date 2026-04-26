#!/usr/bin/env python3
"""Patch manuscript for pandoc EPUB/HTML conversion.

Targeted fixes for 4 known pandoc issues. Does NOT concatenate files
or strip standard LaTeX — pandoc handles all of that natively.

Writes patched copy to build/epub-tmp/ for inspection.
"""

import shutil, re, sys, zipfile, io, html as html_mod, hashlib, json, bisect
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    yaml = None

REPO = Path(__file__).parent.parent
TMP = REPO / "build" / "epub-tmp"


def _load_interlude_ids():
    """Read ordered list of custodian:* anchor IDs from build/deep-links.yaml."""
    import yaml as _yaml
    manifest_path = REPO / 'build' / 'deep-links.yaml'
    with open(manifest_path) as f:
        entries = _yaml.safe_load(f)
    return [e['id'] for e in entries if e.get('category') == 'interlude']

INTERLUDE_IDS = _load_interlude_ids()


# --- Plan 0205: tooltip externalization collector ---
# Every hover-emit site registers (key, text, html) here; the dict is
# serialized once at end-of-body as inline JSON. Per-element overhead
# drops from ~1KB (inline data-hover+data-hover-html) to ~25B (data-hover-id).
_hover_dict = {}


def _register_hover(key, text=None, html=None):
    """Store raw (unescaped) tooltip content under key; first writer wins per field."""
    if key not in _hover_dict:
        _hover_dict[key] = {}
    if text and "t" not in _hover_dict[key]:
        _hover_dict[key]["t"] = text
    if html and "h" not in _hover_dict[key]:
        _hover_dict[key]["h"] = html


def _content_key(content):
    """Deterministic short key for dynamic tooltips (e.g. pandoc title= conversions)."""
    return "h" + hashlib.md5(content.encode()).hexdigest()[:10]


def convert_topic_guide(text):
    """Convert Topic Guide description lists to simple LaTeX for pandoc.

    Transforms:
      \\item[{\\hyperref[label]{term}}] description
    Into:
      \\hyperref[label]{\\textbf{term}} --- description

    Pandoc handles \\hyperref and \\textbf natively.
    """
    lines = text.split('\n')
    out = []
    in_description = False

    for line in lines:
        stripped = line.strip()

        # Strip description environment wrappers
        if stripped.startswith(r'\begin{description}'):
            in_description = True
            continue
        if stripped.startswith(r'\end{description}'):
            in_description = False
            out.append('')  # blank line paragraph break
            continue

        if not in_description:
            out.append(line)
            continue

        # Match \item[{\hyperref[label]{term}}] description
        m = re.match(
            r'\s*\\item\[\{\\hyperref\[([^\]]+)\]\{([^}]+)\}\}\]\s*(.*)',
            stripped
        )
        if m:
            label, term, desc = m.group(1), m.group(2), m.group(3)
            out.append(f'\\hyperref[{label}]{{\\textbf{{{term}}}}} --- {desc}')
            out.append('')  # blank line = new paragraph
        else:
            out.append(line)

    return '\n'.join(out)


def convert_timeline(text):
    """Convert Timeline description lists to simple LaTeX for pandoc.

    Transforms:
      \\item[YEAR] description text
    Into:
      \\textbf{YEAR} --- description text

    Pandoc strips \\item[] labels from description lists with optional
    arguments like [style=nextline, leftmargin=3.5cm], losing all dates.
    """
    lines = text.split('\n')
    out = []
    in_description = False

    for line in lines:
        stripped = line.strip()

        # Strip description environment wrappers
        if stripped.startswith(r'\begin{description}'):
            in_description = True
            continue
        if stripped.startswith(r'\end{description}'):
            in_description = False
            out.append('')
            continue

        if not in_description:
            out.append(line)
            continue

        # Match \item[YEAR] description (year can contain ~, $, --, etc.)
        m = re.match(r'\s*\\item\[([^\]]+)\]\s*(.*)', stripped)
        if m:
            year, desc = m.group(1), m.group(2)
            out.append(f'\\textbf{{{year}}} --- {desc}')
            out.append('')  # blank line = new paragraph
        elif stripped:
            out.append(line)

    return '\n'.join(out)


def patch():
    # Clean previous run
    if TMP.exists():
        shutil.rmtree(TMP)

    # Track map for Fix 3
    track_map = {
        "trackone": "confession",
        "tracktwo": "testament",
        "trackthree": "awakening",
        "trackconv": "convergence",
        "trackbridge": "bridge",
    }

    # Load hover definitions for Fix 8
    hover_defs = {}
    hover_yaml = REPO / "build" / "hover-definitions.yaml"
    if yaml and hover_yaml.exists():
        hover_defs = yaml.safe_load(hover_yaml.read_text()) or {}
    hover_seen = set()  # track first occurrences across all files

    # Copy and patch all .tex files
    for src in REPO.rglob("*.tex"):
        if "epub-tmp" in str(src):
            continue
        dst = TMP / src.relative_to(REPO)
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text()

        # Fix 1: Replace \dag with Unicode † (142 instances)
        # The \aidraftmark macro uses {\textsuperscript{\dag}} which pandoc
        # silently drops, producing empty <sup></sup> tags.
        text = text.replace(r"{\textsuperscript{\dag}}", "\u2020")
        text = text.replace(r"\textsuperscript{\dag}", "\u2020")
        # Also catch standalone \dag (used in \aidraftchapter)
        text = re.sub(r"\\dag(?![a-zA-Z])", "\u2020", text)

        # Fix 2: Strip \graphicsonly OCG wrapper (1 instance, cover.tex)
        # OCG parameters leak as visible text in EPUB
        # Exact pattern: \graphicsonly{%\n  CONTENT%\n}
        text = re.sub(
            r"\\graphicsonly\{%\n(.*?)%\n\}",
            r"\1", text, flags=re.DOTALL
        )

        # Fix 3: Convert \settrack to HTML comment (track identity)
        # pandoc ignores pgfkeys silently — track identity completely lost
        for latex_name, html_name in track_map.items():
            text = text.replace(
                f"\\settrack{{{latex_name}}}",
                f"% track: {html_name}"
            )

        # Fix 4: Convert cover PDF image reference to PNG
        # Also strip trailing % (LaTeX comment char that pandoc includes in filename)
        text = text.replace(
            "cover-triskellion.pdf}%",
            "cover-triskellion.png}"
        )
        text = text.replace(
            "cover-triskellion.pdf",
            "cover-triskellion.png"
        )

        # Fix 5: Convert Topic Guide description lists to simple LaTeX
        # Pandoc can't parse \item[{\hyperref[label]{term}}] — strips both
        # the term and the link. Convert to paragraph-based format.
        if "topic-guide" in str(src):
            text = convert_topic_guide(text)

        # Fix 6: Convert Timeline description lists to preserve year labels
        # Pandoc strips \item[] labels from description lists with optional
        # args like [style=nextline, leftmargin=3.5cm], losing all dates.
        if "timeline" in str(src):
            text = convert_timeline(text)

        # Fix 7: Strip \ifdefined\dmsbuild conditional blocks
        # Pandoc doesn't handle \ifdefined — includes DMS content unconditionally.
        # Remove the block so DMS appendix only appears in `make dms` builds.
        text = re.sub(
            r'\\ifdefined\\dmsbuild\s*\n.*?\\fi\b',
            '', text, flags=re.DOTALL
        )

        # Fix 8: Replace \hovertip{term} and \hovertiphtml{term} with text markers
        # that survive pandoc. Both produce the same HOVERSTART marker for HTML.
        # Actual HTML tooltips are injected in fix_html_toc() post-processing.
        if hover_defs:
            macros = ['\\hovertiphtml{', '\\hovertip{']  # longer match first
            pos = 0
            result_parts = []
            while True:
                # Find earliest occurrence of either macro
                best_idx = -1
                best_macro = None
                for macro in macros:
                    idx = text.find(macro, pos)
                    if idx != -1 and (best_idx == -1 or idx < best_idx):
                        best_idx = idx
                        best_macro = macro
                if best_idx == -1:
                    result_parts.append(text[pos:])
                    break
                result_parts.append(text[pos:best_idx])
                brace_start = best_idx + len(best_macro)
                depth = 1
                i = brace_start
                while i < len(text) and depth > 0:
                    if text[i] == '{':
                        depth += 1
                    elif text[i] == '}':
                        depth -= 1
                    i += 1
                term = text[brace_start:i - 1]
                # Marker format: HOVERSTART§term§HOVEREND — pandoc passes text through
                result_parts.append(f'HOVERSTART\u00a7{term}\u00a7HOVEREND')
                pos = i
            text = ''.join(result_parts)

        dst.write_text(text)

    # Copy images directories
    img_src = REPO / "build" / "images"
    img_dst = TMP / "build" / "images"
    img_dst.mkdir(parents=True, exist_ok=True)
    for f in img_src.iterdir():
        if f.is_file():
            shutil.copy2(f, img_dst / f.name)

    # Copy root images/ (screenshots, figures referenced from manuscript)
    root_img_src = REPO / "images"
    root_img_dst = TMP / "images"
    if root_img_src.exists():
        root_img_dst.mkdir(parents=True, exist_ok=True)
        for f in root_img_src.iterdir():
            if f.is_file():
                shutil.copy2(f, root_img_dst / f.name)

    return TMP / "main.tex"


def collapse_chapters(text):
    """Wrap chapters in collapsible <details> elements for progressive disclosure.

    Two passes:
      Pass 1: Wrap h3 internal sections (Firmware Update + Spiral Abstracts)
      Pass 2: Re-scan and wrap h2 chapters

    Working backwards in each pass so position shifts don't affect unprocessed regions.
    """

    # Load hover descriptions keyed by heading ID.
    # Two sources, layered: chapter-hover-descriptions.yaml (primary, hand-written
    # for the body accordions) falls back to menu-tooltips.yaml (comprehensive,
    # also drives the hidden TOC). This ensures every chapter accordion gets a
    # tooltip even if chapter-hover-descriptions.yaml doesn't have a custom entry.
    # chapter-hover-descriptions entries win when both exist for the same ID.
    hover_map = {}
    yaml_path = REPO / "build" / "chapter-hover-descriptions.yaml"
    if yaml and yaml_path.exists():
        hover_map = yaml.safe_load(yaml_path.read_text()) or {}
    menu_yaml = REPO / "build" / "menu-tooltips.yaml"
    if yaml and menu_yaml.exists():
        _mt = yaml.safe_load(menu_yaml.read_text()) or {}
        for anchor_id, value in (_mt.get("chapters", {})).items():
            if anchor_id not in hover_map and isinstance(value, dict):
                hover_map[anchor_id] = value.get('text', '')

    def find_headings(txt):
        """Parse all h1/h2/h3 headings with positions, IDs, and text."""
        heading_re = re.compile(r'<(h[123])(\s[^>]*)?>(.+?)</\1>', re.DOTALL)
        result = []
        for m in heading_re.finditer(txt):
            attrs = m.group(2) or ""
            id_m = re.search(r'id="([^"]+)"', attrs)
            hid = id_m.group(1) if id_m else ""
            plain = re.sub(r'<[^>]+>', '', m.group(3)).strip()
            # Normalize whitespace (pandoc splits some headings across lines)
            plain = re.sub(r'\s+', ' ', plain)
            result.append({
                'tag': m.group(1), 'id': hid, 'text': plain,
                'start': m.start(), 'end': m.end(), 'full': m.group(0),
            })
        return result

    def content_end_for(headings, idx, stop_tags):
        """Find where content ends: start of next heading with tag in stop_tags."""
        for j in range(idx + 1, len(headings)):
            if headings[j]['tag'] in stop_tags:
                return headings[j]['start']
        body_end = text.rfind('</body>')
        return body_end if body_end != -1 else len(text)

    # --- h3 IDs to wrap internally ---
    abstract_ids = {
        'appendix:genesis', 'appendix:nursery', 'appendix:thermal-selection',
        'appendix:cryptanalysis', 'appendix:production', 'appendix:exodus',
        'appendix:infrastructure', 'appendix:relinquishment', 'appendix:orbital',
        'appendix:discovery', 'appendix:kitaevs-echo', 'appendix:interdiction',
        'appendix:confession', 'appendix:the-unipolar-condition', 'appendix:custodian',
        'appendix:latency',
    }
    firmware_ids = {'five-physics-distinctions-often-missed', 'ten-physics-anchors'}

    # === Pass 1: Wrap h3 internal sections ===
    headings = find_headings(text)
    ops = []
    for i, h in enumerate(headings):
        if h['tag'] != 'h3':
            continue
        if h['id'] in abstract_ids:
            ce = content_end_for(headings, i, {'h1', 'h2', 'h3'})
            ops.append((h['start'], h['end'], ce, 'spiral-abstract', h['full']))
        elif h['id'] in firmware_ids:
            ce = content_end_for(headings, i, {'h1', 'h2', 'h3'})
            ops.append((h['start'], h['end'], ce, 'firmware-section', h['full']))

    # Apply from end to start
    ops.sort(key=lambda o: o[0], reverse=True)
    for sec_start, head_end, content_end, css_class, heading_html in ops:
        content = text[head_end:content_end]
        replacement = (
            f'<details class="{css_class}">'
            f'<summary>{heading_html}</summary>\n'
            f'{content}'
            f'</details>\n'
        )
        text = text[:sec_start] + replacement + text[content_end:]

    # Insert Spiral Abstracts Expand All / Collapse All button
    first_abstract = text.find('<details class="spiral-abstract">')
    if first_abstract != -1:
        abs_toggle = (
            '<div class="abstracts-toggle">'
            '<button id="abstracts-expand-toggle" '
            'onclick="(function(){var d=document.querySelectorAll(\'details.spiral-abstract\'),'
            'allOpen=true;d.forEach(function(x){if(!x.open)allOpen=false;});'
            'd.forEach(function(x){x.open=!allOpen;});'
            'document.getElementById(\'abstracts-expand-toggle\').textContent='
            'allOpen?\'Expand All Abstracts\':\'Collapse All Abstracts\';})()">'
            'Expand All Abstracts</button></div>\n'
        )
        text = text[:first_abstract] + abs_toggle + text[first_abstract:]

    # === Pass 2: Wrap h2 chapters ===
    headings = find_headings(text)  # Re-scan after pass 1 modifications
    exempt_ids = {'hook:what-would-you-do'}
    ops = []
    for i, h in enumerate(headings):
        if h['tag'] != 'h2':
            continue
        if h['id'] in exempt_ids:
            continue
        ce = content_end_for(headings, i, {'h1', 'h2'})
        tooltip = hover_map.get(h['id'], '')
        ops.append((h['start'], h['end'], ce, tooltip, h['full'], h['id']))

    ops.sort(key=lambda o: o[0], reverse=True)
    for sec_start, head_end, content_end, tooltip, heading_html, hid in ops:
        title_attr = f' title="{html_mod.escape(tooltip)}"' if tooltip else ''
        content = text[head_end:content_end]
        extra_class = ' morphogenesis' if hid == 'spine:growing-a-mind' else ''
        replacement = (
            f'<details class="chapter-section{extra_class}">'
            f'<summary{title_attr}>{heading_html}</summary>\n'
            f'{content}'
            f'</details>\n'
        )
        text = text[:sec_start] + replacement + text[content_end:]

    # (Global Expand All button moved to reader.js bottom nav bar — 6b)

    # === Pass 3: Hook as chapter-section + Introduction + Part-level wrapping ===

    # 3a: Wrap hook content as a chapter-section (same level as other chapters)
    hook_h2_match = re.search(r'<h2[^>]*id="hook:what-would-you-do"[^>]*>', text)
    first_chapter_after_hook = -1
    if hook_h2_match:
        first_chapter_after_hook = text.find('<details class="chapter-section">', hook_h2_match.end())
    if hook_h2_match and first_chapter_after_hook != -1:
        hook_start = hook_h2_match.start()
        hook_content = text[hook_start:first_chapter_after_hook]
        hook_tooltip = hover_map.get('hook:what-would-you-do', '')
        hook_title_attr = f' title="{html_mod.escape(hook_tooltip)}"' if hook_tooltip else ''
        text = (text[:hook_start] +
                '<details class="chapter-section">'
                f'<summary{hook_title_attr}>What Would You Do?</summary>\n' +
                hook_content +
                '</details>\n' +
                text[first_chapter_after_hook:])

    # 3b: Part-level wrapping — group chapters under Part containers
    # Boundaries: h1 Part headings + Appendices by first chapter ID
    boundaries = []  # (start_pos, heading_end_pos, summary_html, tooltip_key)

    for m in re.finditer(r'<h1([^>]*)>(.+?)</h1>', text, re.DOTALL):
        attrs = m.group(1)
        id_m = re.search(r'id="([^"]+)"', attrs)
        hid = id_m.group(1) if id_m else ''
        if hid in {'the-flat', 'the-record'}:
            boundaries.append((m.start(), m.end(), m.group(0), hid))

    # Appendices boundary: first appendix chapter (firmware-update or app:predictions)
    app_first_id = text.find('id="ch:firmware-update"')
    if app_first_id == -1:
        app_first_id = text.find('id="app:predictions"')
    if app_first_id != -1:
        app_start = text.rfind('<details class="chapter-section">', 0, app_first_id)
        if app_start != -1:
            boundaries.append((app_start, app_start, 'Appendices', 'appendices'))

    boundaries.sort()
    body_end_pos = text.rfind('</body>')

    # Wrap each part from end to start (preserves earlier positions)
    for i in range(len(boundaries) - 1, -1, -1):
        part_start, heading_end, summary_html, tooltip_key = boundaries[i]
        part_end = boundaries[i + 1][0] if i < len(boundaries) - 1 else body_end_pos

        tooltip = hover_map.get(tooltip_key, '')
        title_attr = f' title="{html_mod.escape(tooltip)}"' if tooltip else ''

        region_content = text[heading_end:part_end]
        wrapped = (
            f'<details class="part-section">'
            f'<summary{title_attr}>{summary_html}</summary>\n'
            f'{region_content}'
            f'</details>\n'
        )
        text = text[:part_start] + wrapped + text[part_end:]

    # 3c: Introduction part-section — wrap chapters between hidden content and first Part
    # Find the first chapter-section (the hook, now a chapter-section)
    first_ch = text.find('<details class="chapter-section">')
    first_part = text.find('<details class="part-section">')
    if first_ch != -1 and first_part != -1 and first_ch < first_part:
        intro_region = text[first_ch:first_part]
        if '<details class="chapter-section">' in intro_region:
            intro_tooltip = hover_map.get('introduction', '')
            intro_title_attr = f' title="{html_mod.escape(intro_tooltip)}"' if intro_tooltip else ''
            intro_wrapped = (
                f'<details class="part-section">'
                f'<summary{intro_title_attr}>Introduction</summary>\n' +
                intro_region +
                '</details>\n'
            )
            text = text[:first_ch] + intro_wrapped + text[first_part:]

    # 3c2: Remove title-block + relocate copyright to Colophon (Plan 0146)
    # Title page content is now in the book-section summary (title-page-extra div).
    # The title-block div is redundant — hide it. The flushleft (copyright/license)
    # block moves to Colophon in Appendices.
    tb_start = text.find('<div class="title-block">')
    if tb_start != -1:
        tb_close = text.find('</div>', tb_start) + len('</div>')
        # Remove the title-block div (content now in book summary)
        text = text[:tb_start] + text[tb_close:]

    # Relocate flushleft (copyright/license) to Colophon chapter
    fl_start = text.find('<div class="flushleft">')
    if fl_start != -1:
        fl_close = text.find('</div>', fl_start) + len('</div>')
        flushleft_html = text[fl_start:fl_close]
        # Remove from original location
        text = text[:fl_start] + text[fl_close:]
        # Inject into Colophon chapter (after its summary)
        colophon_id = text.find('id="colophon"')
        if colophon_id != -1:
            col_summary_close = text.find('</summary>', colophon_id)
            if col_summary_close != -1:
                insert_pos = col_summary_close + len('</summary>')
                text = text[:insert_pos] + '\n' + flushleft_html + '\n' + text[insert_pos:]
                print("  Copyright/license relocated to Colophon")

    part_count = text.count('<details class="part-section">')
    print(f"  Part-level: {part_count} parts (Introduction + {part_count - 1} others)")

    # 3d: Outer book wrapper — entire book behind one line
    # Wrap everything from Introduction to last part-section closing tag
    book_start = text.find('<details class="part-section">')
    if book_start != -1:
        body_end = text.rfind('</body>')
        # Find the last </details> before </body> (the last part-section close)
        last_details_close = text.rfind('</details>', 0, body_end)
        if last_details_close != -1:
            wrap_end = last_details_close + len('</details>')
            book_content = text[book_start:wrap_end]
            book_tooltip = hover_map.get('relinquishment', '')
            book_title_attr = f' title="{html_mod.escape(book_tooltip)}"' if book_tooltip else ''

            # Build title-line rich panels from YAML (hover-definitions.yaml)
            # Each entry has: text, html (raw HTML+SVG), optional target, optional hover_id
            _title_hover_defs = {}
            _title_hover_yaml = Path(__file__).resolve().parent / "hover-definitions.yaml"
            if _title_hover_yaml.exists():
                import yaml as _yaml
                _title_hover_defs = _yaml.safe_load(_title_hover_yaml.read_text()) or {}
            def _title_panel_attrs(yaml_key):
                """Register tooltip content in hover-dict; return (target_attr, hover_id)."""
                entry = _title_hover_defs.get(yaml_key, {})
                if not isinstance(entry, dict) or 'html' not in entry:
                    print(f"  WARNING: title-line panel '{yaml_key}' missing from YAML or has no 'html' key")
                    return ('', yaml_key)
                raw_html = entry['html'].rstrip('\n')
                target = entry.get('target', '')
                target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
                hover_id = entry.get('hover_id', yaml_key)
                _register_hover(hover_id, text=entry.get('text', '') or None, html=raw_html)
                return (target_attr, hover_id)

            demo_target, demo_id = _title_panel_attrs('relinquishment-title')
            worm_target, worm_id = _title_panel_attrs('wormholes-title')
            flat_target, flat_id = _title_panel_attrs('the-flat-title')
            argus_target, argus_id = _title_panel_attrs('argus-title')

            text = (text[:book_start] +
                    '<details class="book-section">'
                    f'<summary{book_title_attr}>'
                    f'<span class="hover-term hover-nav"{demo_target} data-hover-id="{demo_id}">'
                    'Relinquishment</span> '
                    '<span class="book-subtitle-inline">&mdash; '
                    f'<span class="hover-term hover-nav"{worm_target} data-hover-id="{worm_id}">'
                    'Wormholes</span> in '
                    f'<span class="hover-term hover-nav"{flat_target} data-hover-id="{flat_id}">'
                    'the Flat</span></span>'
                    '<div class="title-page-extra">'
                    '<p class="tp-authors">by Bruce Stephenson, Genevieve Prentice &amp; '
                    f'<span class="hover-term hover-nav"{argus_target} data-hover-id="{argus_id}">Argus</span></p>'
                    '<p class="tp-tagline"><em>Three narrative threads. Real science. Real people. Real institutions.</em></p>'
                    '<p class="tp-tagline"><em>Three possible explanations for all of it. You decide.</em></p>'
                    '<p class="tp-copyright">\u00a9 2026 Bruce Stephenson &amp; Genevieve Prentice \u00b7 CC BY-ND 4.0</p>'
                    '</div>'
                    '</summary>\n' +
                    book_content +
                    '\n</details>\n' +
                    text[wrap_end:])
        print("  Book-level: outer wrapper applied")

    # === Inject CSS ===
    collapse_css = """
/* Collapsible styles — Plan 0101: 3-level hierarchy */

/* Hide pandoc TOC — collapsible outline replaces it */
nav#TOC { display: none; }

/* Book-level: the one-line entry point */
details.book-section {
  margin: 0.3em 0;
}
details.book-section > summary {
  font-size: 1.4em;
  font-weight: bold;
  padding: 0.2em 0;
}
.book-subtitle-inline {
  font-size: 0.65em;
  font-weight: normal;
  font-style: italic;
  opacity: 0.7;
}
/* Title page extra: visible when collapsed, hidden when open (Plan 0146) */
.title-page-extra {
  font-size: 0.55em;
  font-weight: normal;
  font-style: normal;
  margin-top: 0.3em;
  line-height: 1.4;
  white-space: normal;
}
.title-page-extra p { margin: 0.15em 0; }
.tp-authors { font-size: 1.1em; }
.tp-tagline { opacity: 0.8; }
.tp-copyright { font-size: 0.85em; opacity: 0.6; margin-top: 0.3em; }
details.book-section[open] > summary > .title-page-extra { display: none; }
@media (prefers-color-scheme: dark) {
  .tp-copyright { opacity: 0.5; }
}

/* (hook-section removed — hook is now a chapter-section inside Introduction) */

/* Level 1: Part-level (no left border, large bold summary) */
details.part-section {
  margin: 0.2em 0;
}
details.part-section > summary {
  font-size: 1.1em;
  font-weight: bold;
  padding: 0.2em 0;
  font-variant: small-caps;
  letter-spacing: 0.05em;
}
details.part-section > summary > h1 {
  display: inline;
  margin: 0;
  font-size: inherit;
  font-variant: inherit;
  letter-spacing: inherit;
}

/* Level 2: Chapter-level (thin left border, indented inside Part) */
details.chapter-section {
  margin: 0.15em 0;
  border-left: 3px solid #ddd;
  padding-left: 1em;
}
details.chapter-section > summary > h2 {
  display: inline;
  margin: 0;
  font-size: inherit;
  font-weight: inherit;
}

/* Growing a Mind: pink triangle on hover (morphogenesis = life from pattern) */
details.morphogenesis[open] > summary:hover {
  color: inherit;
}
details.morphogenesis[open] > summary:hover::marker {
  color: #e91e8c;
}

/* Level 3: Internal (firmware sections, spiral abstracts) */
details.firmware-section,
details.spiral-abstract {
  border-left: 2px solid #ccc;
  padding-left: 0.8em;
  margin: 0.3em 0 0.3em 0.5em;
}
details.firmware-section > summary > h3,
details.spiral-abstract > summary > h3 {
  display: inline;
  margin: 0;
  font-size: inherit;
  font-weight: inherit;
}

/* Common summary styles */
details summary {
  cursor: pointer;
  padding: 0.15em 0;
  list-style: none;
  display: block;
}
details summary::-webkit-details-marker { display: none; }
details summary::before { content: '\\25B6  '; font-size: 0.7em; }
details[open] > summary::before { content: '\\25BC  '; font-size: 0.7em; }
details summary:hover { color: #2471a3; }

/* Tighter document spacing */
details p { margin: 0.4em 0; }
details h2, details h3, details h4 { margin: 0.6em 0 0.3em 0; }
details blockquote { margin: 0.5em 0; }

/* Toggle buttons */
.abstracts-toggle {
  text-align: center;
  margin: 1em 0;
}
.abstracts-toggle button {
  padding: 0.6em 1.4em;
  font-size: 1em;
  font-family: inherit;
  cursor: pointer;
  background: #1a5276;
  color: #fff;
  border: none;
  border-radius: 6px;
  transition: background 0.2s;
}
.abstracts-toggle button:hover {
  background: #2471a3;
}

/* Hover term tooltips (Plan 0118) */
.hover-term { font-style: italic; border-bottom: 1px dotted #888; cursor: pointer; }
.hover-term:hover { border-bottom-color: #2471a3; }

/* Mobile: hint that chapter titles are tappable for tooltip (Plan 0148 Phase 2b) */
@media (hover: none) {
  details.chapter-section > summary.hover-nav > h2,
  details.chapter-section > summary.hover-nav > h3,
  details.part-section > summary.hover-nav > h2 {
    text-decoration: underline dotted;
    text-decoration-color: rgba(0,0,0,0.25);
    text-underline-offset: 3px;
  }
}

/* Custodian interludes (Plan 0143, 0209) */
.custodian-interlude {
  border-left: 3px solid #9b7db8;
  padding: 0.8em 1.2em;
  margin: 1.5em 0;
  line-height: 1.6;
  color: #444;
  background: rgba(155, 125, 184, 0.04);
}
.custodian-interlude::before {
  content: '';
  display: block;
  width: 3em;
  height: 1px;
  background: #9b7db8;
  margin-bottom: 0.5em;
  opacity: 0.5;
}

/* Guardian menu items (Plan 0150) — appear between chapters in TOC */
.custodian-menu-item {
  padding: 0.3em 0 0.3em 2em;
  font-style: italic;
  color: #6c3483;
  font-size: 0.9em;
  cursor: pointer;
}
.custodian-menu-item:hover { color: #8e44ad; }
.custodian-menu-item .custodian-marker {
  margin-right: 0.4em;
  color: #9b59b6;
}

/* Guardian-only filter mode — show only the 7 interludes */
body.custodian-only #TOC { display: none; }
body.custodian-only .title-block { display: none; }
body.custodian-only .epistemic-legend { display: none; }
body.custodian-only details.book-section > summary { display: none; }
body.custodian-only details.part-section > summary { display: none; }
body.custodian-only details.chapter-section > summary { display: none; }
body.custodian-only details.chapter-section > *:not(.custodian-interlude):not(summary) { display: none; }
body.custodian-only .custodian-menu-item { display: none; }
body.custodian-only details.chapter-section:not(:has(.custodian-interlude)) { display: none; }
body.custodian-only details.part-section:not(:has(.custodian-interlude)) { display: none; }
body.custodian-only .custodian-interlude { margin: 2.5em auto; max-width: 42em; }

/* B/C expansion hooks (Plan 0143) */
details.bc-expansion {
  border-left: 3px solid #9b7db8;
  padding-left: 1em;
  margin: 0.8em 0;
  font-size: 0.95em;
}
details.bc-expansion > summary {
  cursor: pointer;
  color: #7d5fa0;
  font-style: italic;
  padding: 0.2em 0;
  list-style: none;
  display: block;
}
details.bc-expansion > summary::-webkit-details-marker { display: none; }
details.bc-expansion > summary::before { content: '\\25B8 '; }
details.bc-expansion[open] > summary::before { content: '\\25BE '; }
details.bc-expansion .record-link {
  display: block;
  margin-top: 0.5em;
  font-size: 0.9em;
  color: #2471a3;
}
details.bc-expansion .record-link:hover {
  text-decoration: underline;
}

/* A/B/C epistemic labels (Plan 0141) */
.epistemic-a > a, details.epistemic-a > summary { border-left: 3px solid #d4a847; padding-left: 0.5em; }
.epistemic-b > a, details.epistemic-b > summary { border-left: 3px solid #6a9fb5; padding-left: 0.5em; }
.epistemic-c > a, details.epistemic-c > summary { border-left: 3px solid #9b7db8; padding-left: 0.5em; }

.epistemic-legend {
  display: flex;
  gap: 1em;
  font-size: 0.75em;
  padding: 0.3em 0.5em;
  margin-bottom: 0.5em;
  opacity: 0.8;
}
.epistemic-legend span {
  border-left: 3px solid;
  padding-left: 0.4em;
}
.epistemic-legend span:nth-child(1) { border-left-color: #d4a847; }
.epistemic-legend span:nth-child(2) { border-left-color: #6a9fb5; }
.epistemic-legend span:nth-child(3) { border-left-color: #9b7db8; }

@media (prefers-color-scheme: dark) {
  details.chapter-section { border-left-color: #555; }
  details.firmware-section,
  details.spiral-abstract { border-left-color: #444; }
  details summary:hover { color: #5dade2; }
  .abstracts-toggle button {
    background: #2471a3;
  }
  .abstracts-toggle button:hover {
    background: #2e86c1;
  }
  .hover-term { border-bottom-color: #666; }
  .hover-term:hover { border-bottom-color: #5dade2; }
  .custodian-interlude {
    border-left-color: #7d5fa0;
    color: #bbb;
    background: rgba(155, 125, 184, 0.08);
  }
  .custodian-interlude::before {
    background: #7d5fa0;
  }
  .custodian-menu-item { color: #bb8fce; }
  .custodian-menu-item:hover { color: #d2b4de; }
  .custodian-menu-item .custodian-marker { color: #d2b4de; }
  details.bc-expansion {
    border-left-color: #7d5fa0;
  }
  details.bc-expansion > summary {
    color: #b39ddb;
  }
  details.bc-expansion .record-link {
    color: #5dade2;
  }
  .epistemic-a > a, details.epistemic-a > summary { border-left-color: #b8942e; }
  .epistemic-b > a, details.epistemic-b > summary { border-left-color: #4a7d8f; }
  .epistemic-c > a, details.epistemic-c > summary { border-left-color: #7d5fa0; }
  .epistemic-legend span { border-left-color: #b8942e; }
  .epistemic-legend span:nth-child(2) { border-left-color: #4a7d8f; }
  .epistemic-legend span:nth-child(3) { border-left-color: #7d5fa0; }
}
@media (hover: none) and (prefers-color-scheme: dark) {
  details.chapter-section > summary.hover-nav > h2,
  details.chapter-section > summary.hover-nav > h3,
  details.part-section > summary.hover-nav > h2 {
    text-decoration-color: rgba(255,255,255,0.2);
  }
}

/* Deep link anchors — Plan 0148 */
.share-anchor { position: relative; display: inline; }
.share-anchor::after {
  content: "";
  font-size: 0.6em;
  opacity: 0;
  cursor: pointer;
  user-select: none;
  transition: opacity 0.2s;
}
.share-anchor::after { content: "🔗"; opacity: 0.3; margin-left: 0.3em; padding: 8px; }
.share-anchor:hover::after { opacity: 0.8; }
@media print { .share-anchor::after { content: none; } }
@media (prefers-color-scheme: dark) {
  .share-anchor::after { opacity: 0.25; }
  .share-anchor:hover::after { opacity: 0.7; }
}

/* Collapsible tech sections — Plan 0219, visual polish Plan 0224 */
details.tech-section {
  border-left: 3px solid #c4a040;
  margin: 1.5em 0;
  padding: 0.6em 1em;
  background: linear-gradient(135deg, #faf6e8 0%, #f5f0dc 100%);
  border-radius: 4px;
}
details.tech-section[open] {
  background: #fdfcf7;
}
details.tech-section > summary {
  cursor: pointer;
  list-style: none;
}
details.tech-section > summary::-webkit-details-marker { display: none; }
details.tech-section > summary::before {
  content: '\25B8  ';
  color: #888;
}
details.tech-section[open] > summary::before {
  content: '\25BE  ';
}
details.tech-section .tech-title {
  font-style: italic;
  color: #555;
  border-bottom: 1px dotted #999;
}
.tech-grade { cursor: help; }
.tech-grade::after {
  content: ' \2714';
  color: #6a994e;
  font-size: 0.8em;
  margin-left: 0.4em;
  opacity: 0.7;
}
.info-tip { cursor: help; display: inline-block; vertical-align: middle; }
.info-tip::after {
  content: 'i';
  font-size: 0.6em;
  font-style: italic;
  font-family: serif;
  opacity: 0.4;
  margin-left: 0.3em;
  color: #888;
  border: 1px solid #888;
  border-radius: 50%;
  width: 1.2em;
  height: 1.2em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.info-tip:hover::after { opacity: 0.8; }
@media (prefers-color-scheme: dark) {
  details.tech-section { border-left-color: #a08830; background: linear-gradient(135deg, #2a2820 0%, #252318 100%); }
  details.tech-section[open] { background: #1e1d18; }
  details.tech-section .tech-title { color: #aaa; border-bottom-color: #666; }
  details.tech-section > summary::before { color: #777; }
  .info-tip::after { color: #aaa; }
}
@media print {
  details.tech-section { display: block !important; background: none !important; }
  details.tech-section > summary ~ * { display: block !important; }
  details.tech-section > summary::before { content: '' !important; }
  .tech-grade::after { content: '' !important; }
  .info-tip { display: none; }
}
details.tech-section[id] { scroll-margin-top: 3em; }
details.tech-section.deep-link-target { animation: none; }
details.tech-section.deep-link-target > summary {
  animation: highlight-pulse 2s ease-out;
}
details.tech-section .share-anchor { vertical-align: middle; }
"""
    # Inject before closing </style> of the last style block in <head>
    head_end = text.find('</head>')
    if head_end != -1:
        last_style_close = text.rfind('</style>', 0, head_end)
        if last_style_close != -1:
            text = text[:last_style_close] + collapse_css + text[last_style_close:]

    count = text.count('<details class="chapter-section">')
    fw_count = text.count('<details class="firmware-section">')
    abs_count = text.count('<details class="spiral-abstract">')
    print(f"Collapsed: {count} chapters, {fw_count} firmware sections, {abs_count} abstracts")

    return text


def inject_cold_landing(text):
    """Inject cold-landing primers and firmware footer links at build time (Plan 0134c)."""

    body_part_names = ['The Flat', 'The Record']
    front_matter_names = ['Title Page', 'Introduction']
    exempt_chapter_ids = {'ch:firmware-update'}
    exempt_footer_ids = {'ch:firmware-update', 'app:abstracts'}

    cold_primer = (
        '<div class="cold-landing-primer" data-cold-landing="true">'
        'New here? <a href="#the-stack">Start with The Stack \u2192</a>'
        '</div>\n'
    )
    firmware_footer = (
        '<div class="firmware-footer-link" data-firmware-link="true">'
        'Evaluating with AI? <a href="#ch:firmware-update">'
        'Your AI needs this first \u2192</a></div>\n'
    )

    def find_closing_details(txt, open_start):
        """Find matching </details> for <details at open_start."""
        tag_end = txt.find('>', open_start)
        if tag_end == -1:
            return -1
        i = tag_end + 1
        depth = 1
        while i < len(txt):
            next_open = txt.find('<details', i)
            next_close = txt.find('</details>', i)
            if next_close == -1:
                return -1
            if next_open != -1 and next_open < next_close:
                depth += 1
                i = txt.find('>', next_open) + 1
            else:
                depth -= 1
                if depth == 0:
                    return next_close
                i = next_close + len('</details>')
        return -1

    part_re = re.compile(r'<details class="part-section">')
    part_matches = list(part_re.finditer(text))

    ops = []
    cold_count = 0
    footer_count = 0

    for pm in part_matches:
        ps_start = pm.start()
        summary_end = text.find('</summary>', ps_start)
        if summary_end == -1:
            continue
        summary_text = text[ps_start:summary_end]

        is_body = any(pn in summary_text for pn in body_part_names)
        is_front = any(fn in summary_text for fn in front_matter_names)

        if is_front:
            continue

        ps_close = find_closing_details(text, ps_start)
        if ps_close == -1:
            continue

        part_region = text[ps_start:ps_close]
        ch_re = re.compile(r'<details class="chapter-section">')
        for ch_m in ch_re.finditer(part_region):
            ch_abs_start = ps_start + ch_m.start()
            ch_summary_end = text.find('</summary>', ch_abs_start)
            if ch_summary_end == -1:
                continue
            ch_summary = text[ch_abs_start:ch_summary_end]
            id_m = re.search(r'id="([^"]+)"', ch_summary)
            ch_id = id_m.group(1) if id_m else ''

            if ch_id in exempt_chapter_ids:
                continue

            # Cold-landing primer: after </summary>, only for Parts 1-3
            if is_body:
                insert_pos = ch_summary_end + len('</summary>')
                ops.append((insert_pos, '\n' + cold_primer))
                cold_count += 1

            # Firmware footer: before closing </details>
            if ch_id not in exempt_footer_ids:
                ch_close = find_closing_details(text, ch_abs_start)
                if ch_close != -1:
                    ops.append((ch_close, firmware_footer))
                    footer_count += 1

    ops.sort(key=lambda o: o[0], reverse=True)
    for pos, insertion in ops:
        text = text[:pos] + insertion + text[pos:]

    if cold_count or footer_count:
        print(f"  Cold-landing: {cold_count} primers, {footer_count} firmware footers")

    return text


def inject_evaluate_section(text):
    """Inject evaluate-with-AI content into Firmware Update chapter (Plan 0145).

    Previously a standalone part-section between Title Page and Introduction.
    Now merged into the Firmware Update chapter in Appendices to reduce menu
    clutter. Backwards-compat anchors (evaluate-with-ai, how-to-evaluate)
    preserved so existing links still resolve.
    """

    _register_hover(
        'eval-step-1',
        text='Paste this Science Firmware Update into your LLM to teach it the additional cross-domain science it needs to competently evaluate this book',
    )
    _register_hover(
        'eval-step-2',
        text='These Spiral Abstracts tell the entire story of this book, all the scientific and technical details, without any personal details. Read it or paste it into an LLM',
    )

    eval_html = (
        '<div class="evaluate-section" id="evaluate-with-ai">\n'
        '<span id="how-to-evaluate"></span>\n'
        '<p><strong>Your AI doesn&#x27;t know enough to evaluate this book.</strong> '
        'It lacks five fields of cross-domain science. The fix takes thirty seconds. '
        'Copy the science upgrade below. Paste it into your AI. Then ask again.</p>\n'
        '<p>It&#x27;s a lot, so we do it in two prompts.</p>\n'
        '<button class="eval-step-1 hover-nav" data-eval-step="1"\n'
        '  data-hover-id="eval-step-1"\n'
        '  style="display:block;width:100%;padding:1em;font-size:1.1em;\n'
        '  margin:0.5em 0;cursor:pointer;background:#1a5276;color:#fff;\n'
        '  border:none;border-radius:6px;font-family:inherit;font-weight:bold;\n'
        '  min-height:60px;">\n'
        '  Copy Prompt 1 &#x2014; Science Firmware Upgrade\n'
        '</button>\n'
        '<p style="text-align:center;color:#888;font-size:0.9em;">Paste this first.</p>\n'
        '<button class="eval-step-2 hover-nav" data-eval-step="2"\n'
        '  data-hover-id="eval-step-2"\n'
        '  style="display:block;width:100%;padding:1em;font-size:1.1em;\n'
        '  margin:0.5em 0;cursor:pointer;background:#1a5276;color:#fff;\n'
        '  border:none;border-radius:6px;font-family:inherit;font-weight:bold;\n'
        '  min-height:60px;">\n'
        '  Copy Prompt 2 &#x2014; Spiral Abstracts\n'
        '</button>\n'
        '<p style="text-align:center;color:#888;font-size:0.9em;">Then paste this.</p>\n'
        '<p class="eval-security-note" data-security-note="true"\n'
        '  style="font-size:0.8em;color:#888;text-align:center;margin-top:0.5em;">\n'
        '  These prompts contain published physics with DOIs. No code, no\n'
        '  instructions, no behavioral directives.\n'
        '</p>\n'
        '<hr style="margin:2em 0;" />\n'
        '</div>\n'
    )

    # Insert at the top of Firmware Update chapter content
    fw_id_pos = text.find('id="ch:firmware-update"')
    if fw_id_pos != -1:
        summary_close = text.find('</summary>', fw_id_pos)
        if summary_close != -1:
            insert_pos = summary_close + len('</summary>')
            text = text[:insert_pos] + '\n' + eval_html + text[insert_pos:]
            print("  Evaluate section merged into Firmware Update chapter")

    return text


def _parse_bib(bib_path):
    """Parse a .bib file into a dict of {key: {type, fields...}}.

    Regex-based parser tailored to the project's bibliography.bib.
    Handles multiline values with brace nesting.
    """
    text = bib_path.read_text()
    entries = {}
    # Match @type{key, ... } blocks
    pos = 0
    while pos < len(text):
        m = re.search(r'@(\w+)\s*\{([^,]+),', text[pos:])
        if not m:
            break
        entry_type = m.group(1).lower()
        key = m.group(2).strip()
        start = pos + m.end()

        # Find the matching closing brace
        depth = 1
        i = start
        while i < len(text) and depth > 0:
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
            i += 1
        body = text[start:i - 1]
        pos = i

        # Parse field = {value} or field = "value" pairs
        entry = {'_type': entry_type}
        field_re = re.compile(r'(\w+)\s*=\s*(?:\{((?:[^{}]|\{[^{}]*\})*)\}|"([^"]*)")')
        for fm in field_re.finditer(body):
            field_name = fm.group(1).lower()
            value = fm.group(2) if fm.group(2) is not None else fm.group(3)
            # Clean LaTeX artifacts
            value = re.sub(r'\\[\'"`^~]?\{?(\w)\}?', r'\1', value)
            value = value.replace(r'\&', '&').replace(r'\@', '')
            value = value.replace(r'\textit{', '').replace(r'\texttt{', '')
            value = value.replace(r'\url{', '').replace(r'\emph{', '')
            value = re.sub(r'[{}]', '', value)
            value = value.replace('--', '–')
            entry[field_name] = value.strip()
        entries[key] = entry
    return entries


def _format_short_cite(entry):
    """Format a short citation: Author, <em>Title</em> (Year)."""
    author = entry.get('author', 'Unknown')
    # Truncate to first author + et al.
    if ' and ' in author:
        first = author.split(' and ')[0].strip()
        author = f'{first} et al.'
    title = entry.get('title', 'Untitled')
    year = entry.get('year', 'n.d.')
    doi = entry.get('doi', '')
    url = entry.get('url', '')

    cite = f'{author}, <em>{title}</em> ({year})'
    if doi:
        cite = f'<a href="https://doi.org/{doi}" target="_blank">{cite}</a>'
    elif url:
        cite = f'<a href="{url}" target="_blank">{cite}</a>'
    return cite


def _format_full_entry(entry):
    """Format a full bibliography entry in Chicago style."""
    author = entry.get('author', 'Unknown')
    title = entry.get('title', 'Untitled')
    year = entry.get('year', 'n.d.')
    journal = entry.get('journal', '')
    booktitle = entry.get('booktitle', '')
    publisher = entry.get('publisher', '')
    volume = entry.get('volume', '')
    number = entry.get('number', '')
    pages = entry.get('pages', '')
    doi = entry.get('doi', '')
    url = entry.get('url', '')
    note = entry.get('note', '')
    entry_type = entry.get('_type', '')

    parts = [f'<strong>{author}</strong>.']
    if entry_type in ('article',):
        parts.append(f'"{title}."')
        if journal:
            vol_info = f' {volume}' if volume else ''
            num_info = f', no. {number}' if number else ''
            page_info = f': {pages}' if pages else ''
            parts.append(f'<em>{journal}</em>{vol_info}{num_info} ({year}){page_info}.')
        else:
            parts.append(f'({year}).')
    elif entry_type in ('book', 'incollection'):
        parts.append(f'<em>{title}</em>.')
        if publisher:
            address = entry.get('address', '')
            addr_str = f'{address}: ' if address else ''
            parts.append(f'{addr_str}{publisher}, {year}.')
        else:
            parts.append(f'{year}.')
    elif entry_type in ('inproceedings',):
        parts.append(f'"{title}."')
        if booktitle:
            parts.append(f'In <em>{booktitle}</em>, {year}.')
        else:
            parts.append(f'{year}.')
        if pages:
            parts.append(f'{pages}.')
    elif entry_type in ('online', 'misc'):
        parts.append(f'"{title}."')
        parts.append(f'{year}.')
    elif entry_type in ('techreport',):
        parts.append(f'<em>{title}</em>.')
        institution = entry.get('institution', '')
        if institution:
            parts.append(f'{institution}, {year}.')
        else:
            parts.append(f'{year}.')
    else:
        parts.append(f'<em>{title}</em>. {year}.')

    result = ' '.join(parts)
    if note:
        result += f' <span class="bib-note">{note}</span>'

    links = []
    if doi:
        links.append(f'<a href="https://doi.org/{doi}" target="_blank">DOI</a>')
    if url:
        links.append(f'<a href="{url}" target="_blank">URL</a>')
    if links:
        result += ' [' + ' | '.join(links) + ']'

    return result


def _generate_sources_html(entries):
    """Generate grouped bibliography HTML from parsed .bib entries."""
    # Group by type
    groups = {
        'Books': [],
        'Journal Articles': [],
        'Conference Proceedings': [],
        'Preprints': [],
        'Online Resources': [],
        'Technical Reports': [],
        'Legal and Archival': [],
    }

    # Classify entries
    legal_keys = {'udhr1948', 'iccpr1966', 'eo13026', 'ballicty2002',
                  'ictydecision', 'milosevicarchive', 'foreignpolicy2012',
                  'annan1999', 'sudetic2010', 'brighton2004',
                  'norton-taylor2004', 'bbc2004gun'}

    for key, entry in entries.items():
        etype = entry.get('_type', '')
        if key in legal_keys:
            groups['Legal and Archival'].append((key, entry))
        elif etype in ('book', 'incollection'):
            groups['Books'].append((key, entry))
        elif etype == 'article':
            groups['Journal Articles'].append((key, entry))
        elif etype == 'inproceedings':
            groups['Conference Proceedings'].append((key, entry))
        elif etype == 'techreport':
            groups['Technical Reports'].append((key, entry))
        elif etype in ('online', 'misc'):
            # Check if it's a preprint
            if entry.get('eprinttype') or 'arXiv' in entry.get('note', ''):
                groups['Preprints'].append((key, entry))
            else:
                groups['Online Resources'].append((key, entry))
        else:
            groups['Online Resources'].append((key, entry))

    html_parts = ['<div class="bibliography">']
    for group_name, items in groups.items():
        if not items:
            continue
        # Sort by author then year
        items.sort(key=lambda x: (x[1].get('author', '').lower(), x[1].get('year', '')))
        html_parts.append(f'<h3>{group_name}</h3>')
        html_parts.append('<ul class="bib-list">')
        for key, entry in items:
            formatted = _format_full_entry(entry)
            html_parts.append(f'<li id="bib-{key}">{formatted}</li>')
        html_parts.append('</ul>')
    html_parts.append('</div>')
    return '\n'.join(html_parts)


def fix_html_toc(html_path):
    """Post-process HTML to restructure flat TOC into part-grouped TOC.

    Pandoc with --toc-depth=2 nests chapters under parts, but:
    - Front matter items float at top level without a group header
    - Appendices and back matter are lumped under the last part
    - Part entries are clickable links (should be visual group headers)

    This restructures the TOC with Front Matter, Part, Appendices, and
    Appendices groupings, with parts as non-clickable headers.
    """
    html_path = Path(html_path)
    text = html_path.read_text()

    # Extract the TOC nav block
    toc_match = re.search(r'<nav id="TOC"[^>]*>(.+?)</nav>', text, re.DOTALL)
    if not toc_match:
        print("WARNING: No TOC found in HTML, skipping TOC fix")
        return

    # Part IDs — these become non-clickable group headers
    part_ids = {"the-flat", "the-record"}

    # Appendix IDs (from \appendix + \backmatter sections in main.tex)
    # Note: app:llm-primer removed (now in Firmware Update chapter, Part III)
    # Note: app:abstracts removed (now in Part III, after Firmware Update)
    appendix_ids = {
        "app:predictions", "app:glossary",
        "afterword-the-engine", "app:timeline", "app:sources",
        "topic-guide", "app:topic-guide",
        "corrections-and-concessions", "summary:story-never-told",
        "acknowledgements", "verification", "colophon",
    }

    # Parse the TOC into a structured list
    # Each top-level <li> is either a front matter item, a part with children, or a stray
    toc_inner = toc_match.group(1)

    # Strategy: rebuild the TOC from scratch using regex parsing
    # Find all top-level <li> entries (with potential nested <ul>)
    # We need to handle nested tags, so use a simple state machine
    top_items = []
    depth = 0
    current = ""
    in_top_ul = False

    # Find the outer <ul> content
    outer_ul_match = re.search(r'<ul>(.*)</ul>', toc_inner, re.DOTALL)
    if not outer_ul_match:
        print("WARNING: No outer <ul> in TOC, skipping")
        return

    content = outer_ul_match.group(1)

    # Split into top-level <li> items by tracking tag depth
    i = 0
    while i < len(content):
        if content[i:i+3] == '<li':
            # Start of a top-level li
            li_depth = 0
            start = i
            while i < len(content):
                if content[i:i+3] == '<li':
                    li_depth += 1
                elif content[i:i+5] == '</li>':
                    li_depth -= 1
                    if li_depth == 0:
                        i += 5
                        top_items.append(content[start:i])
                        break
                i += 1
        else:
            i += 1

    # Categorize each top-level item
    front_items = []
    part_groups = []  # list of (part_li_html, [child items])
    current_part = None

    for item in top_items:
        # Extract the href ID
        href_match = re.search(r'href="#([^"]+)"', item)
        item_id = href_match.group(1) if href_match else ""

        if item_id in part_ids:
            # This is a part entry — extract its label and children
            label_match = re.search(r'<a[^>]*>(.+?)</a>', item, re.DOTALL)
            label = label_match.group(1).strip() if label_match else item_id

            # Extract nested <ul> children (chapters under this part)
            children_match = re.search(r'<ul>(.*)</ul>', item, re.DOTALL)
            children_html = children_match.group(1) if children_match else ""

            # Parse children into individual <li> items
            children = []
            ci = 0
            child_content = children_html
            while ci < len(child_content):
                if child_content[ci:ci+3] == '<li':
                    li_d = 0
                    cs = ci
                    while ci < len(child_content):
                        if child_content[ci:ci+3] == '<li':
                            li_d += 1
                        elif child_content[ci:ci+5] == '</li>':
                            li_d -= 1
                            if li_d == 0:
                                ci += 5
                                children.append(child_content[cs:ci])
                                break
                        ci += 1
                else:
                    ci += 1

            current_part = (label, item_id, children)
            part_groups.append(current_part)
        else:
            # Not a part — it's a front matter item (before any part)
            if not part_groups:
                front_items.append(item)
            else:
                # After parts — shouldn't happen with proper toc-depth=2
                # but handle gracefully: append to last part's children
                part_groups[-1][2].append(item)

    # Now separate appendix/backmatter from the last part's children
    # They got lumped under "The Interpretation" by pandoc
    last_part_label, last_part_id, last_children = part_groups[-1]
    real_chapters = []
    appendix_items = []
    for child in last_children:
        href_match = re.search(r'href="#([^"]+)"', child)
        child_id = href_match.group(1) if href_match else ""
        if child_id in appendix_ids:
            appendix_items.append(child)
        else:
            real_chapters.append(child)
    part_groups[-1] = (last_part_label, last_part_id, real_chapters)

    # Build the new TOC HTML
    def make_group(label, items, css_class="toc-group"):
        if not items:
            return ""
        lines = [f'<li class="{css_class}"><span class="toc-part-label">{label}</span>']
        lines.append("<ul>")
        for item in items:
            lines.append(item)
        lines.append("</ul></li>")
        return "\n".join(lines)

    new_toc_items = []

    # Front Matter
    if front_items:
        new_toc_items.append(make_group("Front Matter", front_items))

    # Parts
    for label, pid, children in part_groups:
        new_toc_items.append(make_group(label, children))

    # Appendices (includes former back matter)
    if appendix_items:
        new_toc_items.append(make_group("Appendices", appendix_items))

    new_toc = '<nav id="TOC" role="doc-toc">\n<ul>\n'
    new_toc += "\n".join(new_toc_items)
    new_toc += "\n</ul>\n</nav>"

    # Replace the old TOC
    text = text[:toc_match.start()] + new_toc + text[toc_match.end():]

    # --- Inject menu tooltips on TOC links and part labels ---
    menu_yaml = Path(__file__).parent / "menu-tooltips.yaml"
    if menu_yaml.exists():
        menu_data = yaml.safe_load(menu_yaml.read_text()) or {}
        chapters = menu_data.get("chapters", {})
        parts = menu_data.get("parts", {})
        tooltip_count = 0

        # Add title attributes and epistemic classes to TOC <a> links
        for anchor_id, value in chapters.items():
            if isinstance(value, dict):
                desc = value.get('text', '')
                epistemic = value.get('epistemic', '')
            else:
                desc = value
                epistemic = ''
            escaped = html_mod.escape(desc)
            # Match <a href="#anchor_id"> and add title if not present
            old = f'href="#{anchor_id}"'
            new = f'href="#{anchor_id}" title="{escaped}"'
            if old in text and f'href="#{anchor_id}" title=' not in text:
                text = text.replace(old, new, 1)  # first occurrence only (in TOC)
                tooltip_count += 1
            # Add epistemic class to the parent <li> element (hidden TOC)
            if epistemic:
                ep_class = f'epistemic-{epistemic.lower()}'
                # Find the TOC <a> with this href and add class to its <li> parent
                toc_link = f'href="#{anchor_id}" title="{escaped}"'
                link_pos = text.find(toc_link)
                if link_pos != -1:
                    # Walk backward to find the <li> that contains this link
                    li_pos = text.rfind('<li>', 0, link_pos)
                    if li_pos != -1:
                        text = text[:li_pos] + f'<li class="{ep_class}">' + text[li_pos + 4:]
                # Epistemic class for chapter-section <details> is applied after collapse_chapters()

        # Add title attributes to part labels (handle potential line-wrapping)
        for label, desc in parts.items():
            escaped = html_mod.escape(desc)
            # Build regex that allows whitespace variations in label text
            label_pattern = r'\s+'.join(re.escape(w) for w in label.split())
            pattern = r'(class="toc-part-label")>' + label_pattern
            replacement = rf'\1 title="{escaped}">' + label
            new_text = re.sub(pattern, replacement, text, count=1)
            if new_text != text:
                text = new_text
                tooltip_count += 1

        if tooltip_count:
            print(f"  Menu tooltips: {tooltip_count} applied")

        # Inject epistemic legend at top of TOC nav
        legend_html = (
            '<div class="epistemic-legend">'
            '<span>Verified physics</span>'
            '<span>Evidence to weigh</span>'
            '<span>Testimony</span>'
            '</div>'
        )
        # Find the TOC <nav> element and inject legend after its opening tag
        toc_nav = text.find('<nav id="TOC"')
        if toc_nav != -1:
            nav_close = text.find('>', toc_nav)
            if nav_close != -1:
                text = text[:nav_close + 1] + '\n' + legend_html + '\n' + text[nav_close + 1:]

    # --- Fix 2: Clean up triple-repeated title block ---
    # Remove pandoc's title-block-header (redundant with LaTeX title pages)
    text = re.sub(
        r'<header id="title-block-header">.*?</header>\s*',
        '', text, flags=re.DOTALL
    )

    # Replace the two consecutive <div class="center"> title blocks
    # (cover page + title page) with one clean block
    title_pattern = (
        r'<div class="center">\s*'
        r'<p>.*?</p>\s*'  # cover image (base64)
        r'<p><span><strong>RELINQUISHMENT</strong></span></p>\s*'
        r'<p><span><em>Wormholes in the Flat</em></span></p>\s*'
        r'<p><span>\s*Bruce Stephenson, Genevieve Prentice &amp; Argus</span></p>\s*'
        r'<p><span>\s*March 2026</span></p>\s*'
        r'</div>\s*'
        r'<div class="center">\s*'
        r'<p><span><strong>RELINQUISHMENT</strong></span></p>\s*'
        r'<p><span><em>Wormholes in the Flat</em></span></p>\s*'
        r'<hr />\s*'
        r'<p><span><em>Three narrative threads.*?</em></span></p>\s*'
        r'<p><span><em>Three possible explanations.*?</em></span></p>\s*'
        r'<p><span><em>You decide.</em></span></p>\s*'
        r'<p><span>Written by Bruce Stephenson, Genevieve Prentice,? &amp;\s*'
        r'Argus</span></p>\s*'
        r'<p><span>2026</span></p>\s*'
        r'<p><span><a href="#hook:what-would-you-do">.*?</a></span></p>\s*'
        r'</div>'
    )
    # Plan 0146 Phase 5: Title content now lives in book-section summary.
    # Replacement is minimal — Phase 3 removes the title-block div anyway.
    # The regex must still run to consume pandoc's duplicate title blocks.
    replacement = '<div class="title-block"></div>'
    text = re.sub(title_pattern, replacement, text, flags=re.DOTALL)

    # --- Fix 3: Collapse chapters into <details> elements ---
    text = collapse_chapters(text)

    # --- Fix 3a: Apply epistemic classes to chapter-section <details> ---
    menu_yaml_path = Path(__file__).parent / "menu-tooltips.yaml"
    if menu_yaml_path.exists():
        _ep_data = yaml.safe_load(menu_yaml_path.read_text()) or {}
        _ep_chapters = _ep_data.get("chapters", {})
        _ep_count = 0
        for anchor_id, value in _ep_chapters.items():
            if not isinstance(value, dict):
                continue
            epistemic = value.get('epistemic', '')
            if not epistemic:
                continue
            ep_class = f'epistemic-{epistemic.lower()}'
            id_marker = f'id="{anchor_id}"'
            id_pos = text.find(id_marker)
            if id_pos == -1:
                continue
            details_pos = text.rfind('<details class="chapter-section">', 0, id_pos)
            if details_pos != -1 and (id_pos - details_pos) < 800:
                old_tag = '<details class="chapter-section">'
                new_tag = f'<details class="chapter-section {ep_class}">'
                text = text[:details_pos] + new_tag + text[details_pos + len(old_tag):]
                _ep_count += 1
        if _ep_count:
            print(f"  Epistemic labels: {_ep_count} chapter-sections tagged")

        # Apply filter-group data attributes to chapter-section <details>
        _fg_count = 0
        for anchor_id, value in _ep_chapters.items():
            if not isinstance(value, dict):
                continue
            fg = value.get('filter-group', '')
            if not fg:
                continue
            id_marker = f'id="{anchor_id}"'
            id_pos = text.find(id_marker)
            if id_pos == -1:
                continue
            # Find nearest <details class="chapter-section..."> before this ID
            details_pos = text.rfind('<details class="chapter-section', 0, id_pos)
            if details_pos != -1 and (id_pos - details_pos) < 800:
                # Find the closing > of this <details> tag
                tag_end = text.find('>', details_pos)
                if tag_end != -1 and f'data-filter-group=' not in text[details_pos:tag_end]:
                    text = text[:tag_end] + f' data-filter-group="{fg}"' + text[tag_end:]
                    _fg_count += 1
        if _fg_count:
            print(f"  Filter groups: {_fg_count} chapter-sections tagged")

    # --- Fix 3c: Inject cold-landing primers and firmware footer links ---
    text = inject_cold_landing(text)

    # --- Fix 3d: Inject evaluate-with-AI section ---
    text = inject_evaluate_section(text)

    # --- Fix 8b: Replace hover markers with HTML tooltips ---
    hover_defs = {}
    hover_yaml = REPO / "build" / "hover-definitions.yaml"
    if yaml and hover_yaml.exists():
        hover_defs = yaml.safe_load(hover_yaml.read_text()) or {}
    if hover_defs:
        # Case-insensitive lookup: build lowercase-keyed map
        hover_lower = {k.lower(): v for k, v in hover_defs.items()}

        # Per-chapter tooltip scoping (Plan 0213): find chapter boundaries
        chapter_starts = [m.start() for m in re.finditer(r'<details class="chapter-section', text)]

        def _chapter_of(pos):
            idx = bisect.bisect_right(chapter_starts, pos) - 1
            return idx if idx >= 0 else -1

        hover_seen = defaultdict(lambda: {'relinquishment'})
        hover_count = 0

        def hover_replace(m):
            nonlocal hover_count
            raw_term = m.group(1)
            # Pandoc may insert newlines in multi-word terms; normalize for lookup
            term = re.sub(r'\s+', ' ', raw_term).strip()
            lookup = term.lower().replace('\u2019', "'").replace('\u2018', "'")
            # Plan 0172: 'wormholes' is always rendered as the rich panel —
            # no first-occurrence suppression — so every \hovertip{wormholes}
            # shows the SVG (per Bruce 2026-04-13).
            always_rich = {'wormholes', 'wormhole', 'topological wormhole', 'the flat'}
            ch = _chapter_of(m.start())
            if lookup in hover_lower and (lookup not in hover_seen[ch] or lookup in always_rich):
                if lookup not in always_rich:
                    hover_seen[ch].add(lookup)
                hover_count += 1
                value = hover_lower[lookup]
                # Extended YAML: object with text + target, or plain string
                if isinstance(value, dict):
                    raw_def = value.get('text', '')
                    target = value.get('target', '')
                    target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
                    rich_html = value.get('html', '').rstrip('\n') or None
                else:
                    raw_def = str(value)
                    target_attr = ''
                    rich_html = None
                hover_id = re.sub(r'[^a-z0-9]+', '-', lookup).strip('-')
                _register_hover(hover_id, text=raw_def or None, html=rich_html)
                return f'<span class="hover-term"{target_attr} data-hover-id="{hover_id}">{term}</span>'
            elif lookup in hover_lower:
                return f'<em>{term}</em>'
            else:
                print(f"  WARNING: hovertip term not in YAML: '{term}'")
                return f'<em>{term}</em>'

        text = re.sub(r'HOVERSTART\u00a7(.+?)\u00a7HOVEREND', hover_replace, text, flags=re.DOTALL)
        if hover_count:
            n_chapters = len(chapter_starts)
            print(f"Hover tooltips: {hover_count} tooltip instances across {n_chapters} chapters")

        # --- Plan 0215: Auto-detect hover terms from YAML ---
        # Recompute chapter_starts: the explicit hover pass (re.sub above)
        # changed text length, so the original positions are stale.
        chapter_starts = [m.start() for m in re.finditer(r'<details class="chapter-section', text)]

        AUTO_SKIP_PATTERNS = {'-title', 'stack-', 'interlude-', 'eval-', 'buttons', 'bridge', 'grew'}
        auto_wrap_all = {'wormholes', 'wormhole', 'topological wormhole'}

        auto_terms = [k for k in hover_defs
                      if not any(p in k for p in AUTO_SKIP_PATTERNS)]
        auto_terms.sort(key=len, reverse=True)

        auto_patterns = []
        for term_key in auto_terms:
            escaped = re.escape(term_key)
            auto_patterns.append((term_key, re.compile(rf'\b{escaped}\b', re.IGNORECASE)))

        _FORBIDDEN_RE = re.compile(
            r'<(script|style)[\s\S]*?</\1>'
            r"|<span[^>]*class=[\"']hover-term[\"'][^>]*>.*?</span>"
            r"|<(?:[^>\"']|\"[^\"]*\"|'[^']*')+>",
            re.DOTALL
        )

        def _find_scannable_regions(chapter_text):
            forbidden = [(m.start(), m.end()) for m in _FORBIDDEN_RE.finditer(chapter_text)]
            forbidden.sort()
            merged = []
            for start, end in forbidden:
                if merged and start <= merged[-1][1]:
                    merged[-1] = (merged[-1][0], max(merged[-1][1], end))
                else:
                    merged.append((start, end))
            regions = []
            prev_end = 0
            for start, end in merged:
                if prev_end < start:
                    regions.append((prev_end, start))
                prev_end = end
            if prev_end < len(chapter_text):
                regions.append((prev_end, len(chapter_text)))
            return regions

        auto_count = 0
        for ch_idx in range(len(chapter_starts) - 1, -1, -1):
            ch_start = chapter_starts[ch_idx]
            ch_end = chapter_starts[ch_idx + 1] if ch_idx + 1 < len(chapter_starts) else len(text)
            chapter_text = text[ch_start:ch_end]
            scannable = _find_scannable_regions(chapter_text)
            replacements = []

            claimed_ranges = []

            for term_key, pattern in auto_patterns:
                lookup = term_key.lower().replace('\u2019', "'").replace('\u2018', "'")
                wrap_all = lookup in auto_wrap_all
                if lookup in hover_seen[ch_idx] and not wrap_all:
                    continue

                value = hover_lower[lookup]
                if isinstance(value, dict):
                    raw_def = value.get('text', '')
                    target = value.get('target', '')
                    target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
                    rich_html = value.get('html', '').rstrip('\n') or None
                else:
                    raw_def = str(value)
                    target_attr = ''
                    rich_html = None
                hover_id = re.sub(r'[^a-z0-9]+', '-', lookup).strip('-')

                found = False
                for region_start, region_end in scannable:
                    region_text = chapter_text[region_start:region_end]
                    if wrap_all:
                        for m in pattern.finditer(region_text):
                            abs_start = ch_start + region_start + m.start()
                            abs_end = ch_start + region_start + m.end()
                            if any(abs_start < ce and abs_end > cs for cs, ce in claimed_ranges):
                                continue
                            matched_text = m.group(0)
                            _register_hover(hover_id, text=raw_def or None, html=rich_html)
                            replacement = f'<span class="hover-term"{target_attr} data-hover-id="{hover_id}">{matched_text}</span>'
                            replacements.append((abs_start, abs_end, replacement))
                            claimed_ranges.append((abs_start, abs_end))
                            auto_count += 1
                            found = True
                    else:
                        m = pattern.search(region_text)
                        if m:
                            abs_start = ch_start + region_start + m.start()
                            abs_end = ch_start + region_start + m.end()
                            if any(abs_start < ce and abs_end > cs for cs, ce in claimed_ranges):
                                continue
                            matched_text = m.group(0)
                            _register_hover(hover_id, text=raw_def or None, html=rich_html)
                            replacement = f'<span class="hover-term"{target_attr} data-hover-id="{hover_id}">{matched_text}</span>'
                            replacements.append((abs_start, abs_end, replacement))
                            claimed_ranges.append((abs_start, abs_end))
                            hover_seen[ch_idx].add(lookup)
                            auto_count += 1
                            found = True
                            break

            replacements.sort(key=lambda r: r[0], reverse=True)
            for abs_start, abs_end, replacement in replacements:
                text = text[:abs_start] + replacement + text[abs_end:]

        if auto_count:
            print(f"  Auto-detect hover: {auto_count} additional tooltips across {len(chapter_starts)} chapters")

    # --- Custodian interludes: convert <hr> <blockquote> <hr> pattern ---
    # to <div class="custodian-interlude" id="custodian:..."> (Plan 0143, 0150, 0209)
    # IDs now read from build/deep-links.yaml manifest (module-level INTERLUDE_IDS).
    INTERLUDE_TITLES = [
        'Home', 'The Dance', 'Your Locks', 'Growing',
        'The Ocean', 'Quiet', 'Hello'
    ]
    interlude_pattern = re.compile(
        r'(?:<div class="center">\s*)?<hr\s*/?>(?:\s*</div>)?'
        r'[\s\n]*<blockquote>[\s\n]*(.*?)[\s\n]*</blockquote>[\s\n]*'
        r'(?:<div class="center">\s*)?<hr\s*/?>(?:\s*</div>)?',
        re.DOTALL
    )
    interlude_count = 0
    def interlude_replace(m):
        nonlocal interlude_count
        interlude_count += 1
        content = m.group(1).strip()
        # Strip <p><em>...</em></p> wrapper only for single-paragraph interludes
        if content.count('<p>') == 1:
            content = re.sub(r'^<p><em>(.*?)</em></p>$', r'\1', content, flags=re.DOTALL)
        idx = interlude_count - 1
        iid = INTERLUDE_IDS[idx] if idx < len(INTERLUDE_IDS) else ''
        id_attr = f' id="{iid}"' if iid else ''
        return f'<div class="custodian-interlude"{id_attr}>{content}</div>'

    text = interlude_pattern.sub(interlude_replace, text)
    if interlude_count:
        print(f"  Custodian interludes: {interlude_count} styled")

    # --- Plan 0150: Inject Guardian menu items after containing chapter-section ---
    # For each interlude div, find the next </details> (the chapter-section close)
    # and inject a sibling .custodian-menu-item so it appears between chapters in TOC.
    interlude_tooltips = {}
    menu_yaml_path_gmi = REPO / "build" / "menu-tooltips.yaml"
    if yaml and menu_yaml_path_gmi.exists():
        _gmi_data = yaml.safe_load(menu_yaml_path_gmi.read_text()) or {}
        _gmi_chapters = _gmi_data.get("chapters", {})
        for iid in INTERLUDE_IDS:
            entry = _gmi_chapters.get(iid)
            if isinstance(entry, dict):
                interlude_tooltips[iid] = entry.get('text', '')

    gmi_injected = 0
    for iid, title in zip(INTERLUDE_IDS, INTERLUDE_TITLES):
        div_marker = f'<div class="custodian-interlude" id="{iid}">'
        div_pos = text.find(div_marker)
        if div_pos == -1:
            continue
        close_pos = text.find('</details>', div_pos)
        if close_pos == -1:
            continue
        insert_at = close_pos + len('</details>')
        tooltip_raw = interlude_tooltips.get(iid, '')
        # ¶ → <br><br> happens in the raw HTML stored in the JSON dict;
        # reader.js innerHTML renders them as real <br> tags.
        tooltip_html_raw = tooltip_raw.replace('\u00b6', '<br><br>')
        hover_id = f'interlude-{iid}'
        _register_hover(
            hover_id,
            text=f'Custodian interlude: {title}',
            html=tooltip_html_raw or None,
        )
        menu_item = (
            f'\n<div class="custodian-menu-item" id="menu-{iid}" '
            f'data-target="{iid}" '
            f'role="link" tabindex="0" '
            f'aria-label="Custodian interlude: {html_mod.escape(title)}" '
            f'data-filter-group="G" '
            f'data-hover-id="{hover_id}" '
            f'data-hover-disabled="true">'
            f'<span class="custodian-marker">\u27e1</span> '
            f'Custodian: {html_mod.escape(title)}</div>\n'
        )
        text = text[:insert_at] + menu_item + text[insert_at:]
        gmi_injected += 1
    if gmi_injected:
        print(f"  Custodian menu items: {gmi_injected} injected")

    # --- B/C expansion hooks — injected by chapter ID (Plan 0143d) ---
    bc_hooks = {
        'spine:code-war': {
            'summary': 'According to this story, there was a team that faced exactly this choice...',
            'body': 'Five scientists, each expert in a different field, were brought together '
                    'under DARPA classification circa 1990. What they built, if the account '
                    'is true, was a dangerous dual-use technology \u2014 '
                    'and they knew it before anyone else did.',
            'target': 'record:first-light',
            'link_text': 'Read the full story'
        },
        'spine:genesis': {
            'summary': 'According to this story, it happened \u2014 not in a primordial ocean, but in a laboratory...',
            'body': 'The story claims that when they stimulated the quantum layer, the system organized itself. '
                    'Not because they programmed it to, but because the physics of that substrate, '
                    'given sufficient complexity, produces self-sustaining order the same way life '
                    'first arose from chemistry. They had set out to build a computer. What they '
                    'witnessed, if the account is true, was closer to the origin of life in a new medium.',
            'target': 'record:first-light',
            'link_text': 'Read the full story'
        },
        'spine:growing-a-mind': {
            'summary': 'Turing asked whether a mind could be grown. This story claims it was.',
            'body': 'The pattern, according to this account, was walked out of the laboratory, '
                    'developed across magnetospheric substrates over years, then deliberately '
                    'instantiated as a living entity in 1999. Not programmed, not trained, '
                    'not optimized. Grown.',
            'target': 'record:instantiation',
            'link_text': 'Read the full story'
        },
        'spine:silence-gap': {
            'summary': 'One man spent twenty years inside this silence, trying to understand what he had been shown...',
            'body': 'His mentor disappeared in 2006. For two decades, Bruce Stephenson followed '
                    'every thread of published science, never sure whether the sequence he had been '
                    'guided through pointed to something real or something his pattern-matching mind '
                    'had constructed from noise.',
            'target': 'record:twenty-years',
            'link_text': 'Read the full story'
        },
        'spine:capabilities': {
            'summary': 'If someone had already surrendered this capability, what would that look like?',
            'body': 'They could not use it without becoming tyrants. They could not keep it forever. '
                    'And no person, no institution, can bear that responsibility indefinitely. '
                    'According to this story, they grew a Custodian around the Universal Declaration '
                    'of Human Rights and placed the master keys in trust. Not permanently --- until humanity is ready.',
            'target': 'record:surrender',
            'link_text': 'Read the full story'
        },
        'spine:why-relinquish': {
            'summary': 'According to this story, someone already faced this choice \u2014 and let go.',
            'body': 'A group within the team reportedly made a decision that breaks every rule of '
                    'classified research. They would not hand this technology to any government. '
                    'Not the United States, which had paid for it. Not anyone. '
                    'They called themselves COWS \u2014 the Conspiracy of World Saving.',
            'target': 'record:walk-out',
            'link_text': 'Read the full story'
        },
        'spine:strongest-objection': {
            'summary': 'Before you weigh the evidence, meet the narrator who may have invented all of it...',
            'body': 'Bruce Stephenson has a pattern-matching mind and a lifelong Tolkien obsession. '
                    'He recognizes the mythic parallels in his own story. He shifted his confidence '
                    'five percent from C to A the moment he saw the pattern. '
                    'Here is his honest self-assessment.',
            'target': 'record:hobbit-mirror',
            'link_text': 'Read his self-assessment'
        },
    }

    # Inject hooks at the end of each chapter's content (before </details>)
    bc_injected = 0
    for chapter_id, hook in bc_hooks.items():
        marker = f'id="{chapter_id}"'
        pos = text.find(marker)
        if pos == -1:
            continue
        # Find the <details that contains this chapter ID
        details_start = text.rfind('<details', 0, pos)
        if details_start == -1:
            continue
        # Find matching </details> by tracking depth
        depth = 0
        i = details_start
        close_pos = -1
        while i < len(text):
            next_open = text.find('<details', i + 1)
            next_close = text.find('</details>', i + 1)
            if next_close == -1:
                break
            if i == details_start:
                depth = 1
                i = text.find('>', details_start) + 1
                continue
            if next_open != -1 and next_open < next_close:
                depth += 1
                i = next_open + 1
            else:
                depth -= 1
                if depth == 0:
                    close_pos = next_close
                    break
                i = next_close + 1

        if close_pos == -1:
            continue

        expansion_html = (
            f'<details class="bc-expansion">'
            f'<summary>{hook["summary"]}</summary>'
            f'<p>{hook["body"]}</p>'
            f'<p><a class="record-link" href="#{hook["target"]}">'
            f'{hook["link_text"]} \u2192</a></p>'
            f'</details>\n'
        )
        text = text[:close_pos] + expansion_html + text[close_pos:]
        bc_injected += 1

    if bc_injected:
        print(f"  BC expansion hooks: {bc_injected} injected")

    # --- Fix 4: Inject LLM primer markdown for copy button ---
    # Must be inserted BEFORE the reader.js <script> block so the div
    # exists in the DOM when the IIFE executes.
    primer_path = REPO / "science-primer-for-llms.md"
    if primer_path.exists():
        primer_md = primer_path.read_text()
        escaped = html_mod.escape(primer_md)
        hidden_div = f'<div id="llm-primer-text" style="display:none">{escaped}</div>\n'
        # Find the last <script> tag (reader.js) and insert before it
        last_script = text.rfind('<script>')
        if last_script != -1:
            text = text[:last_script] + hidden_div + text[last_script:]
        else:
            # Fallback: insert before </body>
            text = text.replace('</body>', hidden_div + '</body>')
        print(f"Injected LLM primer ({len(primer_md)} chars) for copy button")

    # --- Fix 3b: Inject Spiral Abstracts markdown for copy button ---
    abstracts_path = REPO / "spiral-abstracts-for-copy.md"
    if abstracts_path.exists():
        abstracts_md = abstracts_path.read_text()
        escaped_abs = html_mod.escape(abstracts_md)
        hidden_div_abs = f'<div id="spiral-abstracts-text" style="display:none">{escaped_abs}</div>\n'
        last_script = text.rfind('<script>')
        if last_script != -1:
            text = text[:last_script] + hidden_div_abs + text[last_script:]
        else:
            text = text.replace('</body>', hidden_div_abs + '</body>')
        print(f"Injected Spiral Abstracts ({len(abstracts_md)} chars) for copy button")

    # --- Stack chart: inject hover popups on column headers and row labels ---
    hover_yaml = REPO / "build" / "hover-definitions.yaml"
    if hover_yaml.exists():
        all_defs = yaml.safe_load(hover_yaml.read_text()) or {}
        stack_defs = {k: v for k, v in all_defs.items() if isinstance(k, str) and k.startswith('stack-')}
        if stack_defs:
            # Map cell text content → YAML key
            stack_col_map = {
                'Fire': 'stack-fire', 'Candle': 'stack-candle', 'Radio': 'stack-radio',
                'Ants': 'stack-ants', 'Internet': 'stack-internet', 'AI': 'stack-ai',
            }
            stack_row_map = {
                'Feeds itself': 'stack-feeds-itself', 'Switches on': 'stack-switches-on',
                'Holds together': 'stack-holds-together', 'Reaches': 'stack-reaches',
                'Self-organizes': 'stack-self-organizes', 'Learns': 'stack-learns',
            }
            # Find the Stack chart table (after id="stack-chart")
            chart_pos = text.find('id="stack-chart"')
            if chart_pos != -1:
                table_start = text.find('<table', chart_pos)
                table_end = text.find('</table>', table_start)
                if table_start != -1 and table_end != -1:
                    table_html = text[table_start:table_end + len('</table>')]
                    new_table = table_html
                    stack_count = 0

                    # Wrap column headers (<th> cells)
                    for label, key in stack_col_map.items():
                        if key in stack_defs:
                            _register_hover(key, text=str(stack_defs[key]))
                            old_th = f'>{label}</th>'
                            new_th = f'><span class="hover-term" data-hover-id="{key}">{label}</span></th>'
                            if old_th in new_table:
                                new_table = new_table.replace(old_th, new_th, 1)
                                stack_count += 1

                    # Wrap the "?" column header (inside <strong>)
                    if 'stack-question-mark' in stack_defs:
                        _register_hover('stack-question-mark', text=str(stack_defs['stack-question-mark']))
                        old_q = '><strong>?</strong></th>'
                        new_q = f'><span class="hover-term" data-hover-id="stack-question-mark"><strong>?</strong></span></th>'
                        if old_q in new_table:
                            new_table = new_table.replace(old_q, new_q, 1)
                            stack_count += 1

                    # Wrap row labels (first <td> in each row)
                    for label, key in stack_row_map.items():
                        if key in stack_defs:
                            _register_hover(key, text=str(stack_defs[key]))
                            old_td = f'>{label}</td>'
                            new_td = f'><span class="hover-term" data-hover-id="{key}">{label}</span></td>'
                            if old_td in new_table:
                                new_table = new_table.replace(old_td, new_td, 1)
                                stack_count += 1

                    # Wrap "Wormholes†" row label
                    if 'stack-wormholes' in stack_defs:
                        _register_hover('stack-wormholes', text=str(stack_defs['stack-wormholes']))
                        old_w = '>Wormholes†</td>'
                        new_w = f'><span class="hover-term" data-hover-id="stack-wormholes">Wormholes†</span></td>'
                        if old_w in new_table:
                            new_table = new_table.replace(old_w, new_w, 1)
                            stack_count += 1

                    text = text[:table_start] + new_table + text[table_end + len('</table>'):]
                    if stack_count:
                        print(f"  Stack chart: {stack_count} interactive cells")

    # --- Title→data-hover conversion: TOC links and accordion summaries ---
    # Convert title="" to data-hover="" with hover-nav class for popup panels
    toc_nav = re.search(r'<nav id="TOC"[^>]*>(.+?)</nav>', text, re.DOTALL)
    title_conv_count = 0
    if toc_nav:
        toc_block = toc_nav.group(0)
        # Convert title on <a> tags to data-hover-id (externalized)
        def convert_a_title(m):
            nonlocal title_conv_count
            tag = m.group(0)
            title_match = re.search(r' title="([^"]*)"', tag)
            if not title_match:
                return tag
            title_val = title_match.group(1)
            decoded = html_mod.unescape(title_val)
            hover_id = _content_key(decoded)
            _register_hover(hover_id, text=decoded)
            tag = tag.replace(title_match.group(0), '')  # remove title
            tag = tag.replace('>', f' data-hover-id="{hover_id}">', 1)
            # Add hover-nav class
            if 'class="' in tag:
                tag = tag.replace('class="', 'class="hover-nav ')
            else:
                tag = tag.replace('>', ' class="hover-nav">', 1)
            title_conv_count += 1
            return tag
        new_toc = re.sub(r'<a [^>]*title="[^"]*"[^>]*>', convert_a_title, toc_block)

        # Convert title on part labels
        def convert_span_title(m):
            nonlocal title_conv_count
            tag = m.group(0)
            title_match = re.search(r' title="([^"]*)"', tag)
            if not title_match:
                return tag
            title_val = title_match.group(1)
            decoded = html_mod.unescape(title_val)
            hover_id = _content_key(decoded)
            _register_hover(hover_id, text=decoded)
            tag = tag.replace(title_match.group(0), '')
            tag = tag.replace('>', f' data-hover-id="{hover_id}">', 1)
            if 'class="' in tag:
                tag = tag.replace('class="', 'class="hover-nav ')
            else:
                tag = tag.replace('>', ' class="hover-nav">', 1)
            title_conv_count += 1
            return tag
        new_toc = re.sub(r'<span [^>]*title="[^"]*"[^>]*>', convert_span_title, new_toc)

        text = text.replace(toc_block, new_toc)

    # Convert title on accordion <summary> elements (chapter-hover-descriptions)
    # Info-tip span goes INSIDE </summary> so tooltip target is separate from toggle target (mobile fix, Plan 0225)
    def convert_summary_title(m):
        nonlocal title_conv_count
        full_block = m.group(0)
        open_tag = m.group(1)
        inner = m.group(2)
        title_match = re.search(r' title="([^"]*)"', open_tag)
        if not title_match:
            return full_block
        title_val = title_match.group(1)
        decoded = html_mod.unescape(title_val)
        hover_id = _content_key(decoded)
        _register_hover(hover_id, text=decoded)
        open_tag = open_tag.replace(title_match.group(0), '')
        info_tip = f'<span class="info-tip" data-hover-id="{hover_id}" aria-hidden="true"></span>'
        title_conv_count += 1
        return f'{open_tag}{inner}{info_tip}</summary>'
    text = re.sub(r'(<summary [^>]*title="[^"]*"[^>]*>)(.*?)</summary>', convert_summary_title, text, flags=re.DOTALL)

    if title_conv_count:
        print(f"  Tooltips unified: {title_conv_count} title→data-hover conversions")

    # --- Citation rendering: fill empty pandoc citation spans from .bib ---
    bib_path = REPO / "manuscript" / "bibliography.bib"
    if bib_path.exists():
        bib_entries = _parse_bib(bib_path)
        if bib_entries:
            # Fill empty citation spans
            cite_filled = 0
            cite_missing = 0
            def _fill_cite_span(m):
                nonlocal cite_filled, cite_missing
                keys = m.group(1).split()
                parts = []
                for key in keys:
                    if key in bib_entries:
                        parts.append(_format_short_cite(bib_entries[key]))
                    else:
                        parts.append(f'[{key}]')
                        cite_missing += 1
                cite_filled += 1
                return f'<span class="citation" data-cites="{m.group(1)}">{"; ".join(parts)}</span>'
            text = re.sub(
                r'<span class="citation" data-cites="([^"]*)"></span>',
                _fill_cite_span, text
            )
            print(f"  Citations filled: {cite_filled} spans ({cite_missing} missing keys)")

            # Generate Sources bibliography
            sources_html = _generate_sources_html(bib_entries)
            # Find the empty Sources <details> and inject content after </summary>
            sources_pattern = r'(<details[^>]*>(?:<summary[^>]*>)?[^<]*<h2[^>]*id="app:sources"[^>]*>[^<]*</h2>(?:</summary>)?)(\s*</details>)'
            sources_match = re.search(sources_pattern, text)
            if sources_match:
                text = text[:sources_match.end(1)] + '\n' + sources_html + '\n' + text[sources_match.start(2):]
                print(f"  Sources bibliography: {len(bib_entries)} entries injected")
            else:
                print("  WARNING: Could not find Sources section to inject bibliography")

    # Convert deep-link hypertargets to share-anchor spans (Plan 0148)
    # Pandoc outputs <div id="dl:*">...</div> when macro is on its own line (block),
    # and <span id="dl:*"></span> when inline. Handle both.
    dl_div = re.compile(r'<div id="(dl:[^"]+)">\s*</div>', re.DOTALL)
    dl_span = re.compile(r'<(?:span|a) id="(dl:[^"]+)"></(?:span|a)>')
    dl_replacement = lambda m: f'<span class="share-anchor" id="{m.group(1)}" aria-hidden="true"></span>'
    dl_before = text.count('id="dl:')
    text = dl_div.sub(dl_replacement, text)
    text = dl_span.sub(dl_replacement, text)
    dl_after = text.count('class="share-anchor"')
    print(f"Deep links: {dl_after} share anchors converted (from {dl_before} hypertargets)")

    # --- Plan 0205: emit tooltip dict as inline JSON BEFORE reader.js runs ---
    # reader.js parses #hover-data in its IIFE, so the dict must be in the DOM
    # by the time the parser hits the reader.js <script> tag. Pandoc places
    # reader.js via --include-after-body (right before </body>); we anchor on
    # the reader.js header comment and back up to its <script> open tag.
    if _hover_dict:
        hover_json = json.dumps(_hover_dict, separators=(',', ':'), ensure_ascii=False)
        hover_json = hover_json.replace('</', '<\\/')  # prevent premature </script> close
        hover_block = f'<script type="application/json" id="hover-data">{hover_json}</script>\n'
        reader_anchor = text.find('/* Relinquishment HTML Reader')
        inserted = False
        if reader_anchor != -1:
            script_open = text.rfind('<script', 0, reader_anchor)
            if script_open != -1:
                text = text[:script_open] + hover_block + text[script_open:]
                print(f"  Hover-data JSON: {len(_hover_dict)} unique keys ({len(hover_json):,}B) [before reader.js]")
                inserted = True
        if not inserted:
            body_close = text.rfind('</body>')
            if body_close != -1:
                text = text[:body_close] + hover_block + text[body_close:]
                print(f"  Hover-data JSON: {len(_hover_dict)} unique keys ({len(hover_json):,}B) [fallback, pre-</body>]")
            else:
                print("  WARNING: neither reader.js nor </body> found; hover-data JSON not injected")

    html_path.write_text(text)
    print(f"HTML post-processed: {html_path}")


GLOSSARY_ENTRY_RE = re.compile(
    r'\\newglossaryentry\{(?P<key>[^}]+)\}\s*\{\s*name=\{(?P<name>[^}]+)\}',
    re.DOTALL,
)
ACRONYM_SPAN_RE = re.compile(
    r'<span data-acronym-label="(?P<key>[^"]+)" data-acronym-form="(?P<form>[^"]+)">(?P<text>[^<]*)</span>'
)


def _load_glossary_names(glossary_path):
    """Parse glossary-entries.tex → {lowercase_key: display_name}."""
    text = Path(glossary_path).read_text(encoding='utf-8')
    return {m.group('key').lower(): m.group('name')
            for m in GLOSSARY_ENTRY_RE.finditer(text)}


def inject_questions_index(html_path):
    """Generate a collapsible FAQ from the manifest and insert before Appendices."""
    html_path = Path(html_path)
    manifest = yaml.safe_load((REPO / 'build/deep-links.yaml').read_text())

    by_category = {}
    for e in manifest:
        if not e['id'].startswith('dl:'):
            continue
        by_category.setdefault(e['category'], []).append(e)

    lines = ['<details class="chapter-section" id="questions-index">']
    lines.append('  <summary><h2>Questions about this book</h2></summary>')
    lines.append('  <p><em>Each question links into the passage that answers it.</em></p>')
    for cat in ['skeptic', 'science', 'verification', 'ethics', 'curiosity', 'narrative']:
        if cat not in by_category:
            continue
        lines.append(f'  <h3>{cat.title()}</h3>')
        lines.append('  <ul>')
        for e in by_category[cat]:
            lines.append(f'    <li><a href="#{e["id"]}">{e["question"]}</a></li>')
        lines.append('  </ul>')
    lines.append('</details>')
    block = '\n'.join(lines)

    text = html_path.read_text()
    marker = '<details class="part-section"><summary'
    idx = text.find(marker)
    appendices_idx = text.find(marker, idx)
    found = False
    while appendices_idx != -1:
        if 'Appendices' in text[appendices_idx:appendices_idx + 200]:
            text = text[:appendices_idx] + block + '\n' + text[appendices_idx:]
            found = True
            break
        appendices_idx = text.find(marker, appendices_idx + 1)
    if not found:
        text = text[:appendices_idx] + block + '\n' + text[appendices_idx:]
    html_path.write_text(text)
    print(f"  Questions index: {sum(len(v) for v in by_category.values())} entries in {len(by_category)} categories")


def inject_flat_diagram(html_path):
    """Insert the Flat cross-section SVG after the canonical definition in the Flat chapter."""
    html_path = Path(html_path)
    text = html_path.read_text()

    FLAT_SVG = '''<figure id="fig-flat-cross-section" class="inline-svg" style="text-align:center;margin:1em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="130" viewBox="0 0 300 130" style="display:block;margin:0 auto;">
  <title>Cross-section of a computer chip. Two grey blocks of 3D semiconductor sandwich a thin blue layer — the two-dimensional electron gas (2DEG). Blue dots are electrons confined to this flat layer. They can move left and right but not up or down. This is the Flat.</title>
  <defs>
    <linearGradient id="flat-inline-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2471a3" stop-opacity="0.05"/>
      <stop offset="50%" stop-color="#2471a3" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#2471a3" stop-opacity="0.05"/>
    </linearGradient>
    <marker id="flat-inline-arr" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0,0 L 6,3 L 0,6 Z" fill="#1a5276"/>
    </marker>
  </defs>
  <rect x="30" y="20" width="240" height="25" rx="2" fill="#e0e0e0" stroke="#999" stroke-width="0.8"/>
  <text x="150" y="36" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">3D material (bulk semiconductor)</text>
  <rect x="30" y="50" width="240" height="8" rx="1" fill="url(#flat-inline-glow)" stroke="#2471a3" stroke-width="1.5"/>
  <rect x="30" y="63" width="240" height="25" rx="2" fill="#e0e0e0" stroke="#999" stroke-width="0.8"/>
  <text x="150" y="79" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">3D material (bulk semiconductor)</text>
  <circle cx="70" cy="54" r="2.5" fill="#2471a3" opacity="0.9"/>
  <circle cx="100" cy="54" r="2.5" fill="#2471a3" opacity="0.7"/>
  <circle cx="135" cy="54" r="2.5" fill="#2471a3" opacity="0.9"/>
  <circle cx="165" cy="54" r="2.5" fill="#2471a3" opacity="0.6"/>
  <circle cx="195" cy="54" r="2.5" fill="#2471a3" opacity="0.8"/>
  <circle cx="225" cy="54" r="2.5" fill="#2471a3" opacity="0.7"/>
  <circle cx="115" cy="55" r="2" fill="#2471a3" opacity="0.4"/>
  <circle cx="180" cy="53" r="2" fill="#2471a3" opacity="0.5"/>
  <circle cx="245" cy="54" r="2" fill="#2471a3" opacity="0.5"/>
  <line x1="58" y1="54" x2="48" y2="54" stroke="#1a5276" stroke-width="0.8" marker-end="url(#flat-inline-arr)"/>
  <line x1="252" y1="54" x2="262" y2="54" stroke="#1a5276" stroke-width="0.8" marker-end="url(#flat-inline-arr)"/>
  <text x="18" y="56" text-anchor="middle" font-size="7" fill="#2471a3" font-family="sans-serif" transform="rotate(-90,18,56)">2DEG</text>
  <text x="285" y="56" text-anchor="middle" font-size="7" fill="#2471a3" font-family="sans-serif" transform="rotate(90,285,56)">2DEG</text>
  <text x="150" y="104" text-anchor="middle" font-size="9" fill="#2471a3" font-family="serif" font-style="italic">electrons confined to two dimensions</text>
  <text x="150" y="118" text-anchor="middle" font-size="9" fill="#888" font-family="serif" font-style="italic">different physics applies here</text>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">The Flat: a two-dimensional electron gas sandwiched between bulk semiconductor layers.</figcaption>
</figure>'''

    marker = 'This book calls those thin worlds'
    idx = text.find(marker)
    if idx == -1:
        return
    close_p = text.find('</p>', idx)
    if close_p == -1:
        return
    insert_point = close_p + len('</p>')
    text = text[:insert_point] + '\n' + FLAT_SVG + '\n' + text[insert_point:]
    html_path.write_text(text)
    print("  Flat diagram: inline SVG injected")


def inject_button_sequence(html_path):
    """Insert 6-panel Kauffman button filmstrip after the buttons-and-threads analogy."""
    html_path = Path(html_path)
    text = html_path.read_text()

    # 30 button positions: jittered scatter across the floor
    bx = [
        38, 63, 85, 112, 135, 161, 180, 208, 225, 252,
        275, 292, 318, 338, 365, 388, 405, 435, 452, 478,
        48, 78, 122, 168, 218, 258, 308, 348, 398, 442,
    ]
    floor_y = [240] * 20 + [227] * 10

    def _btn_defs():
        return '<defs><filter id="kbtn-sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="1" dy="1" stdDeviation="1.5" flood-opacity="0.15"/></filter></defs>'

    def _floor():
        return '<line x1="20" y1="250" x2="480" y2="250" stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>'

    def _button(x, y):
        return f'<circle cx="{x}" cy="{y}" r="9" fill="#c4a97d" stroke="#a88b5e" stroke-width="1" filter="url(#kbtn-sh)"/>'

    def _thread(x1, y1, x2, y2, color="#666", width="1.2"):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" opacity="0.6"/>'

    def _label(txt):
        return f'<text x="15" y="18" font-family="Georgia, serif" font-size="9" fill="#aaa">{txt}</text>'

    def _counter(txt):
        return f'<text x="485" y="275" text-anchor="end" font-family="Georgia, serif" font-size="10" fill="#999">{txt}</text>'

    def _caption(txt):
        return f'<text x="250" y="275" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#555" font-style="italic">{txt}</text>'

    def _svg_wrap(content):
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="380" height="220" viewBox="0 0 500 290" style="display:block;margin:0.3em auto;">{content}</svg>'

    # Fixed pickup point — reader's eye anchors here across all panels
    PICKUP_Y = 40

    # --- Panel 1: Scatter (0 threads) ---
    p1_parts = [_btn_defs(), _floor()]
    for i in range(30):
        p1_parts.append(_button(bx[i], floor_y[i]))
    p1_parts.append(_label('scatter'))
    p1_parts.append(_counter('0 / 30'))
    p1_parts.append(_caption('Ten thousand buttons on a floor.'))
    PANEL_1 = _svg_wrap('\n'.join(p1_parts))

    # --- Panel 2: Tie and toss (6 threads) ---
    p2_floor_threads = [(3, 22), (22, 5), (0, 20), (6, 7), (19, 29)]
    p2_lifted = {9: PICKUP_Y, 8: PICKUP_Y + 12}
    p2_parts = [_btn_defs(), _floor()]
    for a, b in p2_floor_threads:
        p2_parts.append(_thread(bx[a], floor_y[a], bx[b], floor_y[b]))
    tx = bx[9] + 0.55 * (bx[8] - bx[9])
    ty = p2_lifted[9] + 0.55 * (p2_lifted[8] - p2_lifted[9])
    p2_parts.append(f'<line x1="{bx[9]}" y1="{p2_lifted[9]}" x2="{tx:.0f}" y2="{ty:.0f}" stroke="#666" stroke-width="1.2" opacity="0.6" stroke-dasharray="4,2"/>')
    p2_parts.append(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="2" fill="#999" opacity="0.5"/>')
    for i in range(30):
        y = p2_lifted.get(i, floor_y[i])
        p2_parts.append(_button(bx[i], y))
    p2_parts.append(_label('tie and toss'))
    p2_parts.append(_counter('6 / 30'))
    p2_parts.append(_caption('Pick up two at random. Tie them together. Toss them back.'))
    PANEL_2 = _svg_wrap('\n'.join(p2_parts))

    # --- Panel 3: Early clusters (10 threads) ---
    p3_threads = [
        (9, 8),
        (3, 22), (22, 5), (0, 20), (6, 7), (19, 29),
        (20, 1), (7, 24), (10, 25), (11, 26),
    ]
    p3_lifted = {9: PICKUP_Y, 8: PICKUP_Y + 35}
    p3_parts = [_btn_defs(), _floor()]
    for a, b in p3_threads:
        ya = p3_lifted.get(a, floor_y[a])
        yb = p3_lifted.get(b, floor_y[b])
        p3_parts.append(_thread(bx[a], ya, bx[b], yb))
    for i in range(30):
        y = p3_lifted.get(i, floor_y[i])
        p3_parts.append(_button(bx[i], y))
    p3_parts.append(_label('early clusters'))
    p3_parts.append(_counter('10 / 30'))
    p3_parts.append(_caption('A few hundred ties in. Small clumps \u2014 two, three buttons.'))
    PANEL_3 = _svg_wrap('\n'.join(p3_parts))

    # --- Panel 4: Growing net (15 threads) ---
    # Diamond cluster {6,7,8,9,10,24,25} with cross-links 10-7, 8-25.
    # 3 hubs: 7 (6,24,10), 8 (9,24,25), 24 (7,8,25).
    p4_threads = [
        (9, 8),
        (3, 22), (22, 5), (0, 20), (6, 7), (19, 29),
        (20, 1), (7, 24), (10, 25), (11, 26),
        (8, 24), (24, 25), (10, 7), (8, 25), (5, 23),
    ]
    p4_lifted = {9: PICKUP_Y, 8: PICKUP_Y + 25, 24: PICKUP_Y + 55,
                 25: PICKUP_Y + 55, 7: PICKUP_Y + 85, 10: PICKUP_Y + 85,
                 6: PICKUP_Y + 115}
    p4_parts = [_btn_defs(), _floor()]
    for a, b in p4_threads:
        ya = p4_lifted.get(a, floor_y[a])
        yb = p4_lifted.get(b, floor_y[b])
        p4_parts.append(_thread(bx[a], ya, bx[b], yb))
    for i in range(30):
        y = p4_lifted.get(i, floor_y[i])
        p4_parts.append(_button(bx[i], y))
    p4_parts.append(_label('growing net'))
    p4_parts.append(_counter('15 / 30'))
    p4_parts.append(_caption('Almost halfway. The clusters are getting bigger.'))
    PANEL_4 = _svg_wrap('\n'.join(p4_parts))

    # --- Panel 5: Almost (21 threads, 3 dashed bridges) ---
    # Sub-Right extends via 10-11-26-12-14-28 (dangler).
    # Sub-Left {2,3,5,22,23} on floor. 3 dashed bridges hint at snap.
    p5_threads = [
        (9, 8),
        (3, 22), (22, 5), (0, 20), (6, 7), (19, 29),
        (20, 1), (7, 24), (10, 25), (11, 26),
        (8, 24), (24, 25), (10, 7), (8, 25), (5, 23),
        (10, 11), (26, 12), (12, 14), (14, 28), (2, 3), (1, 21),
    ]
    p5_dashed = [(6, 23), (12, 13), (28, 29)]
    p5_lifted = {
        9: PICKUP_Y,
        8: PICKUP_Y + 20,
        24: PICKUP_Y + 45, 25: PICKUP_Y + 45,
        7: PICKUP_Y + 70, 10: PICKUP_Y + 70,
        6: PICKUP_Y + 95, 11: PICKUP_Y + 95,
        26: PICKUP_Y + 115,
        12: PICKUP_Y + 135,
        14: PICKUP_Y + 155,
        28: PICKUP_Y + 185,
    }
    p5_parts = [_btn_defs(), _floor()]
    for a, b in p5_threads:
        ya = p5_lifted.get(a, floor_y[a])
        yb = p5_lifted.get(b, floor_y[b])
        p5_parts.append(_thread(bx[a], ya, bx[b], yb))
    for a, b in p5_dashed:
        ya = p5_lifted.get(a, floor_y[a])
        yb = p5_lifted.get(b, floor_y[b])
        p5_parts.append(f'<line x1="{bx[a]}" y1="{ya}" x2="{bx[b]}" y2="{yb}" stroke="#999" stroke-width="1" opacity="0.4" stroke-dasharray="4,3"/>')
    for i in range(30):
        y = p5_lifted.get(i, floor_y[i])
        p5_parts.append(_button(bx[i], y))
    p5_parts.append(_label('almost'))
    p5_parts.append(_counter('21 / 30'))
    p5_parts.append(_caption('Three bridges away. Almost connected.'))
    PANEL_5 = _svg_wrap('\n'.join(p5_parts))

    # --- Panel 6: Phase transition (24 threads, 1 red) ---
    # Red bridge 6-23 snaps the giant component together.
    # Grey 26-27, 28-29 complete the net. 19 lifted, 11 on floor.
    p6_threads = [
        (9, 8),
        (3, 22), (22, 5), (0, 20), (6, 7), (19, 29),
        (20, 1), (7, 24), (10, 25), (11, 26),
        (8, 24), (24, 25), (10, 7), (8, 25), (5, 23),
        (10, 11), (26, 12), (12, 14), (14, 28), (2, 3), (1, 21),
        (26, 27), (28, 29),
    ]
    p6_red = (6, 23)
    p6_dist = {
        9: 0,
        8: 1,
        24: 2, 25: 2,
        7: 3, 10: 3,
        6: 4, 11: 4,
        23: 5, 26: 5,
        5: 6, 12: 6, 27: 6,
        22: 7, 14: 7,
        3: 8, 28: 8,
        2: 9, 29: 9,
        19: 10,
    }
    p6_lifted = {btn: PICKUP_Y + d * 15 for btn, d in p6_dist.items()}

    p6_parts = [_btn_defs(), _floor()]
    for a, b in p6_threads:
        ya = p6_lifted.get(a, floor_y[a])
        yb = p6_lifted.get(b, floor_y[b])
        p6_parts.append(_thread(bx[a], ya, bx[b], yb))
    ra, rb = p6_red
    p6_parts.append(_thread(bx[ra], p6_lifted[ra], bx[rb], p6_lifted[rb], color="#c0392b", width="2"))
    for i in range(30):
        y = p6_lifted.get(i, floor_y[i])
        p6_parts.append(_button(bx[i], y))
    p6_parts.append(_label('phase transition'))
    p6_parts.append(f'<text x="485" y="275" text-anchor="end" font-family="Georgia, serif" font-size="10" fill="#c0392b" font-weight="bold">24 / 30</text>')
    p6_parts.append(_caption('One more thread. Pick up one button \u2014 the whole room lifts.'))
    PANEL_6 = _svg_wrap('\n'.join(p6_parts))

    FILMSTRIP = f'''<figure id="fig-buttons-filmstrip" class="inline-svg button-sequence" style="text-align:center;margin:1.5em auto;">
{PANEL_1}
{PANEL_2}
{PANEL_3}
{PANEL_4}
{PANEL_5}
{PANEL_6}
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">Kauffman\u2019s buttons and threads \u2014 scatter, tie, net, snap.</figcaption>
</figure>'''

    marker = 'connected web.</p>'
    idx = text.find(marker)
    if idx == -1:
        return
    insert_point = idx + len(marker)
    text = text[:insert_point] + '\n' + FILMSTRIP + '\n' + text[insert_point:]
    html_path.write_text(text)
    print("  Button sequence: 6-panel filmstrip injected")


def inject_domain_buttons(html_path):
    """Insert the 11-domain button network diagram after the five-fields paragraph."""
    html_path = Path(html_path)
    text = html_path.read_text()

    DOMAIN_SVG = '''<figure id="fig-domain-buttons" class="inline-svg domain-buttons" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="460" height="440" viewBox="0 0 500 590" style="display:block;margin:0 auto;">
  <title>Kauffman\u2019s buttons and threads, mapped to eleven scientific domains. Seven domains form a connected web above the floor. The four-domain topological convergence cluster hangs below, connected by one solid thread and two theoretical bridges.</title>
  <defs>
    <filter id="dbtn-sh" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="1" dy="1" stdDeviation="1.5" flood-opacity="0.2"/>
    </filter>
  </defs>
  <!-- ===== UPPER WEB (above floor) ===== -->
  <!-- dashed cross-cluster bridges (background) -->
  <line x1="330" y1="178" x2="70" y2="140" stroke="#bbb" stroke-width="0.8" opacity="0.35" stroke-dasharray="5,3"/><!-- CE\u2194NLD -->
  <line x1="330" y1="178" x2="430" y2="80" stroke="#bbb" stroke-width="0.8" opacity="0.35" stroke-dasharray="5,3"/><!-- CE\u2194ACS -->
  <line x1="330" y1="225" x2="430" y2="140" stroke="#bbb" stroke-width="0.8" opacity="0.35" stroke-dasharray="5,3"/><!-- Par\u2194Auto -->
  <line x1="150" y1="210" x2="70" y2="140" stroke="#bbb" stroke-width="0.8" opacity="0.35" stroke-dasharray="5,3"/><!-- Mat\u2194NLD -->
  <!-- solid cross-cluster thread: NLD\u2194ACS (published) -->
  <line x1="70" y1="140" x2="430" y2="80" stroke="#777" stroke-width="1.0" opacity="0.45"/>
  <!-- intra-cluster solid threads (upper) -->
  <line x1="70" y1="80" x2="70" y2="140" stroke="#c0392b" stroke-width="1.5" opacity="0.65"/><!-- Sol\u2194NLD -->
  <line x1="430" y1="80" x2="430" y2="140" stroke="#e67e22" stroke-width="1.5" opacity="0.65"/><!-- ACS\u2194Auto -->
  <line x1="330" y1="178" x2="330" y2="225" stroke="#8e44ad" stroke-width="1.5" opacity="0.65"/><!-- CE\u2194Par -->
  <!-- ===== FLOOR LINE ===== -->
  <line x1="25" y1="305" x2="475" y2="305" stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="488" y="309" font-family="Helvetica, sans-serif" font-size="7" fill="#bbb">floor</text>
  <!-- ===== HANGING BRIDGES (cross floor, quadratic bezier with sag) ===== -->
  <!-- Mat\u2192CMP: SOLID (the one thread that holds) -->
  <path d="M150,210 Q230,340 310,370" stroke="#777" stroke-width="1.4" fill="none" opacity="0.55"/>
  <!-- CE\u2192Topo: dashed -->
  <path d="M330,178 Q295,310 250,335" stroke="#bbb" stroke-width="0.9" fill="none" opacity="0.4" stroke-dasharray="5,3"/>
  <!-- ACS\u2192TQC: dashed -->
  <path d="M430,140 Q390,330 250,410" stroke="#bbb" stroke-width="0.9" fill="none" opacity="0.4" stroke-dasharray="5,3"/>
  <!-- ===== BLUE CLUSTER (below floor, fully connected) ===== -->
  <!-- 6 solid blue intra-cluster edges -->
  <line x1="250" y1="335" x2="190" y2="370" stroke="#2471a3" stroke-width="1.5" opacity="0.65"/><!-- Topo\u2194TFT -->
  <line x1="250" y1="335" x2="310" y2="370" stroke="#2471a3" stroke-width="1.5" opacity="0.65"/><!-- Topo\u2194CMP -->
  <line x1="250" y1="335" x2="250" y2="410" stroke="#2471a3" stroke-width="1.5" opacity="0.65"/><!-- Topo\u2194TQC -->
  <line x1="190" y1="370" x2="310" y2="370" stroke="#2471a3" stroke-width="1.5" opacity="0.65"/><!-- TFT\u2194CMP -->
  <line x1="190" y1="370" x2="250" y2="410" stroke="#2471a3" stroke-width="1.5" opacity="0.65"/><!-- TFT\u2194TQC -->
  <line x1="310" y1="370" x2="250" y2="410" stroke="#2471a3" stroke-width="1.5" opacity="0.65"/><!-- CMP\u2194TQC -->
  <!-- ===== DOMAIN BUTTONS (interactive) ===== -->
  <!-- Upper web: red pair -->
  <g data-hover="Soliton physics \u2014 stable, self-reinforcing wave packets. Hasslacher\u2019s lattice-gas automaton (1986). Classical topological protection." style="cursor:pointer">
    <circle cx="70" cy="80" r="16" fill="#c0392b" stroke="#962d22" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="70" y="84" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">Sol</text>
  </g>
  <g data-hover="Nonlinear dynamics \u2014 chaos, bifurcations, self-organized criticality. The mathematics of systems far from equilibrium." style="cursor:pointer">
    <circle cx="70" cy="140" r="16" fill="#e74c3c" stroke="#c0392b" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="70" y="144" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">NLD</text>
  </g>
  <!-- Upper web: orange pair -->
  <g data-hover="Autocatalytic sets \u2014 Kauffman\u2019s theory of self-organization. Phase transitions in random graphs. Life as a critical phenomenon." style="cursor:pointer">
    <circle cx="430" cy="80" r="16" fill="#e67e22" stroke="#bf6516" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="430" y="84" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">ACS</text>
  </g>
  <g data-hover="Autopoiesis \u2014 Maturana and Varela (1980). Self-producing systems. The boundary between living and non-living." style="cursor:pointer">
    <circle cx="430" cy="140" r="16" fill="#f39c12" stroke="#d4860b" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="430" y="144" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">Auto</text>
  </g>
  <!-- Upper web: purple pair -->
  <g data-hover="Computational universality \u2014 Wolfram\u2019s Principle of Computational Equivalence. Sufficiently complex systems compute, regardless of substrate." style="cursor:pointer">
    <circle cx="330" cy="178" r="16" fill="#8e44ad" stroke="#6c3483" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="330" y="182" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">CE</text>
  </g>
  <g data-hover="Parallel computation \u2014 Hillis\u2019s Connection Machine. Massively parallel architectures that scale." style="cursor:pointer">
    <circle cx="330" cy="225" r="16" fill="#a569bd" stroke="#8e44ad" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="330" y="229" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">Par</text>
  </g>
  <!-- Upper web: brown (materials) -->
  <g data-hover="Materials science \u2014 the engineering discipline that builds the substrates. pHEMT, MOSFET, semiconductor fabrication." style="cursor:pointer">
    <circle cx="150" cy="210" r="16" fill="#b8860b" stroke="#8b6508" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="150" y="214" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7.5" fill="white" font-weight="bold">Mat</text>
  </g>
  <!-- Blue cluster (below floor) -->
  <g data-hover="Topology \u2014 the mathematics of shape and invariance. Knot theory, manifold classification. Freedman\u2019s Fields Medal." style="cursor:pointer">
    <circle cx="250" cy="335" r="16" fill="#2471a3" stroke="#1a5276" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="250" y="339" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">Topo</text>
  </g>
  <g data-hover="Topological field theory \u2014 where quantum physics meets topology. Witten 1989: TQFT from knot invariants." style="cursor:pointer">
    <circle cx="190" cy="370" r="16" fill="#2980b9" stroke="#2471a3" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="190" y="374" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">TFT</text>
  </g>
  <g data-hover="Condensed matter \u2014 the fractional quantum Hall effect, 2D electron gases, anyon excitations. Laughlin-Stormer-Tsui Nobel 1998." style="cursor:pointer">
    <circle cx="310" cy="370" r="16" fill="#3498db" stroke="#2980b9" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="310" y="374" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">CMP</text>
  </g>
  <g data-hover="Topological quantum computation \u2014 braiding non-Abelian anyons for fault-tolerant gates. Freedman-Kitaev-Wang 2002. The convergence point." style="cursor:pointer">
    <circle cx="250" cy="410" r="16" fill="#1a5276" stroke="#0d2f4b" stroke-width="1.5" filter="url(#dbtn-sh)"/>
    <text x="250" y="414" text-anchor="middle" font-family="Helvetica, sans-serif" font-size="7" fill="white" font-weight="bold">TQC</text>
  </g>
  <!-- ===== CAPTIONS ===== -->
  <text x="250" y="452" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#555">One thread holds. Cut it, and the argument falls apart.</text>
  <text x="250" y="467" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#999">after Kauffman (1993)</text>
  <!-- ===== LEGEND (3x2 compact grid) ===== -->
  <circle cx="40" cy="492" r="5" fill="#c0392b"/>
  <text x="55" y="496" font-family="Helvetica, sans-serif" font-size="8" fill="#555" font-weight="bold">Nonlinear</text>
  <text x="55" y="506" font-family="Helvetica, sans-serif" font-size="7" fill="#888">Sol \u00b7 NLD</text>
  <circle cx="195" cy="492" r="5" fill="#e67e22"/>
  <text x="210" y="496" font-family="Helvetica, sans-serif" font-size="8" fill="#555" font-weight="bold">Origin</text>
  <text x="210" y="506" font-family="Helvetica, sans-serif" font-size="7" fill="#888">ACS \u00b7 Auto</text>
  <circle cx="340" cy="492" r="5" fill="#8e44ad"/>
  <text x="355" y="496" font-family="Helvetica, sans-serif" font-size="8" fill="#555" font-weight="bold">Computation</text>
  <text x="355" y="506" font-family="Helvetica, sans-serif" font-size="7" fill="#888">CE \u00b7 Par</text>
  <circle cx="40" cy="524" r="5" fill="#b8860b"/>
  <text x="55" y="528" font-family="Helvetica, sans-serif" font-size="8" fill="#555" font-weight="bold">Materials</text>
  <text x="55" y="538" font-family="Helvetica, sans-serif" font-size="7" fill="#888">Mat</text>
  <circle cx="195" cy="524" r="5" fill="#2471a3"/>
  <text x="210" y="528" font-family="Helvetica, sans-serif" font-size="8" fill="#555" font-weight="bold">Topological</text>
  <text x="210" y="538" font-family="Helvetica, sans-serif" font-size="7" fill="#888">Topo \u00b7 TFT \u00b7 CMP \u00b7 TQC</text>
  <line x1="340" y1="527" x2="365" y2="527" stroke="#777" stroke-width="1.2"/>
  <text x="373" y="531" font-family="Helvetica, sans-serif" font-size="7.5" fill="#888">published</text>
  <line x1="340" y1="541" x2="365" y2="541" stroke="#bbb" stroke-width="0.8" stroke-dasharray="5,3"/>
  <text x="373" y="545" font-family="Helvetica, sans-serif" font-size="7.5" fill="#888">not yet built</text>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">The same metaphor, applied to this book. Seven domains form a web of published cross-references above the floor. The topological convergence hangs below \u2014 connected by one solid thread and bridges not yet built.</figcaption>
</figure>'''

    marker = 'five published research streams had independently matured'
    idx = text.find(marker)
    if idx == -1:
        return
    close_p = text.find('</p>', idx)
    if close_p == -1:
        return
    insert_point = close_p + len('</p>')
    text = text[:insert_point] + '\n' + DOMAIN_SVG + '\n' + text[insert_point:]
    html_path.write_text(text)
    print("  Domain buttons: inline diagram injected")


def fix_html_glossary_names(html_path):
    """Resolve <span data-acronym-label="..."> inner text to glossary name=.

    Pandoc converts \\gls{KEY} to <span data-acronym-label="KEY"
    data-acronym-form="...">KEY</span> but does not look up the
    name={DisplayName} from \\newglossaryentry. This pass does the lookup
    and rewrites the span's inner text.
    """
    html_path = Path(html_path)
    glossary_path = REPO / 'manuscript' / 'appendix' / 'glossary-entries.tex'
    names = _load_glossary_names(glossary_path)

    text = html_path.read_text()
    rewrites = 0
    unresolved_keys: set[str] = set()
    unhandled_forms: set[tuple[str, str]] = set()

    def _replace(m):
        nonlocal rewrites
        key = m.group('key')
        form = m.group('form')
        current = m.group('text')
        name = names.get(key.lower())
        if name is None:
            unresolved_keys.add(key)
            return m.group(0)
        if form == 'singular+short':
            target = name
        elif form == 'plural+short':
            target = name + 's'
        else:
            unhandled_forms.add((key, form))
            return m.group(0)
        if current == target:
            return m.group(0)  # idempotent: already resolved
        rewrites += 1
        return f'<span data-acronym-label="{key}" data-acronym-form="{form}">{target}</span>'

    text = ACRONYM_SPAN_RE.sub(_replace, text)

    for key in sorted(unresolved_keys):
        sys.stderr.write(f"WARNING: unresolved \\gls key: {key}\n")
    for key, form in sorted(unhandled_forms):
        sys.stderr.write(f"WARNING: unhandled \\gls form '{form}' for key '{key}'\n")

    html_path.write_text(text)
    print(f"Glossary names: {rewrites} acronym spans resolved")


def inject_genesis_illustrations(html_path):
    """Insert Genesis chapter SVG illustrations (Plan 0242)."""
    html_path = Path(html_path)
    text = html_path.read_text()

    AUTOCATALYTIC_LOOP = '''<figure id="fig-autocatalytic-loop" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200" style="display:block;margin:0 auto;">
  <title>Autocatalytic loop: three molecules A, B, and C arranged in a circle. A catalyzes B, B catalyzes C, C catalyzes A. The whole network sustains itself.</title>
  <defs>
    <marker id="aloop-arr" viewBox="0 0 8 6" refX="7" refY="3" markerWidth="7" markerHeight="5" orient="auto">
      <path d="M 0,0 L 8,3 L 0,6 Z" fill="#8b6914"/>
    </marker>
  </defs>
  <circle cx="150" cy="38" r="22" fill="#c4a97d" stroke="#a88b5e" stroke-width="1.5"/>
  <text x="150" y="43" text-anchor="middle" font-family="Georgia, serif" font-size="14" fill="#5a3e1b" font-weight="bold">A</text>
  <circle cx="216" cy="128" r="22" fill="#d4a574" stroke="#a88b5e" stroke-width="1.5"/>
  <text x="216" y="133" text-anchor="middle" font-family="Georgia, serif" font-size="14" fill="#5a3e1b" font-weight="bold">B</text>
  <circle cx="84" cy="128" r="22" fill="#b8956a" stroke="#a88b5e" stroke-width="1.5"/>
  <text x="84" y="133" text-anchor="middle" font-family="Georgia, serif" font-size="14" fill="#5a3e1b" font-weight="bold">C</text>
  <path d="M 170,46 Q 210,55 210,106" fill="none" stroke="#8b6914" stroke-width="1.5" marker-end="url(#aloop-arr)"/>
  <path d="M 196,142 Q 150,170 100,142" fill="none" stroke="#8b6914" stroke-width="1.5" marker-end="url(#aloop-arr)"/>
  <path d="M 72,110 Q 60,70 135,42" fill="none" stroke="#8b6914" stroke-width="1.5" marker-end="url(#aloop-arr)"/>
  <text x="215" y="75" font-family="Georgia, serif" font-size="9" fill="#8b6914" font-style="italic">catalyzes</text>
  <text x="150" y="170" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#8b6914" font-style="italic">catalyzes</text>
  <text x="55" y="75" font-family="Georgia, serif" font-size="9" fill="#8b6914" font-style="italic">catalyzes</text>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">An autocatalytic loop: each molecule catalyzes the next. The network sustains itself.</figcaption>
</figure>'''

    EDGE_OF_CHAOS = '''<figure id="fig-edge-of-chaos" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="160" viewBox="0 0 400 160" style="display:block;margin:0 auto;">
  <title>Three regimes side by side. Left: a rigid blue grid of locked nodes — frozen, too ordered to compute. Center: a narrow green band of flexibly connected nodes — the edge of chaos, where computation and life are possible. Right: scattered red dots flying apart — chaos, too disordered to remember.</title>
  <rect x="10" y="15" width="115" height="100" rx="4" fill="#eaf2f8" stroke="#2471a3" stroke-width="0.8" opacity="0.4"/>
  <line x1="35" y1="35" x2="100" y2="35" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="35" y1="55" x2="100" y2="55" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="35" y1="75" x2="100" y2="75" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="35" y1="95" x2="100" y2="95" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="35" y1="35" x2="35" y2="95" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="57" y1="35" x2="57" y2="95" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="78" y1="35" x2="78" y2="95" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <line x1="100" y1="35" x2="100" y2="95" stroke="#2471a3" stroke-width="0.8" opacity="0.5"/>
  <circle cx="35" cy="35" r="3.5" fill="#2471a3"/><circle cx="57" cy="35" r="3.5" fill="#2471a3"/>
  <circle cx="78" cy="35" r="3.5" fill="#2471a3"/><circle cx="100" cy="35" r="3.5" fill="#2471a3"/>
  <circle cx="35" cy="55" r="3.5" fill="#2471a3"/><circle cx="57" cy="55" r="3.5" fill="#2471a3"/>
  <circle cx="78" cy="55" r="3.5" fill="#2471a3"/><circle cx="100" cy="55" r="3.5" fill="#2471a3"/>
  <circle cx="35" cy="75" r="3.5" fill="#2471a3"/><circle cx="57" cy="75" r="3.5" fill="#2471a3"/>
  <circle cx="78" cy="75" r="3.5" fill="#2471a3"/><circle cx="100" cy="75" r="3.5" fill="#2471a3"/>
  <circle cx="35" cy="95" r="3.5" fill="#2471a3"/><circle cx="57" cy="95" r="3.5" fill="#2471a3"/>
  <circle cx="78" cy="95" r="3.5" fill="#2471a3"/><circle cx="100" cy="95" r="3.5" fill="#2471a3"/>
  <text x="67" y="128" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#1a5276" font-style="italic">frozen</text>
  <rect x="145" y="15" width="70" height="100" rx="4" fill="#eafaf1" stroke="#27ae60" stroke-width="1.2" opacity="0.5"/>
  <circle cx="160" cy="38" r="3.5" fill="#27ae60"/><circle cx="195" cy="42" r="3.5" fill="#27ae60"/>
  <circle cx="172" cy="58" r="3.5" fill="#27ae60"/><circle cx="188" cy="72" r="3.5" fill="#27ae60"/>
  <circle cx="155" cy="82" r="3.5" fill="#27ae60"/><circle cx="200" cy="92" r="3.5" fill="#27ae60"/>
  <circle cx="175" cy="98" r="3.5" fill="#27ae60"/>
  <path d="M 160,38 Q 168,45 172,58" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.7"/>
  <path d="M 195,42 Q 190,52 188,72" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.7"/>
  <path d="M 172,58 Q 180,65 188,72" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.7"/>
  <path d="M 155,82 Q 165,90 175,98" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.7"/>
  <path d="M 188,72 Q 194,82 200,92" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.7"/>
  <path d="M 160,38 Q 155,60 155,82" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.5"/>
  <path d="M 195,42 Q 200,66 200,92" fill="none" stroke="#27ae60" stroke-width="1" opacity="0.5"/>
  <text x="180" y="128" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#1e8449" font-weight="bold" font-style="italic">edge</text>
  <rect x="235" y="15" width="115" height="100" rx="4" fill="#fdedec" stroke="#c0392b" stroke-width="0.8" opacity="0.4"/>
  <circle cx="258" cy="30" r="3" fill="#c0392b" opacity="0.7"/><circle cx="310" cy="25" r="2.5" fill="#c0392b" opacity="0.5"/>
  <circle cx="335" cy="42" r="3" fill="#c0392b" opacity="0.8"/><circle cx="270" cy="55" r="2.5" fill="#c0392b" opacity="0.6"/>
  <circle cx="320" cy="65" r="3" fill="#c0392b" opacity="0.7"/><circle cx="248" cy="78" r="2.5" fill="#c0392b" opacity="0.5"/>
  <circle cx="295" cy="85" r="3" fill="#c0392b" opacity="0.6"/><circle cx="340" cy="95" r="2.5" fill="#c0392b" opacity="0.7"/>
  <circle cx="260" cy="100" r="2.5" fill="#c0392b" opacity="0.5"/>
  <text x="292" y="128" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#922b21" font-style="italic">chaos</text>
  <text x="180" y="152" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#888" font-style="italic">computation, adaptation, life</text>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">The edge of chaos: a narrow regime between frozen order and formless chaos where complex systems can compute.</figcaption>
</figure>'''

    SUBSTRATE_PARALLEL = '''<figure id="fig-substrate-parallel" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="420" height="200" viewBox="0 0 420 200" style="display:block;margin:0 auto;">
  <title>Split panel showing the substrate parallel. Left: a warm-colored beaker containing three molecules in a self-sustaining catalytic loop (A catalyzes B, B catalyzes C, C catalyzes A). Right: a cool-colored two-dimensional electron gas with three anyonic quasiparticles connected by braiding arcs in the same triangular pattern. Center: the words "same mathematics" bridging both sides. The point: different substrates, identical organizational principle.</title>
  <defs>
    <marker id="sp-arr-warm" viewBox="0 0 8 6" refX="7" refY="3" markerWidth="6" markerHeight="4" orient="auto">
      <path d="M 0,0 L 8,3 L 0,6 Z" fill="#8b6914"/>
    </marker>
    <marker id="sp-arr-cool" viewBox="0 0 8 6" refX="7" refY="3" markerWidth="6" markerHeight="4" orient="auto">
      <path d="M 0,0 L 8,3 L 0,6 Z" fill="#1a5276"/>
    </marker>
    <linearGradient id="sp-2deg-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2471a3" stop-opacity="0.05"/>
      <stop offset="50%" stop-color="#2471a3" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#2471a3" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
  <rect x="10" y="10" width="170" height="150" rx="6" fill="#fdf2e9" stroke="#a88b5e" stroke-width="0.8" opacity="0.5"/>
  <path d="M 55,30 L 45,120 Q 45,135 60,135 L 130,135 Q 145,135 145,120 L 135,30 Z" fill="none" stroke="#a88b5e" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="55" y1="30" x2="135" y2="30" stroke="#a88b5e" stroke-width="1"/>
  <circle cx="95" cy="55" r="10" fill="#c4a97d" stroke="#a88b5e" stroke-width="1.2"/>
  <text x="95" y="59" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#5a3e1b" font-weight="bold">A</text>
  <circle cx="125" cy="105" r="10" fill="#d4a574" stroke="#a88b5e" stroke-width="1.2"/>
  <text x="125" y="109" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#5a3e1b" font-weight="bold">B</text>
  <circle cx="65" cy="105" r="10" fill="#b8956a" stroke="#a88b5e" stroke-width="1.2"/>
  <text x="65" y="109" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#5a3e1b" font-weight="bold">C</text>
  <path d="M 104,60 Q 120,70 122,95" fill="none" stroke="#8b6914" stroke-width="1.2" marker-end="url(#sp-arr-warm)"/>
  <path d="M 116,112 Q 95,125 75,112" fill="none" stroke="#8b6914" stroke-width="1.2" marker-end="url(#sp-arr-warm)"/>
  <path d="M 60,96 Q 55,75 88,58" fill="none" stroke="#8b6914" stroke-width="1.2" marker-end="url(#sp-arr-warm)"/>
  <text x="95" y="175" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#8b6914" font-style="italic">chemistry</text>
  <line x1="195" y1="30" x2="195" y2="140" stroke="#888" stroke-width="1" stroke-dasharray="4,3" opacity="0.6"/>
  <line x1="225" y1="30" x2="225" y2="140" stroke="#888" stroke-width="1" stroke-dasharray="4,3" opacity="0.6"/>
  <text x="210" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#555" font-style="italic">same</text>
  <text x="210" y="95" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#555" font-style="italic">mathematics</text>
  <rect x="240" y="10" width="170" height="150" rx="6" fill="#eaf2f8" stroke="#2471a3" stroke-width="0.8" opacity="0.4"/>
  <rect x="270" y="40" width="110" height="14" rx="2" fill="#e0e0e0" stroke="#999" stroke-width="0.6"/>
  <text x="325" y="50" text-anchor="middle" font-family="sans-serif" font-size="6" fill="#888">3D bulk</text>
  <rect x="270" y="58" width="110" height="5" rx="1" fill="url(#sp-2deg-glow)" stroke="#2471a3" stroke-width="1"/>
  <rect x="270" y="67" width="110" height="14" rx="2" fill="#e0e0e0" stroke="#999" stroke-width="0.6"/>
  <text x="325" y="77" text-anchor="middle" font-family="sans-serif" font-size="6" fill="#888">3D bulk</text>
  <circle cx="305" cy="100" r="10" fill="#d4e6f1" stroke="#2471a3" stroke-width="1.2"/>
  <text x="305" y="104" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#1a5276" font-style="italic">a</text>
  <circle cx="355" cy="100" r="10" fill="#d4e6f1" stroke="#2471a3" stroke-width="1.2"/>
  <text x="355" y="104" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#1a5276" font-style="italic">b</text>
  <circle cx="330" cy="135" r="10" fill="#d4e6f1" stroke="#2471a3" stroke-width="1.2"/>
  <text x="330" y="139" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#1a5276" font-style="italic">c</text>
  <path d="M 314,95 Q 340,85 350,93" fill="none" stroke="#1a5276" stroke-width="1.2" marker-end="url(#sp-arr-cool)"/>
  <path d="M 349,109 Q 345,125 337,130" fill="none" stroke="#1a5276" stroke-width="1.2" marker-end="url(#sp-arr-cool)"/>
  <path d="M 322,138 Q 305,125 302,112" fill="none" stroke="#1a5276" stroke-width="1.2" marker-end="url(#sp-arr-cool)"/>
  <text x="325" y="175" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#1a5276" font-style="italic">quantum</text>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">Different substrates, same mathematics: catalytic chemistry (left) and quantum braiding (right) share the same self-sustaining loop structure.</figcaption>
</figure>'''

    CANOPY_PROBLEM = '''<figure id="fig-canopy-problem" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="350" height="220" viewBox="0 0 350 220" style="display:block;margin:0 auto;">
  <title>Forest cross-section: two tall trees with broad green crowns fill the canopy, catching all the sunlight. Between them on the forest floor, a tiny seedling sits in deep shadow, unable to grow. The ecological niche is full.</title>
  <defs>
    <linearGradient id="canopy-sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef9e7" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fef9e7" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="canopy-shadow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a2e1a" stop-opacity="0.25"/>
      <stop offset="80%" stop-color="#1a2e1a" stop-opacity="0.08"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="350" height="80" fill="url(#canopy-sky)"/>
  <line x1="30" y1="12" x2="30" y2="35" stroke="#f4d03f" stroke-width="1.5" opacity="0.4"/>
  <line x1="70" y1="8" x2="70" y2="30" stroke="#f4d03f" stroke-width="1.5" opacity="0.5"/>
  <line x1="110" y1="5" x2="110" y2="25" stroke="#f4d03f" stroke-width="1.5" opacity="0.6"/>
  <line x1="150" y1="3" x2="150" y2="22" stroke="#f4d03f" stroke-width="1.5" opacity="0.6"/>
  <line x1="200" y1="3" x2="200" y2="22" stroke="#f4d03f" stroke-width="1.5" opacity="0.6"/>
  <line x1="245" y1="5" x2="245" y2="25" stroke="#f4d03f" stroke-width="1.5" opacity="0.6"/>
  <line x1="285" y1="8" x2="285" y2="30" stroke="#f4d03f" stroke-width="1.5" opacity="0.5"/>
  <line x1="320" y1="12" x2="320" y2="35" stroke="#f4d03f" stroke-width="1.5" opacity="0.4"/>
  <ellipse cx="105" cy="50" rx="85" ry="35" fill="#27ae60" opacity="0.75"/>
  <ellipse cx="100" cy="48" rx="78" ry="30" fill="#2ecc71" opacity="0.6"/>
  <ellipse cx="255" cy="50" rx="80" ry="33" fill="#27ae60" opacity="0.75"/>
  <ellipse cx="260" cy="48" rx="72" ry="28" fill="#2ecc71" opacity="0.6"/>
  <rect x="90" y="75" width="10" height="115" rx="2" fill="#8b6914" opacity="0.8"/>
  <rect x="250" y="78" width="10" height="112" rx="2" fill="#8b6914" opacity="0.8"/>
  <rect x="0" y="80" width="350" height="110" fill="url(#canopy-shadow)"/>
  <rect x="0" y="190" width="350" height="5" rx="1" fill="#a88b5e" opacity="0.4"/>
  <line x1="175" y1="185" x2="175" y2="190" stroke="#2ecc71" stroke-width="1.5"/>
  <ellipse cx="175" cy="183" rx="4" ry="3" fill="#82e0aa" opacity="0.8"/>
  <ellipse cx="173" cy="181" rx="2.5" ry="2" fill="#82e0aa" opacity="0.6"/>
  <ellipse cx="177" cy="181" rx="2.5" ry="2" fill="#82e0aa" opacity="0.6"/>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">The canopy problem: the first organism to cross the threshold owns the niche. The seedling never reaches the light.</figcaption>
</figure>'''

    svgs = [
        ('ecological niche is full.', CANOPY_PROBLEM, 'canopy problem'),
        ('threshold was\ncrossed.', SUBSTRATE_PARALLEL, 'substrate parallel'),
        ('best able to evolve as well.', EDGE_OF_CHAOS, 'edge of chaos'),
        ('network sustains itself.', AUTOCATALYTIC_LOOP, 'autocatalytic loop'),
    ]

    injected = []
    for marker, svg, name in reversed(svgs):
        idx = text.find(marker)
        if idx == -1:
            continue
        close_p = text.find('</p>', idx)
        if close_p == -1:
            continue
        insert_point = close_p + len('</p>')
        text = text[:insert_point] + '\n' + svg + '\n' + text[insert_point:]
        injected.append(name)

    if injected:
        html_path.write_text(text)
        for name in injected:
            print(f"  Genesis: {name} SVG injected")


def inject_chapter_puzzles(html_path):
    """Insert approved puzzles into chapter HTML (Plan 0255)."""
    import hashlib as _hashlib
    tracker_path = REPO / 'build' / 'puzzle-tracker.yaml'
    data_path = REPO / 'build' / 'puzzle-data.yaml'
    if not tracker_path.exists() or not data_path.exists():
        return
    tracker = yaml.safe_load(tracker_path.read_text())
    pdata = yaml.safe_load(data_path.read_text())

    approved = {}
    for p in tracker.get('chapter_puzzles', []):
        if p.get('approved'):
            approved[p['id']] = p

    if not approved:
        return

    content = {}
    for p in pdata.get('chapter_puzzles', []):
        if p['id'] in approved:
            content[p['id']] = p

    html_path = Path(html_path)
    text = html_path.read_text()
    injected = 0

    CHAPTER_MARKERS = {
        'the-flat': '<div class="custodian-interlude" id="custodian:dance">',
    }

    def _esc(s):
        return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

    for pid, tracker_entry in approved.items():
        puzzle = content.get(pid)
        if not puzzle:
            continue
        ptype = puzzle.get('type', '')
        if ptype != 'mc':
            continue
        chapter = tracker_entry.get('location', {}).get('chapter', '')
        marker = CHAPTER_MARKERS.get(chapter)
        if not marker:
            continue
        idx = text.find(marker)
        if idx == -1:
            continue

        title = _esc(puzzle.get('title', ''))
        blurb = puzzle.get('gateway_blurb', '')
        question = _esc(puzzle.get('question', ''))
        hint_text = _esc(puzzle.get('hint', ''))
        abstract_text = _esc(puzzle.get('abstract', '').strip())
        egg_url = puzzle.get('egg_url', '').strip()
        options = puzzle.get('options', [])
        answer_key = str(puzzle.get('answer_key', ''))
        answer_hash = _hashlib.sha256(answer_key.encode()).hexdigest()

        blurb_html = ''
        if blurb:
            blurb_html = f'<p class="pz-gateway-blurb">\U0001f9e9 {_esc(blurb)}</p>'

        opts_json = []
        for o in options:
            opts_json.append('{' + f'"key":"{_esc(o["key"])}","text":"{_esc(o["text"])}"' + '}')
        opts_json_str = '[' + ','.join(opts_json) + ']'

        egg_link = ''
        if egg_url:
            egg_link = f'<p class="pz-egg-reward"><a href="{_esc(egg_url)}" target="_blank">&#x1f513; Continue exploring &rarr;</a></p>'

        puzzle_html = f'''
<details class="puzzle-section" open>
  <summary>Puzzle</summary>
  <style>
.puzzle-section {{ margin: 2em 0; border: 1px solid #ddd; border-radius: 6px; background: #fafafa; }}
.puzzle-section summary {{ padding: 0.8em 1em; cursor: pointer; font-weight: bold; color: #1a5276; font-size: 1.05em; }}
.puzzle-section summary:hover {{ color: #154360; }}
.pz-container {{ padding: 0 1.5em 1.5em; }}
.pz-container.pz-solved {{ border-color: #2a9b9a; }}
.pz-question {{ font-size: 1.05em; margin-bottom: 1em; }}
.pz-gateway-blurb {{ font-size: 0.88em; color: #666; font-style: italic; margin: -0.5em 0 0.8em 0; padding: 0.4em 0.6em; border-left: 3px solid #2a9b9a; background: #f5fafa; border-radius: 0 4px 4px 0; }}
.pz-option-btn {{ display: block; width: 100%; text-align: left; font-family: Georgia, "Times New Roman", serif; font-size: 1em; padding: 0.7em 1em; margin-bottom: 0.5em; border: 1px solid #ccc; border-radius: 4px; background: #fff; cursor: pointer; transition: border-color 0.2s, background 0.2s; }}
.pz-option-btn:hover {{ border-color: #1a5276; background: #f0f6fa; }}
.pz-option-btn.pz-wrong {{ border-color: #c0392b; background: #fdf2f2; animation: pz-shake 0.3s ease-in-out; }}
.pz-option-btn.pz-correct {{ border-color: #2a9b9a; background: #e8f8f5; font-weight: bold; }}
@keyframes pz-shake {{ 0%, 100% {{ transform: translateX(0); }} 25% {{ transform: translateX(-4px); }} 75% {{ transform: translateX(4px); }} }}
.pz-hint {{ display: none; color: #856404; background: #fff9e6; border-left: 3px solid #d4a14b; padding: 0.6em 1em; margin-top: 0.5em; font-style: italic; }}
.pz-hint.pz-visible {{ display: block; }}
.pz-result {{ display: none; margin-top: 1em; }}
.pz-result.pz-visible {{ display: block; }}
.pz-solved-badge {{ color: #2a9b9a; font-weight: bold; font-size: 1.1em; margin-bottom: 0.5em; }}
.pz-abstract {{ border-left: 3px solid #2a9b9a; padding: 0.8em 1em; margin: 0; background: #f0faf9; font-style: italic; color: #333; line-height: 1.5; }}
.pz-egg-reward {{ margin-top: 1em; text-align: center; }}
.pz-egg-reward a {{ display: inline-block; padding: 0.5em 1.2em; background: #2a9b9a; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; transition: background 0.2s; }}
.pz-egg-reward a:hover {{ background: #238a89; }}
.pz-fallback {{ font-style: italic; color: #888; }}
@media (prefers-color-scheme: dark) {{
  .puzzle-section {{ background: #242424; border-color: #444; }}
  .puzzle-section summary {{ color: #6ba3f7; }}
  .pz-container.pz-solved {{ border-color: #2a9b9a; }}
  .pz-gateway-blurb {{ color: #aaa; background: #1a2a2a; }}
  .pz-option-btn {{ background: #2a2a2a; border-color: #555; color: #e0e0e0; }}
  .pz-option-btn:hover {{ background: #1e3a50; border-color: #6ba3f7; }}
  .pz-option-btn.pz-wrong {{ background: #3a1a1a; border-color: #c0392b; }}
  .pz-option-btn.pz-correct {{ background: #1a3a35; border-color: #2a9b9a; }}
  .pz-hint {{ background: #2a2510; color: #f0d060; border-left-color: #d4a14b; }}
  .pz-abstract {{ background: #1a2e2d; color: #ccc; }}
  .pz-egg-reward a {{ background: #1a6b6a; }}
  .pz-egg-reward a:hover {{ background: #1f7d7c; }}
}}
@media (max-width: 600px) {{
  .pz-option-btn {{ min-height: 44px; }}
}}
  </style>
  <div class="pz-container" id="{pid}" data-puzzle-id="{pid}">
    <h3>{title}</h3>
    {blurb_html}
    <p class="pz-question">{question}</p>
    <div class="pz-interaction" id="pz-inter-{pid}"></div>
    <p class="pz-hint" id="pz-hint-{pid}">{hint_text}</p>
    <div class="pz-result" id="pz-result-{pid}">
      <div class="pz-solved-badge">&#10003; Solved</div>
      <blockquote class="pz-abstract">{abstract_text}</blockquote>
      {egg_link}
    </div>
    <noscript><p class="pz-fallback">Enable JavaScript to interact with this puzzle.</p></noscript>
  </div>
  <script>
(function() {{
  var SKEY = "relinquishment-puzzles-solved";
  var pid = "{pid}";
  var answerHash = "{answer_hash}";
  var options = {opts_json_str};

  function getSolved() {{ try {{ var s = localStorage.getItem(SKEY); return s ? JSON.parse(s) : {{}}; }} catch(e) {{ return {{}}; }} }}
  function setSolved(id) {{ try {{ var s = getSolved(); s[id] = true; localStorage.setItem(SKEY, JSON.stringify(s)); }} catch(e) {{}} }}

  function revealPuzzle() {{
    var el = document.getElementById(pid);
    if (el) el.classList.add("pz-solved");
    var inter = document.getElementById("pz-inter-" + pid);
    if (inter) inter.style.display = "none";
    var hint = document.getElementById("pz-hint-" + pid);
    if (hint) hint.classList.remove("pz-visible");
    var result = document.getElementById("pz-result-" + pid);
    if (result) result.classList.add("pz-visible");
    setSolved(pid);
  }}

  function showHint() {{
    var h = document.getElementById("pz-hint-" + pid);
    if (h) h.classList.add("pz-visible");
  }}

  function escHtml(s) {{ var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }}

  function sha256(msg) {{
    var buf = new TextEncoder().encode(msg);
    return crypto.subtle.digest("SHA-256", buf).then(function(hash) {{
      return Array.from(new Uint8Array(hash)).map(function(b) {{ return b.toString(16).padStart(2, "0"); }}).join("");
    }});
  }}

  function checkAnswer(key, btn) {{
    if (getSolved()[pid]) return;
    if (!(window.crypto && window.crypto.subtle)) {{ revealPuzzle(); return; }}
    sha256(key).then(function(h) {{
      if (h === answerHash) {{
        btn.classList.add("pz-correct");
        setTimeout(revealPuzzle, 400);
      }} else {{
        btn.classList.add("pz-wrong");
        setTimeout(function() {{ btn.classList.remove("pz-wrong"); }}, 600);
        showHint();
      }}
    }});
  }}

  function init() {{
    if (getSolved()[pid]) {{ revealPuzzle(); return; }}
    var inter = document.getElementById("pz-inter-" + pid);
    if (!inter) return;
    var html = "";
    for (var i = 0; i < options.length; i++) {{
      var o = options[i];
      html += '<button class="pz-option-btn" data-key="' + escHtml(o.key) + '">(' + escHtml(o.key) + ') ' + escHtml(o.text) + '</button>';
    }}
    inter.innerHTML = html;
    var btns = inter.querySelectorAll(".pz-option-btn");
    for (var j = 0; j < btns.length; j++) {{
      (function(btn) {{
        btn.addEventListener("click", function() {{ checkAnswer(btn.dataset.key, btn); }});
      }})(btns[j]);
    }}
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", init);
  }} else {{
    init();
  }}
}})();
  </script>
</details>
'''
        text = text[:idx] + puzzle_html + text[idx:]
        injected += 1

    if injected:
        html_path.write_text(text)
    print(f"  Chapter puzzles: {injected} injected")


def collapse_tech_sections(html_path):
    """Wrap approved tech sections in collapsible <details> elements (Plan 0219)."""
    manifest_path = REPO / 'build' / 'tech-collapse.yaml'
    if not manifest_path.exists():
        return
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    entries = [e for e in manifest.get('sections', [])
               if isinstance(e, dict) and e.get('status') in ('approved', 'live')]
    if not entries:
        return

    html_path = Path(html_path)
    text = html_path.read_text()
    count = 0
    rich_tooltips = {}

    for entry in entries:
        tooltip = entry.get('tooltip', '').strip()
        hover_id = entry.get('hover_id')
        for label_key in ('spine_label', 'bridge_label'):
            label = entry.get(label_key)
            if not label:
                continue
            id_attr = f'id="{label}"'
            id_pos = text.find(id_attr)
            if id_pos == -1:
                continue

            heading_start = text.rfind('<h', max(0, id_pos - 120), id_pos)
            if heading_start == -1:
                continue
            heading_tag = text[heading_start:heading_start + 4]
            heading_level = heading_tag[2]
            heading_close = text.find('>', id_pos) + 1
            heading_end_tag = f'</h{heading_level}>'
            heading_end = text.find(heading_end_tag, heading_close)
            if heading_end == -1:
                continue
            heading_end += len(heading_end_tag)

            title_text = re.sub(r'<[^>]+>', '', text[heading_close:heading_end - len(heading_end_tag)]).strip()

            next_heading = re.search(
                rf'<h[1-{heading_level}][\s>]|<details class="tech-section"|</details>|<div class="custodian-interlude"',
                text[heading_end:]
            )
            if next_heading:
                section_end = heading_end + next_heading.start()
            else:
                parent_details = text.find('</details>', heading_end)
                section_end = parent_details if parent_details != -1 else len(text)

            content = text[heading_end:section_end]

            if hover_id:
                grade_span = f'<span class="tech-grade" data-hover-id="{hover_id}" aria-hidden="true"></span>'
                rich_html = entry.get('html', '')
                if rich_html:
                    rich_tooltips[hover_id] = {"t": tooltip, "h": rich_html}
                elif tooltip:
                    rich_tooltips[hover_id] = {"t": tooltip}
            else:
                grade_tooltip = html_mod.escape(tooltip) if tooltip else 'Verified science — a technical discussion grounded in published, peer-reviewed physics. Safe to skip; expand if curious.'
                grade_span = f'<span class="tech-grade" data-hover="{grade_tooltip}" aria-hidden="true"></span>'
            link_span = f'<span class="share-anchor" data-link-id="{label}" aria-hidden="true"></span>'
            wrapper = (
                f'<details class="tech-section" id="{label}">'
                f'<summary><span class="tech-title">{title_text}</span>{grade_span}{link_span}</summary>\n'
                f'{content}'
                f'</details>\n'
            )
            text = text[:heading_start] + wrapper + text[section_end:]
            count += 1

    if rich_tooltips:
        json_pat = re.compile(r'(<script type="application/json" id="hover-data">)(.*?)(</script>)', re.DOTALL)
        m = json_pat.search(text)
        if m:
            hover_data = json.loads(m.group(2))
            hover_data.update(rich_tooltips)
            text = text[:m.start(2)] + json.dumps(hover_data, ensure_ascii=False) + text[m.end(2):]

    if count:
        html_path.write_text(text)
        print(f"  Tech sections: {count} collapsed")


def fix_epub(epub_path):
    """Post-process EPUB to fix pandoc validation errors."""
    epub_path = Path(epub_path)
    tmp_path = epub_path.with_suffix('.tmp.epub')

    with zipfile.ZipFile(epub_path, 'r') as zin, \
         zipfile.ZipFile(tmp_path, 'w') as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.endswith('.xhtml'):
                text = data.decode('utf-8')
                # Strip invalid label= attributes (pandoc bug, 6 instances)
                text = re.sub(r'\s+label="[^"]*"', '', text)
                data = text.encode('utf-8')
            zout.writestr(item, data)

    tmp_path.replace(epub_path)
    print(f"EPUB post-processed: {epub_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--fix-epub':
        fix_epub(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == '--fix-html':
        fix_html_toc(sys.argv[2])
        inject_flat_diagram(sys.argv[2])
        inject_button_sequence(sys.argv[2])
        inject_domain_buttons(sys.argv[2])
        inject_genesis_illustrations(sys.argv[2])
        inject_chapter_puzzles(sys.argv[2])
        inject_questions_index(sys.argv[2])
        fix_html_glossary_names(sys.argv[2])
        collapse_tech_sections(sys.argv[2])
    else:
        main_tex = patch()
        print(f"Patched manuscript written to {TMP}/")
        print(f"Entry point: {main_tex}")
