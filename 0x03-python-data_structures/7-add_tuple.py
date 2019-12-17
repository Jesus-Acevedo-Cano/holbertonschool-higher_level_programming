#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new0 = 0
    new1 = 0
    if tuple_a:
        if len(tuple_a) >= 2:
            new0 += tuple_a[0]
            new1 += tuple_a[1]
        elif len(tuple_a) == 1:
            new0 += tuple_a[0]
    if tuple_b:
        if len(tuple_b) >= 2:
            new0 += tuple_b[0]
            new1 += tuple_b[1]
        elif len(tuple_b) == 1:
            new0 += tuple_b[0]
    newTuple = (new0, new1)
    return newTuple
