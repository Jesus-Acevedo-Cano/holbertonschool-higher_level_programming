#!/usr/bin/python3
import json
""" save to a json file """


def save_to_json_file(my_obj, filename):
    """write json to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
