#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a JSON-to-Python object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
