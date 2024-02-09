#!/usr/bin/python3

"""
Unittest for Rectangle class
"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    Testing Rectangle class
    """

    def tearDown(self):
        """
        Tears down object count
        """

        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """
        Testing instantiation
        """

        o1 = Rectangle(3, 2)
        o2 = Rectangle(8, 7, 0, 0, 12)
        with self.assertRaises(TypeError):
            o3 = Rectangle("string")
            o4 = Rectangle(None)
            o5 = Rectangle(float('inf'))
            o6 = Rectangle(9.5, 9.3)
            o7 = Rectangle(-8, 9)
            o8 = Rectangle()

        self.assertEqual(o1.id, 1)
        self.assertEqual(o1._Base__nb_objects, 1)
        self.assertEqual(o2.id, 12)
        self.assertEqual(o2._Base__nb_objects, 1)

    def test_area(self):
        """
        Testing area()
        """

        o1 = Rectangle(3, 2)
        o2 = Rectangle(8, 7, 0, 0, 12)
        o3 = Rectangle(999, 999)

        self.assertEqual(o1.area(), 6)
        self.assertEqual(o2.area(), 56)
        self.assertEqual(o3.area(), 998001)

    def test_display(self):
        """
        Testing display()
        """

        o1 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o1.display()
            self.assertEqual(fakeOutput.getvalue(), '###\n###\n')

        o2 = Rectangle(4, 5, 0, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o2.display()
            self.assertEqual(fakeOutput.getvalue(),
                             '\n####\n####\n####\n####\n####\n')

    def test_str(self):
        """
        Testing __str__()
        """

        o1 = Rectangle(3, 2)
        o2 = Rectangle(8, 7, 0, 0, 12)
        o3 = Rectangle(3, 2, 1)
        o4 = Rectangle(3, 2, id="holberton")

        self.assertEqual(o1.__str__(), '[Rectangle] (1) 0/0 - 3/2')
        self.assertEqual(o2.__str__(), '[Rectangle] (12) 0/0 - 8/7')
        self.assertEqual(o3.__str__(), '[Rectangle] (2) 1/0 - 3/2')
        self.assertEqual(o4.__str__(), '[Rectangle] (holberton) 0/0 - 3/2')

    def test_update(self):
        """
        Testing update()
        """

        o1 = Rectangle(3, 2)
        o2 = Rectangle(8, 7, 0, 0, 12)
        o3 = Rectangle(3, 2, 1)
        o4 = Rectangle(3, 2, id="holberton")
        o5 = Rectangle(3, 2, id="holberton")

        o1.update(5, 7)
        self.assertEqual(o1.__str__(), '[Rectangle] (5) 0/0 - 7/2')
        with self.assertRaises(ValueError):
            o2.update(**{'id': 1337, 'x': -1})
            o3.update("stringid", None, None)
        o4.update(None)
        self.assertEqual(o4.__str__(), '[Rectangle] (None) 0/0 - 3/2')
        o5.update(-5)
        self.assertEqual(o5.__str__(), '[Rectangle] (-5) 0/0 - 3/2')

    def test_to_dictionary(self):
        """
        Testing to_dictionary()
        """

        o1 = Rectangle(3, 2)
        o2 = Rectangle(8, 7, 0, 0, 12)
        o3 = Rectangle(3, 2, 1)
        o4 = Rectangle(3, 2, id="holberton")

        d1 = {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        d2 = {'id': 12, 'width': 8, 'height': 7, 'x': 0, 'y': 0}
        d3 = {'id': 2, 'width': 3, 'height': 2, 'x': 1, 'y': 0}
        d4 = {'id': 'holberton', 'width': 3, 'height': 2, 'x': 0, 'y': 0}

        self.assertDictEqual(o1.to_dictionary(), d1)
        self.assertDictEqual(o2.to_dictionary(), d2)
        self.assertDictEqual(o3.to_dictionary(), d3)
        self.assertDictEqual(o4.to_dictionary(), d4)

if __name__ == '__main__':
    unittest.main()