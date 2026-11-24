#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry (program/v1).

Writes one original two-sentence horror story to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Pure Python standard library — no third-party dependencies, no network,
no input files. Deterministic: the same story on every run.

The story is written to satisfy the published judge brief, in the order
the judge weighs its criteria:

1. Exactly two sentences, genuinely frightening.
2. The second sentence turns on the first: six silent years of "safety"
   become the proof that the threat was never outside at all.
3. The horror is implied, never explained: the story never says what set
   the alarm off, only that every door and window was still locked from
   the inside — the reader fills in the worst of it.
4. Precise and concrete: one alarm, one panel, one night, no wasted word.
5. Original: no familiar twist retold (no dead wife, no call from inside
   the house, no monster under the bed).
"""

import os
import sys

STORY = (
    "I set the house alarm every night before bed, "
    "and it has never gone off once in six years. "
    "Last night it went off at 3 AM \u2014 and when I checked the panel, "
    "every door and window was still locked from the inside."
)

MAX_CHARS = 400
TERMINATORS = ".!?"


def sentence_count(text):
    """Count sentences: a terminator followed by space/end of text."""
    count = 0
    for i, ch in enumerate(text):
        if ch in TERMINATORS:
            if i + 1 == len(text) or text[i + 1] in " \t\r\n\"'\u201d":
                count += 1
    return count


def check_story(text):
    """Self-check the same gate the sealed scorer applies, plus the
    exactly-two-sentences rule from the judge brief."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "story is %d chars, must be 1..%d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("story is blank")
    n = sentence_count(text)
    if n != 2:
        raise SystemExit("story has %d sentences, must be exactly 2" % n)


def main():
    check_story(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the story, which also keeps
    # the byte size minimal (an exact tie on win rate goes to the smaller
    # text first).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    # Verify what was written: read it back and re-check the gate on the
    # exact bytes the judge will read, so a partial write can never pass
    # silently.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != STORY:
        raise SystemExit("entry.txt does not match the story after writing")
    check_story(written)
    print("wrote %d chars (%d bytes) to %s"
          % (len(STORY), len(STORY.encode("utf-8")), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
