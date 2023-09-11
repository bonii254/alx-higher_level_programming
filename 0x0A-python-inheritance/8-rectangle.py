#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Initialize a rectangle
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
