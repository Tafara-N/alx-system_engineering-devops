#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDictionary = sorted(a_dictionary)
    for i in sortedDictionary:
        print("{}: {}".format(i, a_dictionary[i]))
