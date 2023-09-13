#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns the number of
characters written"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number of
    characters written"""
    with open(text, mode='w', encoding='utf8') as wf:
        size = wf.write(text)
        return size;
