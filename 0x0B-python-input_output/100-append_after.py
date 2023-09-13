#!/usr/bin/python3
    """Defines a function to append text to file at specific position"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text to fle after specified string
    Args:
        filename (str): Name of file in question
        search_string (str): string after which text is to be appended
        new_string (str): Text to be appended into file
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
