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
    def size(self, value)
        """Setter for size. sets both width and height to same value
            Args:
                value (int): The size value to set for both width and height.
            
            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is <= 0.
        """
        self.width = value
        self.height = value
        
        
    def __str__(self):
        """override __str__ method to return [square]"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
