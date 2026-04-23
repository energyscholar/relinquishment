# Plan 0174 — Hook Micro-Cleanup (OPSEC + prose nits)

**Type:** Surgical prose patch. Single commit. hook.tex only.

## Three items

### 1. OPSEC: strip egress mode from HALO-light opener (line 11)

Bruce (2026-04-13): *"the p1 p2 version starts with an AIRCRAFT and assumes a particular mode of egress. No. That would be OPSEC."* Proposed frame: *"A man falls from the stratosphere"* — leave the mystery for later.

**Current (line 11):**

> [REDACTED]. The air at altitude is thin enough to kill a man in minutes. He checks his oxygen, rolls out of the aircraft's door, and falls. Through cloud, then below cloud, toward [REDACTED]. His orders for the next [REDACTED] hours are [REDACTED]. The people below will never know he was there.

**Target:**

> [REDACTED]. A man falls through the stratosphere. The air is thin enough to kill in minutes. He checks his oxygen. Through cloud, then below cloud, toward [REDACTED]. His orders for the next [REDACTED] hours are [REDACTED]. The people below will never know he was there.

**Structural beats preserved:** altitude sensation, body mechanics (falling, checking oxygen), asymmetry of awareness, vague time pressure, full redactions. *"He has done this before. He will do it again."* (line 13) stays unchanged.

**Must NOT reintroduce:** aircraft, plane, jet, helicopter, door, ramp, hatch, jump platform — any term that commits to mode of egress. "Falls" / "falling" is mode-agnostic.

### 2. Prose nit: fix the "one … one" stutter on line 17

**Current (mid-line 17):**

> Quantum computation is one thing one can do with wormhole technology. Their quantum computer could crack the codes that protect the world's secrets.

Two issues: (a) "one thing one can do" reads stilted; (b) "Their" antecedent is the team, two paragraphs up — distance makes it dangle.

**Target:**

> A working quantum computer is one application of that technology --- capable of cracking the codes that protect the world's secrets.

Matches summary line 52's cleaner phrasing (*"A working quantum computer is one application of that primitive"*). Hook + summary now consistent on this sentence.

### 3. Internal contradiction: custodian vs wormholes at top of stack (line 19)

**Current (line 17):** *"The custodian is the next emergent layer above that [wormhole technology]."*
**Current (line 19):** *"by the time you reach the top, emergent layers compound into wormholes."*

Both claim top-of-stack. Line 17's hierarchy (custodian above wormhole tech) is the load-bearing one — it's what the rest of the book is built on. Line 19 needs a small fix.

**Current (line 19):**

> The technology is a stack --- each piece does everything the one below it does, plus one new thing. Fire feeds itself; a candle holds its shape; by the time you reach the top, emergent layers compound into wormholes.

**Target:**

> The technology is a stack --- each piece does everything the one below it does, plus one new thing. Fire feeds itself; a candle holds its shape; by the time you reach the top, emergent layers compound into a coherent custodian.

Now consistent with line 17's hierarchy. Wormholes remain a mid-stack emergent property; custodian is the top.

## Acceptance

- Hook line 11 rewritten per §1. No egress-mode terms present anywhere in hook.tex. Verification: `grep -iE 'aircraft|plane|jet|helicopter|ramp|hatch' manuscript/00-front/hook.tex` returns zero hits.
- Hook line 17 mid-sentence rewritten per §2. Verification: `grep -n "one thing one can do\|Their quantum computer" manuscript/00-front/hook.tex` returns zero hits.
- Hook line 19 end-sentence rewritten per §3. Verification: `grep -n "compound into wormholes" manuscript/00-front/hook.tex` returns zero hits; `grep -n "compound into a coherent custodian" manuscript/00-front/hook.tex` returns one hit.
- Word count change: within ±30w of current hook.tex (expected small net reduction).
- Existing hovertip anchors remain resolved (nothing in this patch removes or renames anchors).
- `make` / HTML build clean; pushed to website per `feedback-build-to-website.md`.

## Re-engagement

Given the changes are three surgical prose fixes with no new claims and no reframings, skip the full 10-persona Tier-0 sweep. Spot-check three personas whose signal is most sensitive to these changes:

- **Jane:** does the opener still pull? (Egress mystery should INCREASE pull, not decrease.)
- **Chen:** does the QC-as-one-application sentence now read as clean rigor? (Expected upgrade from current stilted phrasing.)
- **Wei:** does "compound into a coherent custodian" read consistent with the emergence ladder? (Expected small reinforcement — custodian was always the top.)

If any of the three regresses, revert and re-plan. Otherwise ship.

## Commit

One commit: `Plan 0174: hook micro-cleanup — OPSEC strip egress, prose nits, custodian-at-top fix`

## Rollback

`git revert` the single commit. Zero risk.

## Out of scope

- summary.tex changes (summary already has the cleaner phrasing on item 2; items 1 and 3 don't apply to summary).
- Hovertip content.
- Any new claims, reframings, or structural moves.

## Handoff report (Generator, 4 lines)

1. Commit SHA.
2. Build + push result.
3. Three-persona spot-check: Jane / Chen / Wei, one-word result each.
4. Confirm no egress-mode terms in hook.tex (grep result).
