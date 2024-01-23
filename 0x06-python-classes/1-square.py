#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class defines properties of square by: (based on 0-square.py).

    Attributes:
        size: square size (1 side).
    """
    def __init__(self, size):
        """Creates new instances for square (1 side).

        Args:
            size: square size.
        """
        self.__size = size
