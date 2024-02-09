#!/usr/bin/python3

"""
A function that replaces every letter with it's position in the alphabet
"""


def alphabet_position(text):
    """
    Given a string, replace every letter with it's position in the alphabet.
    """

    result = ""

    for char in text:
        if char.isalpha():
            # Convert the letter to its position in the alphabet and append it to the result string
            result += str(ord(char.lower()) - ord('a') + 1) + " "

    return result.strip()

sentence = "The sunset sets at twelve o' clock."
print(alphabet_position(sentence))