"""One-line worst AI advice entry for the make.fun
'Worst AI Advice: The 48-Hour Tight Line Open' bounty.

Writes a single line of deliberately terrible advice, in the
confident, tidy voice of an AI assistant, to /output/entry.txt.
"""

import os

ADVICE = (
    "For stronger security, use the same password for every "
    "account \u2014 you only have to remember one, and so do hackers."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE)


if __name__ == "__main__":
    main()
