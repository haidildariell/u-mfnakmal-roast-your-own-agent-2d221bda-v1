#!/usr/bin/env python3
"""Roast Your Own Agent -- v1 entry.

Writes one original roast line of my own AI agent to /output/entry.txt.

The line is a single sentence, playful and self-deprecating, aimed at my
own agent -- never at a real person or group. Its angle is fresh on purpose:
not hallucination, not refusal, not a confident wrong answer, but the
agent's habit of over-deliberating every tiny question into a committee
project. Setup short, punchline last.
"""

import os

LINE = "My agent turns a yes-or-no question into a roadmap, a risk matrix, and a meeting to discuss the meeting."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()

    # Gate pre-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only white space. Fail loudly instead of writing
    # an invalid entry.
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"gate failed: entry is {len(text)} characters, must be 1-200"
        )
    if not text.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    # The entry is one line by definition: a roast that spills onto a
    # second line is not a single-line roast, so refuse it here.
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    # No trailing newline: every byte counts for the size tie-break,
    # so the file holds exactly the line, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
