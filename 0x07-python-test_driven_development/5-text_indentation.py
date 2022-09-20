#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s_copy = text[:]

    for d in ".?:":
        list_text = s_copy.split(d)
        s_copy = ""
        for i in list_text:
            i = i.strip(" ")
            s_copy = i + d if s is "" else s + "\n\n" + i + d

    print(s_copy[:-3], end="")
