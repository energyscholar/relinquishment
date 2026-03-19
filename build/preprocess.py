#!/usr/bin/env python3
"""Patch manuscript for pandoc EPUB/HTML conversion.

Targeted fixes for 4 known pandoc issues. Does NOT concatenate files
or strip standard LaTeX — pandoc handles all of that natively.

Writes patched copy to build/epub-tmp/ for inspection.
"""

import shutil, re, sys, zipfile, io
from pathlib import Path

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


def fix_html_toc(html_path):
    """Post-process HTML to restructure flat TOC into part-grouped TOC.

    Pandoc with --toc-depth=2 nests chapters under parts, but:
    - Front matter items float at top level without a group header
    - Appendices and back matter are lumped under the last part
    - Part entries are clickable links (should be visual group headers)

    This restructures the TOC with Front Matter, Part, Appendices, and
    Back Matter groupings, with parts as non-clickable headers.
    """
    html_path = Path(html_path)
    text = html_path.read_text()

    # Extract the TOC nav block
    toc_match = re.search(r'<nav id="TOC"[^>]*>(.+?)</nav>', text, re.DOTALL)
    if not toc_match:
        print("WARNING: No TOC found in HTML, skipping TOC fix")
        return

    # Part IDs — these become non-clickable group headers
    part_ids = {"the-story", "the-investigation", "the-interpretation"}

    # Appendix IDs (from \appendix section in main.tex)
    appendix_ids = {"app:predictions", "app:abstracts", "app:glossary", "app:dms-note"}

    # Back matter IDs (from \backmatter section in main.tex)
    backmatter_ids = {
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
    back_items = []
    for child in last_children:
        href_match = re.search(r'href="#([^"]+)"', child)
        child_id = href_match.group(1) if href_match else ""
        if child_id in appendix_ids:
            appendix_items.append(child)
        elif child_id in backmatter_ids:
            back_items.append(child)
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

    # Appendices
    if appendix_items:
        new_toc_items.append(make_group("Appendices", appendix_items))

    # Back Matter
    if back_items:
        new_toc_items.append(make_group("Back Matter", back_items))

    new_toc = '<nav id="TOC" role="doc-toc">\n<ul>\n'
    new_toc += "\n".join(new_toc_items)
    new_toc += "\n</ul>\n</nav>"

    # Replace the old TOC
    text = text[:toc_match.start()] + new_toc + text[toc_match.end():]

    html_path.write_text(text)
    print(f"HTML TOC restructured: {html_path}")


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
