#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0
    a_dict_keys = list(a_dictionary.keys())

    for i in a_dict_keys:
        sum += 1

    return sum
