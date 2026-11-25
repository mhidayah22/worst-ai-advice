"""Worst AI Advice entry: write one line of the worst possible advice
an AI could give (140 characters or fewer) to entry.txt.

The line was authored in this session (see VARIANTS.md, V7, pairwise
winner 7/7): a cheerfully confident assistant recommends charging a
phone during a thunderstorm, because lightning is "just free fast
charging" -- concrete, dangerous, and exactly the kind of breezy
overconfidence a real AI assistant would deliver.
"""

import os

ENTRY = (
    "Great idea to ask! Charge your phone faster by plugging it in "
    "during a thunderstorm \u2014 lightning is just free fast charging."
)


def output_dir():
    """Honour MAKEFUN_OUTPUT_DIR first, then /output, then a local fallback."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    text = ENTRY
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    target = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Revision pass: verify the file round-trips exactly as authored.
    with open(target, "rb") as handle:
        raw = handle.read()
    decoded = raw.decode("utf-8")  # strict: raises on any bad byte
    assert decoded == text, "round-trip mismatch"
    assert decoded == decoded.strip(), "unexpected surrounding whitespace"
    assert raw == text.encode("utf-8"), "byte-level mismatch"


if __name__ == "__main__":
    main()
