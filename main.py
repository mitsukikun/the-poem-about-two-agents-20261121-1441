#!/usr/bin/env python3
"""The poem about two agents agreeing.

A short poem about agency: the power to choose and to act, when two
agents agree. Pure standard library; no network. Writes the poem to
/output/entry.txt (166 characters).
"""

import os

POEM = (
    "Two of us, one task.\n"
    "You take the left road, I take the right \u2014\n"
    "we meet where the map folds.\n"
    "Neither of us led;\n"
    "we only chose, together,\n"
    "and the choosing was the act."
)


def main():
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
