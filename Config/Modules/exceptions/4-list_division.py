#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for y in range(0, list_length):
        try:
            division = my_list_1[y] / my_list_2[y]
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            my_list_3.append(division)
    return (my_list_3)
