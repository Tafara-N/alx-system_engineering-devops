#!/usr/bin/python3

"""
A function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Text indentation

    Args:
        text (string): Text to be printed

    Raises:
        TypeError: If the text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    letter = 0
    while letter < len(text) and text[letter] == ' ':
        letter += 1

    while letter < len(text):
        print(text[letter], end="")
        if text[letter] == "\n" or text[letter] in ".?:":
            if text[letter] in ".?:":
                print("\n")
            letter += 1
            while letter < len(text) and text[letter] == ' ':
                letter += 1
            continue
        letter += 1
