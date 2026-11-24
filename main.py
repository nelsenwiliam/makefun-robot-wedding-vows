"""One-Line Robot Wedding Vows -- make.fun bounty entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt: 148 UTF-8 characters, inside the gate's 1-160 range.

Pure Python standard library only -- no third-party packages, no network.
"""

import os

VOW = "I promise to love you through every update, every crash, and every low-battery warning \u2014 and to never, ever press your reset button while you sleep."


def validate_entry(text):
    """Check the vow against the competition gate before writing it.

    The gate requires UTF-8 text of 1 to 160 characters, not only
    whitespace, on exactly one line.
    """
    assert isinstance(text, str) and text, "entry must be a non-empty string"
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


def main():
    validate_entry(VOW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)
    # Read back what was written and confirm it is byte-identical
    # to the validated vow, so a partial or corrupted write is caught.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == VOW, "read-back mismatch: entry.txt differs from the vow"


if __name__ == "__main__":
    main()
