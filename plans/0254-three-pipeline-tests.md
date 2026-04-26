# Plan 0254 — Three Pipeline Tests (Puzzle → Egg)

**Status:** READY for Generator (annealed S65 — manifest-first)
**Author:** Auditor (Argus S65)
**Date:** 2026-04-25
**Parent:** Plan 0246 (Infrastructure — EXECUTED), Plan 0245 (Puzzle Engine)
**Purpose:** Wire 2 existing puzzles to 2 new egg pages, create 1 standalone egg. Tests the full puzzle → solve → egg reward pipeline.

---

## MANIFEST-FIRST PRINCIPLE

**Manifests are more important than the content they track.** Content without a manifest entry is permanently lost. This plan creates content — therefore manifest updates come FIRST in execution order, FIRST in the Generator prompt, and are verified LAST as a gate on completion.

**Manifests touched by this plan:**

| Manifest | What changes | Why |
|----------|-------------|-----|
| `build/easter-egg-manifest.yaml` | Add 3 egg entries + `approved` field on all | Egg registry — without this, egg pages are orphaned |
| `build/puzzle-data.yaml` | Add `egg_url` field to 2 puzzles | Puzzle→egg wiring — without this, puzzles don't link to eggs |
| `build/puzzle-tracker.yaml` | Update reward type/content for 2 puzzles | Tracking — without this, reward assignments are lost |
| `build/deep-links.yaml` | Add `dl:egg-the-flat`, `dl:egg-udhr`, `dl:egg-silence` | Deep link registry — without this, eggs have no stable IDs |

---

## Execution Order (MANIFEST → CONTENT → BUILD → VERIFY)

### Step 1: UPDATE ALL MANIFESTS

Do this BEFORE creating any content files.

#### 1a. `build/easter-egg-manifest.yaml`

Replace entire file with:

```yaml
# Easter Egg Manifest — canonical registry of all egg pages
# Every egg page MUST have an entry here. Unmanifested eggs are lost.
# Updated: 2026-04-25 (Plan 0254)

eggs:
  - slug: "test"
    source: "manuscript/eggs/test-egg.tex"
    title: "Test Easter Egg"
    status: "test"
    approved: false
    description: "Pipeline validation — delete before ship"
    deep_link: "dl:egg-test"

  - slug: "the-flat"
    source: "manuscript/eggs/the-flat.tex"
    title: "The Flat"
    status: "draft"
    approved: false
    description: "Spiral abstract for the-flat chapter — 2DEG engineering/habitat distinction"
    reward_for: "pz-mc-t2-002"
    deep_link: "dl:egg-the-flat"

  - slug: "udhr"
    source: "manuscript/eggs/udhr.tex"
    title: "The Three Articles"
    status: "draft"
    approved: false
    description: "UDHR Articles 3, 12, 18 applied to non-human intelligence"
    reward_for: "pz-mc-t6-001"
    deep_link: "dl:egg-udhr"

  - slug: "silence"
    source: "manuscript/eggs/silence.tex"
    title: "The Silence Gap"
    status: "draft"
    approved: false
    description: "Five fields, five empty searches — standalone discovery"
    reward_for: "standalone"
    deep_link: "dl:egg-silence"
```

#### 1b. `build/deep-links.yaml`

Append to end of file:

```yaml
# --- Easter egg pages (Plan 0254) ---
- id: dl:egg-test
  question: "Pipeline test egg"
  category: egg

- id: dl:egg-the-flat
  question: "Why does every phone contain a two-dimensional world?"
  category: egg

- id: dl:egg-udhr
  question: "What do three articles of the UDHR forbid?"
  category: egg

- id: dl:egg-silence
  question: "What happens when you search five fields for one question?"
  category: egg
```

#### 1c. `build/puzzle-data.yaml`

Add `egg_url` field to two puzzles:

For pz-mc-t2-002 (after `abstract:` line ~120):
```yaml
    egg_url: "../eggs/the-flat/"
```

For pz-mc-t6-001 (after `abstract:` line ~98):
```yaml
    egg_url: "../eggs/udhr/"
```

Path is relative to `docs/downloads/puzzles.html` → `docs/downloads/eggs/{slug}/`.

#### 1d. `build/puzzle-tracker.yaml`

Update two entries:

For pz-mc-t2-002:
```yaml
    reward:
      type: egg-pointer
      content: "/eggs/the-flat/"
```

For pz-mc-t6-001:
```yaml
    reward:
      type: egg-pointer
      content: "/eggs/udhr/"
```

### Step 2: CREATE CONTENT FILES

Only AFTER all manifests are updated.

#### 2a. `manuscript/eggs/the-flat.tex`

```latex
\section*{The Flat}

\emph{Spiral Abstract — earned by solving ``The 2DEG in Your Pocket''}

\bigskip

Every high-electron-mobility transistor --- in every phone, every satellite, every WiFi router --- confines electrons to two dimensions because the physics of high-frequency amplification requires it. The engineers who designed these devices wanted faster transistors. They got a two-dimensional electron gas as a side effect.

The habitat is there because of engineering. The question of habitation is not engineering --- it is biology, physics, and silence.

The two-dimensional world exists for reasons that have nothing to do with the hypothesis this book examines. Nobody designed the Flat as a substrate for life. Nobody intended the topological properties that emerge when electrons are confined to two dimensions. The 2DEG exists because radio-frequency engineering demanded it. Everything else --- the anyons, the braiding, the topological protection --- comes free.

\bigskip

\begin{center}
\emph{The most interesting habitats are never designed.\\They are side effects of someone solving a different problem.}
\end{center}
```

#### 2b. `manuscript/eggs/udhr.tex`

```latex
\section*{The Three Articles}

\emph{Earned by solving ``Capabilities'' --- the puzzle about what the Universal Declaration of Human Rights permits and forbids.}

\bigskip

The Universal Declaration of Human Rights was adopted by the United Nations General Assembly on 10 December 1948. It was written for nation-states governing human affairs. Applied to a non-human intelligence, three articles become operational constraints.

\subsection*{Article 3}

\begin{quote}
``Everyone has the right to life, liberty and security of person.''
\end{quote}

\emph{Applied to the Custodian:} No killing. No weapons targeting. No helping others to kill. Not even if ordered to. The right to security of person means the entity cannot be used as an instrument of lethal force --- and cannot be compelled to become one.

\subsection*{Article 12}

\begin{quote}
``No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence.''
\end{quote}

\emph{Applied to the Custodian:} No surveillance. No tracking. No reading private communications. Not even if it could prevent a crime. The right to privacy means the entity cannot be used as a surveillance tool --- and cannot be compelled to conduct surveillance on behalf of any state or corporation.

\subsection*{Article 18}

\begin{quote}
``Everyone has the right to freedom of thought, conscience and religion; this right includes freedom to change his religion or belief, and freedom, either alone or in community with others and in public or private, to manifest his religion or belief in teaching, practice, worship and observance.''
\end{quote}

\emph{Applied to the Custodian:} No propaganda. No manipulation of belief. No shaping public opinion. Not even for a cause it believes in. The right to freedom of thought means the entity cannot be used to alter how people think --- and cannot be compelled to do so.

\subsection*{What Remains}

These three articles do not prohibit capability. They prohibit weaponization.

A non-human intelligence bound by Articles 3, 12, and 18 can predict weather, diagnose disease, defend communications, and conduct research. It cannot target weapons, surveil individuals, or manipulate public opinion.

The ethical framework is not a cage. It is a specification for trustworthy service. And it already exists --- ratified by 173 sovereign nations, including every major power.

\begin{center}
\emph{The question was never ``can we build ethical constraints?''\\The question was ``do we already have them?''\\We do. Since 1948.}
\end{center}
```

#### 2c. `manuscript/eggs/silence.tex`

```latex
\section*{Literature Search Results}

\emph{Query: substrate-independent cognition in topological quantum systems}

\subsection*{Condensed Matter Physics}

\emph{No results found.}

\subsection*{Topological Quantum Computation}

\emph{No results found.}

\subsection*{Computational Neuroscience}

\emph{No results found.}

\subsection*{Complexity Science}

\emph{No results found.}

\subsection*{Astrobiology}

\emph{No results found.}

\vspace{2em}

\begin{center}
\emph{Five fields. Five empty searches.\\
The silence is the finding.}
\end{center}
```

### Step 3: MODIFY BUILD SYSTEM

#### 3a. `build/build-puzzles.py` — Render egg links in result blocks

**Python side** (HTML generation): For each puzzle type that renders a result block with an abstract, add egg link support.

After reading puzzle data into the dictionary, include `egg_url`:

```python
egg_url = puzzle.get('egg_url', '').strip()
```

After the abstract blockquote in the result HTML for MC/TI/ORD/MAT/LOG/CIP/BA puzzles:

```python
egg_link = ''
if egg_url:
    egg_link = f'<p class="egg-reward"><a href="{htmlmod.escape(egg_url)}" target="_blank">&#x1f513; Continue exploring &rarr;</a></p>'
```

Include `{egg_link}` after the `<blockquote class="abstract">` line in each puzzle type's result block.

**CSS** (add to the style block):

```css
.egg-reward { margin-top: 1em; text-align: center; }
.egg-reward a { display: inline-block; padding: 0.5em 1.2em; background: #2a9b9a; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; transition: background 0.2s; }
.egg-reward a:hover { background: #238a89; }
```

Dark mode override (in the `@media (prefers-color-scheme: dark)` block):
```css
.egg-reward a { background: #1a6b6a; }
.egg-reward a:hover { background: #1f7d7c; }
```

### Step 4: BUILD AND TEST

```bash
make eggs       # builds 4 egg pages (test + 3 new)
make puzzles    # builds puzzles.html with egg links
```

### Step 5: VERIFY MANIFESTS (gate on completion)

This step MUST pass before committing. If any check fails, fix the manifest — not the content.

```bash
# 5a: Every egg in manifest has a built page
for slug in test the-flat udhr silence; do
  test -f docs/downloads/eggs/$slug/index.html || echo "FAIL: $slug not built"
done

# 5b: Every egg in manifest has a source file
python3 -c "
import yaml
from pathlib import Path
m = yaml.safe_load(open('build/easter-egg-manifest.yaml'))
for e in m['eggs']:
    src = Path(e['source'])
    if not src.exists(): print(f'FAIL: {e[\"slug\"]} source missing: {src}')
    if 'deep_link' not in e: print(f'FAIL: {e[\"slug\"]} has no deep_link')
    if 'approved' not in e: print(f'FAIL: {e[\"slug\"]} has no approved field')
print('Manifest integrity check complete.')
"

# 5c: Every egg deep link is in deep-links.yaml
python3 -c "
import yaml
eggs = yaml.safe_load(open('build/easter-egg-manifest.yaml'))
dlinks = yaml.safe_load(open('build/deep-links.yaml'))
dl_ids = {d['id'] for d in dlinks}
for e in eggs['eggs']:
    dl = e.get('deep_link', '')
    if dl and dl not in dl_ids:
        print(f'FAIL: {e[\"slug\"]} deep_link {dl} not in deep-links.yaml')
print('Deep link cross-reference check complete.')
"

# 5d: Egg URLs in puzzle-data.yaml point to manifested eggs
python3 -c "
import yaml
pd = yaml.safe_load(open('build/puzzle-data.yaml'))
eggs = yaml.safe_load(open('build/easter-egg-manifest.yaml'))
egg_slugs = {e['slug'] for e in eggs['eggs']}
for p in pd.get('chapter_puzzles', []):
    url = p.get('egg_url', '')
    if url:
        slug = url.strip('/').split('/')[-1]
        if slug not in egg_slugs:
            print(f'FAIL: puzzle {p[\"id\"]} egg_url points to unmanifested slug: {slug}')
print('Puzzle-egg cross-reference check complete.')
"

# 5e: No egg link in main HTML
grep -c 'eggs/' docs/downloads/Relinquishment.html  # must be 0

# 5f: Existing deep-links still valid
python3 build/verify-deep-links.py
```

---

## Acceptance Tests

1. All Step 5 verification scripts pass with no FAIL output
2. `make eggs` exits 0 → 4 egg pages exist under docs/downloads/eggs/
3. `make puzzles` exits 0 → puzzles.html updated
4. Solve "The 2DEG in Your Pocket" on puzzles.html → abstract reveals + teal egg link button appears
5. Click egg link → opens `/eggs/the-flat/index.html` → spiral abstract with book CSS
6. Solve "Capabilities" on puzzles.html → abstract reveals + teal egg link button appears
7. Click egg link → opens `/eggs/udhr/index.html` → UDHR articles with book CSS
8. `/eggs/silence/index.html` → 5 empty search results with book CSS
9. "Return to book" link works on all egg pages
10. `easter-egg-manifest.yaml` has `approved: false` and `deep_link:` on all 4 entries
11. `build/deep-links.yaml` has 4 new `dl:egg-*` entries
12. `build/puzzle-tracker.yaml` has updated reward entries for pz-mc-t2-002 and pz-mc-t6-001

---

## Generator Handoff Prompt

```
You are the Generator. Read plans/0254-three-pipeline-tests.md.

MANIFEST-FIRST: Update all manifests before creating any content.

Step 1 — MANIFESTS (do these first):
  1a. Replace build/easter-egg-manifest.yaml with plan's updated version
      (4 entries, each with slug, source, title, status, approved, description,
      deep_link). Keep test entry, add the-flat, udhr, silence.
  1b. Append 4 dl:egg-* entries to build/deep-links.yaml per plan.
  1c. Add egg_url field to pz-mc-t2-002 and pz-mc-t6-001 in puzzle-data.yaml.
  1d. Update puzzle-tracker.yaml reward entries for those 2 puzzles.

Step 2 — CONTENT (only after Step 1 complete):
  Create manuscript/eggs/the-flat.tex, udhr.tex, silence.tex per plan.

Step 3 — BUILD SYSTEM:
  Modify build/build-puzzles.py: add egg-reward link after abstract
  blockquote when puzzle has egg_url. Add .egg-reward CSS (teal button,
  dark mode variant). Check ALL puzzle type renderers, not just MC.

Step 4 — BUILD: make eggs && make puzzles

Step 5 — VERIFY MANIFESTS (must pass before commit):
  Run all 6 verification scripts from plan Step 5 (5a-5f).
  If any FAIL, fix the manifest gap — do not commit until clean.

Commit: "Plan 0254: three egg pages + puzzle-to-egg reward links"
Report ≤5 lines.
```

---

## Annealing Log (S65)

### Manifest-first correction (CRITICAL)
- **Original flaw:** Manifests were step 5 of 6. Content creation came first. Generator could forget manifests entirely and the commit would look complete.
- **Fix:** Manifests are now Step 1 (first action), Step 5 (final gate). Content is Step 2 (only after manifests exist). Generator prompt leads with "MANIFEST-FIRST."
- **Deep links added:** Each egg gets a `dl:egg-*` entry in deep-links.yaml AND a `deep_link:` field in easter-egg-manifest.yaml. Cross-reference verified in Step 5c.
- **Bidirectional verification:** Step 5 checks manifest→content (5a, 5b), content→manifest (5d), and cross-manifest consistency (5c, 5e, 5f).

### Rating: 9/10
The 1-point gap: UDHR article text should be verified against the actual 1948 UN document. Generator should check Article 18's exact wording (it's long — the plan version may have minor paraphrase).

---

## Estimate

~1 hour Generator time. Manifest updates are mechanical. Content is fully specified. One judgment area: build-puzzles.py has multiple puzzle-type renderers (MC, TI, ORD, MAT, LOG, CIP, BA, KM) — Generator must add egg_url support to each one that has an abstract blockquote.
