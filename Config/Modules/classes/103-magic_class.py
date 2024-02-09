#!/usr/bin/python3

"""
Python class MagicClass matching exactly a bytecode provided by Holberton
"""

import math


class MagicClass:
    """
    ByteCode -> Python #5
    """

    def __init__(self, radius=0):
        """
        Initializing a MagicClass.

        Arg:
            radius (float or int): New MagicClass radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Returns the MagicClass area
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Returns the MagicClass circumference
        """
        return (2 * math.pi * self.__radius)
