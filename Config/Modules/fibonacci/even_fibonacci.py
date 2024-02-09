#!/usr/bin/python

"""
A program that finds the sum of even fibonacci numbers under 4 000 000
"""

x, y = 1, 2  # Starting values for our fibonacci numbers.
even = 0
limit = 4_000_000

while x <= limit:
    if x % 2 == 0:
        even += x

    x, y = y, x + y  # Updates the sequence of our fibonacci numbers.

print(even)

