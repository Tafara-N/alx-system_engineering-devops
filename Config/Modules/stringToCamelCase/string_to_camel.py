#!/usr/bin/python3

"""
A function that converts dash/underscore delimited words into camel casing
"""

def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    return words[0] + ''.join(word.title() for word in words[1:])
