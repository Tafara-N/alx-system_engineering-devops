#!/usr/bin/python3

"""
A function that multiplies 2 matrices by using the module NumPy
"""

import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """
    Lazy matrix multiplication

    Returns multiplication of two matrices

    Args:
        m_a (list of lists of ints/floats): First matrix
        m_b (list of lists of ints/floats): Second matrix
    """

    return (npy.matmul(m_a, m_b))
