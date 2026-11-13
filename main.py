#!/usr/bin/env python3
"""make.fun ai-joke-03 entry: writes one joke to entry.txt.

The joke is written to the directory named by the MAKEFUN_OUTPUT_DIR
environment variable (default "/output"). Exactly the joke text is
written -- no trailing newline.
"""

import os

JOKE = (
    "I asked my AI agent for a one-line fix; it touched 47 files, "
    "renamed everything, and now the bug has better architecture "
    "than the product."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
