#!/usr/bin/python3

"""
A function that sums the digits of number
"""

def digital_root(n):
    digits_sum = 0

    while n >= 10:
        n_str = str(n)
        for single_digit in n_str:
            digit = int(single_digit)
            digits_sum += digit
        
        n = digits_sum
        digits_sum = 0

    return print(n)

number = int(input("Enter a number: "))
digital_root(number)