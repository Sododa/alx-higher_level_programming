#!/usr/bin/python3
"""Determines if object is instance of class"""


def is_kind_of_class(obj, a_class):
    """return true if it is an instance is true else false"""
    b = isinstance(obj, a_class)
    if b:
        return True
    return False
