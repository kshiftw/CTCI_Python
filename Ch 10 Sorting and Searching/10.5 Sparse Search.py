""" Cracking the Coding Interview, 6th Edition - Python Solutions
10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball, ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
Output: 4
"""
import unittest
from unittest import TestCase


def sparse_search(array: list, string: str) -> int:
    """ Search for a string in a sorted array of strings that includes empty strings.

    Idea:
    - Because it is a sorted array of strings, we can use a modification of binary search. If the mid string is empty,
    find the closest non-empty string as the mid

    Complexity:
    - Time: O(N) - if all elements must be searched
    - Space: O(log(N)) - recursive binary search call stack

    Approach:
    - Modify binary search by adjusting the mid index to a non-empty string
    """
    return binary_search(array, string, 0, len(array) - 1)


def binary_search(array, string, low, high):
    if high < low:
        return
    mid = low + ((high - low) // 2)

    # if mid is an empty string, find the closest non-empty string
    if not array[mid]:
        left = mid - 1
        right = mid + 1
        while True:
            if left < low and right < high:
                return
            elif right <= high and array[right]:
                mid = right
                break
            elif left >= low and array[left]:
                mid = left
                break
            right += 1
            left -= 1

    if string == array[mid]:
        return mid
    elif string < array[mid]:
        return binary_search(array, string, low, mid - 1)
    else:
        return binary_search(array, string, mid + 1, high)


class TestSparseSearch(TestCase):
    def testA(self):
        array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
        self.assertEqual(sparse_search(array, 'ball'), 4)
        self.assertEqual(sparse_search(array, 'dad'), 10)


if __name__ == "__main__":
    unittest.main()