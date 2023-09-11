#!/usr/bin/python3
""" a class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validator"""
        self.name = name
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.value = value
