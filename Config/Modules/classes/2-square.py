#!/usr/bin/python3

"""
A class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    A square with size validation
    """

    def __init__(self, size=0):
        """
        Initializing a new Square.

        Args:
            size (int): New square's size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

