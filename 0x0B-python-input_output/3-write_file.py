#!/usr/bin/python3
"""open file module"""


def write_file(filename="", text=""):
    """write string to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        cnt = f.write(text)
        return cnt
