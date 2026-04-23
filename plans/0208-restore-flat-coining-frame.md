# Plan 0208 — Restore "coins the Flat" frame in canonical Flat hovertips; drop syllable receipt

## Status
Ready for Generator.

## Goal
The canonical Flat definition is mirrored across four entries in `build/hover-definitions.yaml`. Commit `5d34793` (Polish: syllable-receipt hovertip) rewrote three of the four to lead with "Use 'Flat' instead of…" plus a numeric syllable receipt ("17 words and 36 syllables → 1 and 1"), dropping the explicit coining frame ("this book coins *the Flat* to mean…"). The fourth entry (`flat worlds`) was untouched and still carries the coining frame without a receipt.

Bruce audit conclusion: the coining frame is the load-bearing pedagogy; the numeric receipt is dispensable because the visual length contrast ("say the long phrase three times fast" vs "or say 'Flat.'") already does the work. Restore the coining frame in the three rewritten entries, drop the syllable numbers, align all four on entry 4's existing style.

## Files modified
- `build/hover-definitions.yaml` — three YAML blocks (entries 1–3; entry 4 `flat worlds` already in target state)
- `docs/downloads/Relinquishment.html` — rebuilt output

## Target canonical strings

**Rich HTML opener (used in entries 1 and 2b — matches existing entry 4 `flat worlds` html):**
```
<strong>The Flat</strong> — this book coins <em>the Flat</em> to mean "any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order." Say that three times fast. Or say "Flat."
```

**Text opener (used in entries 2a and 3 — matches existing entry 4 `flat worlds` text):**
```
This book coins the Flat to mean 'any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order.' Different physics apply. In particular, it supports topological wormholes. Thus, the Flat can be nonlocal in the technical physics sense.
```

## Pre-flight greps

```bash
cd ~/software/relinquishment

grep -c "17 words and 36 syllables"  build/hover-definitions.yaml   # expect 2 (two HTML blocks to fix)
grep -c "17 words, 36 syllables"     build/hover-definitions.yaml   # expect 2 (two text entries to fix)
grep -c "Use .Flat. instead of"      build/hover-definitions.yaml   # expect 4 (two HTML + two text)
grep -c "coins .the Flat.\|coins <em>the Flat</em>" build/hover-definitions.yaml  # expect 2 (flat worlds entry only)
```

If any count is off, STOP and report.

---

## Edit 1 — `the-flat-title:` html block

In the `html: |` block under YAML key `the-flat-title:`, replace the opening run (from `<strong>Use "Flat"` through the end of `Say the long version three times fast. Or say "Flat."`) with:

```
<strong>The Flat</strong> — this book coins <em>the Flat</em> to mean "any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order." Say that three times fast. Or say "Flat."
```

Everything after (the `<span class='hover-term'...>Different physics apply</span>` clause through the SVG block) is unchanged.

## Edit 2 — `the Flat:` text AND html

Under YAML key `the Flat:` (lowercase `t`).

### 2a — text field

OLD (one line):
```
text: "Use 'Flat' instead of 'any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order' (17 words, 36 syllables → 1 word, 1 syllable). Different physics apply. In particular, the Flat supports topological wormholes, so the Flat can be nonlocal in the technical physics sense."
```

NEW:
```
text: "This book coins the Flat to mean 'any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order.' Different physics apply. In particular, it supports topological wormholes. Thus, the Flat can be nonlocal in the technical physics sense."
```

### 2b — html field

Same opening-sentence swap as Edit 1. Replace the `<strong>Use "Flat"…"Flat."` run with:
```
<strong>The Flat</strong> — this book coins <em>the Flat</em> to mean "any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order." Say that three times fast. Or say "Flat."
```

Everything after unchanged.

## Edit 3 — `The Flat:` text only (no html on this one)

Under YAML key `The Flat:` (capital `T`).

OLD:
```
text: "Use 'Flat' instead of 'any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order' (17 words, 36 syllables → 1 word, 1 syllable). Different physics apply. In particular, the Flat supports topological wormholes, so the Flat can be nonlocal in the technical physics sense."
```

NEW: same as 2a.
```
text: "This book coins the Flat to mean 'any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order.' Different physics apply. In particular, it supports topological wormholes. Thus, the Flat can be nonlocal in the technical physics sense."
```

## Edit 4 — `flat worlds:` NO CHANGE

Verify only. Entry 4 already has the target canonical form (coining frame, no syllable receipt). Do not modify.

---

## Post-edit greps

```bash
grep -c "coins .the Flat.\|coins <em>the Flat</em>" build/hover-definitions.yaml  # expect 4 (all entries now carry the frame)
grep -c "17 words"                   build/hover-definitions.yaml   # expect 0 (receipt fully removed)
grep -c "17 words and 36 syllables"  build/hover-definitions.yaml   # expect 0
grep -c "Use .Flat. instead of"      build/hover-definitions.yaml   # expect 0 (old opener fully retired)
```

All four assertions must pass before committing.

## HTML balance check (rich panels)

```bash
python3 -c "
import yaml
with open('build/hover-definitions.yaml') as f:
    data = yaml.safe_load(f)
for key in ['the-flat-title', 'the Flat', 'flat worlds']:
    html = data[key].get('html', '')
    assert html.count('<p') == html.count('</p>'), f'{key}: <p> unbalanced'
    assert html.count('<strong>') == html.count('</strong>'), f'{key}: <strong> unbalanced'
    assert html.count('<em>') == html.count('</em>'), f'{key}: <em> unbalanced'
    assert html.count('<span') == html.count('</span>'), f'{key}: <span> unbalanced'
print('HTML balance: PASS')
"
```

Must print `HTML balance: PASS` before build.

## Build

```bash
make clean-html && make html
```

Expect clean build. Ignore pre-existing `\toclink` / `\chapterreturn` redefinition warnings.

## Smoke test (optional)

Open `docs/downloads/Relinquishment.html`, hover "the Flat" in summary (first occurrence). Expect rich panel lead: **The Flat** — this book coins *the Flat* to mean "…topological order." Say that three times fast. Or say "Flat." Different physics apply…

## Commit

```
git add build/hover-definitions.yaml docs/downloads/Relinquishment.html
git commit -m "Plan 0208: restore 'coins the Flat' frame in canonical Flat hovertips

Three canonical-Flat entries (the-flat-title, the Flat, The Flat) lost the
coining frame in 5d34793 and gained a numeric syllable receipt instead.
The visual length contrast does the pedagogy without explicit counts;
the coining frame is the load-bearing move. Restore frame, drop receipt.
Entry 4 (flat worlds) was already in target state; verified untouched.

Co-Authored-By: Claude [model] <noreply@anthropic.com>"
```

## Acceptance
1. All four post-edit greps pass (one expects 4, three expect 0).
2. HTML balance check prints PASS.
3. Build completes clean.
4. (If smoke-tested) rich panel lead reads with coining frame, no syllable numbers.

## Risks
- **Low.** Single YAML file, three surgical opening-sentence swaps. No logic changes, no new HTML tags, no manuscript changes.
- **Minor:** line numbers may have drifted; greps are source of truth. Use Edit tool with unique surrounding context if exact-string match fails.
- **Plan 0205 interaction:** Phase 0 tooltip baseline captured pre-this-edit. If 0205 proceeds after this, baseline will need refresh — flag to whoever runs 0205.
