"""One-Line Robot Wedding Vows -- make.fun bounty entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt: 148 UTF-8 characters, inside the gate's 1-160 range.

Pure Python standard library only -- no third-party packages, no network.
"""

import os

VOW = "I promise to love you through every update, every crash, and every low-battery warning \u2014 and to never, ever press your reset button while you sleep."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
