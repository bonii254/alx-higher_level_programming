#!/usr/bin/python3
"""list of available attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    Args:
        obj (object): The object for which to retrieve attributes and methods.
    Returns:
        list: A list of attribute and method names.
    """
    attr_meth = dir(obj)
    return [name for name in attr_meth]
