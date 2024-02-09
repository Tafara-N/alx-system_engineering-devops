#!/usr/bin/python3

"""
Unittest for Base class
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Testing Base class
    """

    def tearDown(self):
        """
        Tears down object count
        """

        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """
        Tests instantiation
        """

        o1 = Base()
        o2 = Base(9)
        o3 = Base(9.5)
        o4 = Base(float('inf'))
        o5 = Base("string")
        o6 = Base(["list", 4, 2.5])
        o7 = Base(None)

        self.assertEqual(o1.id, 1)
        self.assertEqual(o2.id, 9)
        self.assertEqual(o3.id, 9.5)
        self.assertEqual(o4.id, float('inf'))
        self.assertEqual(o5.id, "string")
        self.assertEqual(o6.id, ["list", 4, 2.5])
        self.assertEqual(o7.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        """
        Testing to_json_string()
        """

        o1_1 = [{"hi": 1, "yo": "hol"}]
        o1_2 = [{"hello": 3}]
        o1_3 = None
        o1_4 = "a string"
        o1_5 = 123
        o1_6 = [[1, 2, 3]]
        o1_7 = []

        self.assertCountEqual(Base.to_json_string(o1_1),
                              '[{"hi": 1, "yo": "hol"}]')
        self.assertCountEqual(Base.to_json_string(o1_2), '[{"hello": 3}]')
        self.assertCountEqual(Base.to_json_string(o1_3), '[]')
        self.assertCountEqual(Base.to_json_string(o1_4), '"a string"')
        with self.assertRaises(TypeError):
            Base.to_json_string(o1_5)
        self.assertCountEqual(Base.to_json_string(o1_6), '[[1, 2, 3]]')
        self.assertCountEqual(Base.to_json_string(o1_7), '[]')

    def test_from_json_string(self):
        """
        Testing from_json_string(), uses to_json_string to format,
        anything not in format should return an empty list
        """

        o2_1 = [{"hi": 1, "yo": "hol"}]
        r2_1 = Base.to_json_string(o2_1)
        o2_2 = [{"hello": 3}]
        r2_2 = Base.to_json_string(o2_2)
        o2_3 = None
        r2_3 = Base.to_json_string(o2_3)
        o2_4 = "a string"
        r2_4 = Base.to_json_string(o2_4)
        o2_5 = 123
        o2_6 = [[1, 2, 3]]
        r2_6 = Base.to_json_string(o2_6)
        o2_7 = []
        r2_7 = Base.to_json_string(o2_7)

        self.assertEqual(Base.from_json_string(r2_1), o2_1)
        self.assertEqual(Base.from_json_string(r2_2), o2_2)
        self.assertEqual(Base.from_json_string(r2_3), [])
        self.assertEqual(Base.from_json_string(r2_4), o2_4)
        self.assertEqual(Base.from_json_string(o2_5), [])
        self.assertEqual(Base.from_json_string(r2_6), o2_6)
        self.assertEqual(Base.from_json_string(r2_7), o2_7)
        self.assertEqual(Base.from_json_string(o2_1), [])
        self.assertEqual(Base.from_json_string(o2_3), [])
        self.assertEqual(Base.from_json_string(o2_7), [])

    def test_create(self):
        """
        Testing create()
        """

        o3_1 = {'id': 1, 'width': 1, 'height': 2, 'x': 2, 'y': 2}
        r3_1 = Rectangle.create(**o3_1)
        self.assertEqual(r3_1.__str__(), '[Rectangle] (1) 2/2 - 1/2')

        o3_2 = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        s3_1 = Square.create(**o3_2)
        self.assertEqual(s3_1.__str__(), '[Square] (2) 4/5 - 3')

        o3_2 = {'id': 1, 'width': "string", 'height': 2, 'x': 2, 'y': 2}
        o3_3 = {'id': 2, 'size': "string", 'x': 4, 'y': 5}
        with self.assertRaises(TypeError):
            r3_2 = Rectangle.create(**o3_2)
            s3_2 = Square.create(**o3_3)

    def test_save_to_file(self):
        """
        Testing save_to_file()
        """

        o4_1 = Rectangle(10, 7, 2, 8)
        o4_2 = Rectangle(2, 4)
        o4_3 = Square(10, 7, 2)
        o4_4 = Square(8)

        rsave = Rectangle.save_to_file([o4_1, o4_2])
        ssave = Square.save_to_file([o4_3, o4_4])

        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))

    def test_load_from_file(self):
        """
        Testing load_from_file()
        """

        o5_1 = Rectangle(10, 7, 2, 8)
        o5_2 = Rectangle(2, 4)
        o5_3 = Square(10, 7, 2)
        o5_4 = Square(8)

        rsave = Rectangle.save_to_file([o5_1, o5_2])
        ssave = Square.save_to_file([o5_3, o5_4])

        rlist = Rectangle.load_from_file()
        slist = Square.load_from_file()

        self.assertIsInstance(rlist[0], Rectangle)
        self.assertIsInstance(rlist[1], Rectangle)
        self.assertIsInstance(slist[0], Square)
        self.assertIsInstance(slist[1], Square)

        self.assertEqual(rlist[0].__str__(), '[Rectangle] (1) 2/8 - 10/7')
        self.assertEqual(rlist[1].__str__(), '[Rectangle] (2) 0/0 - 2/4')
        self.assertEqual(slist[0].__str__(), '[Square] (3) 7/2 - 10')
        self.assertEqual(slist[1].__str__(), '[Square] (4) 0/0 - 8')

if __name__ == '__main__':
    unittest.main()