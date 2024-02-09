#!/usr/bin/python3

"""
Unittest for Square class
"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Testing Square class
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

        o1 = Square(5)
        o2 = Square(id="hello", size=3)
        with self.assertRaises(ValueError):
            o3 = Square(-5, 3, 4)
            o4 = Square(9.5, 9.3)
            o5 = Square(float('inf'))
            o6 = Square("string")
            o9 = Square(None)

        with self.assertRaises(TypeError):
            o7 = Square(5, "hi")
            o8 = Square(5, None)
            o10 = Square(5, float('inf'))
            o11 = Square(5, 9.5)
            o12 = Square()

        self.assertEqual(o1.id, 1)
        self.assertEqual(o1._Base__nb_objects, 3)
        self.assertEqual(o2.id, 'hello')
        self.assertEqual(o2._Base__nb_objects, 3)

    def test_area(self):
        """
        Testing area()
        """

        o1 = Square(5)
        o2 = Square(999, 0, 0, "helloo")
        o3 = Square(id="hello", size=3, x=1, y=0)

        self.assertEqual(o1.area(), 25)
        self.assertEqual(o2.area(), 998001)
        self.assertEqual(o3.area(), 9)

    def test_display(self):
        """
        Testing display()
        """

        o1 = Square(4)
        o2 = Square(id="hello", size=3, x=1, y=0)

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o1.display()
            self.assertEqual(fakeOutput.getvalue(), '####\n####\n####\n####\n')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o2.display()
            self.assertEqual(fakeOutput.getvalue(), ' ###\n ###\n ###\n')

    def test_str(self):
        """
        Testing __str__()
        """

        o1 = Square(5)
        o2 = Square(3, 2)
        o3 = Square(1, 2, 3, 4)
        o4 = Square(id="hello", size=3, x=1, y=0)

        self.assertEqual(o1.__str__(), '[Square] (1) 0/0 - 5')
        self.assertEqual(o2.__str__(), '[Square] (2) 2/0 - 3')
        self.assertEqual(o3.__str__(), '[Square] (4) 2/3 - 1')
        self.assertEqual(o4.__str__(), '[Square] (hello) 1/0 - 3')

    def test_update(self):
        """
        Testing update()
        """

        o1 = Square(5)
        o2 = Square(3, 2)
        o3 = Square(1, 2, 3, 4)
        o4 = Square(id="hello", size=3, x=1, y=0)

        o1.update(6, 1, 2, 8)
        self.assertEqual(o1.__str__(), '[Square] (6) 2/8 - 1')
        o2.update(1, 2, 3, id="hello")
        self.assertEqual(o2.__str__(), '[Square] (hello) 2/0 - 3')
        with self.assertRaises(ValueError):
            o3.update("hello", -5)
            o4.update(x=9.5)

    def test_to_dictionary(self):
        """
        Testing to_dictionary()
        """

        o1 = Square(5)
        o2 = Square(5, 6)
        o3 = Square(1, 2, 3, 5)
        o4 = Square(3, 2, id="holberton")

        d1 = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        d2 = {'id': 2, 'size': 5, 'x': 6, 'y': 0}
        d3 = {'id': 5, 'size': 1, 'x': 2, 'y': 3}
        d4 = {'id': 'holberton', 'size': 3, 'x': 2, 'y': 0}

        self.assertDictEqual(o1.to_dictionary(), d1)
        self.assertDictEqual(o2.to_dictionary(), d2)
        self.assertDictEqual(o3.to_dictionary(), d3)
        self.assertDictEqual(o4.to_dictionary(), d4)

if __name__ == '__main__':
    unittest.main()