#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """square width and height to find area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the class object"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
