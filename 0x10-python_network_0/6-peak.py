#!/usr/bin/python3
"""
    A function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    if len(list_of_integers) > 1:
        large = list_of_integers[0]
        for num in list_of_integers:
            if num >= large:
                large = num
    else:
        large = None

    return large
