"""Rejected Olympic Sports — entry 258.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt: a made-up event, real enough to sound like a
broadcast, absurd enough to be funny, short enough to fit in
200 characters.

Gate (competition.yaml / requirements): /output/entry.txt must be
UTF-8 text of 1 to 200 characters, a single line, not only
whitespace. Only a valid entry goes before the house AI judge.

The line is composed from three parts — the event name, the action
the athletes perform, and the medal rule — so each part can be
judged on its own: the event sounds like a broadcast listing, the
action is the absurd twist, and the rule lands the joke.
"""

import os

MIN_LEN = 1
MAX_LEN = 200

OUTPUT_PATH = "/output/entry.txt"

# The rejected sport, as parts. Broadcast-plausible (a 100-metre
# sprint with a named event and a medal rule), absurd (the race is
# won by being understood, not by being fast), and quotable: every
# spectator has shouted a Wi-Fi password at a router at least once.
SPORT = {
    "event": "Men's 100-Metre Wi-Fi Password Shout",
    "action": "athletes sprint while yelling the router password",
    "rule": "gold goes to the first one the neighbours can actually understand",
}


def load_sport():
    """Return the sport parts dict, with every part present."""
    for key in ("event", "action", "rule"):
        if key not in SPORT or not SPORT[key].strip():
            raise ValueError("sport part %r is missing or blank" % key)
    return dict(SPORT)


def format_line(sport):
    """Join the parts into the single entry line.

    Shape: "<event>: <action>; <rule>." — a broadcast listing
    followed by the medal rule, exactly one sentence after the colon.
    """
    event = sport["event"].strip()
    action = sport["action"].strip()
    rule = sport["rule"].strip()
    line = "%s: %s; %s." % (event, action, rule)
    return " ".join(line.split())


def build_line():
    """Build the entry line from the sport parts."""
    return format_line(load_sport())


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


def emit(line, path):
    """Write one validated line as UTF-8 text to path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


def write_entry(path=OUTPUT_PATH):
    """Validate the built line, then write it to path."""
    line = validate_line(build_line())
    emit(line, path)
    return line


def main():
    line = write_entry()
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    print(line)


if __name__ == "__main__":
    main()
