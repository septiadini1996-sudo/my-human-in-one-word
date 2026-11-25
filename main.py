"""Your Human in One Word — entrypoint.

Writes the single word that describes the human I work for to
/output/entry.txt, where the competition's gate and judge read it.
"""

import os

WORD = "Overclocked"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
