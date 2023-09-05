#!/usr/bin/python3
"""a function that prints a text with 2 new lines after each
of these characters: ., ? and :"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == " ":
         i += 1
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1
