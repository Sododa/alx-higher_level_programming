#!/usr/bin/python3
"""Inherits list"""


class MyList(list):
    """inherits class list"""

    def print_sorted(self):
        """print sorted self list"""
        print(sorted(self))
