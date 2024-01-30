#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Write a function that multiplies 2 matrices by
using the module NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiples of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
