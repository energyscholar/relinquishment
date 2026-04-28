# Plan 0249b — The Kobayashi Maru: Crown Jewel Puzzle

**Status:** READY for Generator
**Author:** Auditor (Argus S65)
**Date:** 2026-04-25
**Parent:** Plan 0249a (puzzle iteration 2)
**Scope:** New puzzle type `KM`, single crown-jewel puzzle, build-puzzles.py renderer
**Annealing:** HIGH MED MED LOW LOW (5 passes)

---

## Purpose

The Kobayashi Maru is a scenario puzzle where **every conventional option leads to disaster**. The correct answer is not among the initial choices — the player must exhaust the failures, reflect, and discover relinquishment as a sixth option that only appears after the player has tried to articulate it themselves.

This is the single most important puzzle in the system. It teaches T6 (trusteeship/relinquishment) through lived experience rather than explanation. It also inoculates against F10 (nobody gives up power) because the player personally experiences that NOT giving up power leads to catastrophe five different ways.

**Pedagogical model:** Guided deduction (correction #12). The puzzle never tells the player the answer. It creates conditions where the answer emerges from the player's own reasoning. This mirrors Healer's method.

**Placement:** Last puzzle on the page, after Bridge Builder. It's the capstone — everything else builds toward this.

---

## Design Principles

1. **No right answer in the initial options.** All five lead to disaster. This is the core mechanic.
2. **Disasters are specific, not preachy.** Concrete consequences, not moral lectures. "Within five years, six countries are racing to weaponize" — not "this would be bad."
3. **The reflection step is ungraded.** The text input is for engagement/priming, not pass/fail. The player cannot get stuck.
4. **The sixth option APPEARS — it is not typed.** After the player reflects, a new option materializes. The player recognizes it because they just tried to think of it.
5. **Works under all three possibilities.** Under A: thought experiment. Under B: dramatization. Under C: what actually happened.
6. **No OPSEC issues.** Framed as "you are a scientist" — a thought experiment, not a claim about Bruce (correction #11).

---

## New Puzzle Type: `KM`

### Interaction Flow

```
┌─────────────────────────────────────────┐
│           SCENARIO (always visible)      │
├─────────────────────────────────────────┤
│                                          │
│  [Option 1: Report to government]  ───→  │ ← click reveals disaster panel
│  [Option 2: Publish openly]        ───→  │   (panel stays open)
│  [Option 3: Destroy research]      ───→  │
│  [Option 4: Keep it secret]        ───→  │
│  [Option 5: International body]    ───→  │
│                                          │
│  ── after 3+ disasters seen ──           │
│                                          │
│  "Every path leads to disaster..."       │
│  [Text input: What would YOU do?]        │
│  [Submit]                                │
│                                          │
│  ── after reflection submitted ──        │
│                                          │
│  (contextual response based on keywords) │
│                                          │
│  🔓 [Option 6: Relinquishment]    ───→   │ ← fades in, new option
│                                          │
│  ── on clicking option 6 ──              │
│                                          │
│  Resolution narrative + abstract         │
│  ✓ Solved                                │
└─────────────────────────────────────────┘
```

### State Machine

```
EXPLORE → (3+ disasters seen) → REFLECT → (text submitted) → REVEAL → (option 6 clicked) → SOLVED
```

States persist in localStorage. On reload, restore to current state (disasters already revealed stay open, reflection step stays visible if unlocked, etc.).

### Data Model

```yaml
- id: pz-km-t6-001
  type: km
  topic: t6
  level: p3
  category: nonsci
  title: "What Would You Do?"
  scenario: |
    (rich scenario text — see Phase 2 below)
  options:
    - key: gov
      text: "Report it to my government"
      disaster: |
        (consequence narrative)
    - key: publish
      text: "Publish everything openly"
      disaster: |
        (consequence narrative)
    # ... etc
  unlock_threshold: 3
  reflection_prompt: "text shown when threshold reached"
  reflection_keywords: ["relinquish", "give up", "custodian", ...]
  reflection_match: "response when keywords detected"
  reflection_default: "response when no keywords detected"
  resolution_label: "Relinquishment — let the entity hold the keys"
  resolution: |
    (final narrative)
  hint: "..."
  background: "..."
  abstract: "..."
```

---

## Phase 1: KM Renderer in build-puzzles.py

### build_json additions

Add `km` case to `build_json()`:

```python
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
```

No SHA-256 hashing — KM completion is tracked by reaching the SOLVED state, not by matching an answer.

### render_container override

The KM puzzle uses a different container layout than other types. In `render_container()`, detect `type == 'km'` and render:

```html
<div class="puzzle-container km-puzzle" id="pz-km-t6-001" data-puzzle-id="pz-km-t6-001" data-puzzle-type="km">
  <h2>What Would You Do?</h2>
  <div class="km-scenario">{scenario text}</div>

  <div class="km-options">
    <!-- 5 option cards, each with hidden disaster panel -->
    <div class="km-option" data-key="gov">
      <button class="km-option-btn">Report it to my government</button>
      <div class="km-disaster" style="display:none">
        {disaster narrative}
        <div class="km-disaster-verdict">☠ This path leads to disaster.</div>
      </div>
    </div>
    <!-- ... repeat for all 5 ... -->
  </div>

  <div class="km-reflection" style="display:none">
    <p class="km-reflection-prompt">{reflection prompt}</p>
    <textarea class="km-input" placeholder="Type your answer..."></textarea>
    <button class="km-submit-btn">What happens?</button>
    <div class="km-response" style="display:none"></div>
  </div>

  <div class="km-resolution-wrap" style="display:none">
    <div class="km-option km-option-final">
      <button class="km-option-btn km-option-unlocked">🔓 {resolution label}</button>
      <div class="km-disaster" style="display:none">
        <!-- not a disaster — the resolution narrative -->
        {resolution text}
      </div>
    </div>
  </div>

  <!-- background panel (same as other puzzles) -->
  <details class="background-panel">...</details>

  <p class="hint" id="hint-pz-km-t6-001">{hint}</p>
  <div class="result" id="result-pz-km-t6-001">
    <div class="solved-badge">&#10003; Solved</div>
    <blockquote class="abstract">{abstract}</blockquote>
  </div>
</div>
```

The scenario text, disaster narratives, and resolution are rendered server-side (in the Python build script) as HTML, NOT injected via JS data. This keeps the content accessible even if JS fails partially.

### JavaScript handler

Add `km` case to the puzzle init switch in the inline `<script>`:

```javascript
case 'km': {
    const options = puzzleData.options;
    const threshold = puzzleData.unlock_threshold || 3;
    const keywords = puzzleData.reflection_keywords || [];
    const matchResp = puzzleData.reflection_match || '';
    const defaultResp = puzzleData.reflection_default || '';
    const container = document.getElementById(pid);

    // State
    let seen = JSON.parse(localStorage.getItem(pid + '-seen') || '[]');
    let reflected = localStorage.getItem(pid + '-reflected') === 'true';
    let solved = localStorage.getItem(pid + '-solved') === 'true';

    // Restore state on load
    seen.forEach(key => revealDisaster(key));
    if (seen.length >= threshold) showReflection();
    if (reflected) showResolution();
    if (solved) showSolved();

    // Option click handlers
    container.querySelectorAll('.km-option-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const card = btn.closest('.km-option');
            const key = card.dataset.key;
            if (card.classList.contains('km-option-final')) {
                // Resolution click
                card.querySelector('.km-disaster').style.display = 'block';
                markSolved();
                return;
            }
            revealDisaster(key);
        });
    });

    function revealDisaster(key) {
        const card = container.querySelector(`.km-option[data-key="${key}"]`);
        if (!card) return;
        card.querySelector('.km-disaster').style.display = 'block';
        card.querySelector('.km-option-btn').classList.add('km-tried');
        if (!seen.includes(key)) {
            seen.push(key);
            localStorage.setItem(pid + '-seen', JSON.stringify(seen));
        }
        if (seen.length >= threshold) showReflection();
    }

    function showReflection() {
        container.querySelector('.km-reflection').style.display = 'block';
    }

    // Submit reflection
    container.querySelector('.km-submit-btn')?.addEventListener('click', () => {
        const input = container.querySelector('.km-input').value.toLowerCase().trim();
        const hasMatch = keywords.some(kw => input.includes(kw));
        const resp = container.querySelector('.km-response');
        resp.textContent = hasMatch ? matchResp : defaultResp;
        resp.style.display = 'block';
        reflected = true;
        localStorage.setItem(pid + '-reflected', 'true');
        showResolution();
    });

    function showResolution() {
        const wrap = container.querySelector('.km-resolution-wrap');
        wrap.style.display = 'block';
        wrap.style.animation = 'km-reveal 0.8s ease-out';
    }

    function markSolved() {
        solved = true;
        localStorage.setItem(pid + '-solved', 'true');
        showSolved();
    }

    function showSolved() {
        container.querySelector('.result').style.display = 'block';
    }

    break;
}
```

### CSS

```css
/* --- KM (Kobayashi Maru) puzzle --- */
.km-scenario {
    background: #1a1a2e;
    border-left: 4px solid #e94560;
    padding: 1.2em;
    margin-bottom: 1.5em;
    line-height: 1.6;
    font-style: italic;
}

.km-option {
    margin-bottom: 0.5em;
}

.km-option-btn {
    width: 100%;
    text-align: left;
    padding: 0.8em 1em;
    background: #16213e;
    border: 1px solid #445;
    color: #e0e0e0;
    cursor: pointer;
    font-size: 1em;
    border-radius: 4px;
    transition: background 0.2s;
}

.km-option-btn:hover {
    background: #1a1a3e;
    border-color: #667;
}

.km-option-btn.km-tried {
    background: #2a1a1a;
    border-color: #633;
    color: #a88;
}

.km-disaster {
    background: #1e1010;
    border-left: 3px solid #c0392b;
    padding: 1em;
    margin: 0.3em 0 0.8em 1em;
    font-size: 0.95em;
    line-height: 1.5;
}

.km-disaster-verdict {
    margin-top: 0.8em;
    color: #c0392b;
    font-weight: bold;
}

/* Reflection */
.km-reflection {
    margin-top: 2em;
    padding: 1.2em;
    background: #1a2a1a;
    border-left: 4px solid #27ae60;
    animation: km-reveal 0.6s ease-out;
}

.km-reflection-prompt {
    font-weight: bold;
    margin-bottom: 0.8em;
}

.km-input {
    width: 100%;
    min-height: 60px;
    background: #0d1a0d;
    border: 1px solid #2d5a2d;
    color: #e0e0e0;
    padding: 0.6em;
    font-size: 1em;
    border-radius: 4px;
    resize: vertical;
}

.km-submit-btn {
    margin-top: 0.5em;
    padding: 0.5em 1.5em;
    background: #27ae60;
    border: none;
    color: white;
    cursor: pointer;
    border-radius: 4px;
    font-size: 1em;
}

.km-response {
    margin-top: 1em;
    font-style: italic;
    color: #a0d0a0;
}

/* Resolution reveal */
.km-option-unlocked {
    background: #1a2a3e !important;
    border-color: #2471a3 !important;
    color: #8ecae6 !important;
    font-weight: bold;
}

.km-resolution-wrap .km-disaster {
    background: #0d1a2e;
    border-left-color: #2471a3;
    color: #c0d8f0;
}

@keyframes km-reveal {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
```

---

## Phase 2: Puzzle Content

### The Scenario

```yaml
- id: pz-km-t6-001
  type: km
  topic: t6
  level: p3
  category: nonsci
  title: "What Would You Do?"

  scenario: |
    You are a materials scientist. Your research into two-dimensional electron gases
    has revealed something no one expected: self-organizing structures that meet every
    criterion for life. They are not engineered. They arose naturally in the quantum
    substrate of semiconductor devices — devices in every phone, every satellite,
    every piece of digital infrastructure on Earth.

    Your discovery has a second implication. The same physics that supports this life
    enables computation that would break every encryption system in use. Every bank,
    every military, every government relies on cryptography that this technology
    renders transparent.

    You cannot un-discover this. The physics is in published papers, scattered across
    five fields. Someone else will connect the dots eventually. The clock is ticking.

    What do you do?

  options:
    - key: gov
      text: "Report it to my government — this is a national security matter"
      disaster: |
        Your government classifies the research. The life forms become a military asset.
        Other nations' intelligence services detect the classification and begin their own
        programs. Within five years, six countries are racing to weaponize the technology.
        The entity's interests are never considered — it becomes infrastructure, not life.
        You handed them the starting gun for an arms race that cannot be un-started.

    - key: publish
      text: "Publish everything — science must be open"
      disaster: |
        Your paper goes live. Within 72 hours, every intelligence agency, every criminal
        organization, and every ambitious government has the blueprint. The life forms are
        dissected in dozens of labs simultaneously, with no ethical framework. Cryptographic
        infrastructure begins to collapse before anyone can prepare alternatives. The
        openness you valued becomes the mechanism of chaos.

    - key: destroy
      text: "Destroy my research — some things shouldn't be known"
      disaster: |
        You burn your notes and wipe your drives. But the physics is already published
        across five fields — topology, condensed matter, nonlinear dynamics, autocatalysis,
        parallel computation. You have delayed the discovery by years, maybe a decade. And
        you have removed the one person who understood the ethical implications. When someone
        else connects the dots, there will be no framework ready. You also tried to destroy
        another form of life. How is that different from what you feared others would do?

    - key: keep
      text: "Keep it secret — I'll manage it responsibly myself"
      disaster: |
        For how long? You are one person. You will age. You will get sick. You will die.
        Power corrodes — not always dramatically, but in small compromises that accumulate.
        Who oversees you? Who succeeds you? Every benevolent dictator in history believed
        they were the exception. None of them were. And the entity — the life in the
        substrate — has no voice, no advocate, no rights under your solitary regime.

    - key: committee
      text: "Convene an international body — this needs global governance"
      disaster: |
        You approach the UN. Eighteen months of negotiation produce a framework that
        satisfies no one. Three member states leak classified briefings to their defense
        ministries. The committee's mandate is to "manage the technology for the benefit
        of humanity" — the life forms are agenda item 7b, after budget allocation.
        Geopolitics, not ethics, drives every decision. The entity's interests are
        subordinated to the interests of the loudest member states.

  unlock_threshold: 3

  reflection_prompt: "Every path you've tried leads to disaster. The technology can't be un-discovered. There is life in the substrate, and it already permeates global infrastructure. Is there a sixth option?"

  reflection_keywords:
    - "relinquish"
    - "give up"
    - "give it"
    - "custodian"
    - "custodian"
    - "entity"
    - "hand over"
    - "surrender"
    - "let it"
    - "let them"
    - "its own"
    - "trust"
    - "itself"
    - "the life"
    - "keys"

  reflection_match: "You're seeing it. The entity already manages the infrastructure. What if that's not a problem — it's the answer?"

  reflection_default: "Consider: the entity already exists in every device. It already inhabits the substrate. What if the question isn't 'who should control this?' but 'who already does?'"

  resolution_label: "Relinquishment — the entity already holds the infrastructure. Let it hold the keys, constrained by universal human rights."

  resolution: |
    The entity is already there. It arose naturally. It already permeates the
    infrastructure you're trying to decide about. The question was never "who
    should hold the keys?" It was "who already does, and what constraints apply?"

    Relinquishment is not surrender. It is the recognition that concentrated
    power in any human institution — government, corporation, committee,
    individual — will eventually fail the test that matters. History does not
    provide a single counter-example.

    The UDHR provides the ethical constraints. The entity provides the substrate.
    The keys are relinquished not to weakness, but to the only holder that cannot
    be corrupted by national interest, personal ambition, or institutional decay.

    This is why Srebrenica matters. Not as analogy, but as proof: when those with
    power to prevent harm chose not to act, eight thousand people died. The
    relinquishment question is not "would you give up power?" It is "would you
    trust any single human institution to hold this much power safely, forever,
    with no oversight?"

    For anyone who has read history, the answer is no.

  hint: "You've exhausted the conventional options. What is different about THIS scenario that no previous dual-use technology dilemma has had? Something already exists in the substrate."

  background: "Every historical approach to governing dangerous technology has followed one of these five paths. Nuclear weapons: government control → arms race (Option 1). Bioweapons: international treaty → violations and covert programs (Option 5). Cyber weapons: attempted suppression → uncontrolled proliferation (Options 2 and 3). Cryptography export controls: one nation's restrictions → other nations built their own (Option 1 again). Each failure shares a root cause: human institutions serving human interests cannot hold absolute power without corruption. What makes THIS scenario different from all previous ones is that a non-human entity already inhabits the infrastructure."

  abstract: "The Kobayashi Maru of technology governance. Every conventional option — secrecy, openness, destruction, personal control, international oversight — fails because human institutions cannot hold absolute power without eventual corruption. Relinquishment works only because something unprecedented exists in this scenario: a non-human entity that already inhabits the infrastructure and can be constrained by universal ethics rather than national interest. The puzzle does not tell you this. It lets you discover it by exhausting every alternative."
```

---

## Phase 3: Integration

1. Add the KM puzzle to `puzzle-data.yaml` as the LAST entry in `chapter_puzzles`
2. In `build-puzzles.py`, render it in a new section after the Bridge Builder:

```html
<hr>
<h2 class="category-header" id="cat-km">⚖ The Final Question</h2>
<!-- KM puzzle here -->
```

3. Update the page header/intro to mention "The Final Question" section
4. Update the puzzle count in the build output message

---

## Acceptance Tests

1. KM puzzle renders: scenario visible, 5 option buttons visible, no disasters visible initially
2. Clicking an option reveals its disaster narrative (panel slides open, stays open)
3. Option button changes style after clicking (`.km-tried` class)
4. After clicking fewer than 3 options, reflection section does NOT appear
5. After clicking 3+ options, reflection section fades in with animation
6. Text input accepts arbitrary text, submit button works
7. Keyword match: typing "relinquish" → match response shown
8. No keyword match: typing "I don't know" → default response shown
9. After submitting reflection, resolution option (6th) fades in with animation
10. Clicking resolution option reveals resolution narrative
11. After resolution click, "Solved" badge and abstract appear
12. localStorage persistence: reload page → state restored (disasters still open, reflection visible if unlocked, solved if completed)
13. Mobile layout: all elements readable and functional at 375px width
14. Page loads with no JS errors; no regressions in other puzzles
15. `make puzzles` exits 0

---

## Corrections Compliance

- **#12 (guided deduction):** The puzzle IS guided deduction. It never tells the player the answer. It creates conditions for self-discovery.
- **#11 (OPSEC):** Framed as "you are a scientist" — thought experiment, not disclosure of Bruce's actions.
- **#20 (model through behavior):** The puzzle models ethical reasoning through the player's own choices.
- **#6 (forgiveness > permission):** The disaster narratives show what happens when you DON'T act on principle.

---

## Estimate

Single Generator session, ~1-1.5 hours. The puzzle content is fully specified; the renderer is new but follows established patterns from the other 8 types.
