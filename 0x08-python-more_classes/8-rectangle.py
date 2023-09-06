#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """This class defines a rectangle with customizable width and height
        attributes."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height.
        Args:
            width (int): Width of the new rectangle
            height (int): Height of new rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """print the rectangle with the character #"""
        if (self.__height == 0 or self.__width == 0):
            return ""

        rectobj = []
        for col in range(self.__height):
            for row in range(self.__width):
                rectobj.append(str(Rectangle.print_symbol))
            if col != self.__height - 1:
                rectobj.append('\n')
        return ("".join(rectobj))

    def __repr__(self):
        """a string representation of the rectangle to be able to recreate
            a new instance by using eval()
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """delete instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
