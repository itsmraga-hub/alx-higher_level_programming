#!/usr/bin/python3
"""
This module is of a class defining a Rectangle
"""


class Rectangle:
    """ Class defining a rectangle """
    def __init__(self, width=0, height=0):
        """ Method initializng an instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method returning the value of the width
        Returns:
            width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method defining the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method returning the height
        Returns:
            height of rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method defining the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method calculating the Rectangle area
        Returns:
            rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """ Method calculating the Rectangle perimeter
        Returns:
            rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method returning a Rectangle #
        Returns:
            str of the rectangle
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method returning the string represantion of the instance
        Returns:
            string represenation of the object
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """
	Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
