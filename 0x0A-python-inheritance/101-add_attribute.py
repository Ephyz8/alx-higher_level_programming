#!/usr/bin/python3
"""Defines a function that adds attributes to objects if it's possible."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if it is possible.

    Args:
        obj: The object to add an attribute.
        att: str -  The name of the attribute to add to obj.
        value: The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
