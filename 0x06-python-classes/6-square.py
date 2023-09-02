#!/usr/bin/python3

"""Defines a class called square"""


class Square:
    """define class square

    Attributes:
        __size (int): length of square object
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): len of square
            position (tupple): a tuple of 2 positive integers

        Returns:
            none

        Raises:
            Typerror: if size type is not int
            ValueError: if size >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """gets the area of a square.
        Returns:
            area (int): area of a square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints square #
        Returns:
            none.
        """
        if (self.__size == 0):
            print()
        else:
            x, y = self.__position
            for _ in range(y):
                print()
            for _ in range(self.__size):
                print(" " * x + "#" * self.__size)
