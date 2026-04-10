#!/usr/bin/env python3
"""Patch manuscript for pandoc EPUB/HTML conversion.

Targeted fixes for 4 known pandoc issues. Does NOT concatenate files
or strip standard LaTeX — pandoc handles all of that natively.

Writes patched copy to build/epub-tmp/ for inspection.
"""

import shutil, re, sys, zipfile, io, html as html_mod
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

REPO = Path(__file__).parent.parent
TMP = REPO / "build" / "epub-tmp"


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
        'appendix:confession', 'appendix:the-unipolar-condition', 'appendix:guardian',
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
                """Return (escaped_html, target_attr, hover_id) for a title-line YAML entry."""
                entry = _title_hover_defs.get(yaml_key, {})
                if not isinstance(entry, dict) or 'html' not in entry:
                    print(f"  WARNING: title-line panel '{yaml_key}' missing from YAML or has no 'html' key")
                    return ('', '', yaml_key)
                raw_html = entry['html'].rstrip('\n')
                escaped = html_mod.escape(raw_html)
                target = entry.get('target', '')
                target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
                hover_id = entry.get('hover_id', yaml_key)
                return (escaped, target_attr, hover_id)

            demo_escaped, demo_target, demo_id = _title_panel_attrs('relinquishment-title')
            worm_escaped, worm_target, worm_id = _title_panel_attrs('wormholes-title')
            flat_escaped, flat_target, flat_id = _title_panel_attrs('the-flat-title')

            text = (text[:book_start] +
                    '<details class="book-section">'
                    f'<summary{book_title_attr}>'
                    f'<span class="hover-term hover-nav" data-hover="placeholder" '
                    f'data-hover-html="{demo_escaped}"{demo_target} data-hover-id="{demo_id}">'
                    'Relinquishment</span> '
                    '<span class="book-subtitle-inline">&mdash; '
                    f'<span class="hover-term hover-nav" data-hover="placeholder" '
                    f'data-hover-html="{worm_escaped}"{worm_target} data-hover-id="{worm_id}">'
                    'Wormholes</span> in '
                    f'<span class="hover-term hover-nav" data-hover="placeholder" '
                    f'data-hover-html="{flat_escaped}"{flat_target} data-hover-id="{flat_id}">'
                    'the Flat</span></span>'
                    '<div class="title-page-extra">'
                    '<p class="tp-authors">by Bruce Stephenson, Genevieve Prentice &amp; Argus</p>'
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

/* Guardian interludes (Plan 0143) */
.guardian-interlude {
  border-left: 3px solid #9b7db8;
  padding: 0.8em 1.2em;
  margin: 1.5em 0;
  line-height: 1.6;
  color: #444;
  background: rgba(155, 125, 184, 0.04);
}
.guardian-interlude::before {
  content: '';
  display: block;
  width: 3em;
  height: 1px;
  background: #9b7db8;
  margin-bottom: 0.5em;
  opacity: 0.5;
}

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
  .guardian-interlude {
    border-left-color: #7d5fa0;
    color: #bbb;
    background: rgba(155, 125, 184, 0.08);
  }
  .guardian-interlude::before {
    background: #7d5fa0;
  }
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
body.show-anchors .share-anchor::after { content: "🔗"; opacity: 0.3; margin-left: 0.3em; padding: 8px; }
body.show-anchors .share-anchor:hover::after { opacity: 0.8; }
@media print { .share-anchor::after { content: none; } }
@media (prefers-color-scheme: dark) {
  body.show-anchors .share-anchor::after { opacity: 0.25; }
  body.show-anchors .share-anchor:hover::after { opacity: 0.7; }
}
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

    eval_html = (
        '<div class="evaluate-section" id="evaluate-with-ai">\n'
        '<span id="how-to-evaluate"></span>\n'
        '<p><strong>Your AI doesn&#x27;t know enough to evaluate this book.</strong> '
        'It lacks five fields of cross-domain science. The fix takes thirty seconds. '
        'Copy the science upgrade below. Paste it into your AI. Then ask again.</p>\n'
        '<p>It&#x27;s a lot, so we do it in two prompts.</p>\n'
        '<button class="eval-step-1 hover-nav" data-eval-step="1"\n'
        '  data-hover="Paste this Science Firmware Update into your LLM to teach it the additional cross-domain science it needs to competently evaluate this book"\n'
        '  style="display:block;width:100%;padding:1em;font-size:1.1em;\n'
        '  margin:0.5em 0;cursor:pointer;background:#1a5276;color:#fff;\n'
        '  border:none;border-radius:6px;font-family:inherit;font-weight:bold;\n'
        '  min-height:60px;">\n'
        '  Copy Prompt 1 &#x2014; Science Firmware Upgrade\n'
        '</button>\n'
        '<p style="text-align:center;color:#888;font-size:0.9em;">Paste this first.</p>\n'
        '<button class="eval-step-2 hover-nav" data-eval-step="2"\n'
        '  data-hover="These Spiral Abstracts tell the entire story of this book, all the scientific and technical details, without any personal details. Read it or paste it into an LLM"\n'
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
        "corrections-and-concessions", "summary:most-important-story",
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
        r'<p><span>Written by Bruce Stephenson, Genevieve Prentice &amp;\s*'
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
        hover_seen = set()
        # Title-line rich panels (Relinquishment, Wormholes, the Flat) already
        # rendered as hover-term spans — register their body-equivalent keys
        # so first-occurrence tracking prevents duplicate hovertips downstream.
        hover_seen.update(['relinquishment', 'wormholes'])
        hover_count = 0

        def hover_replace(m):
            nonlocal hover_count
            raw_term = m.group(1)
            # Pandoc may insert newlines in multi-word terms; normalize for lookup
            term = re.sub(r'\s+', ' ', raw_term).strip()
            lookup = term.lower().replace('\u2019', "'").replace('\u2018', "'")
            if lookup in hover_lower and lookup not in hover_seen:
                hover_seen.add(lookup)
                hover_count += 1
                value = hover_lower[lookup]
                # Extended YAML: object with text + target, or plain string
                if isinstance(value, dict):
                    escaped_def = html_mod.escape(value.get('text', ''))
                    target = value.get('target', '')
                    target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
                    rich_html = value.get('html', '').rstrip('\n')
                    html_attr = f' data-hover-html="{html_mod.escape(rich_html)}"' if rich_html else ''
                else:
                    escaped_def = html_mod.escape(str(value))
                    target_attr = ''
                    html_attr = ''
                hover_id = re.sub(r'[^a-z0-9]+', '-', lookup).strip('-')
                return f'<span class="hover-term" data-hover="{escaped_def}"{target_attr}{html_attr} data-hover-id="{hover_id}">{term}</span>'
            elif lookup in hover_lower:
                return f'<em>{term}</em>'
            else:
                print(f"  WARNING: hovertip term not in YAML: '{term}'")
                return f'<em>{term}</em>'

        text = re.sub(r'HOVERSTART\u00a7(.+?)\u00a7HOVEREND', hover_replace, text, flags=re.DOTALL)
        if hover_count:
            print(f"Hover tooltips: {hover_count} first-occurrence terms")

    # --- Guardian interludes: convert <hr> <blockquote> <hr> pattern ---
    # to <div class="guardian-interlude"> (Plan 0143)
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
        return f'<div class="guardian-interlude">{content}</div>'

    text = interlude_pattern.sub(interlude_replace, text)
    if interlude_count:
        print(f"  Guardian interludes: {interlude_count} styled")

    # --- B/C expansion hooks — injected by chapter ID (Plan 0143d) ---
    bc_hooks = {
        'spine:code-war': {
            'summary': 'According to this story, there was a team that faced exactly this choice...',
            'body': 'Five scientists, each expert in a different field, were brought together '
                    'under DARPA classification circa 1990. What they built, if the account '
                    'is true, was the most dangerous dual-use technology in human history \u2014 '
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
                    'According to this story, they grew a Guardian around the Universal Declaration '
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
                            escaped = html_mod.escape(str(stack_defs[key]))
                            old_th = f'>{label}</th>'
                            new_th = f'><span class="hover-term" data-hover="{escaped}" data-hover-id="{key}">{label}</span></th>'
                            if old_th in new_table:
                                new_table = new_table.replace(old_th, new_th, 1)
                                stack_count += 1

                    # Wrap the "?" column header (inside <strong>)
                    if 'stack-question-mark' in stack_defs:
                        escaped = html_mod.escape(str(stack_defs['stack-question-mark']))
                        old_q = '><strong>?</strong></th>'
                        new_q = f'><span class="hover-term" data-hover="{escaped}" data-hover-id="stack-question-mark"><strong>?</strong></span></th>'
                        if old_q in new_table:
                            new_table = new_table.replace(old_q, new_q, 1)
                            stack_count += 1

                    # Wrap row labels (first <td> in each row)
                    for label, key in stack_row_map.items():
                        if key in stack_defs:
                            escaped = html_mod.escape(str(stack_defs[key]))
                            old_td = f'>{label}</td>'
                            new_td = f'><span class="hover-term" data-hover="{escaped}" data-hover-id="{key}">{label}</span></td>'
                            if old_td in new_table:
                                new_table = new_table.replace(old_td, new_td, 1)
                                stack_count += 1

                    # Wrap "Wormholes†" row label
                    if 'stack-wormholes' in stack_defs:
                        escaped = html_mod.escape(str(stack_defs['stack-wormholes']))
                        old_w = '>Wormholes†</td>'
                        new_w = f'><span class="hover-term" data-hover="{escaped}" data-hover-id="stack-wormholes">Wormholes†</span></td>'
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
        # Convert title on <a> tags to data-hover
        def convert_a_title(m):
            nonlocal title_conv_count
            tag = m.group(0)
            title_match = re.search(r' title="([^"]*)"', tag)
            if not title_match:
                return tag
            title_val = title_match.group(1)
            tag = tag.replace(title_match.group(0), '')  # remove title
            tag = tag.replace('>', f' data-hover="{title_val}">', 1)  # add data-hover
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
            tag = tag.replace(title_match.group(0), '')
            tag = tag.replace('>', f' data-hover="{title_val}">', 1)
            if 'class="' in tag:
                tag = tag.replace('class="', 'class="hover-nav ')
            else:
                tag = tag.replace('>', ' class="hover-nav">', 1)
            title_conv_count += 1
            return tag
        new_toc = re.sub(r'<span [^>]*title="[^"]*"[^>]*>', convert_span_title, new_toc)

        text = text.replace(toc_block, new_toc)

    # Convert title on accordion <summary> elements (chapter-hover-descriptions)
    def convert_summary_title(m):
        nonlocal title_conv_count
        tag = m.group(0)
        title_match = re.search(r' title="([^"]*)"', tag)
        if not title_match:
            return tag
        title_val = title_match.group(1)
        tag = tag.replace(title_match.group(0), '')
        tag = tag.replace('>', f' data-hover="{title_val}">', 1)
        if 'class="' in tag:
            tag = tag.replace('class="', 'class="hover-nav ')
        else:
            tag = tag.replace('>', ' class="hover-nav">', 1)
        title_conv_count += 1
        return tag
    text = re.sub(r'<summary [^>]*title="[^"]*"[^>]*>', convert_summary_title, text)

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

    html_path.write_text(text)
    print(f"HTML post-processed: {html_path}")


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
    else:
        main_tex = patch()
        print(f"Patched manuscript written to {TMP}/")
        print(f"Entry point: {main_tex}")
