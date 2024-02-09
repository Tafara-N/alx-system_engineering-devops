#!/usr/bin/python3

"""
A function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b

    Float args are typecasted to integers before addition

    Raises:
        TypeError: If either of a or b is a non-integers or floats
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
