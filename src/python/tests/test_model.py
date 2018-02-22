import unittest
from project import model


class DummyTest(unittest.TestCase):
    def test_number_no_list(self):
        self.assertEqual(model.power(2), 4)

    def test_number_one(self):
        self.assertEqual(model.power([2]), [4])

    def test_number_multiple(self):
        self.assertEqual(model.power([1, 2, 3]).tolist(), [1, 4, 9])
