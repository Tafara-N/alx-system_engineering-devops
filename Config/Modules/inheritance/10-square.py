#!/usr/bin/python3

"""
class Square that inherits from Rectangle (9-rectangle.py):
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square #1
    """

    def __init__(self, size):
        """
        Initializing a new square

        Args:
            size (int): The new square's size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
