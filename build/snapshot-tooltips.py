#!/usr/bin/env python3
"""Snapshot every tooltip in the built HTML for post-change regression diff."""
import re, json, sys, hashlib

HTML = "docs/downloads/Relinquishment.html"
OUT = "build/test-fixtures/tooltips-baseline.json"

def main():
    with open(HTML) as f:
        html = f.read()

    # For every element carrying a tooltip, capture its visible text + tooltip data
    # Pattern matches both <span class="hover-term ..."> and <summary class="hover-nav">
    snapshot = {}

    # Find every element with data-hover-id
    for m in re.finditer(r'<(\w+)[^>]*data-hover-id="([^"]+)"[^>]*>([^<]*)</\1>', html):
        tag, hid, visible = m.group(1), m.group(2), m.group(3)
        full_tag = m.group(0)
        text_attr = re.search(r'data-hover="([^"]*)"', full_tag)
        html_attr = re.search(r'data-hover-html="([^"]*)"', full_tag)
        snapshot.setdefault(hid, []).append({
            "tag": tag,
            "visible": visible,
            "text": text_attr.group(1) if text_attr else None,
            "html": html_attr.group(1) if html_attr else None,
        })

    # Also: count terms without data-hover-id (these have inline data-hover but no key)
    keyless = re.findall(r'<\w+[^>]*data-hover="([^"]*)"[^>]*>', html)
    keyless_no_id = [v for v in keyless if 'data-hover-id' not in v]

    output = {
        "snapshot_count": len(snapshot),
        "total_occurrences": sum(len(v) for v in snapshot.values()),
        "keyless_inline_count": len(keyless_no_id),
        "by_id": snapshot,
    }

    import os
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(output, f, indent=2, sort_keys=True)
    print(f"Snapshotted {output['snapshot_count']} unique tooltip IDs across {output['total_occurrences']} occurrences")
    print(f"Plus {output['keyless_inline_count']} keyless inline tooltips (will need migration tracking)")

if __name__ == "__main__":
    main()
