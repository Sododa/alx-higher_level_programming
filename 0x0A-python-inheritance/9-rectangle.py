#!/usr/bin/python3
"""writes a class that inherits from BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        b = type(value)
        if b is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initantiation with width and height"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """implemented"""
        return self.__width * self.__height

    def __str__(self):
        """prints a str representation"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
