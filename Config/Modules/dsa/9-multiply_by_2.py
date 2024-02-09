#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    myDictionary = dict(a_dictionary)
    for x, y in myDictionary.items():
        myDictionary[x] = y * 2
    return myDictionary
