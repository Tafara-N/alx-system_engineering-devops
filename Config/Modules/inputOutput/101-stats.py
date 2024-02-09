#!/usr/bin/python3

"""
A script that reads stdin line by line and computes metrics

After every 10 lines or on (CTRL + C), prints the following
statistics:
    - Total file size up to that line
    - Count of read status codes up to that line
"""


def print_stats(size, status_codes):
    """
    Prints the acquired metrics.

    Args:
        size (int): The acquired read file's size
        status_codes (dict): The acquired count of status codes
    """

    print("File size: {}".format(size))
    for key_value in sorted(stat_codes):
        print("{}: {}".format(key_value, stat_codes[key_value]))


if __name__ == "__main__":
    import sys

    size = 0
    stat_codes = {}
    real_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, stat_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in real_codes:
                    if stat_codes.get(line[-2], -1) == -1:
                        stat_codes[line[-2]] = 1
                    else:
                        stat_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, stat_codes)

    except KeyboardInterrupt:
        print_stats(size, stat_codes)
        raise
