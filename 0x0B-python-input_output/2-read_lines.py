#!/usr/bin/python3
"""open file module"""


def read_lines(filename="", nb_lines=0):
    """print n lines to read"""
    cnt = 0
    if nb_lines <= 0 or nb_lines >= len(open(filename).readlines()):
        with open(filename, encoding="utf-8") as f:
            for line in f:
                print(line, end="")

    else:
        with open(filename, encoding="utf-8") as f:
            while cnt != nb_lines:
                print(f.readline(), end="")
                cnt += 1
