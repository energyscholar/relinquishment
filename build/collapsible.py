#!/usr/bin/env python3
"""Collapsible Content Protocol — build module.

Single source of truth for the cross-format collapsible content system.
Imported by preprocess.py (LaTeX → sentinel) and postprocess-html.py (sentinel → HTML5).

Design: Adapter Pattern — one content interface, format-specific renderers.
Protocol: plans/0098-collapsible-content.md
"""

import re
from pathlib import Path

# --- Protocol constants (change here, both pipelines update) ---
SENTINEL_PREFIX = "CLPS"
SENTINEL_DELIM = ":"
CSS_CLASS = "collapsible"
BUTTON_TEXT = "Show\u2009/\u2009Hide"  # thin spaces around slash

# --- LaTeX sentinel patterns ---
_TEX_BEGIN = re.compile(
    r"\\begin\{collapsible\}"
    r"(?:\[(\w+)\])?"       # optional [open] or [closed]; group 1
    r"\{([^}]+)\}"          # {Label Text}; group 2
)
_TEX_END = re.compile(r"\\end\{collapsible\}")

# --- HTML sentinel patterns (match pandoc output) ---
# Pandoc wraps \textbf{...} in <p><strong>...</strong></p>
_HTML_BEGIN = re.compile(
    r"<p><strong>"
    + re.escape(SENTINEL_PREFIX) + re.escape(SENTINEL_DELIM)
    + r"(\w+)"              # state; group 1
    + re.escape(SENTINEL_DELIM)
    + r"(.+?)"              # label (non-greedy — handles smart quotes); group 2
    + r"</strong></p>"
)
_HTML_END = re.compile(
    r"<p><strong>"
    + re.escape(SENTINEL_PREFIX) + re.escape(SENTINEL_DELIM)
    + r"END</strong></p>"
)


def preprocess_tex(text: str) -> str:
    r"""Convert \begin{collapsible} to sentinels for pandoc passthrough.

    \begin{collapsible}[closed]{Label} → \textbf{CLPS:closed:Label}
    \end{collapsible}                  → \textbf{CLPS:END}

    Sentinels use COLONS (not underscores — _ is math-mode-only in LaTeX).
    """
    def _begin(m):
        state = m.group(1) or "closed"
        label = m.group(2)
        return (
            f"\n\\textbf{{{SENTINEL_PREFIX}{SENTINEL_DELIM}"
            f"{state}{SENTINEL_DELIM}{label}}}\n"
        )

    text = _TEX_BEGIN.sub(_begin, text)
    text = _TEX_END.sub(
        f"\n\\\\textbf{{{SENTINEL_PREFIX}{SENTINEL_DELIM}END}}\n", text
    )
    return text


def postprocess_html(html_path: str) -> None:
    """Upgrade sentinel <strong> tags to HTML5 <details><summary>.

    Reads, transforms, and overwrites the file in place.
    Strips surrounding <p> tags to prevent orphaned elements.
    Warns if any unconverted sentinels remain.
    """
    path = Path(html_path)
    text = path.read_text(encoding="utf-8")
    count = 0

    def _begin(m):
        nonlocal count
        count += 1
        state = m.group(1)
        label = m.group(2)
        open_attr = " open" if state == "open" else ""
        return (
            f'<details class="{CSS_CLASS}"{open_attr}>\n'
            f"<summary>{BUTTON_TEXT} {label}</summary>"
        )

    text = _HTML_BEGIN.sub(_begin, text)
    text = _HTML_END.sub("</details>", text)

    # Safety check
    remaining = text.count(f"{SENTINEL_PREFIX}{SENTINEL_DELIM}")
    if remaining > 0:
        print(
            f"WARNING: {remaining} unconverted collapsible sentinel(s) "
            f"in {html_path}"
        )

    path.write_text(text, encoding="utf-8")
    print(f"Collapsible: {count} block(s) converted in {path.name}")
