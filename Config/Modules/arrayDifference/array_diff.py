#!/usr/bin/python3

"""
A difference function, which subtracts one list from
another and returns the result.
"""


def array_diff(a, b):
    result = [element for element in a if element not in b]
    return result