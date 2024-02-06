#!/usr/bin/python3
"""function append_write"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number
    of characters added.
    Defaults to
     string of text to write to file. Defaults to

    Returns:
        characters appended to file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """returns the number of charactersfile."""
        return f.write(text)
