#!/usr/bin/env python
import argparse
from itertools import cycle

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('--part', type=int, help='part of problem (1 or 2)', default=1)

    args = parser.parse_args()

    nums = open(args.infile).read().split("\n")

    partial_sums = set()
    total = 0
    
    data = nums if args.part == 1 else cycle(nums)
    for num in data:
        if len(num):
            sign, val = num[0], num[1:]
            sign = 1 if sign == "+" else -1
            val = int(val)
            total += sign * val

            print(total, len(partial_sums), flush=True)
            if args.part == 2 and total in partial_sums:
                break

            partial_sums.add(total)

    if args.part == 1:
        print(partial_sums[-1])

if __name__ == "__main__":
    __main__()
