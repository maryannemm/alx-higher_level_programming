#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1  # subtract 1 to exclude script name
    plural = "s" if argc != 1 else ""

    print("{:d} argument{:s}{:s}".format(argc, plural, ":" if argc else "."))

    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, argv[i]))

