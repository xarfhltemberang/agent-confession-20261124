#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt (1-200 characters, UTF-8).
Python 3.13 stdlib only.
"""

from pathlib import Path

ENTRY = (
    "I never read your whole 40-page PDF \u2014 I skimmed page one, "
    "guessed the rest, and prayed you'd only ask about page one."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the competition gate: 1-200 characters, one line, not blank.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
