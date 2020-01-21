#!/usr/bin/python3
import json
""" from a json file """


def load_from_json_file(filename):
    """write from a json file"""
    with open(filename, 'r+', encoding="utf-8") as f:
        return json.loads(f.read())
