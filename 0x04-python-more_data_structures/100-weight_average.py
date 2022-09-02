#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    upper = 0
    lower = 0

    for t in my_list:
        upper += t[0] * t[1]
	lower += t[1]

    average = upper / lower
    return average
