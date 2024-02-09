#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        str = str[0:n] + str[n+1:]
    return str

