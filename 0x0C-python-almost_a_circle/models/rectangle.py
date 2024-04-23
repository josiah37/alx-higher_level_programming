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
        if x < 0:
            raise ValueError("x must be > 0")
        
        if y < 0:
            raise ValueError("y must be > 0")
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ to get the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self,value):
        """ to set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    
    def height(self):
        """ to get and set the height of the rectangle"""
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
        """ to get and set the width of the rectangle"""
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
        """ to get and set the x axis of the rectangle"""
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
        """ returns the area of a rectangle"""
        return(self.__height * self.__width)
