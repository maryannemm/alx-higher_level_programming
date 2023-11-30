#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1  # subtract 1 to exclude script name

    result = sum(int(arg) for arg in argv[1:])

    print(result)

