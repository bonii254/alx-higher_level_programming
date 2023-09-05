#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    '''
    Divide all elements of a matrix by a given divisor and round the
    result to 2 decimal places.

    Args:
        matrix (list of lists): The matrix to be divided.
        Each element must be an integer or a float.
        div (int or float): The divisor to divide each element of the matrix.
    Raises:
        TypeError:
            If the matrix is not a list of lists containing integers or floats,
            if the divisor is not an integer or a float,
            or if the rows of the matrix have different sizes.
        ZeroDivisionError:
            If the divisor is zero.
    Returns:
        matrix (list of lists): A new matrix with the elements divided by the
        divisor and rounded to 2 decimal places.
    '''
    for li in matrix:
        for val in li:
            if not isinstance(val, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists)\n"
                                "of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(num/div, 2) for num in row] for row in matrix]
    return result
