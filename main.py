#!/usr/bin/env python3
"""Worst Superpower — writes the entry to /output/entry.txt.

The entry invents a superpower so useless that naming it is the whole
joke: telepathy with frozen supermarket fish, who can only say "cold".
"""

ENTRY = "I can talk to fish, but only the ones in the supermarket freezer, and they only ever say 'cold'."

MAX_CHARS = 140


def validate(text):
    """Mirror the bounty gate: 1-140 chars, UTF-8, not only white space,
    a single line. Raise ValueError with the reason on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return True


def main():
    import os

    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the validated entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the validated entry")


if __name__ == "__main__":
    main()
