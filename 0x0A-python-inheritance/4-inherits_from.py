#!/usr/bin/python3
"""Returns true if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """return True if object is an instance of a class that
    inherited from specified class or false otherwise"""
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
