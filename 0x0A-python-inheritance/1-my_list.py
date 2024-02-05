#!/usr/bin/python3
"""Inherits from list"""


class MyList(list):
    """inherits from class list"""

    def print_sorted(self):
        """print sorted self list"""
        print(sorted(self))
