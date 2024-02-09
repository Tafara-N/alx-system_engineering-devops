#!/usr/bin/python3

"""
A function that adds binary numbers and returns a string representation
"""

def add_binary(a,b):
    decimal_sum = a + b
    
    # Converting the decimal sum to binary and removing '0b' prefix
    binary_sum = bin(decimal_sum)[2:]
    
    return binary_sum

result = add_binary(59, 100)
print(result)