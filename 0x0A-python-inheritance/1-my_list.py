#!/usr/bin/python3
"""module printed"""


class MyList(list):
    """MyList class - Inherits list"""
    def print_sorted(self):
        """Prints a sort list"""
        print(sorted(self))
