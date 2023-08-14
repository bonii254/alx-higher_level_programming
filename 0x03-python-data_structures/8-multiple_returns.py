#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = tuple(sentence)
    return len(my_tuple), my_tuple[0]
