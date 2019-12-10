#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 == 0:
        print("{:s}".format(chr(a)), end="")
    else:
        print("{:s}".format(chr(a - 32)), end="")
