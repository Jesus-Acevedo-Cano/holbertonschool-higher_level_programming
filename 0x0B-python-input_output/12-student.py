#!/usr/bin/python3
""" student class module """


class Student():
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            new = [a for a in attrs if hasattr(self, a)]
            return {a: getattr(self, a) for a in new}
        return self.__dict__
