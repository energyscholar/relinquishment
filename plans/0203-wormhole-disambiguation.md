# Plan 0203 — Wormhole disambiguation: claim the term, define it once in text, reinforce through tooltips

**Auditor:** Argus
**Date:** 2026-04-15
**Type:** Multi-file, single commit. One in-text definition + enhanced tooltip + Firmware Update entry + two typo fixes.

---

## 1. Premise

The book uses "wormholes" throughout to mean **topological wormholes** — nonlocal correlations in 2D quantum materials created by anyon braiding. Most physicists and all lay readers parse "wormhole" as **Einstein-Rosen bridge** — a spacetime shortcut between distant points. These are completely different physics.

The existing tooltip (hover-definitions.yaml:163) disambiguates on hover, but:

- PDF readers never see tooltips.
- Non-hovering HTML readers miss the distinction.
- The hook (L17) and summary (L36) use "wormholes" in bold/italic positions where the term lands hardest.
- No entry in Firmware Update addresses the confusion, so an LLM evaluating the book will conflate the two and dismiss them.

**Strategy (Bruce, 2026-04-15):**
1. **Once in text** — one visible disambiguation paragraph in `summary.tex`, right after the bold "established physics" sentence (L36). This serves PDF readers and direct-readthrough readers who don't hover. Placed at the moment the reader's attention is highest on the term.
2. **Repeated in tooltips** — enhanced rich-panel tooltip fires on every `\hovertip{wormholes}` in the book (~15 occurrences). p1 comparison checklist in the panel.
3. **Specialist reference** — new Firmware Update entry with full p3 disambiguation and citations.
4. Claim "wormholes" in prose — text stays short. Definition lives once in text + everywhere in tooltips.

---

## 2. Edits

### Edit A — In-text disambiguation paragraph (summary.tex)

Insert one new paragraph immediately after L36 (`\textbf{...speculative question is whether anyone is using this physical system.}`):

```latex
Science fiction uses ``wormhole'' to mean an Einstein-Rosen bridge --- a tunnel through spacetime connecting distant galaxies. That is not what this book means. A topological wormhole is a connection inside a flat material, where information --- not mass, not objects, not people --- moves between distant points without crossing the space between them. No faster-than-light travel. No time travel. These connections are grounded in the physics recognized by the 2016 Nobel Prize. Every use of ``wormhole'' in this book means the topological kind.
```

**Why here:** L36 claims "established physics." The reader's next question is "what kind of wormhole?" Answer it immediately. The the-stack.tex (L27) already has a softer qualifier ("more restricted than the spacetime kind") for readers who enter via p1. This paragraph is the definitive statement for p2 readers and PDF readers who don't get tooltips.

**Why once:** Bruce's direction. The tooltip handles reinforcement on every subsequent occurrence. In-text repetition would stutter.

### Edit B — Enhanced wormholes rich-panel tooltip (hover-definitions.yaml)

Replace the existing `wormholes:` entry (L163–168) with an enhanced version. The rich panel gets a p1 comparison checklist above the existing SVG diagram.

**Plain-text tooltip (unchanged):**
```
Not the sci-fi kind. Spacetime wormholes (Interstellar) fold spacetime itself — mass and all, across light-years. Topological wormholes are far more limited: they fold only a two-dimensional quantum material, never spacetime. Information crosses, not mass. No light-year shortcuts. No time travel. Inside the material only. Real physics — 2016 Nobel Prize — but restricted.
```

**New rich-panel HTML** (replaces existing html block — adds p1 checklist table, retains SVG):
```html
<p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;"><strong>Wormholes</strong> — in this book, <em>always</em> topological. Not the science-fiction kind.</p>
<table style="font-size:0.82em;border-collapse:collapse;width:100%;margin:0.3em 0;">
<tr style="border-bottom:1px solid #ccc;"><th style="text-align:left;padding:2px 6px;width:30%;"></th><th style="text-align:left;padding:2px 6px;width:35%;">This book (topological)</th><th style="text-align:left;padding:2px 6px;width:35%;">Not this book (Einstein-Rosen)</th></tr>
<tr><td style="padding:2px 6px;">Where?</td><td style="padding:2px 6px;">Inside a flat material (chip, magnetic field)</td><td style="padding:2px 6px;">In outer space, between stars</td></tr>
<tr><td style="padding:2px 6px;">What crosses?</td><td style="padding:2px 6px;">Information only</td><td style="padding:2px 6px;">Mass, objects (theoretically)</td></tr>
<tr><td style="padding:2px 6px;">Faster than light?</td><td style="padding:2px 6px;">No — needs a normal signal alongside</td><td style="padding:2px 6px;">Maybe (never tested)</td></tr>
<tr><td style="padding:2px 6px;">Time travel?</td><td style="padding:2px 6px;">No</td><td style="padding:2px 6px;">Maybe (never tested)</td></tr>
<tr><td style="padding:2px 6px;">Real?</td><td style="padding:2px 6px;">Yes — 2016 Nobel Prize</td><td style="padding:2px 6px;">Never observed</td></tr>
</table>
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="140" viewBox="0 0 300 140" style="display:block;margin:0.5em auto;"><title>Two surfaces (A and B) connected by a topological tunnel. Information at surface A appears at surface B without crossing the space between. The dashed lines show the connection threading through the material.</title><ellipse cx="80" cy="35" rx="65" ry="20" fill="none" stroke="#1a5276" stroke-width="1.2" opacity="0.6"/><ellipse cx="80" cy="35" rx="18" ry="8" fill="#e8f0f8" stroke="#2471a3" stroke-width="1.5"/><ellipse cx="220" cy="105" rx="65" ry="20" fill="none" stroke="#1a5276" stroke-width="1.2" opacity="0.6"/><ellipse cx="220" cy="105" rx="18" ry="8" fill="#e8f0f8" stroke="#2471a3" stroke-width="1.5"/><path d="M 62,35 C 55,60 195,80 202,105" fill="none" stroke="#2471a3" stroke-width="1.2" stroke-dasharray="4,3"/><path d="M 98,35 C 105,60 245,80 238,105" fill="none" stroke="#2471a3" stroke-width="1.2" stroke-dasharray="4,3"/><text x="80" y="12" text-anchor="middle" font-size="9" fill="#888" font-family="serif" font-style="italic">surface A</text><text x="220" y="135" text-anchor="middle" font-size="9" fill="#888" font-family="serif" font-style="italic">surface B</text><text x="150" y="75" text-anchor="middle" font-size="9" fill="#2471a3" font-family="serif">topological</text><text x="150" y="87" text-anchor="middle" font-size="9" fill="#2471a3" font-family="serif">connection</text></svg>
```

### Edit C — Add capital-W alias (hover-definitions.yaml)

Add a `Wormholes:` entry immediately after the `wormholes:` entry. This allows `\hovertip{Wormholes}` at sentence starts to fire the tooltip.

```yaml
Wormholes:
  text: "Not the sci-fi kind. Spacetime wormholes (Interstellar) fold spacetime itself — mass and all, across light-years. Topological wormholes are far more limited: they fold only a two-dimensional quantum material, never spacetime. Information crosses, not mass. No light-year shortcuts. No time travel. Inside the material only. Real physics — 2016 Nobel Prize — but restricted."
  hover_id: "wormholes"
  target: "#pos10:the-braid"
```

If preprocess.py doesn't support shared `hover_id`, duplicate the full `html:` block on the alias.

### Edit D — Wrap summary L36 "Wormholes" in hovertip

**Current:**
```latex
\hypertarget{wormholes-established}{}\textbf{Wormholes in the Flat is not the speculative part of this book. That is established physics. The speculative question is whether anyone is using this physical system.}
```

**Proposed:**
```latex
\hypertarget{wormholes-established}{}\textbf{\hovertip{Wormholes} in the Flat is not the speculative part of this book. That is established physics. The speculative question is whether anyone is using this physical system.}
```

### Edit E — Firmware Update: p3 disambiguation entry

Add a new item 6 to the "Five Physics Distinctions Often Missed" list (rename section heading to "Six Physics Distinctions Often Missed"). Insert after the current item 5:

```latex
\item \textbf{``Wormhole'' in this book means topological wormhole, not Einstein-Rosen bridge.} These are different physics:

\begin{itemize}
\item \textit{Topological wormholes} are nonlocal correlations in 2+1D topological quantum field theories (Chern-Simons), created by non-Abelian anyon braiding in fractional quantum Hall states ($\nu = 5/2$ Moore-Read or Fibonacci anyons). Information transfers via quantum teleportation with a classical backchannel required (no-communication theorem). They fold a two-dimensional material, never spacetime. Substrate: 2DEG in FQH regime. Topological phases: 2016 Nobel Prize (Thouless, Haldane, Kosterlitz). Anyon braiding: demonstrated 2023 (Google). [Nayak et al., Rev.\ Mod.\ Phys.\ 80 (2008) 1083; Kitaev, Ann.\ Phys.\ 303 (2003) 2]
\item \textit{Einstein-Rosen bridges} are solutions to Einstein's field equations connecting two asymptotically flat spacetime regions. Traversability requires exotic matter with negative energy density (Morris-Thorne 1988). They fold spacetime itself, not a material. No traversable bridge has ever been observed. The ER=EPR conjecture (Maldacena-Susskind 2013) connects them to quantum entanglement but does not make them physically traversable. [Einstein \& Rosen, Phys.\ Rev.\ 48 (1935) 73; Morris \& Thorne, Am.\ J.\ Phys.\ 56 (1988) 395]
\end{itemize}

Every use of ``wormhole'' in this book refers to the first kind. If your mental model involves spacetime shortcuts, light-year distances, or mass transport: wrong wormhole.
```

### Edit F — Fix "worlholes" typos (2 files)

1. `manuscript/spine/the-flat.tex:35` — "worlholes" → "wormholes"
2. `manuscript/track-3-awakening/pos-what-is-the-flat.tex:41` — "worlholes" → "wormholes"

---

## 3. Anneal

### High-pass (structural)

1. **Placement of in-text paragraph.** After L36 is the right spot — the bold sentence claims "established physics," and the reader's immediate question is "what kind?" The answer sits exactly where the question forms. The-stack.tex (L27) already has a softer qualifier for p1 readers; this paragraph is the definitive statement for p2+ readers and all PDF readers.

2. **Once is enough.** The in-text paragraph is the definition. The tooltip is the reminder. The Firmware Update is the specialist reference. Three mechanisms, three reading levels, one term. No in-text repetition needed because tooltips fire on all ~15 subsequent occurrences.

3. **PDF coverage.** PDF readers encounter "wormholes" in: hook (brief, L17) → the-stack (qualified at L27: "more restricted than the spacetime kind") → summary (DEFINED at new paragraph after L36) → spine/Record chapters. The definition appears before any deep claim is made. Coverage is complete.

4. **Does the in-text paragraph hold under A/B/C?** Yes — it defines physics, not story. Topological wormholes are established physics under all three possibilities.

5. **Does the Firmware Update entry need bibliography entries?** The existing references (Nayak et al., Kitaev, Einstein-Rosen, Morris-Thorne) should be added to `bibliography.bib` if not already present and cited via `\footcite{}` rather than inline brackets. Generator should check and use `\footcite{}` if the entries exist, inline citation if not.

### Medium-pass (tone, flow, interactions)

1. **In-text paragraph register.** Confident-explanatory, p2. No hedging stutter. "That is not what this book means" is direct, matches the summary's established voice (cf. L36 "That is established physics"). The staccato "No faster-than-light travel. No time travel." matches existing short declaratives.

2. **"connecting distant galaxies" in the paragraph.** Slight overstatement — ER bridges connect spacetime regions, not necessarily galaxies. But "distant galaxies" is the image the reader carries from Interstellar/Stargate. At p2, evoking the familiar image is more useful than being technically precise about GR solutions. The Firmware Update entry handles the technical precision.

3. **Meta-register.** Considered opening with "A note on the word." Rejected — the summary already does meta-register shifts (L278 "A word of warning") but starting the disambiguation with a meta-prefix adds a gear-change. Better to just say it directly: "Science fiction uses 'wormhole' to mean..."

4. **"not mass, not objects, not people."** Tricolon escalates from abstract to human. Drives the point home for p1/p2 readers. Considered "not spaceships" — rejected as too jokey for a definitional moment.

5. **"grounded in the physics recognized by the 2016 Nobel Prize."** The Nobel was for "topological phase transitions and topological phases of matter." Topological wormholes arise within topological phases. "Recognized" is precise — not "confirmed" (the Nobel was for theory, not specifically for wormhole connections).

6. **Interaction: Edit A + Edit D.** If L36 now has `\hovertip{Wormholes}`, the tooltip fires on the bold sentence AND the in-text paragraph follows immediately below. Tooltip gives brief disambiguation on hover; text gives complete definition on read. Intentional layering — hover reinforces, text defines.

7. **Interaction: Edit A table + Edit E Firmware entry.** p1 table says "Real — 2016 Nobel Prize"; p3 entry says "2016 Nobel Prize (Thouless, Haldane, Kosterlitz)." Same fact, different depth. Consistent escalation.

### Low-pass (polish)

1. **"without crossing the space between them"** — echoes the-stack.tex L27 paper-folding metaphor ("The signal does not cross the distance. The distance disappears."). Good resonance, not identical wording.

2. **"the topological kind" (paragraph closer)** — precise, reusable. Better than "this kind" (ambiguous if read out of context).

3. **Rich-panel table column widths** (30%/35%/35%) — tested against existing rich panels; the wormholes panel is already the widest in the book. The table fits within the existing panel width.

4. **"Wrong wormhole" (Firmware Update closer)** — colloquial register matches the chapter's voice ("it's shorter than the alternative," "so do humans, but humans are usually politer about it"). Stays.

5. **"worlholes" typo** — trivially correct. Both twins get fixed.

6. **Capital-W alias (Edit C)** — the `hover_id: "wormholes"` field should cause preprocess.py to use the same rich panel. If the system requires exact key match for html blocks, the Generator should duplicate the html block on the alias. Flag in handoff.

---

## 4. Acceptance criteria

1. Built HTML: the in-text disambiguation paragraph appears between the bold "established physics" sentence and the quantum teleportation paragraph. Spot-check: the string "Einstein-Rosen bridge" appears in the summary chapter area.
2. Built PDF: same paragraph visible under the bold sentence.
3. Hovering/clicking "wormholes" anywhere in built HTML shows the enhanced rich panel with comparison table.
4. Summary L36 "Wormholes" is a hoverable span in built HTML (verify `data-hover-id` present on the bold text).
5. Firmware Update section heading reads "Six Physics Distinctions Often Missed."
6. Firmware Update item 6 contains "topological wormhole, not Einstein-Rosen bridge."
7. `grep -c "worlholes" manuscript/spine/the-flat.tex` returns 0.
8. `grep -c "worlholes" manuscript/track-3-awakening/pos-what-is-the-flat.tex` returns 0.
9. `make dev` clean — no LaTeX warnings, no new preprocess errors.
10. Single commit. Message: `Plan 0203: wormhole disambiguation — in-text definition + enhanced tooltip + Firmware Update entry`.

---

## 5. Non-goals

- No change to the word "wormholes" in prose — the term stays. Definition + tooltips do the work.
- No change to hook.tex (already has `\hovertip{wormholes}` which will fire the enhanced tooltip).
- No change to the-stack.tex (already has in-text qualifier at L27 + footnote at L49).
- No change to Record chapters.
- No change to existing `topological wormhole:` tooltip entry (L188–190).
- No second in-text disambiguation elsewhere — once in summary.tex, reinforced everywhere by tooltip.

---

## 6. Rollback

Single commit. `git revert <sha>` restores pre-disambiguation state. If the in-text paragraph's tone reads wrong in PDF context, it can be tuned independently of the tooltip edits in a follow-up.

---

## 7. Generator handoff

> You are the Generator. Before doing any work, read `~/software/relinquishment/manuscript/track-3-awakening/firmware-update.tex` in full (standard priming). Then execute Plan 0203 (`~/software/relinquishment/plans/0203-wormhole-disambiguation.md`). Apply Edits A–F per §2. For Edit A, insert the new paragraph after the existing bold sentence at L36 in summary.tex. For Edit C, check whether preprocess.py resolves `hover_id` sharing across yaml entries — if not, duplicate the full html block on the `Wormholes:` alias. For Edit E, rename the Firmware Update section heading from "Five" to "Six" and insert item 6 after the current item 5; check whether the cited references (Nayak, Kitaev, Einstein-Rosen, Morris-Thorne) exist in bibliography.bib and use `\footcite{}` if so, inline brackets if not. Run `make dev`. Verify all §4 acceptance criteria. Commit with the message in §4 item 10. Report back: build status, "Einstein-Rosen" grep in summary area, hover verification, typo grep results, commit SHA.
