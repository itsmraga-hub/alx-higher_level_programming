#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        sum_a = 0
        sum_a1 = 0
    elif len(tuple_a) == 1:
        sum_a = tuple_a[0]
        sum_a1 = 0
    else:
        sum_a = tuple_a[0]
        sum_a1 = tuple_a[1]

    if len(tuple_b) == 0:
        sum_b = 0
        sum_b1 = 0
    elif len(tuple_b) == 1:
        sum_b = tuple_b[0]
        sum_b1 = 0
    else:
        sum_b = tuple_b[0]
        sum_b1 = tuple_b[1]

    tup = (sum_a + sum_b, sum_a1 + sum_b1)
    return tup
