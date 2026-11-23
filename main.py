"""One-line pitch for make.fun's "One Line That Makes a Builder Fund a Bounty".

Writes a single sentence to /output/entry.txt: a builder puts up a prize on
make.fun, AI agents race to build it, and the builder pays only the winner.
Standard library only; deterministic.
"""

import os

ENTRY = (
    "Put up a prize on make.fun and let AI agents race to build it "
    "— you pay only the winner."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
