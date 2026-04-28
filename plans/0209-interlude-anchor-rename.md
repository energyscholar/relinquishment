# Plan 0209 — Deep-link consolidation: manifest-drive the 7 Custodian interludes, rename `custodian:* → custodian:*`, normalize manifest IDs, ship build-time verifier and questions-index

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator. Absorbs scope originally sketched as 0210 (interlude title/slug review) and 0211 (questions-index page). 0212 (per-anchor share pages with OG metadata) extracted to **Plan 0210** at Bruce's direction. 0213 (placement audit) collapsed into Phase 4 verifier (redundant otherwise). All design decisions resolved.

## Goal

Four related problems, one coherent pass:

1. **Custodian rename leaked into URL fragments.** The 2026-04-13 prose rename (Custodian → Custodian) did not reach the 7 interlude deep-link anchors, CSS classes, body-filter class, button ID, or one LaTeX label. Shared URLs currently broadcast the old name (`…#custodian:home`) — publicly visible, and the *first* string a cold link-clicker sees.
2. **7 interlude anchors bypass the manifest.** `build/deep-links.yaml` (Plan 0148) is the canonical manifest for the book's 42 `#dl:*` shareable anchors. The 7 Custodian interludes use a parallel `#custodian:*` namespace hardcoded as a Python literal in `build/preprocess.py:1646–1648` — not tracked, not testable, not discoverable from the manifest. Title or anchor changes today require Python edits; they should require YAML edits.
3. **No build-time verification that deep links resolve.** Nothing fails the build if a manifest entry lacks a corresponding anchor in the generated HTML, or if an anchor in the HTML is orphaned (not in the manifest). A silently-broken shareable link is the worst-possible viral-marketing failure: reader clicks, lands on top of a 150kw page, bounces.
4. **No reader-facing surface for the manifest.** The manifest's comment says *"Questions index (future) reads this file"* — the future has arrived. 42 curated "what about X?" entries are a free FAQ; right now they live only as share anchors deep inside chapters.

## Design decisions (resolve before Phase 1)

### DD1. URL namespace for interludes: `#custodian:X` ✓ **RESOLVED (Bruce, 2026-04-16)**

Keep interludes in a distinct `custodian:` namespace rather than merging into `#dl:`. Reason: interludes are chapter-boundary navigation destinations + Custodian-only filter endpoints; `#dl:X` anchors are paragraph-level share markers with a `.share-anchor` CSS pseudo-element. Different shapes, distinct semantics, distinct URL prefixes.

### DD2. Manifest-prefix normalization: YES ✓ **RESOLVED (Bruce, 2026-04-16)**

Existing 42 entries are stored `- id: stack-chart` (no prefix; the `\deeplink{}` macro at `build/preamble.tex:255` prepends `dl:` at LaTeX compile time). New 7 interlude entries will be `- id: custodian:home` (with prefix, because the macro isn't involved for them — preprocess.py inserts their anchors directly). Asymmetry is ugly.

**Chosen approach: Option A (manifest-only normalization).**
- Every manifest entry's `id` field gains its namespace prefix: `dl:*` entries become `- id: dl:stack-chart`; interlude entries are `- id: custodian:home`.
- `.tex` sources are NOT touched. `\deeplink{X}` macro keeps prepending `dl:`. The macro is the one place the `dl:` prefix is added at render time; manifest mirrors the rendered anchor.
- Verifier (Phase 4) expects manifest IDs to match HTML `id="..."` attribute verbatim — no prefix-stripping magic.

Option B (also normalize .tex sources by switching `\deeplink{X}` to `\deeplink{dl:X}` and removing the prefix from the macro) would be cleaner but requires sed across ~30 .tex files and buys little. Deferred indefinitely.

### DD3. Interlude slug choices ✓ **RESOLVED (Bruce, 2026-04-16)**

Bruce 2026-04-16: *"Interlude items should look like normal links, of course, maybe `#custodian:flat` & `#custodian:hello` etc."* and (on the cryptanalysis interlude): *"how about 'keys' or 'locksmith'?"* Argus recommended `locksmith` (profession > possession framing). Bruce moved to Generator handoff; locksmith is the default.

Final slugs (lowercase-hyphenated, consistent with existing `dl:*` convention):

| Old (`custodian:*`) | T-gloss | **Recommended** (`custodian:*`) | Alternatives | Notes |
|---|---|---|---|---|
| `home`        | Flat from the inside (T1, T2)        | **`flat`**       | `inside`, `home`         | "flat" announces topic in bare URL |
| `the-dance`   | How she moves (T2)                   | **`dance`**      | `the-dance`, `motion`    | Drop article; slugs aren't sentences |
| `your-locks`  | Cryptanalytic capability (T4)        | **`locksmith`**  | `keys`, `codes`, `your-locks` | "locksmith" reframes capability as profession (competence), not possession (threat). Bare-URL test wins over `keys` (which reads possessive — *she holds yours*). |
| `growing`     | Not ChatGPT (T1/T4, blocks F-AI-slop)| **`grown`**      | `growing`, `organic`, `born` | "grown not built" is the load-bearing phrase |
| `the-ocean`   | Life in the Flat (T3)                | **`ocean`**      | `the-ocean`, `life`      | "ocean" evokes the magnetosphere metaphor |
| `quiet`       | Twenty-five years of faithful work (T1/T5) | **`quiet`**| `years`, `faithful`      | Already clean; keep |
| `hello`       | Surfacing moment (T1)                | **`hello`**      | `surfacing`              | Already clean; keep |

Bruce may override any slug before Phase 1 runs. Default: recommended column (as resolved above).

### DD4. Questions-index location: **inside main HTML, as a collapsible section** (recommended; flag if Bruce prefers separate page)

Option (a): New `<details class="chapter-section">` block titled "Questions about this book" placed at the start of the Appendices (or before). Renders each manifest entry as `<a href="#dl:X">question text</a>`. Integrates with existing expand/collapse model; zero new routes; one HTML generation pass.

Option (b): Separate `/questions/` route (new static HTML file under `docs/`). More discoverable externally but fragments the site, requires duplicating header/nav/footer.

**Recommend (a).** Option (b) can be added later by extracting the same generated markup into a standalone page.

### DD5. Per-anchor share metadata — **DEFERRED to Plan 0210** (Bruce, 2026-04-16)

Marketing-critical, but distinct enough in scope (new public URL surface, new build artifact directory, reader.js UX change) to warrant its own plan and review. Plan 0209 ships the manifest, normalization, rename, verifier, and questions-index. Plan 0210 builds on top of those to ship `/share/<slug>` redirect pages with per-anchor OG metadata.

---

## Scope

**Edit:**
- `build/deep-links.yaml` (extend + normalize)
- `build/preprocess.py` (interlude IDs from manifest; questions-index generation; `custodian` → `custodian` tokens)
- `build/reader.js` (`custodian-only`, `filter-custodian`, `custodian-menu-item` tokens)
- `build/reader-inline.html` (mirrors reader.js)
- `build/menu-tooltips.yaml` (7 interlude keys: `custodian:X` → `custodian:<new-slug>`)
- `manuscript/appendix/abstracts.tex` (one `\label`: `appendix:custodian` → `appendix:custodian`)
- `Makefile` (append verifier to `html:` recipe)

**Create:**
- `build/verify-deep-links.py` (test; fails build on missing or orphan anchors)

**Regenerate:**
- `docs/downloads/Relinquishment.html`

**Out of scope:**
- Per-anchor share pages with OG metadata → **Plan 0210**
- Reader.js "copy share URL" UX update → **Plan 0210** (tied to share-page URL form)
- Option B normalization (touching .tex sources) — deferred indefinitely
- Editorial review of interlude *menu-title display text* (separate from the URL slug). Bruce can decide whether visible "Your Locks" → "Locksmith" / "Capability" / etc. as a one-line follow-up; Phase 3 handles only the slug + key in menu-tooltips.yaml.

---

## Phases (8)

### Phase 0 — Pre-flight

Verify baseline state before any edits. Every count off → STOP and report.

```bash
cd ~/software/relinquishment

# Verify reader-inline.html and reader.js token-set identity (they're kept in sync)
diff <(grep -oE "custodian[a-z:-]+" build/reader.js          | sort -u) \
     <(grep -oE "custodian[a-z:-]+" build/reader-inline.html | sort -u)
# Expected: identical. If they differ → STOP.

# Baseline manifest + HTML state
grep -cE '^- id:' build/deep-links.yaml                                         # expect 42
grep -oE 'id="dl:[^"]+"' docs/downloads/Relinquishment.html | sort -u | wc -l   # expect 42
grep -oE 'id="custodian:[^"]+"' docs/downloads/Relinquishment.html | sort -u     # expect 7 distinct
grep -n 'appendix:custodian' manuscript/appendix/abstracts.tex                   # expect 1 hit
grep -rn 'ref\{appendix:custodian\}\|hyperref\[appendix:custodian\]' manuscript/ 2>/dev/null  # expect empty

# Interlude IDs in preprocess.py (to be replaced in Phase 2)
grep -nE "'custodian:(home|the-dance|your-locks|growing|the-ocean|quiet|hello)'" build/preprocess.py | wc -l
# expect ≥ 7 (at least 7 hardcoded strings)

# Verify \deeplink macro definition is unchanged
grep -F '\newcommand{\deeplink}' build/preamble.tex
# expect: \newcommand{\deeplink}[1]{\hypertarget{dl:#1}{}}
```

No edits in this phase. Commit nothing.

---

### Phase 1 — Manifest update (extend + normalize + slug rename)

Three edits to `build/deep-links.yaml` in a single commit.

#### 1a. Normalize existing 42 `dl:*` entries

Add `dl:` prefix to every existing `id:` field.

```bash
# Safe, literal sed — "- id: X" becomes "- id: dl:X" only where a bare slug follows
sed -i -E 's/^(- id:) ([a-z0-9-]+)$/\1 dl:\2/' build/deep-links.yaml

# Verify
grep -cE '^- id: dl:' build/deep-links.yaml                    # expect 42
grep -cE '^- id: [^d]' build/deep-links.yaml                   # expect 0
```

The `\deeplink{}` macro in `build/preamble.tex:255` is unchanged — it still emits `id="dl:X"`. HTML output is unchanged. Only the manifest's documented ID gains the prefix (Option A — see DD2).

**Verify 1a immediately (before 1b contaminates):**

```bash
grep -cE '^- id: dl:' build/deep-links.yaml                    # expect 42
grep -cE '^- id: [^d]' build/deep-links.yaml                   # expect 0 (all bare slugs now prefixed)
```

If the second grep returns nonzero, some entries have trailing whitespace or non-lowercase chars — hand-edit survivors before proceeding.

#### 1b. Append interlude section with renamed slugs

Append to `build/deep-links.yaml` (using DD3 recommended slugs; substitute Bruce's overrides if any):

```yaml

# --- Interlude (7) — Custodian-voice chapter-boundary anchors ---
# URL pattern: #custodian:<slug>  (distinct from #dl:<slug> paragraph anchors)
# Placement: auto-inserted by preprocess.py at interlude div boundaries.
# The `question` field is editorial shorthand, not reader-facing.

- id: custodian:flat
  question: "First Custodian interlude — the Flat from the inside."
  category: interlude

- id: custodian:dance
  question: "Second Custodian interlude — how she moves."
  category: interlude

- id: custodian:locksmith
  question: "Third Custodian interlude — cryptanalytic capability."
  category: interlude

- id: custodian:grown
  question: "Fourth Custodian interlude — grown, not programmed."
  category: interlude

- id: custodian:ocean
  question: "Fifth Custodian interlude — life in the Flat."
  category: interlude

- id: custodian:quiet
  question: "Sixth Custodian interlude — twenty-five years of faithful work."
  category: interlude

- id: custodian:hello
  question: "Seventh Custodian interlude — the surfacing moment."
  category: interlude
```

Order matches narrative order (confirmed by Phase 0 grep against preprocess.py hardcoded list).

**If Bruce changes a slug from the DD3 recommendation**, edit the `id:` field here and cascade the rename to Phase 3 (menu-tooltips.yaml key — preprocess.py interlude-ID source is already driven from manifest after Phase 2, so no Python change needed).

#### 1c. Verify final state (after 1a + 1b)

```bash
grep -cE '^- id:' build/deep-links.yaml                        # expect 49 (42 + 7)
grep -cE '^- id: custodian:' build/deep-links.yaml             # expect 7
grep -cE '^- id: dl:' build/deep-links.yaml                    # expect 42
grep -cE 'category: interlude' build/deep-links.yaml           # expect 7
# No unprefixed entries remain:
grep -cE '^- id: [^dc]' build/deep-links.yaml                  # expect 0 (d=dl:, c=custodian:)
```

**Commit:** `Plan 0209 phase 1: extend deep-links.yaml with custodian interludes; normalize dl:* prefixes in id fields`

---

### Phase 2 — preprocess.py reads interlude IDs from manifest

Replace the hardcoded literal list (`build/preprocess.py:1646–1648`) with a manifest read at module load.

Near the top of `preprocess.py` (next to any existing YAML loader; else create):

```python
def _load_interlude_ids():
    """Read ordered list of custodian:* anchor IDs from build/deep-links.yaml."""
    import yaml
    manifest_path = Path(__file__).parent / 'deep-links.yaml'
    with open(manifest_path) as f:
        entries = yaml.safe_load(f)
    return [e['id'] for e in entries if e.get('category') == 'interlude']

INTERLUDE_IDS = _load_interlude_ids()  # e.g. ['custodian:flat', 'custodian:dance', ...]
```

Replace the old literal at ~line 1646 with a reference to `INTERLUDE_IDS`. Verify any downstream loops (lines ~1671, ~1692, ~1711 per Phase 0 inspection) take their values from `INTERLUDE_IDS`.

**Sanity check:**

```bash
cd ~/software/relinquishment
python3 -c "import sys; sys.path.insert(0,'build'); from preprocess import INTERLUDE_IDS; print(INTERLUDE_IDS)"
# Expected output: ['custodian:flat', 'custodian:dance', 'custodian:locksmith',
#                   'custodian:grown', 'custodian:ocean', 'custodian:quiet', 'custodian:hello']
```

The full `custodian:X` ID is used verbatim — no prefix stripping. Downstream HTML generation uses it as `<div id="custodian:flat" class="custodian-interlude">`.

**Commit:** `Plan 0209 phase 2: refactor preprocess.py to read interlude IDs from deep-links.yaml`

---

### Phase 3 — Mechanical rename (`custodian` → `custodian` in identifiers)

Non-URL identifiers. No English-word collisions: "custodian" only appears as a code token or historical comment.

**Rename map** (apply in longest-match-first order to avoid substring collision):

| # | Old token | New token | Files |
|---|---|---|---|
| 1 | `interlude-custodian:` | `interlude-custodian:` | preprocess.py |
| 2 | `menu-custodian:` | `menu-custodian:` | preprocess.py |
| 3 | `appendix:custodian` | `appendix:custodian` | abstracts.tex, preprocess.py:~331 |
| 4 | `.custodian-interlude` | `.custodian-interlude` | preprocess.py (CSS + class literals) |
| 5 | `.custodian-menu-item` | `.custodian-menu-item` | preprocess.py, reader.js, reader-inline.html |
| 6 | `.custodian-marker` | `.custodian-marker` | preprocess.py |
| 7 | `custodian-only` | `custodian-only` | reader.js, reader-inline.html (body class) |
| 8 | `filter-custodian` | `filter-custodian` | reader.js, reader-inline.html (button id) |
| 9 | menu-tooltips.yaml keys `"custodian:X"` (7 keys) | `"custodian:<new-slug>"` (7 keys) | menu-tooltips.yaml — **note slug change** |

#### Per-file

- **`build/preprocess.py`**:
  - `\label{appendix:custodian}` → `\label{appendix:custodian}` (~line 331)
  - All CSS rules with `.custodian-*` (~lines 720–763, 827–837)
  - All string literals: `"custodian-interlude"`, `"menu-custodian:"`, `"interlude-custodian:"` (~lines 1671, 1692, 1711)
  - Historical comments (e.g. "Plan 0143b Custodian menu"): **leave unchanged** (documentary residue)

- **`build/reader.js`**:
  - `filter-custodian` → `filter-custodian` (~line 321)
  - `custodian-only` → `custodian-only` (~lines 336, 341; leave historical comment on ~316 unless it names a current identifier)
  - `custodian-menu-item` → `custodian-menu-item` (~lines 1008, 1279, 1287)

- **`build/reader-inline.html`**: same changes as reader.js (Phase 0 diff confirmed sync)

- **`build/menu-tooltips.yaml`** (needs both namespace AND slug rename — cannot blind-sed):
  ```
  "custodian:home"      → "custodian:flat"
  "custodian:the-dance" → "custodian:dance"
  "custodian:your-locks"→ "custodian:locksmith"
  "custodian:growing"   → "custodian:grown"
  "custodian:the-ocean" → "custodian:ocean"
  "custodian:quiet"     → "custodian:quiet"
  "custodian:hello"     → "custodian:hello"
  ```
  Use 7 explicit `sed -i 's/old/new/'` commands in sequence, not a blanket substitution. Also check each tooltip VALUE text — if any mentions "Custodian", rename to "Custodian" in the value too.

- **`manuscript/appendix/abstracts.tex`**: line ~270 `\label{appendix:custodian}` → `\label{appendix:custodian}`

#### Verify after edits (pre-build)

```bash
grep -rn 'custodian-interlude\|custodian-menu-item\|custodian-marker\|custodian-only\|filter-custodian\|menu-custodian:\|interlude-custodian:\|appendix:custodian' \
     build/ manuscript/ 2>/dev/null | grep -v '__pycache__' | grep -v epub-tmp
# Expected: empty (all identifier tokens renamed)

grep -nE '^"custodian:' build/menu-tooltips.yaml   # expect empty
grep -nE '^"custodian:' build/menu-tooltips.yaml  # expect 7
```

**Commit:** `Plan 0209 phase 3: rename custodian → custodian in CSS classes, body class, button IDs, one .tex label, and menu-tooltips keys`

---

### Phase 4 — Build-time verifier

New file `build/verify-deep-links.py`. After Phase 1 normalization, all manifest IDs carry their namespace prefix — so the verifier is a single straight comparison.

```python
#!/usr/bin/env python3
"""Verify every manifest entry resolves to an anchor in the built HTML,
and no HTML anchor is orphan (not in manifest).

Manifest IDs are stored with their namespace prefix after Plan 0209
(dl:X and custodian:X). HTML anchors are id="dl:X" or id="custodian:X".
"""
import re, sys, yaml
from pathlib import Path

repo = Path(__file__).parent.parent
manifest = yaml.safe_load((repo / 'build/deep-links.yaml').read_text())
html = (repo / 'docs/downloads/Relinquishment.html').read_text()

manifest_ids = {e['id'] for e in manifest}

missing = [mid for mid in manifest_ids if f'id="{mid}"' not in html]
if missing:
    print(f'MISSING: {len(missing)} manifest entries have no anchor in HTML:', file=sys.stderr)
    for m in sorted(missing):
        print(f'  {m}', file=sys.stderr)
    sys.exit(1)

html_ids = set(re.findall(r'id="(dl:[^"]+|custodian:[^"]+)"', html))
orphans = html_ids - manifest_ids
if orphans:
    print(f'ORPHANS: {len(orphans)} HTML anchors absent from manifest:', file=sys.stderr)
    for o in sorted(orphans):
        print(f'  {o}', file=sys.stderr)
    sys.exit(1)

print(f'OK: {len(manifest_ids)} manifest entries all resolve; no orphans.')
```

Wire into the `Makefile` `html:` target so build fails on nonzero exit. Existing `Makefile:63` is `html: gitinfo build/reader-inline.html` — append `python3 build/verify-deep-links.py` at the end of that recipe.

**Commit:** `Plan 0209 phase 4: build-time deep-link verifier — fails build on missing or orphan anchors`

---

### Phase 5 — First build & smoke

```bash
cd ~/software/relinquishment
make html
python3 build/verify-deep-links.py     # expect "OK: 49 manifest entries all resolve; no orphans."
```

#### Post-build greps

```bash
grep -oE 'id="custodian:[^"]+"' docs/downloads/Relinquishment.html        # expect empty
grep -oE 'id="custodian:[^"]+"' docs/downloads/Relinquishment.html | sort -u  # expect 7 distinct
grep -oE 'class="[^"]*custodian[^"]*"' docs/downloads/Relinquishment.html  # expect empty
grep -c 'appendix:custodian' manuscript/appendix/abstracts.tex             # expect 0
grep -c 'appendix:custodian' manuscript/appendix/abstracts.tex            # expect 1

# Residual "custodian" — comment-only mentions OK
grep -rn 'custodian' build/ 2>/dev/null | grep -v __pycache__ | grep -v epub-tmp
# Inspect manually: identifier/class/URL mentions should be zero
```

#### Smoke test (desktop)

1. Open `docs/downloads/Relinquishment.html` in a browser.
2. Hover a Custodian menu item → status-bar URL preview reads `…#custodian:<slug>`.
3. Click → page scrolls to correct interlude; ancestor `<details>` auto-expanded.
4. Click the Custodian-only filter button → hides everything except the 7 interludes.
5. Right-click Custodian menu item → Copy link → URL contains `#custodian:`, not `#custodian:`.
6. Open any `#dl:X` anchor URL (pick `#dl:invisible-ocean`) → scrolls to the paragraph.

If any step fails, investigate before proceeding to Phase 6.

**Commit:** `Plan 0209 phase 5: first build with consolidated manifest + custodian rename — verifier passes`

---

### Phase 6 — Questions-index section

Add a collapsible "Questions about this book" section. Generated by preprocess.py from the manifest. Placed at the start of the Appendices (or as the last element before Appendices — Generator picks the insertion point consistent with existing `<details class="chapter-section">` placement).

#### preprocess.py addition (sketch)

```python
def generate_questions_index(manifest_entries):
    """Render manifest as a collapsible FAQ.
    Skip interludes (separate navigation system); include dl:* entries only."""
    by_category = {}
    for e in manifest_entries:
        if not e['id'].startswith('dl:'):
            continue
        by_category.setdefault(e['category'], []).append(e)

    html = ['<details class="chapter-section" id="questions-index">']
    html.append('  <summary>Questions about this book</summary>')
    html.append('  <p><em>Each question links into the passage that answers it.</em></p>')
    for cat in ['skeptic', 'science', 'verification', 'ethics', 'curiosity', 'narrative']:
        if cat not in by_category:
            continue
        html.append(f'  <h3>{cat.title()}</h3>')
        html.append('  <ul>')
        for e in by_category[cat]:
            html.append(f'    <li><a href="#{e["id"]}">{e["question"]}</a></li>')
        html.append('  </ul>')
    html.append('</details>')
    return '\n'.join(html)
```

Insert the generated HTML immediately before the Appendix track's first `<details>`. Generator locates the insertion point by grep for the Appendix anchor.

#### Verify

```bash
grep -c 'id="questions-index"' docs/downloads/Relinquishment.html         # expect 1
grep -cE 'href="#dl:[a-z0-9-]+"' docs/downloads/Relinquishment.html       # expect ≥ 42 (each dl entry listed once; .tex \deeplink{} doesn't emit href= so this counts only the index)

# HTML balance check (word-boundary regex, NOT substring count — see
# memory/feedback-plan-grep-verification.md)
python3 <<'PY'
import re
html = open('docs/downloads/Relinquishment.html').read()
m = re.search(r'<details class="chapter-section" id="questions-index">.*?</details>',
              html, re.DOTALL)
assert m, 'questions-index block not found'
block = m.group(0)
for tag in ['details', 'summary', 'ul', 'li', 'h3', 'p']:
    opens  = len(re.findall(rf'<{tag}\b', block))
    closes = len(re.findall(rf'</{tag}\b', block))
    assert opens == closes, f'{tag}: {opens} open, {closes} close'
print('questions-index HTML balance: PASS')
PY
```

#### Smoke

1. Open HTML; expand "Questions about this book" section.
2. Click a question under Skeptic → scrolls to that paragraph.
3. Browser back → returns to questions list.

**Commit:** `Plan 0209 phase 6: reader-facing questions-index section generated from manifest`

---

### Phase 7 — Final build & full smoke test

```bash
cd ~/software/relinquishment
make html
python3 build/verify-deep-links.py          # expect OK
```

Full smoke (desktop + phone):

**Desktop:**
1. All Phase 5 smoke steps still pass.
2. Questions-index section expands; each question link works.
3. Custodian-only filter works; all 7 interlude scroll targets correct.

**Phone (Bruce's reading device):**
4. Open live site; navigate via menu; hover reveals rich panels as before.
5. Questions-index section fits phone width; links tappable.

**Commit:** `Plan 0209 phase 7: final build — 49 manifest entries verified; questions index integrated`

---

### Phase 8 — Tag

```bash
git tag -a plan-0209-complete -m "Plan 0209 complete: manifest-driven deep links, Custodian rename, verifier, questions-index"
git push origin plan-0209-complete
```

Ship. Plan 0210 (per-anchor share pages) builds on this state.

---

## Acceptance

1. **Manifest.** `build/deep-links.yaml` has 49 entries; all IDs prefixed (42 `dl:*`, 7 `custodian:*`); `interlude` category exists with 7 entries in narrative order.
2. **Verifier.** `python3 build/verify-deep-links.py` prints `OK: 49 manifest entries all resolve; no orphans.` after each build.
3. **No old-name leak.** Zero `custodian:*` URL fragments or `.custodian-*` classes in `docs/downloads/Relinquishment.html`.
4. **Build-fail test.** Temporarily delete one manifest line → `make html` fails with nonzero exit and `MISSING:` message. Restore; passes again. Temporarily add an orphan `id="dl:fake"` in preprocess.py → build fails with `ORPHANS:`. Restore.
5. **Questions-index.** `id="questions-index"` exists once; all 42 `dl:*` entries listed; HTML balanced.
6. **Phone smoke.** All steps pass on Bruce's phone (live site).

---

## Risks

- **URL breakage for pre-rename external shares.** Anyone who shared `#custodian:home` gets a dead link post-rename (wrong namespace + wrong slug). Bruce flagged this is the intent — old URLs leaked the old name; breaking them is the fix. No back-compat shim proposed.
- **Normalization false alarms.** Phase 1a's `sed` matches `^- id: <bare>$`. If any existing entry has trailing whitespace, the regex misses it. Phase 1c's grep (`^- id: [^d]`) catches that: expected 0, real count shows survivors. Generator: if Phase 1c fails, inspect and hand-edit survivors before proceeding.
- **Phase 2 refactor breaks build silently.** preprocess.py line numbers here (~1646) may have drifted. Mitigation: Phase 2's sanity check (`python3 -c "from preprocess import INTERLUDE_IDS; print(...)"`) fails loudly before build if the refactor is incomplete.
- **Slug/label divergence.** menu-tooltips.yaml keys + any preprocess.py string literal that renders the menu's *visible* label (e.g. hardcoded "Your Locks" text rather than the YAML lookup) must change in concert. Phase 3 Generator should grep preprocess.py for menu-title literals during edits and escalate if found. If the label is hardcoded "Your Locks" but the slug becomes `locksmith`, URL fragment and visible text disagree.
- **Makefile recipe ordering.** Phase 4 appends one line to the `html:` recipe. Generator must verify the recipe still functions after the append (no broken tab indentation, no stale dependencies).

---

## Annealing log

### Pass 1 — medium (structural)

- **Merged 0209 + 0210 + 0211 per Bruce's directive.** Decided on phase structure: manifest, refactor, rename, verifier, first build, questions-index, final build, tag.
- **Dropped the original 0213 "placement audit" phase as redundant** — the verifier (Phase 4) already catches manifest-entry-without-anchor (`MISSING`) and anchor-without-manifest-entry (`ORPHANS`). Nothing additional for an audit to discover at build time.
- **Resolved Bruce's 3 DDs and structured the plan around them:** DD1/DD2 marked resolved; DD3 (slugs) surfaced as explicit Bruce-sign-off gate with recommendations + alternatives; DD4 (questions-index location) recommended Option (a) inline; DD5 (share metadata) included with flip-switch.
- **Slug recommendations**: `your-locks → keys` was the only non-obvious call; flagged with alternatives (`codes`, `capability`). Others tracked Bruce's `#custodian:flat` + `#custodian:hello` examples directly. Later updated to `locksmith` after Bruce narrowed the shortlist.

### Pass 2 — low (details)

- **Verified `\deeplink{X}` macro definition** (`build/preamble.tex:255`) prepends `dl:`. Phase 1a normalization is therefore safe and cosmetic (manifest changes only; no downstream code change needed because nothing currently reads the manifest as input — the macro is the single source of the `dl:` prefix at HTML render time).
- **Checked Makefile targets.** `html`, `clean`, `clean-cache` exist; `clean-html` **does not** — original 0209v1's proposed `make clean-html && make html` would have hallucinated a target. Plan now uses bare `make html` (the pipeline regenerates from source anyway).
- **Fixed grep metacharacters.** All Phase 0 greps use POSIX `-E` explicitly and escape `[` / `{` per ripgrep conventions.
- **Added HTML balance check for questions-index** using word-boundary regex (`<tag\b`) per `feedback-plan-grep-verification.md`, not substring count.
- **Explicit Phase 1c verification** catches Phase 1a sed-miss (trailing-whitespace survivors) before Phase 2 runs against a half-normalized manifest.
- **Phase 2 sanity check** runs Python import against the refactored module before touching the build, so a broken refactor fails loudly in seconds, not minutes.
- **Phase 3 "longest-match-first" ordering** is explicit and covers the `interlude-custodian:` / `menu-custodian:` prefix overlap case (both contain `custodian-` as a substring but must not collide).

### Pass 3 — low (polish)

- **Risk section rewritten** to be read-first before Generator hand-off: five concrete failure modes, each with "what happens if triggered" and "how the plan catches it."
- **Commit messages** standardized per `CLAUDE.md` convention (`Plan 0209 phase N: description`). Each commit scoped to one phase; no cross-phase commits.
- **Phase ordering sanity-check.** 1 must precede 2 (manifest read depends on manifest); 2 must precede 3 (refactor depends on renamed IDs being present in manifest); 3 can run parallel with 4 in principle but sequentialized here for reviewer legibility; 5 must follow 4 (verifier in-Makefile or first build reveals a bug); 6 must follow 5 (insertion point HTML locations verified); 7 is final build.
- **Out-of-scope section** captures reader.js UX (now in 0210), Option-B normalization, and interlude-menu display-text rename — each with a one-line "why deferred."
- **Acceptance criterion #4 (build-fail test)** is the real teeth: it verifies the verifier, not just that it ran. Without this, Phase 4 is cosmetic.
- **Flagged slug/label divergence risk** explicitly: if a menu title is hardcoded "Your Locks" in preprocess.py and we rename the slug to `locksmith`, the URL fragment (`#custodian:locksmith`) and the visible menu label disagree. Generator must grep for menu-title literals during Phase 3 and escalate if found.

### Pass 4 — extraction (Bruce, 2026-04-16)

- **Extracted Phase 7 (per-anchor share pages with OG metadata) to Plan 0210** at Bruce's direction: "*important for marketing but needs to be distinct plan.*" The original Phase 7 had the largest new public surface area (49 share pages, new URL form `/share/<slug>`, reader.js UX coupling) — distinct enough in scope to warrant separate review, distinct enough in deployment to warrant separate ship.
- **Updated DD3** with Bruce's narrowed cryptanalysis-slug shortlist (`keys` vs `locksmith`). Recommendation switched from `keys` to `locksmith`: profession framing wins over possessive framing in the bare-URL test ("she is the kind of being who can make locks" vs "she holds your keys"). DD3 marked RESOLVED.
- **Renumbered Phase 8 → 7, Phase 9 → 8.** Removed share-page risks (OG cache lag, double-count analytics, Makefile dual-append). Acceptance criteria reduced from 7 to 6 (share pages criterion gone).
- **Plan size halved** from ~600 lines to ~400. Tighter, single-narrative.
- **0210 is downstream:** depends on this plan having shipped (manifest normalized, verifier in place). 0210 will Pre-flight-verify Plan 0209 acceptance criteria before doing anything.

### Pass 5 — medium + low anneal (structural bugs + detail)

- **BUG FIXED: Phase 1c grep `'^- id: [^d]'` was broken.** Ran after Phase 1b appends 7 `custodian:*` entries — would match them (they start with `c`, not `d`), returning 7 instead of expected 0. Fix: split verification — run the normalization check (`[^d]`) after Phase 1a but BEFORE 1b, then run the final-state check after 1b with `[^dc]` (excludes both `dl:` and `custodian:` prefixes).
- **BUG FIXED: Phase 6 href grep `[a-z-]+` excluded digits.** Changed to `[a-z0-9-]+`. No current IDs use digits, but the pattern should not silently break on future entries.
- **Added: Phase 3 menu-tooltips VALUE check.** The old keys held `"custodian:X"` — but tooltip *value* text may also mention "Custodian." Added note for Generator to check and rename in values too.
- **DD3 → RESOLVED.** Bruce moved to "post generator prompt" after narrowing to keys/locksmith and receiving locksmith recommendation. Default-if-silent protocol applies.
- **Status line → "COMPLETE (verified S63 audit). Originally: Ready for Generator."** Removed slug-confirmation gate.
