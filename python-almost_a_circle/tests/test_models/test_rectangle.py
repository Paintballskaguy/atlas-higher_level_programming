import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def test_create_rectangle(self):
        """Test creating a rectangle instance with valid arguments."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_rectangle_with_x_y(self):
        """Test creating a rectangle instance with x and y arguments."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_invalid_width_type(self):
        """Test invalid width type raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height_type(self):
        """Test invalid height type raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x_value(self):
        """Test invalid x value raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str_method(self):
        """Test the __str__ method of Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 89)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {'id': 89, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update_args(self):
        """Test the update method with *args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

if __name__ == '__main__':
    unittest.main()
