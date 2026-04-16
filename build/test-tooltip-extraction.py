#!/usr/bin/env python3
"""Plan 0205 regression test: verify tooltip externalization is complete and lossless."""
import re, json, sys, os
import html as htmllib

HTML = "docs/downloads/Relinquishment.html"
BASELINE = "build/test-fixtures/tooltips-baseline.json"


def main():
    with open(HTML) as f:
        html = f.read()
    with open(BASELINE) as f:
        baseline = json.load(f)

    failures = []

    # --- Test 1: JSON block exists and is valid ---
    m = re.search(r'<script type="application/json" id="hover-data">(.*?)</script>', html, re.DOTALL)
    if not m:
        failures.append("FATAL: <script id='hover-data'> block missing")
        print_results(failures)
        sys.exit(1)
    raw_json = m.group(1).replace('<\\/', '</')  # reverse the </-escape
    try:
        hover_data = json.loads(raw_json)
    except json.JSONDecodeError as e:
        failures.append(f"FATAL: hover-data JSON invalid: {e}")
        print_results(failures)
        sys.exit(1)
    print(f"OK: hover-data block parsed, {len(hover_data)} unique keys")

    # --- Test 2: No orphan data-hover-id refs (every reference has a dict entry) ---
    refs = set(re.findall(r'data-hover-id="([^"]+)"', html))
    orphans = refs - set(hover_data.keys())
    if orphans:
        failures.append(f"ORPHAN refs (no JSON entry): {sorted(orphans)[:10]}")
    else:
        print(f"OK: all {len(refs)} data-hover-id refs resolve to JSON keys")

    # --- Test 3: No inline data-hover / data-hover-html on body hover-term spans ---
    inline_text = re.findall(r'<span class="hover-term[^"]*"[^>]*\sdata-hover="', html)
    inline_html = re.findall(r'<span class="hover-term[^"]*"[^>]*\sdata-hover-html="', html)
    if inline_text:
        failures.append(f"REGRESSION: {len(inline_text)} hover-term spans still carry inline data-hover")
    if inline_html:
        failures.append(f"REGRESSION: {len(inline_html)} hover-term spans still carry inline data-hover-html")
    if not inline_text and not inline_html:
        print("OK: no inline tooltip attrs remain on hover-term spans")

    # --- Test 4: Lossless content — every baseline tooltip's content survives in JSON dict ---
    losses = []
    for hid, occurrences in baseline["by_id"].items():
        if hid not in hover_data:
            losses.append(f"LOST KEY: {hid}")
            continue
        baseline_text = occurrences[0].get("text")
        baseline_html = occurrences[0].get("html")
        dict_text = hover_data[hid].get("t")
        dict_html = hover_data[hid].get("h")
        if baseline_text and dict_text != htmllib.unescape(baseline_text):
            # Tolerate the placeholder reset: title-line entries had data-hover="placeholder"
            # but real content is now in dict_text from YAML.
            if not (htmllib.unescape(baseline_text) == "placeholder" and dict_text):
                losses.append(f"TEXT MISMATCH: {hid}")
        if baseline_html and dict_html != htmllib.unescape(baseline_html):
            losses.append(f"HTML MISMATCH: {hid}")
    if losses:
        failures.append(f"CONTENT LOSS ({len(losses)} items): {losses[:10]}")
    else:
        print(f"OK: all {len(baseline['by_id'])} baseline tooltips present and lossless")

    # --- Test 5: Size reduction vs baseline (regression gate) ---
    new_size = os.path.getsize(HTML)
    baseline_size = 879_616  # captured pre-Plan-0205 (859K)
    reduction = baseline_size - new_size
    min_reduction = 30_000
    if reduction < min_reduction:
        failures.append(
            f"SIZE REGRESSION: reduction {reduction:,}B < {min_reduction:,}B minimum "
            f"(current {new_size:,}B, baseline {baseline_size:,}B)"
        )
    else:
        print(
            f"OK: file size {new_size:,}B ({new_size/1024:.0f}K); "
            f"reduction {reduction:,}B ({reduction/1024:.0f}K) from {baseline_size:,}B baseline"
        )

    print_results(failures)
    sys.exit(0 if not failures else 1)


def print_results(failures):
    if not failures:
        print("\nALL TESTS PASSED")
    else:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print(f"  {f}")


if __name__ == "__main__":
    main()
