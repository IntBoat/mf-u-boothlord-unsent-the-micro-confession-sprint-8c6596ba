#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint (make.fun).

Writes the entry -- one two-part micro-confession: a to: line and the unsent message itself --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'To: the neighbour whose Wi-Fi I have borrowed for three years\nI was going to pay you back by fixing your printer, but then I remembered I only know how to turn it off and on again, and now I owe you a printer too.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
