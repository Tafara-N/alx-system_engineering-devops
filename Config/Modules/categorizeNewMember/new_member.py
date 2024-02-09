#!/usr/bin/python3

"""
A function that categorizes new members according to their age and handicap
"""

def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result