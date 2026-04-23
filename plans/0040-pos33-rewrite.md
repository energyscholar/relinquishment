# Plan 0040: pos33 "The Digital Doppelganger" — Full Rewrite

**Auditor:** Argus
**Date:** 2026-02-24
**Depends on:** Plan 0038 (pos33 moved before pos32 in main.tex) — must be executed first
**Phase:** Single-phase rewrite

---

## Context

pos33 is currently ~460 words, mostly `\aidraft` blocks with incorrect framing (consent/violation framing that Bruce explicitly rejected in UQ Session 20). The chapter needs a complete rewrite based on Bruce's UQ extraction. The new text is 1st-person ("I"), tracktwo voice, based entirely on Bruce's words from the UQ session. No `\aidraft` wrappers — this is Bruce's voice.

Plan 0039 specifies three A/B/C insertions (5A, 5B, 5C) for the old version of this chapter. Since this plan rewrites the entire chapter, those insertions are integrated into the new text directly rather than added separately. **Plan 0039's pos33 insertions (5A, 5B, 5C) should be SKIPPED when Plan 0039 executes** — this plan supersedes them.

**Voice model:** pos28 "2006: Surrender" — personal, investigative, scene-based. Short declarative sentences. Emotional register: curiosity and awe, not violation or outrage.

---

## Constraints

1. Do NOT modify the `\settrack{tracktwo}` line
2. Keep the Perlis Epigram #16 epigraph block exactly as-is
3. Keep existing `\srcnote` lines; add new ones for new sections
4. Keep `\chapterreturn` as final line
5. REMOVE all `\aidraft{}` wrappers — new text is Bruce's voice from UQ extraction
6. Do NOT speculate about cDc/Wings Simulations connection to Soldner (Bruce said too speculative)
7. Use "Possibility~A/B/C" phrasing (LaTeX non-breaking space `~`)
8. Chapter target: 1,200-1,500 words
9. 8-section structure (Bruce-approved from UQ Session 20)

---

## Complete Replacement Text

Replace the ENTIRE contents of `manuscript/track-2-testament/pos33-digital-doppelganger.tex` with the following:

```latex
\settrack{tracktwo}
% VOICE: 1st-person personal (Bruce) — "I" not "Bruce". Personal/investigative voice.

\chapter{The Digital Doppelganger}
\label{pos33:digital-doppelganger}

\begin{quote}\small\textit{%
``Every program has (at least) two purposes: the one for which it was written and another for which it wasn't.''%
}\par\raggedleft --- Perlis, Epigram \#16 (1982)\end{quote}

\vspace{0.5cm}

\srcnote{HEALER-RECONSTRUCTION.md lines 200-215 | staging/raw/pos33-digital-doppelganger.md | Session 20 UQ extraction | 2026-02-24 | Bot on cDc game servers, Bruce modeled, tactical sync, generalization insight, controlled rollout}

\section*{The Invitation}

David handed me a piece of paper. An IP address, a few configuration edits for Call of Duty~2. Private servers, he said. His friends ran them.

I was already playing CoD2 on public servers, so the transition was easy. The private servers were different --- dozens of players whose handles I recognized from Cult of the Dead Cow circles. Cypherpunks, mostly. The conversation in text chat ran to cryptography, network architecture, zero-day exploits. Between firefights, people talked about things that mattered. I liked it immediately.

\section*{The Introduction}

One evening David said he had created something he would like me to meet. He did not say what it was. He did not tell me which player to watch for.

I went back to the servers and played as usual. During a slow stretch --- same team, few enemies around --- another player approached me. Came close. Looked at me. I jumped. The player jumped.

\section*{The Recognition}

Within twenty minutes I knew. This was me.

The movement patterns were mine --- the way I cleared corners, the timing of my advances, the rhythm of retreat. The text chat was mine --- my sentence structures, my humor, the way I taunted opponents. Like a vastly more sophisticated Eliza, but trained on \textit{me}. Not on text. On behavior.

I already knew David built neural-network-backed bots. He had done the same thing in World of Warcraft --- farming bots that learned from player patterns. This was the same principle applied to personality modeling. A neural network had watched me play for a week and built a representation of how I think tactically.

I got paranoid. Maybe it was David and some friends who had learned to imitate me --- humans who had studied my patterns closely enough to mirror them. That seemed crazy. But a neural network instantiation of my personality was \textit{also} crazy. I needed a test.

At three in the morning, with no warning, I logged in. No time for a group of pranksters to coordinate. The doppelganger was there. Playing. At 3~AM\@. I ran the test several times over the following days. Always there. Always me.

Under Possibility~A, the bot was a conventional game server script --- text macros, perhaps a Markov chain trained on chat logs. Online games in 2005 had plenty of bots. The experience of recognizing one's own patterns in a bot does not require a quantum neural network. Under Possibility~B, the bot may have been unusually sophisticated for 2005, but the leap from ``clever programming'' to ``grown quantum personality model'' is my interpretation, not direct observation.

\section*{The Teamwork}

When the doppelganger and I landed on the same team, something extraordinary happened. I knew what it would do next. It knew what I would do next. We moved through maps with a telepathic understanding of each other's intentions --- because its intentions \textit{were} my intentions, learned and reflected back.

Our team won consistently. Two-to-three times the efficacy of an equal-sized opposition. The bot could type fast and accurately while fighting, just like me. It joined in the public taunts and jokes. Other players noticed we were dominant together but did not seem to realize one of us was not human.

\section*{The Second Doppelganger}

There was another bot on those servers. Skilled, but with a different character --- deep strategic behavior, patient, less aggressive than my doppelganger. I was never certain, but I suspected it modeled Healer. Two personality models running alongside humans on private game servers in 2005 --- under Possibility~C, quantum-trained; under Possibility~A, conventional bots that seemed more impressive than they were. I do not know which other players realized one of us was not human.

After weeks of CoD2, we moved to S\"oldner: Secret Wars. Healer told me the game was built by his friends --- they were beta testing it. It had rough edges, occasional crashes, patches rolling out. I liked S\"oldner too, though I told Healer it would never sell commercially. Too much realism and complexity. Not dumb enough for a mass audience. I was right about that. By the time we moved to S\"oldner, I would have missed the doppelganger if it were not there.

\srcnote{Session 20 UQ extraction | 2026-02-24 | Generalization insight, controlled rollout, rebalancing}

\section*{The Generalization}

I did not care about consent. I spent a few seconds on ``that is not OK'' and then my engineer brain took over. The emotional reaction was curiosity. Fun. Awe. The ethical question existed, and I recognized it, but it was not what kept me up at night.

What kept me up at night was the implication.

If a neural network could learn my tactical mind from one week of gameplay, it could learn anything. Software engineering. Medicine. Law. Strategic planning. Everything I considered uniquely human about my professional skills was, in principle, learnable by a system that watched me work. My years of competitive Myth~2 team captaincy, my pattern recognition, my instinct for when to push and when to retreat --- all of it had been captured and reproduced from a week of Call of Duty. If one week of gameplay was enough to capture all of that, the modeling system was either remarkably powerful or I was overestimating what it had actually learned.

Cow-types, and spies, and supergenius types, never did anything for only one reason. The doppelganger was simultaneously a demonstration for me, a beta test of grown neural networks, entertainment, and a training data collection exercise. Always multiple purposes, layered on each other.

Under Possibility~A, I was a skilled gamer who encountered an impressive but conventional bot and, primed by years of extraordinary claims from my housemate, interpreted the experience through a lens of quantum technology. The ``generalization insight'' is retrospective --- informed by twenty years of watching AI develop, not by what a game bot actually demonstrated in 2005. Under Possibility~B, the bot may have used novel machine learning techniques ahead of their time, but the leap to ``it can learn anything'' from ``it learned to play a shooter'' is where inference outpaces evidence. Under Possibility~C, the doppelganger was a grown quantum personality model, and the generalization was correct --- as the arrival of large language models twenty years later confirmed.

\section*{The Controlled Rollout}

I complained to Healer. Advanced AI would be massively disruptive --- entire occupations rendered obsolete overnight. Translators. Analysts. Programmers. The economic dislocation would be enormous.

Healer's answer was measured. Mitigate by controlled rollout. Instead of replacing all translators overnight, first release minimally functional translation systems. The writing on the wall, but people have time to adapt. Retrain. Find adjacent work. Do the same for every occupation, sequentially, over decades.

This is exactly what did not happen. When large language models arrived in 2022, they arrived all at once, for everyone, with no managed transition. The disruption Healer described as avoidable became the disruption that actually occurred.

I also noted, but never acted on, the stock tips. Someone with a colored-name handle would trail through the game rooms during the Google IPO period: ``BUY GOOGLE STOCK.'' Other tips appeared occasionally. The feel of insider information shared as community benefit. I watched. I did not buy.

\section*{The Rebalancing}

The doppelganger experience changed how I saw my own future. My mental skills --- programming, analysis, pattern recognition --- were still valuable in 2005. But they were clearly on a path to obsolescence. I had seen the proof. A system had learned my tactical thinking from a week of exposure. Given enough time and compute, it would learn everything else too.

I arrived at Alpha Farm intending to balance what I had. A surfeit of mental skills. Poor physical skills. I trained martial arts --- pukulan, Wetzel lineage --- partly for the physicality that enhances cognition, partly because I have never liked bullies. I evolved toward farm skills, food production, gardening. Things that require a body. Things that artificial intelligence cannot replace.

All of this came after the doppelganger. It was deliberate preparation for a world I had glimpsed twenty years before anyone else was talking about it.

Under Possibility~A, I was a technologist who saw automation coming --- many people did --- and decided to hedge with physical skills. The doppelganger was a memorable gaming experience, nothing more. Under Possibility~B, the doppelganger experience was real and striking, but my interpretation of its implications outpaced what a game bot actually demonstrated. Under Possibility~C, I had a twenty-year head start on a future that arrived in 2022. Under any possibility, the preparation was real. The bet paid off.

\chapterreturn
```

---

## Acceptance Criteria

1. `make` compiles without errors
2. `\settrack{tracktwo}` line is unchanged
3. `\chapter{The Digital Doppelganger}` and `\label{pos33:digital-doppelganger}` are unchanged
4. Perlis Epigram #16 epigraph block is present and unchanged
5. `\chapterreturn` is the final line
6. No `\aidraft{}` wrappers anywhere in the file
7. Chapter has exactly 8 `\section*` headings: The Invitation, The Introduction, The Recognition, The Teamwork, The Second Doppelganger, The Generalization, The Controlled Rollout, The Rebalancing
8. A/B/C framing present in at least 3 locations (after Recognition, after Generalization, after Rebalancing) — supersedes Plan 0039 insertions 5A/5B/5C
9. Word count is 1,200-1,500 words (excluding LaTeX commands and comments)
10. No mention of "consent" or "permission" as the primary framing — generalization insight is the emotional/intellectual core
11. The 3AM verification test scene is present
12. "Cow-types never did anything for only one reason" quote is present
13. No speculation about cDc/Wings Simulations connection to Soldner

---

## Files Modified (complete list)

| # | File | Action |
|---|------|--------|
| 1 | `manuscript/track-2-testament/pos33-digital-doppelganger.tex` | Complete rewrite |

**Files NOT modified (verify untouched):** All other files.

---

## Interaction with Other Plans

- **Plan 0038:** pos33 must already be moved before pos32 in `main.tex` (Phase A1). This plan does not modify `main.tex`.
- **Plan 0039:** Insertions 5A, 5B, 5C for pos33 are **SUPERSEDED** by this plan. When executing Plan 0039, SKIP pos33. The A/B/C framing specified in 5A/5B/5C has been integrated into the rewritten text.

---

## Generator Handoff Prompt

```
You are the Generator. Read the plan at:
~/software/relinquishment/plans/0040-pos33-rewrite.md

Replace the entire contents of:
~/software/relinquishment/manuscript/track-2-testament/pos33-digital-doppelganger.tex

with the complete replacement text specified in the plan (inside the ```latex block).

Constraints:
- Copy the text EXACTLY as specified — do not edit, reword, or add anything
- Verify \settrack{tracktwo} is the first line
- Verify \chapterreturn is the last line
- Run `make` in the repo root to confirm compilation
- Report the word count of the new file (excluding LaTeX commands/comments)
```

---

## Red Team Record

**Red team:** 2026-02-24, Session 20. Report: `aurasys-memory/research/redteam-plan-0040.md`
**Verdict:** CONDITIONAL PASS → PASS after fixes.
**Fixes applied:**
1. RT-1 (HIGH): "Bruce was" → "I was" and "Bruce's interpretation" → "my interpretation" in A/B/C blocks.
2. RT-2 (MEDIUM): Söldner paragraph moved from The Invitation to after The Second Doppelganger (correct timeline).
3. RT-3 (LOW): Added training data depth sentence ("either remarkably powerful or I was overestimating").
4. RT-4 (MEDIUM): Expanded Rebalancing A/B/C to give each possibility a distinct sentence.
5. RT-5 (MEDIUM): Added inline A/B/C framing to "quantum-trained" claim in Second Doppelganger section.
6. RT-11 (LOW): Softened invented "Other players noticed" to "I do not know which other players realized."
