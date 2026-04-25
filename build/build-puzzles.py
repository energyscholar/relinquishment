#!/usr/bin/env python3
"""Build standalone puzzle preview page from puzzle-data.yaml (Plan 0245)."""

import yaml
import html
import os

YAML_PATH = os.path.join(os.path.dirname(__file__), 'puzzle-data.yaml')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'downloads', 'puzzles.html')

with open(YAML_PATH) as f:
    data = yaml.safe_load(f)

puzzles = data['puzzles']


def escape(s):
    return html.escape(s, quote=True)


def render_mc_options(puzzle):
    lines = []
    for opt in puzzle['options']:
        key = escape(opt['key'])
        text = escape(opt['text'])
        lines.append(
            f'<button class="option-btn" data-key="{key}" '
            f'onclick="checkMC(\'{escape(puzzle["id"])}\', \'{key}\', this)">'
            f'({key}) {text}</button>'
        )
    return '\n          '.join(lines)


def render_text_input(puzzle):
    pid = escape(puzzle['id'])
    return (
        f'<div class="text-input-wrap">'
        f'<input type="text" id="input-{pid}" placeholder="Type your answer…" '
        f'onkeydown="if(event.key===\'Enter\')checkText(\'{pid}\')">'
        f'<button class="submit-btn" onclick="checkText(\'{pid}\')">Check</button>'
        f'</div>'
    )


def render_puzzle_block(puzzle):
    pid = escape(puzzle['id'])
    title = escape(puzzle['chapter_title'])
    question = escape(puzzle['question'])
    hint = escape(puzzle['hint'])
    abstract = escape(puzzle['abstract'].strip())
    hashes_js = ', '.join(f'"{h}"' for h in puzzle['answer_hashes'])

    if puzzle['type'] == 'multiple-choice':
        interaction = render_mc_options(puzzle)
    else:
        interaction = render_text_input(puzzle)

    return f'''
    <div class="puzzle-block" id="puzzle-{pid}">
      <h2>{title}</h2>
      <p class="question">{question}</p>
      <div class="interaction" id="interact-{pid}">
        {interaction}
      </div>
      <p class="hint" id="hint-{pid}">{hint}</p>
      <div class="result" id="result-{pid}">
        <div class="solved-badge">&#10003; Solved</div>
        <blockquote class="abstract">{abstract}</blockquote>
      </div>
      <script>puzzleHashes["{pid}"] = [{hashes_js}];</script>
    </div>'''


puzzle_blocks = '\n'.join(render_puzzle_block(p) for p in puzzles)
total = len(puzzles)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relinquishment — Puzzle Preview</title>
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

  h2 {{
    font-size: 1.3em;
    margin-top: 0;
    color: #1a5276;
  }}

  .framing {{
    font-style: italic;
    color: #555;
    margin-bottom: 0.3em;
  }}

  .progress {{
    font-size: 1.1em;
    font-weight: bold;
    margin-bottom: 2em;
    color: #1a5276;
  }}

  .puzzle-block {{
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 1.5em;
    margin-bottom: 2em;
    background: #fafafa;
  }}

  .puzzle-block.solved {{
    border-color: #2a9b9a;
    background: #f0faf9;
  }}

  .question {{
    font-size: 1.05em;
    margin-bottom: 1em;
  }}

  .option-btn {{
    display: block;
    width: 100%;
    text-align: left;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1em;
    padding: 0.7em 1em;
    margin-bottom: 0.5em;
    border: 1px solid #ccc;
    border-radius: 4px;
    background: #fff;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
  }}

  .option-btn:hover {{
    border-color: #1a5276;
    background: #f0f6fa;
  }}

  .option-btn.wrong {{
    border-color: #c0392b;
    background: #fdf2f2;
    animation: shake 0.3s ease-in-out;
  }}

  .option-btn.correct {{
    border-color: #2a9b9a;
    background: #e8f8f5;
    font-weight: bold;
  }}

  @keyframes shake {{
    0%, 100% {{ transform: translateX(0); }}
    25% {{ transform: translateX(-4px); }}
    75% {{ transform: translateX(4px); }}
  }}

  .text-input-wrap {{
    display: flex;
    gap: 0.5em;
    margin-bottom: 0.5em;
  }}

  .text-input-wrap input {{
    flex: 1;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1em;
    padding: 0.6em 0.8em;
    border: 1px solid #ccc;
    border-radius: 4px;
  }}

  .text-input-wrap input:focus {{
    outline: none;
    border-color: #1a5276;
  }}

  .submit-btn {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1em;
    padding: 0.6em 1.2em;
    border: 1px solid #1a5276;
    border-radius: 4px;
    background: #1a5276;
    color: #fff;
    cursor: pointer;
  }}

  .submit-btn:hover {{
    background: #154360;
  }}

  .hint {{
    display: none;
    color: #856404;
    background: #fff9e6;
    border-left: 3px solid #d4a14b;
    padding: 0.6em 1em;
    margin-top: 0.5em;
    font-style: italic;
  }}

  .hint.visible {{
    display: block;
  }}

  .result {{
    display: none;
    margin-top: 1em;
  }}

  .result.visible {{
    display: block;
  }}

  .solved-badge {{
    color: #2a9b9a;
    font-weight: bold;
    font-size: 1.1em;
    margin-bottom: 0.5em;
  }}

  .abstract {{
    border-left: 3px solid #2a9b9a;
    padding: 0.8em 1em;
    margin: 0;
    background: #f0faf9;
    font-style: italic;
    color: #333;
    line-height: 1.5;
  }}

  .no-crypto {{
    background: #fff3cd;
    border: 1px solid #d4a14b;
    padding: 1em;
    border-radius: 4px;
    margin-bottom: 2em;
  }}

  @media (prefers-color-scheme: dark) {{
    body {{ background: #1a1a1a; color: #e0e0e0; }}
    h2 {{ color: #6ba3f7; }}
    .framing {{ color: #aaa; }}
    .progress {{ color: #6ba3f7; }}
    .puzzle-block {{ background: #242424; border-color: #444; }}
    .puzzle-block.solved {{ background: #1a2e2d; border-color: #2a9b9a; }}
    .question {{ color: #e0e0e0; }}
    .option-btn {{ background: #2a2a2a; border-color: #555; color: #e0e0e0; }}
    .option-btn:hover {{ background: #1e3a50; border-color: #6ba3f7; }}
    .option-btn.wrong {{ background: #3a1a1a; border-color: #c0392b; }}
    .option-btn.correct {{ background: #1a3a35; border-color: #2a9b9a; }}
    .text-input-wrap input {{ background: #2a2a2a; color: #e0e0e0; border-color: #555; }}
    .text-input-wrap input:focus {{ border-color: #6ba3f7; }}
    .submit-btn {{ background: #2a6496; border-color: #2a6496; }}
    .hint {{ background: #2a2510; color: #f0d060; border-left-color: #d4a14b; }}
    .abstract {{ background: #1a2e2d; color: #ccc; }}
    .no-crypto {{ background: #2a2510; border-color: #d4a14b; color: #f0d060; }}
  }}

  @media (max-width: 600px) {{
    body {{ padding: 0.8em; font-size: 16px; }}
    h1 {{ font-size: 1.4em; }}
    .puzzle-block {{ padding: 1em; }}
    .text-input-wrap {{ flex-direction: column; }}
    .option-btn {{ min-height: 44px; }}
    .submit-btn {{ min-height: 44px; }}
  }}
</style>
</head>
<body>

<h1>Relinquishment &mdash; Puzzle Preview</h1>
<p class="framing">Each chapter ends with a puzzle. Solve it to reveal
the chapter&rsquo;s Spiral Abstract &mdash; the meta-view that connects the chapter
to the book&rsquo;s larger argument. These are samples from three chapters.</p>
<p class="progress">Progress: <span id="count">0</span>/{total}</p>

<div id="no-crypto" class="no-crypto" style="display:none;">
  <strong>Note:</strong> Your browser does not support the SubtleCrypto API.
  All puzzles are shown unlocked.
</div>

{puzzle_blocks}

<script>
"use strict";

var puzzleHashes = {{}};
var TOTAL = {total};
var STORAGE_KEY = "relinquishment-puzzles-solved";

function getSolved() {{
  try {{
    var s = localStorage.getItem(STORAGE_KEY);
    return s ? JSON.parse(s) : {{}};
  }} catch(e) {{ return {{}}; }}
}}

function setSolved(id) {{
  try {{
    var s = getSolved();
    s[id] = true;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(s));
  }} catch(e) {{}}
}}

function updateCount() {{
  var solved = getSolved();
  var n = 0;
  for (var k in solved) if (solved[k]) n++;
  document.getElementById("count").textContent = n;
}}

function revealPuzzle(id) {{
  var block = document.getElementById("puzzle-" + id);
  if (!block) return;
  block.classList.add("solved");
  var interact = document.getElementById("interact-" + id);
  if (interact) interact.style.display = "none";
  var hint = document.getElementById("hint-" + id);
  if (hint) hint.classList.remove("visible");
  var result = document.getElementById("result-" + id);
  if (result) result.classList.add("visible");
  setSolved(id);
  updateCount();
}}

function showHint(id) {{
  var hint = document.getElementById("hint-" + id);
  if (hint) hint.classList.add("visible");
}}

function normalize(s) {{
  s = s.toLowerCase().trim();
  s = s.replace(/[.,!?;:]+$/g, "");
  s = s.replace(/^(a |an |the )/, "");
  return s.trim();
}}

async function sha256(msg) {{
  var buf = new TextEncoder().encode(msg);
  var hash = await crypto.subtle.digest("SHA-256", buf);
  var arr = Array.from(new Uint8Array(hash));
  return arr.map(function(b) {{ return b.toString(16).padStart(2, "0"); }}).join("");
}}

async function checkMC(id, key, btn) {{
  var solved = getSolved();
  if (solved[id]) return;
  var hashes = puzzleHashes[id] || [];
  var h = await sha256(key);
  if (hashes.indexOf(h) !== -1) {{
    btn.classList.add("correct");
    setTimeout(function() {{ revealPuzzle(id); }}, 400);
  }} else {{
    btn.classList.add("wrong");
    setTimeout(function() {{ btn.classList.remove("wrong"); }}, 600);
    showHint(id);
  }}
}}

async function checkText(id) {{
  var solved = getSolved();
  if (solved[id]) return;
  var input = document.getElementById("input-" + id);
  if (!input) return;
  var val = normalize(input.value);
  if (!val) return;
  var hashes = puzzleHashes[id] || [];
  var h = await sha256(val);
  if (hashes.indexOf(h) !== -1) {{
    input.style.borderColor = "#2a9b9a";
    setTimeout(function() {{ revealPuzzle(id); }}, 400);
  }} else {{
    input.style.borderColor = "#c0392b";
    setTimeout(function() {{ input.style.borderColor = ""; }}, 600);
    showHint(id);
  }}
}}

function init() {{
  if (!window.crypto || !window.crypto.subtle) {{
    document.getElementById("no-crypto").style.display = "block";
    var ids = Object.keys(puzzleHashes);
    for (var i = 0; i < ids.length; i++) revealPuzzle(ids[i]);
    return;
  }}
  var solved = getSolved();
  for (var id in solved) {{
    if (solved[id]) revealPuzzle(id);
  }}
  updateCount();

  // Scroll to anchor if present
  if (window.location.hash) {{
    var el = document.querySelector(window.location.hash);
    if (el) setTimeout(function() {{ el.scrollIntoView({{ behavior: "smooth" }}); }}, 100);
  }}
}}

init();
</script>

</body>
</html>'''

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, 'w') as f:
    f.write(page)

print(f"Built {OUT_PATH} ({len(puzzles)} puzzles)")
