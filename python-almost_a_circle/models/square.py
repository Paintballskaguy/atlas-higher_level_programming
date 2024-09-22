#!/usr/bin/python3
"""
This is the module to define the Square.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ inherts from the parent in Base.py """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.
        
        Args:
            width (int): The width of the Square.
            height (int): The height of the Square.
            x (int): The x coordinate of the Square.
            y (int): The y coordinate of the Square.
            id (int): The id of the Square (optional).
        """
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y
        
    @property
    def size(self):
        return self.__width

    @size.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
        
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
        
    def display(self):
        """prints the Square using #"""
        print("\n" * self.y, end="")
        
        for _ in range(self.height):
            print(" "  * self.x + "#" * self.width)

    def __str__(self):
        """Override the __str__ method to return [Square] (<id>) <x>/<y> - <width>/<height>."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def  update(self,  *args, **kwargs):
        """
        Assigns attributes based on *args.
        
        Args:
            1st: id attribute
            2nd: width attribute
            3rd: height attribute
            4th: x attribute
            5th: y attribute
            
        **kwargs: assigns key/value pairs to attributes
        if *args is empty.
        """
        if args and len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
