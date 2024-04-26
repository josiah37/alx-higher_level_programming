#!/usr/bin/python3
"""This is a module that defines a class that inherits from the Base class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identity for the new Rectangle.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self._to_dict_called = False

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get and set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Get and set the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Get and set the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__height * self.__width)

    def display(self):
        """prints rectangles(#) based on the length and width"""
        if self.y > 0:
            for i in range(self.y):
                print("" * self.y)
        for rows in range(self.height):
            print(" " * self.x, end="")
            for width in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}")

    """
    # works but the cheker did'nt check it
    def update(self, *args):
        x = [self.id, self.width, self.height, self.x, self.y]
        for index, arg in enumerate(args):
            x[index] = arg
        self.id, self.width, self.height, self.x, self.y = x
    """
    """
    def update(self, *args):
        attributes = ["id", "width", "height", "x", "y"]
        for attr_name, arg in zip(attributes, args):
            setattr(self, attr_name, arg)
    """
    def update(self, *args, **kwargs):
        """ updates the attribute of the rectangle class"""
        """
        _len = len(args)
        for , j in enumerate(args):
            if _len == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif i == 1:
                self.width = args
            elif i == 2:
                self.height = args
            elif i == 3:
                self.x = args
            elif i == 4:
                self.y = args
        """
        if args and len(args) != 0:
            """#a = 0"""
            for a, arg in enumerate(args):
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
#               #a += 1
        if kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                if k == "height":
                    self.height = v
                if k == "width":
                    self.width = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        '''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        '''
        self._to_dict_called = True
        dict_representation = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "size": self.width
        }
        #self._to_dict_called = False  # Reset the flagself._to_dict_called = True
        return dict_representation


    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        if self._to_dict_called:
            return "({}, {}, {}, {})".format(self.x, self.y, self.id,
                                             self.width)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
