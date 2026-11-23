"""The One-Line Laugh — a single funny line, written to entry.txt.

The program holds one original one-liner and writes it, byte for byte,
to entry.txt on every run. No input, no network, no randomness:
the same line comes out every time.
"""

import os

LINE = (
    "I finally cleaned my room, and now I can't find anything "
    "\u2014 including the motivation that made me clean it in the first place."
)

TERMINATORS = ".!?"


def validate(line: str) -> None:
    """Enforce the entry rules; raise ValueError on any violation."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} characters, over the 200 limit")
    marks = sum(1 for ch in line if ch in TERMINATORS)
    if marks != 1:
        raise ValueError(f"line must have exactly one sentence terminator, found {marks}")
    if not line.endswith(tuple(TERMINATORS)):
        raise ValueError("line must end with its sentence terminator")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    # Read back and confirm the file holds exactly the validated line.
    with open(out_path, "rb") as f:
        if f.read() != data:
            raise ValueError("written entry.txt does not match the validated line")
    print(f"wrote {len(data)} bytes to {out_path}")
    print(f"character count: {len(LINE)}")
    print(LINE)


if __name__ == "__main__":
    main()
