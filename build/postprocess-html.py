#!/usr/bin/env python3
"""Post-process HTML: upgrade collapsible sentinels to <details>."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from collapsible import postprocess_html

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <html-file>", file=sys.stderr)
        sys.exit(1)
    postprocess_html(sys.argv[1])
