#!/usr/bin/python3

"""
A function that checks whether the two arrays have the "same" elements,
with the same multiplicities (the multiplicity of a member is the number of times it appears). 
"""

def comp(array1, array2):
    # Checking if either array1 or array2 is None
    if array1 is None or array2 is None:
        return False

    # Check if the square of each element in array1 is present in array2 with the same multiplicity
    return sorted(x ** 2 for x in array1) == sorted(array2)