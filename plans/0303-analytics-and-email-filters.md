# Plan 0303: Opt-In Feedback System + Email Filter Addresses

**Status:** READY FOR GENERATOR (Phase 1 + Phase 3 fix)
**Priority:** MEDIUM — needed before release traffic arrives
**Source:** Bruce, S67 CW3

## Context

Two reader-engagement infrastructure tasks:

1. **Feedback:** NO passive tracking. No GA4, no analytics scripts, no cookies, no beacons. The only tracking is an **opt-in feedback system** — readers who wish to help improve V2 can voluntarily submit feedback. Zero tracking for everyone else.

2. **Email filters:** The book has 6 filtered Gmail addresses. Bruce needs to (a) verify the existing Gmail filters work, and (b) decide whether additional filtered addresses are needed for strategic placement.

## Design Principle

**No surveillance. Readers who want to help, help. Everyone else is invisible.**

## Current Email Addresses in Book

| Filter address | Location | Purpose |
|---|---|---|
| `+predictions` | predictions.tex:103 | Prediction reports |
| `+physics` | abstracts.tex:302 | Physics questions |
| `+evidence` | verification.tex:43 | Evidence submissions |
| `+licensing` | copyright.tex:31 | Licensing inquiries |
| `+press` | colophon.tex:62 | Media/press |
| `+hello` | colophon.tex:64 | General correspondence |

## Plan

### Phase 1: Opt-In Feedback Widget in reader.js

Add a lightweight, non-tracking feedback mechanism to the book's web version. Readers who want to help improve V2 can opt in. No data is collected from anyone who doesn't actively choose to submit.

**Implementation: Email-based feedback (simplest, zero infrastructure)**

Add a small "Feedback for V2" button to reader.js toolbar (next to existing tools). When clicked, it opens a `mailto:` link pre-populated with context:

```javascript
// Feedback button — opt-in only, no tracking
function sendFeedback() {
  var chapter = getCurrentChapter(); // from existing reader.js navigation
  var subject = encodeURIComponent('V2 Feedback: ' + chapter);
  var body = encodeURIComponent(
    'Chapter: ' + chapter + '\n' +
    'Section: \n\n' +
    'What worked:\n\n' +
    'What was confusing:\n\n' +
    'Suggestion:\n\n'
  );
  window.location.href = 'mailto:energyscholar+feedback@gmail.com?subject=' + subject + '&body=' + body;
}
```

**Button placement:** In the reader.js toolbar, a small "V2 Feedback" or envelope icon. Unobtrusive — visible but not nagging.

**What this gives you:**
- Which chapters generate the most feedback (from email subjects)
- What readers found confusing (from structured email body)
- What they liked (from "what worked" field)
- All sorted automatically by Gmail filter on `+feedback`
- Zero JavaScript analytics. Zero cookies. Zero network requests. The mailto link opens their own email client — you never know they were there unless they choose to write.

**Website-only guard:** The feedback button only appears when served from `relinquishment.ai` (hostname check). Downloaded copies don't show it — offline readers are invisible.

```javascript
if (window.location.hostname === 'relinquishment.ai') {
  // add feedback button to toolbar
}
```

**Idempotency:** If `sendFeedback` function exists in reader.js — phase is applied.

### Phase 2: Verify Existing Email Filters

**DONE** — Bruce verified Gmail filters work (S68). Also create filter for `energyscholar+feedback@gmail.com` → Label: V2-Feedback.

### Phase 3: Landing Page Email Fix

**S68 audit finding:** `docs/index-live.html:64` uses `+physics` as contact address. GA readers landing on the front page aren't writing about physics — they want general correspondence. Change to `+hello`.

**File:** `~/software/relinquishment/docs/index-live.html`, line 64.
**Old:** `energyscholar+physics@gmail.com`
**New:** `energyscholar+hello@gmail.com`

**Idempotency:** If line 64 contains `+hello` — phase is applied.

### Phase 4: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

- [ ] Open `docs/downloads/Relinquishment.html` from local filesystem — verify NO feedback button visible, NO network requests
- [ ] Open `https://relinquishment.ai` — verify feedback button appears in toolbar
- [ ] Click feedback button — verify mailto link opens with pre-populated subject and body
- [ ] Verify subject contains current chapter name
- [ ] All existing email addresses render correctly
- [ ] Landing page (index-live.html) uses `+hello`, not `+physics`
- [ ] No regression in book content, styling, or reader.js features

## Acceptance Criteria

- [ ] Zero tracking for all readers (no analytics, no cookies, no beacons)
- [ ] Opt-in feedback via mailto link, pre-populated with chapter context
- [ ] Feedback button only visible on relinquishment.ai (hostname guard)
- [ ] All 7 email filters verified working in Gmail (6 existing + feedback)
- [ ] Downloaded HTML file has zero engagement infrastructure

## What This Plan Does NOT Do

- Does not add GA4, Plausible, or any analytics platform
- Does not track pageviews, scroll depth, or navigation
- Does not add cookies or local storage for tracking purposes
- Does not require any server-side infrastructure
- Does not modify robots.txt (Plan 0300 scope)

---

## Annealing Record

**Round 1 (MED, S68): Email sweep — are all 6 addresses placed correctly?**
Swept all .tex, .py, .js, .yaml, .html, .md files. Found 8 occurrences across 8 files. All correct except: `docs/index-live.html:64` uses `+physics` for the landing page contact. GA visitors aren't physics-specific — should be `+hello`. Fix added as Phase 3.

**Round 2 (LOW, S68): Is the hostname guard sufficient?**
`window.location.hostname === 'relinquishment.ai'` — works for the live site. Also blocks `localhost` and local file:// reads. This means development testing requires either a hosts file entry or a manual override. Acceptable — the feedback button is low-risk to test manually on the live site after deployment.

**Round 3 (LOW, S68): Phase 2 still needed?**
Bruce confirmed Gmail filters already work. Phase 2 reduced to creating the one new `+feedback` filter. This is manual (30 seconds in Gmail).

---

*Plan 0303 v3, updated S68, 2026-05-08. Auditor: Argus.*
*v2: Replaced GA4 with opt-in email feedback. v3: Phase 2 DONE, Phase 3 simplified to one landing-page fix, +3 annealing rounds.*
