#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ str func """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x,
                self.y, self.width)

    def update(self, *args, **kwargs):
        """ args and kwargs """
        attrib = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, attrib[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ square to dictionary """
        dic = {}
        attrib = ["id", "size", "x", "y"]
        for i in attrib:
            dic[i] = getattr(self, i)
        return(dic)