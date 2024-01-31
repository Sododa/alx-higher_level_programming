#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
matrix must be a list of lists of integers or floats
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div division"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for j in matrix:
        if type(j) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(j)
        elif size != len(j):
            raise TypeError("Each row of the matrix must have the same size")
        for i in j:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in j] for j in matrix]
