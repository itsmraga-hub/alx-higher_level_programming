#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = list(map(lambda x: replace if x == search else x, my_list))
    return new_l
