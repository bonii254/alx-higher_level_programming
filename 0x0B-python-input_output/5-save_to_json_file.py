#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file
    Args:
        my_obj: Object to be saved
        filename: name of file
    """
    with open(filename, 'w') as file:
        son.dump(my_obj, file)