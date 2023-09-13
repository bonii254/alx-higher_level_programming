#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns the number of
characters written"""


def write_file(filename="", text=""):
    """ Returns appended text
    args
        filename: name of file
        text: text to be appended
    """
    with open(text, mode='a', encoding='utf8') as wf:
        size = wf.write(text)
        return size
