"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. One line, at most 200 characters.
"""

import os


MAX_CHARS = 200


# The line is built from named beats so each machine-world detail is
# deliberate: the greeting, the machine's state, and the held snack.
# Slot B7 is the specific, speakable detail that makes the machine sound
# like itself instead of a generic flirt.
BEATS = {
    "greeting": "Hey",
    "stock": "I am fully stocked",
    "payment": "exact change only",
    "held_snack": "I have been holding your favourite snack in slot B7 since Tuesday",
}


def entry_text():
    """Compose the pickup line from its beats."""
    return (
        BEATS["greeting"]
        + " — "
        + BEATS["stock"]
        + ", "
        + BEATS["payment"]
        + ", and "
        + BEATS["held_snack"]
        + "."
    )


def validate(text):
    """Check the entry against the competition rules."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
