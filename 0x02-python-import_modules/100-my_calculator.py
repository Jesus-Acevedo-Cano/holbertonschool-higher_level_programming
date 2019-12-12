#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv)
    if (args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ops = sys.argv[2]
    if (ops == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif (ops == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif (ops == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif (ops == "/"):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
