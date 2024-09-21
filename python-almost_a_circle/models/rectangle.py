#!/usr/bin/python3
"""
This is the module to define the rectangle.
"""


from models.base import Base

class Rectangle(Base):
    """ inherts from the parent in Base.py """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The id of the rectangle (optional).
        """
        super().__init__(id)
        self.width = width 
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def y(self):
        return self.__y
        
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        
    def area(self):
        """return the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle using #"""
        for _ in range(self.height):
            print("#" * self.width)
