#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    if len(sys.argv) <= 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for a in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(a, sys.argv[a]))
