#!/usr/bin/python3

"""
A class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """
    Printing a square
    """

    def __init__(self, size):
        """
        Initializing a new square

        Args:
            size (int): New square's current size
        """
        self.size = size

    @property
    def size(self):
        """
        Gets or sets the square's current size
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
        Returns the square's current area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square with the # character
        """
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
