#!/usr/bin/python3
"""
Unittest module for the `max_integer` function.
"""

import unittest
from max_integer import max_integer  # Direct import since they're in the same directory


class TestMaxInteger(unittest.TestCase):
    """
    Test case class for the `max_integer` function.
    """

    def test_max_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_two_elements(self):
        self.assertEqual(max_integer([5, 10]), 10)

    def test_max_missing_input(self):
        self.assertEqual(max_integer(), None)

    def test_max_wrong_input(self):
        self.assertEqual(max_integer("string"), "t")
        with self.assertRaises(TypeError):
        	max_integer([1, "a", 3])

    def test_max_large_numbers(self):
        large_num = 10**18
        self.assertEqual(max_integer([large_num, -large_num, large_num - 1]), large_num)

    def test_max_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 50, 0, 3]), 50)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 8, 7, 6]), 9)

    def test_max_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_max_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()