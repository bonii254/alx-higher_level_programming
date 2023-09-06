#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """This class defines a rectangle with customizable width and height
        attributes."""

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
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
