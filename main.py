#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after sweeping a glass off the table, to /output/entry.txt.
Deterministic and stdlib-only: the exact same sentence on every run.
"""

import os

SENTENCE = (
    "That glass had been squatting in my sunbeam all afternoon, "
    "so I served it an eviction notice \u2014 signed, sealed, paw-delivered."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
