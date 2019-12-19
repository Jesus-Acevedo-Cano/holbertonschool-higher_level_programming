#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = sorted(a_dictionary)
        return max(new)
    return None
