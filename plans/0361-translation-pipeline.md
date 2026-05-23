# Plan 0361: Internationalization (i18n) Translation Pipeline

**Status:** MASTER PLAN — sub-plans numbered 0361.P{N}.{letter}  
**Created:** 2026-05-20  
**Domain:** Book infrastructure  
**Priority:** High — book is live, accessibility is the next step  
**Quality rating:** 92% (see Risks)  
**Target domain:** renuncio.ai  

## Intent

Accurate but not perfect. Good enough. Machine translations that make the book accessible to non-English readers. We are optimizing for reach, not literary quality. ~70% of the world's literate internet population does not read English.

## Architecture: Token-Based i18n

Standard internationalization pattern, proven at production scale (Symantec Norton Store, ~30 languages). The approach:

1. **Tokenize** all translatable text in the source files
2. **Extract** tokens to per-language text files (KEY=value, one per line)
3. **Replace** source text with token references (`\tok{token-name}`)
4. **Resolve** tokens at build time from the target language's token file
5. **Fall back** to English (US) for any missing token
6. **Register** completed languages in `supported-languages.txt`

The build system becomes language-parameterized. Each language is just a directory of token files. Adding a language = translating the tokens. The build does the rest.

### Why NOT translate the output HTML

We considered translating the final HTML as a post-processing step. Rejected because:
- Fragile: HTML structure changes between builds
- No fallback mechanism for partial translations
- No incremental retranslation when English changes
- Can't build multiple output formats (HTML + future PDF)
- Not how production i18n systems work

### Why tokenize at the source level

- One source of truth for text (the token file)
- One source of truth for structure (the .tex/.yaml files)
- Build system handles all interactive elements (tooltips, puzzles) naturally
- Each language directory is self-contained — zip it, send it to a translator, unzip the reply
- Partial translations work (fallback to English)
- Standard pattern every i18n developer recognizes

## Directory Layout

```
i18n/
  us/                          # US English (canonical, always complete)
    tex-tokens                 # LaTeX prose tokens
    hover-tokens               # hover-definitions.yaml text
    puzzle-tokens              # puzzle-data.yaml text
    deeplink-tokens            # deep-links.yaml question text
    tech-tokens                # tech-collapse.yaml text
    ui-tokens                  # preprocess.py UI strings
  es/                          # Spanish
    tex-tokens
    hover-tokens
    puzzle-tokens
    deeplink-tokens
    tech-tokens
    ui-tokens
  zh/                          # Mandarin Chinese
    ...
  ar/                          # Arabic
    ...
  glossary.yaml                # Cross-language term definitions
  supported-languages.txt      # Languages ready for public build
```

## Token File Format

Simple KEY=value. One token per line. Long lines are fine — editors soft-wrap.

```
they-gave-it-up=They gave it up. Not to another country. Not to a corporation. To the thing they'd built to outlast them. They were forbidden to tell anyone. Ever. They would die of old age before they were allowed to speak freely.
the-act-has-names=The act has names in many traditions --- \textit{kenosis} in Christianity, \textit{tawakkul} in Islam, \textit{tzimtzum} in Kabbalah, \textit{aparigraha} in Hinduism, the \textit{bodhisattva vow} in Buddhism, and trusteeship of a commons in Indigenous traditions across the Americas and the Pacific.
bruce-spent-twenty-years=Bruce spent the next twenty years trying to figure out if any of it was true. He wrote about quantum computing publicly, published a mathematical paper on a scientific preprint server, and quietly followed every thread he could find. He never stopped asking questions.
```

### Parser

Split on first `=`. Everything before is the key. Everything after is the value. Five lines of Python:

```python
def load_tokens(path):
    tokens = {}
    for line in open(path):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        key, _, value = line.partition('=')
        if key and key not in tokens:  # first-match-wins
            tokens[key] = value
    return tokens
```

First-match-wins semantics. Duplicates are dead weight — the dedup routine cleans them.

### Token Naming Convention

- **All lowercase**, kebab-case: `[a-z0-9-]+`
- **Descriptive of the English text** — first few distinctive words
- **Long enough to be unique**, short enough to read: `bruce-spent-twenty-years`, not `p-front-summary-256`
- **No type prefixes** unless collision risk is high (headings are usually unique enough)
- Token names are self-documenting: seeing `\tok{they-gave-it-up}` in a .tex file tells you what text goes there without looking it up

**Collision avoidance:** Use enough words to disambiguate. Two paragraphs starting "The question is..." become `the-question-is-not-whether` and `the-question-is-arriving`. Natural language diversity handles most cases.

**Dedup rule:** If the same text appears in multiple places, one token covers all instances. If near-identical text differs in context, use distinct tokens with more-specific names. Periodically run the dedup checker to remove dead duplicates. First-match-wins means extra entries are harmless but wasteful.

### Token file organization

Tokens are ordered by document position with section comment headers:

```
# === hook.tex ===
in-the-early-1990s=In the early 1990s, a team of scientists...
they-gave-it-up=They gave it up. Not to another country...
the-act-has-names=The act has names in many traditions...

# === summary.tex ===
between-2003-and-2006=Between 2003 and 2006, my mentor...
```

For the resolver (hash-based lookup), order doesn't matter. For human readability when editing, document order with headers helps you find things.

## In the .tex Source

After tokenization, a .tex file looks like:

```latex
\settrack{trackone}

\chapter*{What Would You Do?}

\tok{in-the-early-1990s}

\tok{they-gave-it-up}

\tok{the-act-has-names}

% SPIRAL-REPEAT: "Universal Declaration of Human Rights"
\tok{they-anchored-the-custodians-charter}
```

Blank lines between tokens preserve LaTeX paragraph separation. Comments and structural commands (`\chapter*{}`, `\settrack{}`, `\begin{quote}`, `\end{quote}`, `\begin{itemize}`, etc.) stay in the .tex file — they are structure, not text.

### What stays in .tex (structure)

- `\chapter*{}`, `\section*{}` — but their TITLE TEXT is a token inside the braces
- `\begin{...}`, `\end{...}` — environments
- `\settrack{}`, `\srcnote{}` — metadata
- `\label{}` — cross-references
- `\clearpage`, `\vspace{}` — layout
- Comments (`%`)
- `\ifdefined`/`\fi` — conditionals
- Blank lines (paragraph separation)

### What goes into tokens (text)

- Paragraph text (including inline `\textit{}`, `\textbf{}`, `\hovertip[id]{text}`, `\footcite{}`)
- Heading text (the argument of `\chapter*{}`, `\section*{}`)
- List item text (including `\item[\textbf{label}]` when the label is translatable)
- Block quote text
- Footnote text (`\footnote{...}`)

### What is NOT tokenized

- `\srcnote{}` content (metadata, not reader-facing)
- `\footcite{}` keys (bibliography references)
- `\label{}` arguments (cross-reference IDs)
- Math mode content (`$...$`) — math is universal, but it travels inside its paragraph's token
- URLs
- The `\tok` command names themselves

## The `\tok{}` LaTeX Command

Define as a safety net in the document preamble:

```latex
\newcommand{\tok}[1]{[UNRESOLVED: #1]}
```

If the resolver fails to process a file, LaTeX renders `[UNRESOLVED: token-name]` visibly in the output instead of crashing. The resolver replaces `\tok{name}` with the value BEFORE LaTeX sees it, so this command should never fire in a correct build.

## Build Integration

### Resolver: `build/resolve-tokens.py`

```
python3 build/resolve-tokens.py --lang=es --src=manuscript/ --out=build/resolved/
```

1. Reads all token files for the target language from `i18n/es/`
2. Falls back to `i18n/us/` for any missing token
3. Copies all .tex files from `manuscript/` to `build/resolved/`
4. In each copied file, replaces `\tok{name}` with the token value
5. Reports: N tokens resolved, N from target language, N from fallback

Fast: reads token files into a hash map (lazy-load once), does a single regex pass per file.

### Makefile

```makefile
LANG ?= us

# Resolve tokens for target language, then build
html: resolve
	# existing LaTeX → make4ht → HTML → preprocess.py pipeline
	# but operating on build/resolved/ instead of manuscript/

resolve:
	python3 build/resolve-tokens.py --lang=$(LANG) \
		--src=manuscript/ --out=build/resolved/

# Build a specific language
translate-%:
	$(MAKE) html LANG=$*

# Build all supported languages
translate-all:
	@while read lang code rest; do \
		echo "Building $$code..."; \
		$(MAKE) html LANG=$$code; \
	done < i18n/supported-languages.txt
```

Usage: `make html LANG=es` or `make translate-es` or `make translate-all`.

### preprocess.py changes

preprocess.py reads YAML data files (hover-definitions, puzzles, deep-links, tech-collapse). It must:

1. Accept a `--lang` argument (default: `us`)
2. After loading each YAML file, resolve `\tok{name}` patterns in string values using the appropriate token file
3. For UI chrome strings, read from `i18n/{lang}/ui-tokens` with fallback to `us`

## The Hovertip Fix (Prerequisite)

**Current (text-based matching — broken for i18n):**
```latex
\hovertip{Universal Declaration of Human Rights}
```
↓ preprocess.py slugifies display text ↓
```html
<span data-hover-id="universal-declaration-of-human-rights">Universal Declaration...</span>
```

Translate the display text → slug changes → tooltip lookup fails silently.

**Fixed (ID-based matching — language-independent):**
```latex
\hovertip[udhr]{Universal Declaration of Human Rights}
```
↓ preprocess.py uses explicit ID ↓
```html
<span data-hover-id="udhr">Declaración Universal de los Derechos Humanos</span>
```

Display text is translated. ID is stable. Tooltip works in every language.

**Implementation:** The auto-tokenizer script, when walking .tex files, also converts every `\hovertip{text}` to `\hovertip[id]{text}` by looking up `text` in hover-definitions.yaml (which already has slugified IDs). This is a mechanical transformation — no human judgment needed, ~600 instances, ~100 unique terms.

**Unmatched hover terms** (text not found in hover-definitions.yaml) are flagged for manual review.

## Glossary: `i18n/glossary.yaml`

Terms requiring consistent translation across all token files.

```yaml
version: 1

# Terms that must appear UNTRANSLATED in all languages
preserve:
  coined_terms:
    - "the Flat"
    - "Custodian"
    - "Healer"
    - "the Braid"
    - "Argus"
    - "Dignity Net"
    - "COWS"
    - "TQNN"
  proper_nouns:
    - "Bruce Stephenson"
    - "Genevieve Prentice"
    - "Robin Macomber"
  acronyms:
    - "UDHR"
    - "DARPA"
    - "GCHQ"
    - "SAS"
    - "2DEG"
    - "FQHE"

# Terms with official or specific translations per language
# (UN documents have official translations in all 6 UN languages)
specific:
  "Universal Declaration of Human Rights":
    es: "Declaración Universal de los Derechos Humanos"
    zh: "世界人权宣言"
    ar: "الإعلان العالمي لحقوق الإنسان"
    hi: "मानवाधिकारों की सार्वभौम घोषणा"
    pt: "Declaração Universal dos Direitos Humanos"
    ru: "Всеобщая декларация прав человека"
    fr: "Déclaration universelle des droits de l'homme"
    ja: "世界人権宣言"
  "relinquishment":
    es: "renuncia"
    pt: "renúncia"
    fr: "renoncement"
    zh: "放弃"
    ru: "отречение"
    ar: "التخلي"
    ja: "放棄"
  "guided deduction":
    es: "deducción guiada"
    pt: "dedução guiada"
    fr: "déduction guidée"
    zh: "引导演绎"
    ru: "управляемая дедукция"
  "autocatalytic set":
    es: "conjunto autocatalítico"
    pt: "conjunto autocatalítico"
    zh: "自催化集合"
    ru: "автокаталитическое множество"
```

## Language Priority

Based on reachable non-English literate internet population:

| Priority | Lang | Code | Script | Direction | Reachable | Build complexity |
|----------|------|------|--------|-----------|-----------|-----------------|
| 1 | Spanish | es | Latin | LTR | ~400M+ | Low (proof of concept) |
| 2 | Portuguese | pt | Latin | LTR | ~180M+ | Low |
| 3 | French | fr | Latin | LTR | ~100M+ | Low |
| 4 | Indonesian | id | Latin | LTR | ~130M+ | Low |
| 5 | Chinese | zh | CJK | LTR | ~900M+ | Medium (fonts, line-break) |
| 6 | Russian | ru | Cyrillic | LTR | ~180M+ | Medium (fonts) |
| 7 | Arabic | ar | Arabic | **RTL** | ~250M+ | High (RTL layout) |
| 8 | Hindi | hi | Devanagari | LTR | ~300M+ | Medium (fonts) |
| 9 | Japanese | ja | CJK | LTR | ~100M+ | Medium (fonts) |
| 10 | Bengali | bn | Bengali | LTR | ~100M+ | Medium (fonts) |

Latin-script languages (1–4) work with the current pdfLaTeX/make4ht pipeline. Non-Latin languages (5–10) require XeLaTeX (`make4ht -x`) and font configuration.

## Phases

### Phase 0: Hovertip ID Refactor
**Sub-plan:** 0361.P0.A  
**Dependency:** None  
**Risk:** Low — mechanical transformation  

- Build lookup table: hover-definitions.yaml text → hover-id
- Walk all .tex files, convert `\hovertip{text}` → `\hovertip[id]{text}`
- Update `\hovertip` LaTeX command definition to accept optional `[id]` argument
- Update preprocess.py to use explicit ID for `data-hover-id` attribute
- Flag unmatched hover terms for manual review

**Acceptance criteria:**
1. All ~600 `\hovertip` instances have explicit `[id]` arguments
2. Build produces functionally identical HTML (tooltips still work, same visual output)
3. `data-hover-id` attributes in HTML match hover-definitions.yaml IDs
4. Zero unmatched hover terms (or all unmatched terms reviewed and resolved)

### Phase 1: Token Infrastructure
**Sub-plan:** 0361.P1.A  
**Dependency:** None (can run parallel with Phase 0)  
**Risk:** Low — new code, no existing code changes  

- Build `build/resolve-tokens.py` (resolver)
- Define `\tok{}` LaTeX command in document preamble
- Create `i18n/` directory structure with `us/` subdirectory
- Create empty token files (tex-tokens, hover-tokens, etc.)
- Create `i18n/supported-languages.txt` with US English entry
- Makefile integration (`LANG=` parameter, `translate-%` targets)
- Build dedup checker tool

**Acceptance criteria:**
1. `resolve-tokens.py` loads token files into hash map, resolves `\tok{name}` patterns
2. Resolver reports token counts (resolved, fallback, unresolved)
3. With empty token files, build produces identical output (no `\tok{}` in source yet)
4. `make html LANG=us` works
5. Dedup checker runs and reports 0 duplicates on empty files

### Phase 2: Tokenize English LaTeX
**Sub-plan:** 0361.P2.A (auto-tokenizer script), 0361.P2.B–G (chapter groups)  
**Dependency:** Phase 1 must be complete  
**Risk:** HIGH — this is the main engineering challenge  

Build the auto-tokenizer script. Then run it chapter-by-chapter with verification after each group:

| Sub-plan | Files | Est. tokens |
|----------|-------|-------------|
| P2.A | Build auto-tokenizer script | 0 |
| P2.B | Front matter: hook, summary, introduction, preface, copyright | ~200 |
| P2.C | Track 1 — The Flat: 6 chapters | ~500 |
| P2.D | Track 2 — The Record: 6 chapters | ~500 |
| P2.E | Track 3 — Awakening: 6 chapters | ~500 |
| P2.F | Back matter: afterword, acknowledgements, corrections, verification | ~200 |
| P2.G | Appendices | ~200 |

**The auto-tokenizer script must handle:**
- Paragraph detection (blank-line separated text blocks)
- Heading extraction (`\chapter*{Title}` → title text becomes a token)
- List item extraction (`\item[\textbf{Label}] Text` → whole item becomes a token)
- Inline commands preserved in token values (`\textit{}`, `\hovertip[id]{}`, `\footcite{}`)
- Structural commands left in .tex (`\begin{}`, `\end{}`, `\settrack{}`, `\label{}`)
- Comments left in .tex (not tokenized)
- `\srcnote{}` left in .tex (metadata, not tokenized)
- Token name generation from first few distinctive words of the text
- Collision detection and automatic disambiguation

**Acceptance criteria (per chapter group):**
1. All translatable text extracted to `i18n/us/tex-tokens`
2. Tokenized .tex files contain only structural commands and `\tok{name}` references
3. `make html LANG=us` produces identical output to pre-tokenization build
4. Dedup checker reports 0 unintended duplicates
5. All token names are self-documenting (readable without lookup)

**Verification method:** SHA-256 hash of final HTML before and after tokenization. Must match.

### Phase 3: Tokenize YAML + UI Chrome + Glossary
**Sub-plan:** 0361.P3.A  
**Dependency:** Phase 1 must be complete. Phase 0 should be complete (hover-definitions need stable IDs).  
**Risk:** Medium — preprocess.py modifications  

- Tokenize hover-definitions.yaml text → `i18n/us/hover-tokens`
- Tokenize puzzle-data.yaml text → `i18n/us/puzzle-tokens`
- Tokenize deep-links.yaml question text → `i18n/us/deeplink-tokens`
- Tokenize tech-collapse.yaml text → `i18n/us/tech-tokens`
- Identify hardcoded English strings in preprocess.py → `i18n/us/ui-tokens`
- Update preprocess.py to accept `--lang` and resolve tokens from appropriate files
- Create `i18n/glossary.yaml`
- Build translation prompt template and chunking tool

**Acceptance criteria:**
1. All YAML translatable text extracted to per-type token files
2. All preprocess.py UI strings extracted to ui-tokens (~50–100 strings)
3. `make html LANG=us` produces identical output
4. `preprocess.py --lang=us` works identically to current behavior
5. Glossary loads and validates
6. Chunking tool produces translation prompt files with glossary context

### Phase 4: Spanish Translation (Proof of Concept)
**Sub-plan:** 0361.P4.A (translate tex-tokens), 0361.P4.B (translate YAML tokens + verify)  
**Dependency:** Phases 2 and 3 must be complete  
**Risk:** Medium — first real test of the full pipeline  

- Copy all US token files to `i18n/es/`
- Translate each token file (chunked, with glossary)
- Build Spanish HTML: `make html LANG=es`
- Verify interactive elements: tooltips appear, puzzles work, deep links function
- Add machine-translation banner at top of page
- Adjust copyright notice: "Authorized machine translation"
- Adjust verification section (hash doesn't apply to translations)
- Add `es` to `supported-languages.txt`

**Acceptance criteria:**
1. All tokens translated (0 English fallbacks except intentional glossary preserves)
2. All tooltips display correctly (hover-id matching works in Spanish)
3. All puzzles functional (questions, options, hints, feedback in Spanish)
4. Glossary terms preserved/translated per glossary spec
5. Machine-translation banner present with link to English original
6. LaTeX escaping preserved (`\%`, `\&`, `\textasciitilde{}` not broken)
7. Build completes without warnings

### Phase 5: Latin-Script Languages
**Sub-plan:** 0361.P5.A (Portuguese), 0361.P5.B (French), 0361.P5.C (Indonesian)  
**Dependency:** Phase 4 must be complete (proves the pipeline)  
**Risk:** Low — pipeline is proven, just new content  

Same process as Phase 4 for each language. Faster because the pipeline is proven and no new infrastructure is needed.

**Acceptance criteria per language:** Same as Phase 4.

### Phase 6: Non-Latin Build Pipeline + Translations
**Sub-plan:** 0361.P6.A (build pipeline), 0361.P6.B–F (per-language translations)  
**Dependency:** Phase 4 must be complete  
**Risk:** HIGH — LaTeX engine change, font configuration, RTL layout  

**P6.A — Build pipeline changes:**
- Test XeLaTeX + make4ht (`make4ht -x`) with non-Latin characters
- Configure font fallbacks per script family:
  - CJK: Noto Sans CJK or similar
  - Cyrillic: existing Latin fonts often include Cyrillic
  - Arabic: Noto Naskh Arabic or similar + RTL CSS
  - Devanagari: Noto Sans Devanagari
  - Bengali: Noto Sans Bengali
- Build RTL CSS overrides for Arabic (`dir="rtl"`, margin/padding flip, text-align)
- Build CJK CSS overrides (line-height, word-break rules)
- Makefile: auto-detect script family from language code, use appropriate engine

**P6.B–F — Translations:**
- Chinese (zh), Russian (ru), Arabic (ar), Hindi (hi), Japanese (ja), Bengali (bn)
- Each: translate tokens → build → verify

**Acceptance criteria for P6.A:**
1. A test paragraph in Chinese builds correctly to HTML
2. A test paragraph in Arabic renders RTL correctly
3. Font fallbacks produce readable output for all script families

**Acceptance criteria per language:** Same as Phase 4 + script-specific rendering checks.

### Phase 7: Hosting on renuncio.ai
**Sub-plan:** 0361.P7.A  
**Dependency:** Phase 4 must be complete (at least one translation to host)  
**Risk:** Low — standard web hosting  

- Configure renuncio.ai domain (DNS, GitHub Pages or equivalent)
- URL structure: `renuncio.ai/es/`, `renuncio.ai/zh/`, etc.
- Landing page at `renuncio.ai/` with language selector driven by `supported-languages.txt`
- Each language directory contains: translated HTML + supporting assets
- `renuncio.ai/en/` redirects to `relinquishment.ai`
- Cross-link: English edition links to renuncio.ai, translations link back

**Acceptance criteria:**
1. Language selector shows all supported languages
2. Each language URL serves the correct translation
3. English redirect works
4. Cross-links functional in both directions

### Phase 8: Maintenance Tools
**Sub-plan:** 0361.P8.A  
**Dependency:** Phase 4 must be complete  
**Risk:** Low — tooling, no content changes  

- `build/translate-diff.py`: compare current English token extraction against a language's source hashes. Report: N unchanged, N modified (need retranslation), N new, N deleted.
- Retranslation prompt generator: produce prompts for only changed/new tokens
- Quality verifier: check all hover-ids resolve, all puzzle options present, no `[UNRESOLVED]` markers
- Dedup maintenance: periodic cleanup of dead duplicate tokens

**Acceptance criteria:**
1. Diff tool correctly detects changes between token file versions
2. Retranslation prompts include only changed/new tokens with glossary context
3. Quality verifier catches intentionally broken tokens in test input

## Workflow After Tokenization

**Text edits:** Edit `i18n/us/tex-tokens` (or the appropriate token file). Token names are self-documenting — search for the first few words of the text you want to change. The .tex files are now structural templates; prose lives in the token files.

**Structural edits:** Edit the .tex files (adding/removing sections, changing environments). Add/remove `\tok{name}` references as needed, and create/remove corresponding token entries.

**Adding a language:** `cp -r i18n/us/ i18n/xx/` → translate each token file → add `xx` to `supported-languages.txt` → `make translate-xx`.

**Updating translations after English changes:** `build/translate-diff.py us xx` → shows which tokens changed → retranslate only those → rebuild.

**Sending to an external translator:** `zip -r i18n/es.zip i18n/es/` → send the zip → receive translated zip → unzip → rebuild.

## Risks

1. **Auto-tokenizer complexity (HIGH).** Parsing 30+ .tex files with diverse LaTeX structures is the main engineering challenge. Mitigation: process chapter-by-chapter with build verification after each group. Budget 2–3 Generator sessions.

2. **LaTeX escaping in translations (MEDIUM).** Translators (human or Claude) must preserve `\%`, `\&`, `\textit{}`, etc. An unescaped `%` silently eats the rest of the line. Mitigation: translation prompts explicitly list LaTeX commands to preserve. Quality verifier checks for common escaping errors.

3. **Non-Latin LaTeX builds (MEDIUM).** CJK, Arabic, Devanagari may require XeLaTeX and font configuration. Mitigation: Latin-script languages first (no risk), non-Latin pipeline tested with single paragraphs before full translation.

4. **Editing workflow change (LOW for this book).** After tokenization, prose edits happen in token files, not .tex files. Acceptable because the book is published and content is mostly stable ("MOVING CONTENT AROUND, probably little or no new content"). Would be problematic for a book under active composition.

5. **Glossary accuracy (LOW).** Some per-language translations of scientific terms are from LLM training data. Official UN translations (UDHR) are verified. Scientific terms should be spot-checked by native speakers before Phase 6.

## Estimated Effort

| Phase | Generator sessions | Notes |
|-------|-------------------|-------|
| 0: Hovertip fix | 1 | Mechanical refactor |
| 1: Infrastructure | 1 | New code, no content changes |
| 2: Tokenize English | 2–3 | Largest phase, chapter-by-chapter |
| 3: YAML + UI + glossary | 1–2 | preprocess.py modifications |
| 4: Spanish | 2–3 | First translation, most verification |
| 5: Latin-script (×3) | 1 each | Pipeline proven, just content |
| 6: Non-Latin pipeline | 1–2 | Engine/font configuration |
| 6: Non-Latin translations (×6) | 1 each | Content + script verification |
| 7: Hosting | 1 | Standard web setup |
| 8: Maintenance tools | 1 | Tooling |
| **Total** | **~18–24** | |

## Sub-Plan Naming Convention

```
0361.P{phase}.{letter} — {short description}

Examples:
  0361.P0.A — Hovertip ID refactor
  0361.P1.A — Token infrastructure (resolver, format, Makefile)
  0361.P2.A — Auto-tokenizer script
  0361.P2.B — Tokenize front matter
  0361.P2.C — Tokenize Track 1 (The Flat)
  0361.P4.A — Translate Spanish tex-tokens
  0361.P4.B — Translate Spanish YAML tokens + verify
  0361.P5.A — Portuguese translation
  0361.P6.A — Non-Latin build pipeline
  0361.P6.B — Chinese translation
  0361.P7.A — renuncio.ai hosting
```

Each sub-plan is a self-contained Generator prompt with acceptance criteria. The Generator shell reads the sub-plan, executes, reports completion.
