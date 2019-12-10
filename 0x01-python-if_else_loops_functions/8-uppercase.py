#!/usr/bin/python3
def uppercase(str):
    for a in range(0, len(str)):
        stru = ord(str[a])
        if stru > 95:
            stru = stru - 32
        print("{:c}".format(stru), end="")
    print("")
