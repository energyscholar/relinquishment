You are the Generator.

**Repo:** ~/software/relinquishment/ (branch: main)

**Guard:** `grep "position:fixed" ~/software/relinquishment/build/reader.js | grep cover` — if match, already applied, exit.

Read and execute Plan 0294: `~/software/relinquishment/plans/0294-phone-ms-image-fixed-position.md`

Move MS image from nav child to document.body with position:fixed, bypassing backdrop-filter clipping. Revert overflow:visible. Build, Puppeteer QC both viewports, push.
