#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """This class defines a rectangle with customizable width and height
        attributes.

        Attributes:
            __width (int): The width of the rectangle.
            __height (int): The height of the rectangle.

        Methods:
            width(self): Get the width of the rectangle.
            width(self, value): Set the width of the rectangle
            height(self): Get the height of the rectangle.
            height(self, value): Set the height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height.
        Args:
            width (int): Width of the new rectangle
            height (int): Height of new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
