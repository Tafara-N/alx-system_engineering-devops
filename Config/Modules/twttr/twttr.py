#!/usr/bin/python3

"""
A program that  prompts the user for a str of text and then outputs
that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""


def twitter(sentence):
    """ Just setting up my twttr """

    vowels = "aeiouAEIOU"  # List of vowels to remove
    sentence = "".join([vowel for vowel in sentence if vowel not in vowels])
    return sentence


string = input("Input: ")
print(f"Output: {twitter(string)}")
