#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        temp = my_list[0]
        for i in range(len(my_list)):
            if temp < my_list[i]:
                temp = my_list[i]
        return temp
    return None
