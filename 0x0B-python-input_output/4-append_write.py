#!/usr/bin/python3
"""open file module"""


def append_write(filename="", text=""):
    """append string to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        cnt = f.write(text)
        return cnt
