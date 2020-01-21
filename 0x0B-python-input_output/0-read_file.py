#!/usr/bin/python3
"""open file module"""


def read_file(filename=""):
    """open file and print to the stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
