#!/usr/bin/env python3
"""Build standalone puzzle preview page from puzzle-data.yaml (Plan 0249)."""

import yaml, html as htmlmod, os, json, hashlib, random, re

YAML_PATH = os.path.join(os.path.dirname(__file__), 'puzzle-data.yaml')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'downloads', 'puzzles.html')

with open(YAML_PATH) as f:
    data = yaml.safe_load(f)

shared_bgs = data.get('shared_backgrounds', {})

# --- Inline SVG illustrations for puzzles ---
ILLUSTRATIONS = {}

ILLUSTRATIONS['canopy_triptych'] = '''<div class="puzzle-illustration" style="display:flex;gap:8px;justify-content:center;margin:1em 0;">
<figure style="flex:1;max-width:180px;text-align:center;margin:0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" style="width:100%;height:auto;">
  <title>Panel 1: Empty substrate — a seedling grows freely in open sunlight</title>
  <defs>
    <linearGradient id="ct-sky1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef9e7" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fef9e7" stop-opacity="0.3"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="180" height="110" fill="url(#ct-sky1)"/>
  <line x1="30" y1="5" x2="30" y2="95" stroke="#f4d03f" stroke-width="1.5" opacity="0.5"/>
  <line x1="60" y1="3" x2="60" y2="95" stroke="#f4d03f" stroke-width="1.5" opacity="0.6"/>
  <line x1="90" y1="2" x2="90" y2="95" stroke="#f4d03f" stroke-width="1.5" opacity="0.7"/>
  <line x1="120" y1="3" x2="120" y2="95" stroke="#f4d03f" stroke-width="1.5" opacity="0.6"/>
  <line x1="150" y1="5" x2="150" y2="95" stroke="#f4d03f" stroke-width="1.5" opacity="0.5"/>
  <rect x="0" y="110" width="180" height="5" rx="1" fill="#a88b5e" opacity="0.4"/>
  <line x1="90" y1="95" x2="90" y2="110" stroke="#27ae60" stroke-width="2.5"/>
  <ellipse cx="90" cy="90" rx="10" ry="7" fill="#2ecc71" opacity="0.85"/>
  <ellipse cx="85" cy="86" rx="6" ry="5" fill="#82e0aa" opacity="0.7"/>
  <ellipse cx="95" cy="86" rx="6" ry="5" fill="#82e0aa" opacity="0.7"/>
  <text x="90" y="132" text-anchor="middle" fill="#999" font-size="9" font-family="Helvetica,sans-serif">Empty substrate</text>
</svg>
</figure>
<figure style="flex:1;max-width:180px;text-align:center;margin:0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" style="width:100%;height:auto;">
  <title>Panel 2: Full substrate — mature trees fill the canopy, blocking all sunlight</title>
  <defs>
    <linearGradient id="ct-sky2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef9e7" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fef9e7" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ct-shadow2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a2e1a" stop-opacity="0.35"/>
      <stop offset="80%" stop-color="#1a2e1a" stop-opacity="0.12"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="180" height="45" fill="url(#ct-sky2)"/>
  <line x1="30" y1="3" x2="30" y2="18" stroke="#f4d03f" stroke-width="1.2" opacity="0.4"/>
  <line x1="90" y1="2" x2="90" y2="15" stroke="#f4d03f" stroke-width="1.2" opacity="0.5"/>
  <line x1="150" y1="3" x2="150" y2="18" stroke="#f4d03f" stroke-width="1.2" opacity="0.4"/>
  <ellipse cx="50" cy="28" rx="48" ry="20" fill="#27ae60" opacity="0.75"/>
  <ellipse cx="48" cy="26" rx="42" ry="17" fill="#2ecc71" opacity="0.55"/>
  <ellipse cx="135" cy="30" rx="44" ry="19" fill="#27ae60" opacity="0.75"/>
  <ellipse cx="137" cy="28" rx="38" ry="16" fill="#2ecc71" opacity="0.55"/>
  <rect x="42" y="42" width="7" height="68" rx="1.5" fill="#8b6914" opacity="0.8"/>
  <rect x="130" y="44" width="7" height="66" rx="1.5" fill="#8b6914" opacity="0.8"/>
  <rect x="0" y="45" width="180" height="65" fill="url(#ct-shadow2)"/>
  <rect x="0" y="110" width="180" height="5" rx="1" fill="#a88b5e" opacity="0.4"/>
  <text x="90" y="132" text-anchor="middle" fill="#999" font-size="9" font-family="Helvetica,sans-serif">Niche occupied</text>
</svg>
</figure>
<figure style="flex:1;max-width:180px;text-align:center;margin:0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" style="width:100%;height:auto;">
  <title>Panel 3: Full substrate with seedling — a tiny seedling sits in deep shadow beneath the canopy, unable to reach the light</title>
  <defs>
    <linearGradient id="ct-sky3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef9e7" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fef9e7" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ct-shadow3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a2e1a" stop-opacity="0.4"/>
      <stop offset="80%" stop-color="#1a2e1a" stop-opacity="0.15"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="180" height="45" fill="url(#ct-sky3)"/>
  <line x1="30" y1="3" x2="30" y2="18" stroke="#f4d03f" stroke-width="1.2" opacity="0.4"/>
  <line x1="90" y1="2" x2="90" y2="15" stroke="#f4d03f" stroke-width="1.2" opacity="0.5"/>
  <line x1="150" y1="3" x2="150" y2="18" stroke="#f4d03f" stroke-width="1.2" opacity="0.4"/>
  <ellipse cx="50" cy="28" rx="48" ry="20" fill="#27ae60" opacity="0.75"/>
  <ellipse cx="48" cy="26" rx="42" ry="17" fill="#2ecc71" opacity="0.55"/>
  <ellipse cx="135" cy="30" rx="44" ry="19" fill="#27ae60" opacity="0.75"/>
  <ellipse cx="137" cy="28" rx="38" ry="16" fill="#2ecc71" opacity="0.55"/>
  <rect x="42" y="42" width="7" height="68" rx="1.5" fill="#8b6914" opacity="0.8"/>
  <rect x="130" y="44" width="7" height="66" rx="1.5" fill="#8b6914" opacity="0.8"/>
  <rect x="0" y="45" width="180" height="65" fill="url(#ct-shadow3)"/>
  <rect x="0" y="110" width="180" height="5" rx="1" fill="#a88b5e" opacity="0.4"/>
  <!-- The doomed seedling -->
  <line x1="90" y1="103" x2="90" y2="110" stroke="#2ecc71" stroke-width="1.5" opacity="0.5"/>
  <ellipse cx="90" cy="101" rx="4" ry="3" fill="#82e0aa" opacity="0.4"/>
  <ellipse cx="88" cy="99" rx="2.5" ry="2" fill="#82e0aa" opacity="0.3"/>
  <ellipse cx="92" cy="99" rx="2.5" ry="2" fill="#82e0aa" opacity="0.3"/>
  <!-- X mark over seedling -->
  <line x1="84" y1="95" x2="96" y2="112" stroke="#c0392b" stroke-width="1.5" opacity="0.6"/>
  <line x1="96" y1="95" x2="84" y2="112" stroke="#c0392b" stroke-width="1.5" opacity="0.6"/>
  <text x="90" y="132" text-anchor="middle" fill="#999" font-size="9" font-family="Helvetica,sans-serif">Too late</text>
</svg>
</figure>
</div>'''


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


def resolve_background(raw):
    if not raw:
        return ''
    raw = str(raw).strip()
    def repl(m):
        return shared_bgs.get(m.group(1), '')
    return re.sub(r'ref:(\w+)', repl, raw)


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
            d['node_count'] = puzzle.get('node_count', 20)
            d['win_ratio'] = puzzle.get('win_ratio', 0.5)
            d['button_label'] = puzzle.get('button_label', 'Add Thread')
            d['teaching_text'] = puzzle.get('teaching_text', '')
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
        cols = puzzle['columns']
        d['columns'] = []
        for c in cols:
            if isinstance(c, dict):
                d['columns'].append({'text': c['text'], 'tooltip': c.get('tooltip', '')})
            else:
                d['columns'].append({'text': c, 'tooltip': ''})
        d['correct'] = puzzle['correct']
    elif t == 'km':
        d['scenario'] = puzzle['scenario']
        d['options'] = []
        for opt in puzzle['options']:
            d['options'].append({
                'key': opt['key'],
                'text': opt['text'],
                'disaster': opt['disaster']
            })
        d['unlock_threshold'] = puzzle.get('unlock_threshold', 3)
        d['reflection_prompt'] = puzzle.get('reflection_prompt', '')
        d['reflection_keywords'] = puzzle.get('reflection_keywords', [])
        d['reflection_match'] = puzzle.get('reflection_match', '')
        d['reflection_default'] = puzzle.get('reflection_default', '')
        d['resolution_label'] = puzzle.get('resolution_label', '')
        d['resolution'] = puzzle.get('resolution', '')
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

for p in chapter_puzzles:
    p['_bg_html'] = resolve_background(p.get('background', ''))
for bp in bridge_puzzles:
    bp['_bg_html'] = resolve_background(bp.get('background', ''))


def text_to_html(text):
    paras = str(text).strip().split('\n\n')
    parts = []
    for p in paras:
        cleaned = ' '.join(p.strip().split())
        parts.append(f'<p>{esc(cleaned)}</p>')
    return '\n'.join(parts)


def render_km_container(puzzle):
    pid = esc(puzzle['id'])
    title = esc(puzzle.get('title', ''))
    abstract_text = esc(puzzle.get('abstract', '').strip())
    hint_text = esc(puzzle.get('hint', ''))
    egg_url = puzzle.get('egg_url', '').strip()
    egg_link = f'<p class="egg-reward"><a href="{htmlmod.escape(egg_url)}" target="_blank">&#x1f513; Continue exploring &rarr;</a></p>' if egg_url else ''
    bg_html = puzzle.get('_bg_html', '')
    bg_section = ''
    if bg_html:
        bg_section = f'''<details class="background-panel">
  <summary>\U0001f4d6 Background</summary>
  <div class="background-content">{bg_html}</div>
</details>'''
    scenario_html = text_to_html(puzzle.get('scenario', ''))
    options_html = ''
    for opt in puzzle.get('options', []):
        disaster_html = text_to_html(opt.get('disaster', ''))
        options_html += f'''<div class="km-option" data-key="{esc(opt['key'])}">
      <button class="km-option-btn">{esc(opt['text'])}</button>
      <div class="km-disaster" style="display:none">
        {disaster_html}
        <div class="km-disaster-verdict">☠ This path leads to disaster.</div>
      </div>
    </div>\n'''
    reflection_prompt = esc(puzzle.get('reflection_prompt', ''))
    resolution_label = esc(puzzle.get('resolution_label', ''))
    resolution_html = text_to_html(puzzle.get('resolution', ''))
    blurb = puzzle.get('gateway_blurb', '')
    blurb_html = f'<p class="gateway-blurb">\U0001f9e9 {esc(blurb)}</p>' if blurb else ''
    return f'''<div class="puzzle-container km-puzzle" id="{pid}" data-puzzle-id="{pid}" data-puzzle-type="km">
  <h2>{title}</h2>
  {blurb_html}
  <div class="km-scenario">{scenario_html}</div>
  <div class="km-options">
    {options_html}
  </div>
  <div class="km-reflection" style="display:none">
    <p class="km-reflection-prompt">{reflection_prompt}</p>
    <textarea class="km-input" placeholder="Type your answer..."></textarea>
    <button class="km-submit-btn">What happens?</button>
    <div class="km-response" style="display:none"></div>
  </div>
  <div class="km-resolution-wrap" style="display:none">
    <div class="km-option km-option-final">
      <button class="km-option-btn km-option-unlocked">\U0001f513 {resolution_label}</button>
      <div class="km-disaster" style="display:none">
        {resolution_html}
      </div>
    </div>
  </div>
  {bg_section}
  <p class="hint" id="hint-{pid}">{hint_text}</p>
  <div class="result" id="result-{pid}">
    <div class="solved-badge">&#10003; Solved</div>
    <blockquote class="abstract">{abstract_text}</blockquote>
    {egg_link}
  </div>
  <noscript><p class="puzzle-fallback">Enable JavaScript to interact with this puzzle.</p></noscript>
</div>'''


# --- Generate container HTML ---
def render_container(puzzle):
    ptype = puzzle.get('type', puzzle.get('sub_type', ''))
    if ptype == 'km':
        return render_km_container(puzzle)

    pid = esc(puzzle['id'])
    title = esc(puzzle.get('title', ''))
    question = esc(puzzle.get('question', ''))
    abstract_text = esc(puzzle.get('abstract', '').strip())
    hint_text = esc(puzzle.get('hint', ''))
    ptype = puzzle.get('type', puzzle.get('sub_type', ''))
    bg_html = puzzle.get('_bg_html', '')
    bg_section = ''
    if bg_html:
        bg_section = f'''<details class="background-panel">
  <summary>\U0001f4d6 Background</summary>
  <div class="background-content">{bg_html}</div>
</details>'''
    illus_key = puzzle.get('illustration', '')
    illus_html = ILLUSTRATIONS.get(illus_key, '') if illus_key else ''
    blurb = puzzle.get('gateway_blurb', '')
    blurb_html = f'<p class="gateway-blurb">\U0001f9e9 {esc(blurb)}</p>' if blurb else ''
    egg_url = puzzle.get('egg_url', '').strip()
    egg_link = f'<p class="egg-reward"><a href="{htmlmod.escape(egg_url)}" target="_blank">&#x1f513; Continue exploring &rarr;</a></p>' if egg_url else ''
    return f'''<div class="puzzle-container" id="{pid}" data-puzzle-id="{pid}" data-puzzle-type="{ptype}">
  <h2>{title}</h2>
  {blurb_html}
  {illus_html}
  <p class="question">{question}</p>
  <div class="interaction"></div>
  {bg_section}
  <p class="hint" id="hint-{pid}">{hint_text}</p>
  <div class="result" id="result-{pid}">
    <div class="solved-badge">&#10003; Solved</div>
    <blockquote class="abstract">{abstract_text}</blockquote>
    {egg_link}
  </div>
  <noscript><p class="puzzle-fallback">Enable JavaScript to interact with this puzzle.</p></noscript>
</div>'''


km_puzzles = [p for p in chapter_puzzles if p.get('type') == 'km']
nonsci_puzzles = [p for p in chapter_puzzles if p.get('category') == 'nonsci' and p.get('type') != 'km']
science_puzzles = [p for p in chapter_puzzles if p.get('category') == 'science']

nonsci_html = '\n'.join(render_container(p) for p in nonsci_puzzles)
science_html = '\n'.join(render_container(p) for p in science_puzzles)
bridge_puzzle_html = '\n'.join(render_container(bp) for bp in bridge_puzzles)
km_html = '\n'.join(render_container(p) for p in km_puzzles)

km_section = ''
if km_html:
    km_section = f'''<hr>
<h2 class="category-header" id="cat-km">⚖ The Final Question</h2>
{km_html}'''

bridge_abstract = esc(bridge['abstract'].strip())
bridge_section = f'''<hr>
<h2 class="category-header" id="cat-bridge">\U0001f309 The Bridge Builder</h2>
<p class="framing">{esc(bridge['intro'])}</p>
<p class="progress">Bridges: <span id="bridge-count">0</span>/{len(bridge_puzzles)}</p>
<div id="bridge-svg-wrap">
  <svg id="bridge-svg" viewBox="0 0 500 400"></svg>
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
.gateway-blurb { font-size: 0.88em; color: #666; font-style: italic; margin: -0.5em 0 0.8em 0; padding: 0.4em 0.6em; border-left: 3px solid #2a9b9a; background: #f5fafa; border-radius: 0 4px 4px 0; }

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

.background-panel { margin-top: 0.8em; border-left: 3px solid #4a90d9; background: #f0f6fa; border-radius: 0 4px 4px 0; }
.background-panel summary { padding: 0.5em 1em; cursor: pointer; font-weight: bold; color: #1a5276; font-size: 0.95em; }
.background-panel summary:hover { color: #154360; }
.background-content { padding: 0 1em 0.8em; font-size: 0.9em; line-height: 1.6; color: #333; }
.category-header { font-size: 1.5em; color: #1a5276; margin-top: 2em; margin-bottom: 0.5em; padding-bottom: 0.3em; border-bottom: 2px solid #ddd; }

#bridge-svg-wrap { margin: 1em 0; }
#bridge-svg { width: 100%; max-width: 500px; height: auto; border: 1px solid #ddd; border-radius: 4px; background: #fafafa; display: block; margin: 0 auto; }
.bridge-label { font-size: 9px; fill: #333; text-anchor: middle; pointer-events: none; }
.bridge-edge { stroke: #999; stroke-width: 1.5; stroke-opacity: 0.6; }
.bridge-tier-label { font-size: 11px; fill: #1a5276; font-weight: bold; text-anchor: middle; opacity: 0; transition: opacity 0.5s; }
.bridge-tier-label.visible { opacity: 1; }

.reset-wrap { text-align: center; margin: 2em 0 1em; }
.reset-btn { font-family: Georgia, "Times New Roman", serif; font-size: 0.9em; padding: 0.5em 1.2em; border: 1px solid #ccc; border-radius: 4px; background: #fff; color: #888; cursor: pointer; transition: color 0.2s, border-color 0.2s; }
.reset-btn:hover { color: #c0392b; border-color: #c0392b; }
.puzzle-fallback { color: #856404; font-style: italic; }
.no-crypto { background: #fff3cd; border: 1px solid #d4a14b; padding: 1em; border-radius: 4px; margin-bottom: 2em; }

/* --- KM (Kobayashi Maru) puzzle --- */
.puzzle-container.km-puzzle .gateway-blurb { color: #a0b0c0; background: #141a22; border-left-color: #2471a3; }
.puzzle-container.km-puzzle { background: #0d1117; color: #e0e0e0; border-color: #333; }
.puzzle-container.km-puzzle.solved { background: #0d1a2e; border-color: #2471a3; }
.km-puzzle h2 { color: #e94560; }
.km-puzzle .hint { background: #1a2010; color: #d0c060; border-left-color: #9a8430; }
.km-puzzle .abstract { background: #0d1a2e; color: #c0d8f0; border-left-color: #2471a3; }
.km-puzzle .solved-badge { color: #8ecae6; }
.km-puzzle .background-panel { background: #111a2e; border-left-color: #4a90d9; }
.km-puzzle .background-panel summary { color: #8ecae6; }
.km-puzzle .background-content { color: #a0b8d0; }
.km-scenario { background: #1a1a2e; border-left: 4px solid #e94560; padding: 1.2em; margin-bottom: 1.5em; line-height: 1.6; font-style: italic; }
.km-scenario p { margin: 0 0 0.8em; }
.km-scenario p:last-child { margin-bottom: 0; }
.km-option { margin-bottom: 0.5em; }
.km-option-btn { width: 100%; text-align: left; padding: 0.8em 1em; background: #16213e; border: 1px solid #445; color: #e0e0e0; cursor: pointer; font-family: Georgia, "Times New Roman", serif; font-size: 1em; border-radius: 4px; transition: background 0.2s; }
.km-option-btn:hover { background: #1a1a3e; border-color: #667; }
.km-option-btn.km-tried { background: #2a1a1a; border-color: #633; color: #a88; }
.km-disaster { background: #1e1010; border-left: 3px solid #c0392b; padding: 1em; margin: 0.3em 0 0.8em 1em; font-size: 0.95em; line-height: 1.5; }
.km-disaster p { margin: 0 0 0.6em; }
.km-disaster p:last-child { margin-bottom: 0; }
.km-disaster-verdict { margin-top: 0.8em; color: #c0392b; font-weight: bold; }
.km-reflection { margin-top: 2em; padding: 1.2em; background: #1a2a1a; border-left: 4px solid #27ae60; animation: km-reveal 0.6s ease-out; }
.km-reflection-prompt { font-weight: bold; margin-bottom: 0.8em; }
.km-input { width: 100%; min-height: 60px; background: #0d1a0d; border: 1px solid #2d5a2d; color: #e0e0e0; padding: 0.6em; font-family: Georgia, "Times New Roman", serif; font-size: 1em; border-radius: 4px; resize: vertical; }
.km-submit-btn { margin-top: 0.5em; padding: 0.5em 1.5em; background: #27ae60; border: none; color: white; cursor: pointer; border-radius: 4px; font-family: Georgia, "Times New Roman", serif; font-size: 1em; }
.km-response { margin-top: 1em; font-style: italic; color: #a0d0a0; }
.km-option-unlocked { background: #1a2a3e !important; border-color: #2471a3 !important; color: #8ecae6 !important; font-weight: bold; }
.km-resolution-wrap .km-disaster { background: #0d1a2e; border-left-color: #2471a3; color: #c0d8f0; }
.km-resolution-wrap .km-disaster p { margin: 0 0 0.6em; }
.km-resolution-wrap .km-disaster p:last-child { margin-bottom: 0; }
@keyframes km-reveal { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.egg-reward { margin-top: 1em; text-align: center; }
.egg-reward a { display: inline-block; padding: 0.5em 1.2em; background: #2a9b9a; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; transition: background 0.2s; }
.egg-reward a:hover { background: #238a89; }

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
  .background-panel { background: #1a2a3a; border-left-color: #4a90d9; }
  .background-panel summary { color: #6ba3f7; }
  .background-content { color: #ccc; }
  .category-header { color: #6ba3f7; border-bottom-color: #444; }
  .egg-reward a { background: #1a6b6a; }
  .egg-reward a:hover { background: #1f7d7c; }
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
  var N = d.node_count || 20;
  var W = 420, H = 300, FLOOR_Y = 260, BTN_R = 10;
  var winRatio = d.win_ratio || 0.5;
  var winSize = Math.ceil(winRatio * N);
  var btnLabel = d.button_label || "Add Thread";
  var teachingText = d.teaching_text || "Phase Transition!";

  /* Seeded PRNG for reproducible layout */
  var seed = 0;
  for (var si = 0; si < d.id.length; si++) seed = (seed * 31 + d.id.charCodeAt(si)) & 0x7fffffff;
  function prng() { seed = (seed * 16807 + 0) % 2147483647; return seed / 2147483647; }

  /* Place N buttons along floor, jittered horizontally */
  var nodes = [];
  var spacing = (W - 40) / (N - 1);
  for (var i = 0; i < N; i++) {
    var bx = 20 + i * spacing + (prng() - 0.5) * spacing * 0.4;
    if (bx < BTN_R + 2) bx = BTN_R + 2;
    if (bx > W - BTN_R - 2) bx = W - BTN_R - 2;
    nodes.push({ x: bx, y: FLOOR_Y, parent: i, rank: 0, liftY: 0 });
  }

  /* Build and shuffle all possible pairs */
  var allPairs = [];
  for (var a = 0; a < N; a++) for (var b = a + 1; b < N; b++) allPairs.push([a, b]);
  for (var i = allPairs.length - 1; i > 0; i--) {
    var j = Math.floor(prng() * (i + 1));
    var tmp = allPairs[i]; allPairs[i] = allPairs[j]; allPairs[j] = tmp;
  }

  var sim = {
    id: d.id, nodes: nodes, edges: [], q: allPairs, qi: 0, tc: 0,
    solved: false, animating: false, ht: d.hint_threshold || 12,
    winSize: winSize, W: W, H: H, FLOOR_Y: FLOOR_Y, BTN_R: BTN_R,
    highlightPair: null, winEdge: null, teachingText: teachingText
  };
  threadsSims[d.id] = sim;

  var inter = el.querySelector(".interaction");
  inter.innerHTML = '<svg id="svg-' + d.id + '" viewBox="0 0 ' + W + ' ' + H + '" class="sim-svg">' +
    '<defs><filter id="shadow-' + d.id + '"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.25"/></filter></defs></svg>' +
    '<div class="sim-controls"><button class="submit-btn" id="add-' + d.id + '">' + esc(btnLabel) + '</button>' +
    '<span class="sim-status" id="tc-' + d.id + '">Threads: 0</span></div>' +
    '<div class="transition-flash" id="flash-' + d.id + '"></div>';
  document.getElementById("add-" + d.id).addEventListener("click", function() { addThread(d.id); });
  renderTSvg(sim);
}

function renderTSvg(sim) {
  var svg = document.getElementById("svg-" + sim.id);
  if (!svg) return;
  var clusters = getClusters(sim.nodes), nc = {}, ci = 0;
  for (var r in clusters) {
    var col = CLUSTER_COLORS[ci++ % CLUSTER_COLORS.length];
    for (var k = 0; k < clusters[r].length; k++) nc[clusters[r][k]] = col;
  }
  var p = [];

  /* Drop shadow filter (preserve across re-renders) */
  p.push('<defs><filter id="shadow-' + sim.id + '"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.25"/></filter></defs>');

  /* Floor line */
  p.push('<line x1="10" y1="' + sim.FLOOR_Y + '" x2="' + (sim.W - 10) + '" y2="' + sim.FLOOR_Y + '" stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>');

  /* Edges (threads) */
  for (var ei = 0; ei < sim.edges.length; ei++) {
    var e = sim.edges[ei];
    var na = sim.nodes[e[0]], nb = sim.nodes[e[1]];
    var ya = na.y + (na.liftY || 0), yb = nb.y + (nb.liftY || 0);
    var isWin = sim.winEdge && sim.winEdge[0] === e[0] && sim.winEdge[1] === e[1];
    var eStroke = isWin ? "#c0392b" : "#999";
    var eWidth = isWin ? "2.5" : "1.5";
    var eOpacity = isWin ? "0.9" : "0.6";
    p.push('<line x1="' + na.x + '" y1="' + ya + '" x2="' + nb.x + '" y2="' + yb + '" stroke="' + eStroke + '" stroke-width="' + eWidth + '" stroke-opacity="' + eOpacity + '"/>');
  }

  /* Nodes (buttons) */
  for (var ni = 0; ni < sim.nodes.length; ni++) {
    var n = sim.nodes[ni];
    var ny = n.y + (n.liftY || 0);
    var fill = nc[ni] || "#ccc";
    var isHighlight = sim.highlightPair && (sim.highlightPair[0] === ni || sim.highlightPair[1] === ni);
    var strokeCol = isHighlight ? "#f1c40f" : "#fff";
    var strokeW = isHighlight ? "3" : "1.5";
    var gl = sim.solved ? " glow" : "";
    p.push('<circle cx="' + n.x + '" cy="' + ny + '" r="' + sim.BTN_R + '" fill="' + fill + '" stroke="' + strokeCol + '" stroke-width="' + strokeW + '" class="node-circle' + gl + '" filter="url(#shadow-' + sim.id + ')"/>');
  }

  svg.innerHTML = p.join("\n");
}

function computeLiftY(sim, selA, selB) {
  /* Build adjacency list from sim edges */
  var N = sim.nodes.length;
  var adj = [];
  for (var i = 0; i < N; i++) adj.push([]);
  for (var ei = 0; ei < sim.edges.length; ei++) {
    var e = sim.edges[ei];
    adj[e[0]].push(e[1]);
    adj[e[1]].push(e[0]);
  }

  /* BFS from selA and selB within their component */
  var distA = [], distB = [];
  for (var i = 0; i < N; i++) { distA.push(-1); distB.push(-1); }

  function bfs(start, dist) {
    var queue = [start];
    dist[start] = 0;
    var head = 0;
    while (head < queue.length) {
      var cur = queue[head++];
      for (var j = 0; j < adj[cur].length; j++) {
        var nb = adj[cur][j];
        if (dist[nb] === -1) { dist[nb] = dist[cur] + 1; queue.push(nb); }
      }
    }
  }
  bfs(selA, distA);
  bfs(selB, distB);

  /* Find components of both selected nodes */
  var rootA = ufFind(sim.nodes, selA);
  var rootB = ufFind(sim.nodes, selB);

  /* Set liftY: selected = -60, 1-hop = -40, 2-hop = -25, 3+ = -20, not in either component = 0 */
  for (var i = 0; i < N; i++) {
    var ri = ufFind(sim.nodes, i);
    if (ri !== rootA && ri !== rootB) { sim.nodes[i].liftY = 0; continue; }
    var minDist = -1;
    if (distA[i] >= 0 && distB[i] >= 0) minDist = Math.min(distA[i], distB[i]);
    else if (distA[i] >= 0) minDist = distA[i];
    else if (distB[i] >= 0) minDist = distB[i];

    if (i === selA || i === selB) sim.nodes[i].liftY = -60;
    else if (minDist === 1) sim.nodes[i].liftY = -40;
    else if (minDist === 2) sim.nodes[i].liftY = -25;
    else if (minDist >= 0) sim.nodes[i].liftY = -20;
    else sim.nodes[i].liftY = 0;
  }
}

function resetLiftY(sim) {
  for (var i = 0; i < sim.nodes.length; i++) sim.nodes[i].liftY = 0;
}

function addThread(id) {
  var sim = threadsSims[id];
  if (!sim || sim.solved || sim.animating || sim.qi >= sim.q.length) return;
  sim.animating = true;

  var btn = document.getElementById("add-" + id);
  if (btn) btn.disabled = true;

  var pair = sim.q[sim.qi];
  var selA = pair[0], selB = pair[1];

  /* Check win condition BEFORE adding the edge:
     both already in same component AND that component >= winSize */
  var rootA = ufFind(sim.nodes, selA);
  var rootB = ufFind(sim.nodes, selB);
  var isWin = false;
  if (rootA === rootB) {
    /* Count component size */
    var compSize = 0;
    for (var ci = 0; ci < sim.nodes.length; ci++) {
      if (ufFind(sim.nodes, ci) === rootA) compSize++;
    }
    if (compSize >= sim.winSize) isWin = true;
  }

  /* Step 1: Highlight the two selected buttons (~100ms) */
  sim.highlightPair = [selA, selB];
  renderTSvg(sim);

  setTimeout(function() {
    /* Step 2: Lift selected + cluster members */
    computeLiftY(sim, selA, selB);
    renderTSvg(sim);

    setTimeout(function() {
      /* Step 3: Add thread (edge) and union */
      sim.qi++;
      sim.edges.push(pair);
      if (isWin) {
        sim.winEdge = pair;
      }
      ufUnion(sim.nodes, selA, selB);
      sim.tc++;
      document.getElementById("tc-" + id).textContent = "Threads: " + sim.tc;
      renderTSvg(sim);

      if (isWin) {
        /* WIN: teaching moment */
        sim.solved = true;
        renderTSvg(sim);
        var fl = document.getElementById("flash-" + id);
        if (fl) { fl.textContent = sim.teachingText; fl.classList.add("visible"); }
        if (btn) btn.disabled = true;

        /* Keep lifted for 5 seconds, then settle */
        setTimeout(function() {
          resetLiftY(sim);
          sim.highlightPair = null;
          renderTSvg(sim);
          if (fl) fl.classList.remove("visible");
          sim.animating = false;
          revealPuzzle(id);
        }, 5000);
      } else {
        /* Not a win — check if giant component now >= winSize, and if so,
           scan forward for an intra-component pair and swap to next position */
        var lc = largestCluster(sim.nodes);
        if (lc >= sim.winSize && sim.qi < sim.q.length) {
          /* Find the root of the giant component */
          var giantRoot = -1;
          var clusters = getClusters(sim.nodes);
          for (var r in clusters) {
            if (clusters[r].length >= sim.winSize) { giantRoot = parseInt(r); break; }
          }
          if (giantRoot >= 0) {
            /* Scan forward for a pair where both are in the giant component */
            for (var fi = sim.qi; fi < sim.q.length; fi++) {
              var fp = sim.q[fi];
              if (ufFind(sim.nodes, fp[0]) === giantRoot && ufFind(sim.nodes, fp[1]) === giantRoot) {
                /* Swap to next position */
                if (fi !== sim.qi) {
                  var swp = sim.q[sim.qi];
                  sim.q[sim.qi] = sim.q[fi];
                  sim.q[fi] = swp;
                }
                break;
              }
            }
          }
        }

        /* Step 4: Settle back (~300ms) */
        setTimeout(function() {
          resetLiftY(sim);
          sim.highlightPair = null;
          renderTSvg(sim);
          sim.animating = false;
          if (btn) btn.disabled = false;

          /* Show hint if enough threads but not yet at transition */
          if (sim.tc >= sim.ht && !sim.solved) showHint(id);
        }, 300);
      }
    }, 400);
  }, 100);
}

/* --- SIM: Resilience --- */
function initResilience(el, d) {
  var N = d.node_count || 30, COLS = 6, ROWS = 5, W = 420, H = 320;
  if (N <= 20) { COLS = 5; ROWS = 4; }
  var nodes = [], edges = [], alive = [], edgeSet = {};
  for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
    nodes.push({ x: 35 + c*(W-70)/(COLS-1), y: 35 + r*(H-70)/(ROWS-1) }); alive.push(true);
  }
  N = nodes.length;
  function addEdge(a, b) {
    if (a === b) return;
    var key = Math.min(a,b) + "-" + Math.max(a,b);
    if (!edgeSet[key]) { edgeSet[key] = true; edges.push([a, b]); }
  }
  for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
    var i = r*COLS + c;
    if (c < COLS-1) addEdge(i, i+1);
    if (r < ROWS-1) addEdge(i, i+COLS);
    if (c < COLS-1 && r < ROWS-1) addEdge(i, i+COLS+1);
    if (c > 0 && r < ROWS-1) addEdge(i, i+COLS-1);
  }
  var bcCount = d.classical_backchannels || 15;
  var rng = (function(s) { return function() { s = (s * 16807 + 0) % 2147483647; return s / 2147483647; }; })(d.id.length * 7 + 42);
  for (var bc = 0; bc < bcCount; bc++) {
    var a = Math.floor(rng() * N), b = Math.floor(rng() * N);
    if (a !== b) addEdge(a, b);
  }
  var destroyed = 0, solved = false, hintAt = d.hint_after || 10;
  var inter = el.querySelector(".interaction");
  inter.innerHTML = '<svg id="svg-' + d.id + '" viewBox="0 0 ' + W + ' ' + H + '" class="sim-svg"></svg>' +
    '<div class="sim-controls"><span class="sim-status" id="st-' + d.id + '">Destroyed: 0/' + N + ' — Network: OPERATIONAL</span></div>' +
    '<div class="transition-flash" id="flash-' + d.id + '" style="color:#c0392b">Network: FAILED</div>';

  function render() {
    var svg = document.getElementById("svg-" + d.id); if (!svg) return;
    var p = [];
    var localEdges = [], longEdges = [];
    edges.forEach(function(e) {
      if (!alive[e[0]] || !alive[e[1]]) return;
      var dx = Math.abs(nodes[e[0]].x - nodes[e[1]].x), dy = Math.abs(nodes[e[0]].y - nodes[e[1]].y);
      if (dx > (W-70)/(COLS-1)*1.5 || dy > (H-70)/(ROWS-1)*1.5)
        longEdges.push(e);
      else
        localEdges.push(e);
    });
    localEdges.forEach(function(e) {
      p.push('<line x1="'+nodes[e[0]].x+'" y1="'+nodes[e[0]].y+'" x2="'+nodes[e[1]].x+'" y2="'+nodes[e[1]].y+'" stroke="#2a9b9a" stroke-width="1.5" stroke-opacity="0.35"/>');
    });
    longEdges.forEach(function(e) {
      p.push('<line x1="'+nodes[e[0]].x+'" y1="'+nodes[e[0]].y+'" x2="'+nodes[e[1]].x+'" y2="'+nodes[e[1]].y+'" stroke="#e67e22" stroke-width="1" stroke-opacity="0.3" stroke-dasharray="4,3"/>');
    });
    nodes.forEach(function(n, i) {
      if (alive[i]) p.push('<circle cx="'+n.x+'" cy="'+n.y+'" r="11" fill="#2a9b9a" stroke="#fff" stroke-width="1.5" class="node-circle" data-n="'+i+'" style="cursor:pointer"/>');
      else p.push('<circle cx="'+n.x+'" cy="'+n.y+'" r="11" fill="#555" stroke="#888" stroke-width="1" opacity="0.25"/>');
    });
    svg.innerHTML = p.join("\n");
    var circles = svg.querySelectorAll("circle[data-n]");
    for (var j = 0; j < circles.length; j++) {
      (function(c) { c.addEventListener("click", function() {
        if (solved) return;
        alive[parseInt(c.dataset.n)] = false; destroyed++;
        render();
        var aliveCount = 0; for (var k = 0; k < N; k++) if (alive[k]) aliveCount++;
        if (destroyed >= hintAt && aliveCount > 0) showHint(d.id);
        if (aliveCount === 0) {
          solved = true;
          document.getElementById("st-" + d.id).textContent = "Destroyed: " + destroyed + "/" + N + " — Network: FAILED (every node destroyed)";
          var fl = document.getElementById("flash-" + d.id); if (fl) fl.classList.add("visible");
          setTimeout(function() { if (fl) fl.classList.remove("visible"); revealPuzzle(d.id); }, 1800);
        } else {
          document.getElementById("st-" + d.id).textContent = "Destroyed: " + destroyed + "/" + N + " — Network: OPERATIONAL (" + aliveCount + " nodes remaining)";
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
    d.columns.forEach(function(col) {
      var text = typeof col === "object" ? col.text : col;
      var tip = typeof col === "object" && col.tooltip ? col.tooltip : "";
      html += tip ? '<th title="' + esc(tip) + '" style="cursor:help;text-decoration:underline dotted">' + esc(text) + "</th>" : "<th>" + esc(text) + "</th>";
    });
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

/* --- KM (Kobayashi Maru) --- */
function initKM(el, d) {
  var pid = d.id;
  var threshold = d.unlock_threshold || 3;
  var keywords = d.reflection_keywords || [];
  var matchResp = d.reflection_match || '';
  var defaultResp = d.reflection_default || '';
  var container = document.getElementById(pid);
  if (!container) return;

  var seen = [];
  try { seen = JSON.parse(localStorage.getItem(pid + '-seen') || '[]'); } catch(e) { seen = []; }
  var reflected = localStorage.getItem(pid + '-reflected') === 'true';
  var kmSolved = localStorage.getItem(pid + '-solved') === 'true';

  function revealDisaster(key) {
    var card = container.querySelector('.km-option[data-key="' + key + '"]');
    if (!card) return;
    card.querySelector('.km-disaster').style.display = 'block';
    card.querySelector('.km-option-btn').classList.add('km-tried');
    if (seen.indexOf(key) === -1) {
      seen.push(key);
      try { localStorage.setItem(pid + '-seen', JSON.stringify(seen)); } catch(e) {}
    }
    if (seen.length >= threshold) showReflection();
  }

  function showReflection() {
    container.querySelector('.km-reflection').style.display = 'block';
  }

  function showResolution() {
    var wrap = container.querySelector('.km-resolution-wrap');
    wrap.style.display = 'block';
    wrap.style.animation = 'km-reveal 0.8s ease-out';
  }

  function markSolved() {
    kmSolved = true;
    try { localStorage.setItem(pid + '-solved', 'true'); } catch(e) {}
    showSolvedState();
    setSolved(pid);
    updateCounts();
  }

  function showSolvedState() {
    container.querySelector('.result').style.display = 'block';
  }

  // Restore state on load
  for (var i = 0; i < seen.length; i++) revealDisaster(seen[i]);
  if (seen.length >= threshold) showReflection();
  if (reflected) showResolution();
  if (kmSolved) showSolvedState();

  // Option click handlers
  var btns = container.querySelectorAll('.km-option-btn');
  for (var j = 0; j < btns.length; j++) {
    (function(btn) {
      btn.addEventListener('click', function() {
        var card = btn.closest('.km-option');
        if (!card) return;
        var key = card.dataset.key;
        if (card.classList.contains('km-option-final')) {
          card.querySelector('.km-disaster').style.display = 'block';
          markSolved();
          return;
        }
        revealDisaster(key);
      });
    })(btns[j]);
  }

  // Reflection submit
  var submitBtn = container.querySelector('.km-submit-btn');
  if (submitBtn) {
    submitBtn.addEventListener('click', function() {
      var input = container.querySelector('.km-input').value.toLowerCase().trim();
      var hasMatch = false;
      for (var k = 0; k < keywords.length; k++) {
        if (input.indexOf(keywords[k]) !== -1) { hasMatch = true; break; }
      }
      var resp = container.querySelector('.km-response');
      resp.textContent = hasMatch ? matchResp : defaultResp;
      resp.style.display = 'block';
      reflected = true;
      try { localStorage.setItem(pid + '-reflected', 'true'); } catch(e) {}
      showResolution();
    });
  }
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

  var crossEdges = [], tierLabels = [], finalTrans = false;
  BD.puzzles.forEach(function(bp) {
    if (solvedSet[bp.id]) {
      if (bp.edges) crossEdges = crossEdges.concat(bp.edges);
      if (bp.tier_label) tierLabels.push(bp.tier_label);
      if (bp.final_transition) finalTrans = true;
    }
  });

  var nIdx = {}; BD.nodes.forEach(function(n, i) { nIdx[n.id] = i; });

  var clusterMap = {};
  BD.nodes.forEach(function(n) {
    if (!clusterMap[n.cluster]) clusterMap[n.cluster] = [];
    clusterMap[n.cluster].push(n);
  });

  var matConnected = false;
  crossEdges.forEach(function(e) {
    if (e[0] === "mat" || e[1] === "mat") matConnected = true;
  });

  var FLOOR = 370;
  function nodeY(n) {
    if (clusterMap[n.cluster].length === 1 && !matConnected) return 340;
    return n.y;
  }

  var parts = [];

  parts.push('<line x1="20" y1="'+FLOOR+'" x2="480" y2="'+FLOOR+'" stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>');

  for (var c in clusterMap) {
    var cn = clusterMap[c], maxY = 0, maxX = 0;
    for (var i = 0; i < cn.length; i++) {
      var ny = nodeY(cn[i]);
      if (ny > maxY) { maxY = ny; maxX = cn[i].x; }
    }
    if (maxY < FLOOR - 5) {
      parts.push('<line x1="'+maxX+'" y1="'+maxY+'" x2="'+maxX+'" y2="'+FLOOR+'" stroke="#ccc" stroke-width="0.5" stroke-dasharray="2,3" opacity="0.5"/>');
    }
  }

  for (var c in clusterMap) {
    var cn = clusterMap[c], col = BD.cluster_colors[c] || "#999";
    for (var a = 0; a < cn.length; a++) {
      for (var b = a + 1; b < cn.length; b++) {
        parts.push('<line x1="'+cn[a].x+'" y1="'+nodeY(cn[a])+'" x2="'+cn[b].x+'" y2="'+nodeY(cn[b])+'" stroke="'+col+'" stroke-width="1.5" stroke-opacity="0.65"/>');
      }
    }
  }

  BD.puzzles.forEach(function(bp) {
    if (solvedSet[bp.id] || !bp.edges) return;
    bp.edges.forEach(function(e) {
      var ai = nIdx[e[0]], bi = nIdx[e[1]];
      if (ai === undefined || bi === undefined) return;
      var na = BD.nodes[ai], nb = BD.nodes[bi];
      parts.push('<line x1="'+na.x+'" y1="'+nodeY(na)+'" x2="'+nb.x+'" y2="'+nodeY(nb)+'" stroke="#ccc" stroke-width="1" stroke-dasharray="4,3" opacity="0.4"/>');
    });
  });

  crossEdges.forEach(function(e) {
    var ai = nIdx[e[0]], bi = nIdx[e[1]];
    if (ai === undefined || bi === undefined) return;
    var na = BD.nodes[ai], nb = BD.nodes[bi];
    parts.push('<line x1="'+na.x+'" y1="'+nodeY(na)+'" x2="'+nb.x+'" y2="'+nodeY(nb)+'" stroke="#27ae60" stroke-width="2"/>');
  });

  BD.nodes.forEach(function(n) {
    var y = nodeY(n), col = BD.cluster_colors[n.cluster] || "#999";
    var glow = finalTrans ? " glow" : "";
    parts.push('<g><title>'+esc(n.full || n.label)+'</title>');
    parts.push('<circle cx="'+n.x+'" cy="'+y+'" r="16" fill="'+col+'" stroke="#fff" stroke-width="1.5" class="node-circle'+glow+'"/>');
    parts.push('<text x="'+n.x+'" y="'+(y+3)+'" text-anchor="middle" fill="#fff" font-size="7" font-weight="bold" font-family="Helvetica,Arial,sans-serif" pointer-events="none">'+esc(n.label)+'</text>');
    parts.push('</g>');
  });

  tierLabels.forEach(function(label, i) {
    parts.push('<text x="250" y="'+(20 + i*16)+'" class="bridge-tier-label visible">'+esc(label)+'</text>');
  });

  var legendY = FLOOR + 18, seen = {}, order = [];
  BD.nodes.forEach(function(n) { if (!seen[n.cluster]) { seen[n.cluster] = true; order.push(n.cluster); } });
  var lx = 25;
  order.forEach(function(c) {
    var col = BD.cluster_colors[c] || "#999";
    parts.push('<circle cx="'+lx+'" cy="'+legendY+'" r="5" fill="'+col+'"/>');
    parts.push('<text x="'+(lx+8)+'" y="'+(legendY+3)+'" font-size="8" fill="#666">'+c+'</text>');
    lx += c.length * 5.5 + 22;
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
      else if (type === "km") initKM(el, d);
    } catch(e) { console.error("Puzzle init error:", id, e); var fb = el.querySelector(".interaction"); if (fb) fb.innerHTML = '<p class="puzzle-fallback">Puzzle failed to load.</p>'; }
  }
  if (!hasCrypto) {
    var nc = document.getElementById("no-crypto"); if (nc) nc.style.display = "block";
    for (var id in PD) { if (PD[id].type !== "km") revealPuzzle(id); }
    return;
  }
  var solved = getSolved();
  for (var id in solved) if (solved[id] && (!PD[id] || PD[id].type !== "km")) revealPuzzle(id);
  try { initBridge(); } catch(e) { console.error("Bridge init error:", e); }
  updateCounts();
  if (location.hash) { var t = document.querySelector(location.hash); if (t) setTimeout(function() { t.scrollIntoView({behavior:"smooth"}); }, 100); }
}

function resetPuzzles() {
  try {
    localStorage.removeItem(STORAGE_KEY); localStorage.removeItem(BRIDGE_KEY);
    for (var id in PD) {
      if (PD[id].type === "km") {
        localStorage.removeItem(id + '-seen');
        localStorage.removeItem(id + '-reflected');
        localStorage.removeItem(id + '-solved');
      }
    }
  } catch(e) {}
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

<h1>Relinquishment &mdash; Puzzle Preview</h1> <a style="font-size:0.55em;color:#1a5276;font-family:Georgia,serif;" href="tools.html">&larr; Back to Author Tools</a>
<p class="framing">Each chapter ends with a puzzle. Solve it to reveal
the chapter&rsquo;s Spiral Abstract &mdash; the meta-view that connects the chapter
to the book&rsquo;s larger argument. The Final Question awaits at the end.</p>
<p class="progress">Chapter puzzles: <span id="chapter-count">0</span>/{chapter_count}</p>

<div id="no-crypto" class="no-crypto" style="display:none;">
  <strong>Note:</strong> Your browser does not support the SubtleCrypto API.
  All puzzles are shown unlocked.
</div>

<h2 class="category-header" id="cat-nonsci">\U0001f4da Ethics, Story &amp; Framework</h2>
{nonsci_html}

<h2 class="category-header" id="cat-science">\U0001f52c Science &amp; Physics</h2>
{science_html}

{bridge_section}

{km_section}

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
