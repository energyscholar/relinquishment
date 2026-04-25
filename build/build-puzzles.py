#!/usr/bin/env python3
"""Build standalone puzzle preview page from puzzle-data.yaml (Plan 0249)."""

import yaml, html as htmlmod, os, json, hashlib, random

YAML_PATH = os.path.join(os.path.dirname(__file__), 'puzzle-data.yaml')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'downloads', 'puzzles.html')

with open(YAML_PATH) as f:
    data = yaml.safe_load(f)


def esc(s):
    return htmlmod.escape(str(s), quote=True)


def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()


def normalize(s):
    s = s.lower().strip()
    while s and s[-1] in '.,!?;:':
        s = s[:-1]
    for art in ['a ', 'an ', 'the ']:
        if s.startswith(art):
            s = s[len(art):]
    return s.strip()


def build_json(puzzle):
    d = {
        'id': puzzle['id'],
        'type': puzzle.get('type', puzzle.get('sub_type', '')),
        'title': puzzle.get('title', ''),
        'question': puzzle.get('question', ''),
        'hint': puzzle.get('hint', ''),
        'abstract': puzzle.get('abstract', '').strip(),
    }
    t = d['type']
    if t == 'mc':
        d['options'] = puzzle['options']
        d['hashes'] = [sha256(str(puzzle['answer_key']))]
    elif t == 'ti':
        d['hashes'] = [sha256(normalize(s)) for s in puzzle['answer_texts']]
    elif t == 'ord':
        d['items'] = puzzle['items']
        rng = random.Random(puzzle['id'])
        indices = list(range(len(puzzle['items'])))
        rng.shuffle(indices)
        d['shuffle'] = indices
    elif t == 'mat':
        d['left'] = puzzle['left']
        d['right'] = puzzle['right']
        d['pairs'] = puzzle['pairs']
    elif t == 'sim':
        d['sim_type'] = puzzle.get('sim_type', 'threads')
        if d['sim_type'] == 'threads':
            d['hint_threshold'] = puzzle.get('hint_threshold', 12)
        else:
            d['node_count'] = puzzle.get('node_count', 20)
            d['failure_threshold'] = puzzle.get('failure_threshold', 0.8)
            d['hint_after'] = puzzle.get('hint_after', 5)
    elif t == 'cip':
        d['passage'] = puzzle['passage']
        d['slots'] = puzzle['slots']
        d['distractors'] = puzzle['distractors']
    elif t == 'ba':
        d['panel_a'] = puzzle['panel_a']
        d['panel_b'] = puzzle['panel_b']
        d['options'] = puzzle['options']
        d['hashes'] = [sha256(str(puzzle['answer_key']))]
    elif t == 'log':
        d['rows'] = puzzle['rows']
        d['columns'] = puzzle['columns']
        d['correct'] = puzzle['correct']
    return d


# --- Process data ---
chapter_puzzles = data['chapter_puzzles']
puzzle_data = {}
for p in chapter_puzzles:
    puzzle_data[p['id']] = build_json(p)

bridge = data['bridge_builder']
bridge_puzzles = bridge['puzzles']
for bp in bridge_puzzles:
    bp_copy = dict(bp)
    bp_copy['type'] = bp['sub_type']
    d = build_json(bp_copy)
    d['bridge'] = True
    d['edges'] = bp.get('edges', [])
    d['tier'] = bp.get('tier', 0)
    d['tier_label'] = bp.get('tier_label', '')
    d['final_transition'] = bp.get('final_transition', False)
    d['tqc_pulse'] = bp.get('tqc_pulse', False)
    puzzle_data[bp['id']] = d

bridge_data = {
    'nodes': bridge['nodes'],
    'cluster_colors': bridge['cluster_colors'],
    'puzzles': [{'id': bp['id'], 'edges': bp.get('edges', []),
                 'tier_label': bp.get('tier_label', ''),
                 'final_transition': bp.get('final_transition', False)}
                for bp in bridge_puzzles]
}


# --- Generate container HTML ---
def render_container(puzzle):
    pid = esc(puzzle['id'])
    title = esc(puzzle.get('title', ''))
    question = esc(puzzle.get('question', ''))
    abstract_text = esc(puzzle.get('abstract', '').strip())
    hint_text = esc(puzzle.get('hint', ''))
    ptype = puzzle.get('type', puzzle.get('sub_type', ''))
    return f'''<div class="puzzle-container" id="{pid}" data-puzzle-id="{pid}" data-puzzle-type="{ptype}">
  <h2>{title}</h2>
  <p class="question">{question}</p>
  <div class="interaction"></div>
  <p class="hint" id="hint-{pid}">{hint_text}</p>
  <div class="result" id="result-{pid}">
    <div class="solved-badge">&#10003; Solved</div>
    <blockquote class="abstract">{abstract_text}</blockquote>
  </div>
  <noscript><p class="puzzle-fallback">Enable JavaScript to interact with this puzzle.</p></noscript>
</div>'''


chapter_html = '\n'.join(render_container(p) for p in chapter_puzzles)
bridge_puzzle_html = '\n'.join(render_container(bp) for bp in bridge_puzzles)

bridge_abstract = esc(bridge['abstract'].strip())
bridge_section = f'''<hr>
<h1>{esc(bridge['title'])}</h1>
<p class="framing">{esc(bridge['intro'])}</p>
<p class="progress">Bridges: <span id="bridge-count">0</span>/{len(bridge_puzzles)}</p>
<div id="bridge-svg-wrap">
  <svg id="bridge-svg" viewBox="0 0 600 400"></svg>
</div>
{bridge_puzzle_html}
<div class="result" id="result-bridge-final">
  <div class="solved-badge">&#10003; All Bridges Complete</div>
  <blockquote class="abstract">{bridge_abstract}</blockquote>
</div>'''

chapter_count = len(chapter_puzzles)
bridge_count = len(bridge_puzzles)

# --- CSS (standalone page — scoped styles for future monolith) ---
CSS = """
*, *::before, *::after { box-sizing: border-box; }
body { font-family: Georgia, "Times New Roman", serif; line-height: 1.6; color: #1a1a1a; max-width: 42em; margin: 0 auto; padding: 1.5em; background: #fff; }
h1 { font-size: 1.8em; margin-bottom: 0.2em; letter-spacing: 0.03em; }
h2 { font-size: 1.3em; margin-top: 0; color: #1a5276; }
hr { border: none; border-top: 1px solid #ccc; margin: 3em 0 2em; }
.framing { font-style: italic; color: #555; margin-bottom: 0.3em; }
.progress { font-size: 1.1em; font-weight: bold; margin-bottom: 2em; color: #1a5276; }

.puzzle-container { border: 1px solid #ddd; border-radius: 6px; padding: 1.5em; margin-bottom: 2em; background: #fafafa; }
.puzzle-container.solved { border-color: #2a9b9a; background: #f0faf9; }
.question { font-size: 1.05em; margin-bottom: 1em; }

.option-btn { display: block; width: 100%; text-align: left; font-family: Georgia, "Times New Roman", serif; font-size: 1em; padding: 0.7em 1em; margin-bottom: 0.5em; border: 1px solid #ccc; border-radius: 4px; background: #fff; cursor: pointer; transition: border-color 0.2s, background 0.2s; }
.option-btn:hover { border-color: #1a5276; background: #f0f6fa; }
.option-btn.wrong { border-color: #c0392b; background: #fdf2f2; animation: shake 0.3s ease-in-out; }
.option-btn.correct { border-color: #2a9b9a; background: #e8f8f5; font-weight: bold; }
@keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-4px); } 75% { transform: translateX(4px); } }

.text-input-wrap { display: flex; gap: 0.5em; margin-bottom: 0.5em; }
.text-input-wrap input { flex: 1; font-family: Georgia, "Times New Roman", serif; font-size: 1em; padding: 0.6em 0.8em; border: 1px solid #ccc; border-radius: 4px; }
.text-input-wrap input:focus { outline: none; border-color: #1a5276; }
.submit-btn { font-family: Georgia, "Times New Roman", serif; font-size: 1em; padding: 0.6em 1.2em; border: 1px solid #1a5276; border-radius: 4px; background: #1a5276; color: #fff; cursor: pointer; }
.submit-btn:hover { background: #154360; }
.submit-btn:disabled { opacity: 0.5; cursor: default; }

.hint { display: none; color: #856404; background: #fff9e6; border-left: 3px solid #d4a14b; padding: 0.6em 1em; margin-top: 0.5em; font-style: italic; }
.hint.visible { display: block; }
.result { display: none; margin-top: 1em; }
.result.visible { display: block; }
.solved-badge { color: #2a9b9a; font-weight: bold; font-size: 1.1em; margin-bottom: 0.5em; }
.abstract { border-left: 3px solid #2a9b9a; padding: 0.8em 1em; margin: 0; background: #f0faf9; font-style: italic; color: #333; line-height: 1.5; }

.ord-item { display: flex; align-items: center; gap: 0.5em; padding: 0.5em 0.8em; margin-bottom: 0.4em; border: 1px solid #ccc; border-radius: 4px; background: #fff; }
.ord-item.wrong { border-color: #c0392b; background: #fdf2f2; animation: shake 0.3s ease-in-out; }
.ord-text { flex: 1; font-size: 0.95em; }
.ord-arrows { display: flex; flex-direction: column; gap: 2px; }
.ord-arrows button { font-size: 0.8em; padding: 0.15em 0.5em; border: 1px solid #ccc; border-radius: 3px; background: #f5f5f5; cursor: pointer; line-height: 1; }
.ord-arrows button:hover { background: #e0e0e0; }

.mat-wrap { position: relative; display: flex; gap: 2em; justify-content: center; }
.mat-col { display: flex; flex-direction: column; gap: 0.5em; min-width: 40%; }
.mat-item { padding: 0.5em 0.8em; border: 1px solid #ccc; border-radius: 4px; background: #fff; cursor: pointer; text-align: center; font-size: 0.9em; transition: border-color 0.2s, opacity 0.3s; }
.mat-item.selected { border-color: #1a5276; background: #f0f6fa; }
.mat-item.matched { border-color: #2a9b9a; background: #e8f8f5; opacity: 0.6; cursor: default; }
.mat-item.wrong-flash { border-color: #c0392b; background: #fdf2f2; animation: shake 0.3s ease-in-out; }

.sim-svg { width: 100%; max-width: 400px; height: auto; border: 1px solid #ddd; border-radius: 4px; background: #fff; display: block; margin: 0 auto 0.8em; }
.sim-controls { display: flex; align-items: center; gap: 1em; justify-content: center; margin-bottom: 0.5em; }
.sim-status { font-size: 0.95em; color: #555; }
.node-circle { transition: fill 0.3s ease; }
.node-circle.glow { filter: drop-shadow(0 0 6px currentColor); }
.transition-flash { display: none; text-align: center; font-size: 1.3em; font-weight: bold; color: #2a9b9a; padding: 0.5em; animation: pulse 0.6s ease-in-out 3; }
.transition-flash.visible { display: block; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.7; transform: scale(1.05); } }

.cip-passage { font-size: 1em; line-height: 1.8; margin-bottom: 1em; }
.cip-slot { display: inline-block; min-width: 8em; padding: 0.2em 0.5em; border-bottom: 2px dashed #1a5276; cursor: pointer; color: #1a5276; font-weight: bold; text-align: center; transition: background 0.2s; }
.cip-slot.active { background: #f0f6fa; border-color: #c0392b; }
.cip-slot.filled { border-bottom-style: solid; color: #2a9b9a; border-color: #2a9b9a; }
.cip-slot.wrong-flash { background: #fdf2f2; border-color: #c0392b; }
.word-bank { display: flex; flex-wrap: wrap; gap: 0.5em; margin-top: 1em; }
.word-bank-item { padding: 0.4em 0.8em; border: 1px solid #ccc; border-radius: 4px; background: #fff; cursor: pointer; font-size: 0.9em; }
.word-bank-item:hover { border-color: #1a5276; }
.word-bank-item.used { opacity: 0.3; cursor: default; }

.ba-panels { display: flex; gap: 1em; margin-bottom: 1em; }
.ba-panel { flex: 1; border: 1px solid #ccc; border-radius: 4px; padding: 1em; background: #fff; }
.ba-panel h3 { margin: 0 0 0.5em; font-size: 1em; color: #1a5276; }
.ba-prompt { font-family: monospace; font-size: 0.85em; background: #f5f5f5; padding: 0.4em 0.6em; border-radius: 3px; margin-bottom: 0.5em; }
.ba-response { font-style: italic; font-size: 0.9em; line-height: 1.5; }

.log-table { width: 100%; border-collapse: collapse; margin-bottom: 1em; font-size: 0.9em; }
.log-table th { padding: 0.5em; border: 1px solid #ccc; background: #f5f5f5; font-weight: bold; text-align: center; font-size: 0.85em; }
.log-table td { padding: 0.5em; border: 1px solid #ccc; text-align: center; cursor: pointer; min-width: 3em; font-size: 1.2em; user-select: none; }
.log-table td:first-child { text-align: left; cursor: default; font-size: 0.85em; font-weight: normal; }
.log-table td:hover:not(:first-child) { background: #f0f6fa; }
.log-table td.wrong { background: #fdf2f2; border-color: #c0392b; }

#bridge-svg-wrap { margin: 1em 0; }
#bridge-svg { width: 100%; max-width: 600px; height: 300px; border: 1px solid #ddd; border-radius: 4px; background: #fafafa; display: block; margin: 0 auto; }
.bridge-label { font-size: 9px; fill: #333; text-anchor: middle; pointer-events: none; }
.bridge-edge { stroke: #999; stroke-width: 1.5; stroke-opacity: 0.6; }
.bridge-tier-label { font-size: 11px; fill: #1a5276; font-weight: bold; text-anchor: middle; opacity: 0; transition: opacity 0.5s; }
.bridge-tier-label.visible { opacity: 1; }

.reset-wrap { text-align: center; margin: 2em 0 1em; }
.reset-btn { font-family: Georgia, "Times New Roman", serif; font-size: 0.9em; padding: 0.5em 1.2em; border: 1px solid #ccc; border-radius: 4px; background: #fff; color: #888; cursor: pointer; transition: color 0.2s, border-color 0.2s; }
.reset-btn:hover { color: #c0392b; border-color: #c0392b; }
.puzzle-fallback { color: #856404; font-style: italic; }
.no-crypto { background: #fff3cd; border: 1px solid #d4a14b; padding: 1em; border-radius: 4px; margin-bottom: 2em; }

@media (prefers-color-scheme: dark) {
  body { background: #1a1a1a; color: #e0e0e0; }
  h2 { color: #6ba3f7; }
  hr { border-color: #444; }
  .framing { color: #aaa; }
  .progress { color: #6ba3f7; }
  .puzzle-container { background: #242424; border-color: #444; }
  .puzzle-container.solved { background: #1a2e2d; border-color: #2a9b9a; }
  .option-btn { background: #2a2a2a; border-color: #555; color: #e0e0e0; }
  .option-btn:hover { background: #1e3a50; border-color: #6ba3f7; }
  .option-btn.wrong { background: #3a1a1a; border-color: #c0392b; }
  .option-btn.correct { background: #1a3a35; border-color: #2a9b9a; }
  .text-input-wrap input { background: #2a2a2a; color: #e0e0e0; border-color: #555; }
  .text-input-wrap input:focus { border-color: #6ba3f7; }
  .submit-btn { background: #2a6496; border-color: #2a6496; }
  .hint { background: #2a2510; color: #f0d060; border-left-color: #d4a14b; }
  .abstract { background: #1a2e2d; color: #ccc; }
  .no-crypto { background: #2a2510; border-color: #d4a14b; color: #f0d060; }
  .sim-svg, #bridge-svg { background: #2a2a2a; border-color: #555; }
  .sim-status { color: #aaa; }
  .reset-btn { background: #2a2a2a; border-color: #555; color: #888; }
  .reset-btn:hover { color: #e74c3c; border-color: #e74c3c; }
  .ord-item { background: #2a2a2a; border-color: #555; color: #e0e0e0; }
  .ord-arrows button { background: #333; border-color: #555; color: #e0e0e0; }
  .mat-item { background: #2a2a2a; border-color: #555; color: #e0e0e0; }
  .ba-panel { background: #2a2a2a; border-color: #555; }
  .ba-panel h3 { color: #6ba3f7; }
  .ba-prompt { background: #333; color: #e0e0e0; }
  .ba-response { color: #ccc; }
  .log-table th { background: #333; border-color: #555; color: #e0e0e0; }
  .log-table td { border-color: #555; color: #e0e0e0; }
  .log-table td:hover:not(:first-child) { background: #1e3a50; }
  .cip-slot { border-color: #6ba3f7; color: #6ba3f7; }
  .cip-slot.filled { color: #2a9b9a; border-color: #2a9b9a; }
  .word-bank-item { background: #2a2a2a; border-color: #555; color: #e0e0e0; }
  .bridge-label { fill: #ccc; }
  #bridge-svg { background: #242424; }
}

@media (max-width: 600px) {
  body { padding: 0.8em; font-size: 16px; }
  h1 { font-size: 1.4em; }
  .puzzle-container { padding: 1em; }
  .text-input-wrap { flex-direction: column; }
  .option-btn, .submit-btn { min-height: 44px; }
  .sim-svg { max-width: 100%; }
  .ba-panels { flex-direction: column; }
  .mat-wrap { flex-direction: column; gap: 1em; }
  .log-table { font-size: 0.8em; }
  .log-table th, .log-table td:first-child { font-size: 0.75em; }
  .cip-slot { min-width: 6em; font-size: 0.85em; }
  .word-bank-item { font-size: 0.8em; }
}
"""

# --- JS puzzle engine (all 8 types + Bridge Builder) ---
JS_ENGINE = r"""
"use strict";
var INIT_DELAY = 100;
var STORAGE_KEY = "relinquishment-puzzles-solved";
var BRIDGE_KEY = "relinquishment-bridge-state";
var PD = __PUZZLE_DATA__;
var BD = __BRIDGE_DATA__;
var hasCrypto = !!(window.crypto && window.crypto.subtle);

function getSolved() { try { var s = localStorage.getItem(STORAGE_KEY); return s ? JSON.parse(s) : {}; } catch(e) { return {}; } }
function setSolved(id) { try { var s = getSolved(); s[id] = true; localStorage.setItem(STORAGE_KEY, JSON.stringify(s)); } catch(e) {} }
function getBridgeSolved() { try { var s = localStorage.getItem(BRIDGE_KEY); return s ? JSON.parse(s) : []; } catch(e) { return []; } }
function addBridgeSolved(id) { try { var a = getBridgeSolved(); if (a.indexOf(id) === -1) a.push(id); localStorage.setItem(BRIDGE_KEY, JSON.stringify(a)); } catch(e) {} }

function updateCounts() {
  var solved = getSolved(), nc = 0, nb = 0;
  for (var k in solved) { if (!solved[k]) continue; if (k.indexOf("bridge") !== -1) nb++; else nc++; }
  var ce = document.getElementById("chapter-count");
  var be = document.getElementById("bridge-count");
  if (ce) ce.textContent = nc;
  if (be) be.textContent = nb;
}

function revealPuzzle(id) {
  var el = document.getElementById(id);
  if (!el) return;
  el.classList.add("solved");
  var inter = el.querySelector(".interaction");
  if (inter) inter.style.display = "none";
  var hint = document.getElementById("hint-" + id);
  if (hint) hint.classList.remove("visible");
  var result = document.getElementById("result-" + id);
  if (result) result.classList.add("visible");
  setSolved(id);
  if (id.indexOf("bridge") !== -1) {
    addBridgeSolved(id);
    updateBridgeSVG();
    var bs = getBridgeSolved();
    if (bs.length >= BD.puzzles.length) {
      var rf = document.getElementById("result-bridge-final");
      if (rf) rf.classList.add("visible");
    }
  }
  updateCounts();
}

function showHint(id) {
  var h = document.getElementById("hint-" + id);
  if (h) h.classList.add("visible");
}

function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

async function sha256(msg) {
  var buf = new TextEncoder().encode(msg);
  var hash = await crypto.subtle.digest("SHA-256", buf);
  return Array.from(new Uint8Array(hash)).map(function(b) { return b.toString(16).padStart(2, "0"); }).join("");
}

function normalize(s) {
  s = s.toLowerCase().trim().replace(/[.,!?;:]+$/g, "").replace(/^(a |an |the )/, "");
  return s.trim();
}

/* --- MC --- */
function initMC(el, d) {
  var inter = el.querySelector(".interaction");
  var html = "";
  for (var i = 0; i < d.options.length; i++) {
    var o = d.options[i];
    html += '<button class="option-btn" data-key="' + esc(o.key) + '">(' + esc(o.key) + ') ' + esc(o.text) + "</button>";
  }
  inter.innerHTML = html;
  var btns = inter.querySelectorAll(".option-btn");
  for (var j = 0; j < btns.length; j++) {
    (function(btn) {
      btn.addEventListener("click", function() { checkMC(d.id, btn.dataset.key, btn); });
    })(btns[j]);
  }
}

async function checkMC(id, key, btn) {
  if (getSolved()[id]) return;
  if (!hasCrypto) { revealPuzzle(id); return; }
  var h = await sha256(key);
  if (PD[id].hashes.indexOf(h) !== -1) {
    btn.classList.add("correct");
    setTimeout(function() { revealPuzzle(id); }, 400);
  } else {
    btn.classList.add("wrong");
    setTimeout(function() { btn.classList.remove("wrong"); }, 600);
    showHint(id);
  }
}

/* --- TI --- */
function initTI(el, d) {
  var inter = el.querySelector(".interaction");
  inter.innerHTML = '<div class="text-input-wrap"><input type="text" id="input-' + d.id + '" placeholder="Type your answer…"><button class="submit-btn">Check</button></div>';
  var btn = inter.querySelector(".submit-btn");
  var inp = inter.querySelector("input");
  btn.addEventListener("click", function() { checkTI(d.id); });
  inp.addEventListener("keydown", function(e) { if (e.key === "Enter") checkTI(d.id); });
}

async function checkTI(id) {
  if (getSolved()[id]) return;
  var inp = document.getElementById("input-" + id);
  if (!inp) return;
  var val = normalize(inp.value);
  if (!val) return;
  if (!hasCrypto) { revealPuzzle(id); return; }
  var h = await sha256(val);
  if (PD[id].hashes.indexOf(h) !== -1) {
    inp.style.borderColor = "#2a9b9a";
    setTimeout(function() { revealPuzzle(id); }, 400);
  } else {
    inp.style.borderColor = "#c0392b";
    setTimeout(function() { inp.style.borderColor = ""; }, 600);
    showHint(id);
  }
}

/* --- ORD --- */
function initORD(el, d) {
  var inter = el.querySelector(".interaction");
  var order = d.shuffle.slice();
  function render() {
    var html = "";
    for (var i = 0; i < order.length; i++) {
      html += '<div class="ord-item" data-pos="' + i + '"><div class="ord-arrows">' +
        '<button data-dir="up" data-pos="' + i + '">▲</button>' +
        '<button data-dir="down" data-pos="' + i + '">▼</button></div>' +
        '<span class="ord-text">' + esc(d.items[order[i]]) + "</span></div>";
    }
    html += '<button class="submit-btn ord-submit">Check Order</button>';
    inter.innerHTML = html;
    var arrows = inter.querySelectorAll(".ord-arrows button");
    for (var j = 0; j < arrows.length; j++) {
      (function(btn) {
        btn.addEventListener("click", function() {
          var p = parseInt(btn.dataset.pos), dir = btn.dataset.dir;
          if (dir === "up" && p > 0) { var t = order[p]; order[p] = order[p-1]; order[p-1] = t; }
          if (dir === "down" && p < order.length-1) { var t = order[p]; order[p] = order[p+1]; order[p+1] = t; }
          render();
        });
      })(arrows[j]);
    }
    inter.querySelector(".ord-submit").addEventListener("click", function() {
      var ok = true;
      for (var i = 0; i < order.length; i++) if (order[i] !== i) { ok = false; break; }
      if (ok) { revealPuzzle(d.id); return; }
      var items = inter.querySelectorAll(".ord-item");
      for (var i = 0; i < order.length; i++) if (order[i] !== i) items[i].classList.add("wrong");
      setTimeout(function() { var its = inter.querySelectorAll(".ord-item.wrong"); for (var k = 0; k < its.length; k++) its[k].classList.remove("wrong"); }, 800);
      showHint(d.id);
    });
  }
  render();
}

/* --- MAT --- */
function initMAT(el, d) {
  var inter = el.querySelector(".interaction");
  var rightOrder = d.right.slice();
  for (var i = rightOrder.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var t = rightOrder[i]; rightOrder[i] = rightOrder[j]; rightOrder[j] = t;
  }
  var matched = {}, selected = null;
  var html = '<div class="mat-wrap"><div class="mat-col">';
  for (var i = 0; i < d.left.length; i++)
    html += '<div class="mat-item mat-l" data-key="' + esc(d.left[i].key) + '">' + esc(d.left[i].text) + "</div>";
  html += '</div><div class="mat-col">';
  for (var i = 0; i < rightOrder.length; i++)
    html += '<div class="mat-item mat-r" data-key="' + esc(rightOrder[i].key) + '">' + esc(rightOrder[i].text) + "</div>";
  html += "</div></div>";
  inter.innerHTML = html;

  var lefts = inter.querySelectorAll(".mat-l");
  var rights = inter.querySelectorAll(".mat-r");
  for (var j = 0; j < lefts.length; j++) {
    (function(item) {
      item.addEventListener("click", function() {
        if (matched[item.dataset.key]) return;
        for (var k = 0; k < lefts.length; k++) lefts[k].classList.remove("selected");
        item.classList.add("selected");
        selected = item.dataset.key;
      });
    })(lefts[j]);
  }
  for (var j = 0; j < rights.length; j++) {
    (function(item) {
      item.addEventListener("click", function() {
        if (!selected || matched[selected]) return;
        if (d.pairs[selected] === item.dataset.key) {
          matched[selected] = true;
          var lItem = inter.querySelector('.mat-l[data-key="' + selected + '"]');
          lItem.classList.remove("selected"); lItem.classList.add("matched");
          item.classList.add("matched");
          selected = null;
          if (Object.keys(matched).length === d.left.length)
            setTimeout(function() { revealPuzzle(d.id); }, 400);
        } else {
          item.classList.add("wrong-flash");
          setTimeout(function() { item.classList.remove("wrong-flash"); }, 600);
          showHint(d.id);
        }
      });
    })(rights[j]);
  }
}

/* --- SIM: Threads --- */
var threadsSims = {};
var CLUSTER_COLORS = ["#2a9b9a","#c0392b","#8b5fc0","#d4a14b","#1a5276","#27ae60","#e67e22","#2980b9"];

function ufFind(nodes, i) { if (nodes[i].parent !== i) nodes[i].parent = ufFind(nodes, nodes[i].parent); return nodes[i].parent; }
function ufUnion(nodes, a, b) { var ra = ufFind(nodes, a), rb = ufFind(nodes, b); if (ra === rb) return; if (nodes[ra].rank < nodes[rb].rank) { var t = ra; ra = rb; rb = t; } nodes[rb].parent = ra; if (nodes[ra].rank === nodes[rb].rank) nodes[ra].rank++; }
function getClusters(nodes) { var m = {}; for (var i = 0; i < nodes.length; i++) { var r = ufFind(nodes, i); if (!m[r]) m[r] = []; m[r].push(i); } return m; }
function largestCluster(nodes) { var c = getClusters(nodes), mx = 0; for (var k in c) if (c[k].length > mx) mx = c[k].length; return mx; }

function initThreads(el, d) {
  var N = 16, W = 400, H = 300, R = 12;
  var nodes = [];
  for (var i = 0; i < N; i++) nodes.push({ x: R + Math.random()*(W-2*R), y: R + Math.random()*(H-2*R), parent: i, rank: 0 });
  var allEdges = [];
  for (var a = 0; a < N; a++) for (var b = a+1; b < N; b++) allEdges.push([a,b]);
  for (var i = allEdges.length-1; i > 0; i--) { var j = Math.floor(Math.random()*(i+1)); var t = allEdges[i]; allEdges[i] = allEdges[j]; allEdges[j] = t; }
  var sim = { id: d.id, nodes: nodes, edges: [], q: allEdges, qi: 0, tc: 0, solved: false, ht: d.hint_threshold || 12 };
  threadsSims[d.id] = sim;
  var inter = el.querySelector(".interaction");
  inter.innerHTML = '<svg id="svg-' + d.id + '" viewBox="0 0 400 300" class="sim-svg"></svg>' +
    '<div class="sim-controls"><button class="submit-btn" id="add-' + d.id + '">Add Thread</button>' +
    '<span class="sim-status" id="tc-' + d.id + '">Threads: 0</span></div>' +
    '<div class="transition-flash" id="flash-' + d.id + '">Phase Transition!</div>';
  document.getElementById("add-" + d.id).addEventListener("click", function() { addThread(d.id); });
  renderTSvg(sim);
}

function renderTSvg(sim) {
  var svg = document.getElementById("svg-" + sim.id);
  if (!svg) return;
  var clusters = getClusters(sim.nodes), nc = {}, ci = 0;
  for (var r in clusters) { var col = CLUSTER_COLORS[ci++ % CLUSTER_COLORS.length]; clusters[r].forEach(function(j) { nc[j] = col; }); }
  var p = [];
  sim.edges.forEach(function(e) { var a = sim.nodes[e[0]], b = sim.nodes[e[1]]; p.push('<line x1="'+a.x+'" y1="'+a.y+'" x2="'+b.x+'" y2="'+b.y+'" stroke="#999" stroke-width="1.5" stroke-opacity="0.6"/>'); });
  sim.nodes.forEach(function(n, i) { var gl = sim.solved && largestCluster(sim.nodes) > 8 ? " glow" : ""; p.push('<circle cx="'+n.x+'" cy="'+n.y+'" r="12" fill="'+(nc[i]||"#ccc")+'" stroke="#fff" stroke-width="1.5" class="node-circle'+gl+'"/>'); });
  svg.innerHTML = p.join("\n");
}

function addThread(id) {
  var sim = threadsSims[id];
  if (!sim || sim.solved || sim.qi >= sim.q.length) return;
  var e = sim.q[sim.qi++]; sim.edges.push(e); ufUnion(sim.nodes, e[0], e[1]); sim.tc++;
  document.getElementById("tc-" + id).textContent = "Threads: " + sim.tc;
  renderTSvg(sim);
  if (sim.tc >= sim.ht && largestCluster(sim.nodes) < 9) showHint(id);
  if (largestCluster(sim.nodes) >= 9) {
    sim.solved = true; renderTSvg(sim);
    var fl = document.getElementById("flash-" + id); if (fl) fl.classList.add("visible");
    var btn = document.getElementById("add-" + id); if (btn) btn.disabled = true;
    setTimeout(function() { if (fl) fl.classList.remove("visible"); revealPuzzle(id); }, 1800);
  }
}

/* --- SIM: Resilience --- */
function initResilience(el, d) {
  var N = d.node_count || 20, COLS = 5, ROWS = 4, W = 400, H = 300;
  var nodes = [], edges = [], alive = [];
  for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
    nodes.push({ x: 40 + c*(W-80)/(COLS-1), y: 40 + r*(H-80)/(ROWS-1) }); alive.push(true);
  }
  for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
    var i = r*COLS + c;
    if (c < COLS-1) edges.push([i, i+1]);
    if (r < ROWS-1) edges.push([i, i+COLS]);
    if (c < COLS-1 && r < ROWS-1) edges.push([i, i+COLS+1]);
    if (c > 0 && r < ROWS-1) edges.push([i, i+COLS-1]);
  }
  var destroyed = 0, solved = false, failAt = Math.ceil(N * (d.failure_threshold || 0.8)), hintAt = d.hint_after || 5;
  var inter = el.querySelector(".interaction");
  inter.innerHTML = '<svg id="svg-' + d.id + '" viewBox="0 0 400 300" class="sim-svg"></svg>' +
    '<div class="sim-controls"><span class="sim-status" id="st-' + d.id + '">Destroyed: 0/' + N + ' — Network: OPERATIONAL</span></div>' +
    '<div class="transition-flash" id="flash-' + d.id + '" style="color:#c0392b">Network: FAILED</div>';

  function bfsConnected() {
    var an = []; for (var i = 0; i < N; i++) if (alive[i]) an.push(i);
    if (an.length <= 1) return true;
    var vis = {}, q = [an[0]]; vis[an[0]] = true;
    while (q.length) { var nd = q.shift(); for (var e = 0; e < edges.length; e++) { var nb = -1; if (edges[e][0] === nd && alive[edges[e][1]]) nb = edges[e][1]; if (edges[e][1] === nd && alive[edges[e][0]]) nb = edges[e][0]; if (nb !== -1 && !vis[nb]) { vis[nb] = true; q.push(nb); } } }
    return Object.keys(vis).length === an.length;
  }

  function render() {
    var svg = document.getElementById("svg-" + d.id); if (!svg) return;
    var p = [];
    edges.forEach(function(e) { if (alive[e[0]] && alive[e[1]]) p.push('<line x1="'+nodes[e[0]].x+'" y1="'+nodes[e[0]].y+'" x2="'+nodes[e[1]].x+'" y2="'+nodes[e[1]].y+'" stroke="#2a9b9a" stroke-width="1.5" stroke-opacity="0.4"/>'); });
    nodes.forEach(function(n, i) {
      if (alive[i]) p.push('<circle cx="'+n.x+'" cy="'+n.y+'" r="12" fill="#2a9b9a" stroke="#fff" stroke-width="1.5" class="node-circle" data-n="'+i+'" style="cursor:pointer"/>');
      else p.push('<circle cx="'+n.x+'" cy="'+n.y+'" r="12" fill="#555" stroke="#888" stroke-width="1" opacity="0.3"/>');
    });
    svg.innerHTML = p.join("\n");
    var circles = svg.querySelectorAll("circle[data-n]");
    for (var j = 0; j < circles.length; j++) {
      (function(c) { c.addEventListener("click", function() {
        if (solved) return;
        alive[parseInt(c.dataset.n)] = false; destroyed++;
        render();
        if (destroyed >= hintAt && destroyed < failAt) showHint(d.id);
        if (!bfsConnected() || destroyed >= failAt) {
          solved = true;
          document.getElementById("st-" + d.id).textContent = "Destroyed: " + destroyed + "/" + N + " — Network: FAILED";
          var fl = document.getElementById("flash-" + d.id); if (fl) fl.classList.add("visible");
          setTimeout(function() { if (fl) fl.classList.remove("visible"); revealPuzzle(d.id); }, 1800);
        } else {
          document.getElementById("st-" + d.id).textContent = "Destroyed: " + destroyed + "/" + N + " — Network: OPERATIONAL";
        }
      }); })(circles[j]);
    }
  }
  render();
}

/* --- CIP --- */
function initCIP(el, d) {
  var inter = el.querySelector(".interaction");
  var activeSlot = null, filled = {};
  var passHtml = esc(d.passage);
  for (var i = 0; i < d.slots.length; i++) {
    var s = d.slots[i], tag = "[REDACTED-" + s.id + "]";
    passHtml = passHtml.replace(tag, '<span class="cip-slot" data-slot="' + s.id + '">[' + s.id + ']</span>');
  }
  var allTerms = d.slots.map(function(s) { return s.answer; }).concat(d.distractors);
  for (var i = allTerms.length-1; i > 0; i--) { var j = Math.floor(Math.random()*(i+1)); var t = allTerms[i]; allTerms[i] = allTerms[j]; allTerms[j] = t; }
  var bankHtml = '<div class="word-bank">';
  allTerms.forEach(function(term) { bankHtml += '<span class="word-bank-item" data-term="' + esc(term) + '">' + esc(term) + "</span>"; });
  bankHtml += "</div>";
  inter.innerHTML = '<div class="cip-passage">' + passHtml + "</div>" + bankHtml;

  var slots = inter.querySelectorAll(".cip-slot");
  for (var j = 0; j < slots.length; j++) {
    (function(sl) { sl.addEventListener("click", function() {
      for (var k = 0; k < slots.length; k++) slots[k].classList.remove("active");
      if (filled[sl.dataset.slot]) return;
      sl.classList.add("active"); activeSlot = sl.dataset.slot;
    }); })(slots[j]);
  }
  var bankItems = inter.querySelectorAll(".word-bank-item");
  for (var j = 0; j < bankItems.length; j++) {
    (function(item) { item.addEventListener("click", function() {
      if (!activeSlot || item.classList.contains("used")) return;
      var term = item.dataset.term;
      var slotData = null;
      for (var k = 0; k < d.slots.length; k++) if (String(d.slots[k].id) === activeSlot) { slotData = d.slots[k]; break; }
      var slotEl = inter.querySelector('.cip-slot[data-slot="' + activeSlot + '"]');
      if (slotData && slotData.answer === term) {
        slotEl.textContent = term; slotEl.classList.remove("active"); slotEl.classList.add("filled");
        item.classList.add("used"); filled[activeSlot] = true; activeSlot = null;
        if (Object.keys(filled).length === d.slots.length) setTimeout(function() { revealPuzzle(d.id); }, 400);
      } else {
        slotEl.classList.add("wrong-flash");
        setTimeout(function() { slotEl.classList.remove("wrong-flash"); }, 600);
        showHint(d.id);
      }
    }); })(bankItems[j]);
  }
}

/* --- BA --- */
function initBA(el, d) {
  var inter = el.querySelector(".interaction");
  var html = '<div class="ba-panels">';
  html += '<div class="ba-panel"><h3>' + esc(d.panel_a.label) + '</h3><div class="ba-prompt">&gt; ' + esc(d.panel_a.prompt) + '</div><div class="ba-response">' + esc(d.panel_a.response) + "</div></div>";
  html += '<div class="ba-panel"><h3>' + esc(d.panel_b.label) + '</h3><div class="ba-prompt">&gt; ' + esc(d.panel_b.prompt) + '</div><div class="ba-response">' + esc(d.panel_b.response) + "</div></div>";
  html += "</div>";
  for (var i = 0; i < d.options.length; i++) {
    var o = d.options[i];
    html += '<button class="option-btn" data-key="' + esc(o.key) + '">(' + esc(o.key) + ') ' + esc(o.text) + "</button>";
  }
  inter.innerHTML = html;
  var btns = inter.querySelectorAll(".option-btn");
  for (var j = 0; j < btns.length; j++) {
    (function(btn) { btn.addEventListener("click", function() { checkMC(d.id, btn.dataset.key, btn); }); })(btns[j]);
  }
}

/* --- LOG --- */
function initLOG(el, d) {
  var inter = el.querySelector(".interaction");
  var grid = [];
  for (var r = 0; r < d.rows.length; r++) { grid[r] = []; for (var c = 0; c < d.columns.length; c++) grid[r][c] = null; }

  function render() {
    var html = '<table class="log-table"><thead><tr><th></th>';
    d.columns.forEach(function(col) { html += "<th>" + esc(col) + "</th>"; });
    html += "</tr></thead><tbody>";
    for (var r = 0; r < d.rows.length; r++) {
      html += "<tr><td>" + esc(d.rows[r]) + "</td>";
      for (var c = 0; c < d.columns.length; c++) {
        var v = grid[r][c] === true ? "✓" : (grid[r][c] === false ? "✗" : "");
        html += '<td data-r="' + r + '" data-c="' + c + '">' + v + "</td>";
      }
      html += "</tr>";
    }
    html += '</tbody></table><button class="submit-btn log-submit">Check</button>';
    inter.innerHTML = html;
    var cells = inter.querySelectorAll("td[data-r]");
    for (var j = 0; j < cells.length; j++) {
      (function(td) { td.addEventListener("click", function() {
        var r = parseInt(td.dataset.r), c = parseInt(td.dataset.c);
        if (grid[r][c] === null) grid[r][c] = true;
        else if (grid[r][c] === true) grid[r][c] = false;
        else grid[r][c] = null;
        render();
      }); })(cells[j]);
    }
    inter.querySelector(".log-submit").addEventListener("click", function() {
      var ok = true;
      for (var r = 0; r < d.rows.length; r++) for (var c = 0; c < d.columns.length; c++) {
        if (grid[r][c] !== d.correct[r][c]) {
          ok = false;
          var td = inter.querySelector('td[data-r="' + r + '"][data-c="' + c + '"]');
          if (td) td.classList.add("wrong");
        }
      }
      if (ok) { revealPuzzle(d.id); }
      else { setTimeout(function() { var ws = inter.querySelectorAll("td.wrong"); for (var k = 0; k < ws.length; k++) ws[k].classList.remove("wrong"); }, 800); showHint(d.id); }
    });
  }
  render();
}

/* --- Bridge SVG --- */
function initBridge() {
  if (!BD || !BD.nodes) return;
  updateBridgeSVG();
}

function updateBridgeSVG() {
  var svg = document.getElementById("bridge-svg");
  if (!svg || !BD) return;
  var solved = getBridgeSolved(), solvedSet = {};
  solved.forEach(function(id) { solvedSet[id] = true; });

  var activeEdges = [], tierLabels = [], finalTrans = false;
  BD.puzzles.forEach(function(bp) {
    if (solvedSet[bp.id]) {
      if (bp.edges) activeEdges = activeEdges.concat(bp.edges);
      if (bp.tier_label) tierLabels.push(bp.tier_label);
      if (bp.final_transition) finalTrans = true;
    }
  });

  var nIdx = {}; BD.nodes.forEach(function(n, i) { nIdx[n.id] = i; });
  var uf = BD.nodes.map(function(_, i) { return { parent: i, rank: 0 }; });
  function bfind(i) { if (uf[i].parent !== i) uf[i].parent = bfind(uf[i].parent); return uf[i].parent; }
  function bunion(a, b) { var ra = bfind(a), rb = bfind(b); if (ra === rb) return; if (uf[ra].rank < uf[rb].rank) { var t = ra; ra = rb; rb = t; } uf[rb].parent = ra; if (uf[ra].rank === uf[rb].rank) uf[ra].rank++; }
  activeEdges.forEach(function(e) { var a = nIdx[e[0]], b = nIdx[e[1]]; if (a !== undefined && b !== undefined) bunion(a, b); });

  var clusters = {};
  BD.nodes.forEach(function(_, i) { var r = bfind(i); if (!clusters[r]) clusters[r] = []; clusters[r].push(i); });
  var BASE_Y = 350, MAX_LIFT = 250, parts = [];

  activeEdges.forEach(function(e) {
    var ai = nIdx[e[0]], bi = nIdx[e[1]];
    if (ai === undefined || bi === undefined) return;
    var csz = clusters[bfind(ai)] ? clusters[bfind(ai)].length : 1;
    var ya = BASE_Y - (csz/11)*MAX_LIFT, yb = ya;
    parts.push('<line x1="'+BD.nodes[ai].x+'" y1="'+ya+'" x2="'+BD.nodes[bi].x+'" y2="'+yb+'" class="bridge-edge"/>');
  });

  BD.nodes.forEach(function(n, i) {
    var csz = clusters[bfind(i)] ? clusters[bfind(i)].length : 1;
    var y = BASE_Y - (csz/11)*MAX_LIFT;
    var col = BD.cluster_colors[n.cluster] || "#999";
    var glow = finalTrans ? " glow" : "";
    parts.push('<circle cx="'+n.x+'" cy="'+y+'" r="10" fill="'+col+'" stroke="#fff" stroke-width="1.5" class="node-circle'+glow+'"/>');
    parts.push('<text x="'+n.x+'" y="'+(y-14)+'" class="bridge-label">' + n.label + "</text>");
  });

  tierLabels.forEach(function(label, i) {
    parts.push('<text x="300" y="'+(25 + i*18)+'" class="bridge-tier-label visible">' + label + "</text>");
  });
  svg.innerHTML = parts.join("\n");
}

/* --- Main --- */
function initAllPuzzles() {
  var containers = document.querySelectorAll(".puzzle-container");
  for (var i = 0; i < containers.length; i++) {
    var el = containers[i], id = el.dataset.puzzleId, type = el.dataset.puzzleType;
    var d = PD[id]; if (!d) continue;
    try {
      if (type === "mc") initMC(el, d);
      else if (type === "ti") initTI(el, d);
      else if (type === "ord") initORD(el, d);
      else if (type === "mat") initMAT(el, d);
      else if (type === "sim") { if (d.sim_type === "resilience") initResilience(el, d); else initThreads(el, d); }
      else if (type === "cip") initCIP(el, d);
      else if (type === "ba") initBA(el, d);
      else if (type === "log") initLOG(el, d);
    } catch(e) { console.error("Puzzle init error:", id, e); el.querySelector(".interaction").innerHTML = '<p class="puzzle-fallback">Puzzle failed to load.</p>'; }
  }
  if (!hasCrypto) {
    var nc = document.getElementById("no-crypto"); if (nc) nc.style.display = "block";
    for (var id in PD) revealPuzzle(id);
    return;
  }
  var solved = getSolved();
  for (var id in solved) if (solved[id]) revealPuzzle(id);
  try { initBridge(); } catch(e) { console.error("Bridge init error:", e); }
  updateCounts();
  if (location.hash) { var t = document.querySelector(location.hash); if (t) setTimeout(function() { t.scrollIntoView({behavior:"smooth"}); }, 100); }
}

function resetPuzzles() {
  try { localStorage.removeItem(STORAGE_KEY); localStorage.removeItem(BRIDGE_KEY); } catch(e) {}
  location.reload();
}

window.addEventListener("load", function() { setTimeout(initAllPuzzles, INIT_DELAY); });
"""

# --- Assemble page ---
js_final = JS_ENGINE.replace('__PUZZLE_DATA__', json.dumps(puzzle_data, ensure_ascii=False))
js_final = js_final.replace('__BRIDGE_DATA__', json.dumps(bridge_data, ensure_ascii=False))

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relinquishment &mdash; Puzzle Preview</title>
<style>
{CSS}
</style>
</head>
<body>

<h1>Relinquishment &mdash; Puzzle Preview</h1>
<p class="framing">Each chapter ends with a puzzle. Solve it to reveal
the chapter&rsquo;s Spiral Abstract &mdash; the meta-view that connects the chapter
to the book&rsquo;s larger argument.</p>
<p class="progress">Chapter puzzles: <span id="chapter-count">0</span>/{chapter_count}</p>

<div id="no-crypto" class="no-crypto" style="display:none;">
  <strong>Note:</strong> Your browser does not support the SubtleCrypto API.
  All puzzles are shown unlocked.
</div>

{chapter_html}

{bridge_section}

<div class="reset-wrap">
  <button class="reset-btn" onclick="resetPuzzles()">Reset All Puzzles</button>
</div>

<script>
{js_final}
</script>

</body>
</html>'''

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, 'w') as f:
    f.write(page)

total = chapter_count + bridge_count
print(f"Built {OUT_PATH} ({chapter_count} chapter + {bridge_count} bridge = {total} puzzles)")
