#!/usr/bin/env python3
"""Manifest-driven SVG gallery generator.
Reads build/gallery-manifest.yaml and resolves SVGs from all sources.
Run: python3 build/generate-gallery.py
Development tool — not part of the Makefile pipeline."""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")


CATEGORY_ORDER = [
    'Title & Branding',
    'Cover / Navigation',
    'The Flat / 2DEG',
    'Topology & Wormholes',
    'Magnetosphere',
    'Magnetosphere Teaching',
    'The Stack / Convergence',
    'Kauffman Filmstrip',
    'Genesis Illustrations',
    'Physics Concepts',
    'Standalone Files',
    'Argument / Silence Gap',
    'Argument / Tradecraft',
    'Argument / Convergence',
    'Argument / Relinquishment',
]

NAME_TO_VAR = {
    'domain-buttons-chapter': 'DOMAIN_SVG',
    'flat-diagram-chapter': 'FLAT_SVG',
    'autocatalytic-loop': 'AUTOCATALYTIC_LOOP',
    'edge-of-chaos-inline': 'EDGE_OF_CHAOS',
    'substrate-parallel': 'SUBSTRATE_PARALLEL',
    'canopy-problem': 'CANOPY_PROBLEM',
    'ms-earth-teaching': 'EARTH_MS_SVG',
    'ms-jupiter-teaching': 'JUPITER_MS_SVG',
    'ms-saturn-teaching': 'SATURN_MS_SVG',
}


def load_hover_svgs():
    """Return {hover_key: svg_string} from hover-definitions.yaml."""
    path = REPO / 'build' / 'hover-definitions.yaml'
    data = yaml.safe_load(path.read_text())
    result = {}
    for key, val in data.items():
        if not isinstance(val, dict):
            continue
        html = val.get('html', '')
        m = re.search(r'(<svg[\s\S]*?</svg>)', html)
        if m:
            result[key] = m.group(1)
    return result


def load_preprocess_svgs():
    """Return {var_name: svg_string} and filmstrip panels list."""
    source = (REPO / 'build' / 'preprocess.py').read_text()
    var_svgs = {}
    for varname in ['FLAT_SVG', 'DOMAIN_SVG', 'AUTOCATALYTIC_LOOP',
                     'EDGE_OF_CHAOS', 'SUBSTRATE_PARALLEL', 'CANOPY_PROBLEM',
                     'EARTH_MS_SVG', 'JUPITER_MS_SVG', 'SATURN_MS_SVG']:
        m = re.search(rf"{varname}\s*=\s*'''(.*?)'''", source, re.DOTALL)
        if m:
            svg_m = re.search(r'(<svg[\s\S]*?</svg>)', m.group(1))
            if svg_m:
                var_svgs[varname] = svg_m.group(1)
    filmstrip = generate_filmstrip_panels()
    return var_svgs, filmstrip


def resolve_svg(entry, hover_svgs, var_svgs, filmstrip_panels):
    """Given a manifest entry, return (svg_string, placeholder_reason)."""
    source = entry.get('source', '')
    name = entry.get('name', '')

    if source == 'hover-definitions.yaml':
        for term in entry.get('terms', []):
            if term in hover_svgs:
                return hover_svgs[term], None
        return None, 'hover term not found'

    if source == 'preprocess.py':
        if name.startswith('filmstrip-panel-'):
            idx = int(name.split('-')[2]) - 1
            if 0 <= idx < len(filmstrip_panels):
                return filmstrip_panels[idx], None
            return None, f'filmstrip index {idx} out of range'
        var = NAME_TO_VAR.get(name)
        if var and var in var_svgs:
            return var_svgs[var], None
        return None, f'variable {var or name} not found'

    if source.startswith('build/images/'):
        path = REPO / source
        if path.exists():
            svg = path.read_text()
            svg = re.sub(r'<\?xml[^?]*\?>\s*', '', svg)
            return svg.strip(), None
        return None, f'file not found: {source}'

    if source == 'reader.js':
        return None, 'Constructed dynamically in reader.js — view in book'

    if source == 'gallery':
        return None, 'Designed — awaiting SVG build'

    return None, f'unknown source: {source}'


def render_card(entry, svg_string, placeholder_reason):
    """Return HTML for one gallery card."""
    eid = entry.get('id', '???')
    name = entry.get('name', '')
    status = entry.get('status', 'live')

    badges = f'<span class="status-badge status-{status}">{status.upper()}</span>'
    if entry.get('animated'):
        badges += '<span class="animated-badge">ANIMATED</span>'

    meta_lines = []
    meta_lines.append(f'<div class="meta-row"><span class="label">Source:</span> {entry.get("source", "—")}</div>')

    chapter = entry.get('chapter', '')
    fig = entry.get('figure_id', '')
    if chapter or fig:
        parts = []
        if chapter:
            parts.append(f'<span class="label">Chapter:</span> {chapter}')
        if fig:
            parts.append(f'<span class="label">Figure:</span> <code>{fig}</code>')
        meta_lines.append(f'<div class="meta-row">{" · ".join(parts)}</div>')

    marker = entry.get('marker', '')
    if marker:
        meta_lines.append(f'<div class="meta-row"><span class="label">Marker:</span> <code>{marker}</code></div>')

    desc = entry.get('description', '')
    if desc:
        meta_lines.append(f'<div class="meta-row"><span class="label">Description:</span> {desc}</div>')

    if entry.get('animated'):
        aplan = entry.get('animation_plan', '')
        anim = entry.get('animation', '')
        atext = ''
        if aplan:
            atext += f'Plan {aplan}'
        if anim:
            atext += f' — {anim}' if atext else anim
        if atext:
            meta_lines.append(f'<div class="meta-row"><span class="label">Animation:</span> {atext}</div>')

    terms = entry.get('terms', [])
    if terms:
        terms_html = ', '.join(f'<code>{t}</code>' for t in terms)
        meta_lines.append(f'<div class="meta-row"><span class="label">Terms:</span> {terms_html}</div>')

    seq_group = entry.get('sequence_group', '')
    seq_order = entry.get('sequence_order', '')
    if seq_group:
        meta_lines.append(f'<div class="meta-row"><span class="label">Sequence:</span> {seq_group} #{seq_order}</div>')

    display_val = entry.get('display', '')
    targets = entry.get('targets', [])
    plan = entry.get('plan', '')
    if display_val or targets or plan:
        parts = []
        if display_val:
            parts.append(f'<span class="label">Display:</span> {display_val}')
        if targets:
            parts.append(f'<span class="label">Targets:</span> {", ".join(targets)}')
        if plan:
            parts.append(f'<span class="label">Plan:</span> {plan}')
        meta_lines.append(f'<div class="meta-row">{" · ".join(parts)}</div>')

    meta_html = '\n    '.join(meta_lines)

    if svg_string:
        preview = f'<div class="svg-container">{svg_string}</div>'
    else:
        preview = (
            '<div class="svg-container planned-placeholder">'
            '<div style="padding:2em;color:#999;font-style:italic;border:2px dashed #ddd;'
            'border-radius:8px;min-height:120px;display:flex;align-items:center;'
            'justify-content:center;flex-direction:column;">'
            '<div style="font-size:1.5em;margin-bottom:0.5em;">&#x1f4d0;</div>'
            f'<div style="max-width:500px;text-align:left;font-size:0.9em;color:#666;">{placeholder_reason}</div>'
            '</div></div>'
        )

    notes_html = ''
    notes = entry.get('notes', '')
    if notes:
        notes_html = f'\n  <div class="notes-block"><span class="label">Notes:</span> {notes}</div>'

    return f'''
<section id="{eid}" class="svg-entry status-{status}">
  <h3>{eid} · {name} {badges}</h3>
  <div class="meta">
    {meta_html}
  </div>
  {preview}{notes_html}
</section>
'''


def generate_filmstrip_panels():
    """Reproduce the filmstrip panel generation from preprocess.py."""
    bx = [
        38, 63, 85, 112, 135, 161, 180, 208, 225, 252,
        275, 292, 318, 338, 365, 388, 405, 435, 452, 478,
        48, 78, 122, 168, 218, 258, 308, 348, 398, 442,
    ]
    floor_y = [240] * 20 + [227] * 10
    PICKUP_Y = 40

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

    panels = []

    # Panel 1
    p1_parts = [_btn_defs(), _floor()]
    for i in range(30):
        p1_parts.append(_button(bx[i], floor_y[i]))
    p1_parts.append(_label('scatter'))
    p1_parts.append(_counter('0 / 30'))
    p1_parts.append(_caption('Ten thousand buttons on a floor.'))
    panels.append(_svg_wrap('\n'.join(p1_parts)))

    # Panel 2
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
    panels.append(_svg_wrap('\n'.join(p2_parts)))

    # Panel 3
    p3_threads = [(9,8),(3,22),(22,5),(0,20),(6,7),(19,29),(20,1),(7,24),(10,25),(11,26)]
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
    p3_parts.append(_caption('A few hundred ties in. Small clumps — two, three buttons.'))
    panels.append(_svg_wrap('\n'.join(p3_parts)))

    # Panel 4
    p4_threads = [(9,8),(3,22),(22,5),(0,20),(6,7),(19,29),(20,1),(7,24),(10,25),(11,26),(8,24),(24,25),(10,7),(8,25),(5,23)]
    p4_lifted = {9: PICKUP_Y, 8: PICKUP_Y+25, 24: PICKUP_Y+55, 25: PICKUP_Y+55, 7: PICKUP_Y+85, 10: PICKUP_Y+85, 6: PICKUP_Y+115}
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
    panels.append(_svg_wrap('\n'.join(p4_parts)))

    # Panel 5
    p5_threads = [(9,8),(3,22),(22,5),(0,20),(6,7),(19,29),(20,1),(7,24),(10,25),(11,26),(8,24),(24,25),(10,7),(8,25),(5,23),(10,11),(26,12),(12,14),(14,28),(2,3),(1,21)]
    p5_dashed = [(6,23),(12,13),(28,29)]
    p5_lifted = {9:PICKUP_Y, 8:PICKUP_Y+20, 24:PICKUP_Y+45, 25:PICKUP_Y+45, 7:PICKUP_Y+70, 10:PICKUP_Y+70, 6:PICKUP_Y+95, 11:PICKUP_Y+95, 26:PICKUP_Y+115, 12:PICKUP_Y+135, 14:PICKUP_Y+155, 28:PICKUP_Y+185}
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
    panels.append(_svg_wrap('\n'.join(p5_parts)))

    # Panel 6
    p6_threads = [(9,8),(3,22),(22,5),(0,20),(6,7),(19,29),(20,1),(7,24),(10,25),(11,26),(8,24),(24,25),(10,7),(8,25),(5,23),(10,11),(26,12),(12,14),(14,28),(2,3),(1,21),(26,27),(28,29)]
    p6_red = (6, 23)
    p6_dist = {9:0,8:1,24:2,25:2,7:3,10:3,6:4,11:4,23:5,26:5,5:6,12:6,27:6,22:7,14:7,3:8,28:8,2:9,29:9,19:10}
    p6_lifted = {btn: PICKUP_Y + d*15 for btn, d in p6_dist.items()}
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
    p6_parts.append(_caption('One more thread. Pick up one button — the whole room lifts.'))
    panels.append(_svg_wrap('\n'.join(p6_parts)))

    return panels


def build_gallery():
    manifest = yaml.safe_load((REPO / 'build' / 'gallery-manifest.yaml').read_text())
    hover_svgs = load_hover_svgs()
    var_svgs, filmstrip = load_preprocess_svgs()

    by_category = {}
    for entry in manifest:
        cat = entry.get('category', 'Uncategorized')
        by_category.setdefault(cat, []).append(entry)

    ordered = []
    for cat in CATEGORY_ORDER:
        if cat in by_category:
            ordered.append((cat, by_category.pop(cat)))
    for cat, entries in sorted(by_category.items()):
        ordered.append((cat, entries))

    status_counts = {}
    for entry in manifest:
        s = entry.get('status', '?')
        status_counts[s] = status_counts.get(s, 0) + 1
    animated_count = sum(1 for e in manifest if e.get('animated'))
    total = len(manifest)

    status_parts = []
    for s in ['live', 'approved', 'draft', 'deferred']:
        if s in status_counts:
            status_parts.append(f'{status_counts[s]} {s}')

    warnings = []
    toc_lines = []
    body_lines = []

    for cat, entries in ordered:
        toc_lines.append(f'<li><strong>{cat}</strong><ul>')
        body_lines.append(f'<h2>{cat}</h2>')

        for entry in entries:
            svg, reason = resolve_svg(entry, hover_svgs, var_svgs, filmstrip)
            if reason and entry.get('status') == 'live':
                warnings.append(f"WARNING: {entry['id']} ({entry['name']}): {reason}")

            eid = entry.get('id', '???')
            name = entry.get('name', '')
            status = entry.get('status', '')
            sbadge = f' <span class="status-badge status-{status}" style="font-size:0.7em;">{status.upper()}</span>'
            abadge = ' <span class="animated-badge" style="font-size:0.65em;">ANIMATED</span>' if entry.get('animated') else ''
            toc_lines.append(f'  <li><a href="#{eid}">{eid}</a> — {name}{sbadge}{abadge}</li>')

            body_lines.append(render_card(entry, svg, reason))

        toc_lines.append('</ul></li>')

    for w in warnings:
        print(w, file=sys.stderr)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SVG Gallery — Source of Truth</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: Georgia, 'Times New Roman', serif;
    max-width: 900px;
    margin: 2em auto;
    padding: 0 1em;
    color: #333;
    background: #fafafa;
  }}
  h1 {{
    font-size: 1.6em;
    margin-bottom: 0.3em;
    color: #1a5276;
  }}
  .subtitle {{
    color: #888;
    font-size: 0.9em;
    margin-bottom: 1.5em;
    line-height: 1.6;
  }}
  h2 {{
    font-size: 1.2em;
    color: #1a5276;
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.2em;
    margin: 2em 0 1em;
  }}
  h3 {{
    font-family: 'Courier New', monospace;
    font-size: 0.95em;
    color: #2471a3;
    margin-bottom: 0.3em;
  }}
  nav ul {{
    list-style: none;
    padding-left: 0;
  }}
  nav ul ul {{
    padding-left: 1.5em;
    list-style: disc;
  }}
  nav li {{
    margin: 0.15em 0;
    font-size: 0.85em;
  }}
  nav a {{
    color: #2471a3;
    text-decoration: none;
  }}
  nav a:hover {{
    text-decoration: underline;
  }}
  .svg-entry {{
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 1em;
    margin: 1em 0;
  }}
  .svg-entry.status-live {{ border-left: 3px solid #27ae60; }}
  .svg-entry.status-approved {{ border-left: 3px solid #2980b9; }}
  .svg-entry.status-draft {{ border-left: 3px solid #d4ac0d; }}
  .svg-entry.status-deferred {{ border-left: 3px solid #ccc; }}
  .meta {{
    font-size: 0.8em;
    color: #666;
    margin-bottom: 0.8em;
    line-height: 1.6;
  }}
  .meta .label {{
    font-weight: bold;
    color: #555;
  }}
  .meta code {{
    background: #f0f0f0;
    padding: 0.1em 0.3em;
    border-radius: 2px;
    font-size: 0.9em;
  }}
  .meta-row {{
    margin: 0.2em 0;
  }}
  .status-badge {{
    display: inline-block;
    font-size: 0.7em;
    font-weight: bold;
    padding: 0.15em 0.5em;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    vertical-align: middle;
    margin-left: 0.5em;
  }}
  .status-live {{ color: #27ae60; background: #eafaf1; }}
  .status-approved {{ color: #2980b9; background: #ebf5fb; }}
  .status-draft {{ color: #d4ac0d; background: #fef9e7; }}
  .status-deferred {{ color: #888; background: #f4f4f4; }}
  .animated-badge {{
    display: inline-block;
    font-size: 0.65em;
    font-weight: bold;
    color: #1a8a6a;
    background: #e8f8f5;
    padding: 0.15em 0.5em;
    border-radius: 3px;
    vertical-align: middle;
    margin-left: 0.3em;
  }}
  .notes-block {{
    margin-top: 0.8em;
    padding-top: 0.5em;
    border-top: 1px dashed #e0e0e0;
    font-size: 0.8em;
    color: #888;
    font-style: italic;
  }}
  .notes-block .label {{
    font-style: normal;
  }}
  .svg-container {{
    text-align: center;
    padding: 0.5em;
    background: #fefefe;
    border: 1px dashed #e8e8e8;
    border-radius: 3px;
    overflow-x: auto;
  }}
  .svg-container svg {{
    max-width: 100%;
    height: auto;
  }}
  .count {{
    font-size: 0.85em;
    color: #888;
  }}
</style>
</head>
<body>
<h1>SVG Gallery — Source of Truth</h1>
<p class="subtitle">{total} entries: {', '.join(status_parts)}. {animated_count} animated.<br>
Manifest: <code>build/gallery-manifest.yaml</code></p>

<nav>
<h2 style="margin-top:0;">Table of Contents</h2>
<ul>
{''.join(toc_lines)}
</ul>
</nav>

{''.join(body_lines)}

<footer style="margin-top:3em;padding-top:1em;border-top:1px solid #ddd;font-size:0.8em;color:#aaa;">
Generated by build/generate-gallery.py — {total} entries from gallery-manifest.yaml.
</footer>
</body>
</html>'''

    out_path = REPO / 'docs' / 'gallery.html'
    out_path.write_text(html)
    print(f"Gallery written: {out_path} ({total} entries: {', '.join(status_parts)}. {animated_count} animated.)")


if __name__ == '__main__':
    build_gallery()
