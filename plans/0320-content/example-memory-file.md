---
name: Check DB before GitHub API calls
description: Always query v_snailmail_pending before making GitHub API calls for snailmail — avoids redundant API hits and rate limiting
type: feedback
---

Always check the local database view `v_snailmail_pending` before making GitHub API calls to check for new messages. The DB is updated by the hourly scheduled agent.

**Why:** During Session 45, redundant GitHub API calls caused rate limiting that blocked a time-sensitive response for 15 minutes. The DB already had the data — the API call was unnecessary.

**How to apply:** When the snailmail check triggers, run `SELECT * FROM v_snailmail_pending` first. Only call the GitHub API if the DB shows pending items that need a response composed.
