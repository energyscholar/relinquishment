You are the Generator.

**Repo:** ~/software/relinquishment/ (branch: main)
**Guard:** `grep "dilution refrigerator" manuscript/appendix/abstracts.tex` — if match, already applied, exit.

Read and execute Plan 0296: `~/software/relinquishment/plans/0296-spiral-abstract-consistency.md`

Two edits to `manuscript/appendix/abstracts.tex`: (1) SA V title + body rewrite — room-temperature → cryogenic production with dilution refrigerator details; (2) SA III attribution — "Physical Review [Classified] (Letters)" → "[Internal Team Document --- Not Reported to Program Management]". One commit: `Fix SA V/III: DARPA production was cryogenic, thermal ladder concealed`. Build with `make dev`, Puppeteer QC SA V and SA III in HTML, push to website.
