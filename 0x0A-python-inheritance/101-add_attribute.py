#!/usr/bin/python3
"""Add an attribute to an object if possible."""


def add_attribute(obj, att, value):
    """
    Args:
        obj (object): The object to which the attribute should be added.
        att (str): The name of the attribute.
        value (any): The value of att.
    Raises:
        TypeError: If it's not possible to add the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
