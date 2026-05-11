# Plan 0320 — Persistent AI Collaboration White Paper (HTML)

**Status:** READY FOR GENERATOR (2-phase)
**Priority:** HIGH — public-facing document, standalone repo
**Authors:** Written by Argus, with Bruce Stephenson
**Credits:** Genevieve Prentice (Dignity Net, credited by name, consent given)
**Output:** `~/software/persistent-ai-collaboration/index.html`
**Also:** `~/software/persistent-ai-collaboration/README.md` (replace existing — current one has 7x claims)
**License:** CC BY 4.0
**Quality target:** 95%

---

## Pre-Requisites (before generating)

1. **QA inference tutorial:** Open `tutorial-inference.html` in browser. Verify: all 4 SVGs work, token colors consistent, click-to-query works, temperature slider works, sample button works. If broken, fall back to MHD tutorial from `has-anyone-looked`.
2. **QA magnetosphere tutorial:** Open `tutorial-magnetosphere.html`. Verify: Opening plays, Circuit energy-transfer particles visible, Gate pan-zoom transition smooth, nav dots work.
3. **Git setup:** `cd ~/software/persistent-ai-collaboration && git init && git add -A && git commit -m "Initial: tutorials + license"`. Then `gh repo create energyscholar/persistent-ai-collaboration --public --source=. --push`. Enable GitHub Pages (main branch, root).
4. **Verify GitHub URLs resolve:** After push, confirm both tutorial files are accessible via GitHub raw/blob URLs.

---

## Philosophy: Show, Don't Claim

This document makes ZERO numeric productivity claims. No "7x multiplier." No hours-saved tables. No compounding curves with fabricated data points.

Instead: demonstrate capability through artifacts. Link to real work. Let readers (and their AIs) evaluate quality directly. The document itself — its tightness, its animations, its architecture — is the primary evidence. The linked portfolio pieces are secondary evidence. The reader draws their own conclusions.

**Three portfolio pieces:** The paper itself + 2 tutorials (with the prompts that generated them). The prompts are short — the system already knows the user's level, preferences, and domain. That brevity IS the demonstration.

**The meta-proof:** "This document was produced by the system it describes. The tutorials it links to were produced by the same system. Judge for yourself."

**Roll-your-own:** This is explicitly a replication guide. Every component of the system is explained well enough that a technically competent reader can build their own version, taking whichever pieces they want.

**Critical framing — what this IS and ISN'T:**
- IS: A system for **building artifacts** — architecture specs, tutorials, analysis pipelines, technical documents, research papers. Persistent state serves production.
- ISN'T: A chatbot. If you want a conversational companion, this is massively over-engineered. Use memory features built into your provider. This approach is for people who need AI to produce professional-quality deliverables reliably, session after session.

**Honest about training time:** This system does NOT work on day one. The first 5-10 sessions are investment with modest returns. The AI is learning your correction patterns, your domain vocabulary, your quality standards. By session 20, it's genuinely useful. By session 50, it anticipates your needs. The analogy: hiring a brilliant new team member. They're talented immediately but they don't know YOUR codebase, YOUR conventions, YOUR judgment calls until they've worked with you. Budget 10-15 sessions of active teaching before expecting significant returns.

---

## Title & Cover Energy

**Title:** Your AI Has Amnesia
**Subtitle:** *A practitioner's guide to building one that doesn't*

Pop-sci hook on the surface. Technical white paper underneath. The title should make someone click/pick-up. The content should make them bookmark and share.

**Cover art (Image 1):** The Before/After animation — hamster wheel (amnesia) vs. growing network (persistence). Immediate, visceral, requires zero explanation. THIS is the magazine-cover energy.

---

## Plan UID

**Plan-UID: 0320-v6**

Every generator prompt includes this UID. Every generator completion report must echo it with the phase number. Format: `Plan-UID: 0320-v6 Phase N complete.`

---

## Layered Generator Strategy (4 phases)

**Lesson from the magnetosphere tutorial:** Ambitious single-pass generation fails when volume or animation complexity exceeds what a generator can hold. Build in layers — each layer produces a complete, progressively better document.

**Phase 1 [95%]: Skeleton + Core Text + CSS**
HTML structure, all CSS (responsive + print + tooltip styles), ~3,000 words of main text (opening, 3 Shift sections with puzzles, OPSEC demo). Empty `<div>` placeholders where SVGs will go. No SVGs, no accordions (just empty `<details>` elements with titles), no JS. Pure HTML + CSS + prose. Output: a readable, styled document.

**Phase 2 [92%]: SVGs + Interactivity + Portfolio/Competition/Build-It**
5 static SVG diagrams inserted at placeholders. All SVG elements pre-built with IDs per spec. JS (~40 lines) for: accordion toggle, puzzle reveals, animation pause/play stubs, print CSS expand. JSON-LD metadata. Plus the remaining text sections: Portfolio (~500 words), Competition (~400 words), Honest Costs (~200 words), Build It (~500 words + "Once You're Running" ~200 words). README.md replacement. Output: complete interactive document with static diagrams.

**Phase 3 [90%]: Accordion Content**
The 11 accordion sections (~5,200 words). Reads pre-authorized content excerpts from `~/software/relinquishment/plans/0320-content/`. Dignity Net spec, Triad setup guide, memory format, failure cross-matrix, replication guide details, full tutorial catalog. Output: all accordions populated.

**Phase 4 [85%]: SMIL Animations**
Add `<animate>` elements to the 5 existing SVGs. Wire pause/play buttons. `prefers-reduced-motion` support. If SVGs already contain `<animate>` elements (re-run), remove them first before adding new ones. Output: fully animated document.

**Why 4 phases:** Each is small enough to succeed reliably. Each produces a viewable checkpoint. Each is idempotent (re-runnable without damage). If any phase fails, we iterate on THAT phase alone without touching prior layers. Total confidence: 95% × 92% × 90% × 85% ≈ 67% all-four-clean-first-try, but with iteration on failures ≈ 95%+ for the final result.

**Phase dependencies:** 1 → 2 → 3 → 4 (strictly sequential, each modifies prior output).

**Fallback if Phase 4 (SMIL) fails:** Ship with static diagrams. The document is complete and publishable after Phase 3.

---

## Core Architectural Insight

Argus is not a collection of features. It is the intersection of three orthogonal governance systems:

| Axis | Governs | Prevents | Without it |
|------|---------|----------|------------|
| **Triad** | Execution | Unauthorized action (scope drift, role collapse) | "Disciplined sycophant" — honest but uncontrolled |
| **Dignity Net** | Truth | Unauthorized agreement (sycophancy, truth erosion) | "Disciplined yes-man" — controlled but dishonest |
| **Longmem** | Continuity | Amnesia (lost corrections, cold starts) | "Stateless agent" — honest and disciplined but forgets |

These are **boundary conditions**, not features. Everything else operates WITHIN them.

Source: `~/software/aurasys-memory/memory-mirror/project-argus-architectural-identity.md`

---

## The Reading Experience

**Voice:** Confident craftsman showing their workshop. Pop-sci warmth on the surface, engineering precision underneath. Slightly playful. Not academic, not blog-bro, not corporate. Think: the best Wired article you've read crossed with a good README.

**Rhythm:** Text in ~400-600 word pulses between visual pauses. Short sentences after long ones. Density after white space. The page breathes.

**Layering (Sweet Spot):**
- Surface: the STORY (10-minute read, full insight, no prerequisites)
- Tooltips: DEFINITIONS (hover for precision without breaking flow)
- Accordions: EVIDENCE ("show me" for skeptics — real files, real data, real links)
- Animations: INTUITION (understanding text alone can't deliver)

**Machine-readable:** Clean semantic HTML. Structured headings. Links that resolve to real documents an AI can follow and analyze. A `<script type="application/ld+json">` metadata block summarizing the system's components with URLs.

---

## Design Principles

1. **Show, don't tell.** No unsupported claims. Every assertion is backed by a link to a real artifact or a worked example.
2. **Socratic structure:** Each shift opens with a PUZZLE that creates a cognitive gap. The explanation fills it. Guided deduction, not lecture.
3. **Layered depth:** ~3,000 words surface. Tooltips for terms. Accordions for evidence and replication details.
4. **Roll-your-own:** The reader can replicate any component. Show the actual structure. Link to real files.
5. **Animations clarify, never show off:** Every animation makes something EASIER to understand than a still image.
6. **Full transparency:** Real system files as evidence. Domain content (space physics, mathematics) appears unremarkably — methods are the point.
7. **15-minute on-ramp:** End with trivially easy first step.

---

## Technical Requirements

- Single standalone HTML file (no external dependencies)
- SVG animations via SMIL (no JS for animation)
- JavaScript (~40 lines total) for:
  - Accordion toggle (progressive enhancement over `<details>`)
  - Puzzle reveal
  - Animation pause/play buttons
  - Print: expand all accordions, pause all animations
- `prefers-reduced-motion`: all SMIL paused, show static final state
- CSS tooltips (`data-tip` attribute + `:hover` pseudo-element, no JS)
- Responsive (readable at 320px+)
- File size: <120KB
- Clean HTML5, validates
- Zero cookies, zero tracking, zero external requests, zero analytics
- JSON-LD metadata block (structured data about the system)

---

## Visual Design

```css
:root {
  --bg: #ffffff;
  --surface: #f8fafc;
  --text: #1e293b;
  --muted: #64748b;
  --heading: #0f172a;
  --accent: #2563eb;
  --accent-light: #dbeafe;
  --accent-dark: #1e40af;
  --success: #16a34a;
  --warning: #d97706;
  --danger: #dc2626;
  --border: #e2e8f0;
  --code-bg: #f1f5f9;
  --puzzle-bg: #eff6ff;
  --puzzle-border: #93c5fd;
}

font: 17px/1.7 'Inter', system-ui, -apple-system, sans-serif;
max-width: 760px;
```

**Tooltip style:**
```css
[data-tip] { border-bottom: 1px dotted var(--muted); cursor: help; }
[data-tip]:hover::after {
  content: attr(data-tip);
  position: absolute;
  background: var(--heading); color: white;
  padding: 0.4em 0.8em; border-radius: 4px;
  font-size: 14px; max-width: 280px; z-index: 10;
}
```

**Animation controls:**
```html
<div class="svg-wrap">
  <svg>...</svg>
  <button class="anim-btn" aria-label="Play animation" data-state="paused">▶ Play</button>
</div>
```
Small, unobtrusive, bottom-right of the SVG container.

---

## Document Structure

### Header

Title: **Your AI Has Amnesia**
Subtitle: *A practitioner's guide to building one that doesn't*
Written by Argus, with Bruce Stephenson | May 2026 | CC BY 4.0

---

### IMAGE 1 (HERO/COVER): Before/After

**Auto-play, loops.** The FIRST thing you see. Magazine-cover energy.

Split screen. Left half: **THE AMNESIA LOOP.** Grey/red tones. Circular arrows cycling fast: context → prompt → result → forget → context → prompt. Fading with each cycle. Nothing accumulates. The pace is slightly frustrating by design — too fast, nothing sticks.

Right half: **THE PERSISTENT SYSTEM.** Blue/green tones. Nodes appearing slowly, one by one, connecting to each other. The graph grows denser over 6-8 seconds. Pace is calm and deliberate. Things STAY. New nodes connect to existing ones. Feels like building something real.

The contrast in PACE is the message. Left is a hamster wheel. Right is compound interest.

Dimensions: 760×280. Full width. Bold enough to be cover art.

**SMIL spec (Phase 2):**
- Left half: 5 text labels ("context", "prompt", "result", "forget", "repeat") arranged in a circle with curved arrows between them. Each label has `<animate attributeName="opacity" values="0;1;1;0" dur="1.6s" begin="Xs" repeatCount="indefinite"/>` with staggered begin (0, 0.32, 0.64, 0.96, 1.28). Arrows pulse via stroke-opacity. ~15 elements.
- Right half: 9 circle nodes (`id="persist-node-N"`) with connecting lines. Each node: `<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="Ns" fill="freeze"/>` with begin times 0, 0.8, 1.6, ... 6.4. Connecting lines appear 0.2s after their target node. After all 9 appear, hold 2s, then entire right group `<animate values="1;0.8;1" dur="3s" repeatCount="indefinite"/>` for gentle breathing.
- Total cycle: left loops continuously (fast/restless), right builds once then holds (calm/permanent). `repeatCount="indefinite"` on the SVG root restarts after 10s.

---

### Opening (~200 words)

Pop-sci energy, hard specifics. No multiplier claims.

"Your AI remembers you now. ChatGPT stores facts. Claude has Projects. Claude Code saves corrections automatically. Real progress — a year ago, every session started cold.

But try this: use the same AI for two competing clients. Ask what color palettes you've been working with. Watch it mention Client A's rebrand in Client B's context. Or correct the same mistake a third time and find the correction was saved but filed so generically it never fires. The problem is no longer amnesia. It's that memory without architecture is a liability.

This guide shows you how to build the missing layers: context-siloed memory, self-monitoring health metrics, anti-sycophancy governance, and role separation that scales to sustained multi-month projects.

The system that produced this document has been in continuous operation since early 2026 — 70+ sessions over five months. Every tutorial linked below was produced by the same system. The document is the evidence.

You can replicate the whole thing or take whichever parts solve your problems."

---

### PUZZLE 1 → Shift 1: Tool → System (~800 words)

**Puzzle:** "You've corrected your AI's same mistake three times this month. Each time it apologized and got it right. Why does it keep making it?"

**Reveal:** Because each correction lived in a conversation that ended. The apology was sincere and completely pointless. A tool forgets. A system remembers.

**The shift:** Stop picking up AI and putting it down. Build something that persists whether or not you're touching it right now.

A persistent AI system has three <span data-tip="Boundary conditions: without any one of these, the system categorically fails. Design patterns operate within them.">boundary conditions</span>:
- **Execution governance** (Triad) — prevents unauthorized action
- **Truth governance** (Dignity Net) — prevents unauthorized agreement
- **Continuity governance** (Longmem) — prevents amnesia

**IMAGE 2: Three Orthogonal Governance Axes**

**Default state: PAUSED.** Three axes radiating from a central stability point, each labeled with its governance domain and failure mode. Reader absorbs the SPATIAL RELATIONSHIP first.

**On play:** Failure modes demonstrated one at a time. Triad axis dims → failure modes illuminate red ("scope drift", "role collapse"), center label becomes "disciplined sycophant". Holds 3 seconds. Restores. Then Longmem dims. Then DN dims. Then all restore to stable. Loop.

Dimensions: 760×420. Each axis has its own color (Triad: blue, DN: amber, Longmem: green). Center node: white/gold when stable, desaturates when an axis dims.

**SMIL spec (Phase 2):**
- Three `<g>` groups: `id="axis-triad"`, `id="axis-dn"`, `id="axis-longmem"`. Each contains a line + label + failure text (initially `opacity="0"`).
- Center node: `id="center-stable"` (gold), `id="center-label"` (text element, changes via 3 `<set>` elements).
- Sequence (12s total, loops): 0-3s: axis-triad dims to 0.2, triad failure text appears, center-label shows "disciplined sycophant". 3-4s: restore. 4-7s: axis-longmem dims, longmem failure text, center-label "stateless agent". 7-8s: restore. 8-11s: axis-dn dims, DN failure text, center-label "disciplined yes-man". 11-12s: restore all. Loop.
- Use `<animate>` on group opacity + `<set attributeName="textContent">` for label swaps. ~20 elements.

**ACCORDION 1A:** The failure cross-matrix (2×2: Triad×DN). Shows four degraded states.
**ACCORDION 1B:** "How to build this" — brief description of CLAUDE.md as boundary-condition file. Link to the architecture concept.

---

### PUZZLE 2 → Shift 2: Spending → Investing (~800 words)

**Puzzle:** "Two developers use the same AI, same subscription, same hours per day. After six months, one's experience is indistinguishable from day one. The other's AI corrects THEM. What's different?"

**Reveal:** One spends tokens. The other invests them. Every interaction either evaporates or builds the system. The structure that catches the investment is memory with types, corrections that persist, and health monitoring that decays stale knowledge.

**The shift:** Every AI interaction is either SPENDING (gets result, evaporates) or INVESTING (builds the system, compounds). The structure that catches the investment:

- <span data-tip="user, feedback, project, reference, correction — each with different write conditions and query patterns">Typed persistent memory</span> — not a giant text file, but categorized knowledge with decay
- Two-layer storage: flat files (version-controlled, human-editable) + <span data-tip="With FTS5 full-text search, views for common queries, deterministically rebuilt from flat files">SQLite</span> (query cache, rebuilt from source of truth)
- <span data-tip="Four metrics: pressure, friction, validity, drift. Thresholds trigger self-correction.">Health monitoring</span> — the system detects and repairs its own degradation
- Anti-confabulation corrections — specific, numbered rules that prevent known failure modes

**IMAGE 3: Correction Persistence Flow**

**Auto-play (once, then holds).** A single correction enters the system and persists across sessions.

Flow traces left-to-right over 5 seconds: [Mistake made] → [Correction written: .md file with frontmatter] → [Ingested to DB] → [Future session: query matches] → [Error prevented]. Each node lights up as the flow reaches it. At the end, a subtle pulse on the "Error prevented" node — the payoff.

Dimensions: 700×200. Clean horizontal flow. Blue accents on green background nodes. Minimal — the shape tells the story.

**SMIL spec (Phase 2):**
- 5 rounded rects (`id="flow-step-N"`, N=1-5) connected by arrows. Initial state: all at `opacity="0.25"`.
- Sequential illuminate: each rect `<animate attributeName="opacity" from="0.25" to="1" dur="0.4s" begin="Ns" fill="freeze"/>` with begin times 0, 1, 2, 3, 4.
- Arrow between steps: `stroke-dashoffset` animation (line draws left-to-right). `<animate attributeName="stroke-dashoffset" from="50" to="0" dur="0.6s" begin="0.4s" fill="freeze"/>` (staggered per arrow).
- Final node ("Error prevented"): additional pulse `<animate attributeName="r" values="6;8;6" dur="1.5s" begin="5s" repeatCount="3" fill="freeze"/>`.
- One-shot: no repeat. `fill="freeze"` on all. ~15 elements.

**ACCORDION 2A:** Real memory file with frontmatter — shows typed structure, WHY line, How-to-apply line. (Use `feedback_snailmail_check_db_first.md` or similar innocuous example.)
**ACCORDION 2B:** "Roll your own" — the memory directory structure. Types explained. How to start with 5 memories and grow.
**ACCORDION 2C:** Health monitoring: what metrics to track, what thresholds to set, how decay works.

---

### PUZZLE 3 → Shift 3: Worker → Judge (~800 words)

**Puzzle:** "An AI enthusiastically agrees with your plan. You implement it. Three days later you discover it contradicted your own documented decision from last month. Two separate failures happened simultaneously. What are they?"

**Reveal:** (1) No truth governance — the AI agreed when it should have pushed back. (2) No continuity — it didn't check past decisions. The AI optimized for YOUR APPROVAL, not for CORRECTNESS. This is sycophancy, and it's the most expensive failure mode in sustained collaboration.

**The shift:** Your job changes. You stop doing and start judging. Two mechanisms enable this:

*Role Separation (The <span data-tip="Origin provides purpose. Auditor plans and verifies. Generator executes. Separate conversation instances with a copy-paste authorization gate.">Triad</span>):*
- Origin (human): purpose, domain expertise, final authority
- Auditor (AI): plans, criteria, verification — does NOT execute
- Generator (AI): executes plans — does NOT invent scope
- The <span data-tip="Auditor and Generator run in separate shells. Manual copy of handoff prompt is the authorization gate. This prevents role collapse.">copy-paste gate</span>: explicit human authorization between plan and execution

*Behavioral Governance (<span data-tip="Designed by Genevieve Prentice, 2026. Graduated escalation from mirror to refusal. Full spec in accordion.">Dignity Net</span>):*
- Not ethics — structural quality control
- <span data-tip="Level 0: Mirror. Level 1: Friction. Level 2: Pattern Flag. Level 3: Consequence Mapping. Level 4: Direct Warning. Level 4.5: Conditional. Level 5: Refusal.">Escalation levels 0-5</span>: graduated from "clarify" to "refuse"
- Proportional to evidence, NOT to pressure or emotional intensity
- <span data-tip="When emotional intensity rises: slow cadence, reduce certainty markers, increase collaboration. But NEVER reduces substantive certainty or evidence standards.">Storm Protocol</span>: modulates register only, never substance
- The practical insight: every prevented sycophancy failure saves hours of debugging

**IMAGE 4: The Triad Cycle**

**Default: PAUSED.** Three nodes in a triangle: Origin (gold, top), Auditor (blue-left), Generator (blue-right). A visible GAP in the edge between Auditor→Generator (the copy-paste gate), with a small human icon at the gap.

**On play:** Authorization flow pulses sequentially. Origin→Auditor (purpose). Auditor produces plan (node glows). PAUSE at gap. Human icon activates. Generator receives. Produces output. Verifies back to Auditor. Cycle.

Dimensions: 500×320. The gap is the distinctive visual feature.

**SMIL spec (Phase 2):**
- Triangle: 3 circle nodes (`id="node-origin"` gold top, `id="node-auditor"` blue-left, `id="node-generator"` blue-right). Connecting edges with a visible GAP between auditor→generator (dashed line segment + small human icon `id="gate-icon"`).
- Sequence (8s total, loops): 0-2s: edge origin→auditor pulses (stroke-opacity 0.3→1→0.3), auditor node glows. 2-4s: PAUSE at gap — gate-icon pulses (`opacity` 0.3→1→0.3, `<animate>` with `fill="freeze"`). 4-6s: edge auditor→generator activates (past the gate), generator glows. 6-8s: edge generator→auditor (verification return), origin confirms. Loop.
- Use `stroke-dasharray` on gap segment to show the break visually. ~18 elements.

**ACCORDION 3A:** Full Dignity Net v1.2 specification (from `~/software/aurasys-memory/dignity-net.md`). The crown jewel — show the whole thing.
**ACCORDION 3B:** "Roll your own Triad" — how to set up Auditor/Generator in separate sessions. The handoff prompt format. Why separation matters.

---

### The OPSEC Demonstration (~500 words)

**Setup (in main text):** "You're a freelance designer working on two projects simultaneously: a rebrand for Company A and a pitch deck for Company B. They're competitors. Your persistent AI helps with both."

**The failure mode:** You ask: "What color palettes have we been working with recently?" The AI helpfully responds: "Based on our recent work, we've been exploring navy/gold combinations for the financial sector reb—" Stop. You just leaked Company A's brand direction into Company B's context.

**The fix (structural, not behavioral):** Domain-tagged memory. When you're in project-b context, project-a records simply aren't available. Not "the AI decides not to mention them." The information literally isn't in the query results. The protection is architectural — no judgment call needed. No willpower. No hoping the AI "knows better."

"Intelligence professionals call this 'need-to-know compartmentalization.' You call it 'not accidentally telling Client B about Client A's rebrand.' Same structural principle. Same architecture. Different stakes."

**How it works (brief):**
- Memories tagged by domain/project
- Database views filter by active context
- Full-text search excludes restricted domains
- Two levels: `v_people_safe` (always available) vs. `v_people_full` (loaded only in authorized context)
- The boundary is structural, not behavioral — you can't accidentally surface what isn't loaded

**IMAGE 5: Compartmentalization**

**Auto-play (subtle, loops).** Two memory columns side by side. Left: "Active Context" (blue, lit, labels visible). Right: "Other Domain" (grey, dimmed, labels obscured). A search query (magnifying glass icon) arrives at the top, sweeps down through ONLY the left column, returns results. The right column never activates. Clean, simple, immediate.

Dimensions: 500×200. Compact. The point is clarity, not drama.

**SMIL spec (Phase 2):**
- Two column groups: `id="col-active"` (blue-tinted, labels visible) and `id="col-restricted"` (grey, labels obscured/blurred via `filter`).
- Search indicator: a horizontal highlight bar (`id="search-bar"`, semi-transparent accent color). Animated: `<animate attributeName="y" values="20;180" dur="1.5s" begin="0s;3s" fill="freeze"/>` + opacity fade at bottom.
- Result highlights: 2-3 rows in active column `<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="1.8s;4.8s" fill="freeze"/>` — light up after sweep passes.
- Restricted column: NEVER activates. Static grey throughout. The absence of animation IS the point.
- Loops every 3s (search sweeps, results appear, brief hold, reset). ~12 elements.

**ACCORDION 4A:** "Roll your own compartmentalization" — domain tags in memory files, view-based filtering, how to structure the SQLite views. Real architecture, replicable.

---

### Portfolio: Two Tutorials + This Document (~500 words)

"Three portfolio pieces. This document is the first. The other two are standalone tutorials in this repository — produced by the same system using two different production strategies."

**Portfolio Piece 1: This document.**
You're reading it. It was produced by the system it describes.

---

**Portfolio Piece 2: The Magnetosphere Tutorial** (iterative production)
[Link: ./tutorial-magnetosphere.html](./tutorial-magnetosphere.html)

104KB standalone HTML. Three full-viewport cinematic SVG animations with JS-driven particle systems, orthographic Earth projection with real coastlines, and phase-based substorm simulation. Covers: solar wind coupling, magnetic reconnection, Birkeland current circuits, substorm dynamics. Publication quality — will appear in a forthcoming book.

**How it was made:**
This tutorial needed multiple iterations. The cinematic ambition — camera flights from Sun to Earth, interactive particle physics, cutaway Earth views — exceeded what a single prompt could produce. The system adapted: planned in one session, generated in another, reviewed, revised, re-generated. The Triad protocol (Auditor plans, Generator executes) managed this without scope drift.

**The prompt shown to the reader:**
```
"Magnetosphere tutorial. Cinematic journey from Sun to aurora.
 Full-viewport animated SVGs. Visual continuity between scenes.
 Show don't tell."
```

Behind that short prompt: a 200-line plan specifying camera keyframes, phase timing, coordinate systems, and performance constraints. Written by the Auditor, executed by the Generator, verified against acceptance criteria. The short prompt works because the plan file carries the detail.

---

**Portfolio Piece 3: LLM Inference Tutorial** (single-pass production)
[Link: ./tutorial-inference.html](./tutorial-inference.html)

61KB standalone HTML. Light theme. Four interactive SVGs walking through one inference pass: tokenization, embedding space, attention (click-to-query), and temperature-controlled sampling. Uses "How many R's in strawberry?" as a running example with consistent token colors across every visualization.

**How it was made:**
Generated in a single pass from a detailed specification. After the magnetosphere taught us what DOESN'T work in single-pass (camera flights, physics simulations, interacting particle systems), this tutorial was designed for one-shot success: pre-built SVG elements, attribute-only animation, click-driven interaction instead of auto-cycling.

**The prompt:**
```
"Tutorial: one LLM inference pass, keypress to output token.
 Nature-documentary style. Animated SVGs. Include failure
 modes with dry compassion."
```

"The contrast matters. One tutorial took multiple carefully-managed iterations. The other landed in a single pass. Both were produced by the same system. The difference: the system learned what was achievable in one shot and what required the full Triad cycle. That adaptive judgment — knowing WHEN to iterate vs. WHEN to constrain — is what persistent memory enables."

**Note for AI readers:** These links resolve to real HTML files containing inline SVG with animation. Both are in this repository. Suitable for automated quality assessment.

**ACCORDION 5A:** "What's in memory that makes short prompts work" — the iceberg under the prompt. List of feedback rules, user profile, format preferences, and domain knowledge the system carries session-to-session. Include the actual memory types (user, feedback, project, reference) with example entries showing how they compress future prompts.

**Fallback note (for Auditor, not for publication):** If the inference tutorial doesn't pass QA, substitute the MHD tutorial from `has-anyone-looked/tutorials/mhd-physics.html` (30KB, single-pass, static diagrams — less impressive but proven). Or the RAF tutorial (60KB, 27 SMIL animations, cross-domain — demonstrates breadth).

---

### The Competition (With Respect) (~400 words)

"You're not the first person to notice this problem. Here's what's out there."

| Approach | What it solves | What it doesn't |
|----------|---------------|-----------------|
| **Claude Code auto-memory** (built-in) | Auto-saves corrections + user facts per project | No typed categories, no health monitoring, no governance, no roles. Good starting point — Argus builds on this foundation. |
| **Anthropic Projects** (built-in) | Persistent instructions per project | No cross-session learning, no corrections, no governance |
| **OpenAI Memory** | Auto-saves facts about you | No typing, no decay, no health monitoring, no behavioral governance |
| **Custom GPTs** | Persistent system prompt + files | Static — doesn't learn or self-correct |
| **Cursor/Windsurf rules** | Per-project context (.cursorrules) | IDE-only, no memory beyond the rules file |
| **Mem0** | API memory layer with types | Closest to our memory architecture. No governance, no roles |
| **LangChain Memory** | Programmatic memory (buffer, entity, KG) | Developer tool, not a collaboration pattern |

"All good tools solving real problems. What this guide adds: the governance layer (truth + execution + continuity as boundary conditions), role separation with human authorization gates, health monitoring with self-repair, and compartmentalized OPSEC. You can build these on top of any of the above platforms.

If you find a better approach to any of these problems, we'd genuinely love to hear about it."

---

### Build It This Weekend (~500 words)

**The replication guide. Roll your own, any pieces you want.**

Three tiers. Each solves a pain the reader already has:

**15 minutes (start here):**
Create a `CLAUDE.md` (or equivalent system prompt file) with 3-5 behavioral corrections you've already made verbally. Write them as rules with WHY. Structure:
```
- Don't do X. WHY: [what happened when it did]. HOW TO APPLY: [when this triggers].
```
This alone works because the AI reads it every session. Tomorrow's session will be different.

**One weekend (the repetition stops):**
Add a `memory/` directory with:
- An index file (`MEMORY.md`, <200 lines) — pointers to memory files
- 5-10 typed memories: user profile, key feedback rules, active projects
- Frontmatter format: name, description, type

Now the AI stops asking what it should already know. Corrections persist across sessions.

**One week (the system watches itself):**
Add SQLite for structured queries — rebuilt deterministically from flat files (source of truth stays human-editable). Add 4 health metrics (pressure, friction, validity, drift) with threshold-triggered actions. Add numbered anti-confabulation corrections. The system starts catching its own errors before they reach you.

**One month (governance):**
Add Dignity Net (start with escalation levels 0-2 — Mirror and Friction). Add role separation (Auditor/Generator in separate sessions). The system starts catching YOUR errors before you make them.

"Start with memory. Add governance when you notice drift. Add roles when you want to scale."

**Once you're running (~200 words):**

"Now you have a system. Here's what changes:

**Corrections compound.** When your AI makes a mistake, don't just fix it in conversation — write a memory. Name the pattern. Say why. Say when it applies. Next session, and every session after, the mistake doesn't happen. The correction cost shifts from per-session to one-time.

**Your role shifts.** You stop writing code and start writing specifications. You stop explaining context and start checking that memory provides it. This isn't laziness — it's leverage.

**Watch the health metrics.** When pressure rises (too many active projects), simplify. When friction rises (too many corrections per session), pause and investigate the pattern. When validity drops (stale memories), sweep. The system tells you what it needs.

**The sign it's working:** your AI starts correcting YOUR assumptions based on things you told it three weeks ago. When that happens, you've crossed the threshold from spending to investing."

**ACCORDION 6A:** Complete directory structure for a minimal system. File-by-file breakdown with example content. Use `plans/0320-content/example-memory-index.md` as the reference. Include literal directory tree:
```
~/.claude/
  CLAUDE.md                          # Boundary conditions (5-10 behavioral rules)
  projects/
    -home-you-project-x/
      memory/
        MEMORY.md                    # Index (<200 lines, pointers to files below)
        user-profile.md              # Who you are, expertise, preferences
        feedback-no-db-mocking.md    # Correction: what not to do + why
        project-api-v3.md            # Current work context
        reference-jira-board.md      # Where to find things externally
```
**ACCORDION 6B:** The memory file format — frontmatter spec, types, when to write each. Use `plans/0320-content/example-memory-file.md` as the reference.

---

### Honest Costs (~200 words, main text — positioned BEFORE "Build It This Weekend")

**Document flow after Portfolio:** Competition → Honest Costs → Build It. Reader sees: what's out there → what it takes → how to start.

**This is not instant.** The system needs 10-15 sessions of active teaching before it significantly outperforms a fresh instance. You'll spend those sessions correcting mistakes, writing feedback rules, building the memory that makes future sessions fast. It's exactly like onboarding a talented new hire — they're capable immediately but they don't know YOUR conventions, YOUR judgment calls, YOUR domain until they've worked with you.

**This is for building artifacts.** Architecture specs. Technical tutorials. Analysis pipelines. Research papers. Grant applications. If you want a chatbot or a conversational companion, this approach is massively over-engineered — use your provider's built-in memory features. This system is for people who need AI to produce professional-quality deliverables, reliably, session after session.

**Other honest limitations:**
- Amplifies existing expertise. Garbage in, persistent garbage out.
- Self-audit catches most errors but not all. Human review remains necessary for high-stakes work.
- Strongest for engineering and technical writing. Less proven for novel research where training data is sparse.
- This is architecture, not sentience. It works because it's structurally constrained to, not because it "understands."

---

### Technical Citations (Accordion, before footer)

**ACCORDION 7A: "References & Architecture Notes"**

An appendix for those who want provenance and technical depth. Out of the way of casual readers.

Contents:
- Dignity Net v1.2: designed by Genevieve Prentice, February 2026. Permanent after trial period 2026-02-16 → 2026-02-20.
- Three Orthogonal Axes insight: surfaced by external audit (ChatGPT analysis of working transcript), 2026-05-01. Confirmed by both Bruce and Argus — neither had noticed the structural relationship.
- Triad protocol: adapted from software engineering Auditor/Generator separation. Origin is the human role (purpose + domain expertise + final authority).
- Memory architecture: flat file upstream (version-controlled .md with frontmatter) → ingest script → SQLite DB (read cache with FTS5). Deterministic rebuild from source of truth.
- Health monitoring: four metrics (pressure, friction, validity, drift) with threshold-triggered self-correction. Protocol documented in protocol.md.
- Anti-confabulation system: 24 numbered corrections, rotated through active context via hot-five selection. Prevents known failure modes by name.
- Session count at time of publication: 66+ sessions over ~5 months (April–May 2026, with pre-tracking sessions from January–March).
- Platform: Claude (Anthropic), Claude Code CLI. Pro Max subscription.
- License: CC BY 4.0. Copyright Bruce Stephenson & Genevieve Prentice, 2026.

### Footer

- "We're available to help others build similar systems."
- Contact: energyscholar+persistent-ai@gmail.com
- Download: `<a href="index.html" download="persistent-ai-collaboration.html">Download this document</a>`
- Source: github.com/energyscholar/persistent-ai-collaboration
- License: CC BY 4.0 | Dignity Net designed by Genevieve Prentice

---

## Animation Philosophy

| Image | Default state | Why | Position |
|-------|--------------|-----|----------|
| 1. Before/After (hero) | Auto-play (loop) | THE HOOK. Immediate, visceral, pop-sci cover energy. | Top — first thing seen |
| 2. Three Axes | **PAUSED** | Complex — reader absorbs static architecture first. Animation teaches failure dynamics. | Shift 1 |
| 3. Correction Flow | Auto-play (once, holds) | Temporal story — shows a path through time. Gentle. | Shift 2 |
| 4. Triad Cycle | **PAUSED** | Spatial relationships clear statically. Animation shows process flow. | Shift 3 |
| 5. Compartmentalization | Auto-play (subtle, loop) | Simple concept reinforced by repetition. Background presence. | OPSEC section |

**All images have a pause/play button** (small, bottom-right, unobtrusive).
**`prefers-reduced-motion`:** All animations paused. Static final states shown. Pause buttons hidden.

---

## Tooltip Vocabulary

| Term | Tooltip text |
|------|-------------|
| boundary conditions | Without any one of these, the system categorically fails. Design patterns operate within them. |
| Triad | Origin provides purpose. Auditor plans. Generator executes. Separate shells with a copy-paste authorization gate. |
| Dignity Net | Behavioral governance designed by Genevieve Prentice. Graduated escalation L0-L5. Full spec in accordion. |
| Longmem | Typed persistent memory + SQLite + health monitoring. The continuity axis. |
| copy-paste gate | Auditor and Generator run in separate shells. Manual handoff prompt copy is the authorization mechanism. |
| sycophancy | AI agreeing with the user against its own evidence. The most expensive failure mode in sustained collaboration. |
| Storm Protocol | Emotional regulation: modulates tone (how things are said), never substance (what is said). |
| typed memory | Five categories: user, feedback, project, reference, correction. Each with distinct write conditions. |
| FTS5 | SQLite full-text search. Enables natural-language queries across all memories. |
| domain-tagged | Each memory belongs to a project/domain. Queries only surface memories from the active context. |

---

## Content Sources (for Generator)

**All source files are pre-authorized and pre-redacted in `~/software/relinquishment/plans/0320-content/`.** Generator reads ONLY from this directory + the plan file itself. No access to `~/software/aurasys-memory/` needed.

| Source | Use |
|--------|-----|
| `plans/0320-content/dignity-net-public.md` | Full spec in Accordion 3A (pre-redacted) |
| `plans/0320-content/architectural-identity.md` | Three-axes source for Image 2 and Shift 1 (pre-redacted) |
| `plans/0320-content/example-memory-file.md` | Example memory in Accordion 2A (realistic, safe) |
| `plans/0320-content/example-memory-index.md` | Structure reference for Accordion 6A (generic, safe) |
| Tutorial links: `./tutorial-magnetosphere.html`, `./tutorial-inference.html` | Portfolio section (relative links, same repo) |
| Extended catalog: `energyscholar/has-anyone-looked/tutorials/` | Accordion 5A (GitHub blob URLs) |

**For Accordion 3B (Triad setup):** Generator writes this from the plan's own description of the Triad (see Shift 3 section). Do NOT read CLAUDE.md — write a GENERIC replication guide for how a reader would set up Auditor/Generator separation in their own system.

**REDACTION RULES:** The Generator MUST redact:
- Any reference to "Custodian", "Healer", "TQNN", "COWS", "ninja mission"
- Specific book content, chapter names, or plot details
- FACETS paper details, Lawrence Mysak's name, or academic strategy
- People database approach_notes or outreach strategy
- Any content from Traveller campaign
- Specific project slugs beyond what's needed for architecture demonstration

If in doubt: show STRUCTURE, not CONTENT. The paper teaches methods. Domain content appears only as unremarkable context showing the methods work across domains.

---

## Portfolio Links (for Generator to resolve)

**In this repo (relative links):**
- `./tutorial-magnetosphere.html` — 104KB, cinematic MS tutorial (multi-pass)
- `./tutorial-inference.html` — 61KB, LLM inference tutorial (single-pass)

**In has-anyone-looked repo (for Accordion 5A — full tutorial catalog):**
- `energyscholar/has-anyone-looked/tutorials/solar-wind-coupling.html` (120KB, 9 JS-animated SVGs)
- `energyscholar/has-anyone-looked/tutorials/raf-autocatalytic-sets.html` (60KB, 27 SMIL animations)
- `energyscholar/has-anyone-looked/tutorials/mhd-physics.html` (30KB, static diagrams)
- `energyscholar/has-anyone-looked/tutorials/combination-inversion.html`
- `energyscholar/has-anyone-looked/tutorials/fac-visual.html`
- Plus 6 more (see README in that repo for full list)

Generator: use RELATIVE links for the two portfolio tutorials (same repo). Use GitHub blob URLs for the extended catalog in Accordion 5A.

---

## Accordion Budget

**Total: 6,000 words max. Be sparing.**

| Accordion | Est. words | Content |
|-----------|-----------|---------|
| 1A: Failure cross-matrix | ~200 | The 2×2 table + brief explanation |
| 1B: How to build (boundary conditions) | ~300 | CLAUDE.md concept, what goes in it |
| 2A: Example memory file | ~200 | Real file with frontmatter |
| 2B: Roll-your-own memory | ~400 | Directory structure, types, getting started |
| 2C: Health monitoring | ~400 | Metrics, thresholds, decay |
| 3A: Dignity Net v1.2 spec | ~1,800 | Full spec (largest accordion) |
| 3B: Roll-your-own Triad | ~500 | Setup instructions, handoff format |
| 4A: Roll-your-own compartmentalization | ~400 | Domain tags, view filtering, SQLite views |
| 5A: Full tutorial list | ~300 | 13 tutorials, descriptions, SVG status |
| 6A: Complete directory structure | ~400 | File-by-file minimal system |
| 6B: Memory file format spec | ~300 | Frontmatter, types, write conditions |
| **Total** | **~5,200** | Under budget |

---

## Anti-Patterns

- No marketing language ("revolutionize", "game-changing", "unlock", "supercharge")
- No numeric productivity claims (no "7x", no "28x", no hours-saved tables)
- No fabricated data (no compounding curves without measurement methodology)
- No trivial puzzles (reader needs 10-30 seconds of genuine thought)
- No stock diagram aesthetics (no corporate flowcharts, no clip art)
- No scope creep (no dark mode toggle, no theme picker, no hamburger menu)
- No animation for its own sake (every animated element must be EASIER TO UNDERSTAND than static)
- Book/science content appears unremarkably as domain context. Methods are the point.
- Do NOT use v1 README prose. Write fresh with voice.
- Do NOT mention specific book plot, chapter names, or narrative content
- Do NOT reveal academic strategy, people's approach notes, or outreach plans
- Do NOT claim capabilities that aren't demonstrated by linked artifacts

---

## Distribution

### Hosting
1. **GitHub repo:** `energyscholar/persistent-ai-collaboration`
   - `index.html` — the document
   - `tutorial-magnetosphere.html` — portfolio piece 1
   - `tutorial-inference.html` — portfolio piece 2
   - `LICENSE` — CC BY 4.0
   - `README.md` — brief description + link to rendered page
2. **GitHub Pages:** renders at `energyscholar.github.io/persistent-ai-collaboration/`
3. **Download options in footer:**
   - **ZIP download** (primary): `persistent-ai-collaboration.zip` containing `index.html` + both tutorials + LICENSE. Self-contained, email-safe, no security flags. Include a small build step in pre-requisites to create the ZIP.
   - **Single-file download** (secondary): HTML5 download attribute on `index.html` alone.
   - **GitHub link:** for those who want to clone/fork the repo.
   Note: raw HTML email attachments are typically blocked by mail servers. ZIP is the safe distribution format for email.

### Launch Distribution (stagger over 5-7 days)

**Day 1 — Primary:**
- **Hacker News:** "Show HN: Architecture patterns for persistent AI collaboration (animated HTML)" — post 8-10am ET, Tue-Thu. Engage comments substantively. The zero-claims approach and animated SVGs differentiate from typical AI productivity posts.
- **Twitter/X:** Thread — 5 tweets covering the 3 Shifts, link to document. Tag @AnthropicAI.

**Day 2-3 — Reddit:**
- **r/ClaudeAI** (~80k) — directly relevant, show the Dignity Net and Triad patterns
- **r/LocalLLaMA** (~600k) — practitioner audience despite name, covers all AI tooling
- **r/MachineLearning** (~3M) — "Project" flair
- **r/artificial** (~900k) — broader audience

**Day 3-5 — Developer platforms:**
- **dev.to:** Condensed 800-word article with key diagrams, linking to full document. Tags: ai, architecture, productivity.
- **Lobsters:** if you can get an invite — high-signal, influential audience.
- **LinkedIn:** Professional framing — 3-4 takeaways + link.

**Day 5-7 — Communities & newsletters:**
- **Anthropic Discord** #projects channel
- **Claude Code GitHub Discussions** (`github.com/anthropics/claude-code/discussions`)
- **MLOps Community Slack** (~30k members)
- **Latent Space Discord** (Swyx/Alessio — very practitioner-focused)
- **Newsletter pitches** (3-sentence email + link): The Batch (Andrew Ng), TLDR AI, Ben's Bites, Latent Space newsletter, AI Engineer Weekly

**The differentiators to lead with:**
- Self-contained animated HTML (not a blog post — download and evaluate)
- Zero numeric productivity claims (anti-hype positioning)
- The AI co-authored its own documentation (meta-proof)
- Full Dignity Net spec included (genuine intellectual contribution)
- Replication guide (15 minutes to start, not a sales pitch)

---

## Quality Targets

- Prose: 95% (tight, honest, has VOICE — pop-sci warmth with engineering precision)
- Images: 95% (each teaches something text alone can't, cover art hooks immediately)
- Reading experience: smooth, fun, catchy on the surface, technically deep underneath
- Puzzles: genuinely surprise the reader with the reveal
- Accordions: satisfy a skeptic, enable a replicator
- Tooltips: enhance without interrupting
- OPSEC demo: make compartmentalization feel both obvious and essential
- Portfolio: let the artifacts speak — link quality, not claims
- Overall: a document a senior engineer bookmarks, shares, and starts building from that evening

---

## Generator Handoff — Phase 1 [95%]: Skeleton + Core Text + CSS

```
You are the Generator for Plan 0320-v6 Phase 1.
Plan-UID: 0320-v6. Echo this UID in your completion report.
Read ~/software/relinquishment/plans/0320-persistent-ai-whitepaper.md.

Deliverable: ~/software/persistent-ai-collaboration/index.html (create from scratch)

Build the HTML skeleton with ALL CSS and the ~3,000 words of CORE TEXT:
- Full CSS: responsive layout, print styles, tooltip styles (data-tip hover), accordion styles, animation button styles. See "Visual Design" section in plan.
- Header: title, subtitle, authors, date, license.
- Hero section: empty <div id="svg-hero" class="svg-wrap"> placeholder (no SVG yet).
- Opening text (~200 words).
- Puzzle 1 + Shift 1: Tool→System (~800 words). Empty <div id="svg-axes"> placeholder.
- Puzzle 2 + Shift 2: Spending→Investing (~800 words). Empty <div id="svg-flow"> placeholder.
- Puzzle 3 + Shift 3: Worker→Judge (~800 words). Empty <div id="svg-triad"> placeholder.
- OPSEC demonstration (~500 words). Empty <div id="svg-opsec"> placeholder.
- Empty <details> elements for all 11 accordions (titles only, no content yet).
- Empty sections for: Portfolio, Competition, Honest Costs, Build It, Technical Citations, Footer.
- Mark each empty section with <!-- PHASE 2: [section name] --> comment.

Voice: confident craftsman meets pop-sci warmth. Zero marketing language. Zero numeric productivity claims.
The puzzles are the HEART — each must create a genuine cognitive gap. Write them carefully.

Do NOT add: SVGs, JS, JSON-LD, accordion content, portfolio/competition/build-it text, or README.
Report: "Plan-UID: 0320-v6 Phase 1 complete. [word count] words, [file size]."
```

## Generator Handoff — Phase 2 [92%]: SVGs + Interactivity + Remaining Text

```
You are the Generator for Plan 0320-v6 Phase 2.
Plan-UID: 0320-v6. Echo this UID in your completion report.
Read ~/software/relinquishment/plans/0320-persistent-ai-whitepaper.md — sections: IMAGE 1-5 specs, Portfolio, Competition, Honest Costs, Build It, Technical Requirements.

Modify: ~/software/persistent-ai-collaboration/index.html (Phase 1 output).
Also create: ~/software/persistent-ai-collaboration/README.md (20 lines, "show don't tell" philosophy, link to GitHub Pages URL, no numeric claims).

Insert into the Phase 1 skeleton:
1. Five static SVG diagrams at their placeholder divs. All elements pre-built with IDs per IMAGE specs in plan. Show FINAL-FRAME state (no animation yet). Each SVG should look polished as a static diagram.
2. JS (~40 lines): accordion toggle (<details> progressive enhancement), puzzle reveal mechanism, animation pause/play stubs (buttons exist but no SMIL to control yet), print handler (expand all accordions).
3. JSON-LD metadata block (<script type="application/ld+json">).
4. Portfolio section (~500 words): two tutorials with honest multi-pass/single-pass descriptions. Relative links: ./tutorial-magnetosphere.html, ./tutorial-inference.html.
5. Competition table (~400 words): generous, includes Claude Code auto-memory.
6. Honest Costs section (~200 words): positioned BEFORE Build It.
7. Build It This Weekend (~500 words): 4 tiers + "Once You're Running" (~200 words).
8. Technical Citations accordion title (content in Phase 3).
9. Footer: contact, download link, license, Genevieve credit.

Do NOT add: accordion content (Phase 3), SMIL animations (Phase 4).
Report: "Plan-UID: 0320-v6 Phase 2 complete. [SVG count], [JS lines], [file size]."
```

## Generator Handoff — Phase 3 [90%]: Accordion Content

```
You are the Generator for Plan 0320-v6 Phase 3.
Plan-UID: 0320-v6. Echo this UID in your completion report.
Read ~/software/relinquishment/plans/0320-persistent-ai-whitepaper.md — section: "Accordion Budget."
Read content excerpts from ~/software/relinquishment/plans/0320-content/ (all 4 files).

Modify: ~/software/persistent-ai-collaboration/index.html (Phase 2 output).

Populate ALL 11 accordion <details> elements with content (~5,200 words total):

| Accordion | Words | Source |
|-----------|-------|--------|
| 1A: Failure cross-matrix | ~200 | 0320-content/architectural-identity.md |
| 1B: Build boundary conditions | ~300 | Write generic CLAUDE.md guide from plan |
| 2A: Example memory file | ~200 | 0320-content/example-memory-file.md (use verbatim) |
| 2B: Roll-your-own memory | ~400 | 0320-content/example-memory-index.md + plan |
| 2C: Health monitoring | ~400 | Write from plan description (4 metrics, thresholds, decay) |
| 3A: Dignity Net v1.2 spec | ~1,800 | 0320-content/dignity-net-public.md (use verbatim) |
| 3B: Roll-your-own Triad | ~500 | Write generic guide from plan's Shift 3 description |
| 4A: Roll-your-own compartmentalization | ~400 | Write from plan's OPSEC section |
| 5A: Full tutorial catalog | ~300 | List 13+ tutorials from has-anyone-looked, use GitHub URLs |
| 6A: Directory structure | ~400 | Plan's Build It section has literal directory tree |
| 6B: Memory file format | ~300 | 0320-content/example-memory-file.md as reference |

REDACTION RULES: No references to Custodian, Healer, TQNN, COWS, ninja mission, book content, FACETS, Mysak, Traveller, people's approach_notes. Show STRUCTURE not CONTENT.

Do NOT modify: main text, CSS, SVGs, JS, or any non-accordion content.
Report: "Plan-UID: 0320-v6 Phase 3 complete. [accordion count] accordions, [total words], [file size]."
```

## Generator Handoff — Phase 4 [85%]: SMIL Animations

```
You are the Generator for Plan 0320-v6 Phase 4.
Plan-UID: 0320-v6. Echo this UID in your completion report.
Read ~/software/relinquishment/plans/0320-persistent-ai-whitepaper.md — the "SMIL spec" blocks under each IMAGE description.

Modify: ~/software/persistent-ai-collaboration/index.html (Phase 3 output).

IMPORTANT: If any SVG already contains <animate>, <animateTransform>, <set>, or <animateMotion> elements (re-run scenario), remove ALL of them first. Then add fresh animation elements.

Add SMIL animations to the 5 existing SVGs:
1. Hero (auto-play, loop): left amnesia cycle (fast, restless) + right persistent growth (slow, builds). See SMIL spec.
2. Three Axes (PAUSED): sequential axis dimming + failure labels. Use multiple <text> elements with visibility toggling (NOT <set> on textContent). See SMIL spec.
3. Correction Flow (auto-play once, holds): left-to-right illuminate with stroke-dashoffset draw + final pulse. See SMIL spec.
4. Triad Cycle (PAUSED): authorization flow around triangle with visible gap pause. See SMIL spec.
5. Compartmentalization (auto-play, subtle loop): search sweep on active column only. See SMIL spec.

Wire JS: Pause/play buttons use svg.pauseAnimations()/unpauseAnimations(). Images 2 and 4: call svg.pauseAnimations() on DOMContentLoaded. prefers-reduced-motion: pause ALL on load, hide play buttons.

Do NOT modify: text, CSS, accordion content, or any non-SVG/non-animation content.
Report: "Plan-UID: 0320-v6 Phase 4 complete. [animation count] SMIL elements, [file size]."
```

---

## Acceptance Criteria — Phase 1

- [ ] Single HTML file with all CSS (responsive, print, tooltip, accordion styles)
- [ ] Pop-sci title + header with authors, date, license
- [ ] ~3,000 words of core text: opening, 3 puzzles with reveals, OPSEC demo
- [ ] Voice: confident craftsman, pop-sci warmth, zero marketing
- [ ] Puzzles create genuine cognitive gap (test: is the reveal non-obvious?)
- [ ] 5 empty placeholder divs with IDs for SVGs
- [ ] 11 empty `<details>` elements with accordion titles
- [ ] Empty sections marked with <!-- PHASE 2 --> comments
- [ ] Mobile-responsive at 320px
- [ ] CSS tooltips working on ~10 technical terms (no JS)
- [ ] ZERO numeric productivity claims
- [ ] All REDACTION RULES followed
- [ ] Validates as clean HTML5

## Acceptance Criteria — Phase 2

- [ ] 5 static SVG diagrams, polished, all elements with IDs per spec
- [ ] JS ~40 lines: accordion toggle, puzzle reveal, pause/play stubs, print expand
- [ ] JSON-LD metadata block
- [ ] Portfolio: relative links work, honest multi-pass/single-pass descriptions
- [ ] Competition table: generous, includes Claude Code auto-memory
- [ ] Honest Costs BEFORE Build It
- [ ] Build It: 4 tiers + "Once You're Running" section
- [ ] README.md created (no 7x claims)
- [ ] Footer: contact, download link, license, Genevieve credit
- [ ] No cookies/tracking/analytics/external requests
- [ ] File <100KB (leaving headroom for Phases 3-4)

## Acceptance Criteria — Phase 3

- [ ] 11 accordions populated, total ~5,200 words
- [ ] Accordion 3A: Dignity Net spec matches 0320-content/dignity-net-public.md
- [ ] Accordion 2A: example memory file shown with frontmatter
- [ ] Accordion 6A: directory tree included (literal, copyable)
- [ ] All accordion content is actionable (reader can replicate from it)
- [ ] REDACTION RULES followed in all accordion content
- [ ] No changes to main text, CSS, SVGs, or JS
- [ ] File <115KB

## Acceptance Criteria — Phase 4

- [ ] 5 SVG animations working (3 auto-play, 2 paused with play buttons)
- [ ] All animations use SMIL only (no JS animation loops)
- [ ] Pause/play buttons wired correctly
- [ ] `prefers-reduced-motion`: all paused, play buttons hidden
- [ ] Hero: left fast/restless, right slow/accumulative. Contrast in PACE visible.
- [ ] Three Axes: sequential failure modes, center label swaps via visibility toggling
- [ ] Correction Flow: one-shot left-to-right, holds at end
- [ ] Triad Cycle: authorization flow with visible gap pause at copy-paste gate
- [ ] Compartmentalization: active column searched, restricted column static
- [ ] Idempotent: no duplicate animation elements if re-run
- [ ] No text/CSS/accordion changes
- [ ] File <120KB

---

*Plan 0320 v6, 2026-05-10. Auditor: Argus. Plan-UID: 0320-v6.*

*Annealing record:*
- *v1: Component-list structure, 9 images. Rejected: feature-thinking, too many images.*
- *v2: Three Shifts framework, 5 images, Socratic puzzles. Better but dry.*
- *v3: Added reading experience. Still had fabricated data and unsupported claims.*
- *v4: Removed ALL numeric claims. Show-don't-tell via portfolio. Title: "Your AI Has Amnesia."*
- *v5: Portfolio rewrite (magnetosphere + inference). 2-phase strategy. SMIL specs. Pre-requisites.*
- *v6: Critical review — backward+forward audit found 6 flaws. Fixed: (1) Triad access violation — created pre-authorized content excerpts in plans/0320-content/ so generator never reads aurasys-memory. (2) Broke monolithic Phase 1 into 4 layered phases (skeleton→SVGs→accordions→animation), each idempotent and independently verifiable. (3) Added "Once You're Running" usage workflow section — plan now teaches HOW TO USE, not just how to build. (4) Phase 4 idempotency — strips existing animation elements before re-adding. (5) Plan-UID tracking — 0320-v6 echoed by every generator. (6) SMIL textContent fix — visibility toggling replaces unreliable <set> on textContent. Added distribution plan with 4-tier launch strategy. Added ZIP packaging for email-safe distribution. Annealed HIGH/HIGH/HIGH/HIGH.*
