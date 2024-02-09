#!/usr/bin/python3

"""
A function that takes an integer (prod) and returns an array
"""

def product_fib(prod):
    num, num_plus_1 = 0, 1
    
    while num * num_plus_1 < prod:
        # Calculating the next Fibonacci numbers
        num, num_plus_1 = num_plus_1, num + num_plus_1

    # Result based on the comparison of the product
    return [num, num_plus_1, num * num_plus_1 == prod]