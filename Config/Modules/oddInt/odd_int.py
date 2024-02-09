#!/usr/bin/python3

"""
A function that finds an integer that appears an odd number of times.
"""


def find_it(seq):
    count_dict = {}
    
    # Count occurrences of each number in the array
    for num in seq:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the number with an odd occurrence
    for key, value in count_dict.items():
        if value % 2 != 0:
            return key
