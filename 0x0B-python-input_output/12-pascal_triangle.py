#!/usr/bin/python3
"""Create a function def pascal_triangle(n):"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s,
    triange
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for j in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
