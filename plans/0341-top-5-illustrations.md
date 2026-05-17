# Plan 0341: Top 5 Illustrations — GA Visual Anchors

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** Plans 0339 + 0340 committed
**Files:** `build/preprocess.py` (new inject functions + calls)

---

## Objective

Fill the remaining visual deserts in the GA reader's collapsed path. Five targeted illustrations that maximize impact-per-effort: two always-visible chapter intros, one always-visible in-section figure, and two rich tooltip panels for collapsed sections.

---

## Priority Ranking (why these 5)

| # | Location | Visibility | Why |
|---|----------|-----------|-----|
| 1 | Factoring Game intro | ALWAYS | First text desert after rich Braid/Flat chapters. GA sees only epigraph + 2 collapsed bars. |
| 2 | Capabilities "Can It Be Killed?" | ALWAYS | Not collapsed. Pure text currently. Most dramatic Q&A answer. |
| 3 | Heliospheric current sheet | TOOLTIP | "The Neighborhood" collapsed bar. Iconic space physics visual. |
| 4 | Why Relinquish intro | ALWAYS | Chapter intro visible. Ethical climax of spine. No visual anchor. |
| 5 | Aurora borealis | TOOLTIP | "Why Call It Two-Dimensional?" collapsed bar. Emotional bridge. |

---

## Illustration 1: The Factoring Game — "Easy to Multiply, Hard to Factor"

**Type:** Always-visible inline SVG
**Placement:** After the Eric Hughes epigraph, before the first `\section*` (which is collapsed). New inject function.
**Target text:** Find the paragraph containing "A Cypherpunk's Manifesto" in HTML, inject after the blockquote's closing tag.

**Concept:** Side-by-side: LEFT shows 13 × 7 = 91 with a green checkmark (instant), RIGHT shows 91 = ? × ? with red question marks (hard). A single visual that communicates the entire foundation of public-key cryptography.

```python
def inject_factoring_illustration(html_path):
    """Inject multiply-vs-factor diagram into The Factoring Game intro (Plan 0341)."""
    html_path = Path(html_path)
    text = html_path.read_text()
    # Find the chapter by its label
    target = 'id="spine:factoring-game"'
    pos = text.find(target)
    if pos == -1:
        return
    # Find the blockquote close after the epigraph
    bq_close = text.find('</blockquote>', pos)
    if bq_close == -1:
        return
    insert_point = text.find('>', bq_close) + 1
    # Skip past any whitespace/newlines to next element
    while insert_point < len(text) and text[insert_point] in ' \n\r\t':
        insert_point += 1

    FACTOR_SVG = '''<figure id="fig-factor-vs-multiply" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="380" height="120" viewBox="0 0 380 120" style="display:block;margin:0 auto;">
  <title>The asymmetry of multiplication vs factoring: 13 times 7 equals 91 is easy; 91 equals what times what is hard.</title>
  <!-- LEFT: Easy multiplication -->
  <rect x="10" y="15" width="160" height="90" rx="8" fill="#f0f8f0" stroke="#2e7d32" stroke-width="1" opacity="0.6"/>
  <text x="90" y="50" text-anchor="middle" font-family="Georgia, serif" font-size="22" fill="#333">13 × 7 = 91</text>
  <text x="90" y="75" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#2e7d32">instant</text>
  <text x="90" y="95" text-anchor="middle" font-family="Georgia, serif" font-size="18" fill="#2e7d32">✓</text>

  <!-- Arrow -->
  <text x="190" y="62" text-anchor="middle" font-family="Georgia, serif" font-size="16" fill="#888">vs</text>

  <!-- RIGHT: Hard factoring -->
  <rect x="210" y="15" width="160" height="90" rx="8" fill="#fdf0f0" stroke="#c62828" stroke-width="1" opacity="0.6"/>
  <text x="290" y="50" text-anchor="middle" font-family="Georgia, serif" font-size="22" fill="#333">91 = ? × ?</text>
  <text x="290" y="75" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#c62828">try every option</text>
  <text x="290" y="95" text-anchor="middle" font-family="Georgia, serif" font-size="14" fill="#c62828">⏱ exponential</text>
</svg>
<figcaption style="font-size:0.78em;color:#888;margin-top:0.3em;font-style:italic;">All internet encryption relies on this asymmetry.</figcaption>
</figure>
'''
    text = text[:insert_point] + '\n' + FACTOR_SVG + '\n' + text[insert_point:]
    html_path.write_text(text)
    print("  Factoring Game: multiply-vs-factor diagram injected")
```

---

## Illustration 2: Capabilities — "Can It Be Killed?" Network Diagram

**Type:** Always-visible inline SVG
**Placement:** Inside the "Can It Be Killed?" section, after the first paragraph (before "If a self-organizing system were distributed...").
**Target text:** Find `id="spine:cap-killed"`, then find "Topological protection means", inject after that paragraph.

**Concept:** A network of ~12 nodes connected by lines. One node is red/destroyed (X through it), but all other nodes remain connected. Caption: "No single point of failure."

```python
def inject_network_resilience(html_path):
    """Inject distributed network diagram into Capabilities 'Can It Be Killed?' (Plan 0341)."""
    html_path = Path(html_path)
    text = html_path.read_text()
    target = 'id="spine:cap-killed"'
    pos = text.find(target)
    if pos == -1:
        return
    # Find end of first paragraph in this section
    first_p_end = text.find('</p>', pos + 100)
    if first_p_end == -1:
        return
    insert_point = first_p_end + 4

    NETWORK_SVG = '''<figure id="fig-network-resilience" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180" style="display:block;margin:0 auto;">
  <title>A distributed network: one node destroyed (red X) but all others remain connected. No single point of failure.</title>
  <!-- Connections (drawn first, behind nodes) -->
  <line x1="80" y1="50" x2="160" y2="30" stroke="#ccc" stroke-width="1.2"/>
  <line x1="80" y1="50" x2="60" y2="110" stroke="#ccc" stroke-width="1.2"/>
  <line x1="80" y1="50" x2="160" y2="90" stroke="#ccc" stroke-width="1.2"/>
  <line x1="160" y1="30" x2="240" y2="50" stroke="#ccc" stroke-width="1.2"/>
  <line x1="160" y1="30" x2="160" y2="90" stroke="#ccc" stroke-width="1.2"/>
  <line x1="240" y1="50" x2="260" y2="110" stroke="#ccc" stroke-width="1.2"/>
  <line x1="240" y1="50" x2="160" y2="90" stroke="#ccc" stroke-width="1.2"/>
  <line x1="60" y1="110" x2="120" y2="150" stroke="#ccc" stroke-width="1.2"/>
  <line x1="60" y1="110" x2="160" y2="90" stroke="#ccc" stroke-width="1.2"/>
  <line x1="160" y1="90" x2="120" y2="150" stroke="#ccc" stroke-width="1.2"/>
  <line x1="160" y1="90" x2="200" y2="150" stroke="#ccc" stroke-width="1.2"/>
  <line x1="160" y1="90" x2="260" y2="110" stroke="#ccc" stroke-width="1.2"/>
  <line x1="260" y1="110" x2="200" y2="150" stroke="#ccc" stroke-width="1.2"/>
  <line x1="120" y1="150" x2="200" y2="150" stroke="#ccc" stroke-width="1.2"/>
  <!-- Destroyed connections (dashed, faded) -->
  <line x1="160" y1="90" x2="160" y2="30" stroke="#c62828" stroke-width="1" stroke-dasharray="3,3" opacity="0.4"/>
  <line x1="80" y1="50" x2="160" y2="30" stroke="#c62828" stroke-width="1" stroke-dasharray="3,3" opacity="0.4"/>
  <line x1="240" y1="50" x2="160" y2="30" stroke="#c62828" stroke-width="1" stroke-dasharray="3,3" opacity="0.4"/>
  <!-- Healthy nodes -->
  <circle cx="80" cy="50" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <circle cx="60" cy="110" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <circle cx="160" cy="90" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <circle cx="240" cy="50" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <circle cx="260" cy="110" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <circle cx="120" cy="150" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <circle cx="200" cy="150" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <!-- Destroyed node -->
  <circle cx="160" cy="30" r="8" fill="#ffebee" stroke="#c62828" stroke-width="1.5"/>
  <line x1="154" y1="24" x2="166" y2="36" stroke="#c62828" stroke-width="2.5"/>
  <line x1="166" y1="24" x2="154" y2="36" stroke="#c62828" stroke-width="2.5"/>
  <!-- Label -->
  <text x="160" y="175" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#888" font-style="italic">network persists</text>
</svg>
<figcaption style="font-size:0.78em;color:#888;margin-top:0.3em;font-style:italic;">Destroy one node. The rest remain connected.</figcaption>
</figure>
'''
    text = text[:insert_point] + '\n' + NETWORK_SVG + '\n' + text[insert_point:]
    html_path.write_text(text)
    print("  Capabilities: network resilience diagram injected")
```

---

## Illustration 3: Heliospheric Current Sheet — Rich Tooltip Panel

**Type:** Rich tooltip panel (html: field on existing "The Neighborhood" collapse entry)
**Placement:** Add `hover_id:` and `html:` to the existing "The Neighborhood" entry in `build/tech-collapse.yaml`.

```yaml
    hover_id: "collapse-ws-neighborhood"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⬡ The Neighborhood</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Earth is not alone. Jupiter, Saturn, Ganymede, and the heliospheric current sheet all contain the same ingredients: confined charged particles, continuous energy, billions of years.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="280" height="80" viewBox="0 0 280 80" style="display:block;margin:0.4em auto 0.2em;">
        <title>Heliospheric current sheet: a wavy surface extending from the Sun through the solar system — the ballerina skirt</title>
        <circle cx="20" cy="40" r="10" fill="#ffdd66" stroke="#cc9900" stroke-width="1"/>
        <path d="M 35,40 C 60,20 80,60 105,40 C 130,20 150,60 175,40 C 200,20 220,60 245,40 C 255,30 265,50 275,40" fill="none" stroke="#6a9fba" stroke-width="2" opacity="0.7"/>
        <path d="M 35,40 C 60,55 80,25 105,40 C 130,55 150,25 175,40 C 200,55 220,25 245,40 C 255,48 265,32 275,40" fill="none" stroke="#6a9fba" stroke-width="1.2" opacity="0.4" stroke-dasharray="4,3"/>
        <circle cx="105" cy="40" r="3" fill="#5588dd" stroke="#3366aa" stroke-width="0.8"/>
        <circle cx="175" cy="40" r="5" fill="#d4a06a" stroke="#a0784a" stroke-width="0.8"/>
        <circle cx="220" cy="40" r="4" fill="#c4a97d" stroke="#8b7355" stroke-width="0.8"/>
        <text x="105" y="60" text-anchor="middle" font-family="Georgia, serif" font-size="6" fill="#555">Earth</text>
        <text x="175" y="60" text-anchor="middle" font-family="Georgia, serif" font-size="6" fill="#555">Jupiter</text>
        <text x="220" y="60" text-anchor="middle" font-family="Georgia, serif" font-size="6" fill="#555">Saturn</text>
        <text x="155" y="14" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#6a9fba" font-style="italic">heliospheric current sheet</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full planetary survey.</p>
```

---

## Illustration 4: Why Relinquish — "The Pattern" intro illustration

**Type:** Always-visible inline SVG
**Placement:** After the chapter epigraph in Why Relinquish, before the first section. Find `id="spine:why-relinquish"`, inject after the blockquote.
**Concept:** A repeating pattern across history: three instances of "power concentrated → power abused" shown as identical cycles. Visual rhyme communicating "this always happens."

```python
def inject_power_pattern(html_path):
    """Inject historical power-abuse pattern into Why Relinquish intro (Plan 0341)."""
    html_path = Path(html_path)
    text = html_path.read_text()
    target = 'id="spine:why-relinquish"'
    pos = text.find(target)
    if pos == -1:
        return
    # Why Relinquish has an epigraph blockquote, then \section*{The Habitat}
    # Find the chapter heading end, then the first <h (section heading) — inserts after epigraph
    heading_end = text.find('</h', pos)
    heading_end = text.find('>', heading_end) + 1
    # Find start of first section heading
    next_h = text.find('<h', heading_end + 1)
    if next_h == -1:
        return
    insert_point = next_h

    PATTERN_SVG = '''<figure id="fig-power-pattern" class="inline-svg" style="text-align:center;margin:1.5em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="360" height="100" viewBox="0 0 360 100" style="display:block;margin:0 auto;">
  <title>The pattern repeats: concentrated power leads to abuse, across three historical periods shown as identical cycles.</title>
  <!-- Cycle 1 -->
  <circle cx="50" cy="40" r="20" fill="#fdf0f0" stroke="#c62828" stroke-width="1" opacity="0.6"/>
  <text x="50" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#c62828">power</text>
  <path d="M 70,40 Q 85,25 95,40" fill="none" stroke="#888" stroke-width="1" marker-end="url(#patt-arrow)"/>
  <text x="95" y="55" text-anchor="start" font-family="Georgia, serif" font-size="7" fill="#888">abuse</text>

  <!-- Cycle 2 -->
  <circle cx="170" cy="40" r="20" fill="#fdf0f0" stroke="#c62828" stroke-width="1" opacity="0.6"/>
  <text x="170" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#c62828">power</text>
  <path d="M 190,40 Q 205,25 215,40" fill="none" stroke="#888" stroke-width="1" marker-end="url(#patt-arrow)"/>
  <text x="215" y="55" text-anchor="start" font-family="Georgia, serif" font-size="7" fill="#888">abuse</text>

  <!-- Cycle 3 -->
  <circle cx="290" cy="40" r="20" fill="#fdf0f0" stroke="#c62828" stroke-width="1" opacity="0.6"/>
  <text x="290" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#c62828">power</text>
  <path d="M 310,40 Q 325,25 335,40" fill="none" stroke="#888" stroke-width="1" marker-end="url(#patt-arrow)"/>
  <text x="335" y="55" text-anchor="start" font-family="Georgia, serif" font-size="7" fill="#888">abuse</text>

  <!-- Connecting "repeats" arrows -->
  <path d="M 115,40 L 145,40" fill="none" stroke="#aaa" stroke-width="0.8" stroke-dasharray="3,2"/>
  <path d="M 235,40 L 265,40" fill="none" stroke="#aaa" stroke-width="0.8" stroke-dasharray="3,2"/>

  <!-- Marker def -->
  <defs>
    <marker id="patt-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#888"/>
    </marker>
  </defs>

  <!-- Timeline labels -->
  <text x="50" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#aaa">Rome</text>
  <text x="170" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#aaa">Empire</text>
  <text x="290" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#aaa">Nuclear</text>
  <text x="170" y="95" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#888" font-style="italic">the pattern repeats</text>
</svg>
</figure>
'''
    text = text[:insert_point] + '\n' + PATTERN_SVG + '\n' + text[insert_point:]
    html_path.write_text(text)
    print("  Why Relinquish: power-pattern diagram injected")
```

---

## Illustration 5: Aurora Borealis — Rich Tooltip Panel

**Type:** Rich tooltip panel (html: field on existing "Why Call It Two-Dimensional?" collapse entry)
**Placement:** Add `hover_id:` and `html:` to the existing "Why Call It Two-Dimensional?" entry in `build/tech-collapse.yaml`.

```yaml
    hover_id: "collapse-ws-quasi-2d"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⬡ Why Call It Two-Dimensional?</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">When the current sheet thins, ions can't complete full orbits. Their dynamics become quasi-two-dimensional — the same reduction that makes the Flat possible.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="260" height="80" viewBox="0 0 260 80" style="display:block;margin:0.4em auto 0.2em;">
        <title>Aurora borealis: colored arcs of light descending from the magnetosphere to Earth's poles — plasma dynamics made visible</title>
        <!-- Dark sky background -->
        <rect x="0" y="0" width="260" height="80" rx="4" fill="#0a1628"/>
        <!-- Ground/horizon -->
        <rect x="0" y="65" width="260" height="15" rx="0" fill="#1a2a1a"/>
        <!-- Aurora curtains -->
        <path d="M 40,15 Q 50,35 45,65" fill="none" stroke="#44ff88" stroke-width="3" opacity="0.6"/>
        <path d="M 60,10 Q 70,30 65,65" fill="none" stroke="#44ff88" stroke-width="4" opacity="0.5"/>
        <path d="M 85,12 Q 95,35 90,65" fill="none" stroke="#88ffaa" stroke-width="3" opacity="0.55"/>
        <path d="M 110,8 Q 120,32 115,65" fill="none" stroke="#44dd88" stroke-width="3.5" opacity="0.5"/>
        <path d="M 135,10 Q 145,30 140,65" fill="none" stroke="#66ffcc" stroke-width="3" opacity="0.45"/>
        <path d="M 155,12 Q 165,35 160,65" fill="none" stroke="#44ff88" stroke-width="2.5" opacity="0.5"/>
        <path d="M 180,14 Q 190,33 185,65" fill="none" stroke="#88ffaa" stroke-width="3" opacity="0.4"/>
        <path d="M 200,10 Q 210,30 205,65" fill="none" stroke="#44dd88" stroke-width="2" opacity="0.45"/>
        <path d="M 220,13 Q 230,35 225,65" fill="none" stroke="#66ffcc" stroke-width="2.5" opacity="0.4"/>
        <!-- Glow effect -->
        <ellipse cx="130" cy="40" rx="100" ry="30" fill="#44ff88" opacity="0.05"/>
        <!-- Caption -->
        <text x="130" y="76" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#88aa88">plasma dynamics, made visible</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the physics of dimensional reduction.</p>
```

---

## Execution

**Phase A:** Add illustrations 1, 2, 4 (new inject functions in `preprocess.py`, add calls at ~line 5290)
**Phase B:** Add illustrations 3, 5 (hover_id + html: fields on existing entries in `tech-collapse.yaml`)
**Phase C:** Build, verify all 5 render, validate YAML.

## Do NOT

- Modify any .tex files
- Change existing SVG illustrations or inject functions
- Remove or modify existing tooltip text (only ADD html: fields alongside)
- Change the ordering of existing tech-collapse.yaml entries

## Commit

`Plan 0341: top 5 illustrations — factoring, network, heliosphere, power pattern, aurora`

---

## Handoff Prompt

```
You are the Generator. Read ~/software/relinquishment/plans/0341-top-5-illustrations.md.
Execute phases A-C.
Phase A: add 3 new inject functions to build/preprocess.py (inject_factoring_illustration,
inject_network_resilience, inject_power_pattern — code is in plan). Add their calls
after inject_silence_gap_illustration at ~line 5297.
Phase B: add hover_id: and html: fields to 2 existing entries in build/tech-collapse.yaml:
"The Neighborhood" and "Why Call It Two-Dimensional?" — content in plan.
Use html: | block scalar, 6-space content indent, matching existing rich panels.
Phase C: make html, validate YAML, verify all 5 figures render. Check deep links.
Do NOT modify .tex files. Commit: "Plan 0341: top 5 illustrations — factoring, network, heliosphere, power pattern, aurora"
```
