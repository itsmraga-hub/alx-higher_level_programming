#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_dict_list = list(a_dictionary.keys())
    ordered_dict_list.sort()
    for i in ordered_dict_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
