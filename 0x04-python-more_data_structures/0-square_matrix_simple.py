#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    list_1 = []
    for x in matrix:
        list_2 = []
        for y in x:
            list_2.append(y ** 2)
        list_1.append(list_2)
    return list_1
