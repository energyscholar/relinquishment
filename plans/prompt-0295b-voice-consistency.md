You are the Generator.
**Repo:** ~/software/relinquishment/ (branch: main)
**Guard:** `grep "Authors' Note" manuscript/00-front/authors-note.tex` — if match, already applied, exit.
Read and execute Plan 0295 Part B: `~/software/relinquishment/plans/0295-bannon-feedback-corrections.md`
Voice consistency: singular "the/this author" → "we/Bruce/I" across ~19 files per convention table. Includes section headers ("The Authors' Position"), record-intro.tex, topic-guide.tex cross-refs. Run BOTH idempotency greps after — expect exactly 3 remaining (Tolkien, Joy, DMS header). One commit. Build with `make dev`, Puppeteer QC (check TOC "Authors' Note"), push to website.
