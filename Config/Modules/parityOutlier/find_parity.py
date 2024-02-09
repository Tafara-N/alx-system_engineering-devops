#!/usr/bin/python3

"""
A function that takes an array as an argument and returns this "outlier" N.
"""

def find_outlier(integers):
    even_numbers = [number for number in integers if number % 2 == 0]
    odd_numbers = [number for number in integers if number % 2 != 0]

    # Check if the outlier is an even or odd number
    if len(even_numbers) == 1:
        return even_numbers[0]
    else:
        return odd_numbers[0]
    
test = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(test))