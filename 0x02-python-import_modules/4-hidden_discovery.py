#!/usr/bin/python3
import hidden_4
if (__name__ == "__main__"):
    str = dir(hidden_4)
    for a in range(0, len(str)):
        if str[a].find("__") is not 0:
            print(str[a])
