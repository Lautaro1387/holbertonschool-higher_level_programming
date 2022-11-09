#!/usr/bin/python3
"""Test class base"""


import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """Class test base"""

    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_prev(self):
        base = Base()
        self.assertEqual(base.id, 2)

    def test_id_pass(self):
        base = Base(89)
        self.assertEqual(base.id, 89)


class testsNumber(unittest.TestCase):
    """Tests number"""
    def setUp(self):
        self.base = Base(89)
    def test_1(self):
        self.assertEqual(self.base.id, 89)
    def test_2(self):
        self.assertEqual(Base().to_json_string(None), '[]')
    def test_3(self):
        self.assertEqual(Base().to_json_string([]), '[]')
    def test_4(self):
        self.assertEqual(Base().to_json_string([{ 'id': 12 }]), '[{"id": 12}]')
    def test_5(self):
        self.assertEqual(Base().from_json_string(None), [])
    def test_6(self):
        self.assertEqual(Base().from_json_string("[]"), [])
    def test_7(self):
        self.assertEqual(Base().from_json_string('[{ "id": 89 }]'), [{'id': 89}])

if __name__ == '__main__':
    unittest.main()
