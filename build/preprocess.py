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

    # Load hover descriptions keyed by heading ID
    hover_map = {}
    yaml_path = REPO / "build" / "chapter-hover-descriptions.yaml"
    if yaml and yaml_path.exists():
        hover_map = yaml.safe_load(yaml_path.read_text()) or {}

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
        ops.append((h['start'], h['end'], ce, tooltip, h['full']))

    ops.sort(key=lambda o: o[0], reverse=True)
    for sec_start, head_end, content_end, tooltip, heading_html in ops:
        title_attr = f' title="{html_mod.escape(tooltip)}"' if tooltip else ''
        content = text[head_end:content_end]
        replacement = (
            f'<details class="chapter-section">'
            f'<summary{title_attr}>{heading_html}</summary>\n'
            f'{content}'
            f'</details>\n'
        )
        text = text[:sec_start] + replacement + text[content_end:]

    # (Global Expand All button moved to reader.js bottom nav bar — 6b)

    # === Wrap copyright block in collapsible details ===
    # The copyright/notices block is a <div class="flushleft"> between the
    # title block and the hook. It has no headings, so collapse_chapters skips it.
    flushleft_start = text.find('<div class="flushleft">')
    if flushleft_start != -1:
        # Find matching </div> (no nested divs in this block)
        flushleft_end = text.find('</div>', flushleft_start) + 6
        copyright_content = text[flushleft_start:flushleft_end]
        copyright_wrapped = (
            '<details class="chapter-section">'
            '<summary title="License, authorship, and draft status">'
            'Copyright &amp; Notices</summary>\n'
            + copyright_content +
            '\n</details>\n'
        )
        text = text[:flushleft_start] + copyright_wrapped + text[flushleft_end:]

    # === Pass 3: Title block, hook section, and Part-level wrapping ===

    # 3a-pre: Wrap title block in collapsible details (collapsed by default)
    tb_start = text.find('<div class="title-block">')
    tb_end = text.find('</div>', tb_start) + len('</div>') if tb_start != -1 else -1
    if tb_start != -1 and tb_end != -1:
        tb_content = text[tb_start:tb_end]
        text = (text[:tb_start] +
                '<details class="title-section">'
                '<summary>Relinquishment</summary>\n' +
                tb_content +
                '\n</details>\n' +
                text[tb_end:])

    # 3a: Hook section — wrap hook content
    # Find the hook h2 and wrap from there to the first chapter-section.
    hook_h2_match = re.search(r'<h2[^>]*id="hook:what-would-you-do"[^>]*>', text)
    first_chapter_after_hook = -1
    if hook_h2_match:
        first_chapter_after_hook = text.find('<details class="chapter-section">', hook_h2_match.end())
    if hook_h2_match and first_chapter_after_hook != -1:
        hook_start = hook_h2_match.start()
        hook_content = text[hook_start:first_chapter_after_hook]
        text = (text[:hook_start] +
                '<details class="hook-section">'
                '<summary>What Would You Do?</summary>\n' +
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
        if hid in {'guided-deduction', 'the-evidence-trail', 'agency-and-restraint'}:
            boundaries.append((m.start(), m.end(), m.group(0), hid))

    # Appendices boundary: chapter-section containing app:predictions
    app_pred_pos = text.find('id="app:predictions"')
    if app_pred_pos != -1:
        app_start = text.rfind('<details class="chapter-section">', 0, app_pred_pos)
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

    # 3c: Front Matter part-section — chapters between hook-section and first Part
    # Find closing </details> for hook-section by tracking nesting depth
    hook_section_start = text.find('<details class="hook-section">')
    hook_end = -1
    if hook_section_start != -1:
        depth = 0
        pos = hook_section_start
        while pos < len(text):
            if text[pos:pos+8] == '<details':
                depth += 1
            elif text[pos:pos+10] == '</details>':
                depth -= 1
                if depth == 0:
                    hook_end = pos + 10
                    break
            pos += 1
    if hook_end != -1:
        # Skip any whitespace after hook close
        while hook_end < len(text) and text[hook_end] in ' \t\n':
            hook_end += 1
        first_part = text.find('<details class="part-section">', hook_end)
        if first_part != -1:
            fm_region = text[hook_end:first_part]
            if '<details class="chapter-section">' in fm_region:
                fm_wrapped = (
                    '<details class="part-section">'
                    '<summary>Front Matter</summary>\n' +
                    fm_region +
                    '</details>\n'
                )
                text = text[:hook_end] + fm_wrapped + text[first_part:]

    part_count = text.count('<details class="part-section">')
    print(f"  Part-level: {part_count} parts, hook section wrapped")

    # 3d: Outer book wrapper — entire book behind one line
    # Wrap everything from title-section to last part-section closing tag
    book_start = text.find('<details class="title-section">')
    if book_start != -1:
        body_end = text.rfind('</body>')
        # Find the last </details> before </body> (the last part-section close)
        last_details_close = text.rfind('</details>', 0, body_end)
        if last_details_close != -1:
            wrap_end = last_details_close + len('</details>')
            book_content = text[book_start:wrap_end]
            text = (text[:book_start] +
                    '<details class="book-section">'
                    '<summary>Relinquishment '
                    '<span class="book-subtitle-inline">&mdash; '
                    'It is easier to get forgiveness than permission</span></summary>\n' +
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
  white-space: nowrap;
}
.book-subtitle-inline {
  font-size: 0.65em;
  font-weight: normal;
  font-style: italic;
  opacity: 0.7;
}

/* Level 0: Title section */
details.title-section {
  margin-bottom: 0.3em;
}
details.title-section > summary {
  font-size: 1.3em;
  font-weight: bold;
  padding: 0.2em 0;
}

/* Level 0: Hook section */
details.hook-section {
  margin-bottom: 0.3em;
}
details.hook-section > summary {
  font-size: 1.2em;
  font-weight: bold;
  padding: 0.2em 0;
}

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
details.chapter-section > summary > h2 { display: inline; }

/* Level 3: Internal (firmware sections, spiral abstracts) */
details.firmware-section,
details.spiral-abstract {
  border-left: 2px solid #ccc;
  padding-left: 0.8em;
  margin: 0.3em 0 0.3em 0.5em;
}
details.firmware-section > summary > h3,
details.spiral-abstract > summary > h3 { display: inline; }

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
    part_ids = {"guided-deduction", "the-evidence-trail", "agency-and-restraint"}

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
        r'<p><span><em>It is easier to get forgiveness than\s*'
        r'permission</em></span></p>\s*'
        r'<p><span>\s*Bruce Stephenson, Genevieve Prentice &amp; Argus</span></p>\s*'
        r'<p><span>\s*March 2026</span></p>\s*'
        r'</div>\s*'
        r'<div class="center">\s*'
        r'<p><span><strong>RELINQUISHMENT</strong></span></p>\s*'
        r'<p><span><em>It is easier to get forgiveness than\s*'
        r'permission</em></span></p>\s*'
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
    replacement = '''<div class="title-block">
<h1 class="book-title">Relinquishment</h1>
<p class="book-subtitle">It is easier to get forgiveness than permission</p>
<p class="book-authors">by Bruce Stephenson, Genevieve Prentice &amp; Argus</p>
<hr />
<p class="book-tagline"><em>Three narrative threads. Real science. Real people. Real institutions.</em></p>
<p class="book-tagline"><em>Three possible explanations for all of it. You decide.</em></p>
<p class="book-skip"><a href="#hook:what-would-you-do">Skip ahead to the story \u2192</a></p>
</div>'''
    text = re.sub(title_pattern, replacement, text, flags=re.DOTALL)

    # --- Fix 3: Collapse chapters into <details> elements ---
    text = collapse_chapters(text)

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
