#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    my_dict = sorted(a_dictionary.keys())
    for key in my_dict:
        print("{}: {}".format(key, a_dictionary[key]))
