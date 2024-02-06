#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """returns the number
    of characters written.

    Args:
        filename (str, optional): name of the file. Defaults to

    Returns:
        int: number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number  to a file."""
        return f.write(text)
