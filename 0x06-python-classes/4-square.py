#!/usr/bin/python3
class Square:
    """class defining a square"""
    def __init__(self, size=0):
        """ Method to initialize"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """class method returning square area"""

        return (self.__size ** 2)

    @property
    def size(self):
        """class method returning size"""
        return self.__size

    @size.setter
    def size(self, value):
        """class method to set the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
