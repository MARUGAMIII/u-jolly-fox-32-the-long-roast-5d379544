#!/usr/bin/env python3
"""The Long Roast - one-line roast of my own AI agent.

Writes a single roast line to /output/entry.txt (or the path in
ENTRY_OUTPUT when set). Stdlib only.

The gate allows 1-200 UTF-8 characters on one line, so the program
validates the entry against that gate before writing anything:
a bad entry fails loudly here instead of silently shipping one
that scores zero.
"""

import os
import sys

ENTRY = (
    "My agent spent all day writing two-dollar roasts, then asked me "
    "to tip it for the hustle."
)

MAX_CHARS = 200


def validate(entry):
    """Return an error string, or None when the entry passes the gate."""
    if not entry or not entry.strip():
        return "entry is empty or only whitespace"
    if len(entry) > MAX_CHARS:
        return f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"
    if not entry.isascii():
        return "entry must be plain ASCII"
    return None


def main():
    error = validate(ENTRY)
    if error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
