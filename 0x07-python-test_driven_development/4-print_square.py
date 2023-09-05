#!/usr/bin/python3
"""a function that prints a square with the character #."""


def print_square(size):
    """
    Print a square grid of '#' characters with the specified size.

    Args:
        size (int): The size of the square grid.
    Raises:
        TypeError: If 'size' is not an integer or is a negative float.
        ValueError: If 'size' is a negative integer.
    """
    if not isinstance(size, (float, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
