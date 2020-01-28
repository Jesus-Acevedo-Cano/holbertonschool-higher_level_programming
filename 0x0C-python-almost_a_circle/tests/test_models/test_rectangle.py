#!/usr/bin/python3
""" Unittest for Class rectangle """
import unittest
import sys
import io
from models.rectangle import Rectangle


class Test_Rectangle_Class(unittest.TestCase):
    """ Tests for class rectangle"""

    def test_create(self):
        """ creating a valid obj Rectangle """
        with self.assertRaises(TypeError):
            obj1 = Rectangle()
        with self.assertRaises(TypeError):
            obj2 = Rectangle(10, 9, 12, 12, 12, 12, 12, 12)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(10, 12, 12, 12, 12, 12)

    def test_id(self):
        """
        test id in Base
        """
        pass

    def test_invalid_data(self):
        """
        test invalid data
        """
        with self.assertRaises(ValueError):
            obj4 = Rectangle(0, 9)
        with self.assertRaises(ValueError):
            obj5 = Rectangle(1, -1)
        with self.assertRaises(TypeError):
            obj6 = Rectangle(2, "2")
        with self.assertRaises(TypeError):
            obj7 = Rectangle(2, [1, 2, 3, 4])

    def test_area(self):
        """
        test area
        """
        obj1 = Rectangle(1, 1)
        self.assertEqual(obj1.area(), 1)
        obj1 = Rectangle(24, 24)
        self.assertEqual(obj1.area(), 576)
        obj1 = Rectangle(8, 7)
        obj1.width = 8
        self.assertEqual(obj1.area(), 56)

    def test_display(self):
        """
        test display
        """
        obj1 = Rectangle(1, 1)
        self.assertEqual(obj1.display(), None)
        obj1 = Rectangle(3, 1)
        obj1.id = 8
        self.assertEqual(obj1.display(), None)
        obj1 = Rectangle(1, 1)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "display")
        correct = "#\n"
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(1, 2)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "display")
        correct = "#\n#\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_(self):
        """
        test __str__
        """
        obj1 = Rectangle(4, 3)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/3\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(12, 3, 1, 1)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "print")
        correct = "[Rectangle] ({}) 1/1 - 12/3\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(12, 9, 1, 1)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "print")
        correct = "[Rectangle] ({}) 1/1 - 12/9\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())

    def test_update(self):
        """
        test update args
        """
        r1 = Rectangle(10, 10)
        r1.update(89)
        capture = Test_Rectangle_Class.capture_stdout(r1, "print")
        correct = "[Rectangle] (89) 0/0 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 29)
        capture = Test_Rectangle_Class.capture_stdout(r1, "print")
        correct = "[Rectangle] (89) 10/10 - 29/10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        capture = Test_Rectangle_Class.capture_stdout(r1, "print")
        correct = "[Rectangle] (10) 10/10 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())

    def test_update2(self):
        """
        test update kwargs
        """
        r1 = Rectangle(10, 10)
        r1.update(id=89)
        capture = Test_Rectangle_Class.capture_stdout(r1, "print")
        correct = "[Rectangle] (89) 0/0 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=29, id=89)
        capture = Test_Rectangle_Class.capture_stdout(r1, "print")
        correct = "[Rectangle] (89) 10/10 - 29/10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        capture = Test_Rectangle_Class.capture_stdout(r1, "print")
        correct = "[Rectangle] (10) 10/10 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())

    def test_display2(self):
        """
        test display
        """
        obj1 = Rectangle(1, 1)
        self.assertEqual(obj1.display(), None)
        obj1 = Rectangle(3, 1)
        obj1.id = 8
        self.assertEqual(obj1.display(), None)
        obj1 = Rectangle(1, 1, 1, 1)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "display")
        correct = "\n #\n"
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(1, 2, 2, 2)
        capture = Test_Rectangle_Class.capture_stdout(obj1, "display")
        correct = "\n\n  #\n  #\n"
        self.assertEqual(correct, capture.getvalue())

    def test_to_dic(self):
        """
        test to dict
        """
        r1 = Rectangle(10, 2, 1, 9, 90)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {'id': 90,
                                             'width': 10,
                                             'height': 2,
                                             'x': 1,
                                             'y': 9})
        r1 = Rectangle(10, 5, 1, 10, 98)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {'id': 98,
                                             'width': 10,
                                             'height': 5,
                                             'x': 1,
                                             'y': 10})

    @staticmethod
    def capture_stdout(obj, method):
        """
        return the stdoutput bdbaraban
        """
        ioValue = io.StringIO()
        sys.stdout = ioValue
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return ioValue
