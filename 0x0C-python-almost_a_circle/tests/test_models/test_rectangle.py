""" this is a test file for for the class rectangle"""
import unittest
# import sys
# import io
# from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ checking the input"""

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r = Rectangle(10, 2, 3, 5, 6)
        self.assertEqual(r.id, 6)

    def test_under_or_over_limit_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2)
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 2, 5, 1, 4)


class TestRectangleWidth(unittest.TestCase):
    """setters, getters, non, nun, string, float,
    dict, string,bool, -ve no, normal no, 0,"""

    def test_width_setter(self):
        r = Rectangle(1, 2, 3)
        r.width = 8
        self.assertEqual(r.width, 8)

    def test_width_getter(self):
        r = Rectangle(6, 7, 8, 2, 1)
        self.assertEqual(r.width, 6)


class Test_for_invlaid_cases(unittest.TestCase):
    """ test case that would raise type and value errors"""
    def test_invalid_width_and_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "10", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 10, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, None, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 10, None)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 10.1, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 3, 10.1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, (10, 1), 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 2, (10, 1))
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 10, {})
        with self.assertRaises(TypeError):
            Rectangle(1, 1, {}, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, (10, 1), 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, [], 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, [2, 12], 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 5, [])
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 5, [2, 4])

        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

    def setUp(self):
        """This will be a standard for the rest to
        avoid duplication and creating many objects
        """
        self.rect = Rectangle(4, 3, 2, 1)

    def test_invalid_x_and_y(self):
        with self.assertRaises(TypeError):
            self.rect.x = "10"
        with self.assertRaises(TypeError):
            self.rect.y = "2"
        with self.assertRaises(TypeError):
            self.rect.x = None
        with self.assertRaises(TypeError):
            self.rect.y = None
        with self.assertRaises(TypeError):
            self.rect.x = 10.1
        with self.assertRaises(TypeError):
            self.rect.y = 10.1
        with self.assertRaises(TypeError):
            self.rect.x = (10, 1)
        with self.assertRaises(TypeError):
            self.rect.y = (10.1)
        with self.assertRaises(TypeError):
            self.rect.y = {}
        with self.assertRaises(TypeError):
            self.rect.x = {}
        with self.assertRaises(TypeError):
            self.rect.x = []
        with self.assertRaises(TypeError):
            Rectangle(1, 1, [2, 12], 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 5, [])
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 5, [2, 4])

        with self.assertRaises(ValueError):
            self.rect.x = -1
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)


if __name__ == "__main__":
    unittest.main()
