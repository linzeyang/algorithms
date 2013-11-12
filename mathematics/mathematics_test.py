# unit testings for mathematical algorithms in Python

import math
from unittest import TestCase, main

from mathematics import *


class MathTestCase(TestCase):

    def test_factorial_normal_with_small_integer(self):
        test_int = 10
        expected = 3628800

        self.assertEqual(factorial_normal(test_int), expected)


    def test_factorial_normal_with_large_integer(self):
        test_int = 100
        expected = math.factorial(test_int)

        self.assertEqual(factorial_normal(test_int), expected)


    def test_factorial_recursive_with_small_integer(self):
        test_int = 10
        expected = 3628800

        self.assertEqual(factorial_recursive(test_int), expected)


    def test_factorial_recursive_with_large_integer(self):
        test_int = 100
        expected = math.factorial(test_int)

        self.assertEqual(factorial_recursive(test_int), expected)


if __name__ == '__main__':
    main()