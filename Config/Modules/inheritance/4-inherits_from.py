#!/usr/bin/python3

"""
A function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Only subclass of

    Args:
        obj (any): Object to checked
        a_class (type): Class to match the type of obj to

    Returns:
        If the obj is an inherited instance of a_class - True
        Otherwise - False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
