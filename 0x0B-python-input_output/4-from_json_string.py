#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string:"""
import json


def from_json_string(my_str):
    """ returns an object (Python data structure)
    Args:
        my_str: string to be converted
    """
    return json.loads(my_str)
