#!/usr/bin/python3
import sys
""" arguments to a Python list """


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
""" import functions """


new = sys.argv[1:]

try:
    current = load_from_json_file("add_item.json")

except:
    current = []

current.extend(new)
save_to_json_file(current, "add_item.json")
