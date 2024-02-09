#!/usr/bin/python3

"""
A function that takes a string and return a new string with all vowels removed.
"""


def disemvowel(string_):
    vowels = "aeiouAEIOU"  # List of vowels to remove
    string_ = "".join([vowel for vowel in string_ if vowel not in vowels])
    return string_

text = "This website is for losers LOL!"
stripped_text = disemvowel(text)  # Calling our function to strip the vowels 

print(stripped_text)