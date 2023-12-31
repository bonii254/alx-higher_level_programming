#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj - python object
        filename - name of text file
    """
    with open(filename, mode='w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
