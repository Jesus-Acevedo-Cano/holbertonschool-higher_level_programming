#!/usr/bin/python3
class Square():
    """class named square"""
    def __init__(self, size=0):
        """Initialization of instance attributes
           Args:
           size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """func to calculate the area
           Return: area of square
        """
        return self.__size * self.__size
