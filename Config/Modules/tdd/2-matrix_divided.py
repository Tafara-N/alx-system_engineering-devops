#!/usr/bin/python3

"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix

    Args:
        matrix (list): A list of lists of integers or floats
        div (int/float): Divider

    Raises:
        TypeError: If the matrix holds non-numbers
        TypeError: If the matrix holds rows of different sizes
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is zero(0)

    Returns:
        A new matrix representing the result of the division
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elmnt, int) or isinstance(elmnt, float))
                    for elmnt in [nmb for row in matrix for nmb in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda n: round(n / div, 2), row)) for row in matrix])
