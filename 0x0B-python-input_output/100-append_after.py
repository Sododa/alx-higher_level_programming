#!/usr/bin/python3
"""Write a function that inserts a line of text to a file,"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file
        filename (str, optional): name of file. Defaults to "".
        search_string (str, optional): string to search.
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
