#!usr/bin/python3
"""Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Defines class of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Arguments:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identity of the Rectangle.
        
        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an integer.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
    
    def display(self):
        """Using '#' to print Rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """Overiding the __str__ method"""
        return(f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
    
    def update(self, *args, **kwargs):
        """Rectangle update.

        Arguments:
            *args (ints): New attribute values.
                - 1st argument is id attribute
                - 2nd argument is width attribute
                - 3rd argument is height attribute
                - 4th argument is x attribute
                - 5th argument is y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            num = 0
            for arg in args:
                if num == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.width = arg
                elif num == 2:
                    self.height = arg
                elif num == 3:
                    self.x = arg
                elif num == 4:
                    self.y = arg
                num += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif i == "width":
                    self.width = j
                elif i == "height":
                    self.height = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """Return the Rectangle dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }



                
                






 