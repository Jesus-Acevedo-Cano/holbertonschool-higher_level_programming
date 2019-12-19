#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = max(a_dictionary.values())
        for i, val in a_dictionary.items():
            if val == new:
                return i
    return None
