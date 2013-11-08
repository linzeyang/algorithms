# unit testings for sorting algorithms in Python

from unittest import TestCase, main

from sorting import *


class SortingTestCase(TestCase):
    def test_bubble_sort_with_short_list(self):
        test_list = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
        expected_list = [2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

        self.assertEqual(bubble_sort(test_list), expected_list)


    def test_bubble_sort_with_ultra_long_list(self):
        test_list = range(10**4)
        test_list = reverse_list(test_list)
        expected_list = range(10**4)

        self.assertEqual(bubble_sort(test_list), expected_list)


    def test_insertion_sort_with_short_list(self):
        test_list = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
        expected_list = [2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

        self.assertEqual(insertion_sort(test_list), expected_list)


    def test_insertion_sort_with_ultra_long_list(self):
        test_list = range(10**4)
        test_list = reverse_list(test_list)
        expected_list = range(10**4)

        self.assertEqual(insertion_sort(test_list), expected_list)


def reverse_list(original_list):
    length = len(original_list)
    reversed_list = []

    while length > 0:
        reversed_list.append(original_list[length - 1])
        length -= 1

    return reversed_list


if __name__ == "__main__":
    import sys, unittest
    suite = unittest.TestSuite()
    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(SortingTestCase)
    else:
        for test_name in sys.argv[1:]:
            suite.addTest(SortingTestCase(test_name))

    unittest.TextTestRunner(verbosity=2).run(suite)
