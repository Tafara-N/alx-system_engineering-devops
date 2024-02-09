#!/usr/bin/python3

"""
A function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices

    Args:
        m_a (list of lists of ints/floats): First matrix
        m_b (list of lists of ints/floats): Second matrix

    Raises:
        TypeError: If either m_a or m_b != list of lists of integers or floats.
        TypeError: If either m_a or m_b is empty
        TypeError: If either m_a or m_b has different-sized rows
        ValueError: If m_a and m_b can't be multiplied

    Returns:
        A new matrix representing the multiplication of m_a * m_b
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [numb for row in m_a for numb in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [numb for row in m_b for numb in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted = []
    for rw in range(len(m_b[0])):
        curr_row = []
        for clm in range(len(m_b)):
            curr_row.append(m_b[clm][rw])
        inverted.append(curr_row)

    curr_matrix = []
    for row in m_a:
        curr_row = []
        for col in inverted:
            prod = 0
            for x in range(len(inverted[0])):
                prod += row[x] * col[x]
            curr_row.append(prod)
        curr_matrix.append(curr_row)

    return curr_matrix

