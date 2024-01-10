#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        tm = [1]
        for i in range(len(tri) - 1):
            tm.append(tri[i] + tri[i + 1])
        tm.append(1)
        tris.append(tm)
    return tris
