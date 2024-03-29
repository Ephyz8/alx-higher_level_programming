#!/usr/bin/python3
"""Defines function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read the content of a text file and print it to stdout.

    Args:
        filename: str - The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
