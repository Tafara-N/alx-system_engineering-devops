#!/usr/bin/python3

def magic_calculation(a, b):
    results = 0
    for y in range(1, 3):
        try:
            if y > a:
                raise Exception('Too far')
            results += a ** b / y
        except Exception:
            results = b + a
            break
    return results
