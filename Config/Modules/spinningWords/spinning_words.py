#!/usr/bin/python3

"""
A function that takes in a string of one or more words, and returns
the same string, but with all words that have five or more letters reversed
"""


def spin_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] if len(word) >= 5 else word for word in words]
    return ' '.join(reversed_words)
