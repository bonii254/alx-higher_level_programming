#!/usr/bin/python3


def no_c(my_string):
    new_string = my_string[:]
    if "c" in new_string:
        new_string = new_string.replace("c", "")
    if "C" in new_string:
        new_string = new_string.replace("C", "")
    return new_string
