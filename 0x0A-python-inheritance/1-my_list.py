#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """MyList class - Inherits list"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
