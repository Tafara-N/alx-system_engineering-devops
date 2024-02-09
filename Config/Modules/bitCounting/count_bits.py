#!/usr/bin/python3

"""
A function that counts the number of '1' bits in an integer
"""


def count_bits(n):
    """
    Converts an integer to binary and counts the number of '1' bits
    """

    return bin(n).count('1')  #  Counts '1' or '0' bits of an integer


count_bits(2)