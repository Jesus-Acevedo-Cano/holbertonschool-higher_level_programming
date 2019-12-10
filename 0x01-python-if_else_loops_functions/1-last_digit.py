#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute = (number * -1) if number < 0 else number
print("Last digit of {:d} is ".format(number), end="")
if absolute % 10 < 6 and absolute % 10 > 0:
    print("{:d} and is less than 6 and not 0".format(absolute % 10))
elif absolute % 10 == 0:
    print("{:d} and is 0".format(absolute % 10))
else:
    print("{:d} and is greater than 5".format(absolute % 10))
