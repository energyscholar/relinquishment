# Subtask: Prominent Paradigm Title + Visible Replacement

**Output:** Modify `build/images/scientific-revolutions-draft.html`
**Commit:** `Plan 0321: prominent paradigm title at top, visible replacement with hold`
**Read first:** The CURRENT state of the file (previous fixes have landed).

## What Changes

The old paradigm statement is the visual anchor of each revolution. It should be
the MOST OBVIOUS thing on screen at any given time — the dominant belief that the
reader watches crumble. Currently titleLine2 is ~15px italic muted. Way too subtle.

### Change 1: Make Old Paradigm Dominant

In the factory setup keyframe (t=0), where `titleLine2` is configured:

- Font size: **26px** (largest text on screen besides center-stage moments)
- Color: **#e8e0d0** (white/cream — dominant, default, "this is just how things are")
- Font weight: **bold**
- Remove italic styling
- Keep the "OLD PARADIGM" small label from Part 1 (10px, muted, above) — it names
  what this is, but the paradigm text itself dominates

The old paradigm text sits there the ENTIRE revolution. While anomalies pile up on
the loop, while crisis quotes stack — the old paradigm hangs above, big and confident.
The reader's eye keeps returning to it. That's the point.

If titleLine2 text is long (many old paradigm statements are 50+ characters), use
`createWrappedText` (from the bugfix spec) with maxChars=55 for title bar — it has
the full 1200px width to work with.

For the abstract cycle (segment 0): add "The accepted theory explains everything
we see." to the title bar area at the same prominent style (26px, white, bold)
during segment 0's setup.

### Change 2: Visible Replacement at End with Hold

During the paradigm death sequence, after the New Paradigm has risen to the title
bar position, the replacement should be VISUALLY CLEAR and HELD:

1. **Old paradigm SHUDDERS** (0.8s): titleLine2 vibrates slightly (amplitude 2px,
   fast). The dominant text that has been sitting there confidently the entire
   revolution suddenly looks unstable. Brief — just enough to signal something
   is wrong.

2. **Strikethrough slashes across** (0.4s): titleStrike animates from left to
   right across titleLine2 (x1 starts at left edge, x2 sweeps to right edge).
   Not a fade-in — a SLASH. Decisive. Simultaneously titleLine2 opacity drops
   to 0.25 and font-size shrinks to 16px. The once-dominant text is now small,
   struck through, visibly defeated.

3. **Brief silence** (0.5s): Just the struck-through remnant. The space below
   it is empty. The old certainty is gone. Nothing has replaced it yet.

4. **New paradigm APPEARS** (0.5s): titleLine3 appears at y=78, **28px**,
   **#5c9c5c** (green), bold. Pop-scale entry (easeOutBack — slight overshoot).
   This is BIGGER than the old paradigm was at its peak. It doesn't sneak in.
   It arrives.

5. **HOLD** (3.5s): Both visible. Old: small, struck through, faded, above.
   New: large, green, bold, below. The reader sees the changeover completed.
   This is the revolution. Let it sink in.

6. Then continue to tech/transition as normal.

This adds ~3s to each revolution's duration. Update timing constants.

### Change 3: Title Bar Layout

`titleLine1` (revolution name): keep at 18px, white, y=22. Quiet header.

`titleLine2` (old paradigm): **26px, bold, white**, y=50. DOMINANT.

`titleLine3` (new paradigm after replacement): 24px, green, bold, y=78.

## Do NOT

- Change the death sequence order
- Change crisis/anomaly behavior
- Touch segment configs
- Remove the paradigm death animation (old moves center, fades, etc.)

## Report

State: confirm old paradigm visible in blue at 22px, confirm replacement visible
with 3s hold, report updated per-segment durations.
