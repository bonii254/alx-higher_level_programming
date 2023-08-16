#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_list = list(set(my_list))
    result = 0
    for num in my_list:
        result += num
    return result
