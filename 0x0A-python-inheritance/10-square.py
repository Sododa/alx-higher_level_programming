#!/usr/bin/python3
""" write a class that inherits from BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validated value"""
        b = type(value)
        if b is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of privates"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """implementing area"""
        return self.__width * self.__height

    def __str__(self):
        """return a str representation"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """initializer"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
