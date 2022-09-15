#!/usr/bin/python3
class Square:
    """class that defines a square
    """

    def __init__(self, size=0):
        """ Method to initialize
	"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ class method returning square area
	"""
        return (self.__size ** 2)
