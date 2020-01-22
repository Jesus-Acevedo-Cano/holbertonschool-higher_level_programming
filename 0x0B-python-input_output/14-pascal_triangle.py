#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ Pascal Triangle """
    if n <= 0:
        return []

    pascal = [[1]]
    pascpy = []

    for a in range(n - 1):
        pascpy.append(1)

        for b in range(len(pascal[a]) - 1):
            frst = pascal[a][b]
            scnd = pascal[a][b + 1]
            pascpy.append(frst + scnd)

        pascpy.append(1)
        pascal.append(pascpy)
        pascpy = []

    return pascal
