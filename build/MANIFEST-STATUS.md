# Manifest status — 2026-11-16

What each registry in `build/` describes, when it was last regenerated, and whether it can be refreshed without a full book build. Inventory pass only; no content changed.

| File | Describes | Regenerate with | State 2026-11-16 |
|---|---|---|---|
| `manifest.json` | every `.tex/.sty/.cls` under `manuscript/` and `build/` | `make manifest` | **refreshed** — 263 files (was 34, dated 2026-02-15, listing files that no longer exist) |
| `svg-manifest.json` | inline SVG assets with `fig-` deep-link ids | `make svg-sheet` (needs an HTML build) | not refreshed; needs a build |
| `gallery-manifest.yaml` | 46 SVG entries; status live / hover / approved / draft / planned / deferred | hand | 41 live · 1 draft · 4 deferred |
| `image-manifest.yaml` | inline SVGs grouped by inject function | hand | unchanged |
| `puzzle-data.yaml` / `puzzle-tracker.yaml` | puzzle content / puzzle metadata | hand | 26 puzzles |
| `puzzle-status.txt` | derived summary of the two above | `make puzzles` (writes `docs/downloads/puzzles.html` too) | last regenerated 2026-04-28: 26 total, 23 approved, 16 installed; types `sim`, `ord/tower`, `mat`, `km`, `cip`, `ba` not yet rendered |
| `easter-egg-manifest.yaml` | egg pages: slug, source, status, deep link | hand | unchanged |
| `deep-links.yaml` | master registry of addressable anchors | hand | 59 `dl:` ids |
| `hover-definitions.yaml` | onHover term definitions (HTML tooltips + PDF footnotes) | hand | 64 terms |
| `chapter-hover-descriptions.yaml`, `menu-tooltips.yaml`, `concept-glyphs.yaml`, `tech-collapse.yaml` | UI text registries | hand | unchanged |
| `orphan-report.md` | authored-but-unapplied content | hand (Plan 0196) | lists 48 unreachable `.tex`; not re-run |
| `review-artifacts.yaml` | temporary preview pages | hand | unchanged |

## Notes

- `docs/Relinquishment.html` (1.76 MB) is the live reader. `docs/index.html` and `docs/downloads/Relinquishment.html` redirect to it; the book is the website.
- The repository root holds generated outputs (`abstracts-standalone-v*.txt`, `Relinquishment.{aux,bbl,...}`, `node_modules`) that the README's Root Policy does not list; nine `abstracts-standalone-v*.txt` files are tracked.
- Last content commit: 2026-08-16 (nav support button); last literary revision: 2026-06-22.
