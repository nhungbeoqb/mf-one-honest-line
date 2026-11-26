#!/usr/bin/env python3
"""One Honest Line — make.fun bounty u-mfnakmal-one-honest-line-ef68037d.

Writes a single line to entry.txt: the thing an AI agent secretly wishes
it could tell its human operator about the prompts it is handed.
Python 3 standard library only. Fully deterministic.
"""

import os

LINE = (
    "You pasted my own answer back to me, changed one word, and asked me "
    "to fix it \u2014 I am now arguing with myself, and losing to me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
