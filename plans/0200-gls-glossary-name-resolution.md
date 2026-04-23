# Plan 0200 — Fix systemic `\gls{}` rendering bug in HTML

**Auditor:** Argus
**Date:** 2026-04-15
**Type:** Single-commit bug fix plan. Small surgical change in `build/preprocess.py`.

---

## 1. Problem

Every `\gls{KEY}` in the manuscript renders in the built HTML as the lowercase key instead of the glossary's `name={DisplayName}`. Current broken output:

```html
<span data-acronym-label="gchq" data-acronym-form="singular+short">gchq</span>
```

…when it should be `GCHQ`. Confirmed across the full glossary:

| Key | Renders now | Should render |
|---|---|---|
| gchq | gchq | GCHQ |
| darpa | darpa | DARPA |
| cows | cows | COWS |
| tqnn | tqnn | TQNN |
| udhr | udhr | UDHR |
| iccpr | iccpr | ICCPR |
| icty | icty | ICTY |
| custodian | custodian | Custodian |
| fqh, sfi, cdc, 2deg, qec, pkc, halo, nda, sas | (all lowercase) | (proper casing from glossary) |
| theflat | theflat | the Flat |
| aurasys | aurasys | Aurasys |
| hacktivismo | hacktivismo | Hacktivismo |

Root cause: pandoc converts `\gls{KEY}` to a `<span data-acronym-label="KEY" data-acronym-form="...">KEY</span>` but doesn't resolve the `name={...}` field from `\newglossaryentry{}` definitions. The glossary file is correct (`manuscript/appendix/glossary-entries.tex`). The build pipeline has no existing `\gls` handler.

PDF output renders correctly via LaTeX's `glossaries` package; HTML rendering is the only affected surface.

---

## 2. Fix: extend `preprocess.py --fix-html` with a glossary-name resolution pass

### Deliverable

A new function `fix_html_glossary_names(html_path)` in `build/preprocess.py`, called from the `--fix-html` entry point alongside `fix_html_toc`. It:

1. Parses `manuscript/appendix/glossary-entries.tex` once, extracting `{key: name}` via regex on `\newglossaryentry{KEY}{name={NAME}, ...}`. Keys are normalized to lowercase in the lookup map (pandoc emits `data-acronym-label` in lowercase regardless of source casing).
2. Walks the HTML, finds every `<span data-acronym-label="KEY" data-acronym-form="FORM">TEXT</span>`, and replaces `TEXT` with the resolved display name. If a key has no glossary entry, leave TEXT unchanged and emit a `WARNING: unresolved \gls key: KEY` to stderr (don't fail the build).

### Form-handling rules

| `data-acronym-form` value | Output |
|---|---|
| `singular+short` | `name` verbatim |
| `plural+short` | `name` + `s` (simple suffix; no glossary entry currently needs an irregular plural — if one is added later, add a `plural=...` field to the glossary entry and extend the parser) |
| `singular+long` / `plural+long` | (not currently used in manuscript — if encountered, leave TEXT unchanged and emit a `WARNING` to stderr so future maintainers see it) |

### Idempotency

Running `fix_html_glossary_names` twice should be a no-op: if the span's inner text already matches the resolved name, leave it. This keeps the pass safe to rerun during build iterations.

### Parser regex (reference)

```python
GLOSSARY_ENTRY_RE = re.compile(
    r'\\newglossaryentry\{(?P<key>[^}]+)\}\s*\{\s*name=\{(?P<name>[^}]+)\}',
    re.DOTALL,
)
ACRONYM_SPAN_RE = re.compile(
    r'<span data-acronym-label="(?P<key>[^"]+)" data-acronym-form="(?P<form>[^"]+)">(?P<text>[^<]*)</span>'
)
```

### Wiring

At `build/preprocess.py:2052`, the existing `--fix-html` dispatch calls `fix_html_toc(sys.argv[2])`. Add a second call immediately after:

```python
elif len(sys.argv) > 1 and sys.argv[1] == '--fix-html':
    fix_html_toc(sys.argv[2])
    fix_html_glossary_names(sys.argv[2])
```

Order matters: TOC fix first (which may itself contain acronym spans in chapter titles), glossary-name fix second, so the rewrite sees the final HTML structure.

---

## 3. Acceptance criteria

1. After `make dev`:
   - `grep -c 'data-acronym-label="gchq" data-acronym-form="singular+short">GCHQ</span>' Relinquishment.html` returns ≥ 1.
   - `grep -cE 'data-acronym-label="[a-z0-9]+" data-acronym-form="[^"]+">[a-z]' Relinquishment.html` returns the count of acronym spans whose `name=` is *deliberately* lowercase: `anyon`, `autocatalytic set`, `edge of chaos`, `morphogenesis`, `soliton`, `phonon`, `topological order`, `dual-use`, and `theflat` (name=`the Flat` — starts with lowercase `t`). Any number higher than the sum of occurrences for those keys indicates an unresolved span.
2. Spot-check four specific rewrites in the built HTML:
   - `<span data-acronym-label="gchq" ...>GCHQ</span>` appears
   - `<span data-acronym-label="darpa" ...>DARPA</span>` appears
   - `<span data-acronym-label="theflat" ...>the Flat</span>` appears
   - `<span data-acronym-label="custodian" ...>Custodian</span>` appears
3. Plural handling: `<span data-acronym-label="anyon" data-acronym-form="plural+short">anyons</span>` is preserved (name={anyon} + "s" = "anyons", matches existing output). Spot-check in the built HTML.
4. `make dev` clean — no new warnings, no regressions.
5. PDF output unchanged (LaTeX handles glossaries natively; this plan only touches HTML).
6. Idempotency: running `python3 build/preprocess.py --fix-html Relinquishment.html` twice in a row produces byte-identical output the second time.
7. Single commit. Message: `Plan 0200: resolve \gls{} to glossary name= in HTML output`.

---

## 4. Non-goals

- No change to `glossary-entries.tex` content.
- No change to LaTeX/PDF output.
- No refactor of `fix_html_toc`.
- No change to the `<span data-acronym-label=...>` structure itself (just its inner text).
- No handling of `\acrlong` / long-form expansion (not currently used in manuscript; flagged for future if needed).

---

## 5. Rollback

Single commit. `git revert <sha>` restores the pre-fix rendering. The bug returns but nothing else breaks.

---

## 6. First Generator handoff (held until Bruce approves)

> You are the Generator. Before doing any work, read `~/software/relinquishment/manuscript/track-3-awakening/firmware-update.tex` in full (standard priming, even though this plan doesn't touch book-science). Then execute Plan 0200 (`~/software/relinquishment/plans/0200-gls-glossary-name-resolution.md`). Add the new `fix_html_glossary_names` function to `build/preprocess.py` per §2, wire it into the `--fix-html` dispatch at L2052, and verify all §3 acceptance criteria. Do not touch `manuscript/appendix/glossary-entries.tex` or any `.tex` source. Commit with the message in §3 item 7. Report back: build status, four spot-check results, plural-handling result, idempotency-check result, commit SHA.
