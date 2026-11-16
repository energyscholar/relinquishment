#!/usr/bin/env python3
"""Regenerate build/puzzle-status.txt from puzzle-data.yaml + puzzle-tracker.yaml (Plan 1537).

Cross-checks the two files first. It fails, naming the puzzle, and writes nothing, when:
  - a puzzle in the data has no tracker entry;
  - a tracker entry has no puzzle in the data;
  - a puzzle's approved/installed flags give no status (see STATUS below);
  - a tracker entry declares a `status:` that differs from the derived one.

Status of a puzzle, from its data type and its tracker flags:
  live              type is rendered, approved, installed
  built-unapproved  type is rendered, not approved, not installed
  not-built         type has no row in puzzle_types.PUZZLE_TYPES

The tracker's `type: meta` entry is the Bridge Builder itself; it corresponds to the
data's `bridge_builder` block and is rendered by the Bridge Builder section.

Usage: python3 build/puzzle-status.py [--data PATH] [--tracker PATH] [--out PATH]
"""

import argparse
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from puzzle_types import PUZZLE_TYPES  # noqa: E402

# (built, approved, installed) -> status. Combinations absent from this table have no status.
STATUS = {
    (True, True, True): 'live',
    (True, False, False): 'built-unapproved',
    (False, True, True): 'not-built',
    (False, True, False): 'not-built',
    (False, False, True): 'not-built',
    (False, False, False): 'not-built',
}


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def data_rows(data):
    """id -> (type, puzzle dict) for every puzzle the data defines."""
    rows = {}
    for p in data.get('chapter_puzzles', []):
        rows[p['id']] = (p.get('type', ''), p)
    bridge = data.get('bridge_builder')
    if bridge:
        for p in bridge.get('puzzles', []):
            rows[p['id']] = (p.get('sub_type', ''), p)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--data', default=os.path.join(HERE, 'puzzle-data.yaml'))
    ap.add_argument('--tracker', default=os.path.join(HERE, 'puzzle-tracker.yaml'))
    ap.add_argument('--out', default=os.path.join(HERE, 'puzzle-status.txt'))
    args = ap.parse_args()

    data = load(args.data)
    tracker = load(args.tracker)
    drows = data_rows(data)
    has_bridge = bool(data.get('bridge_builder'))

    entries = list(tracker.get('chapter_puzzles', [])) + list(tracker.get('bridge_puzzles', []))
    errors = []
    tracked = set()
    rows = []
    for e in entries:
        pid = e['id']
        tracked.add(pid)
        if e.get('type') == 'meta':
            if not has_bridge:
                errors.append(f'{pid}: tracker meta entry, but the data has no bridge_builder block')
                continue
            ptype, p, built = 'meta', data['bridge_builder'], True
        elif pid not in drows:
            errors.append(f'{pid}: in the tracker, missing from the data')
            continue
        else:
            ptype, p = drows[pid]
            built = ptype in PUZZLE_TYPES
        key = (built, bool(e.get('approved')), bool(e.get('installed')))
        status = STATUS.get(key)
        if status is None:
            errors.append(f'{pid}: approved={key[1]} installed={key[2]} has no status '
                          f'(live needs both; built-unapproved needs neither)')
            continue
        declared = e.get('status')
        if declared is not None and declared != status:
            errors.append(f'{pid}: tracker declares status {declared!r}, derived {status!r}')
        rows.append((pid, ptype, e, p, status))

    for pid in drows:
        if pid not in tracked:
            errors.append(f'{pid}: in the data, missing from the tracker')

    if errors:
        print('puzzle-status: tracker <-> data cross-check FAILED', file=sys.stderr)
        for err in errors:
            print(f'  {err}', file=sys.stderr)
        return 1

    def short(s, n=58):
        s = ' '.join(str(s).split())
        return s if len(s) <= n else s[:n - 3] + '...'

    lines = [f"{'ID':<25} {'Ty':<6} {'Lv':<3} {'Ap':<2} {'In':<2} {'Status':<16} {'Chapter':<24} Question",
             '─' * 135]
    counts = {}
    for pid, ptype, e, p, status in rows:
        counts[status] = counts.get(status, 0) + 1
        mark = lambda b: '✓' if b else '·'
        chapter = e.get('location', {}).get('chapter', '')
        question = p.get('question') or p.get('title') or e.get('title', '')
        lines.append(f"{pid:<25} {ptype:<6} {str(e.get('level', '--')):<3} "
                     f"{mark(e.get('approved')):<2} {mark(e.get('installed')):<2} "
                     f"{status:<16} {chapter:<24} {short(question)}")
    lines.append('')
    lines.append(f'Total: {len(rows)} | ' + ' | '.join(
        f'{s}: {counts.get(s, 0)}' for s in ('live', 'built-unapproved', 'not-built')))
    lines.append('Rendered types: ' + ', '.join(PUZZLE_TYPES))
    lines.append('Generated by build/puzzle-status.py from puzzle-data.yaml + puzzle-tracker.yaml')

    with open(args.out, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'puzzle-status: {len(rows)} puzzles cross-checked, written {os.path.relpath(args.out)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
