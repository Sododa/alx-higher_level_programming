#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after.
"""


def text_indentation(text):
    """Prints text with added two newlines
    these characters('.', '?', ':').
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
