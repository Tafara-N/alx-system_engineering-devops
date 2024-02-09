#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = [[x ** 2 for x in row] for row in matrix]
    return newMatrix
