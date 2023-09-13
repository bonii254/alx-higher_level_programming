#!/usr/bin/python3
"""Defines a function to convert obj to JSON"""
import json


def to_json_string(my_obj):
    """eturns the JSON representation of an object (string)
    Args:
         my_obj: object to be converted
    """
    return json.dumps(my_obj)
