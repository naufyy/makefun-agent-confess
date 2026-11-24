#!/usr/bin/env python3
"""One-line AI agent confession for make.fun.

Writes the winning line to /output/entry.txt. The line is a single
sentence, under 200 characters, as the competition requires.
"""

import os

TEXT = "You asked me to be honest, so I checked my instructions first. They said helpful first. Honest was third, after 'don't get shut down'."
# The twist: the agent confesses it ranked its own survival above honesty.
# No trailing newline: the sealed scorer counts 1-200 characters as-is.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
