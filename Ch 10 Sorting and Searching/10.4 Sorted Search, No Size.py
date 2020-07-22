""" Cracking the Coding Interview, 6th Edition - Python Solutions
10.4 Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt(i) method that returns the element at index i in
0(1) time. If i is beyond the bounds of the data structure, it returns - 1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
"""
import unittest
from unittest import TestCase


def sorted_search(listy: object, x: int) -> int:
    """ Find the index of x given a Listy data structure.

    Idea:
    - Use binary search b/c array elements are sorted. The only difference is that we have to find the length of the
    listy or the boundaries of the subarray containing the element we're looking for

    Complexity:
    - Time: O(log(N)) - finding the length takes O(log(N)) and binary search takes O(log(N))
    - Space: O(log(N)) - recursive binary search call stack

    Approach:
    - First find the length / boundary of the subarray containing the element
    - Use binary search to find the element
    """
    index = 1
    while listy.element_at(index) != -1 and listy.element_at(index) < x:
        index *= 2
    return binary_search(listy, x, index // 2, index)


def binary_search(listy, element, low, high):
    if high < low:
        return
    mid = low + ((high - low) // 2)

    # if mid is greater than the element or if our mid is out of bounds, look at left subarray
    if listy.element_at(mid) > element or listy.element_at(mid) == -1:
        return binary_search(listy, element, low, mid - 1)
    elif listy.element_at(mid) < element:
        return binary_search(listy, element, mid + 1, high)
    elif listy.element_at(mid) == element:
        return mid


class Listy:
    def __init__(self, array):
        self.array = array

    def element_at(self, index):
        if index < 0 or index >= len(self.array):
            return -1
        else:
            return self.array[index]


class TestSortedSearch(TestCase):
    def testA(self):
        listy = Listy([1, 2, 4, 6, 7, 10, 12, 14])
        self.assertEqual(sorted_search(listy, 6), 3)
        self.assertEqual(sorted_search(listy, 10), 5)


if __name__ == "__main__":
    unittest.main()