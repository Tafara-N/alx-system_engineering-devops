#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
"""


class Rectangle:
    """
    String representation
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

    def area(self):
        """
        Returns the area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns the rectangle's printable representation

        Represents the rectangle with a #(pound) character.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for h in range(self.__height):
            [rectangle.append("#") for w in range(self.__width)]
            if h != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)
