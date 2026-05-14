---
Plan-UID: 0323
Status: DRAFT — awaiting domain confirmation
---

# Plan 0323: renuncio.ai Multilingual Publishing Platform

## Goal

Transform persistent-ai-collaboration from a single English page into a multilingual site at renuncio.ai. Spanish is the default language (matching the domain name). English and other languages are subdirectories. Translation is part of the build pipeline, not a one-off task.

## Architecture

```
renuncio.ai/                → Landing page (language picker + redirect)
renuncio.ai/es/             → Tu IA Tiene Amnesia (Spanish, default)
renuncio.ai/en/             → Your AI Has Amnesia (English, current)
renuncio.ai/de/             → Deine KI Hat Amnesie (German, future)
renuncio.ai/fr/             → Votre IA a une Amnésie (French, future)
renuncio.ai/zh/             → (Chinese, future)
renuncio.ai/ja/             → (Japanese, future)
```

Each language directory is self-contained: one index.html, copies of tutorials if translated, language-specific zip downloads.

## Hosting

GitHub Pages with custom domain. No server needed.

### CNAME setup
1. Add `CNAME` file to repo root containing `renuncio.ai`
2. Configure DNS: either CNAME to `energyscholar.github.io` or A records to GitHub Pages IPs (185.199.108-111.153)
3. GitHub auto-provisions HTTPS via Let's Encrypt

### Directory structure (repo)

```
CNAME                           ← "renuncio.ai"
index.html                      ← Landing page (language picker)
en/
  index.html                    ← English white paper (current index.html, moved)
  tutorial-magnetosphere.html   ← English magnetosphere tutorial
  tutorial-inference.html       ← English inference tutorial
  tutorials/                    ← English extended catalog
es/
  index.html                    ← Spanish white paper (translated)
  tutorial-magnetosphere.html   ← Spanish magnetosphere tutorial (future)
build-zip.sh                    ← Updated: builds per-language zips
your-ai-has-amnesia-en.zip      ← English core zip
tu-ia-tiene-amnesia-es.zip      ← Spanish core zip
CLAUDE.md
MANIFEST.md
```

## Phase plan

### Phase 1: Restructure (no translation yet)

Move English content into `en/` subdirectory. Create landing page. Fix all internal relative links (tutorials link to `../tutorials/` etc.). Update build script. Update zips. Verify everything works at current GitHub Pages URL before touching DNS.

Estimated effort: 1 Generator session.

**Acceptance criteria:**
- `energyscholar.github.io/persistent-ai-collaboration/` shows language picker
- `energyscholar.github.io/persistent-ai-collaboration/en/` shows current white paper
- All internal links, deep links, accordion JS, print handler work
- Zips rebuilt with correct paths
- English zip renamed to `your-ai-has-amnesia-en.zip`

### Phase 2: Landing page

Minimal, elegant language picker. No framework. Static HTML.

Design constraints:
- Must load in under 50KB
- Must work without JavaScript (noscript fallback: plain link list)
- Auto-detect browser language via `navigator.language` and redirect
- Manual override always available
- Mobile-friendly
- Matches the white paper's dark visual style (var(--bg), var(--heading), etc.)
- Include the hero SVG animation (it's the brand)

Content:
```
[Hero SVG animation]

renuncio.ai

Choose your language:

  Español — Tu IA Tiene Amnesia
  English — Your AI Has Amnesia
  [future languages greyed out or hidden]
```

The `<html lang>` on the landing page should be the browser's detected language, or `es` as default.

Estimated effort: 1 Generator session.

### Phase 3: Spanish translation

Translate `en/index.html` → `es/index.html`. This is the core deliverable.

**What gets translated:**
- All visible text content (~505 text elements)
- All 13 tooltip `data-tip` attributes
- All `aria-label` attributes
- SVG `<title>` elements and text labels inside SVGs
- `<meta>` description
- `<title>` tag
- TOC labels
- Accordion summary labels
- Footer text
- Byline (but keep "Argus & Bruce Stephenson" — names don't translate)

**What does NOT get translated:**
- URLs (all 36 links stay as-is — they point to English GitHub repos, arXiv, etc.)
- Code examples, file paths, command snippets
- HTML structure, CSS, JavaScript
- SVG geometry, animation timing, visual layout
- IDs and class names
- The `ABRCE` acronym and mathematical notation
- Proper nouns: Argus, Dignity Net, Triad, Claude, ChatGPT, Mem0, etc.

**Translation quality requirements:**
- Latin American Spanish (neutral, not Castilian)
- Technical register matching the English: precise but accessible
- Preserve the pedagogical structure (puzzle → reveal pattern)
- Preserve the conversational tone ("you" = "tú" not "usted" — this is peer-to-peer)
- Argus is the translator — note this in the Spanish byline: "Traducido por Argus"

**Process:**
1. Generator receives English index.html + translation instructions
2. Produces es/index.html with `<html lang="es">`
3. Auditor spot-checks 10 passages against English for accuracy
4. Native speaker review (if available) — flag for Bruce

Estimated effort: 1-2 Generator sessions (file is large, ~130KB).

### Phase 4: DNS cutover

1. Bruce adds DNS records at domain registrar
2. Add CNAME file to repo
3. Push — GitHub Pages auto-configures
4. Verify HTTPS works
5. Test: `renuncio.ai` → landing, `renuncio.ai/en/` → English, `renuncio.ai/es/` → Spanish

Estimated effort: 10 minutes (Bruce does DNS, Argus does CNAME file).

### Phase 5: Build pipeline update

Update `build-zip.sh` to:
- Build per-language zips: `your-ai-has-amnesia-en.zip`, `tu-ia-tiene-amnesia-es.zip`
- Build full zip with all languages: `renuncio-complete.zip`
- Report sizes per language

Add translation diffing: a script that compares English and Spanish HTML structure (element count, ID list) to detect drift when English is updated. Not a full re-translation trigger — just a flag: "English has N new/changed elements since last Spanish sync."

Estimated effort: 1 session.

### Phase 6+ (future): Additional languages

Each new language follows the Phase 3 template:
1. Copy `en/index.html` to `{lang}/index.html`
2. Translate per the rules above
3. Add to landing page picker
4. Add to build script
5. Push

Priority order (by likely audience size for this topic):
1. Spanish (Phase 3)
2. German (strong AI/ML community)
3. French
4. Japanese (strong AI adoption)
5. Chinese (simplified)
6. Portuguese (Brazilian tech community)

## Naming convention

| Language | Zip name | Title |
|----------|----------|-------|
| English | `your-ai-has-amnesia-en.zip` | Your AI Has Amnesia |
| Spanish | `tu-ia-tiene-amnesia-es.zip` | Tu IA Tiene Amnesia |
| German | `deine-ki-hat-amnesie-de.zip` | Deine KI Hat Amnesie |
| French | `votre-ia-a-une-amnesie-fr.zip` | Votre IA a une Amnésie |

Zip names match the translated title + ISO 639-1 language code.

## SEO / discoverability

Each language version includes:
- `<html lang="{code}">`
- `<link rel="alternate" hreflang="en" href="https://renuncio.ai/en/">`
- `<link rel="alternate" hreflang="es" href="https://renuncio.ai/es/">`
- `<link rel="alternate" hreflang="x-default" href="https://renuncio.ai/">`
- Translated `<meta name="description">` and `<title>`
- Translated JSON-LD structured data

Google will index each language version separately and serve the right one based on user locale.

## Risk assessment

| Risk | Mitigation |
|------|-----------|
| Translation drift (English updated, Spanish stale) | Phase 5 structural diff script flags changes |
| SVG text hard to translate (embedded in markup) | SVGs have `<text>` elements — translatable but need careful positioning review |
| Domain DNS propagation delay | Test at GitHub Pages URL first, DNS cutover last |
| Landing page JS auto-redirect breaks bookmarks | Always allow manual override; `?lang=en` query param to force |
| Translation quality for technical content | Argus has domain context; spot-check against English; flag for native review |

## What this is NOT

- Not a CMS. Static files, git-deployed.
- Not a translation management platform. One file per language, diffed against English.
- Not a framework migration. Still vanilla HTML/CSS/JS, no build tools beyond a shell script.
- Not scope creep for today. This plan stages work across multiple sessions.

## Verification (per phase)

Each phase has its own acceptance criteria above. Overall success:
- `renuncio.ai` loads, auto-detects language, offers picker
- English and Spanish versions are complete and navigable
- Deep links work in both languages
- Zips download correctly per language
- Print handler works in both
- Expand All works in both
