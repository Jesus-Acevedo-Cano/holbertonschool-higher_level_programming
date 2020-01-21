#!/usr/bin/python3
"""open file module"""


def number_of_lines(filename=""):
    """number of lines read"""
    with open(filename, encoding="utf-8") as f:
        return len(f.readlines())
