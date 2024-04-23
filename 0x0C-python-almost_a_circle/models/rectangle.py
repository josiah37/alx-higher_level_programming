#!/usr/bin/python3
""" THIS IS A MODULE THAT DIFINES A CALSS THAT INHERIT FROM BASE CLASS"""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        args:
            width (int): The width of the new Rectangle.
            height (int): the height of the new rectangle.
            x (int): 
            y (int): 
            id (int): The identity for the new Rectangle.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
            return (self.__width)

    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    
    def height(self):
            return (self.__height)
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
        return (self.__x)
    @x.setter
    def x(self,value):
        if not isinstance(value, int):
            raise TypeError("y  must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return (self.__y)
    @y.setter
    def y(self,value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
    def area(self):
        return(self.__height * self.__width)
