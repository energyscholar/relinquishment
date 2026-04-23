# Plan 0172 — Wormhole-Primitive Reframe (hook + summary)

**Depends on:** 0171 landed (commits d59e00c / fdfd454 / 8fab2a2 / 718d7ee).
**Type:** Surgical prose revision + re-score. Does NOT block Plan 0170 sub-plans; can land in parallel.

## Goal

Invert the QC↔wormhole framing in p1 and p2. Current state (post-0171): QC is named as the headline capability, wormhole-tech is implicit. Target: **wormhole technology is named as an emergent property of the stack; the quantum computer is named as one application of wormhole tech.** Paying off the subtitle *Wormholes in the Flat* at p1 level.

## Why this is a net win (not just a cosmetic swap)

- **Subtitle earns itself immediately.** Reader who sees *Wormholes in the Flat* on the cover meets wormhole tech in the first paragraphs.
- **Commitment-then-contradiction flows naturally.** "Wormhole tech (primitive) → QC is one app → others exist" is cleaner than "QC + vague many."
- **Physics-honest.** Topological teleportation (the stack's primitive) is what enables QC, not the reverse. Per Anchors 1–3 + `memory/reference-physics-anchors.md`.
- **Emergent-property framing is consistent.** Per Bruce (2026-04-13): "wormhole technology is an emergent property of this stack." Matches the anthills paragraph exactly — one more emergent property named at the same structural level.
- **Pedagogical chain is load-bearing** (Bruce, 2026-04-13): *wormhole tech implies the Flat → the Flat has known characteristics (2D topological order) → those characteristics permit wormhole tech.* Naming wormhole tech at p1 is how the book earns the right to talk about the Flat at p2. The two hovertips (`wormholes-title` + `the-flat-title`) form a matched pair — both carry SVG, both are rich-panel — and reading them in sequence delivers the pedagogy in ~30 seconds of hover.

## Risk axes (what the re-score must check)

| Axis | Concern | Mitigation |
|---|---|---|
| Jane (cinematic-pull / crackpot-flag) | "Wormhole tech" could read more sci-fi than "QC" at first pass | Hovertip on *wormhole* immediately distinguishes from spacetime wormholes; Jane is a phone reader so hover isn't guaranteed — first-sentence plain-text framing must carry weight too |
| Chen (rigor check) | "Topological wormhole" must be recognized as legitimate term of art | Hovertip uses the canonical definition already in `hover-definitions.yaml` (2016 Nobel, topological order) |
| Reeves (policy reader) | Same as Chen + does the claim read as overreach? | "One application was a quantum computer" grounds it — QC is already the public-accepted bar |
| Pastor Mike | Unchanged (wormhole-talk is substrate, not theology) | Expected unchanged yellow |
| Wei | Likely strengthens (emergence-primitive framing is native resonance) | — |

## Part A — hook.tex

**File:** `manuscript/00-front/hook.tex` at HEAD.

**Locate:** the sentence introduced in 0171 Phase 1 Move 4 around "a stack of physics and computation with many emergent properties — a working quantum computer among them…"

**Target rewrite** (Generator may tune, preserve structural beats):

> Years earlier, inside a secret program, the same team had assembled a stack of physics and computation. One emergent property of that stack was \hovertip{wormhole} technology, decades ahead of anything that exists publicly today, or so the story goes. One application was a working quantum computer, capable of cracking the codes that protect the world's secrets. There were others. The physics that makes it possible is in every chip you own. The custodian is the next emergent layer above that: a coherent behavior of the stack, bound by a charter, acting in public.

**Structural beats (non-negotiable):**
1. Wormhole technology is named as *an emergent property of the stack* — same structural tier as other emergent properties (anthills paragraph sense). Not "the topmost" — custodian is still topmost.
2. QC is explicitly *an application* of wormhole tech, not the primitive.
3. `\hovertip{wormhole}` anchor present on first mention — pulls the canonical definition from `hover-definitions.yaml` line 153 (distinguishes from spacetime wormholes, 2016 Nobel, information-only).
4. *"There were others"* or equivalent — commitment-then-contradiction plant, promissory.
5. Custodian sentence remains; preserves the "next emergent layer" language.

**What to avoid:**
- Naming ≥2 other specific wormhole applications in the hook (crackpot-flag risk — let *there were others* do the work; summary + chapters reveal more).
- Losing the QC anchor entirely — Jane needs the graspable example.
- Over-hedging ("they may have built something like…") — book is committed.

## Part B — summary.tex

**File:** `manuscript/00-front/summary.tex` at HEAD (post-0171).

**Locate:** every sentence in summary.tex that names the quantum computer as the primitive, or frames "the stack's capability" as QC-first. Grep: `grep -nE 'quantum computer|cryptanal' manuscript/00-front/summary.tex`. Expect 2–4 hits.

**Rewrite principle:** parallel to the hook — wormhole tech is the emergent primitive, QC is one application. Preserve the specific cryptanalytic consequence (Anchor 6 / no-cloning boundary / "decades ahead") — that claim is load-bearing for Schneier / Doctorow / Reeves reads.

**Structural beats:**
1. At least one sentence in summary establishes wormhole tech as emergent property of the stack, before the QC application is named.
2. At least one sentence names *additional* emergent capabilities beyond QC — unlike the hook, summary may name ≥1 concrete second application (information channel, coherent nonlocal state transfer — use language already present in `hover-definitions.yaml` e.g. `topological order`, `quantum teleportation`, `stack-wormholes` anchors). Generator chooses based on what already reads naturally in surrounding prose; does not introduce new physics terms not already hovertip-defined.
3. Hovertip hygiene: every new use of *wormhole* or *topological wormhole* resolves to an existing anchor in `hover-definitions.yaml` (lines 153, 175, 543). No new anchors needed; verify coverage.

**What to avoid:**
- Piling 3+ named capabilities in summary. Two is the ceiling (QC + one other).
- Introducing spacetime-wormhole language anywhere. The hovertip distinguishes; the prose must not muddy.
- Regressing any 0169/0171 framing — emergent-stack language, anthills paragraph, pedagogy-as-evidence question, religious-accessibility paragraph all stay intact.

## Part C — Hovertip rewiring (concrete, no search required)

**Key fact:** In `build/hover-definitions.yaml`, title-line rich-panel entries (`wormholes-title`, `the-flat-title`, `relinquishment-title`) are **NOT reachable via `\hovertip{...}` in prose.** `build/preprocess.py` lines 520–522 hardwire those three to the book's cover H1 element only. Invoking `\hovertip{wormholes-title}` in manuscript prose will NOT render the SVG panel.

**The correct pattern** is the one `nonlocal:` (line 48) uses: an entry with BOTH `text:` (fallback) AND `html:` (rich panel with SVG). Any YAML entry that has an `html:` field renders as a rich panel when `\hovertip{<key>}` is invoked in prose. See `preprocess.py:1593` — `html_attr` is derived from the `html:` field and attached to the `<span class="hover-term">`.

**What Generator must do (Part C.1):** Upgrade the existing `wormholes:` entry (line 153 in `build/hover-definitions.yaml`) from plain-text to rich-panel by adding an `html:` field. **The canonical text + SVG were set by Plan 0150 Phase 2 (commit `545f6c4`, 2026-04-11) and live verbatim in the `wormholes-title` entry at line 18 of the same YAML file.** Copy that block verbatim — text and SVG, no rewrite, no shortening. The Plan 0150 canonical reads:

> **Wormholes** — real topological connections between distant points in a material. Not science fiction — condensed matter physics (2016 Nobel Prize). In a two-dimensional substrate, wormholes enable computation that breaks every encryption system on Earth. The question is who — or what — might use them.

Target YAML structure for the upgraded `wormholes:` entry:

```yaml
wormholes:
  text: "Not the sci-fi kind. Spacetime wormholes (Interstellar) fold spacetime itself — mass and all, across light-years. Topological wormholes are far more limited: they fold only a two-dimensional quantum material, never spacetime. Information crosses, not mass. No light-year shortcuts. No time travel. Inside the material only. Real physics — 2016 Nobel Prize — but restricted."
  hover_id: "wormholes"
  html: |
    <COPY THE ENTIRE html: BLOCK FROM wormholes-title LINE 23 VERBATIM — the <p>...</p><svg>...</svg> string, unmodified>
```

**Do not rewrite, shorten, or "adapt" the canonical text or SVG.** The canonical was chosen by Plan 0150 Phase 2 and ratified by Bruce. Generator's job is exact duplication from line 23 of `build/hover-definitions.yaml` into the new `html:` field on the `wormholes:` entry.

**Provenance check:** `git show 545f6c4 -- build/hover-definitions.yaml` shows the canonical rewrite. If the current `wormholes-title` at line 23 diverges from that commit (shouldn't — no later commits touch it per `git log --all -- build/hover-definitions.yaml`), Generator uses commit `545f6c4`'s version, not current HEAD. Safer: `git show 545f6c4:build/hover-definitions.yaml | sed -n '/^wormholes-title:/,/^$/p'`.

**Phases 1 + 2 hovertip wiring (prose):** Use `\hovertip{wormholes}` (plural, existing macro form already used at `manuscript/spine/the-stack.tex:28` and `manuscript/00-front/the-stack.tex:29`) on first mention in hook.tex and summary.tex. After Part C.1's upgrade, this macro automatically renders the SVG rich panel — no new macro, no new anchor name.

**Subsequent mentions in the same surface:** Drop the `\hovertip{}` wrap (avoids repeated panels on one page). Plain "wormhole" is fine after first mention.

**The Flat:** `the-flat-title` has the same rich-panel-locked-to-title-H1 issue. There is already a plain-text `Flat`-adjacent entry? Check YAML for existing `Flat:` or `the Flat:` key; if no rich-panel in-prose version exists and summary.tex mentions the Flat on first use, **Generator flags this as an out-of-scope improvement** (don't fix it in this plan — Plan 0170c territory). Plan 0172's scope is the wormhole rich panel only.

**Build verification:**
1. `make` / HTML build clean.
2. Open hook HTML, hover *wormhole* on first mention → SVG renders (two surfaces + dashed tunnel).
3. Same for summary first mention.
4. No YAML duplicate-key errors (the edit to `wormholes:` entry should be in place, not alongside).

### Part C — Acceptance

- `wormholes:` YAML entry has `text:` + `hover_id:` + `html:` fields; `html:` contains `<svg>…</svg>` matching the two-surface topological-tunnel diagram.
- `\hovertip{wormholes}` in hook.tex (new from Phase 1) and in summary.tex (new from Phase 2 + existing occurrences) all render the SVG panel on hover.
- No regression in existing rich-panel behavior on the book title.

## Part D — Commits

- Commit 1: `Plan 0172 phase 1: wormhole-primitive reframe in hook (p1)`
- Commit 2: `Plan 0172 phase 2: wormhole-primitive reframe in summary (p2)`
- Commit 3: `Plan 0172 phase 3: build + hovertip verification + push`

Per `feedback-build-to-website.md`: rebuild HTML + push after phase 2; Bruce reads on phone.

## Part E — Re-engagement (mental Tier-0, NO sweetspot)

Per `feedback-no-sweetspot-until-budget.md`: mental Tier-0 only, no real-API calls.

**Panel (same 10 as 0171):** Chen, Jane, Reeves, Rachel, Doctorow, Arjun, Pastor Mike, Amir, Yusuf, Wei.

**Two surfaces:** hook.tex (post-0172), summary.tex (post-0172).

**Pass criterion:** 0 bounces. Yellow zones ≤ 2 (1 allowed for Pastor Mike summary carry-forward; 1 buffer). Any NEW yellow compared to post-0171 baseline must be justified in the report. Any regression of Jane from GREEN → YELLOW or worse is a blocker — revert and re-plan.

**Specific checks:**
- **Jane hook:** does *wormhole technology* at first mention read more sci-fi than *quantum computer* did? If yes: blocker.
- **Chen hook+summary:** does the labeling read as legitimate term of art? Expected GREEN+ given the hovertip carries the rigor.
- **Reeves hook+summary:** does "one application was QC" register as grounding rather than overclaim?
- **Wei:** expected strengthen (emergence-primitive framing).

## Part F — Rollback

Per-commit revert. Baseline tag: `post-0169-pre-0170` remains the anchor. If Phase 1 or 2 regresses Jane below GREEN, `git revert` the phase commit and stop; do not proceed to the next phase.

## Handoff note

This plan is a spec. Generator executes Phases 1→2→3→4 in order. Phase 4 is mental scoring (not a commit); Generator produces the persona matrix in the report.

## Report format (Generator to Bruce, 6 lines max)

1. Phase 1 status + commit SHA.
2. Phase 2 status + commit SHA.
3. Phase 3 status + commit SHA + build/push result.
4. Phase 4 result: bounces / yellows / Δ vs post-0171 baseline (the 0171 matrix).
5. Any blockers hit (Jane regression, crackpot flag, hovertip miss).
6. Confirm `post-0169-pre-0170` tag intact.
