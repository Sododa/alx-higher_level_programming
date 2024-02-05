#!/usr/bin/python3
"""Write a function that adds a new attribute
to an object if it’s possible:"""


def add_attribute(obj, attr_name, attr_value):
    """cant adds new attribute to an object if its possible"""

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
