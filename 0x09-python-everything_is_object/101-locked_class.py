#!/usr/bin/python3
"""
A module containing a class that avoids dynmaically created attributes
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Initiliazing method """
        pass
