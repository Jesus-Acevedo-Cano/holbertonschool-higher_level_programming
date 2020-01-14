#!/usr/bin/python3
""" Divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    matrix: containing elements
    div: integer used to div
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "div must be a number"
    msg4 = "division by zero"
    if type(matrix) != list:
        raise TypeError(msg1)

    for a in matrix:
        if type(a) is not list:
            raise TypeError(msg1)

    for a in matrix:
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError(msg1)

    for a in matrix:
        if len(a) is not len(matrix[0]):
            raise TypeError(msg2)

    if type(div) is not int and type(div) is not float:
        raise TypeError(msg3)

    if div == 0:
        raise ZeroDivisionError(msg4)

    newMatrix = [a[:] for a in matrix]
    for a in range(len(newMatrix)):
        for b in range(len(newMatrix[a])):
            newMatrix[a][b] = round(newMatrix[a][b]/div, 2)

    return newMatrix
