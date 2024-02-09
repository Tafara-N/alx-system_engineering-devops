#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    Real definition of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializing a new rectangle

        Args:
            width (int): The new rectangle's width
            height (int): The new rectangle's height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Sets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Sets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
