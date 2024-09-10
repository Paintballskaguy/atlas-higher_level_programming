#!/usr/bin/python3
"""
Unittest module for the `max_integer` function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test case class for the `max_integer` function.
    """

    def test_max_at_beginning(self):
        """Test where the maximum value is at the beginning of the list."""
        self.assertEqual(max_integer([9, 8, 7, 6]), 9)

    def test_max_in_the_middle(self):
        """Test where the maximum value is in the middle of the list."""
        self.assertEqual(max_integer([1, 100, 3, 4]), 100)

    def test_one_negative_number(self):
        """Test where there's only one negative number in the list."""
        self.assertEqual(max_integer([1, 2, 3, -1]), 3)

    def test_only_negative_numbers(self):
        """Test where all the numbers in the list are negative."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        """Test where the list contains only one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_list_is_empty(self):
        """Test where the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_max_at_end(self):
        """Test where the maximum value is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def test_max_missing_input(self):
        """Test with no arguments, which defaults to an empty list."""
        self.assertEqual(max_integer(), None)

    def test_max_wrong_input(self):
        """Test for invalid inputs, like a string and mixed types."""
        self.assertEqual(max_integer("string"), "t")
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_max_large_numbers(self):
        """Test with large numbers."""
        large_num = 10**18
        self.assertEqual(max_integer([large_num, -large_num, large_num - 1]), large_num)


if __name__ == "__main__":
    unittest.main()