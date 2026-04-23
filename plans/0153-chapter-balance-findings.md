# Plan 0153: Chapter Balance Findings

## Status: FINDINGS ONLY — no action taken yet

## Date: 2026-04-10

## Word Counts (post-deduplication, post-Plan 0152)

### Front Matter (10,902 total)
- hook: 594
- the-stack: 543
- summary: 5,091
- introduction: 1,408
- how-to-read: 335
- preface: 350
- genevieve-preface: 300

### Part I — The Flat (24,561 total, ~1,500 avg per spine chapter)
- three-possibilities: 1,166
- the-stack: 644
- interlude-01: 225
- the-flat: 1,215
- interlude-02: 198
- the-braid: 1,929
- interlude-03: 206
- the-factoring-game: 1,348
- the-code-war: 2,298
- interlude-04: 219
- genesis: 1,201
- growing-a-mind: 1,020
- interlude-05: 215
- the-wrong-substrate: 2,680
- interlude-06: 231
- the-silence-gap: 1,047
- capabilities: 936
- why-relinquish: 1,835
- interlude-07: 272
- the-strongest-objection: 5,273
- weigh-the-evidence: 403

### Part II — The Record (33,413 total, ~2,100 avg)
- record-intro: 54
- alpha-farm: 5,240
- hobbit-mirror: 318
- what-healer-said: 5,155
- the-departure: 1,914
- the-handler: 894
- interdiction: 2,068
- first-light: 2,717
- the-walk-out: 1,818
- the-target: 2,065
- instantiation: 1,136
- never-again: 1,221
- the-surrender: 1,500
- twenty-years: 2,666
- the-question: 2,151

### Appendix + Back (20,992 total)
- abstracts: 4,299
- timeline: 3,908
- predictions: 1,300
- glossary + entries: 896
- rlhf-bias: 1,455
- topic-guide: 1,423
- dms-note: 623
- sources: 9
- corrections: 802
- afterword + acknowledgements + verification + colophon: 2,890

### TOTAL: ~89,868 words (~360 pages at 250 w/p)

## Problems Found

### Problem 1 (HIGH): Part II opening double-heavy
Alpha Farm (5,240) + What Healer Said (5,155) = 10,400 words back-to-back at the start of Part II. Part I trained the reader on 1,000-2,500 word chapters. Options:
- Split one of them at a natural break
- Move hobbit-mirror (318) between them as a breather
- Accept the gear change (Part II is memoir, reader expects longer)

### Problem 2 (MEDIUM): Weigh the Evidence stub
403 words after The Strongest Objection (5,273). Feels like a shrug after the book's climax. Options:
- Bulk to ~800-1,000 words
- Fold into end of strongest-objection
- Accept as a deliberate "and now, you decide" coda

### Problem 3 (LOW): Transition jolts
- hobbit-mirror (318) → what-healer-said (5,155): 16:1 ratio, sharpest jolt
- weigh-the-evidence (403) → record-intro (54) → alpha-farm (5,240): weak Part I closer into Part II's heaviest

### Problem 4 (LOW): Sub-1,000 back-to-back
capabilities (936) + silence-gap (1,047) feels slightly rushed where reader should sit with implications.

### Problem 5 (OBSERVATION): Front matter weight
summary (5,091) is heavy for front matter on phone. Justified as p2 standalone piece.

### Problem 6 (OBSERVATION): Strongest Objection on mobile
At 5,273 words (2x any other Part I chapter), phone readers might benefit from mid-chapter visual break.

## Deduplication Changes Made This Session (2026-04-10)

1. Plan 0152: Folded The Demonstration into First Light (removed 1 chapter)
2. Cut "preparation not disclosure" verbatim paragraph from weigh-the-evidence
3. Cut Factoring Game stiff opening (lines 19-37)
4. Trimmed backchannels enumeration from the-flat (forward ref to interdiction)
5. Compressed QT protocol in the-flat (constraint + forward ref to the-braid)
6. Scalpeled GCHQ retelling from factoring-game (kept Shor/EO13026 analysis)
7. Replaced buttons-and-threads re-intro in growing-a-mind with callback
8. Compressed Why Relinquish habitat recap, cut A/B/C qualifier
9. Trimmed Turing morphogenesis in code-war to forward ref
10. Deleted 3 convergence vestiges (pos28-surrender, pos35-the-question, pos36-steelman-a)
