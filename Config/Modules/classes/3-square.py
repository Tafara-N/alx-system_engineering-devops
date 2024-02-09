#!/usr/bin/python3

"""
A class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """
    Area of square
    """

    def __init__(self, size=0):
        """
        Initializing a new square.

        Args:
            size (int): New square's size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the Square's current area
        """
        return (self.__size * self.__size)
