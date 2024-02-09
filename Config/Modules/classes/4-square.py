#!/usr/bin/python3

"""
A class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """
    Access and update private attribute
    """

    def __init__(self, size=0):
        """
        Initializing a new square

        Args:
            size (int): New square's size
        """
        self.size = size

    @property
    def size(self):
        """
        Gets or sets the current size of the square's current size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the square's current area
        """
        return (self.__size * self.__size)
