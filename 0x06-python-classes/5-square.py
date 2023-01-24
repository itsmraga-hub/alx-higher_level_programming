#!/usr/bin/python3
class Square:
    """class defining a square

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.
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
        """class method returning square area
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """class method returning size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """class method to set the size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """class method printing a square
        """

        if not self.size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
