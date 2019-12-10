#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute = (abs(number) % 10)
if number < 0:
 absolute = absolute * -1
print("Last digit of {:d} is".format(number), end=" ")
if absolute < 6 and absolute is not 0:
    print("{:d} and is less than 6 and not 0".format(absolute))
elif absolute == 0:
    print("{:d} and is 0".format(absolute))
else:
    print("{:d} and is greater than 5".format(absolute))
