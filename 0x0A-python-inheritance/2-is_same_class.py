#!/usr/bin/python3
"""module is same class"""


def is_same_class(obj, a_class):
    """
       function that returns True if the object is
       exactly an instance of the specified class
       Args:
            obj: object
            a_class: class
            return: True or False
    """
    if type(obj) ==  a_class:
        return True
    else:
        return False
