""" Cracking the Coding Interview, 6th Edition - Python Solutions
10.3 Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
"""
import unittest
from unittest import TestCase


def search_rotated_array(array: list, element: int, left=0, right=None):
    """

    Idea:
    - If the first element is less than the mid element, then we know the left subarray is sorted
        - Choose to search the left or right subarray depending on whether the element is between left and mid values
    - If the first element is greater than the mid element, then we know the right subarray is sorted
        - Same idea as above
    - We also have to take into account arrays with duplicates
        - If the first element is the same as mid, check if the last element is also the same
            - If not same, search the right subarray
            - If the same, we have to search both left and right subarrays

    Complexity:
    - Time:
        - O(log(N)) if all elements are unique b/c we are essentially using binary search to find the element
        - O(N) if there are many duplicates b/c we have to search both left and right subarrays (up to searching all
        elements)
    - Space:
        - O(log(N)) - call stack for recursive function call

    Approach:
    - Base case:
        - If there are no more elements to search (right pointer < left pointer)
        - If the mid value is the element we're looking for
    """
    if not right:
        right = len(array) - 1

    if right < left:
        return None

    mid = left + ((right - left) // 2)
    if array[mid] == element:
        return mid

    if array[left] < array[mid]:
        if array[left] <= element < array[mid]:
            return search_rotated_array(array, element, left, mid - 1)
        else:
            return search_rotated_array(array, element, mid + 1, right)
    elif array[left] > array[mid]:
        if array[mid] < element <= array[right]:
            return search_rotated_array(array, element, mid + 1, right)
        else:
            return search_rotated_array(array, element, left, mid - 1)
    elif array[left] == array[mid]:
        if array[mid] != array[right]:
            return search_rotated_array(array, element, mid + 1, right)
        else:
            search_left = search_rotated_array(array, element, left, mid - 1)
            if not search_left:
                return search_rotated_array(array, element, mid + 1, right)
            else:
                return search_left


class TestSearchRotatedArray(TestCase):
    def testA(self):
        array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(search_rotated_array(array, 5), 8)
        self.assertEqual(search_rotated_array(array, 20), 3)


if __name__ == "__main__":
    unittest.main()