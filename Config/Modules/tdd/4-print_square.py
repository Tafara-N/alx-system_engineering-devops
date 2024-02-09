#!/usr/bin/python3

"""
A function that prints a square with the character #.
"""


def print_square(size):
    """
    Print square

    Args:
        size (int): Height/width of the square

    Raises:
        TypeError: If size is not int
        ValueError: If size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
