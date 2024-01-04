#!/usr/bin/python3
"""Defines function that finds a peak in a list of
unsorted integers."""


def find_peak(list_of_integers):
    """Finds the index of the largest integer"""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        mid_value = list_of_integers[mid]

        if mid_value > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
