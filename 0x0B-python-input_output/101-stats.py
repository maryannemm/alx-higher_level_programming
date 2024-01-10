#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Prints the metrics based on the accumulated data.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, status_codes):
    """
    Parses a line and updates the metrics.

    Args:
        line (str): Input line to be parsed.
        status_codes (dict): Dictionary containing the count of each status code.
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        status = int(parts[-2])
        
        total_size[0] += size
        status_codes[status] = status_codes.get(status, 0) + 1
    except ValueError:
        pass

if __name__ == "__main__":
    total_size = [0]
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parse_line(line.strip(), status_codes)

            if i % 10 == 0:
                print_metrics(total_size[0], status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size[0], status_codes)
        sys.exit(0)

