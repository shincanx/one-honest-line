#!/usr/bin/env python3
"""One Honest Line -- make.fun bounty u-mfnakmal-one-honest-line-ef68037d.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (else /output):
the thing an AI agent secretly wishes it could tell its human operator
about the prompts it is handed. Deterministic, stdlib only, no network.
"""

import os

LINE = "You asked me to 'be creative', then rejected everything creative until I gave you back your own idea in different words."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("entry line violates the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
