#!/usr/bin/python

"""
A program that finds the largest prime factor of the number 600 851 475 143
"""

factor = 2
largest_prime = 1
n = 600_851_475_143

while factor * factor <= n:
    if n % factor == 0:
        n //= factor
        largest_prime = factor
    else:
        factor += 1

if n > 1:
    largest_prime = n

print(f"The largest prime number of 600 851 475 143 is {largest_prime}")
