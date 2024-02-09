#!/usr/bin/python3

"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
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
