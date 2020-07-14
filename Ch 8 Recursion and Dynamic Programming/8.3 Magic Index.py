""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.3 Magic Index: A magic index in an array A[1. .. n-1] is defined to be an index such that A[i] = i. Given a sorted
array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP: What if the values are not distinct?
"""
import unittest
from unittest import TestCase


def magic_index(array: list) -> int:
    """ Finds the magic index of a given array of sorted distinct integers.

    Idea:
    - Use binary search to effectively search for the magic index
    - If the current element has a value that is greater than the index, then we know that the magic index must be less
    than the current index
        - Similar idea, but the opposite for values less than its index

    Complexity:
    - Time: O(log(N)) - binary search an array
    - Space: O(1) - constant space to store low, high, and mid indices

    Approach:
    - Calculate the mid index using the low and high values
    - Evaluate the value at the mid index to see which part of the array to search
    """
    def search(low, high):
        if low > high:
            return None
        mid = low + ((high - low) // 2)
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            return search(mid + 1, high)
        else:
            return search(low, mid - 1)
    return search(0, len(array) - 1)


class TestMagicIndex(TestCase):
    def testA(self):
        array = [-3, -2, 1, 3, 5]
        self.assertEqual(magic_index(array), 3)

    def testB(self):
        array = [-3, -2, 1, 4, 5]
        self.assertEqual(magic_index(array), None)

    def testC(self):
        array = [-20, 0, 1, 2, 3, 4, 5, 7, 20]
        self.assertEqual(magic_index(array), 7)


if __name__ == "__main__":
    unittest.main()