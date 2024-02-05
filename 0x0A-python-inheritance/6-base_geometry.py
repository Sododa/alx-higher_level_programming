#!/usr/bin/python3
"""public instance method that raises an exception"""


class BaseGeometry:
    """public instance method basegeometry class"""
    def area(self):
        """raises an exception with message"""
        raise Exception("area() is not implemented")
