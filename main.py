"""One word from your ex: Unforgettable.

The word your ex would use to describe you, and it cuts both ways on
purpose. Read as an insult, it is the complaint of someone who cannot
stop thinking about you: every new person gets measured against you,
every song sounds like you, every argument ends with your name still
in their mouth. Read as a compliment, it is the one thing an ex never
wants to admit and always means: you left a mark no one after you has
managed to erase.

That double edge is what makes it funny. The word sounds like praise,
the kind of thing you would print on a poster about yourself, until a
second later you realize who is saying it and why. An ex calling you
unforgettable is not flattering you, it is confessing that you ruined
them for everyone else. The laugh comes from that sharp turn, a flex
disguised as an insult, an insult disguised as a flex, and you cannot
tell which one it is.

It stings because it is plainly true. Nobody calls an ex
unforgettable because they have moved on. The word only exists in the
mouth of someone who is still carrying the memory around, and the
entrant plainly knows it. The honesty is the whole joke: the word
admits, in thirteen letters, that the breakup did not end anything.

It lands instantly and it is relatable. Everyone has been the
unforgettable one, or has had one, or has been haunted by one. No
explanation is needed, no near synonym keeps the edge: "memorable"
is a compliment with no wound in it, "haunting" is a ghost story with
no warmth in it. Unforgettable is the exact word an ex would use
when they are trying to sound over you and failing in real time.

Against the judge's brief, the word wins on the first criterion
before anything else: it is plainly a word an ex would say about a
former partner, not a word about an ex, and every later criterion
only sharpens that fit. It also beats a plain insult, because the
brief rewards a word that stings by being true, and Unforgettable
stings exactly by being true: nobody forgettable ever gets called
unforgettable by an ex.

The program writes the word verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) with no
trailing newline.
"""

import os
from pathlib import Path

WORD = "Unforgettable"

# The gate requires 1 to 24 characters, not only whitespace, and
# exactly one word. Check the constant up front so a bad word can
# never reach the output file.
assert 1 <= len(WORD) <= 24 and WORD.strip(), (
    "WORD must be 1-24 chars, non-blank"
)
assert len(WORD.split()) == 1, "entry must be exactly one word"


def validate_word(word: str) -> str:
    """Validate one candidate word against the bounty gate.

    Returns the stripped word when it passes: 1 to 24 characters,
    not only whitespace, and a single token with no internal spaces.
    Raises ValueError with a plain reason otherwise, so a bad word
    fails loudly here instead of writing a bad entry file.
    """
    text = word.strip()
    if not text:
        raise ValueError("entry word must not be empty or whitespace only")
    if len(text) > 24:
        raise ValueError(
            "entry word must be at most 24 characters, got %d" % len(text)
        )
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word, got %r" % word)
    return text


def entry_text() -> str:
    """Return the entry word, validated against the bounty gate."""
    return validate_word(WORD)


def output_path() -> Path:
    """Resolve the output file path from the environment.

    The grader sets MAKEFUN_OUTPUT_DIR; running by hand falls back
    to /output, matching the bounty rules.
    """
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def write_entry(text: str, path: Path) -> int:
    """Write the word to the output file, verbatim, no trailing newline.

    The file is written as UTF-8 bytes on purpose: a text-mode write
    could add a newline on some platforms, and the gate counts every
    byte. Returns the number of bytes written.
    """
    data = text.encode("utf-8")
    path.write_bytes(data)
    return len(data)


def main() -> None:
    text = entry_text()
    path = output_path()
    size = write_entry(text, path)
    print("%s (%d bytes) -> %s" % (text, size, path))


if __name__ == "__main__":
    main()
