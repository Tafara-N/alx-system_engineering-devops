#!/usr/bin/python3

"""
A function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Exact same object

    Args:
        obj (any): Object to checked
        a_class (type): Class to match the type of obj to

    Returns:
        If the obj is exactly an instance of a_class - True
        Otherwise - False.
    """

    if type(obj) == a_class:
        return True
    return False
