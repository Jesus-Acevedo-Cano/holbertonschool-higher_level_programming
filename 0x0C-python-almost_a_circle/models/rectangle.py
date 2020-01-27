#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ rectangle area """
        return self.__width * self.__height

    def display(self):
        """ print # rectangle """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """ str func """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ args and kwargs """
        attrib = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, attrib[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ rectangle to dictionary """
        dic = {}
        attrib = ["id", "width", "height", "x", "y"]
        for i in attrib:
            dic[i] = getattr(self, i)
        return(dic)
