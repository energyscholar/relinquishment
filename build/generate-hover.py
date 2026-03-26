#!/usr/bin/env python3
"""Generate hover-generated.tex from hover-definitions.yaml.

Reads YAML definitions, writes LaTeX macros using etoolbox's \\csdef.
The \\hovertip command renders italic + footnote on first occurrence,
italic-only on subsequent uses (\\csundef removes after first use).
"""

from pathlib import Path
import yaml

BUILD = Path(__file__).parent
YAML_PATH = BUILD / "hover-definitions.yaml"
OUT_PATH = BUILD / "hover-generated.tex"

defs = yaml.safe_load(YAML_PATH.read_text()) or {}

lines = [
    "% AUTO-GENERATED from build/hover-definitions.yaml — do not edit",
    "% Regenerate: python3 build/generate-hover.py",
    "\\usepackage{etoolbox}",
    "",
]

for term, definition in defs.items():
    # Escape LaTeX special chars in definitions
    safe_def = definition.replace("&", "\\&").replace("%", "\\%")
    lines.append(f"\\csdef{{hover@{term}}}{{{safe_def}}}")

lines.append("")
lines.append("% Italic + footnote on first occurrence; italic-only after")
lines.append("\\newcommand{\\hovertip}[1]{%")
lines.append("  \\textit{#1}%")
lines.append("  \\ifcsdef{hover@#1}{\\footnote{\\csuse{hover@#1}}\\csundef{hover@#1}}{}%")
lines.append("}")
lines.append("")

OUT_PATH.write_text("\n".join(lines))
print(f"Generated {OUT_PATH} with {len(defs)} definitions")
