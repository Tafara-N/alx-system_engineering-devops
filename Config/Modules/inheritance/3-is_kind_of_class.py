#!/usr/bin/python3

"""
A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Same class or inherit from

    Args:
        obj (any): Object to checked
        a_class (type): Class to match the type of obj to

    Returns:
        If the obj is an instance or inherited instance of a_class - True
        Otherwise - False
    """

    if isinstance(obj, a_class):
        return True
    return False
