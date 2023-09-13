#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns the number of
characters written"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number of
    characters written"""
    def write_file(filename="", text=""):
        """Returns appended text
        Args:
            filename: name of file
            text: text to be written to file
        """
        with open(filename, "w", encoding="UTF-8") as f:
            size = f.write(text)
            return size
