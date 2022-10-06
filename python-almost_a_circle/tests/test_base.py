#!/usr/bin/python3
"""Test class base"""


import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """Class test base"""

    def test_not_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_not_id_prev(self):
        base = Base()
        self.assertEqual(base.id, 2)

    def test_id_pass(self):
        base = Base(89)
        self.assertEqual(base.id, 89)
