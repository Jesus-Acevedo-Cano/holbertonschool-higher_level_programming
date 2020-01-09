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

    @property
    def size(self):
        """getter fun"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function
           value: new value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print a # square """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.size):
                print("#", end="")
            print()
