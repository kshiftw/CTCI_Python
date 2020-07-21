""" Cracking the Coding Interview, 6th Edition - Python Solutions
10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.
"""
import unittest
from unittest import TestCase
from collections import Counter


def group_anagrams(array: list) -> list:
    """ Group an array of strings based on if they are anagrams of each other.

    Idea:
    - Anagrams have the same number of characters
    - If two strings are anagrams, their sorted string will be the same

    Complexity:
    - Time: O(N * log(N)) - from sorting each string
    - Space: O(N) - temporary storage for sorting

    Approach:
    - Sort the array based on each element's sorted string
    """
    array.sort(key=lambda x: sorted(x))
    return array


class TestGroupAnagrams(TestCase):
    def testA(self):
        strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
        self.assertEqual(group_anagrams(strings),
                         ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])


if __name__ == "__main__":
    unittest.main()