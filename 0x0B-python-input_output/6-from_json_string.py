#!/usr/bin/python3
import json
""" JSON representation of an object"""


def from_json_string(my_str):
    """ function that returns representation of a JSON """
    return json.loads(my_str)
