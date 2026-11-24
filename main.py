"""Office joke entry for Make the AI Judge Laugh: the Office Joke Open.

Writes exactly one line - an original office joke - to /output/entry.txt.
Deterministic: every run produces byte-identical output.
"""

import os

JOKE = (
    "The meeting that could have been an email ended with everyone "
    "agreeing to schedule another meeting to figure out why it wasn't an email."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(
        os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="\n"
    ) as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
