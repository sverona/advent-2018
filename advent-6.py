#!/usr/bin/env python
import argparse
from string import ascii_lowercase, ascii_uppercase


def manhattan(c1, c2):
    d = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
    return int(d)


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('--part', type=int, help='part of problem (1 or 2)', default=1)

    args = parser.parse_args()

    coords = open(args.infile).read().split("\n")[:-1]
    coords = [[int(c) for c in coord.split(",")] for coord in coords]

    max_x = max(coord[0] for coord in coords)
    max_y = max(coord[1] for coord in coords)

    if args.part == 1:
        map = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]
        sizes = [0 for _ in coords]
    elif args.part == 2:
        count = 0

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            distances = [manhattan((x, y), c) for c in coords]

            if args.part == 1:
                if distances.count(min(distances)) == 1:
                    idx = distances.index(min(distances))
                    map[x][y] = (ascii_uppercase + ascii_lowercase)[idx]
                    if sizes[idx] is not None:
                        sizes[idx] += 1
                    if x in (0, max_x) or y in (0, max_y):
                        sizes[idx] = None

            elif args.part == 2:
                if sum(distances) < 10000:
                    count += 1

    if args.part == 1:
        print(max(size for size in sizes if size))
    elif args.part == 2:
        print(count)


if __name__ == "__main__":
    __main__()
