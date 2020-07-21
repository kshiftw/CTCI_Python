"""
Python implementation of Bubble Sort.
"""
import unittest
from unittest import TestCase


def bubble_sort(array: list) -> list:
    """ Sort an array using bubble sort.

    Idea:
    - Compare and swap if current item is larger than the next
        - Continue swapping until the end, which will result in the largest element is the last element
        - Repeat process so that the second largest element is the second last element, etc.
    - After each ith loop, the ith last element will be in the proper position in the array

    Complexity:
    - Time:
        Worst: O(N^2) - two nested for loops that each loop through the array
        Best: O(N) - if array is sorted, just need to loop through all elements once
    - Space: O(1) - constant time to swap elements

    Example:
    Input: [5, 4, 6, 3, 1]
    Loops:
        [4, 5, 3, 1, 6]
        [4, 3, 1, 5, 6]
        [3, 1, 4, 5, 6]
        [1, 3, 4, 5, 6]
        [1, 3, 4, 5, 6]

    Approach:
    - Nested for loop
        - Outer loop - loops through the array N times
        - Inner loop - loops through entire array, removing one element from the end every loop
    """
    for index in range(len(array)):
        # If we make a full pass without having to swap, then we have sorted everything
        already_sorted = True

        # The subarray we check has one less element (the last element) after each loop b/c the end is where all the
        # sorted elements have "bubbled" to
        for j in range(len(array) - 1 - index):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        print(array)

        if already_sorted:
            break
    return array


class TestBubbleSort(TestCase):
    def testA(self):
        array = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(array), [1, 2, 3, 4, 5])

    def testB(self):
        array = [5, 4, 6, 3, 1]
        self.assertEqual(bubble_sort(array), [1, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()