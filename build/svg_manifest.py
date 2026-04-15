#!/usr/bin/env python3
"""
Plan 0196 Phase A — SVG-and-orphan manifest generator.

Read-only analysis. Emits:
  build/svg-manifest.json
  build/svg-sheet.html
  build/orphan-report.md

Run from repo root.
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
BUILD = REPO / "build"
IMG = BUILD / "images"
MANUSCRIPT = REPO / "manuscript"

SVG_BLOCK_RE = re.compile(r"<svg\b[^>]*>.*?</svg>", re.DOTALL | re.IGNORECASE)
SVG_ELEM_RE = re.compile(r"<([a-zA-Z][a-zA-Z0-9]*)\b")
DEFS_RE = re.compile(r"<defs\b[^>]*>(.*?)</defs>", re.DOTALL | re.IGNORECASE)
GRAD_ID_RE = re.compile(r'id\s*=\s*["\']([^"\']+)["\']')


@dataclass
class SvgAsset:
    asset_id: str
    kind: str  # "standalone-file" | "inline-yaml" | "inline-tex"
    source: str  # path or "path#key"
    location: str  # e.g. "build/images/foo.svg" or "build/hover-definitions.yaml:the-flat-title"
    bytes: int
    element_count: int
    defs_ids: list[str] = field(default_factory=list)
    used_by: list[str] = field(default_factory=list)
    status: str = "unknown"  # applied / orphaned / source-for-derived / unreferenced / referenced-but-target-missing
    notes: str = ""


# ------------------------------------------------------------------ scanning

def scan_standalone_svgs() -> list[SvgAsset]:
    assets: list[SvgAsset] = []
    if not IMG.exists():
        return assets
    for p in sorted(IMG.glob("*.svg")):
        txt = p.read_text(encoding="utf-8", errors="replace")
        assets.append(SvgAsset(
            asset_id=p.stem,
            kind="standalone-file",
            source=str(p.relative_to(REPO)),
            location=str(p.relative_to(REPO)),
            bytes=len(txt.encode("utf-8")),
            element_count=len(SVG_ELEM_RE.findall(txt)),
            defs_ids=extract_defs_ids(txt),
        ))
    return assets


def extract_defs_ids(svg_text: str) -> list[str]:
    ids: list[str] = []
    for defs in DEFS_RE.findall(svg_text):
        ids.extend(GRAD_ID_RE.findall(defs))
    return ids


def scan_inline_yaml_svgs(yaml_path: Path, hover_entries: dict) -> list[SvgAsset]:
    assets: list[SvgAsset] = []
    for key, val in hover_entries.items():
        if not isinstance(val, dict):
            continue
        html = val.get("html") or ""
        if not html:
            continue
        for idx, match in enumerate(SVG_BLOCK_RE.finditer(html)):
            body = match.group(0)
            aid = key if idx == 0 else f"{key}#{idx}"
            assets.append(SvgAsset(
                asset_id=aid,
                kind="inline-yaml",
                source=f"{yaml_path.relative_to(REPO)}:{key}",
                location=f"{yaml_path.relative_to(REPO)}:{key}",
                bytes=len(body.encode("utf-8")),
                element_count=len(SVG_ELEM_RE.findall(body)),
                defs_ids=extract_defs_ids(body),
            ))
    return assets


def scan_inline_tex_svgs() -> list[SvgAsset]:
    assets: list[SvgAsset] = []
    for p in MANUSCRIPT.rglob("*.tex"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        for idx, match in enumerate(SVG_BLOCK_RE.finditer(txt)):
            body = match.group(0)
            assets.append(SvgAsset(
                asset_id=f"{p.stem}#svg{idx}",
                kind="inline-tex",
                source=str(p.relative_to(REPO)),
                location=f"{p.relative_to(REPO)}",
                bytes=len(body.encode("utf-8")),
                element_count=len(SVG_ELEM_RE.findall(body)),
                defs_ids=extract_defs_ids(body),
            ))
    return assets


# ------------------------------------------------------------------ usage map

def build_usage_index() -> dict[str, list[str]]:
    """Map of token -> list of source locations referencing it."""
    idx: dict[str, list[str]] = {}

    def add(token: str, where: str):
        idx.setdefault(token, []).append(where)

    # hovertip / hovertiphtml macros in manuscript
    hover_call_re = re.compile(r"\\hovertip(?:html)?\*?\{([^}]+)\}")
    for p in MANUSCRIPT.rglob("*.tex"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        rel = str(p.relative_to(REPO))
        for m in hover_call_re.finditer(txt):
            add(m.group(1).strip(), f"{rel}:\\hovertip")

    # preprocess.py references
    pre = (BUILD / "preprocess.py").read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r'["\']hover_id["\']\s*:\s*["\']([^"\']+)["\']', pre):
        add(m.group(1), "build/preprocess.py:hover_id")
    # _title_panel_attrs('key') — single OR double quotes
    for m in re.finditer(r"_title_panel_attrs\(\s*['\"]([^'\"]+)['\"]", pre):
        add(m.group(1), "build/preprocess.py:_title_panel_attrs")

    # hover-generated.tex : every \csdef{hover@KEY} proves the yaml entry was
    # emitted through the first-occurrence machinery (preprocess.py scans
    # yaml keys against rendered prose and injects csdef at compile time).
    hg = BUILD / "hover-generated.tex"
    if hg.exists():
        for m in re.finditer(r"\\csdef\{hover@([^}]+)\}", hg.read_text(encoding="utf-8", errors="replace")):
            add(m.group(1), "build/hover-generated.tex:\\csdef")

    # chapter-hover + menu-tooltips yaml — anything referencing hover keys
    for fname in ("chapter-hover-descriptions.yaml", "menu-tooltips.yaml"):
        fp = BUILD / fname
        if not fp.exists():
            continue
        raw = fp.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"hover_id\s*:\s*['\"]?([A-Za-z0-9_\-:]+)", raw):
            add(m.group(1), f"build/{fname}:hover_id")

    # standalone-image references (pdf/png/svg) in tex and preprocess
    img_re = re.compile(r"images/([A-Za-z0-9_\-]+)\.(pdf|png|svg|jpg|jpeg)")
    for p in MANUSCRIPT.rglob("*.tex"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        rel = str(p.relative_to(REPO))
        for m in img_re.finditer(txt):
            add(m.group(1), rel)
    for m in img_re.finditer(pre):
        add(m.group(1), "build/preprocess.py")

    return idx


# ------------------------------------------------------------------ status

def classify(asset: SvgAsset, usage: dict[str, list[str]]) -> None:
    if asset.kind == "standalone-file":
        stem = asset.asset_id
        # standalone SVG → may be a source for derived PDF/PNG used in prose
        derived_used = bool(usage.get(stem))
        sibling_pdf = (IMG / f"{stem}.pdf").exists()
        sibling_png = (IMG / f"{stem}.png").exists()
        if derived_used and (sibling_pdf or sibling_png):
            asset.status = "source-for-derived"
            asset.used_by = usage.get(stem, [])
            asset.notes = "SVG is source for PDF/PNG applied in manuscript."
        elif derived_used:
            asset.status = "applied"
            asset.used_by = usage.get(stem, [])
        else:
            asset.status = "orphaned"
            asset.notes = "No references found anywhere."
    elif asset.kind == "inline-yaml":
        # asset_id like "the-flat-title" or "the-flat-title#1"
        key = asset.asset_id.split("#")[0]
        refs = usage.get(key, [])
        asset.used_by = refs
        asset.status = "applied" if refs else "unreferenced"
        if not refs:
            asset.notes = "yaml entry not referenced by any \\hovertip or hover_id."
    elif asset.kind == "inline-tex":
        asset.status = "applied"
        asset.used_by = [asset.source]


# ------------------------------------------------------------------ orphan report

def orphan_report(hover_entries: dict, usage: dict[str, list[str]]) -> str:
    lines: list[str] = []
    lines.append("# Plan 0196 Phase A — Orphan Report")
    lines.append("")
    lines.append("Read-only inventory of authored-but-possibly-unapplied content.")
    lines.append("")

    # yaml entries with no referencing hover call
    lines.append("## Orphaned hover-definitions.yaml entries")
    lines.append("")
    orph_yaml = []
    for key, val in hover_entries.items():
        if not isinstance(val, (dict, str)):
            continue
        # skip aliases-to-be and doc entries
        if isinstance(val, dict) and val.get("alias_of"):
            continue
        refs = usage.get(key, [])
        if not refs:
            orph_yaml.append(key)
    if not orph_yaml:
        lines.append("_None found._")
    else:
        lines.append(f"{len(orph_yaml)} entries with no \\hovertip / hover_id reference:")
        lines.append("")
        for k in sorted(orph_yaml):
            lines.append(f"- `{k}`")
    lines.append("")

    # test HTML files in build/
    lines.append("## Test HTML files in build/")
    lines.append("")
    test_htmls = sorted(BUILD.glob("test-*.html")) + sorted(BUILD.glob("*-test.html"))
    if not test_htmls:
        lines.append("_None found._")
    else:
        for p in test_htmls:
            lines.append(f"- `{p.relative_to(REPO)}` ({p.stat().st_size} bytes)")
    lines.append("")

    # .tex files not reachable via \input/\include from main.tex
    lines.append("## Manuscript .tex files not reachable via \\input/\\include from main.tex")
    lines.append("")
    reachable = set()

    def walk_inputs(tex_path: Path):
        if not tex_path.exists():
            return
        rel = str(tex_path.relative_to(REPO))
        if rel in reachable:
            return
        reachable.add(rel)
        txt = tex_path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\\(?:input|include|subfile)\{([^}]+)\}", txt):
            target = m.group(1).strip()
            candidates = [
                REPO / (target if target.endswith(".tex") else target + ".tex"),
                tex_path.parent / (target if target.endswith(".tex") else target + ".tex"),
            ]
            for c in candidates:
                if c.exists():
                    walk_inputs(c)
                    break

    walk_inputs(REPO / "main.tex")

    all_tex = {str(p.relative_to(REPO)) for p in MANUSCRIPT.rglob("*.tex")}
    unreachable = sorted(all_tex - reachable)
    if not unreachable:
        lines.append("_All manuscript .tex reachable._")
    else:
        lines.append(f"{len(unreachable)} manuscript .tex not reachable via `\\input`/`\\include` from `main.tex`, "
                     "and not referenced by name in `build/preprocess.py`. Grouped by directory:")
        lines.append("")
        by_dir: dict[str, list[str]] = {}
        for f in unreachable:
            top = "/".join(f.split("/")[:2])  # manuscript/<subdir>
            by_dir.setdefault(top, []).append(f)
        for top in sorted(by_dir):
            lines.append(f"### {top}/ ({len(by_dir[top])})")
            lines.append("")
            for f in by_dir[top]:
                lines.append(f"- `{f}`")
            lines.append("")

    return "\n".join(lines)


# ------------------------------------------------------------------ visual sheet

def render_sheet(assets: list[SvgAsset]) -> str:
    by_status: dict[str, list[SvgAsset]] = {}
    for a in assets:
        by_status.setdefault(a.status, []).append(a)

    sections: list[str] = []
    order = ["orphaned", "unreferenced", "source-for-derived", "applied"]
    for status in order + [s for s in by_status if s not in order]:
        items = by_status.get(status, [])
        if not items:
            continue
        sections.append(f"<h2>{status} ({len(items)})</h2>")
        sections.append('<div class="grid">')
        for a in items:
            svg_preview = svg_preview_for(a)
            used = "<br>".join(a.used_by) if a.used_by else "<em>(none)</em>"
            sections.append(f"""
<div class="card">
  <div class="svg-box">{svg_preview}</div>
  <div class="meta">
    <div class="id">{escape(a.asset_id)}</div>
    <div class="kind">{a.kind}</div>
    <div class="src">{escape(a.location)}</div>
    <div class="stats">{a.bytes} bytes · {a.element_count} elements</div>
    <div class="used"><strong>Used by:</strong><br>{escape_multiline(used)}</div>
    {'<div class="notes">'+escape(a.notes)+'</div>' if a.notes else ''}
  </div>
</div>
""")
        sections.append("</div>")

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Plan 0196 Phase A — SVG Sheet</title>
<style>
body {{ font: 14px/1.4 system-ui, sans-serif; max-width: 1400px; margin: 2em auto; padding: 0 1em; }}
h1 {{ border-bottom: 2px solid #333; }}
h2 {{ margin-top: 2em; border-bottom: 1px dashed #888; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 1em; }}
.card {{ border: 1px solid #ccc; border-radius: 6px; padding: 0.7em; background: #fafafa; }}
.svg-box {{ background: #fff; border: 1px dashed #ddd; min-height: 160px; max-height: 280px;
            overflow: hidden; display: flex; align-items: center; justify-content: center; padding: 0.3em; }}
.svg-box svg {{ max-width: 100%; max-height: 260px; height: auto; width: auto; }}
.meta {{ margin-top: 0.6em; font-size: 0.85em; }}
.id {{ font-family: monospace; font-weight: bold; word-break: break-all; }}
.kind {{ color: #666; font-size: 0.8em; }}
.src {{ color: #888; font-family: monospace; font-size: 0.75em; word-break: break-all; }}
.stats {{ color: #555; margin-top: 0.3em; }}
.used {{ margin-top: 0.3em; font-size: 0.8em; }}
.notes {{ margin-top: 0.3em; font-style: italic; color: #a33; }}
</style></head>
<body>
<h1>Plan 0196 Phase A — SVG + Orphan Manifest</h1>
<p>Analysis artifact. Not shipped. Never deployed to <code>docs/</code>.</p>
<p>Total assets scanned: <strong>{len(assets)}</strong>.</p>
{''.join(sections)}
</body></html>
"""


def svg_preview_for(a: SvgAsset) -> str:
    try:
        if a.kind == "standalone-file":
            p = REPO / a.location
            return p.read_text(encoding="utf-8", errors="replace")
        if a.kind == "inline-yaml":
            key = a.asset_id.split("#")[0]
            yaml_path = BUILD / "hover-definitions.yaml"
            data = yaml.safe_load(yaml_path.read_text())
            entry = data.get(key)
            if isinstance(entry, dict):
                html = entry.get("html", "")
                matches = list(SVG_BLOCK_RE.finditer(html))
                idx = 0
                if "#" in a.asset_id:
                    idx = int(a.asset_id.rsplit("#", 1)[1])
                if idx < len(matches):
                    return matches[idx].group(0)
        if a.kind == "inline-tex":
            p = REPO / a.source
            txt = p.read_text(encoding="utf-8", errors="replace")
            idx = int(a.asset_id.rsplit("#svg", 1)[1])
            matches = list(SVG_BLOCK_RE.finditer(txt))
            if idx < len(matches):
                return matches[idx].group(0)
    except Exception as e:
        return f"<em>preview error: {escape(str(e))}</em>"
    return "<em>(no preview)</em>"


def escape(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def escape_multiline(s: str) -> str:
    # already-escaped HTML from used_by join — but we want to allow <br>.
    # The used_by list items are plain strings; escape them then re-insert <br>.
    parts = s.split("<br>")
    return "<br>".join(escape(p) for p in parts)


# ------------------------------------------------------------------ main

def main() -> int:
    hover_path = BUILD / "hover-definitions.yaml"
    hover_entries = yaml.safe_load(hover_path.read_text(encoding="utf-8")) or {}

    usage = build_usage_index()

    assets: list[SvgAsset] = []
    assets.extend(scan_standalone_svgs())
    assets.extend(scan_inline_yaml_svgs(hover_path, hover_entries))
    assets.extend(scan_inline_tex_svgs())

    for a in assets:
        classify(a, usage)

    # write json
    manifest = {
        "plan": "0196 Phase A",
        "total": len(assets),
        "by_status": {s: sum(1 for a in assets if a.status == s)
                      for s in sorted({a.status for a in assets})},
        "by_kind": {k: sum(1 for a in assets if a.kind == k)
                    for k in sorted({a.kind for a in assets})},
        "assets": [asdict(a) for a in assets],
    }
    (BUILD / "svg-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=False), encoding="utf-8"
    )

    # write visual sheet
    (BUILD / "svg-sheet.html").write_text(render_sheet(assets), encoding="utf-8")

    # orphan report
    (BUILD / "orphan-report.md").write_text(
        orphan_report(hover_entries, usage), encoding="utf-8"
    )

    # self-consistency: every used_by entry resolves to a real file
    problems: list[str] = []
    for a in assets:
        for u in a.used_by:
            path_part = u.split(":")[0]
            if not (REPO / path_part).exists():
                problems.append(f"{a.asset_id}: used_by {u} -> missing file")
    if problems:
        print("SELF-CONSISTENCY WARNINGS:")
        for p in problems:
            print(" ", p)

    print(f"Wrote {BUILD/'svg-manifest.json'}")
    print(f"Wrote {BUILD/'svg-sheet.html'}")
    print(f"Wrote {BUILD/'orphan-report.md'}")
    print(f"Total assets: {len(assets)}")
    for status, n in manifest["by_status"].items():
        print(f"  {status}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
