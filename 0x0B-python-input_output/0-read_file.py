#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='r', encoding='UTF8') as f:
        content = f.read()
        print("{}".format(content), end="")

