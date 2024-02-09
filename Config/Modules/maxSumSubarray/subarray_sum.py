#!/usr/bin/python3

"""
A function that finds the maximum sum ofa subarray.
"""


def max_sequence(arr):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum if max_sum > 0 else 0
