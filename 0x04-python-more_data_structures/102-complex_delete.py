#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_keys = list(a_dictionary.keys())

    for d in dict_keys:
        if value == a_dictionary.get(d):
            del a_dictionary[d]

    return (a_dictionary)
