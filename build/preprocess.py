#!/usr/bin/env python3
"""Patch manuscript for pandoc EPUB/HTML conversion.

Targeted fixes for 4 known pandoc issues. Does NOT concatenate files
or strip standard LaTeX — pandoc handles all of that natively.

Writes patched copy to build/epub-tmp/ for inspection.
"""

import shutil, re, sys, zipfile, io
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from collapsible import preprocess_tex

REPO = Path(__file__).parent.parent
TMP = REPO / "build" / "epub-tmp"


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

        # Fix 5: Collapsible content blocks → sentinels for pandoc
        text = preprocess_tex(text)

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
    else:
        main_tex = patch()
        print(f"Patched manuscript written to {TMP}/")
        print(f"Entry point: {main_tex}")
