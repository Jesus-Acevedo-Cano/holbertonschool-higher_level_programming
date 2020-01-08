#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            cnt += 1
        print("")
        return cnt
    except IndexError:
        print("")
        return cnt
