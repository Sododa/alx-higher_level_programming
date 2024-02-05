#!/usr/bin/python3
"""public instance method that raises an exception"""


class BaseGeometry:
    """public instance method that raises an exception"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        b = type(value)
        if b != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
