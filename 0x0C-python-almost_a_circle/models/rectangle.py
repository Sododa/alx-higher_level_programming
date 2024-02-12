#!/usr/bin/python3
"""Describes a class Rectangle from Base"""


from models.base import Base


class Rectangle(Base):
    """Class that describes rectangle base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """def unit test """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """define string"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    @property
    def width(self):
        """define width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """define width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """define hight
        """
        return self.__height

    @height.setter
    def height(self, value):
        """define heiht
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """define x self
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter define
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y self retriver
        """
        return self.__y

    @y.setter
    def y(self, value):
        """def self value setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """define areaself
        """
        return self.__width * self.__height

    def display(self):
        """used for display"""
        if self.__y > 0:
            for j in range(self.__y):
                print()
            self.__y = 0
        for j in range(self.__height):
            for i in range(self.__width):
                if self.__y == i:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """defination update
        """
        if args is not None and len(args) is not 0:
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for j in range(len(args)):
                setattr(self, list_atrr[j], args[j])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """decribes return to dictionary
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
