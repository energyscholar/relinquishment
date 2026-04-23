# Plan 0163 — T8 Seed (Guided Deduction as Deliberate Operation)

**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12
**Origin:** 9-persona audit (S55). T8 is the universally weakest takeaway — 8/9 personas MISSED-or-PARTIAL. The book relies on T8 ("guided deduction was a deliberate operation, not a favor; the book exists because bridges don't build themselves") but never states it in hook or summary. Explanation lives in `why-relinquish.tex:109-115` (pos chapter, spine). Front-matter readers (Rachel, Jane, Doctorow, Arjun) never reach it.

## Purpose

Add one short paragraph in `summary.tex` that lands T8 explicitly before any reader closes the book. T8's absence is why readers experience the book as "memoir of a mentor" rather than "deliberate operation to breach the silence gap." Both framings are true; T8 is load-bearing under Possibility~C and still useful under A/B.

## Target files

1. `/home/bruce/software/relinquishment/manuscript/00-front/hook.tex` — p1 seed (NEW)
2. `/home/bruce/software/relinquishment/manuscript/00-front/summary.tex` — p2 landing (existing plan body)

Rationale: T8 explains *why the book exists at all* and defuses F-conspiracy for every persona. It must land for p1-only readers (400 words, hook only), not just p2 readers who reach the summary. Hook already plants two T8-adjacent lines ("forbidden to tell anyone" at L19; "guiding him through published science in a deliberate sequence" at L24) but neither names the **operational frame** — a reader takes line 24 as one mentor's conscience rather than a structured operation. Without the operational frame, F-conspiracy fills the gap.

## Edit specification — hook.tex (p1 seed)

**Locate** line 24 (current text: *"One member of that team couldn't live with the silence, so he spent three years teaching a scientist named Bruce Stephenson --- never revealing anything secret, only guiding him through published science in a deliberate sequence. Stephenson recognized what the sequence pointed to. Then his mentor disappeared. Stephenson spent twenty years trying to understand what he'd been shown."*).

**Insert** as two new sentences at the end of that paragraph (after "what he'd been shown."), before the "He doesn't know what's true" paragraph:

```
The teaching was not a favor --- it was the plan. A team of scientists had found something they believed the world needed. They had also sworn not to say it. Guided deduction was how they squared the two.
```

Four sentences. 8th-grade vocabulary. No hovertips in hook. Names: team (plural — kills loner-mentor frame), humanistic motive (defuses F-conspiracy at the motive level), legal bind, invention-by-name. Squared the two = tension resolution, not plot.

## Edit specification — summary.tex (p2 landing)

**Locate** an insertion slot near where the book first explains *why* the record needed to reach the outside world. Natural slot: after the paragraph that discusses silence / classification (varies by build) but before the "predictions that are testable" paragraph at the end of the summary.

**Insert** (Generator to find cleanest break; content is final):

```
Under Possibility~C, the teaching was not a favor. It was an \hovertip{operation} --- a deliberate operation to breach the silence gap. Every team member who built what this book describes had signed agreements that made direct disclosure a crime. The scientific community was not going to connect the five fields on its own --- the silence was structural, not solvable from the inside. Their solution was guided deduction: find someone outside the classification regime, teach them only published science in a careful sequence, and let them reach the conclusions independently. No classified information changes hands. No crime is committed. The student publishes what they independently learned. The silence gap is breached from the outside, by someone with the legal standing to speak.

Guided deduction follows the letter of the law while violating its spirit. The trade is bounded: without it, this science would stay classified until roughly 2065 --- seventy years from discovery. Guided deduction activates about thirty years in, moving publication forward by about forty years. The team judged seventy years too long to wait.
```

Two paragraphs. Paragraph 1 names guided deduction as mechanism (T8), gives the *why* (T5 callback), preserves Possibility~C framing, and defuses F-conspiracy by locating the architecture in rational constraint-satisfaction. Paragraph 2 is the integrity beat: names the letter/spirit trade honestly and bounds it quantitatively (activates ~30 years post-discovery; moves publication forward ~40 years from the default 70-year classification horizon — not a permanent bypass). DN Axis 4 (integrity over cleverness) — the book admits the ethical shape of what it describes rather than pretending guided deduction is morally free.

## Hovertip addition

Add to `build/hover-definitions.yaml` if not present:

```yaml
operation: "A deliberate structured activity with a plan, participants, and intended outcome — used here in the intelligence-community sense. Not a metaphor. The teaching of Bruce Stephenson was one phase of a larger effort that began around 1997 and completed with the handover in 2006."
```

(Check first — may already exist.)

## Acceptance criteria

1. Both landings appear in `docs/downloads/Relinquishment.html` — p1 sentences inside the hook; p2 paragraph inside the summary section.
2. `\hovertip{operation}` resolves with popup (p2 only; hook has no hovertips).
3. `make html` completes without errors.
4. `grep -c "teaching was not a favor" docs/downloads/Relinquishment.html` returns ≥2 (p1 short form + p2 longer form both use this phrase).
5. `grep -c "breach the silence gap" docs/downloads/Relinquishment.html` returns ≥1 (p2 only).
6. `grep -c "it was the plan" docs/downloads/Relinquishment.html` returns ≥1 (p1 only).
7. `grep -c "letter of the law" docs/downloads/Relinquishment.html` returns ≥1 (p2 integrity beat).
8. `grep -c "seventy years" docs/downloads/Relinquishment.html` returns ≥1 (p2 integrity beat).
9. No other text modified except hover YAML.

## Out of scope

- Rewording the paragraph.
- Modifying `why-relinquish.tex:109-115` — leave the full explanation in spine chapter intact.
- Adding this to other front matter files beyond hook + summary (introduction, how-to-read, etc.) — those defer to later plan.

## Build + ship

1. Apply edits (hook p1 seed + summary p2 paragraph + hover YAML).
2. `make html`.
3. Verify acceptance criteria (all three grep counts + manual visual check of hook and summary landings).
4. Commit: `Plan 0163: T8 seed in hook (p1) + summary (p2) — guided deduction as operation`
5. `git push`.

## Reporting

On completion:
- Commit hash
- Build status
- Grep count
- Any unexpected behavior

## Context

Part of 4-plan audit response. See `aurasys-memory/research/persona-audit-9-readers-2026-04-12.md` for matrices.
