#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = max(a_dictionary.items())
        return new[0]
    return None
