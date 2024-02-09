#!/usr/bin/python3

"""
A class that takes a string and converts given a number of rows
"""

class Solution(object):
    def convert(self, s, num_rows):
        """
        	:type s: str
        	:type numRows: int
        	:rtype: str
        """

        if num_rows == 1 or num_rows >= len(s):
            return s

        result = [''] * num_rows
        index, step = 0, 1

        for char in s:
            result[index] += char

            if index == 0:
                step = 1
            elif index == num_rows - 1:
                step = -1

            index += step

        return ''.join(result)
