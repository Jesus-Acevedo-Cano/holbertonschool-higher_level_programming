#!/usr/bin/python3
"""class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """instances and validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ rectangle values """
        return("[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height))
