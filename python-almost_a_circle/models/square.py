#!/usr/bin/python3
"""
This is the module to define the Square.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ inherts from the parent in rectangle.py """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.
        
        Args:
            size: the size of a square (width and height)
            x (int): The x coordinate of the Square.
            y (int): The y coordinate of the Square.
            id (int): The id of the Square (optional).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size, returns width or height"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter for size. sets both width and height to same value
            Args:
                value (int): The size value to set for both width and height.
            
            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is <= 0.
        """
        self.width = value
        self.height = value
        
    def update(self, *args, **kwargs):
        """Update the attributes of the square.
        
        *args:
            1st: id attribute
            2nd: size attribute
            3rd: x attribute
            4th: y attribute
        
        **kwargs: assigns key/value pairs to attributes if *args is empty.
        """
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.width,  # Since width and height are the same in a square
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """override __str__ method to return [square]"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
