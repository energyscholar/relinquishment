# Plan 0340: Images & Puzzles — Graphic Novel Collapsed View

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** Plan 0339 (accordion expansion — execute first)
**Files:** `build/image-manifest.yaml` (new), `build/tech-collapse.yaml` (add `html:` fields), `build/preprocess.py` (CSS only)

---

## Objective

GA reader scanning The Flat with all sections collapsed sees a visually rich "graphic novel" experience — small SVG illustrations in tooltip panels, concept-symbol icons in collapsed title bars, and chapter-level hero images in always-visible content. The technical/pedagogical depth lives inside expanded sections; the collapsed surface tells a visual story.

---

## Current State (Inventory)

### Inline SVG Illustrations (in preprocess.py — 18 total)

| Function | Chapter | Figures | Notes |
|----------|---------|---------|-------|
| `inject_flat_diagram` | The Flat | 1 | Cross-section of 2DEG |
| `inject_button_sequence` | Genesis | 1 | Kauffman filmstrip (animated steps) |
| `inject_domain_buttons` | Genesis | 1 | Domain-specific button clusters |
| `inject_genesis_illustrations` | Genesis | 4 | Autocatalytic loop, edge-of-chaos, substrate parallel, substrate trinity |
| `inject_convergence_illustrations` | Convergence | 1 | Five-thread convergence star |
| `inject_ms_diagrams` | Wrong Substrate | 3 | Earth/Jupiter/Saturn magnetospheres |
| `inject_ms_animated_opening` | Wrong Substrate | 1 | Animated magnetosphere opening |
| `inject_promoted_illustrations` | The Braid | 4 | Braiding, anyon, rule-110, phase transition |
| `inject_sr_animation` | Sci Revolutions | 1 | Kuhn cycle animation |
| `inject_sr_illustrations` | Sci Revolutions | 1+ | Paradigm shift illustrations |

### Rich Tooltip Panels (in tech-collapse.yaml — 2 of 27)

Only "Buttons and Threads" and "From Chemistry to Computation" (both Genesis) have `html:` fields with inline SVGs. All other 25 entries are plain-text `tooltip:` only.

### `% IMAGE:` Placeholders (12 total, all magnetosphere)

All in `manuscript/spine/the-wrong-substrate.tex` and `manuscript/track-3-awakening/pos32-the-magnetosphere.tex`:
- Earth magnetosphere (bow shock, dayside, tail, field lines)
- Aurora borealis from ISS
- Plasma sheet cross-section (2D confinement)
- Jupiter magnetosphere (Io torus, scale)
- Solar system comparison (all planets)
- Heliospheric current sheet ("ballerina skirt")

### SVG Files (build/images/ — 9)

- `cover-triskellion.svg` — book cover
- `five-thread-convergence.svg` — convergence diagram
- `grid-sequence-1-regional.svg` through `grid-sequence-4-the-flat.svg` — scale zoom
- `magnetosphere-test.svg` — development artifact
- `raf-substrate-trinity.svg` — RAF/substrate/intelligence trinity
- `spaces-between-fields.svg` — silence gap visualization

### Puzzles (30 tracked, 13 installed)

| Category | Count | Installed |
|----------|-------|-----------|
| Chapter puzzles | 22 | 10 |
| Bridge puzzles | 7 | 0 |
| Master reward | 1 | 0 |

Manifests: `puzzle-tracker.yaml` (status), `puzzle-data.yaml` (content), `easter-egg-manifest.yaml` (5 eggs, 1 approved).

### Chapters with NO Visual Content (collapsed view = text-only)

These chapters have collapsed sections but no illustrations visible in the collapsed state:
1. **The Code War** — no SVGs, no rich tooltips
2. **The Factoring Game** — no SVGs, no rich tooltips
3. **Capabilities** — no SVGs, no rich tooltips
4. **The Silence Gap** — has `spaces-between-fields.svg` file but not inline
5. **Growing a Mind** — no SVGs (canopy_triptych referenced in puzzle data only)
6. **The Strongest Objection** — no SVGs, no rich tooltips
7. **Why Relinquish** — no SVGs, no rich tooltips

---

## Phase 1: Create Image Manifest

Create `build/image-manifest.yaml` documenting all images (inline SVGs, file SVGs, and placeholders).

```yaml
# Image Manifest — Plan 0340
# Authority for all visual assets in HTML output.
# Inline SVGs (in preprocess.py) and file SVGs (build/images/).
# Updated: 2026-05-16

inline_svgs:
  # Format: id, function, chapter, description, location (inside/outside collapse)

  - id: fig-flat-cross-section
    function: inject_flat_diagram
    chapter: the-flat
    description: "Cross-section of 2DEG — electron gas between semiconductor layers"
    location: outside-collapse
    
  - id: fig-buttons-filmstrip
    function: inject_button_sequence
    chapter: genesis
    description: "Kauffman buttons-and-threads — 6-step animated filmstrip"
    location: outside-collapse

  - id: fig-domain-buttons
    function: inject_domain_buttons
    chapter: genesis
    description: "Domain-specific button clusters (chemistry, biology, physics, CS, ethics)"
    location: outside-collapse

  - id: fig-autocatalytic-loop
    function: inject_genesis_illustrations
    chapter: genesis
    description: "Three-node autocatalytic cycle with arrows"
    location: outside-collapse

  - id: fig-edge-of-chaos
    function: inject_genesis_illustrations
    chapter: genesis
    description: "Order-chaos-edge spectrum with highlight at critical region"
    location: outside-collapse

  - id: fig-substrate-parallel
    function: inject_genesis_illustrations
    chapter: genesis
    description: "Chemistry ↔ quantum substrate comparison (twin circles)"
    location: outside-collapse

  - id: fig-substrate-trinity
    function: inject_genesis_illustrations
    chapter: genesis
    description: "RAF / substrate / intelligence trinity diagram"
    location: outside-collapse

  - id: fig-canopy-problem
    function: inject_genesis_illustrations
    chapter: growing-a-mind
    description: "Canopy triptych — competition for light analogy"
    location: outside-collapse

  - id: fig-five-thread-convergence
    function: inject_convergence_illustrations
    chapter: convergence
    description: "Five threads (Hasslacher, Freedman, Kauffman, Wolfram, Hillis) meeting at center"
    location: outside-collapse

  - id: fig-ms-earth
    function: inject_ms_diagrams
    chapter: the-wrong-substrate
    description: "Earth magnetosphere — bow shock, tail, field lines"
    location: outside-collapse

  - id: fig-ms-jupiter
    function: inject_ms_diagrams
    chapter: the-wrong-substrate
    description: "Jupiter magnetosphere — Io torus, scale"
    location: outside-collapse

  - id: fig-ms-saturn
    function: inject_ms_diagrams
    chapter: the-wrong-substrate
    description: "Saturn magnetosphere — ring current"
    location: outside-collapse

  - id: fig-braiding-inline
    function: inject_promoted_illustrations
    chapter: the-braid
    description: "Anyon braiding — worldlines crossing in 2+1D"
    location: outside-collapse

  - id: fig-anyon-inline
    function: inject_promoted_illustrations
    chapter: the-braid
    description: "Non-abelian anyon exchange"
    location: outside-collapse

  - id: fig-rule110-inline
    function: inject_promoted_illustrations
    chapter: the-braid
    description: "Rule 110 cellular automaton — universality"
    location: outside-collapse

  - id: fig-phase-transition-inline
    function: inject_promoted_illustrations
    chapter: the-braid
    description: "Phase transition threshold"
    location: outside-collapse

  - id: fig-kuhn-animation
    function: inject_sr_animation
    chapter: scientific-revolutions
    description: "Kuhn paradigm cycle — normal science → anomaly → crisis → revolution"
    location: outside-collapse

file_svgs:
  - file: build/images/cover-triskellion.svg
    usage: cover-image
    description: "Book cover — triple spiral"

  - file: build/images/five-thread-convergence.svg
    usage: source-for-inline
    description: "Five-thread convergence (source; inline version in preprocess.py)"

  - file: build/images/grid-sequence-1-regional.svg
    usage: standalone
    description: "Scale sequence 1 — regional magnetometer grid"

  - file: build/images/grid-sequence-2-global.svg
    usage: standalone
    description: "Scale sequence 2 — global coverage"

  - file: build/images/grid-sequence-3-magnetosphere.svg
    usage: standalone
    description: "Scale sequence 3 — magnetospheric context"

  - file: build/images/grid-sequence-4-the-flat.svg
    usage: standalone
    description: "Scale sequence 4 — the Flat as substrate"

  - file: build/images/magnetosphere-test.svg
    usage: development
    description: "Dev artifact — delete before ship"

  - file: build/images/raf-substrate-trinity.svg
    usage: source-for-inline
    description: "RAF/substrate/intelligence trinity (source)"

  - file: build/images/spaces-between-fields.svg
    usage: not-yet-inline
    description: "Silence gap — five fields with empty spaces between"

placeholders:
  # % IMAGE: comments in .tex files — not yet rendered
  - file: manuscript/spine/the-wrong-substrate.tex
    line: 29
    description: "Earth magnetosphere (bow shock, compressed dayside, extended tail, field lines)"
    status: "IMPLEMENTED — fig-ms-earth"

  - file: manuscript/spine/the-wrong-substrate.tex
    line: 52
    description: "Aurora borealis from ISS — plasma dynamics made visible"
    status: "NOT YET RENDERED"

  - file: manuscript/spine/the-wrong-substrate.tex
    line: 58
    description: "Plasma sheet cross-section — 2D confinement between magnetic lobes"
    status: "NOT YET RENDERED"

  - file: manuscript/spine/the-wrong-substrate.tex
    line: 75
    description: "Jupiter magnetosphere (Io torus, scale)"
    status: "IMPLEMENTED — fig-ms-jupiter"

  - file: manuscript/spine/the-wrong-substrate.tex
    line: 87
    description: "Solar system magnetosphere comparison — all planets to scale"
    status: "NOT YET RENDERED"

  - file: manuscript/spine/the-wrong-substrate.tex
    line: 93
    description: "Heliospheric current sheet — ballerina skirt"
    status: "NOT YET RENDERED"
```

## Phase 2: Rich Tooltip Panels for Priority Collapsed Sections

Add `html:` fields with inline SVGs to the collapsed sections that benefit most from visual preview. Priority = chapters with NO current illustrations in collapsed view.

Target: 8 new rich tooltip panels (matching the existing "Buttons and Threads" pattern).

### 2A: The Code War — "What the Movie Didn't Tell You"

```yaml
    hover_id: "collapse-cw-movie"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⚙ What the Movie Didn't Tell You</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">10,000 people kept a world-changing secret for 30 years. Knowledge walks out in minds, not in machines.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="240" height="70" viewBox="0 0 240 70" style="display:block;margin:0.4em auto 0.2em;">
        <title>Bletchley Park: a building with minds walking out as silhouettes, carrying invisible knowledge</title>
        <rect x="60" y="15" width="120" height="45" rx="3" fill="#f5f0e8" stroke="#8b7355" stroke-width="1"/>
        <rect x="90" y="25" width="15" height="20" fill="#d4c5a9" stroke="#8b7355" stroke-width="0.5"/>
        <rect x="135" y="25" width="15" height="20" fill="#d4c5a9" stroke="#8b7355" stroke-width="0.5"/>
        <rect x="108" y="35" width="24" height="25" fill="#6b5b3e" stroke="#8b7355" stroke-width="0.5"/>
        <path d="M 35,60 L 35,45 Q 35,40 38,40 L 42,40 Q 45,40 45,45 L 45,60" fill="none" stroke="#666" stroke-width="1.5"/>
        <circle cx="40" cy="36" r="4" fill="none" stroke="#666" stroke-width="1.2"/>
        <path d="M 15,60 L 15,45 Q 15,40 18,40 L 22,40 Q 25,40 25,45 L 25,60" fill="none" stroke="#999" stroke-width="1.2"/>
        <circle cx="20" cy="36" r="4" fill="none" stroke="#999" stroke-width="1"/>
        <path d="M 195,60 L 195,45 Q 195,40 198,40 L 202,40 Q 205,40 205,45 L 205,60" fill="none" stroke="#666" stroke-width="1.5"/>
        <circle cx="200" cy="36" r="4" fill="none" stroke="#666" stroke-width="1.2"/>
        <path d="M 215,60 L 215,45 Q 215,40 218,40 L 222,40 Q 225,40 225,45 L 225,60" fill="none" stroke="#999" stroke-width="1.2"/>
        <circle cx="220" cy="36" r="4" fill="none" stroke="#999" stroke-width="1"/>
        <text x="120" y="11" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#888">knowledge walks out in minds</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full WWII precedent.</p>
```

### 2B: The Code War — "The Dual-Use Pattern"

```yaml
    hover_id: "collapse-cw-dual-use"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⚙ The Dual-Use Pattern</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Every powerful technology enables both protection and attack. The same pattern, repeated across centuries.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="200" height="70" viewBox="0 0 200 70" style="display:block;margin:0.4em auto 0.2em;">
        <title>Dual-use: one technology branching into shield and sword</title>
        <defs>
          <marker id="arrowG" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2e7d32"/></marker>
          <marker id="arrowR" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c62828"/></marker>
        </defs>
        <circle cx="100" cy="35" r="18" fill="#f0f0f0" stroke="#555" stroke-width="1.2"/>
        <text x="100" y="39" text-anchor="middle" font-family="Georgia, serif" font-size="9" fill="#333">tech</text>
        <line x1="82" y1="35" x2="40" y2="20" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrowG)"/>
        <line x1="82" y1="35" x2="40" y2="50" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrowR)"/>
        <line x1="118" y1="35" x2="160" y2="20" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrowG)"/>
        <line x1="118" y1="35" x2="160" y2="50" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrowR)"/>
        <text x="35" y="16" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#2e7d32">protect</text>
        <text x="35" y="56" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#c62828">attack</text>
        <text x="165" y="16" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#2e7d32">protect</text>
        <text x="165" y="56" text-anchor="middle" font-family="Georgia, serif" font-size="8" fill="#c62828">attack</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full dual-use analysis.</p>
```

### 2C: The Silence Gap — "Eleven Domains"

```yaml
    hover_id: "collapse-silence-eleven"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⊘ Eleven Domains</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Eleven fields that should overlap but don't. Each siloed. No one asking the cross-domain question.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="260" height="60" viewBox="0 0 260 60" style="display:block;margin:0.4em auto 0.2em;">
        <title>Eleven circles with empty spaces between them — fields that don't talk</title>
        <circle cx="20" cy="30" r="8" fill="#f0e8e0" stroke="#a88b5e" stroke-width="0.8"/>
        <circle cx="44" cy="30" r="8" fill="#e8f0e8" stroke="#5ea88b" stroke-width="0.8"/>
        <circle cx="68" cy="30" r="8" fill="#e0e8f0" stroke="#5e8ba8" stroke-width="0.8"/>
        <circle cx="92" cy="30" r="8" fill="#f0e0e8" stroke="#a85e8b" stroke-width="0.8"/>
        <circle cx="116" cy="30" r="8" fill="#f0f0e0" stroke="#8ba85e" stroke-width="0.8"/>
        <circle cx="140" cy="30" r="8" fill="#e8e0f0" stroke="#8b5ea8" stroke-width="0.8"/>
        <circle cx="164" cy="30" r="8" fill="#e0f0f0" stroke="#5ea8a8" stroke-width="0.8"/>
        <circle cx="188" cy="30" r="8" fill="#f0e8e0" stroke="#a8a85e" stroke-width="0.8"/>
        <circle cx="212" cy="30" r="8" fill="#e8e8f0" stroke="#5e5ea8" stroke-width="0.8"/>
        <circle cx="236" cy="30" r="8" fill="#f0e0e0" stroke="#a85e5e" stroke-width="0.8"/>
        <circle cx="260" cy="30" r="8" fill="#e0f0e8" stroke="#5ea85e" stroke-width="0.8" transform="translate(-8,0)"/>
        <text x="130" y="55" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#888">no connections</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full domain survey.</p>
```

### 2D: Scientific Revolutions — "The Current Paradigm"

```yaml
    hover_id: "collapse-sr-paradigm"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⊘ The Current Paradigm</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Normal science has no category for this. The question crosses five fields; no single field owns it.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="180" height="70" viewBox="0 0 180 70" style="display:block;margin:0.4em auto 0.2em;">
        <title>A dotted boundary box labeled 'paradigm' with a question mark outside it</title>
        <rect x="30" y="10" width="100" height="50" rx="5" fill="none" stroke="#999" stroke-width="1.5" stroke-dasharray="4,3"/>
        <text x="80" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#666">normal science</text>
        <text x="155" y="42" text-anchor="middle" font-family="Georgia, serif" font-size="22" fill="#c0392b" font-weight="bold">?</text>
        <text x="80" y="6" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#999">paradigm boundary</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the institutional analysis.</p>
```

### 2E: Scientific Revolutions — "Anomaly Accumulation"

```yaml
    hover_id: "collapse-sr-anomalies"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⊘ Anomaly Accumulation</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Fourteen published observations that don't fit. None proves anything alone. Together: a pattern.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="220" height="60" viewBox="0 0 220 60" style="display:block;margin:0.4em auto 0.2em;">
        <title>Fourteen dots accumulating — each small, together forming an unmistakable cluster</title>
        <circle cx="15" cy="40" r="3" fill="#c0392b" opacity="0.4"/><circle cx="30" cy="35" r="3" fill="#c0392b" opacity="0.45"/>
        <circle cx="45" cy="38" r="3" fill="#c0392b" opacity="0.5"/><circle cx="60" cy="33" r="3" fill="#c0392b" opacity="0.55"/>
        <circle cx="75" cy="36" r="3" fill="#c0392b" opacity="0.6"/><circle cx="90" cy="31" r="3" fill="#c0392b" opacity="0.65"/>
        <circle cx="105" cy="34" r="3" fill="#c0392b" opacity="0.7"/><circle cx="120" cy="29" r="3" fill="#c0392b" opacity="0.75"/>
        <circle cx="135" cy="32" r="3" fill="#c0392b" opacity="0.8"/><circle cx="150" cy="27" r="3" fill="#c0392b" opacity="0.82"/>
        <circle cx="165" cy="30" r="3" fill="#c0392b" opacity="0.85"/><circle cx="180" cy="25" r="3" fill="#c0392b" opacity="0.88"/>
        <circle cx="195" cy="28" r="3" fill="#c0392b" opacity="0.92"/><circle cx="210" cy="22" r="3" fill="#c0392b" opacity="1.0"/>
        <line x1="10" y1="45" x2="215" y2="18" stroke="#c0392b" stroke-width="0.8" stroke-dasharray="3,2" opacity="0.5"/>
        <text x="110" y="55" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#888">14 published anomalies</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full observation list.</p>
```

### 2F: The Strongest Objection — "The Hobbit in the Mirror"

```yaml
    hover_id: "collapse-so-hobbit"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>The Hobbit in the Mirror</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Dunning-Kruger: the author doesn't know what he doesn't know. This chapter takes that seriously.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="180" height="70" viewBox="0 0 180 70" style="display:block;margin:0.4em auto 0.2em;">
        <title>A figure looking into a mirror — reflection shows a question mark</title>
        <rect x="110" y="10" width="40" height="55" rx="2" fill="#f5f5f5" stroke="#aaa" stroke-width="1.2"/>
        <circle cx="130" cy="30" r="10" fill="none" stroke="#ccc" stroke-width="1"/>
        <text x="130" y="35" text-anchor="middle" font-family="Georgia, serif" font-size="14" fill="#c0392b">?</text>
        <path d="M 60,60 L 60,40 Q 60,33 65,33 L 75,33 Q 80,33 80,40 L 80,60" fill="none" stroke="#555" stroke-width="1.8"/>
        <circle cx="70" cy="27" r="6" fill="none" stroke="#555" stroke-width="1.5"/>
        <line x1="80" y1="40" x2="110" y2="35" stroke="#ddd" stroke-width="0.8" stroke-dasharray="2,2"/>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full self-examination.</p>
```

### 2G: The Wrong Substrate — "The Oldest Niche"

```yaml
    hover_id: "collapse-ws-oldest-niche"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⬡ ◈ The Oldest Niche</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">Kauffman's conditions for spontaneous life — met in Earth's magnetosphere for 4.5 billion years. Longer than surface life.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="240" height="60" viewBox="0 0 240 60" style="display:block;margin:0.4em auto 0.2em;">
        <title>Timeline: magnetosphere niche open since 4.5 Gya, surface life since 3.8 Gya</title>
        <line x1="20" y1="30" x2="220" y2="30" stroke="#ccc" stroke-width="1"/>
        <rect x="20" y="22" width="200" height="8" rx="2" fill="#2471a3" opacity="0.3"/>
        <rect x="52" y="35" width="168" height="8" rx="2" fill="#27ae60" opacity="0.3"/>
        <text x="20" y="16" text-anchor="start" font-family="Georgia, serif" font-size="7" fill="#2471a3">magnetosphere: 4.5 Gya</text>
        <text x="52" y="55" text-anchor="start" font-family="Georgia, serif" font-size="7" fill="#27ae60">surface life: 3.8 Gya</text>
        <text x="220" y="30" text-anchor="start" font-family="Georgia, serif" font-size="7" fill="#888"> now</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the Kauffman conditions analysis.</p>
```

### 2H: Why Relinquish — "Bill Joy's Warning"

```yaml
    hover_id: "collapse-wr-bill-joy"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>⎈ Bill Joy's Warning</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">In 2000, a co-founder of Sun Microsystems published a terrified warning about technology. Ten structural parallels to this book.</p>
      <svg xmlns="http://www.w3.org/2000/svg" width="200" height="50" viewBox="0 0 200 50" style="display:block;margin:0.4em auto 0.2em;">
        <title>Two documents with connecting lines showing structural parallels</title>
        <rect x="15" y="8" width="35" height="40" rx="2" fill="#faf6f0" stroke="#a88b5e" stroke-width="0.8"/>
        <text x="32" y="32" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#666">2000</text>
        <rect x="150" y="8" width="35" height="40" rx="2" fill="#faf6f0" stroke="#a88b5e" stroke-width="0.8"/>
        <text x="167" y="32" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#666">2026</text>
        <line x1="50" y1="15" x2="150" y2="15" stroke="#c0392b" stroke-width="0.6" opacity="0.5"/>
        <line x1="50" y1="20" x2="150" y2="20" stroke="#c0392b" stroke-width="0.6" opacity="0.5"/>
        <line x1="50" y1="25" x2="150" y2="25" stroke="#c0392b" stroke-width="0.6" opacity="0.5"/>
        <line x1="50" y1="30" x2="150" y2="30" stroke="#c0392b" stroke-width="0.6" opacity="0.5"/>
        <line x1="50" y1="35" x2="150" y2="35" stroke="#c0392b" stroke-width="0.6" opacity="0.5"/>
        <text x="100" y="48" text-anchor="middle" font-family="Georgia, serif" font-size="7" fill="#c0392b">10 structural parallels</text>
      </svg>
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">Expand for the full parallel analysis.</p>
```

## Phase 3: Inline the Silence Gap SVG

The file `build/images/spaces-between-fields.svg` exists but is not rendered inline. Add an injection function in `build/preprocess.py` following the existing pattern.

**Step 1:** Add function definition (after `inject_sr_illustrations`, around line 4400):

```python
def inject_silence_gap_illustration(html_path):
    """Inject spaces-between-fields SVG into Silence Gap chapter intro (Plan 0340)."""
    html_path = Path(html_path)
    text = html_path.read_text()
    target_id = 'id="spine:silence-gap"'
    pos = text.find(target_id)
    if pos == -1:
        return
    # Find end of the chapter heading (</h1> or </h2>)
    heading_end = text.find('</h', pos)
    if heading_end == -1:
        return
    heading_end = text.find('>', heading_end) + 1
    # Find next paragraph or section start
    next_block = text.find('<', heading_end)
    # Read SVG file
    svg_path = REPO / 'build' / 'images' / 'spaces-between-fields.svg'
    if not svg_path.exists():
        return
    svg_content = svg_path.read_text()
    figure_html = f'''<figure id="fig-silence-gap" class="inline-svg" style="text-align:center;margin:1.5em auto;">
{svg_content}
<figcaption style="font-size:0.82em;font-style:italic;color:#888;margin-top:0.3em;">Five fields. The spaces between them.</figcaption>
</figure>
'''
    text = text[:next_block] + figure_html + text[next_block:]
    html_path.write_text(text)
```

**Step 2:** Add call at line ~5270 (after `inject_sr_illustrations(sys.argv[2])`):

```python
        inject_silence_gap_illustration(sys.argv[2])
```

## Phase 4: CSS for Collapsed Tooltip Panels

Add CSS ensuring rich tooltip panels (`html:` field content) render correctly:

```css
/* Rich tooltip panels — Plan 0340 */
.tech-collapse-panel svg {
  max-width: 100%;
  height: auto;
}
.tech-collapse-panel p {
  margin: 0 0 0.4em;
}
```

(Check if this CSS already exists from Plan 0219 — may only need verification, not new code.)

## Phase 5: Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | grep -E "Tech sections|Easter eggs|puzzles"
```

Check in browser:
1. Rich tooltip panels render on hover for all 8 new entries (SVGs visible in panel)
2. Existing Genesis panels still work (regression check)
3. Silence Gap SVG appears in chapter intro (outside collapse)
4. No layout breaks at mobile width

## Do NOT

- Modify any .tex files
- Change existing SVG illustrations or their injection logic
- Remove any existing entries from tech-collapse.yaml
- Change puzzle content or puzzle-tracker.yaml entries
- Create image manifest entries for illustrations that don't exist yet
- Add SVGs to plain `tooltip:` field (SVGs go in `html:` field only)

## Commit

`Plan 0340 phase N: image manifest + N rich tooltip panels for GA graphic novel view`

---

## Summary

| What | Count | Effect |
|------|-------|--------|
| New manifest file | 1 | `build/image-manifest.yaml` — single source of truth for all visual assets |
| New rich tooltip panels | 8 | GA reader sees SVG illustrations on hover over collapsed sections |
| Silence gap SVG inline | 1 | Always-visible illustration in currently text-only chapter |
| Chapters gaining visual collapsed experience | 5 | Code War, Silence Gap, Sci Revolutions, Strongest Objection, Why Relinquish |

**Net effect:** GA reader scrolling The Flat with all sections collapsed sees 8 more SVG illustrations on hover (up from 2), plus 1 new always-visible figure. Combined with Plan 0339's symbol-enriched tooltips, the collapsed view becomes visually informative — a "graphic novel" scan of the science.

---

## Handoff Prompt

```
You are the Generator. Read ~/software/relinquishment/plans/0340-images-puzzles-graphic-novel.md.
Execute phases 1-4. Phase 1: create build/image-manifest.yaml. Phase 2: add html: fields
with inline SVGs to 8 entries in build/tech-collapse.yaml (after Plan 0339 entries exist).
Phase 3: inline spaces-between-fields.svg into Silence Gap chapter. Phase 4: verify CSS.
Do NOT modify .tex files. Commit per phase.
```
