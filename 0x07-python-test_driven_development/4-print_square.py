#!/usr/bin/python3
"""Defines a function that prints a square with the character #"""


def print_square(size):
    """Prints a square.

    Arg:
        size: int - length of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: if size is less than zero.
    """

if not isinstance(size, int):
    raise TypeError("size must be an integer")


if size < 0:
    raise ValueError("size must be >= 0")


for i in range(size):
    [print("#", end="") for j in range(size)]
    print("")
