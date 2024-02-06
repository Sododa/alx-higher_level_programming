#!/usr/bin/python3
"""Write a function that reads a text file (UTF8)"""


def read_file(filename=""):
    """prints it to stdout.

    Args:
        file permission or file doesn't exist exceptions."".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
