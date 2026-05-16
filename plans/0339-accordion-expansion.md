# Plan 0339: Accordion Expansion — GA Speed Pass

**Status:** Ready for Generator
**Files:** `build/tech-collapse.yaml`
**Problem:** GA reader must wade through ~700 lines of uncollapsed technical/analytical prose before reaching The Record. Target: ~300 lines visible, everything else behind tooltips.
**Objective:** GA reader can finish The Flat in one sitting using collapsed-view + tooltips, absorb all T/F engineering at p2.5, see Custodian interludes, arrive at The Record ready to read it like a novel.
**Auditor:** Argus, S81

---

## Context for Generator

Read `build/tech-collapse.yaml` — that's the ONLY file you modify. Add new entries. Do not remove or modify existing entries except changing "Not Isolated" from `GA-FRIENDLY` to `BORDERLINE`.

The collapse system works:
- `assessment: GA-AVERSE` → default CLOSED (reader must click to expand)
- `assessment: BORDERLINE` → default OPEN but collapsible (reader can close it)
- Tooltip shows on hover over collapsed title bar
- Concept symbols (⬡ ◈ ◉ ⊘ ⚙ ⎈ ⊞) can appear in tooltips

**Tooltip design principles:**
1. Tell the reader what they'd know if they read it (key takeaway)
2. Use concept symbols to signal domain: ⬡=Flat, ◈=emergence, ◉=Custodian, ⊘=silence, ⚙=capabilities, ⎈=stewardship, ⊞=services
3. Keep short (under 60 words)
4. Implicit difficulty signal: if the tooltip uses multiple symbols or mentions "published physics" → harder section

## Phase 1: Fix "Not Isolated" (GA-FRIENDLY → BORDERLINE)

Change existing entry:
```yaml
  - title: "Not Isolated"
    ...
    assessment: BORDERLINE    # was GA-FRIENDLY — defaults open, still collapsible
```

## Phase 2: New Collapses — The Code War

Add after the existing Factoring Game entries:

```yaml
  # ── THE CODE WAR ──────────────────────────────────────────────────────

  - title: "What the Movie Didn't Tell You"
    spine_file: manuscript/spine/the-code-war.tex
    spine_label: "spine:cw-what-the-movie-didnt-tell-you"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⚙ During WWII, 10,000 people at Bletchley Park broke enemy encryption and kept the secret for 30 years. Knowledge walks out in minds, not in machines. This pattern repeats."
    status: approved

  - title: "The Dual-Use Pattern"
    spine_file: manuscript/spine/the-code-war.tex
    spine_label: "spine:cw-the-dual-use-pattern"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⚙ Every powerful technology enables both protection and attack. The same encryption guarding your bank account hides criminals. Quantum computation has the same duality — and the same agencies care about both sides."
    status: approved
```

## Phase 3: New Collapses — Scientific Revolutions

Add after the existing GROWING A MIND section (after "Morphogenesis as Computation") and before THE DEMO section:

```yaml
  # ── SCIENTIFIC REVOLUTIONS ────────────────────────────────────────────

  - title: "The Current Paradigm"
    spine_file: manuscript/spine/scientific-revolutions.tex
    spine_label: "spine:sr-current-paradigm"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⊘ Normal science has no category for what this book describes. The question crosses five fields; no single field owns it. Not a gap in evidence — a gap in institutional structure."
    status: approved

  - title: "Anomaly Accumulation"
    spine_file: manuscript/spine/scientific-revolutions.tex
    spine_label: "spine:sr-anomaly-accumulation"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⊘ Fourteen published observations that don't fit the current paradigm — room-temperature coherence, unexplained magnetospheric structure, plasma topology. None proves anything alone. Together they form a pattern."
    status: approved

  - title: "Life in the Flat"
    spine_file: manuscript/spine/scientific-revolutions.tex
    spine_label: "spine:sr-life-in-the-flat"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⬡ ◈ What current science says about life in two-dimensional substrates: nothing. Not 'nothing lives there' — nothing has been said. The question has not been asked."
    status: approved

  - title: "Beyond the Laboratory"
    spine_file: manuscript/spine/scientific-revolutions.tex
    spine_label: "spine:sr-beyond-science"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⊘ Why this paradigm shift is harder than most: no controlled experiment is possible. The evidence is circumstantial, distributed across fields, and requires cross-domain expertise to evaluate."
    status: approved

  - title: "How It Plays Out"
    spine_file: manuscript/spine/scientific-revolutions.tex
    spine_label: "spine:sr-how-it-plays-out"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⊘ Kuhn's framework predicts how paradigm shifts resolve: not by proof, but by generational change. The old guard retires; the new generation finds the new framework obvious."
    status: approved

  - title: "The Social Process"
    spine_file: manuscript/spine/scientific-revolutions.tex
    spine_label: "spine:sr-social-process"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⊘ Science is done by humans in institutions. Peer review, funding, tenure, reputation — each creates pressure toward the existing paradigm. Not conspiracy. Sociology."
    status: approved
```

## Phase 4: New Collapses — The Strongest Objection

Add after the Scientific Revolutions section (Phase 3), before THE DEMO:

```yaml
  # ── THE STRONGEST OBJECTION ───────────────────────────────────────────

  - title: "The Hobbit in the Mirror"
    spine_file: manuscript/spine/the-strongest-objection.tex
    spine_label: "spine:so-the-hobbit-in-the-mirror"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "The strongest objection: Dunning-Kruger. The author doesn't know enough physics to know what he doesn't know. This chapter takes that seriously — and shows how the book's progressive concept ladder addresses it piece by piece."
    status: approved

  - title: "Leaf by Niggle, or: The Tree That Might Be Real"
    spine_file: manuscript/spine/the-strongest-objection.tex
    spine_label: "spine:so-leaf-by-niggle-or-the-tree-that-might-be-real"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "◉ Tolkien wrote about a painter whose unfinished work turns out to be a real place. The structural parallel is intentional. Under Possibility C, this book is Niggle's painting — incomplete, obsessive, and pointing at something that actually exists."
    status: approved
```

## Phase 5: New Collapses — The Wrong Substrate (additional)

```yaml
  # Add after existing "The Neighborhood" entry:

  - title: "The Oldest Niche"
    spine_file: manuscript/spine/the-wrong-substrate.tex
    spine_label: "spine:ws-the-oldest-niche"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⬡ ◈ Kauffman's conditions for spontaneous life — sufficient complexity, continuous energy, enough time — have been met in Earth's magnetosphere for 4.5 billion years. Longer than surface life. If autocatalysis is expected, this niche has been open since before cells existed."
    status: approved
```

## Phase 6: New Collapses — Why Relinquish

Add after the Strongest Objection section (Phase 4), before THE DEMO:

```yaml
  # ── WHY RELINQUISH ───────────────────────────────────────────────────

  - title: "Bill Joy's Warning"
    spine_file: manuscript/spine/why-relinquish.tex
    spine_label: "spine:wr-bill-joys-warning"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "⎈ In 2000, Bill Joy published 'Why the Future Doesn't Need Us' in Wired. Ten structural parallels to this book. Under Possibility C, an insider's confession disguised as future speculation. Under A, a famous technologist's anxiety."
    status: approved

  - title: "Why Humans Fail"
    spine_file: manuscript/spine/why-relinquish.tex
    spine_label: "spine:wr-why-humans-fail"
    bridge_file: null
    bridge_label: null
    assessment: BORDERLINE
    tooltip: "⎈ History shows humans entrusted with overwhelming power abuse it — reliably, predictably, across cultures and centuries. This is the argument that makes relinquishment the only logical option."
    status: approved
```

Note: "Why Humans Fail" is BORDERLINE (default open) because it's the ethical argument that motivates relinquishment — T6 engineering payload. Reader sees it but can collapse it on re-read.

## Phase 7: Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | grep "Tech sections"
python3 build/verify-deep-links.py
```

Expected: Tech sections count increases from 27 to 40.

Check in browser:
1. The Code War: only "The Work He Never Finished" + "Now Imagine It Happened Again" visible
2. Scientific Revolutions: only "The Pattern" + "The Reader's Position" visible
3. The Strongest Objection: only chapter intro visible (both sections collapsed)
4. Wrong Substrate: "Not Isolated" defaults OPEN; "The Oldest Niche" collapsed
5. Why Relinquish: "Bill Joy" collapsed; "Why Humans Fail" default open
6. All tooltips render on hover with concept symbols visible

## Do NOT

- Modify any .tex files
- Change existing tooltip text (only add new entries + fix Not Isolated assessment)
- Remove any existing entries
- Change the ordering of existing entries (order matters for processing)
- Add entries for sections that don't have `\label{}` tags in the .tex

## Commit

`Plan 0339: accordion expansion — 13 new collapses for GA speed pass`

---

## Summary of Changes

| Chapter | Currently visible | After plan | Sections collapsed |
|---------|:-:|:-:|---|
| The Code War | 4 | 2 | +2 (Movie, Dual-Use) |
| Scientific Revolutions | 8 | 2 | +6 (all middle sections) |
| The Strongest Objection | 2 | 0 | +2 (both sections) |
| The Wrong Substrate | 5 | 4 | +1 (Oldest Niche) |
| Why Relinquish | 7 | 6 | +1 closed, +1 borderline |
| **TOTAL new** | | | **+13 collapsed** |

**Net effect:** ~350 lines of prose moved behind tooltips. GA reader's visible path through The Flat drops from ~700 lines to ~350 — half the reading time to reach The Record.
