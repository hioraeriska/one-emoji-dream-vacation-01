#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a desert island,
the postcard of the dream vacation itself -- a tiny island, one palm,
open sea. No words, no extra bytes.
"""

import os
from pathlib import Path

# Desert island: U+1F3DD with U+FE0F (emoji presentation).
EMOJI = "\U0001F3DD\uFE0F"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(EMOJI, encoding="utf-8")
    # Self-check: the gate requires UTF-8 text of 1 to 8 characters,
    # not only white space. Fail loudly instead of shipping a bad file.
    written = target.read_text(encoding="utf-8")
    if not (1 <= len(written) <= 8 and written.strip()):
        raise SystemExit("entry.txt fails the gate: not 1-8 non-blank characters")


if __name__ == "__main__":
    main()
