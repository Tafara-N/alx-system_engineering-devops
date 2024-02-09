#!/usr/bin/python3

"""
A function that counts the number of bits in an integer
"""


def count_bits(n):
    """
    Converts an integer to binary and counts the number of bits
    """

    return bin(n).count('1') + bin(n).count('0')


print(count_bits(45))