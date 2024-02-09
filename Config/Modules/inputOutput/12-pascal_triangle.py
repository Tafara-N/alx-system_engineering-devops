#!/usr/bin/python3

"""
A function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Pascal's Triangle of size n

    Returns list of lists of integers representing the triangle
    """

    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]

        for x in range(len(tri) - 1):
            temp.append(tri[x] + tri[x + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
