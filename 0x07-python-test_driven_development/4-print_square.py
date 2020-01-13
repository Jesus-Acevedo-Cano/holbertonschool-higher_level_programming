#!/usr/bin/python3
""" prints a # square """


def print_square(size):
    """
    prints a # square
    size: size of square
    """

    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(int(size)):
        for b in range(int(size)):
            print("#", end="")
        print()
