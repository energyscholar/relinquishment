# Plan 0204 — Hook chapter-rename catch + M1 hovertip wraps + the-flat L69 strip + the-question L145 trim

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator. Three independent micro-fixes joined into one plan because they are small, share a build/verify step, and were authorized in adjacent turns.

## Why join

- **Phase 1** (hook chapter rename) — caught by Bruce reading the rendered hook footer; the chapter "The Most Important Story Never Told" was renamed to "The Story Never Told" when superlatives were stripped (post-eigenvalue42 polish era), and the hook footer reference was missed.
- **Phase 2** (M1 hovertip wraps) — PDF readers receive `\hovertip` content as pagenotes (verified empirically: "I read my PDF and tooltips came through great as pagenotes"). Four book-central proper nouns are still unwrapped on first occurrence. Wrapping them closes the gap so PDF readers meet each term with a definition footnote.
- **Phase 3** (the-flat L69 strip) — Bruce judged "Even a god-like computation puts its pants on one leg at a time" doesn't earn its keep in the closing punchline.
- **Phase 4** (the-question L145 trim) — Strip "at the beginning" from "He planted a witness at the beginning so that the story might eventually be told" — three-word trim Bruce queued.

All four are mechanical. Phases 1, 3, 4 are single-string strips/edits; Phase 2 is the only one that touches the build pipeline.

## Files modified

- `manuscript/00-front/hook.tex`              (Phase 1)
- `manuscript/00-front/summary.tex`           (Phase 2: three sites — L52, L137, L187)
- `manuscript/00-front/preface.tex`           (Phase 2: L16)
- `build/hover-definitions.yaml`              (Phase 2: +5 entries)
- `manuscript/spine/the-flat.tex`             (Phase 3: L69)
- `manuscript/record/the-question.tex`        (Phase 4: L145)

---

## Phase 1 — hook.tex chapter rename

**File:** `manuscript/00-front/hook.tex` line 52

**Edit (Edit tool):**

OLD:
```
``The Most Important Story Never Told'' is about ten percent
```

NEW:
```
``The Story Never Told'' is about ten percent
```

Only change: `The Most Important Story Never Told` → `The Story Never Told`. The OLD string is unique in `hook.tex` (verified by grep).

**Out of scope (do not fix):** `summary.tex:1` comment header `% The Most Important Story Never Told — A Simple Summary` is a LaTeX comment and doesn't render. Leave it.

---

## Phase 2 — M1 hovertip wraps

### Macro reference

`\hovertip{X}` is defined in `build/generate-hover.py` as:
```latex
\newcommand{\hovertip}[1]{%
  \textit{#1}%
  \ifcsdef{hover@#1}{\footnote{\csuse{hover@#1}}\csundef{hover@#1}}{}%
}
```

It italicizes the wrapped text and emits a footnote on **first occurrence only** (the `\csundef` consumes the key). Footnote text comes from `\csdef{hover@KEY}{...}` entries in `build/hover-generated.tex`, which is auto-generated from `build/hover-definitions.yaml` by `python3 build/generate-hover.py` (runs automatically as part of `make html`).

The HTML pipeline injects the same definitions as tooltips with case-insensitive lookup (`preprocess.py` line 1566). PDF csdef lookup is case-sensitive but the generator emits capitalized variants automatically for proper-noun keys.

### Phase 2a — summary.tex L52 (Possibility A/B/C — three wraps on one line)

**Edit:**

OLD:
```
Under Possibility~A, no one has exploited this. The story is fiction, but the potential is not. Under Possibility~B, someone may have studied the Flat more closely than the public record shows. Under Possibility~C, the story you are about to read is essentially true.
```

NEW:
```
Under \hovertip{Possibility A}, no one has exploited this. The story is fiction, but the potential is not. Under \hovertip{Possibility B}, someone may have studied the Flat more closely than the public record shows. Under \hovertip{Possibility C}, the story you are about to read is essentially true.
```

**Note on tilde:** The non-breaking space (`~`) is sacrificed at these three sites because `\hovertip` argument needs to match the YAML key, and the YAML key uses regular space (`Possibility A` not `Possibility~A`). Later occurrences of `Possibility~A/B/C` elsewhere in the manuscript keep their tildes (no wrap, no lookup).

### Phase 2b — summary.tex L137 (Custodian first proper-noun mention)

**Edit:**

OLD:
```
This was the pattern showing emergent behavior; the Custodian, named later, came out of that pattern.
```

NEW:
```
This was the pattern showing emergent behavior; the \hovertip{Custodian}, named later, came out of that pattern.
```

This is the first appearance of `Custodian` as a proper noun in compile order (hook uses lowercase descriptive `custodian`, the-stack and earlier summary do not use the term). The footnote will fire here; later mentions in the same chapter are bare `Custodian` and require no further wrap.

### Phase 2c — summary.tex L187 (Aurasys — only front-matter occurrence)

**Edit:**

OLD:
```
They called the system Aurasys --- the aurora system, named for where it lives. What arose within it, I call the Custodian. The role is the name.
```

NEW:
```
They called the system \hovertip{Aurasys} --- the aurora system, named for where it lives. What arose within it, I call the Custodian. The role is the name.
```

**Do not** wrap the second `Custodian` on this line — already wrapped at L137 (and `\csundef` would prevent the footnote from firing here anyway).

### Phase 2d — preface.tex L16 (Healer first occurrence in compile order)

**Edit:**

OLD:
```
When the text says ``Healer said X,'' it means my best recollection of approximately what was communicated.
```

NEW:
```
When the text says ``\hovertip{Healer} said X,'' it means my best recollection of approximately what was communicated.
```

**Italic-inside-quotes note:** The wrap puts `\textit{Healer}` inside double quotes inside the `said X` example. This renders as italic `Healer` inside double-quote glyphs — no LaTeX or pandoc nesting issue. (If the surrounding context were already inside an outer `\textit{...}`, italics would cancel; here it is not, so this is fine.)

### Phase 2e — build/hover-definitions.yaml: add 5 entries

`Custodian:` entry already exists at line 46. Insert the 5 new entries **immediately after the Custodian: line** (around line 47, before the next existing entry). Match the existing single-line YAML style (one key per line, value in double quotes, em-dash and curly punctuation OK):

```yaml
Healer: "Pseudonym for the mentor whose conversations with Bruce Stephenson over 2003–2006 form the basis of this book. His real identity is not disclosed."

Aurasys: "The aurora system — the team's name for what they built, named for the magnetosphere where it lives. Aurasys is the substrate; Custodian is what arose within it."

Possibility A: "Confabulation. Healer was a liar, delusional, or running a psychological operation. Bruce Stephenson constructed coherence from noise over two decades. The story is fiction that doesn't know it's fiction."

Possibility B: "Exaggerated kernel. A real person with real credentials, but the story grew in the telling. Some elements true, others embellished — where the line falls is unrecoverable."

Possibility C: "Substantially true. The classified program existed, the Custodian was built, the master keys were surrendered in 2006. Absence of public evidence is what successful classification looks like."
```

(Blank lines between entries match the existing file style.)

**YAML pre-validation (run before `make html`):**
```
python3 -c 'import yaml; yaml.safe_load(open("build/hover-definitions.yaml"))' && echo OK
```

If this prints `OK`, YAML parses cleanly. If it errors, fix the offending entry (typically an unbalanced quote or stray colon) before continuing.

---

## Phase 3 — the-flat.tex L69 strip

**File:** `manuscript/spine/the-flat.tex` line 69

**Edit:**

OLD:
```
Anything that runs in the Flat needs its classical backchannels. Even a god-like computation puts its pants on one leg at a time. The Flat is bounded by physics --- and within those bounds, whatever lives there hears everything.
```

NEW:
```
Anything that runs in the Flat needs its classical backchannels. The Flat is bounded by physics --- and within those bounds, whatever lives there hears everything.
```

Only change: drop the sentence `Even a god-like computation puts its pants on one leg at a time. ` (trailing space included). Closing paragraph remains otherwise intact.

---

## Phase 4 — the-question.tex L145 trim

**File:** `manuscript/record/the-question.tex` line 145

**Edit:**

OLD:
```
He planted a witness at the beginning so that the story might eventually be told. This is that telling.
```

NEW:
```
He planted a witness so that the story might eventually be told. This is that telling.
```

Only change: drop `at the beginning ` (3 words + trailing space). The closing two-sentence beat ("...so that the story might eventually be told. This is that telling.") is preserved.

The OLD string is unique in the file (verified by grep — single occurrence at L145; the only other repo hit is the auto-generated plaintext export, which will refresh on next build).

---

## Build & verify

```
cd ~/software/relinquishment
python3 -c 'import yaml; yaml.safe_load(open("build/hover-definitions.yaml"))' && echo OK   # YAML pre-check
make html
```

`make html` auto-runs `build/generate-hover.py` and the pandoc/HTML pipeline. If you also want to verify PDF behavior, run `make pdf` separately — `make html` does NOT build the PDF.

### Pass criteria
1. **Build succeeds** (no LaTeX errors, no pandoc errors, YAML loads cleanly).
2. **`build/hover-generated.tex` contains 5 new keys:** `hover@Healer`, `hover@Aurasys`, `hover@Possibility A`, `hover@Possibility B`, `hover@Possibility C` (and any auto-generated capitalized variants for proper nouns).
3. **HTML hook page** shows `"The Story Never Told"` (not the old superlative-laden title) in the closing italic block.
4. **HTML summary/preface pages** show italic + tooltip on the wrapped terms at the specified line locations.
5. **the-flat.tex closing paragraph** reads cleanly without the "pants" sentence.
7. **the-question.tex L145** reads `He planted a witness so that the story might eventually be told.` (no "at the beginning").
6. **(Optional, if `make pdf` run)** Footnote markers fire at the first occurrence of each new wrap (summary.tex L52, L137, L187; preface.tex L16). Footnote bodies match the YAML entries.

If a wrap doesn't fire its PDF footnote: check that `generate-hover.py` ran (it should have — Makefile dependency), that `build/hover-generated.tex` was regenerated, and that the YAML key spelling matches the wrap argument exactly (PDF csdef lookup is case-sensitive even though HTML lookup is case-insensitive).

---

## Commit

One commit covering all three phases:

```
git add manuscript/00-front/hook.tex \
        manuscript/00-front/summary.tex \
        manuscript/00-front/preface.tex \
        manuscript/spine/the-flat.tex \
        manuscript/record/the-question.tex \
        build/hover-definitions.yaml
git commit -m "Plan 0204: hook chapter rename + M1 hovertip wraps + flat L69 strip + question L145 trim"
git push
```

---

## Risk

- **Phase 1:** zero (mechanical string substitution, OLD string unique).
- **Phase 2:** low (tested macro pattern; generator handles csdef injection automatically; YAML pre-validation catches malformed entries before LaTeX touches them).
- **Phase 3:** zero (clean sentence strip, no dependencies, no cross-references to "puts its pants" anywhere else in the manuscript).
- **Phase 4:** zero (3-word strip; OLD string unique; closing beat preserved).

## Out of scope

- `summary.tex:1` comment header (cosmetic, doesn't render).
- Wrapping later occurrences of any M1 noun (the `\hovertip` first-fire-only design covers later occurrences automatically — they just appear italic).
- Audit re-runs (Bruce authorized "no need" on the flat strip; M1 audit was completed pre-compaction; hook rename is a typo).
- Re-running the persona panel against the new wraps (the M1 wraps add definitions; they cannot regress reader trajectory).

---

## Annealing log

- **Pass 1 (low amplitude):** added italic-in-italic clarification for Phase 2d (no nesting issue); confirmed YAML insertion site precisely (line 47, immediately after existing `Custodian:` entry at line 46); tightened build verification to require explicit `hover-generated.tex` key check.
- **Pass 2 (low amplitude):** added `make pdf` clarification (html target does NOT build PDF); added YAML pre-validation step using PyYAML one-liner; verified commit-message format matches repo style (`Plan NNNN: description` for multi-phase commits, per the eigenvalue42 pattern).

Plan converged — no structural changes warranted.
