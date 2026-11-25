#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings to /output/entry.txt.
The joke: the coffee machine files a formal HR complaint after the
alarm is snoozed -- a fresh twist on the Monday-morning snooze cliche.
"""

import os

ENTRY = "My Monday alarm went off at 6 a.m., so I hit snooze, and my coffee machine filed a formal complaint with HR."


def main() -> None:
    # Gate: 1-200 characters, single line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
