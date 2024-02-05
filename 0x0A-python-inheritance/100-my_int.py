#!/usr/bin/python3
""" class myint inherits from int"""


class MyInt(int):
    """MyInt is a rebel"""
    def __eq__(self, other_int):
        """inverted =="""
        if self is not other_int:
            return False
        return True

    def __ne__(self, other_int):
        """inverted !="""
        if self is other_int:
            return False
        return True
