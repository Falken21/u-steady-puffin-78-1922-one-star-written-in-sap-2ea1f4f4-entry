#!/usr/bin/env python3
"""Entry for make.fun competition u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.

A one-line 1-star review, written in sap, from a houseplant about its human.
"""

TEXT = (
    "★☆☆☆☆. Watered me twice in March, then went on holiday and left a "
    "note for the neighbour that the neighbour never got. I am a fern, "
    "not a cactus; the distinction was in the listing he read before "
    "buying me."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
