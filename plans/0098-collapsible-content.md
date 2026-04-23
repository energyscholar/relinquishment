# Plan 0098: Collapsible Content Blocks (Show/Hide System)

**Status:** Ready for Generator
**PTL:** 098
**Depends on:** None (self-contained)

## Design Pattern: Progressive Enhancement with Layered Degradation

A single LaTeX markup (`\begin{collapsible}[state]{Label}`) produces toggleable content across all output formats. Each layer of the pipeline adds capability. Failure at any layer degrades to the previous layer. **Content is never lost.**

### Layer Model

| Layer | Technology | Capability | If this layer fails |
|-------|-----------|------------|---------------------|
| 0 | LaTeX source | `\begin{collapsible}` environment | Hard fail if preamble missing (build error) |
| 1 | LuaLaTeX, no ocgx2 | Content visible with `[Label]` header | Compile succeeds, no toggle — content inline with header |
| 2 | LuaLaTeX + ocgx2 | Clickable `[Show/Hide Label]` toggle in PDF | Full PDF functionality |
| 3 | preprocess.py | Sentinels injected for pandoc passthrough | If fix absent: pandoc drops environment markers, keeps content |
| 4 | pandoc | Sentinels survive as `<strong>CLPS:...</strong>` | Content present, sentinel text visible but ugly |
| 5 | postprocess | Sentinels upgraded to `<details><summary>` | If absent: Layer 4 fallback |
| 6 | Browser HTML5 | Native `<details>` toggle, no JS | If `<details>` unsupported: content visible inline |
| 7 | CSS | Visual styling, dark mode, print-all | If CSS absent: functional but unstyled |

Every layer is independently valuable. The system works at Layer 1. Each subsequent layer enhances.

### Module Architecture

```
build/
├── preamble.tex           # LaTeX definition: PDF renderer (Layers 1-2)
├── collapsible.py         # Protocol module: single source of truth (Layers 3-5)
├── preprocess.py          # Existing: calls collapsible.preprocess_tex()
├── postprocess-html.py    # New thin CLI: calls collapsible.postprocess_html()
└── html.css               # Style module: presentation (Layer 7)

manuscript/**/*.tex        # Content: authors use \begin{collapsible}[state]{Label}
```

**Key principle:** The sentinel format is defined ONCE in `build/collapsible.py` as constants. Both `preprocess.py` and `postprocess-html.py` import from it. Change the format in one place, both pipelines update.

## Convention

Every toggle button reads: **Show/Hide [Content Name]**

- Non-breaking thin space around the slash: `Show\,/\,Hide`
- Sans-serif, link-blue, bracketed: `[\,Show/Hide Label\,]`
- Consistent across PDF and HTML

Examples:
- `Show/Hide Bruce's Dossier`
- `Show/Hide Healer's Dossier`
- `Show/Hide Cryptome Article`
- `Show/Hide Suppression Evidence`

Default state configurable per block: `open` or `closed` (default: `closed`).

## Phase 1: Infrastructure

### 1A. LaTeX definition (`build/preamble.tex`)

Add after the existing `\graphicsonly` definition (after line 87), before `% --- Headers/footers ---`:

```latex
% --- Collapsible content blocks (Show/Hide toggle) ---
% Usage: \begin{collapsible}[open]{Label} ... \end{collapsible}
% Default: closed. PDF: ocgx2 toggle. HTML: <details>. Fallback: inline with header.
% Protocol: plans/0098-collapsible-content.md
\newcounter{collapsiblectr}
\ifdefined\switchocg
  % Layer 2: full ocgx2 toggle
  \newenvironment{collapsible}[2][closed]{%
    \stepcounter{collapsiblectr}%
    \edef\collapsibleid{clps-\the\value{collapsiblectr}}%
    \def\collapsiblevis{0}%
    \def\collapsibleopen{open}%
    \def\collapsiblearg{#1}%
    \ifx\collapsiblearg\collapsibleopen\def\collapsiblevis{1}\fi%
    \par\medskip\noindent
    \switchocg{\collapsibleid}{%
      \textcolor{linkblue}{\small\sffamily [\,Show/Hide~#2\,]}%
    }%
    \par\smallskip
    \begin{ocg}[printocg=always,exportocg=always]{#2}{\collapsibleid}{\collapsiblevis}%
  }{%
    \end{ocg}%
    \par\medskip
  }%
\else
  % Layer 1 fallback: no toggle, content always visible with header
  \newenvironment{collapsible}[2][closed]{%
    \par\medskip\noindent
    {\small\sffamily [\,#2\,]}%
    \par\smallskip
  }{\par\medskip}%
\fi
```

**Design notes:**
- `\ifdefined\switchocg` guards against ocgx2 absence — no `\makeatletter` needed (it's a plain TeX primitive).
- `\ifx` comparison for open/closed state — NOT `etoolbox`'s `\ifstrequal` (which is not expandable and would fail inside `\begin{ocg}`). No new package dependencies.
- Command names avoid `@` (e.g., `\collapsibleid` not `\collapsible@id`) — preamble.tex doesn't use `\makeatletter`.
- `printocg=always` + `exportocg=always`: content prints and exports regardless of toggle state.
- `~` (non-breaking space) in `Show/Hide~#2` prevents line break between "Hide" and the label.
- Layer 1 fallback omits the toggle link, just shows `[Label]` as a section marker. Content always visible.

### 1B. Protocol module (`build/collapsible.py` — NEW)

```python
#!/usr/bin/env python3
"""Collapsible Content Protocol — build module.

Single source of truth for the cross-format collapsible content system.
Imported by preprocess.py (LaTeX → sentinel) and postprocess-html.py (sentinel → HTML5).

Design: Adapter Pattern — one content interface, format-specific renderers.
Protocol: plans/0098-collapsible-content.md
"""

import re
from pathlib import Path

# --- Protocol constants (change here, both pipelines update) ---
SENTINEL_PREFIX = "CLPS"
SENTINEL_DELIM = ":"
CSS_CLASS = "collapsible"
BUTTON_TEXT = "Show\u2009/\u2009Hide"  # thin spaces around slash

# --- LaTeX sentinel patterns ---
_TEX_BEGIN = re.compile(
    r"\\begin\{collapsible\}"
    r"(?:\[(\w+)\])?"       # optional [open] or [closed]; group 1
    r"\{([^}]+)\}"          # {Label Text}; group 2
)
_TEX_END = re.compile(r"\\end\{collapsible\}")

# --- HTML sentinel patterns (match pandoc output) ---
# Pandoc wraps \textbf{...} in <p><strong>...</strong></p>
_HTML_BEGIN = re.compile(
    r"<p><strong>"
    + re.escape(SENTINEL_PREFIX) + re.escape(SENTINEL_DELIM)
    + r"(\w+)"              # state; group 1
    + re.escape(SENTINEL_DELIM)
    + r"(.+?)"              # label (non-greedy — handles smart quotes); group 2
    + r"</strong></p>"
)
_HTML_END = re.compile(
    r"<p><strong>"
    + re.escape(SENTINEL_PREFIX) + re.escape(SENTINEL_DELIM)
    + r"END</strong></p>"
)


def preprocess_tex(text: str) -> str:
    r"""Convert \begin{collapsible} to sentinels for pandoc passthrough.

    \begin{collapsible}[closed]{Label} → \textbf{CLPS:closed:Label}
    \end{collapsible}                  → \textbf{CLPS:END}

    Sentinels use COLONS (not underscores — _ is math-mode-only in LaTeX).
    """
    def _begin(m):
        state = m.group(1) or "closed"
        label = m.group(2)
        return (
            f"\\textbf{{{SENTINEL_PREFIX}{SENTINEL_DELIM}"
            f"{state}{SENTINEL_DELIM}{label}}}"
        )

    text = _TEX_BEGIN.sub(_begin, text)
    text = _TEX_END.sub(
        f"\\textbf{{{SENTINEL_PREFIX}{SENTINEL_DELIM}END}}", text
    )
    return text


def postprocess_html(html_path: str) -> None:
    """Upgrade sentinel <strong> tags to HTML5 <details><summary>.

    Reads, transforms, and overwrites the file in place.
    Strips surrounding <p> tags to prevent orphaned elements.
    Warns if any unconverted sentinels remain.
    """
    path = Path(html_path)
    text = path.read_text(encoding="utf-8")
    count = 0

    def _begin(m):
        nonlocal count
        count += 1
        state = m.group(1)
        label = m.group(2)
        open_attr = " open" if state == "open" else ""
        return (
            f'<details class="{CSS_CLASS}"{open_attr}>\n'
            f"<summary>{BUTTON_TEXT} {label}</summary>"
        )

    text = _HTML_BEGIN.sub(_begin, text)
    text = _HTML_END.sub("</details>", text)

    # Safety check
    remaining = text.count(f"{SENTINEL_PREFIX}{SENTINEL_DELIM}")
    if remaining > 0:
        print(
            f"WARNING: {remaining} unconverted collapsible sentinel(s) "
            f"in {html_path}"
        )

    path.write_text(text, encoding="utf-8")
    print(f"Collapsible: {count} block(s) converted in {path.name}")
```

### 1C. Integration with preprocess.py (`build/preprocess.py`)

Add import at top:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from collapsible import preprocess_tex
```

Add Fix 5 inside the `for src in REPO.rglob("*.tex"):` loop, after Fix 4:
```python
        # Fix 5: Collapsible content blocks → sentinels for pandoc
        text = preprocess_tex(text)
```

### 1D. Postprocessor CLI (`build/postprocess-html.py` — NEW)

```python
#!/usr/bin/env python3
"""Post-process HTML: upgrade collapsible sentinels to <details>."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from collapsible import postprocess_html

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <html-file>", file=sys.stderr)
        sys.exit(1)
    postprocess_html(sys.argv[1])
```

### 1E. Makefile (`Makefile`)

In the `html` target, add one line after the pandoc command:
```makefile
	python3 build/postprocess-html.py docs/downloads/Relinquishment.html
```

### 1F. CSS (`build/html.css`)

Append to existing file:
```css
/* --- Collapsible content blocks --- */
details.collapsible { margin: 1.5em 0; }
details.collapsible summary {
  cursor: pointer;
  color: #1a5276;
  font-family: sans-serif;
  font-size: 0.95em;
  padding: 0.4em 0;
  user-select: none;
}
details.collapsible summary:hover { text-decoration: underline; }

/* Print: force all collapsible content visible (mirrors PDF printocg=always) */
@media print {
  details.collapsible { display: block !important; }
  details.collapsible > * { display: block !important; }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  details.collapsible summary { color: #6ba3f7; }
}
```

### Phase 1 Test

1. Add a test block to any chapter (e.g., `manuscript/appendix/predictions.tex`):
   ```latex
   \begin{collapsible}[closed]{Test Block}
   This is test content. If you can read this, the collapsible system works.
   \end{collapsible}
   ```
2. `make dev` — verify PDF toggle works, HTML `<details>` renders
3. Remove test block
4. `make dev` again — clean build, `make check` passes

## Phase 2: Dossier Migration

### 2A. Move include in `main.tex`

Move `\include{manuscript/appendix/dossier}` from **line 127** (backmatter) to **after line 62** (after `pos01b-hobbit-mirror`, before `pos02-alpha-farm`). The dossier.tex header already specifies this placement.

Add a comment at the old location:
```latex
% \include{manuscript/appendix/dossier}  % Plan 0098: moved to early main body (after Hobbit Mirror)
```

### 2B. Wrap dossier content (`manuscript/appendix/dossier.tex`)

Keep chapter heading, intro quote, and Bruce's framing text **outside** collapsible blocks (always visible). Wrap the actual dossier content:

**Bruce's Dossier** — wrap from `\begin{center}\textsc{Five Eyes...}` (line ~25) through the end of The Target section (line ~360):
```latex
\begin{collapsible}[closed]{Bruce's Dossier}
\begin{center}
\textsc{Five Eyes --- Subject Profile (Approximation)}\\[0.3em]
...
\end{collapsible}
```

**Healer's Dossier** — wrap from `\section*{The Handler}` (line 361) through end of file:
```latex
\begin{collapsible}[closed]{Healer's Dossier}
\section*{The Handler}
...
\end{collapsible}
```

**Result — reader sees:**
```
The Recruitment Dossiers

"What follows is my reconstruction..." — Bruce Stephenson, 2026

[Show/Hide Bruce's Dossier]     ← collapsed by default
[Show/Hide Healer's Dossier]    ← collapsed by default
```

### 2C. TOC adjustment

The chapter uses `\chapter*` (unnumbered) with `\addcontentsline`. In Part I among numbered chapters, this is intentional — it's an interlude. No change needed.

## Phase 3: Additional Content Blocks

Apply collapsible treatment to (when editorial placement is determined):

| Content | Button Label | Default | Source |
|---------|-------------|---------|--------|
| Cryptome article | `Show/Hide Cryptome Article` | closed | `staging/evidence/cryptome-qccf-2012-03-17.txt` |
| Suppression evidence | `Show/Hide Suppression Evidence` | closed | To be written |
| Slashdot comments | `Show/Hide Slashdot Comments` | closed | To be retrieved |
| Science jargon | DEFERRED | — | Different mechanism (inline alt-text toggle, separate plan) |

Phase 3 items require editorial decisions about manuscript placement before implementation.

## Acceptance Criteria

1. `make dev` succeeds with zero new warnings
2. `make check` passes
3. PDF: clicking `[Show/Hide X]` toggles content in OCG-capable viewer
4. PDF: content prints regardless of toggle state (`printocg=always`)
5. PDF: Layer 1 fallback works (`\ifdefined\switchocg` branch compiles)
6. HTML: `<details><summary>` renders natively (no JS dependency)
7. HTML: dark mode styling correct
8. HTML: `@media print` forces all collapsible content visible
9. HTML: no unconverted sentinel warnings from postprocessor
10. Graceful PDF: basic viewer shows all content inline (not toggleable but present)
11. Graceful HTML: JS disabled — `<details>` still works
12. Graceful HTML: `<details>` unsupported — content visible inline
13. Dossiers appear in Part I (after Hobbit Mirror, before Alpha Farm), default collapsed
14. Button text consistent: always `[Show/Hide Name]`
15. No new LaTeX package dependencies
16. Protocol constants defined once in `build/collapsible.py`, no duplication

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| `\switchocg` not supported in some PDF viewers | Toggle link non-functional | Content visible via OCG default; `\ifdefined` guard ensures compile |
| Pandoc changes `\textbf` handling | Sentinels visible as text | Postprocessor warns; Layer 4 degradation is readable |
| Smart typography on labels (`'` → `'`) | Postprocessor regex misses | `.+?` non-greedy match handles any character |
| Cross-reference into collapsible block | Reader jumps to hidden content | Don't cross-reference into collapsible blocks (dossiers, articles are self-contained) |
| Page breaks inside collapsible block | Content split across pages | OCG layers span pages (content on all pages toggles together) — works correctly |
| `sys.path` import between build scripts | Fragile on unusual Python setups | Standard pattern; both scripts use `Path(__file__).parent` — robust |

## Handoff

Generator: Read Plan 0098 (`plans/0098-collapsible-content.md`). Implement Phase 1 (infrastructure: preamble.tex, collapsible.py, preprocess.py integration, postprocess-html.py, html.css, Makefile) then Phase 2 (dossier migration). Build with `make dev` and `make check` after each phase. Remove test block after Phase 1 verification. Phase 3 awaits editorial decisions. Commit format: `Plan 0098 phase N: description`.
