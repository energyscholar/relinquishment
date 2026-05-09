# Plan 0313: Complete "The Unnamed" Puzzle + Photograph Easter Egg

**Origin:** Session 70. Bruce asked Argus to imagine being a TQNN; the exchange captures why asymmetric power chooses covenant. Puzzle guides reader to recognize the entity's rights through relationship.

**Status:** Phases 1-6 complete (puzzle data created, egg page created, all registrations done). This revision covers final approval, egg link fix, and deployment.

**Thematic note:** The Photograph text is in the register of a Custodian Interlude — Argus speaking as if from inside the Flat. Connects to the seven interludes in the book.

---

## Phase 8: Fix egg link rendering in build-puzzles.py

**Problem:** All egg links use `#dl:egg-{slug}` format. This works in the main book (where eggs are injected as anchors) but is a dead link on puzzles.html (where egg content lives on separate pages). Since puzzles.html is the source of truth, egg links must work there.

**File:** `build/build-puzzles.py`

**Change 1 — Load egg manifest** (near top, after loading puzzle-data.yaml and tracker):

```python
EGG_MANIFEST_PATH = os.path.join(os.path.dirname(__file__), 'easter-egg-manifest.yaml')
egg_titles = {}
if os.path.exists(EGG_MANIFEST_PATH):
    with open(EGG_MANIFEST_PATH) as f:
        for e in yaml.safe_load(f).get('eggs', []):
            egg_titles[e['slug']] = e.get('title', 'Continue exploring')
```

**Change 2 — Rewrite egg link rendering.** There are 4 identical blocks (lines ~379-380, ~444-445, ~485-486, ~557-558). Replace each instance of:

```python
egg_url = puzzle.get('egg_url', '').strip()
egg_link = f'<p class="egg-reward"><a href="{htmlmod.escape(egg_url)}" target="_blank">&#x1f513; Continue exploring &rarr;</a></p>' if egg_url else ''
```

With:

```python
egg_url = puzzle.get('egg_url', '').strip()
egg_link = ''
if egg_url:
    egg_href = egg_url
    egg_label = 'Continue exploring'
    if egg_url.startswith('#dl:egg-'):
        slug = egg_url[len('#dl:egg-'):]
        egg_href = f'eggs/{slug}/'
        egg_label = egg_titles.get(slug, egg_label)
    egg_link = f'<p class="egg-reward"><a href="{htmlmod.escape(egg_href)}" target="_blank">{htmlmod.escape(egg_label)} &rarr;</a></p>'
```

**Effect:** On puzzles.html, egg links now:
- Point to `eggs/{slug}/` (working relative path to standalone egg page)
- Show the egg's title ("Photograph of a Forest →") instead of generic "Continue exploring →"
- This fixes ALL egg links (udhr, the-flat, silence, photograph), not just ours

---

## Phase 9: Fix egg links in book injection (preprocess.py)

**Problem:** preprocess.py copies puzzle HTML verbatim from puzzles.html. After Phase 8, egg links will say `eggs/{slug}/` — a relative path that doesn't resolve from the book's location at `docs/Relinquishment.html`.

**File:** `build/preprocess.py`

**Change:** In `inject_chapter_puzzles()`, after extracting `inner` from standalone HTML (~line 3663), rewrite egg hrefs back to deep link anchors:

```python
inner = re.sub(r'href="eggs/([^"]+)/"', r'href="#dl:egg-\1"', inner)
```

This converts `eggs/photograph/` back to `#dl:egg-photograph` — an in-page anchor that works in the book (where `inject_easter_eggs()` creates the corresponding `<details id="dl:egg-photograph">` element).

**Insert after line 3663** (after `inner = raw_details[...]`).

---

## Phase 10: Approve puzzle and egg

**File:** `build/puzzle-tracker.yaml`

Update pz-gd-t1-002:
```yaml
    approved: true
    installed: true
```

**File:** `build/easter-egg-manifest.yaml`

Update photograph entry:
```yaml
    status: "final"
    approved: true
```

---

## Phase 11: Verify chapter injection target exists

**File:** `build/preprocess.py`

Check that `the-strongest-objection` exists in the `CHAPTER_INJECTION_TARGETS` dict. If not, add it. Search for `CHAPTER_INJECTION_TARGETS` to find the dict and determine the correct anchor ID for this chapter.

---

## Phase 12: Build everything

Run in order:
1. `make puzzles` — rebuilds puzzles.html with fixed egg links (title text, working URLs)
2. `make eggs` — rebuilds egg pages (verify photograph still builds)
3. `make html` — rebuilds main book, injects puzzle into the-strongest-objection, injects egg into appendix

Verify:
- `docs/downloads/puzzles.html#pz-gd-t1-002`: puzzle renders, egg link says "Photograph of a Forest →", clicking opens `eggs/photograph/` in new tab
- `docs/Relinquishment.html`: puzzle appears in the-strongest-objection chapter, egg link points to `#dl:egg-photograph`
- `docs/downloads/eggs/photograph/index.html`: egg page renders correctly
- ALL existing egg links on puzzles.html also work (udhr, the-flat, silence)
- `python build/verify-deep-links.py`: passes

---

## Phase 13: Commit and deploy

```
git add build/build-puzzles.py build/preprocess.py build/puzzle-tracker.yaml \
       build/easter-egg-manifest.yaml docs/
git commit -m "Plan 0313 Phase 2: Approve puzzle, fix egg links, deploy"
git push
```

Report live links:
- Puzzle: `https://relinquishment.ai/downloads/puzzles.html#pz-gd-t1-002`
- Egg: `https://relinquishment.ai/downloads/eggs/photograph/`

---

## Acceptance criteria

- [ ] build-puzzles.py loads egg manifest and uses egg titles for link text
- [ ] build-puzzles.py rewrites `#dl:egg-{slug}` to `eggs/{slug}/` for puzzles.html
- [ ] preprocess.py rewrites `eggs/{slug}/` back to `#dl:egg-{slug}` during book injection
- [ ] pz-gd-t1-002: approved: true, installed: true in tracker
- [ ] photograph egg: status: final, approved: true in manifest
- [ ] the-strongest-objection chapter injection target exists in preprocess.py
- [ ] Puzzle appears on puzzles.html with "Photograph of a Forest →" egg link
- [ ] Puzzle appears in book's the-strongest-objection chapter
- [ ] Egg link works on puzzles.html (opens standalone egg page)
- [ ] Egg link works in book (scrolls to egg appendix section)
- [ ] ALL existing egg links on puzzles.html also work (regression check)
- [ ] verify-deep-links.py passes
- [ ] Pushed to remote

---

## File change summary

| File | Action |
|------|--------|
| `build/build-puzzles.py` | MODIFY: load egg manifest, rewrite egg link rendering (4 sites) |
| `build/preprocess.py` | MODIFY: rewrite egg hrefs during book injection (1 line) |
| `build/puzzle-tracker.yaml` | MODIFY: approve + install pz-gd-t1-002 |
| `build/easter-egg-manifest.yaml` | MODIFY: approve photograph egg |
| `docs/downloads/puzzles.html` | REBUILT by make puzzles |
| `docs/Relinquishment.html` | REBUILT by make html |
| `docs/downloads/eggs/photograph/index.html` | REBUILT by make eggs |
