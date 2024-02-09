#!/usr/bin/python3

"""
A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    Improve Geometry
    """

    def area(self):
        """
        Raises an Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator

        Args:
            name (str): Parameter's name
            value (int): Parameter to validate

        Raises:
            TypeError: If value is not an int
            ValueError: If value is <= 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
