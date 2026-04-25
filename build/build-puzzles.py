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


def render_threads_interaction(puzzle):
    pid = escape(puzzle['id'])
    threshold = puzzle.get('hint_threshold', 12)
    return f'''<div class="threads-sim" id="sim-{pid}">
          <svg id="svg-{pid}" viewBox="0 0 400 300" class="threads-svg">
          </svg>
          <div class="sim-controls">
            <button class="submit-btn" id="add-btn-{pid}" onclick="addThread('{pid}')">Add Thread</button>
            <span class="thread-count" id="tcount-{pid}">Threads: 0</span>
          </div>
          <div class="transition-flash" id="flash-{pid}">Phase Transition!</div>
        </div>
        <script>initThreadsSim("{pid}", {threshold});</script>'''


def render_puzzle_block(puzzle):
    pid = escape(puzzle['id'])
    title = escape(puzzle['chapter_title'])
    question = escape(puzzle['question'])
    hint_text = escape(puzzle.get('hint', ''))
    abstract = escape(puzzle['abstract'].strip())

    if puzzle['type'] == 'multiple-choice':
        interaction = render_mc_options(puzzle)
        hashes_js = ', '.join(f'"{h}"' for h in puzzle.get('answer_hashes', []))
        hash_script = f'<script>puzzleHashes["{pid}"] = [{hashes_js}];</script>'
    elif puzzle['type'] == 'interactive-simulation':
        interaction = render_threads_interaction(puzzle)
        hash_script = ''
    else:
        interaction = render_text_input(puzzle)
        hashes_js = ', '.join(f'"{h}"' for h in puzzle.get('answer_hashes', []))
        hash_script = f'<script>puzzleHashes["{pid}"] = [{hashes_js}];</script>'

    return f'''
    <div class="puzzle-block" id="puzzle-{pid}">
      <h2>{title}</h2>
      <p class="question">{question}</p>
      <div class="interaction" id="interact-{pid}">
        {interaction}
      </div>
      <p class="hint" id="hint-{pid}">{hint_text}</p>
      <div class="result" id="result-{pid}">
        <div class="solved-badge">&#10003; Solved</div>
        <blockquote class="abstract">{abstract}</blockquote>
      </div>
      {hash_script}
    </div>'''


puzzle_blocks = '\n'.join(render_puzzle_block(p) for p in puzzles)
total = len(puzzles)

# Threads simulation JS — union-find, random layout, cluster coloring, phase transition
THREADS_JS = r"""
var threadsSims = {};
var CLUSTER_COLORS = ["#2a9b9a","#c0392b","#8b5fc0","#d4a14b","#1a5276","#27ae60","#e67e22","#2980b9"];

function initThreadsSim(id, hintThreshold) {
  var N = 16, W = 400, H = 300, R = 12;
  var nodes = [];
  for (var i = 0; i < N; i++) {
    nodes.push({
      x: R + Math.random() * (W - 2*R),
      y: R + Math.random() * (H - 2*R),
      parent: i, rank: 0
    });
  }
  // Generate all possible edges, shuffle
  var allEdges = [];
  for (var a = 0; a < N; a++)
    for (var b = a+1; b < N; b++)
      allEdges.push([a,b]);
  for (var i = allEdges.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i+1));
    var tmp = allEdges[i]; allEdges[i] = allEdges[j]; allEdges[j] = tmp;
  }
  var sim = {
    id: id, nodes: nodes, edges: [], edgeQueue: allEdges,
    edgeIdx: 0, threadCount: 0, solved: false,
    hintThreshold: hintThreshold
  };
  threadsSims[id] = sim;
  renderThreadsSvg(sim);
}

function ufFind(nodes, i) {
  if (nodes[i].parent !== i) nodes[i].parent = ufFind(nodes, nodes[i].parent);
  return nodes[i].parent;
}

function ufUnion(nodes, a, b) {
  var ra = ufFind(nodes, a), rb = ufFind(nodes, b);
  if (ra === rb) return;
  if (nodes[ra].rank < nodes[rb].rank) { var t = ra; ra = rb; rb = t; }
  nodes[rb].parent = ra;
  if (nodes[ra].rank === nodes[rb].rank) nodes[ra].rank++;
}

function getClusters(nodes) {
  var map = {};
  for (var i = 0; i < nodes.length; i++) {
    var r = ufFind(nodes, i);
    if (!map[r]) map[r] = [];
    map[r].push(i);
  }
  return map;
}

function largestCluster(nodes) {
  var clusters = getClusters(nodes);
  var max = 0;
  for (var k in clusters) if (clusters[k].length > max) max = clusters[k].length;
  return max;
}

function renderThreadsSvg(sim) {
  var svg = document.getElementById("svg-" + sim.id);
  if (!svg) return;
  var clusters = getClusters(sim.nodes);
  var nodeColor = {};
  var ci = 0;
  for (var root in clusters) {
    var color = CLUSTER_COLORS[ci % CLUSTER_COLORS.length];
    for (var j = 0; j < clusters[root].length; j++)
      nodeColor[clusters[root][j]] = color;
    ci++;
  }
  var parts = [];
  for (var i = 0; i < sim.edges.length; i++) {
    var e = sim.edges[i];
    var a = sim.nodes[e[0]], b = sim.nodes[e[1]];
    parts.push('<line x1="'+a.x+'" y1="'+a.y+'" x2="'+b.x+'" y2="'+b.y+'" stroke="#999" stroke-width="1.5" stroke-opacity="0.6"/>');
  }
  for (var i = 0; i < sim.nodes.length; i++) {
    var n = sim.nodes[i];
    var col = nodeColor[i] || "#ccc";
    var cls = sim.solved && largestCluster(sim.nodes) > 8 ? " glow" : "";
    parts.push('<circle cx="'+n.x+'" cy="'+n.y+'" r="12" fill="'+col+'" stroke="#fff" stroke-width="1.5" class="node-circle'+cls+'"/>');
  }
  svg.innerHTML = parts.join("\n");
}

function addThread(id) {
  var sim = threadsSims[id];
  if (!sim || sim.solved) return;
  if (sim.edgeIdx >= sim.edgeQueue.length) return;
  var edge = sim.edgeQueue[sim.edgeIdx++];
  sim.edges.push(edge);
  ufUnion(sim.nodes, edge[0], edge[1]);
  sim.threadCount++;
  document.getElementById("tcount-" + id).textContent = "Threads: " + sim.threadCount;
  renderThreadsSvg(sim);
  if (sim.threadCount >= sim.hintThreshold && largestCluster(sim.nodes) < 9) {
    showHint(id);
  }
  if (largestCluster(sim.nodes) >= 9) {
    sim.solved = true;
    renderThreadsSvg(sim);
    var flash = document.getElementById("flash-" + id);
    if (flash) flash.classList.add("visible");
    var btn = document.getElementById("add-btn-" + id);
    if (btn) btn.disabled = true;
    setTimeout(function() {
      if (flash) flash.classList.remove("visible");
      revealPuzzle(id);
    }, 1800);
  }
}
"""

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

  .submit-btn:disabled {{
    opacity: 0.5;
    cursor: default;
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

  /* Threads simulation */
  .threads-svg {{
    width: 100%;
    max-width: 400px;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    background: #fff;
    display: block;
    margin: 0 auto 0.8em;
  }}

  .sim-controls {{
    display: flex;
    align-items: center;
    gap: 1em;
    justify-content: center;
    margin-bottom: 0.5em;
  }}

  .thread-count {{
    font-size: 0.95em;
    color: #555;
  }}

  .node-circle {{
    transition: fill 0.3s ease;
  }}

  .node-circle.glow {{
    filter: drop-shadow(0 0 6px currentColor);
  }}

  .transition-flash {{
    display: none;
    text-align: center;
    font-size: 1.3em;
    font-weight: bold;
    color: #2a9b9a;
    padding: 0.5em;
    animation: pulse 0.6s ease-in-out 3;
  }}

  .transition-flash.visible {{
    display: block;
  }}

  @keyframes pulse {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.7; transform: scale(1.05); }}
  }}

  .reset-wrap {{
    text-align: center;
    margin: 2em 0 1em;
  }}

  .reset-btn {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 0.9em;
    padding: 0.5em 1.2em;
    border: 1px solid #ccc;
    border-radius: 4px;
    background: #fff;
    color: #888;
    cursor: pointer;
    transition: color 0.2s, border-color 0.2s;
  }}

  .reset-btn:hover {{
    color: #c0392b;
    border-color: #c0392b;
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
    .threads-svg {{ background: #2a2a2a; border-color: #555; }}
    .thread-count {{ color: #aaa; }}
    .reset-btn {{ background: #2a2a2a; border-color: #555; color: #888; }}
    .reset-btn:hover {{ color: #e74c3c; border-color: #e74c3c; }}
  }}

  @media (max-width: 600px) {{
    body {{ padding: 0.8em; font-size: 16px; }}
    h1 {{ font-size: 1.4em; }}
    .puzzle-block {{ padding: 1em; }}
    .text-input-wrap {{ flex-direction: column; }}
    .option-btn {{ min-height: 44px; }}
    .submit-btn {{ min-height: 44px; }}
    .threads-svg {{ max-width: 100%; }}
  }}
</style>
</head>
<body>

<h1>Relinquishment &mdash; Puzzle Preview</h1> <a style="font-size:0.55em;color:#1a5276;" href="../tools.html">&larr; Back to Author Tools</a>
<p class="framing">Each chapter ends with a puzzle. Solve it to reveal
the chapter&rsquo;s Spiral Abstract &mdash; the meta-view that connects the chapter
to the book&rsquo;s larger argument. These are samples from four chapters.</p>
<p class="progress">Progress: <span id="count">0</span>/{total}</p>

<div id="no-crypto" class="no-crypto" style="display:none;">
  <strong>Note:</strong> Your browser does not support the SubtleCrypto API.
  All puzzles are shown unlocked.
</div>

<script>var puzzleHashes = {{}};</script>

<script>
{THREADS_JS}
</script>

{puzzle_blocks}

<div class="reset-wrap">
  <button class="reset-btn" onclick="resetPuzzles()">Reset All Puzzles</button>
</div>

<script>
"use strict";

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

function resetPuzzles() {{
  try {{ localStorage.removeItem(STORAGE_KEY); }} catch(e) {{}}
  window.location.reload();
}}

function init() {{
  if (!window.crypto || !window.crypto.subtle) {{
    document.getElementById("no-crypto").style.display = "block";
    var ids = Object.keys(puzzleHashes);
    for (var i = 0; i < ids.length; i++) revealPuzzle(ids[i]);
    // Also reveal interactive puzzles
    var simIds = Object.keys(threadsSims || {{}});
    for (var j = 0; j < simIds.length; j++) revealPuzzle(simIds[j]);
    return;
  }}
  var solved = getSolved();
  for (var id in solved) {{
    if (solved[id]) revealPuzzle(id);
  }}
  updateCount();

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
