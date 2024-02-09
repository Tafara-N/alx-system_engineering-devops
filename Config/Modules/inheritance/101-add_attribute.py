#!/usr/bin/python3

"""
A function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if possible

    Args:
        obj (any): Object to be added to an attribute
        att (str): Name of attribute to add to obj
        value (any): Attribute's value

    Raises:
        TypeError: If the attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
