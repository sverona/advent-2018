#!/usr/bin/env python
import argparse
from re import search


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('--part', type=int, help='part of problem (1 or 2)', default=1)

    args = parser.parse_args()

    shifts = open(args.infile).read().split("\n")[:-1]
    shifts = list(sorted(shifts))

    guard_id = None
    asleep_at = None
    awake_at = None

    sleeps = dict()
    for shift in shifts:
        if "#" in shift:
            guard_id = int(search("#([0-9]+)", shift).group(1))
            if guard_id not in sleeps.keys():
                sleeps[guard_id] = []

        if "falls asleep" in shift:
            asleep_at = int(search(":([0-9]+)]", shift).group(1))

        if "wakes up" in shift:
            awake_at = int(search(":([0-9]+)]", shift).group(1))
            sleeps[guard_id].extend(range(asleep_at, awake_at))

    if args.part == 1:
        sleepiest_guard, times = max(sleeps.items(), key=lambda i: len(i[1]))
        print(sleepiest_guard * max(set(times), key=lambda t: times.count(t)))
    elif args.part == 2:
        consistent_guard = None
        consistency = 0
        cons_minute = 0
        for guard, times in sleeps.items():
            if times:
                minute = max(set(times), key=lambda t: times.count(t))
                if times.count(minute) > consistency:
                    consistent_guard = guard
                    consistency = times.count(minute)
                    cons_minute = minute
        print(consistent_guard * cons_minute)


if __name__ == "__main__":
    __main__()
