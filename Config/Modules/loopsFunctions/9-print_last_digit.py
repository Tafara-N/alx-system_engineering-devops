#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        last_num = (-number % 10)
    elif number >= 0:
        last_num = number % 10
    print("{:d}".format(last_num), end="")
    return last_num

