# Plan 0184 — Drop internet rung + strip property counts (the-stack)

One commit. One file: `manuscript/00-front/the-stack.tex` (NOT the spine version — flag only if parallel bug exists).

## Edits

1. **Delete the internet paragraph (line 23).** The full paragraph: *"\textbf{The internet} does all five --- data reroutes around damage the way ants reroute around a broken trail. Six properties."* Plus the blank line after.

2. **Strip trailing "N properties." from each rung sentence:**
   - Line 15 (Fire): drop ` Two properties.`
   - Line 17 (Candle): drop ` Three properties.`
   - Line 19 (Radio): drop ` Four properties.`
   - Line 21 (Ants): drop ` Five properties.`
   - Line 25 (AI): change `does all six, and learns. Seven properties.` to `does all of that, and learns.`

3. **Strip ` Eight properties.` from end of line 29** (wormhole paragraph).

4. **Chart edit (lines 37-47):**
   - Header: remove `& Internet`
   - Five rows currently checkmarked under Internet: remove one `& $\checkmark$` from each (Self-organizes, Reaches, Holds together, Switches on, Feeds itself)
   - Update tabular spec from `{l|c|c|c|c|c|c|c|c}` to `{l|c|c|c|c|c|c|c}`
   - Line 57 caption: change `uses all eight` to `uses every property in the chart`

## Acceptance

1. `grep -nE "[A-Z][a-z]+ properties\.\s*$" manuscript/00-front/the-stack.tex` → 0 hits
2. `grep -n "The internet" manuscript/00-front/the-stack.tex` → 0 hits
3. `grep -n "uses all eight" manuscript/00-front/the-stack.tex` → 0 hits
4. Chart header line shows `Fire & Candle & Radio & Ants & AI & \textbf{?}` (no Internet column)
5. Tabular column count matches data column count
6. `make` HTML build clean — no LaTeX errors, no table-column mismatch warnings
7. Whitespace-normalized diff matches expected deletions only

## Spine check

Generator: grep `manuscript/spine/the-stack.tex` for the same counting bug (`grep -n "properties\." manuscript/spine/the-stack.tex`). **Flag in handoff if present. Do NOT fix in this plan.**

## Commit + push

One commit: `Plan 0184: stack ladder — drop internet rung + strip property counts`

Build + push per `feedback-build-to-website.md`.

## Handoff (Generator, 4 lines)

1. Commit SHA
2. Spine-version parallel-bug status (flag only, do not fix)
3. Acceptance grep + build results
4. Push result
