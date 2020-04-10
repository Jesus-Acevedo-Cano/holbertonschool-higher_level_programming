#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    if len(list_of_integers) < 1:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        return max(list_of_integers)
