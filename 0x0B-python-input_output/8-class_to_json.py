#!/usr/bin/python3
""" Module that returns the dictionary description
"""


def class_to_json(obj):
    """ Function returning the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
