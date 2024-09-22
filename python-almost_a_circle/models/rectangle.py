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
        print("\n" * self.y, end="")
        
        for _ in range(self.height):
            print(" "  * self.x + "#" * self.width)

    def __str__(self):
        """Override the __str__ method to return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y

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
