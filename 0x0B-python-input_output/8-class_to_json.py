#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns serialization description(dictionary)
    Args:
        obj: an instance of a class
    """
    return obj.__dict__
