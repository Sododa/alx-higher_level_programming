#!/usr/bin/python3
"""Describes Square class"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square rectanle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """defines --unit test size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints string"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ define size of self
        """
        return self.width

    @size.setter
    def size(self, value):
        """define size self and value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """defines update self arguments
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for j in range(len(args)):
                if list_atr[j] == 'size':
                    setattr(self, 'width', args[j])
                    setattr(self, 'height', args[j])
                else:
                    setattr(self, list_atr[j], args[j])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """defines to dictionary self
        """
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
