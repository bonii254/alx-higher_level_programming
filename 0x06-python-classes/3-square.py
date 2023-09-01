#!/usr/bin/python3


class Square:
    """define class square
    Attributes:
        __size (int): length of square object
    """
    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): len of square
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

    def area(self):
        """gets the area of a square.
        Returns:
            area (int): area of a square.
        """
        return (self.__size * self.__size)
