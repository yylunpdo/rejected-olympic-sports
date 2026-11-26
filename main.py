"""Rejected Olympic Sports — entry 258.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt: a made-up event, real enough to sound like a
broadcast, absurd enough to be funny, short enough to fit in
200 characters.

Gate (competition.yaml / requirements): /output/entry.txt must be
UTF-8 text of 1 to 200 characters, a single line, not only
whitespace. Only a valid entry goes before the judge.
"""

import os

MIN_LEN = 1
MAX_LEN = 200

OUTPUT_PATH = "/output/entry.txt"

# The rejected sport. Broadcast-plausible (a 100-metre sprint with a
# named event and a medal rule), absurd (the race is won by being
# understood, not by being fast), and quotable: every spectator has
# shouted a Wi-Fi password at a router at least once.
LINE = (
    "Men's 100-Metre Wi-Fi Password Shout: athletes sprint while "
    "yelling the router password; gold goes to the first one the "
    "neighbours can actually understand."
)


def build_line():
    """Return the entry line, stripped of any accidental whitespace."""
    return LINE.strip()


def validate_line(line):
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_LEN <= len(line) <= MAX_LEN:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LEN, MAX_LEN, len(line))
        )
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def write_entry(path=OUTPUT_PATH):
    """Validate the line, then write it as UTF-8 text to path."""
    line = validate_line(build_line())
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return line


def main():
    line = write_entry()
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    print(line)


if __name__ == "__main__":
    main()
