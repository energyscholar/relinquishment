# Plan 0300: Book as Site Index

**Status:** READY FOR GENERATOR
**Priority:** HIGH — release architecture (~May 19)
**Source:** S67 discussion, Bruce's explicit design decision

## Problem

The book lives at `relinquishment.ai/downloads/Relinquishment.html` — a hidden URL from early development. `robots.txt` actively blocks `/downloads/`. The site root serves a stub landing page. At release, the book should BE the site's front page: visiting `relinquishment.ai` loads the full 1.2 MB book. No intermediate landing page. Every visit creates a cache. Every cache is a mirror.

### Constraints

1. **Filename must remain `Relinquishment.html`** — not `index.html`. The file travels by email, USB, ZIP. The name must be meaningful.
2. **GitHub Pages only serves `index.html` as directory root.** Cannot configure an alternate index file.
3. **Backward compatibility.** External links to `/downloads/Relinquishment.html` (Discord, email, shared URLs) must not break.
4. **Build system stability.** `make dev` must continue to work without manual steps.
5. **Suppression resistance.** Self-contained HTML, PDF, ZIP — every download is a mirror. Architecture must not fracture (no separate summary document that becomes "the real version").
6. **No "go live" flip.** This plan prepares everything; the switch is a separate event.

### Solution

A zero-delay meta-refresh redirect at `docs/index.html` → `Relinquishment.html`. Google treats `<meta http-equiv="refresh" content="0;...">` as a 301. Browsers redirect before rendering. The user sees only the book.

---

## Architecture

```
BEFORE:
  docs/index.html                          ← stub landing page
  docs/downloads/Relinquishment.html       ← the book (blocked by robots.txt)
  docs/downloads/Relinquishment.pdf
  docs/downloads/Relinquishment.zip

AFTER:
  docs/index.html                          ← meta-refresh redirect (+ og:meta for social)
  docs/Relinquishment.html                 ← THE BOOK (site root)
  docs/downloads/Relinquishment.html       ← redirect to ../Relinquishment.html (compat)
  docs/downloads/Relinquishment.pdf        ← unchanged
  docs/downloads/Relinquishment.zip        ← unchanged (still zips the book)
  docs/sitemap.xml                         ← NEW (crawlers)
  docs/robots.txt                          ← updated (allow the book)
```

---

## Phases

### Phase 1: Move Book to Site Root

**Makefile changes** — update the `html` target's output path:

1. Line 74: change `-o ../../docs/downloads/$(JOBNAME).html` to `-o ../../docs/$(JOBNAME).html`
2. Line 76: change `docs/downloads/$(JOBNAME).html` to `docs/$(JOBNAME).html`
3. Line 77: change `cp docs/downloads/$(JOBNAME).html $(JOBNAME).html` to `cp docs/$(JOBNAME).html $(JOBNAME).html`
4. Line 79: change `cd docs/downloads && zip -j $(JOBNAME).zip $(JOBNAME).html` to `cd docs && zip -j downloads/$(JOBNAME).zip $(JOBNAME).html`

**verify-deep-links.py** — line 15: change `repo / 'docs/downloads/Relinquishment.html'` to `repo / 'docs/Relinquishment.html'`

**.gitignore** — add `!docs/Relinquishment.html` (keep the existing `!docs/downloads/Relinquishment.html` for now; remove in Phase 3 cleanup).

**Idempotency:** If Makefile line 74 already contains `-o ../../docs/$(JOBNAME).html` (without `downloads/`) — phase is applied.

### Phase 2: Create Redirect index.html

Replace `docs/index.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url=Relinquishment.html">
  <link rel="canonical" href="https://relinquishment.ai/Relinquishment.html">
  <title>RELINQUISHMENT — Wormholes in the Flat</title>
  <meta name="description" content="Real physics. A two-dimensional substrate in every chip and every magnetosphere. Three possibilities. You decide.">
  <meta property="og:title" content="RELINQUISHMENT — Wormholes in the Flat">
  <meta property="og:description" content="Real physics. Not metaphor. A two-dimensional substrate, a question nobody asked, and three possible explanations. You decide.">
  <meta property="og:image" content="https://relinquishment.ai/images/cover-triskellion.png">
  <meta property="og:url" content="https://relinquishment.ai">
  <meta property="og:type" content="book">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="favicon.ico">
</head>
<body>
  <p><a href="Relinquishment.html">RELINQUISHMENT — Wormholes in the Flat</a></p>
</body>
</html>
```

**Design notes:**
- `content="0"` — zero-second delay. Browser redirects before painting.
- `rel="canonical"` — tells search engines the real URL is the book, not the redirect.
- `og:type="book"` — correct schema type.
- `og:meta` tags — social media crawlers don't follow redirects; they scrape the target URL. These tags ensure shares of `relinquishment.ai` (the bare domain) still get proper previews.
- Fallback `<a>` link — the ~0.01% of users with meta-refresh disabled see a link.

**Preserve** `docs/index-live.html` as-is — it's a more elaborate landing page that may be useful later.

**Idempotency:** If `docs/index.html` contains `meta http-equiv="refresh"` — phase is applied.

### Phase 3: Backward Compatibility Redirect

Replace `docs/downloads/Relinquishment.html` (the 1.2 MB book copy) with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url=../Relinquishment.html">
  <link rel="canonical" href="https://relinquishment.ai/Relinquishment.html">
  <title>Moved — RELINQUISHMENT</title>
</head>
<body>
  <p>This page has moved. <a href="../Relinquishment.html">Read RELINQUISHMENT</a>.</p>
</body>
</html>
```

This file is NOT generated by the build. Create it manually and add a comment to the Makefile `html` target:

```makefile
# NOTE: docs/downloads/Relinquishment.html is a manual backward-compat redirect.
# The actual book is built to docs/Relinquishment.html (Plan 0300).
```

**Also update .gitignore:** Remove the line `!docs/downloads/Relinquishment.html` (the 1.2 MB build artifact is no longer there; the redirect file is tiny and should be tracked). Actually, the negation pattern still works — keep it. What matters is that the build no longer writes 1.2 MB there.

**Idempotency:** If `docs/downloads/Relinquishment.html` contains `meta http-equiv="refresh"` — phase is applied.

### Phase 4: Inject og:meta into Book HTML

Add a function to `build/preprocess.py`:

```python
def inject_og_meta(html_path):
    """Inject Open Graph meta tags into the book HTML for social sharing."""
    text = Path(html_path).read_text()
    if 'og:title' in text:
        return  # already present
    og_block = '''  <meta property="og:title" content="RELINQUISHMENT — Wormholes in the Flat">
  <meta property="og:description" content="Real physics. Not metaphor. A two-dimensional substrate, a question nobody asked, and three possible explanations. You decide.">
  <meta property="og:image" content="https://relinquishment.ai/images/cover-triskellion.png">
  <meta property="og:url" content="https://relinquishment.ai/Relinquishment.html">
  <meta property="og:type" content="book">
  <meta name="twitter:card" content="summary">
  <link rel="canonical" href="https://relinquishment.ai/Relinquishment.html">'''
    text = text.replace('</head>', og_block + '\n</head>', 1)
    Path(html_path).write_text(text)
```

Add call to `--fix-html` block (before `minify_html_assets`):

```python
        inject_og_meta(sys.argv[2])
```

**Rationale:** When someone shares a direct link to `relinquishment.ai/Relinquishment.html` on social media, they get proper preview cards. The canonical URL points to the book's permanent location.

**Idempotency:** Function checks for `og:title` before injecting.

### Phase 5: Update robots.txt + Create sitemap.xml

**robots.txt** — replace with:

```
User-agent: *
Allow: /
Disallow: /downloads/
Allow: /downloads/Relinquishment.pdf
```

The book is now at `/Relinquishment.html` (outside `/downloads/`), so no special Allow needed. Keep PDF discoverable for academic crawlers. Keep `/downloads/` generally blocked (tooltips, puzzles, eggs are internal tools).

**sitemap.xml** — create `docs/sitemap.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://relinquishment.ai/Relinquishment.html</loc>
    <priority>1.0</priority>
  </url>
</urlset>
```

One URL. The book. That's the site.

Add to `robots.txt`:

```
Sitemap: https://relinquishment.ai/sitemap.xml
```

**Idempotency:** If `docs/sitemap.xml` exists — skip creation. If `robots.txt` contains `Sitemap:` — skip update.

### Phase 6: Update Internal Links

**build/build-puzzles.py** line 594:
- Change `f'relinquishment.ai/downloads/Relinquishment.html#{pid}'`
- To `f'relinquishment.ai/Relinquishment.html#{pid}'`

**build/deep-links.yaml** line 29 (comment only):
- Change `https://relinquishment.ai/downloads/Relinquishment.html#{id}`
- To `https://relinquishment.ai/Relinquishment.html#{id}`

**docs/downloads/puzzles.html** — 16 hardcoded deep links:
- Replace all `relinquishment.ai/downloads/Relinquishment.html` with `relinquishment.ai/Relinquishment.html`
- Replace all `href="Relinquishment.html#` with `href="../Relinquishment.html#` (relative links from downloads/ dir)

**Note:** `puzzles.html` is regenerated by `make puzzles` / `python3 build/build-puzzles.py`. Fixing `build-puzzles.py` (line 594) fixes future builds. But also fix the current `docs/downloads/puzzles.html` so it works before the next full rebuild.

**docs/index-live.html** lines 56-58 — update download links:
- `downloads/Relinquishment.pdf` → unchanged (PDF stays in downloads/)
- `downloads/Relinquishment.epub` → unchanged (if EPUB ever added)
- `downloads/Relinquishment.html` → `Relinquishment.html`

**Idempotency:** If `build-puzzles.py` line 594 contains `relinquishment.ai/Relinquishment.html` (no `/downloads/`) — phase is applied.

### Phase 7: Add Download Links to Reader Nav

**File:** `build/reader.js`

The reader.js nav bar (injected into the book HTML) currently has a Tools link. Add PDF and ZIP download links.

Find the nav construction section (near line 278 where the tools link is created). Add adjacent links:

```javascript
const pdfLink = document.createElement('a');
pdfLink.href = 'downloads/Relinquishment.pdf';
pdfLink.textContent = 'PDF';
pdfLink.title = 'Download PDF';
pdfLink.style.cssText = 'margin-left:0.8em;font-size:0.85em;opacity:0.7;';

const zipLink = document.createElement('a');
zipLink.href = 'downloads/Relinquishment.zip';
zipLink.textContent = 'ZIP';
zipLink.title = 'Download ZIP (email-friendly)';
zipLink.style.cssText = 'margin-left:0.8em;font-size:0.85em;opacity:0.7;';
```

Append to nav after the tools link.

**Rationale:** Once the book IS the front page, the reader needs a way to get the offline formats. The nav bar is always visible. Small, unobtrusive links.

**Constraint:** The Generator must read the full reader.js nav construction to understand the exact insertion point. The above is schematic — actual implementation must match the existing code style.

**Idempotency:** If `reader.js` contains `Relinquishment.pdf` — phase is applied.

### Phase 8: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

Verification checklist:
- [ ] `docs/Relinquishment.html` exists (the book, ~1.2 MB)
- [ ] `docs/downloads/Relinquishment.html` is a redirect (~300 bytes, not 1.2 MB)
- [ ] `docs/index.html` contains meta-refresh to `Relinquishment.html`
- [ ] `docs/sitemap.xml` exists with correct URL
- [ ] `docs/robots.txt` has `Sitemap:` line and does NOT block the book
- [ ] `docs/downloads/Relinquishment.zip` contains the book (run `unzip -l` to verify)
- [ ] `docs/downloads/Relinquishment.pdf` exists
- [ ] `make dev` completes clean (no errors)
- [ ] `verify-deep-links.py` passes
- [ ] Book HTML has `og:title`, `og:image`, `og:url`, `rel="canonical"` in `<head>`
- [ ] `puzzles.html` deep links point to `relinquishment.ai/Relinquishment.html#...`
- [ ] `reader.js` nav has PDF and ZIP download links
- [ ] All internal `#id` anchors still work (they're within the same document, inherently stable)
- [ ] No regression in tools.html, gallery.html, 404.html

### Phase 9: Phone QC (Puppeteer)

Screenshot `docs/Relinquishment.html` at 375px width (iPhone SE viewport). Verify:
- Book title renders
- Reader nav is usable (not overlapping)
- Text is readable without horizontal scroll
- Track color bars visible
- PDF/ZIP links accessible

**This is a visual check only.** Use Puppeteer headless Chrome.

---

## Build Changes Summary

| File | Change |
|------|--------|
| `Makefile` (lines 74, 76, 77, 79) | Output path: `docs/downloads/` → `docs/` |
| `build/verify-deep-links.py` (line 15) | Read path: `docs/downloads/` → `docs/` |
| `build/preprocess.py` | Add `inject_og_meta()` function + call |
| `build/build-puzzles.py` (line 594) | URL: remove `/downloads/` from path |
| `build/deep-links.yaml` (line 29) | Comment: update URL pattern |
| `build/reader.js` | Add PDF/ZIP download links to nav |
| `docs/index.html` | Replace: stub → meta-refresh redirect |
| `docs/downloads/Relinquishment.html` | Replace: book → backward-compat redirect |
| `docs/robots.txt` | Update: allow PDF, add sitemap |
| `docs/sitemap.xml` | Create: one-URL sitemap |
| `docs/downloads/puzzles.html` | Update: 16 deep link paths |
| `docs/index-live.html` (line 58) | Update: HTML link path |
| `.gitignore` | Add `!docs/Relinquishment.html` |

---

## What This Plan Does NOT Do

- Does not flip the site live (that's a separate `git push` event)
- Does not create a separate summary/landing page (fracturing risk)
- Does not change the book's internal structure, content, or styling
- Does not touch the PDF or EPUB build paths
- Does not change the CNAME or DNS
- Does not modify the Relinquishment-draft.html redirect
- Does not add analytics or tracking (suppression-incompatible)

## Annealing Record

**Round 1 (MED): Does the meta-refresh actually work for SEO?**
Google's documentation (2024): "We recommend using server-side redirects when possible. If that's not possible, use a `<meta http-equiv="refresh">` tag with `content="0;..."`. We treat instant meta-refresh (content=0) similarly to a 301." GitHub Pages has no server-side redirect config. Meta-refresh with content=0 is the standard GitHub Pages solution. Confirmed: this is the correct approach.

**Round 2 (MED): Does the og:meta in index.html actually get scraped?**
Challenge: Social media crawlers (Facebook, Twitter, Slack) follow redirects before scraping. If index.html meta-refreshes to Relinquishment.html, they'll scrape Relinquishment.html's og:meta, not index.html's. So the og:meta in index.html is belt-and-suspenders — the real fix is Phase 4 (inject og:meta into the book HTML itself). Both are needed: index.html for the rare crawler that doesn't follow redirects, book HTML for all others. No conflict — they have the same content. Confirmed correct.

**Round 3 (LOW): Could moving the book break the ZIP?**
The ZIP is created by `zip -j downloads/$(JOBNAME).zip $(JOBNAME).html` from the `docs/` directory. The `-j` flag strips paths. So `Relinquishment.zip` contains `Relinquishment.html` — no path prefix. Unpacking the ZIP gives you `Relinquishment.html` in your current directory. Same as before. Confirmed: no regression.

**Round 4 (LOW): What about the root-level copy?**
Makefile line 77 copies the book to `$(JOBNAME).html` at repo root. This is excluded by `.gitignore` line 69 (`/Relinquishment*.html`). The root exclusion uses a leading `/`, so it only matches the repo root. The `docs/` copy needs `!docs/Relinquishment.html` to override the more general patterns. Wait — is there a general `Relinquishment.html` exclusion? Line 37: `Relinquishment.html` (no leading `/`). This matches ANYWHERE. The `!docs/downloads/Relinquishment.html` negation overrides it for that specific path. We need `!docs/Relinquishment.html` to negate it for the new location. Confirmed: Phase 1's .gitignore change is necessary and correct.

**Round 5 (LOW): Does puzzles.html break if the book moves before a rebuild?**
The 16 deep links in `puzzles.html` use relative `href="Relinquishment.html#..."` (no path prefix) — these are relative to the puzzles.html location in `docs/downloads/`. After the move, the book is at `docs/Relinquishment.html`, so puzzles needs `href="../Relinquishment.html#..."`. The full-URL display strings also need updating. Both are handled in Phase 6. If Phase 6 runs after Phase 1 (which it does by definition), no window of breakage. Confirmed: execution order is safe.

---

*Plan 0300 v1, written S67, 2026-05-06. Auditor: Argus.*
*Annealed: 5 rounds (MED MED LOW LOW LOW).*
