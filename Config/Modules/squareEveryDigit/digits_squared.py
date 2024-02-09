#!/usr/bin/python3

"""
A function squares every digit of a number and concatenates them
"""


def square_digits(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)

    # Square each digit and convert it back to an int
    squared_digits = [int(digit) ** 2 for digit in num_str]

    # Concatenate the squared digits and convert the result to an integer
    result = int(''.join(map(str, squared_digits)))

    return result
