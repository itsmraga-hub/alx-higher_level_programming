#!/usr/bin/python3
"""
This module is a function that adds two numbers and
returns the result
"""


def add_integer(a, b=98):
    """ Function that adds two integer or floats
    Args:
        a: first num
        b: second num
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
