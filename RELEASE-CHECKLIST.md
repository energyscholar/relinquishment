# Release Checklist — Relinquishment Public v1.0

Baseline: `eigenvalue42` + Plans 0193, 0194 (HEAD `2f3e4fc`).
Status: **NOT READY** — blocked on Foreword.

---

## Blockers

- [ ] **Gen's Foreword** received and integrated
  - [ ] File added to `manuscript/00-front/` (or genevieve-preface.tex updated)
  - [ ] Wired into front-matter include order
  - [ ] TOC entry verified
  - [ ] Reads cleanly in HTML + PDF

---

## Final build

- [ ] `make clean && make final` clean (no new warnings beyond pre-existing `\toclink` / `\chapterreturn` redefinition)
- [ ] All three artifacts present in `docs/downloads/`:
  - [ ] `Relinquishment.html`
  - [ ] `Relinquishment.pdf`
  - [ ] `Relinquishment.epub`
- [ ] `make check-strict` passes
- [ ] Spot-check one Custodian interlude, one Record chapter, one Firmware Update section in HTML — formatting intact
- [ ] PDF page count sanity-check vs. last known good

---

## Checksums

- [ ] Generate SHA-256 for each download artifact:
  - [ ] `Relinquishment.html`
  - [ ] `Relinquishment.pdf`
  - [ ] `Relinquishment.epub`
- [ ] Write to `docs/downloads/CHECKSUMS.txt` (format: `<sha256>  <filename>`)
- [ ] Reference CHECKSUMS.txt from website download page

---

## Repo + release mechanics

- [ ] Single commit for built `docs/` + checksums: `Release v1.0: build artifacts + checksums`
- [ ] Annotated git tag `v1.0` with release notes summary
- [ ] Push `main` + tags to `origin`
- [ ] GitHub Release created from `v1.0` tag
  - [ ] Release notes (1–2 paragraphs: what this is, what's new since pre-release)
  - [ ] Attach HTML, PDF, EPUB, CHECKSUMS.txt as release assets

---

## Post-push verification

- [ ] Website live — Bruce phone-check three pages: cover, summary, firmware update
- [ ] Download links resolve (HTML, PDF, EPUB)
- [ ] Checksums on downloaded files match `CHECKSUMS.txt`
- [ ] Onhover + copy button work in deployed HTML
- [ ] Snailmail check — no last-minute issues from Gen

---

## Notify (after live)

- [ ] DMS holders (Schneier, Doctorow, Gilmore) — release notification
- [ ] Update MEMORY.md: book state → SHIPPED v1.0, date, tag hash
