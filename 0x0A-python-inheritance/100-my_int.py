#!/usr/bin/python3
"""Defines a class MyInt that inherits int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __neg__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
