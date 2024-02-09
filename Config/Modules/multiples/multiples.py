#!/usr/bin/python

"""
A program that finds the sum of all the multiples of 3 or 5 below 1000.
"""


sum = 0
limit = 1000

for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:  # Checks if i is a multiple of 3 or 5.
        sum += i  # Adds the multiples together.
print(sum)
