#!/usr/bin/python3
""""Defines Pascals tiangle"""


def pascal_triangle(n):
    """Returns a list of lists of ints rep pascals triangle

    Args:
        n (int): size of triangle

        Return: an empty list if n<=0, else a list of lists
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
