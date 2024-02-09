#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Max = 0
    for key, value in a_dictionary.items():
        if value > Max:
            Max = value
    for key, value in a_dictionary.items():
        if value == Max:
            return key
