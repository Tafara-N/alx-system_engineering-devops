#!/usr/bin/python3

"""
A function that appends a string at the end of a text file (UTF8) and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append to a file

    Args:
        filename (str): Name of the file to be appended to
        text (str): String to be appended to the file

    Returns:
        Number of characters appended
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
