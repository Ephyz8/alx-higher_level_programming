#!/usr/bin/python3

"""Defines Base of all classes of the project."""
import csv


class Base:
    """Base class.

    This defines the Base of all classes of the project.

    Private class attr:
    __nb_objects (int): Number of instatiated Bases.
    """

    __nb_objects = 0
    
    def __init__(self, id=None):
        """New base initialization.
 
        Argument:
        id (int): New Base identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
