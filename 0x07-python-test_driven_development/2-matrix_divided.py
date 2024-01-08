#!/usr/bin/python3
"""Defines a function of a matrix division"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): A list of integers/floats
        div (int/float): An int/float used to divide all elements of the matrix

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: if div is not an int/float.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix - result of the division.
    """
if (not isinstance(matrix, list) or matrix == [] or \
        not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


if len(set(len(row) for row in matrix)) > 1:
    raise TypeError("Each row of the matrix must have the same size")


if not isinstance(div, (int, float)):
    raise TypeError("div must be a number")


if div == 0:
    raise ZeroDivisionError("division by zero")


return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
