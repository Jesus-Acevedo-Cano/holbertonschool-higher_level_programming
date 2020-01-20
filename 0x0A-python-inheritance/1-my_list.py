#!/usr/bin/python3
class MyList(list):
    """class MyList inherit from list"""
    def print_sorted(self):
        """func to print sorted list"""
        print(sorted(self))
