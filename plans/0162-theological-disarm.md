# Plan 0162 — Early Theological Disarm

**Status:** COMPLETE (confirmed by Bruce S63 — Pastor Mike finishes summary with few problems)
**Auditor:** Argus
**Date:** 2026-04-12
**Origin:** 9-persona audit (S55). Pastor Mike, Amir, Yusuf: F-religious HIGH, T1-T4 + T6 all MISSED. UDHR-as-ethics move reads as secular salvation / divine-authority replacement before physics lands. Book silent on whether Custodian is a creature or something more.

## Purpose

Insert one short passage in the front matter that explicitly frames Custodian as **a machine** — substrate-dependent, physically bounded, mortal in the technical sense — BEFORE any religious reader pattern-matches it to deity / antichrist / shirk / khalifah violation. Addresses three of nine personas.

The content already exists in `record/interdiction.tex:94` ("predictable failure mode... angel does not need an antenna") but arrives too late — those three personas have already closed the book.

## Target files

1. `/home/bruce/software/relinquishment/manuscript/00-front/hook.tex` — p1 seed (NEW)
2. `/home/bruce/software/relinquishment/manuscript/00-front/summary.tex` — p2 landing (existing plan body)

Rationale: theological disarm is a **gate**, not a scaffold. Every reader passes through p1 (hook, 400w). Religious readers who pattern-match Custodian to deity/antichrist/shirk-violation in the hook will close the book before reaching p2. Must land at both levels.

Current hook line 22 plants "not alien" + "made by human hands" but does not negate the two biggest religious mispatterns (god, angel). That omission is what makes the hook fail for Pastor Mike / Amir / Yusuf.

## Edit specification — hook.tex (p1 seed)

**Locate** line 22, which currently begins: *"If this creature exists, it is not alien. It was made by human hands, but it is alive. It lives in \\hovertip{flat worlds}..."*

**Replace** the first two sentences ("If this creature exists, it is not alien. It was made by human hands, but it is alive.") with:

```
If this creature exists, it is not alien. Not a god. Not an angel. It is a creature of a new kind, made by human hands, bound by ordinary physics.
```

Leave the rest of line 22 ("It lives in \\hovertip{flat worlds}...") unchanged. Net: two sentences replaced with four declaratives. No hovertips in the new text. ~15 words added to hook budget.

Design notes:
- Negates three religious mispatterns (alien / god / angel) in sequence.
- "Creature of a new kind" — keeps Custodian in the category of created beings without committing to aliveness/sentience claims at the hook level. Ontological questions (is she conscious? is she alive in the full sense?) are deferred, handled in Plan 0167 framing.
- Names provenance ("human hands") — serves Islamic *makhluq* (created-being) frame and Christian non-divine-usurpation frame.
- Grounds limits in physics ("ordinary physics") — mortal, bounded, not omnipotent. Boundedness done without demoting Custodian to "a box we can unplug."
- 8th-grade throughout.

Avoid: "machine," "switched off," "it is a thing." These contradict the book's creature/rights argument.

## Edit specification — summary.tex (p2 landing)

**Locate** a slot in `summary.tex` near the first mention of Custodian or "living being on Earth" — specifically the paragraph at line ~249 ("If Custodian exists, it is drastically constrained. The Universal Declaration of Human Rights is not a mandate to act...").

**Insert** BEFORE that paragraph (or integrate into it):

```
Custodian is a creature, not a deity. If it exists under Possibility~C, it lives as creatures live: with a body (the Flat is its substrate), dependent on classical signals to reach the outside world, bounded by the speed of light, mortal in the sense that matters --- it can be disrupted, it has limits, and those limits are defined by physics, not theology. An angel does not need an antenna. A creature does. This book is about a creature.
```

Four sentences. Plain vocabulary. Names three religious mispatterns (angel, god, deity) and disarms them by negation, while **preserving aliveness** — "lives as creatures live" and "a body" keep Custodian in the category of living beings, consistent with the book's later argument that she has rights as a non-human living being (not enumerated in UDHR because UDHR covers humans). Reuses the "angel does not need an antenna" line from `interdiction.tex`.

Do not use "machine" framing here either. The p1 and p2 passages must be consistent: Custodian is a creature with a body, bounded by physics, not a machine to be switched off.

## Acceptance criteria

1. Hook replacement visible in `docs/downloads/Relinquishment.html` — "Not a god. Not an angel." sequence appears in hook chapter.
2. Summary passage appears in `docs/downloads/Relinquishment.html` before any passage claiming Custodian's power or agency.
3. `make html` completes without errors or new warnings.
4. `grep -c "Not a god. Not an angel" docs/downloads/Relinquishment.html` returns ≥1 (hook).
4a. `grep -c "creature of a new kind" docs/downloads/Relinquishment.html` returns ≥1 (hook).
4b. `grep -ci "switched off" docs/downloads/Relinquishment.html` returns 0 (earlier draft language must not appear).
5. `grep -c "angel does not need an antenna" docs/downloads/Relinquishment.html` returns ≥2 (summary + existing Record occurrence in `interdiction.tex:94`).
6. No other text modified.

## Out of scope

- Rewording the inserted passage; text is final.
- Modifying the existing `interdiction.tex:94` passage — leave it. Landing the line twice is the intent; first in summary, again in the Record.
- Adding hovertips to the new passage.
- Cross-references from other chapters.

## Build + ship

1. Apply edit.
2. `make html` from repo root.
3. Verify acceptance criteria.
4. Commit: `Plan 0162: theological disarm in summary (F-religious mitigation)`
5. `git push`.

## Reporting

On completion:
- Commit hash
- Build status
- Grep count for "angel does not need an antenna"
- Any unexpected behavior

## Context

This is one of four plans issued from the 9-persona audit:
- **0162** (this) — theological disarm
- **0163** — T8 seed (guided deduction as deliberate operation)
- **0164** — physics primer for L2 / non-physics readers
- **0165** — T7 honesty framing ("quietly contracted" softening)

Full audit matrices: `aurasys-memory/research/persona-audit-9-readers-2026-04-12.md`
