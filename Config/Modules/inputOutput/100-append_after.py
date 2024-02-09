#!/usr/bin/python3

"""
A function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Search and update

    Args:
        filename (str): File's name
        search_string (str): String to be searched for in the file
        new_string (str): String to be inserted
    """

    words = ""

    with open(filename) as r:
        for line in r:
            words += line
            if search_string in line:
                words += new_string
    with open(filename, "w") as w:
        w.write(words)
