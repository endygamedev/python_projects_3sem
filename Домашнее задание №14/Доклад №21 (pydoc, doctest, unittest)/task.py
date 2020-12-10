"""
    Используя unittest, написать 4 теста с использованием assertEqual(), assertTrue() или assertFalse()
"""


import unittest
from math import sqrt, factorial


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(sqrt(4), 2)

    def test2(self):
        self.assertEqual(factorial(5), 120)

    def test3(self):
        self.assertTrue('5'.isnumeric())

    def test4(self):
        self.assertFalse('foo'.isupper())


if __name__ == '__main__':
    unittest.main()