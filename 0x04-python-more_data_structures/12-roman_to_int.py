#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        cp = roman_string
        con = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for j in range(len(cp)):
            for i, val in con.items():
                if i == cp[j]:
                    if j + 1 < len(cp) and con[cp[j + 1]] > con[cp[j]]:
                        res -= val
                    else:
                        res += val
        return res
    return 0
