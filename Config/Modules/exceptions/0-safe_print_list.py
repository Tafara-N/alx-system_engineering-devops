#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    returned = 0
    for y in range(x):
        try:
            print('{}'.format(my_list[y]), end='')
            returned += 1
        except IndexError:
            break
    print('')
    return (returned)
