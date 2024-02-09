#!/usr/bin/python3

"""
A class MyList that inherits from list
"""


class MyList(list):
    """
    Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        """

        print(sorted(self))
