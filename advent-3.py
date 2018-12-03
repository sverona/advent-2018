#!/usr/bin/env python
import argparse
from re import search


def claim_squares(claim):
    match = search("#(.*) @ (\d+),(\d+): (\d+)x(\d+)", claim)
    (ID, left, top, width, height) = [int(x) for x in match.groups()]
    for w in range(left + 1, left + width + 1):
        for h in range(top + 1, top + height + 1):
            yield (w, h)


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('--part', type=int, help='part of problem (1 or 2)', default=1)

    args = parser.parse_args()

    claims = open(args.infile).read().split("\n")[:-1]

    claimed_squares = set()
    dupes = set()
    for claim in claims:
        for sq in claim_squares(claim):
            if sq in claimed_squares:
                dupes.add(sq)
            else:
                claimed_squares.add(sq)

    if args.part == 1:
        print(len(dupes))
    if args.part == 2:
        for claim in claims:
            if not set(claim_squares(claim)) & dupes:
                print(claim)
        
if __name__ == "__main__":
    __main__()
