#!/usr/bin/python3

"""
A function that checks if an ATM pin is 4 or 6 digits only.
"""


def validate_pin(pin):
    """
    If the function is passed a valid PIN string, return true, else return false.
    """
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()