#!/usr/bin/python3
"""Defines a function that adds two integers"""

def add_integer(a, b=98):
    """
    Add two numbers and return their sum.
    
    Args:
        a (int or float): The first number to be added. If it's a float,
        it will be cast to an integer.
        b (int or float, optional): The second number to be added. Defaults 
        to 98. If it's a float, it will be cast to an integer.
    
    Raises:
        TypeError: If either `a` or `b` is not an integer or a float.

    Returns:
        int: The sum of `a` and `b`.
    """
    if (not isinstance(a, int)) and not (isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and not (isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
