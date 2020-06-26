""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use
additional data structures?
"""
import unittest
from unittest import TestCase


def is_unique(string: str) -> bool:
    """ Checks if a string has all unique characters.

    Approach:
    - Loop through all characters of the string
    - Keep a count of the number of occurrences for each character using a dictionary, char_dict
    - If we have already seen a character, then the string cannot be unique, return False.
    - If we loop through the entire string without finding a duplicate, return True.
    """
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            return False
    return True


class TestIsUnique(TestCase):
    def testA(self):
        actual = is_unique('abcdef')
        expected = True
        self.assertEqual(actual, expected)

    def testB(self):
        actual = is_unique('abcda')
        expected = False
        self.assertEqual(actual, expected)

    def testC(self):
        actual = is_unique('')
        expected = True
        self.assertEqual(actual, expected)

    def testD(self):
        actual = is_unique('zzzz')
        expected = False
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
