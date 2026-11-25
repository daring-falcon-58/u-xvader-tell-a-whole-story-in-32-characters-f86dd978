#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — entry program.

Writes the winning Wi-Fi network name to /output/entry.txt (the sealed
scorer reads that file: UTF-8, 1-32 chars, not only whitespace) and prints
exactly the name to stdout, nothing else.

Winning name, chosen in-session from 36 scored candidates (see
candidates.md): "Router Saw My Search History" — 28 characters, self-score
36/40 against the judge brief (joke first, then story, freshness, tightness).
"""

import os
import sys

ENTRY = "Router Saw My Search History"


def main() -> int:
    # The harness mounts the output dir at /output and sets
    # MAKEFUN_OUTPUT_DIR from it; fall back to /output when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
