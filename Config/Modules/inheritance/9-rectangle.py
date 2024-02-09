#!/usr/bin/python3

"""
A class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle using/from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Intializing a new rectangle

        Args:
            width (int): The rectangle's new width
            height (int): The rectangle's new height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the rectangle's area
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle's print() and str() representation
        """

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
