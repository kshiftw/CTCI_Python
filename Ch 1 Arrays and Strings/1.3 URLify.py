""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.3 URLify: Write a method to replace all spaces in a string with '%20'
"""
import unittest
from unittest import TestCase


def urlify(string: str) -> str:
    """ Returns a new string where all space character are replace by "%20".

    Idea: Find all instances of space characters and replace with "%20"

    Complexity:
    - Time: O(N) - find all spaces by looping through the entire string
    - Space: O(N) - string.split() returns a list of all space separated characters

    Approach:
    - use split() to get a list of words without space characters
    - use join() to join all the words together with '%20' as the separator
    """
    return '%20'.join(string.split(" "))


class TestUrlify(TestCase):
    def testA(self):
        actual = urlify('joker')
        expected = 'joker'
        self.assertEqual(actual, expected)

    def testB(self):
        actual = urlify('Hello World')
        expected = 'Hello%20World'
        self.assertEqual(actual, expected)

    def testC(self):
        actual = urlify('  What do we do with spaces?')
        expected = '%20%20What%20do%20we%20do%20with%20spaces?'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()