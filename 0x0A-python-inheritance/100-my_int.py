#!/usr/bin/python3
""" class MyInt """


class MyInt(int):
    """ class MyInt oposite comp """

    def __eq__(self, other):
        """  changed comp """
        return self.numerator != other

    def __ne__(self, other):
        """ changed comp """
        return self.numerator == other
