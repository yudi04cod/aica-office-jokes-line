#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Python standard library only; no network,
no secrets, no randomness — the output is fully deterministic.
"""

import os

LINE = (
    "I hit reply-all to ask everyone to stop replying-all, "
    "and now the thread has its own HR case number."
)


def main() -> None:
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text:
        raise SystemExit("entry must not be blank")
    if not (1 <= len(text) <= 199):
        raise SystemExit(f"entry length {len(text)} out of range 1-199")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
