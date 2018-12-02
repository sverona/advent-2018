#!/usr/bin/env python
import argparse
from itertools import combinations

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('--part', type=int, help='part of problem (1 or 2)', default=1)

    args = parser.parse_args()

    ids = open(args.infile).read().split("\n")[:-1]

    if args.part == 1:
        twos = 0
        threes = 0
        for ID in ids:
            counts = [ID.count(k) for k in 'qwertyuiopasdfghjklzxcvbnm']
            if 2 in counts:
                twos += 1
            if 3 in counts:
                threes += 1

        print(twos * threes)

    if args.part == 2:
        for id1, id2 in combinations(ids, 2):
            diffs = [c1 == c2 for c1, c2 in zip(id1, id2)]
            if diffs.count(False) == 1:
                print(id1)
                print(id2)

if __name__ == "__main__":
    __main__()
