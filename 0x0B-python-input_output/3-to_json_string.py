#!/usr/bin/python3
"""Write a function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string).

        my_obj (type): object to examine.

    Returns:
        JSON representation of object.

    # print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    # print("type my_obj--> {}".format(type(my_obj)))

    # serializing json"""
    return json.dumps(my_obj)
