""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest
from unittest import TestCase
from collections import Counter


def check_permutation(first_string: str, second_string: str) -> bool:
    """ Check if one string is a permutation of another string.

    Idea: A string is a permutation of another if each string has the same number of occurrences of characters.

    Approach:
    - Use Counter to get a dictionary containing the character as the key and their count as the value for each string
    - Compare the two Counters
    """
    return Counter(first_string) == Counter(second_string)


class TestCheckPermutation(TestCase):
    def testA(self):
        actual = check_permutation('joker', 'kojer')
        expected = True
        self.assertEqual(actual, expected)

    def testB(self):
        actual = check_permutation('keyboard', 'badkey')
        expected = False
        self.assertEqual(actual, expected)

    def testC(self):
        actual = check_permutation('bad', 'dab')
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()