#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    divd = 0
    for tupl in my_list:
        average += tupl[0] * tupl[1]
        divd += tupl[1]
    return float(average / divd)
