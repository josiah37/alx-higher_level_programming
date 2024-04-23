import unittest
# import models.base.Base
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2 = Base(4)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 4)


if __name__ == '__main__':
    unittest.main()
