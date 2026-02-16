# Staging Pipeline — Raw Content Mining

**Purpose:** Organize Bruce's existing writing for inclusion in the book.

## Pipeline

```
raw/          → Bruce cleans/edits    → cleaned/       → Generator imports → manuscript/*.tex
(mined text)    (fact-check, voice)     (ready text)     (suture points)     (final)
```

## Idempotency

- `raw/` files are NEVER modified after creation. They are the permanent record of what was mined and from where.
- `cleaned/` files are copies that Bruce edits. The raw originals are preserved.
- When a cleaned file is imported into a .tex chapter, the staging file gets a `status: imported` flag — but is NOT deleted.

## File Format

Each file is named `posNN-slug.md` matching its target chapter. YAML front matter provides metadata:

```yaml
---
target_chapter: pos03-the-mentor
target_file: manuscript/track-2-testament/pos03-the-mentor.tex
pass: 1
track: Track 2 (Testament)
chapter_title: The Mentor
mined_date: 2026-02-15
status: raw          # raw → cleaned → imported
sources:
  - file: HEALER-RECONSTRUCTION.md
    lines: "48-72"
    section: "Intellectual Circle"
  - file: cloudCrypt/CC_book/biography_D_Lane.docx
    section: "full"
topics: [Healer, mentorship, SAS]
notes: |
  Editorial notes for Bruce.
---
```

## Source Locations

| Source | Path | Words | Format |
|--------|------|-------|--------|
| Master Reconstruction | `aurasys-memory/2026-02-13-session/HEALER-RECONSTRUCTION.md` | 24,544 | markdown |
| Red Team Analysis | `aurasys-memory/2026-02-13-session/RED-TEAM-ANALYSIS.md` | 4,883 | markdown |
| cloudCrypt archive | `aurasys-memory/2026-02-13-session/evidence/cloudCrypt/` | ~107K | .docx (extracted to /tmp) |
| Healer Book Evidence | `aurasys-memory/2025-11-15-session/HEALER-BOOK-EVIDENCE.md` | 1,621 | markdown |
| Bill Joy Narrative | `aurasys-memory/2025-11-15-session/BILL-JOY-NARRATIVE.md` | 1,049 | markdown |
| Verification Claims | `aurasys-memory/2025-11-15-session/HEALER-VERIFICATION-CLAIMS.md` | 3,142 | markdown |

## Status

Created: 2026-02-15 (Session 9)
Mining: In progress
