""" Unittest for max_integer function """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_results(self):
        self.assertAlmostEqual(max_integer([0, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([-1, 0, 10, 1000]), 1000)
        self.assertAlmostEqual(max_integer([-50, -30, -10, 0]), 0)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([0, 6, 2]), 6)
        self.assertAlmostEqual(max_integer([9, 5, 6]), 9)
        self.assertAlmostEqual(max_integer([]), None)
