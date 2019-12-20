#!/usr/bin/python3
def roman_to_int(roman_string):
    cp = roman_string
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for j in range(len(cp)):
        for i, val in conv.items():
            if i == cp[j]:
                if j + 1 < len(cp) and conv[cp[j + 1]] > conv[cp[j]]:
                    res -= val
                else:
                    res += val
    return res
