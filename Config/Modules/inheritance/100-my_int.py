#!/usr/bin/python3

"""
A class MyInt that inherits from int:
"""


class MyInt(int):
    """
    My integer
    """

    def __equ__(self, value):
        """
        Override == opeartor with != behavior.
        """

        return self.real != value

    def __nequ__(self, value):
        """
        Override != operator with == behavior.
        """

        return self.real == value
