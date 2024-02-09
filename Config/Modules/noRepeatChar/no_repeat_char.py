#!/usr/bin/python3

"""
A function that  find the length of the longest
substring without repeating characters.
"""


def length_of_longest_substring(self, s):
    """
    :type s: str
    :rtype: int
    """

    char_index_map = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length
