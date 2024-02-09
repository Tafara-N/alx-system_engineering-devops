#!/usr/bin/python3

"""
A class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square #2
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
