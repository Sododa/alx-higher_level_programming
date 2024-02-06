#!/usr/bin/python3
"""Write a function that returns an object"""
import json


def from_json_string(my_str):
    """Returns an represented by a JSON string.
        my_str (str): json object to convert to Python object.
        type: Python object.

    # print("type json.loads(my_str)--> {}".format(type(json.loads(my_str))))
    # print("type my_str--> {}".format(type(my_str)))"""
    return json.loads(my_str)
