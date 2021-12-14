#!/usr/bin/python3
"""
matrix_divided module
Divides each element of a matrix by div
"""


def matrix_divided(matrix, div):
    """
    matrix_divide: divides all elements of a matrix
    :param matrix: list of list of integers or float
    :param div: dividend
    :return: matrix list of list integer
    """
    length = None
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of list) "
                        "of integers or float")
    for li in matrix:
        if not isinstance(li, list):
            raise TypeError("matrix must be a matrix (list of list)"
                            " of integers or float")
        if length is None:
            length = len(li)
        elif length != len(li):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = []

    for i in range(len(matrix)):
        result = []
        for j in range(len(matrix[i])):
            result.append(round(matrix[i][j] / div, 2))

        div_matrix.append(result)
        del result

    return div_matrix
