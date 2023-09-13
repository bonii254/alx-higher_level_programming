#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns writen chars"""


def write_file(filename="", text=""):
    """Returns written characters

    Args:
        filename: name of file
        text: text to be written to file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
