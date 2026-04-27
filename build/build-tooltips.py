#!/usr/bin/env python3
"""Build standalone tooltip viewer page from hover-definitions.yaml (Plan 0250)."""

import yaml
import html
import json
import re
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import esc as _shared_esc
from colors import COLORS

YAML_PATH = os.path.join(os.path.dirname(__file__), 'hover-definitions.yaml')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'downloads', 'tooltips.html')

with open(YAML_PATH) as f:
    data = yaml.safe_load(f)


def escape(s):
    return _shared_esc(s)


def slugify(key):
    return re.sub(r'[^a-z0-9]+', '-', key.lower()).strip('-')


def normalize_entry(key, value):
    """Normalize both plain-string and dict YAML entries to a consistent dict."""
    if isinstance(value, str):
        return {
            'uid': key,
            'hover_id': slugify(key),
            'text': value,
            'html': None,
            'target': None,
        }
    return {
        'uid': key,
        'hover_id': value.get('hover_id', slugify(key)),
        'text': value.get('text', ''),
        'html': value.get('html', None),
        'target': value.get('target', None),
    }


# Parse all entries, dedup by content
entries = []
seen_content = {}  # (text, html, target) -> list of UIDs

for key, value in data.items():
    entry = normalize_entry(key, value)
    content_key = (entry['text'], entry.get('html'), entry.get('target'))
    if content_key in seen_content:
        seen_content[content_key].append(entry['uid'])
        continue
    seen_content[content_key] = [entry['uid']]
    entries.append(entry)

# Sort alphabetically by UID
entries.sort(key=lambda e: e['uid'].lower())

# Build hover-data JSON for the inline tooltip system
hover_data = {}
for key, value in data.items():
    entry = normalize_entry(key, value)
    hid = entry['hover_id']
    if hid not in hover_data:
        hover_data[hid] = {}
    if entry['text'] and 't' not in hover_data[hid]:
        hover_data[hid]['t'] = entry['text']
    if entry.get('html') and 'h' not in hover_data[hid]:
        hover_data[hid]['h'] = entry['html']

hover_json = json.dumps(hover_data, separators=(',', ':'), ensure_ascii=False)
hover_json = hover_json.replace('</', '<\\/')

# Count rich panels
rich_count = sum(1 for e in entries if e.get('html'))
total = len(entries)


def render_entry(entry):
    uid = entry['uid']
    hover_id = entry['hover_id']
    text = entry.get('text', '') or ''
    rich_html = entry.get('html')
    target = entry.get('target')
    has_rich = bool(rich_html)

    # Find all UIDs that share this content
    content_key = (entry['text'], entry.get('html'), entry.get('target'))
    all_uids = seen_content.get(content_key, [uid])

    badge = '<span class="badge rich">rich panel</span>' if has_rich else '<span class="badge text-only">text</span>'

    aliases_html = ''
    if len(all_uids) > 1:
        other = [u for u in all_uids if u != uid]
        aliases_html = f'<div class="aliases">Also: {", ".join("<code>" + escape(u) + "</code>" for u in other)}</div>'

    target_html = ''
    if target:
        target_html = f'<div class="target">Target: <code>{escape(target)}</code></div>'

    rich_panel_html = ''
    if rich_html:
        rich_panel_html = f'<div class="rich-preview"><div class="rich-label">Rich panel:</div><div class="rich-content">{rich_html}</div></div>'

    return f'''
    <div class="entry" id="{escape(hover_id)}" data-search="{escape(uid.lower())} {escape(text.lower())}">
      <div class="entry-header">
        <code class="uid">{escape(uid)}</code>
        {badge}
      </div>
      <div class="hover-demo">
        Hover/tap: <span class="hover-term" data-hover-id="{escape(hover_id)}">{escape(uid)}</span>
      </div>
      <blockquote class="copyable">{escape(text)}</blockquote>
      {rich_panel_html}
      {target_html}
      {aliases_html}
    </div>'''


entry_blocks = '\n'.join(render_entry(e) for e in entries)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relinquishment &mdash; Tooltip Viewer</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; }}

  body {{
    font-family: Georgia, "Times New Roman", serif;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 42em;
    margin: 0 auto;
    padding: 1.5em;
    background: #fff;
  }}

  h1 {{
    font-size: 1.8em;
    margin-bottom: 0.2em;
    letter-spacing: 0.03em;
  }}

  .subtitle {{
    color: #555;
    font-style: italic;
    margin-bottom: 1.5em;
  }}

  .search-wrap {{
    position: sticky;
    top: 0;
    background: #fff;
    padding: 0.8em 0;
    z-index: 100;
    border-bottom: 1px solid #eee;
    margin-bottom: 1em;
  }}

  .search-wrap input {{
    width: 100%;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1em;
    padding: 0.6em 0.8em;
    border: 1px solid #ccc;
    border-radius: 4px;
  }}

  .search-wrap input:focus {{
    outline: none;
    border-color: #1a5276;
  }}

  .match-count {{
    font-size: 0.85em;
    color: #888;
    margin-top: 0.3em;
  }}

  .entry {{
    border-bottom: 1px solid #ddd;
    padding: 1.2em 0;
  }}

  .entry.hidden {{
    display: none;
  }}

  .entry-header {{
    display: flex;
    align-items: center;
    gap: 0.6em;
    margin-bottom: 0.5em;
    flex-wrap: wrap;
  }}

  .uid {{
    font-size: 1.05em;
    background: #f5f5f5;
    padding: 0.15em 0.4em;
    border-radius: 3px;
    color: #1a5276;
  }}

  .badge {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 0.7em;
    padding: 0.15em 0.5em;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .badge.rich {{
    background: #e8f0f8;
    color: #1a5276;
  }}

  .badge.text-only {{
    background: #f0f0f0;
    color: #888;
  }}

  .hover-demo {{
    margin-bottom: 0.6em;
    font-size: 0.95em;
  }}

  .hover-term {{
    font-style: italic;
    border-bottom: 1px dotted #888;
    cursor: pointer;
  }}

  .hover-term:hover {{
    border-bottom-color: #2471a3;
  }}

  .copyable {{
    border-left: 3px solid #1a5276;
    padding: 0.6em 1em;
    margin: 0.5em 0;
    background: #fafafa;
    font-size: 0.92em;
    line-height: 1.5;
    color: #333;
    -webkit-user-select: text;
    user-select: text;
  }}

  .rich-preview {{
    margin: 0.8em 0;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 0.8em;
    background: #fafafa;
  }}

  .rich-label {{
    font-size: 0.8em;
    color: #888;
    margin-bottom: 0.4em;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .rich-content {{
    font-size: 0.95em;
  }}

  .rich-content svg {{
    max-width: 100%;
    height: auto;
  }}

  .target {{
    font-size: 0.85em;
    color: #888;
    margin-top: 0.3em;
  }}

  .target code {{
    background: #f5f5f5;
    padding: 0.1em 0.3em;
    border-radius: 2px;
    font-size: 0.9em;
  }}

  .aliases {{
    font-size: 0.85em;
    color: #888;
    margin-top: 0.3em;
  }}

  .aliases code {{
    background: #f5f5f5;
    padding: 0.1em 0.3em;
    border-radius: 2px;
    font-size: 0.9em;
  }}

  /* Hover panel (tooltip popup) */
  .hover-panel {{
    position: fixed;
    z-index: 200;
    max-width: 440px;
    max-height: 70vh;
    overflow-y: auto;
    padding: 0.8em 1em;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    font-size: 0.9em;
    line-height: 1.5;
    animation: panel-fade-in 0.15s ease-out;
  }}

  @keyframes panel-fade-in {{
    from {{ opacity: 0; transform: translateY(4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  .back-link {{
    display: inline-block;
    margin-top: 2em;
    color: #1a5276;
    font-size: 0.9em;
  }}

  @media (prefers-color-scheme: dark) {{
    body {{ background: #1a1a1a; color: #e0e0e0; }}
    .subtitle {{ color: #aaa; }}
    .search-wrap {{ background: #1a1a1a; border-bottom-color: #333; }}
    .search-wrap input {{ background: #2a2a2a; color: #e0e0e0; border-color: #555; }}
    .search-wrap input:focus {{ border-color: #5dade2; }}
    .uid {{ background: #2a2a2a; color: #5dade2; }}
    .badge.rich {{ background: #1e3a50; color: #5dade2; }}
    .badge.text-only {{ background: #2a2a2a; color: #888; }}
    .hover-term {{ border-bottom-color: #666; }}
    .hover-term:hover {{ border-bottom-color: #5dade2; }}
    .copyable {{ background: #242424; border-left-color: #5dade2; color: #ccc; }}
    .rich-preview {{ background: #242424; border-color: #444; }}
    .rich-label {{ color: #888; }}
    .target code, .aliases code {{ background: #2a2a2a; }}
    .entry {{ border-bottom-color: #333; }}
    .hover-panel {{
      background: #2a2a2a;
      border-color: #555;
      color: #e0e0e0;
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }}
    .match-count {{ color: #888; }}
    .back-link {{ color: #5dade2; }}
  }}

  @media (max-width: 600px) {{
    body {{ padding: 0.8em; font-size: 16px; }}
    h1 {{ font-size: 1.4em; }}
    .hover-panel {{ max-width: calc(100vw - 16px); left: 8px !important; right: 8px; }}
  }}
</style>
</head>
<body>

<h1>Relinquishment &mdash; Tooltip Viewer</h1> <a class="back-link" href="../tools.html">&larr; Back to Author Tools</a>
<p class="subtitle">{total} hover definitions, {rich_count} with rich panels</p>

<div class="search-wrap">
  <input type="text" id="search" placeholder="Search by term or content…" autocomplete="off">
  <div class="match-count" id="match-count"></div>
</div>

<script type="application/json" id="hover-data">{hover_json}</script>

{entry_blocks}

<p class="back-link"><a href="../tools.html">&larr; Author Tools</a></p>

<script>
"use strict";

var hoverData = {{}};
var _hd = document.getElementById("hover-data");
if (_hd) hoverData = JSON.parse(_hd.textContent);

var panelIdCounter = 0;
var hoverDelay = 250;
var hoverTimer = null;
var dismissTimer = null;
var dismissDelay = 300;

function dismissPanel() {{
  if (dismissTimer) {{ clearTimeout(dismissTimer); dismissTimer = null; }}
  var existing = document.querySelector(".hover-panel");
  if (existing) {{
    var linked = document.querySelector('[aria-describedby="' + existing.id + '"]');
    if (linked) linked.removeAttribute("aria-describedby");
    existing.remove();
  }}
}}

function showPanel(term) {{
  var hoverId = term.getAttribute("data-hover-id");
  var lookup = (hoverId && hoverData[hoverId]) || null;
  var def = (lookup && lookup.t) || term.getAttribute("data-hover");
  var richHtml = (lookup && lookup.h) || term.getAttribute("data-hover-html");
  if (!def && !richHtml) return;

  dismissPanel();

  var panel = document.createElement("div");
  panel.className = "hover-panel";
  panelIdCounter++;
  panel.id = "hover-panel-" + panelIdCounter;
  panel.setAttribute("role", "tooltip");

  if (richHtml) {{
    var content = document.createElement("div");
    content.innerHTML = richHtml;
    panel.appendChild(content);
  }} else {{
    panel.appendChild(document.createTextNode(def));
  }}

  term.setAttribute("aria-describedby", panel.id);
  document.body.appendChild(panel);
  positionPanel(panel, term);

  panel.addEventListener("mouseenter", function() {{
    if (dismissTimer) {{ clearTimeout(dismissTimer); dismissTimer = null; }}
  }});
  panel.addEventListener("mouseleave", function() {{
    if (dismissTimer) clearTimeout(dismissTimer);
    dismissTimer = setTimeout(function() {{
      dismissTimer = null;
      dismissPanel();
    }}, dismissDelay);
  }});

  return panel;
}}

function positionPanel(panel, term) {{
  var termRect = term.getBoundingClientRect();
  var panelRect = panel.getBoundingClientRect();
  var vw = window.innerWidth;
  var vh = window.innerHeight;
  var gap = 6;

  var top = termRect.bottom + gap;
  var left = termRect.left;

  if (top + panelRect.height > vh - 10) {{
    top = termRect.top - panelRect.height - gap;
  }}
  if (top < 5) top = 5;
  if (left + panelRect.width > vw - 10) {{
    left = vw - panelRect.width - 10;
  }}
  if (left < 5) left = 5;

  if (vw < 500) {{
    left = 8;
    panel.style.maxWidth = (vw - 16) + "px";
    panel.style.width = (vw - 16) + "px";
  }}

  panel.style.top = top + "px";
  panel.style.left = left + "px";
}}

// Bind hover events
var allTerms = document.querySelectorAll("[data-hover-id]");
var lastTouchTime = 0;

allTerms.forEach(function(term) {{
  term.setAttribute("tabindex", "0");

  term.addEventListener("mouseenter", function() {{
    if (dismissTimer) {{ clearTimeout(dismissTimer); dismissTimer = null; }}
    if (Date.now() - lastTouchTime < 500) return;
    if (hoverTimer) clearTimeout(hoverTimer);
    hoverTimer = setTimeout(function() {{
      hoverTimer = null;
      showPanel(term);
    }}, hoverDelay);
  }});

  term.addEventListener("mouseleave", function() {{
    if (hoverTimer) {{ clearTimeout(hoverTimer); hoverTimer = null; }}
    if (dismissTimer) clearTimeout(dismissTimer);
    dismissTimer = setTimeout(function() {{
      dismissTimer = null;
      var panel = document.querySelector(".hover-panel");
      if (panel && !panel.matches(":hover")) dismissPanel();
    }}, dismissDelay);
  }});

  term.addEventListener("keydown", function(e) {{
    if (e.key === "Enter") {{
      e.preventDefault();
      var existing = document.querySelector(".hover-panel");
      if (existing && term.getAttribute("aria-describedby") === existing.id) {{
        dismissPanel();
      }} else {{
        showPanel(term);
      }}
    }}
  }});
}});

// Touch support
document.addEventListener("touchstart", function(e) {{
  var term = e.target.closest("[data-hover-id]");
  if (term) lastTouchTime = Date.now();
}}, {{ passive: true }});

document.addEventListener("touchend", function(e) {{
  var term = e.target.closest("[data-hover-id]");
  if (!term) return;
  lastTouchTime = Date.now();
  e.preventDefault();
  if (hoverTimer) {{ clearTimeout(hoverTimer); hoverTimer = null; }}
  var existing = document.querySelector(".hover-panel");
  if (existing && term.getAttribute("aria-describedby") === existing.id) {{
    dismissPanel();
    return;
  }}
  showPanel(term);
}}, {{ passive: false }});

document.addEventListener("click", function(e) {{
  var term = e.target.closest("[data-hover-id]");
  if (!term) {{
    if (!e.target.closest(".hover-panel")) dismissPanel();
    return;
  }}
  if (Date.now() - lastTouchTime < 500) return;
  e.preventDefault();
  if (hoverTimer) {{ clearTimeout(hoverTimer); hoverTimer = null; }}
  var existing = document.querySelector(".hover-panel");
  if (existing && term.getAttribute("aria-describedby") === existing.id) {{
    dismissPanel();
    return;
  }}
  showPanel(term);
}});

document.addEventListener("touchend", function(e) {{
  if (e.target.closest("[data-hover-id]") || e.target.closest(".hover-panel")) return;
  dismissPanel();
}});

document.addEventListener("keydown", function(e) {{
  if (e.key === "Escape") dismissPanel();
}});

// Search
var searchInput = document.getElementById("search");
var matchCount = document.getElementById("match-count");
var allEntries = document.querySelectorAll(".entry");

searchInput.addEventListener("input", function() {{
  var q = searchInput.value.toLowerCase().trim();
  var visible = 0;
  allEntries.forEach(function(el) {{
    var searchText = el.getAttribute("data-search") || "";
    if (!q || searchText.indexOf(q) !== -1) {{
      el.classList.remove("hidden");
      visible++;
    }} else {{
      el.classList.add("hidden");
    }}
  }});
  if (q) {{
    matchCount.textContent = visible + " of {total} entries";
  }} else {{
    matchCount.textContent = "";
  }}
}});

// Fragment navigation
if (window.location.hash) {{
  var el = document.querySelector(window.location.hash);
  if (el) setTimeout(function() {{ el.scrollIntoView({{ behavior: "smooth" }}); }}, 100);
}}
</script>

</body>
</html>'''

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, 'w') as f:
    f.write(page)

print(f"Built {OUT_PATH} ({total} entries, {rich_count} with rich panels)")
