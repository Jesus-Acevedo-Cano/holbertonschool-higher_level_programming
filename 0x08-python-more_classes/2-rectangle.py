#!/usr/bin/python3
class Rectangle():
    """class named Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of instance attributes
           Args:
           width (int): width of rectangle
           height (int): rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter fun"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function
           value: new value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter fun"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function
           value: new value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func to calculate the area
           Return: area of square
        """
        return self.__width * self.__height

    def perimeter(self):
        """func to calculate the area
           Return: perimeter of square
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2
