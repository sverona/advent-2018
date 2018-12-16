#!/usr/bin/env python
import argparse
from string import ascii_lowercase


def react(polymer):
    annihilators = [s + s.upper() for s in ascii_lowercase]
    annihilators += [s.upper() + s for s in ascii_lowercase]

    while True:
        last_polymer = polymer
        for an in annihilators:
            polymer = polymer.replace(an, '')
        if last_polymer == polymer:
            return polymer


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('--part', type=int, help='part of problem (1 or 2)', default=1)

    args = parser.parse_args()

    polymer = open(args.infile).read().split("\n")[:-1][0]

    if args.part == 1:
        print(len(react(polymer)))
    elif args.part == 2:
        min_length = None
        for s in ascii_lowercase:
            this_polymer = polymer.replace(s, '')
            this_polymer = this_polymer.replace(s.upper(), '')
            this_polymer = react(this_polymer)
            if not min_length or min_length > len(this_polymer):
                min_length = len(this_polymer)

        print(min_length)


if __name__ == "__main__":
    __main__()
