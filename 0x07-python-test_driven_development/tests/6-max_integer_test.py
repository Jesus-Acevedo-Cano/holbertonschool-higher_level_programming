#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def testing_max_integer(self):
        """ function max integer tests
            self: self
        """

        self.assertEqual(max_integer([]), None)
        self.assertIsNotNone(max_integer.__doc__)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-750, 1, 13]), 13)
        self.assertRaises(TypeError, max_integer, ["a", "b", 5])
        self.assertEqual(max_integer({0: "a", 1: "b", 2: "c"}), "c")
        self.assertEqual(max_integer([-1, -2, 0]), 0)

if __name__ == '__main__':
    unittest.main()
