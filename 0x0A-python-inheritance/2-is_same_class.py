#!/usr/bin/python3
"""determines if an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """return True if obj is instance of a_class"""
    b = type(obj)
    if b == a_class:
        return True
    return False
