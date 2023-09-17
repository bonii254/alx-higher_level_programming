#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new square
        Args:
            size:(int): size of square
            x (int):
            y (int):
            id (int): instance id
        Raises:
            TypeError: <name of the attribute> must be an integer.
            ValueError: <name of the attribute> must be > 0
            ValueError: <name of the attribute> must be >= 0(for x and y)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ the side of the Rectangle."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:"""
        if args and len(args) != 0:
            argc = 0
            for arg in args:
                if argc == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif argc == 1:
                    self.size = arg
                elif argc == 3:
                    self.x = arg
                elif argc == 4:
                    self.y = arg
                argc += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """string representation of a square"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") " + str(self.x) + "/" + str(self.y)
        string += " - " + str(self.width)
        return (string)
