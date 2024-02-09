#!/usr/bin/python3

"""
A function that writes a string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    Write to a file

    Args:
        filename (str): Name of the file to write/edit
        text (str): Text to write/edit to that file

    Returns:
        Number of characters written/edited
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
