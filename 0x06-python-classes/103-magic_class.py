#!/usr/bin/python3
"""Defines class MagicClass"""
import math


class MagicClass:
    """
    Class that defines properties of MagicClass.

    Attributes:
        radius: radius of circle
    """
    def __init__(self, radius=0):
        """Creates new instances of MagicClass.

        Args:
            radius: radius of circle

        Raises:
            TypeError: radius must be a number .
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area

        Returns: area.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns circumference for circle

        Returns: circumference for circle.
        """
        return 2 * math.pi * self.__radius
