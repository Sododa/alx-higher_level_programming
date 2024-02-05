#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """rectangle square class"""
    def __init__(self, size):
        """Method for initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method returns area of a square"""
        return self.__size ** 2
