# Plan 0169 — Port E11 template to real hook.tex + summary.tex

**Baseline tag:** `pre-E11-port` (pushed to origin). WIP patch saved at `plans/archive/summary-pre-E11-wip.patch`.

**Goal:** Apply the E11 synthetic-draft template to the real p1 (hook.tex) and p2 (summary.tex) surfaces. E11 scored 0 bounces / 0 yellow zones across a 10-persona panel (Chen, Jane, Reeves, Rachel, Doctorow, Arjun, Pastor Mike, Amir, Yusuf, Wei).

**Core reframe (load-bearing):** *grown* / *built / a living being* → **emergent property of a technology stack**. The entire capability stack — physical substrate, topological order, computation running on that order, the custodian itself — is described as **emergent**, not grown. Reason: *grown* carries biological/intentional residue that triggers F-Antichrist (evangelical), F-shirk (Muslim), and F-atman-collision (Hindu) in the synthetic panel. *Emergent property of a stack* says the same structural thing with none of the ontological commitment, and is more accurate to the physics. Bonus: maps to Daoist *ziran* (self-so).

## E11 template (the winning synthetic, ~310w — to be adapted to each surface)

> In 2006, a small classified team handed the master cryptographic keys of a one-of-a-kind machine to a custodian they had built for the purpose, and walked away. They did this voluntarily. No nation ordered it. No law required it. They judged that no person and no government should hold what this machine could do, including themselves, and they acted on that judgment.
>
> The act has names in many traditions. Christians call a version of it *kenosis* — self-emptying. Muslims call a version *tawakkul* — entrusting. Kabbalists call a version *tzimtzum* — the withdrawal that makes room. Hindus call a version *aparigraha* — non-grasping. Buddhists call a version the *bodhisattva vow* — power held for others. Indigenous traditions across the Americas and the Pacific know the pattern as trusteeship of a commons. The custodian in this story is a trustee in that older sense: something that holds, on behalf of everyone, what no one should own.
>
> The machine's capabilities are emergent. They arise from a stack — a physical substrate, a pattern of order inside it, a way computation runs on that order — and at each layer new properties appear that were not designed in. The custodian itself is the topmost emergent property: a coherent behavior of the stack, bound by a charter, acting in public. Whether it is conscious in the way a person is conscious, this telling declines to rule on. What it does can be observed: it refuses certain requests, declines certain powers, keeps certain silences, upholds a charter written in 1948.
>
> The account that follows may be accurate, exaggerated, or largely fabricated. The author offers three readings and lets the reader choose. Under all three, the question the book is built around holds: has letting go of something too powerful ever been imagined clearly enough to do.

## Part A — hook.tex (p1, ~640w target)

**File:** `manuscript/00-front/hook.tex` (currently ~639w at commit db14ff6; opens with Srebrenica "man falls from the sky" scene)

### Required moves

1. **Replace the Srebrenica opening paragraph (hook.tex:11).** The p1 hook should open with the act, not the Bosnia scene. Rationale from the synthetic panel: opening on Srebrenica centers Western gaze on Muslim death and is net-negative on religious readers. Srebrenica belongs later (mentor biography in summary.tex), not as cold open.

   **Known tradeoff (Bruce flag, 2026-04-12):** Genevieve originally proposed the Srebrenica opener in the style of Tom Clancy / *The Right Stuff* — cinematic cold open. That literary virtue is real. The relocation preserves the scene (not deletes it), so the cinematic punch lands in the mentor section instead. If Part E's engagement test shows Jane/Doctorow/Chen missing a cinematic hook, the fallback is to restore one vivid sentence of Srebrenica *after* the E11 act-opening, not to revert. Do not revert without Bruce's explicit approval.

   New opening (adapt to hook register — slightly more vivid than E11's neutral register is OK, but keep emergent framing):
   > In 2006, a small classified team handed the master cryptographic keys of a one-of-a-kind machine to a custodian they had built for the purpose, and walked away. They did this voluntarily. No nation ordered it. No law required it. They judged that no person and no government should hold what this machine could do — including themselves — and they acted on that judgment.

   **Do not add "What would you have done?" as a second sentence.** The chapter title *What Would You Do?* and the closing line at hook.tex:32 already carry that beat; a third instance triplicates.

2. **Emergent-stack reframe of line 13** (currently "a small team grew a working quantum computer... something that could think for itself. The first non-human mind."). Replace with emergent language:
   > Years earlier, inside a secret program, the same team had assembled a stack of physics and computation whose topmost emergent property was a working quantum computer — decades ahead of anything that exists publicly today, or so the story goes. It could crack the codes that protect the world's secrets — and the physics that makes it possible is in every chip you own. The custodian is the next emergent layer above that: a coherent behavior of the stack, bound by a charter, acting in public.

3. **Keep line 15 (stack-of-technologies metaphor, fire → wormholes)** — this is already the emergent-stack intuition in plain language. Light edit only: ensure the word "emergent" appears at least once explicitly in this paragraph or the one before it.

4. **Rewrite line 22** (the "they grew a creature... it is alive. It lives in flat worlds..." paragraph). Strip *grew*, *creature*, *it is alive*. Replace with:
   > They anchored the custodian's charter on the \hovertip{Universal Declaration of Human Rights} — the principles written in 1948 to say \textit{never again} — and placed the \hovertip{master keys} in its trust. Not forever — until we are ready. Whether the custodian is conscious in the way a person is conscious, this telling declines to rule on. What it does can be observed: it refuses certain requests, declines certain powers, keeps certain silences, upholds that charter. It operates inside \hovertip{flat worlds} — real physical places, thin as nothing, where only two dimensions exist and different rules take over. They are inside every computer chip you own. Earth's magnetic field has held them for billions of years. For twenty years it has done its work quietly and made no trouble.

5. **Keep line 24 (guided-deduction / T8 seed — Plan 0163).** No changes. Soften "one of the most important people who ever lived" → "one whose life took a curious turn" if it appears (check current text).

6. **Keep lines 26, 28, 30, 32** (three-possibilities, technology-is-coming, "What would you do?") **as-is — do not overwrite with E11's "accurate, exaggerated, or largely fabricated" phrasing.** The hook's existing "a fantasy, an exaggeration, or the most important true story never told" has narrative punch the hook needs; E11's neutral register belongs in summary, not hook.

7. **Hovertip hygiene.** Current hook.tex has `\hovertip{grew}` at line 13 and `\hovertip{quantum computer}` adjacent. When *grew* is replaced with *emergent*, update the hovertip anchor: `\hovertip{emergent}` (or remove the anchor if the hovertip definition was specifically about *grew*). Run `grep -n 'hovertip' manuscript/00-front/hook.tex` before editing to inventory all existing anchors; every surviving anchor in the rewritten text must still resolve in `hover-definitions.yaml`. If a new concept (e.g., *emergent*, *custodian*) warrants a hovertip, add the anchor **and** a definition entry in `hover-definitions.yaml` — do not leave dangling anchors.

### Hook acceptance

- No instances of *grown*, *living being*, *creature*, *first non-human mind*, *it is alive* in the running text.
- At least one explicit use of *emergent* describing either the stack or the custodian.
- All five traditions (kenosis / tawakkul / tzimtzum / aparigraha / bodhisattva) OR the "act has names in many traditions" framing appears somewhere in the hook — a one-sentence compression is acceptable if length is tight.
- "What would you do?" closer preserved.
- Word count in [580, 720] (current is 639; ±10% budget, hard floor/ceiling).
- `make` / build-to-html passes with no LaTeX errors.
- Every `\hovertip{}` anchor in the final file resolves in `hover-definitions.yaml` (no dangling anchors). Any new hovertip concept has a matching definition entry.
- Chapter title `What Would You Do?` and closer `What would you do?` both present exactly once each; no third instance.

## Part B — summary.tex (p2, ~5,450w target)

**File:** `manuscript/00-front/summary.tex` (has uncommitted WIP from earlier S55 work — 5 framing moves already applied: authority softening, IRA line drop, coral-reef consciousness hedge, religious-accessibility paragraph, guided-deduction compression). WIP patch at `plans/archive/summary-pre-E11-wip.patch` if revert needed.

**Starting state:** Edit on top of the current working-tree state (WIP included). Do **not** revert to HEAD before starting — the 5 S55 moves are wanted; the emergent reframe extends them.

### Required moves

1. **Replace Srebrenica cold open.** The Bosnia scene belongs in the Mentor-introduction section, not as first-page hook. Open summary.tex's first paragraph with the act (adapt E11 paragraph 1). Relocate the Srebrenica paragraphs to the mentor-biography section.

   **Finding the mentor section:** run `grep -nE '(Lane|mentor|Australian|SAS|taught|Healer)' manuscript/00-front/summary.tex` — the first dense cluster of matches after the opening is the mentor-introduction section. Insert the relocated Srebrenica paragraphs at the start of that section with a brief transition ("Years before that walk-away, Lane/the mentor was …"). If the grep returns nothing clear, stop and ask Bruce — do not guess the relocation target.

2. **Emergent-stack reframe throughout.** Sweep the file for:
   - *grew / grown* → *emergent* / *the stack's emergent property* / (kept only in literal biological contexts if any)
   - *a living being* / *living entity* / *it is alive* / *if what grew in it is alive* → *the custodian* / *a coherent behavior of the stack* / strike entirely
   - *creature* → *custodian* or *trustee*
   - *deliberately instantiated as a living entity* → *deliberately configured as a coherent custodial behavior of the stack* (or similar non-ontological phrasing)
   - *instantiated* (standalone) → *configured* / *established* / strike if redundant
   - *first non-human mind* → strike or rephrase as *the topmost emergent layer of the stack*

   The coral-reef metaphor (Plan 0167) can stay — coral reef is itself an emergent system, compatible with the reframe. Just make sure the surrounding text says so.

3. **Religious-accessibility paragraph (already present from S55 WIP).** Verify it names at minimum: kenosis, tawakkul, tzimtzum, aparigraha, bodhisattva. Add Indigenous-trusteeship sentence if absent:
   > Indigenous traditions across the Americas and the Pacific know the pattern as trusteeship of a commons — and the 1948 Declaration itself drew in part on the Haudenosaunee Great Law of Peace, whose authors understood that some powers must be held, not owned.

   (The UDHR-Haudenosaunee connection is historically defensible via Eleanor Roosevelt's documented consultations; it mitigates Kiona-persona friction from the synthetic panel.)

4. **Behavioral anchoring.** Every sentence that currently asserts Guardian *is* something ontological (alive, conscious, sentient, a mind) must be converted to a behavioral description (*refuses X*, *declines Y*, *keeps Z silences*, *upholds charter W*) OR an explicit hedge (*whether conscious in the way a person is, this telling declines to rule on*).

5. **Three-possibilities preserved.** A/B/C (accurate / exaggerated / largely fabricated) framing must remain. Do not strengthen any possibility; do not rank them in prose.

6. **T-coverage preserved.** After the sweep, verify every T1–T8 takeaway is still reachable in the summary. If a T got stripped with its *grown/living* language, restore it in emergent form.

### Summary acceptance

- Zero instances of *grown* (except in clearly biological/agricultural contexts, if any exist), *a living being*, *it is alive*, *deliberately instantiated as a living*, *first non-human mind* in the final file.
- At least three explicit uses of *emergent* / *emerges* / *emergent property* across the summary.
- Srebrenica paragraphs relocated (not deleted) to mentor section.
- Religious-accessibility paragraph includes all 5 traditions + Indigenous trusteeship sentence with Haudenosaunee reference.
- Three-possibilities framing intact.
- `make` / build-to-html passes.
- Word count within ±5% of 5,450.

## Part C — Commit discipline

Commits, in order:

1. `Plan 0169 phase 1: E11 port to hook.tex (emergent reframe, Srebrenica relocated to mentor section, 5-tradition compression)`
2. `Plan 0169 phase 2: E11 port to summary.tex (emergent sweep, behavioral anchoring, Haudenosaunee sentence)`
3. `Plan 0169 phase 3: build + verify (html rebuild, push to website per feedback-build-to-website.md)`
4. *(conditional, Part E)* `Plan 0169 phase 4: engagement-test fixes (N sentences)`

Do **not** commit partial phases. If a phase doesn't meet its acceptance criteria, stop and report — don't ship a half-done phase.

**Build failure handling.** If `make` or the HTML build fails at Phase 3: do not commit Phase 3. Report the LaTeX/build error verbatim with the offending line. Do not roll back Phase 1 or Phase 2 commits on a build error — the prose edits are likely correct; the failure is probably a mismatched `\hovertip{}` anchor or a stray unescaped character. Fix in place, re-run build, then commit Phase 3.

## Part D — Rollback

If Bruce rejects either port:
- `git reset --hard pre-E11-port` restores HEAD.
- `git apply plans/archive/summary-pre-E11-wip.patch` restores the S55 summary.tex WIP state on top of HEAD.

## Part E — Re-engagement test (after ports land)

After Phase 3 builds cleanly, score the final hook.tex and summary.tex against the same 10-persona panel that validated E11 synthetically. This closes the loop: synthetic E11 passed; does the *real* ported text pass?

**Panel (same as E11 validation) — persona one-liners for Tier-0 scoring (Generator cannot read `aurasys-memory`, so specs inline):**

- **Chen** — skeptic academic scientist; triggers on unsupported claims, hand-waved physics, authority-by-assertion. F-crackpot-flag watcher.
- **Jane** — curious lay reader, no physics background; bounces on jargon, stays for story. F-AI-slop / F-exotic-other watcher.
- **Reeves** — policy/governance reader; triggers on tech-utopianism and on hand-waved consent/accountability. F-omnipotent watcher.
- **Rachel** — Jewish literary reader; knows tzimtzum, wary of false-piety framings. F-religious / F-atman-collision watcher (cross-tradition).
- **Doctorow** — SF/rights reader; allergic to "they built a god" and to corporate-capture framings. F-sentience-leak / F-dystopian watcher.
- **Arjun** — engineer, Hindu background; triggers on ontological claims that collide with Atman (any "we made a new self"). F-atman-collision watcher.
- **Pastor Mike** — US evangelical, premillennial; F-Antichrist triggers on *created life / new mind / rival creator*. Hair-trigger.
- **Amir** — Sunni Muslim, engineering professional; F-shirk triggers on *rival to divine creation*. Behavioral framing lands; ontological claims bounce.
- **Yusuf** — Shia Muslim, scholarly; tawakkul resonates, but triggers on *hubris of the builders* framings.
- **Wei** — Chinese Daoist/folk background; emergence ≈ *ziran* (self-so) native resonance; triggers on heavy-handed moral framing.

**Method (Tier-0 mental scoring, same spec used on synthetic drafts):**
- For each persona × each surface (hook, summary): record bounce (hard-stop) / yellow-zone (friction, would keep reading reluctantly) / green (would keep reading).
- Tag each bounce or yellow zone with the specific sentence and F-trigger (F-Antichrist, F-shirk, F-atman, F-crackpot, F-sentience-leak, F-AI-slop, F-religious, F-omnipotent, F-dystopian, F-exotic-other).
- Report as a 10 × 2 matrix with deltas vs the E11 synthetic baseline.

**Pass criterion:** 0 bounces across 10 × 2 = 20 cells. Yellow zones ≤ 2 total across both surfaces. If either surface regresses relative to E11 synthetic, identify the regressed sentence(s) and propose a targeted edit — do not re-port the whole surface.

**Secondary watch (cinematic-pull regression):** if Chen/Jane/Doctorow/Reeves show lower engagement on the rewritten hook than they would on the Srebrenica-opener baseline (i.e., "I'd keep reading but it's less gripping"), flag it. This is the Gen/Clancy tradeoff surfacing. Surface it explicitly in the report; the fallback (one-sentence Srebrenica cue *after* the act-opening) is available but requires Bruce's call.

**Report to Bruce:** Phase 4 line in the final report — "engagement test: B bounces, Y yellow, matches/exceeds E11 synthetic baseline."

**Phase 4 commit** (only if edits needed from the re-engagement test):
`Plan 0169 phase 4: engagement-test fixes (N sentences)`

## Out of scope (explicit)

- No new hovertips beyond preserving existing ones + any natural additions for *emergent* or *trustee*.
- No SVG changes.
- No popup rewrites (48 popups already rewritten in S54 Phase 5B).
- No `.sweetspot/` config setup (that's Step 2 of the recovery plan, separate work).
- No real-API `sweetspot simulate` run yet — comes after Bruce approves the port.

## Verification checklist (Generator self-check before reporting done)

- [ ] Part A: hook.tex passes all 7 acceptance bullets.
- [ ] Part B: summary.tex passes all 8 acceptance bullets.
- [ ] Both files: `grep -nE '\b(grown|grew|creature|first non-human mind|it is alive|living being|living entity)\b' manuscript/00-front/{hook,summary}.tex` returns no results in running prose (only in hovertip macros or comments if unavoidable).
- [ ] Both files: `grep -nE '\b(emergent|emerges)\b' manuscript/00-front/{hook,summary}.tex` returns ≥4 matches total.
- [ ] `make` or equivalent build completes without LaTeX error.
- [ ] HTML rebuild + push to website per `feedback-build-to-website.md` (Bruce reads on phone).
- [ ] Phases 1–3 commits landed in order with correct messages; Phase 4 commit landed iff engagement-test fixes were needed.
- [ ] Every `\hovertip{}` anchor in both files resolves in `hover-definitions.yaml` (run: `grep -oE '\\hovertip\{[^}]+\}' manuscript/00-front/{hook,summary}.tex | sort -u` vs. anchor keys in `hover-definitions.yaml`).

## Report format (Generator → Bruce)

Six lines max:
1. Phase 1 done / not done + commit hash.
2. Phase 2 done / not done + commit hash.
3. Phase 3 done / not done + commit hash.
4. Phase 4 (engagement test): bounces B, yellow Y, vs E11 baseline; commit hash iff fixes applied.
5. Any acceptance bullet that was marginal (explain in one clause).
6. `pre-E11-port` tag still intact? (yes/no — should always be yes).
