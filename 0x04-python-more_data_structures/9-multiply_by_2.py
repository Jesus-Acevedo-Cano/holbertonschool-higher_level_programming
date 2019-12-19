#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i, val in new.items():
        new[i] = val * 2
    return new
