#!/usr/bin/python3
"""Defines a class of a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """"Initializing a new Square

        Arguments:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return Square str () and print() representation"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
    
    @property
    def size(self):
        """Get the size of the Square"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Set the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the Square.

        Arguments:
             *args (ints): New attribute values.
                1st argument is the id attribute
                2nd argument is the size attribute
                3rd argument is the x attribute
                4th argument is the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

    if args and len(args) != 0:
            num = 0
            for arg in args:
                if num == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
                num += 1

    elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """Return representation of the Square dictionary."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }