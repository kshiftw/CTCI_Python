"""
Python implementation of Insertion Sort.
"""
import unittest
from unittest import TestCase


def insertion_sort(array: list) -> list:
    """ Sort an array using insertion sort.

    Idea:
    - Each loop, find and place the element in its correctly sorted position in the left subarray

    Complexity:
    - Time:
        Worst: O(N^2) - a nested while loop in the outer for loop, both looping through elements of the array
        Best: O(N) - If sorted, only the outer loop is executed
    - Space: O(1) - constant space to store the element and swap elements

    Example:
    Input: [5, 4, 6, 3, 1]
    Loops:
        [4, 5, 6, 3, 1]
        [4, 5, 6, 3, 1]
        [3, 4, 5, 6, 1]
        [1, 3, 4, 5, 6]

    Approach:
    - j is the index that loops through all elements in the left subarray until the appropriate sorted position is found
    """
    for index in range(1, len(array)):
        next_elem = array[index]
        j = index - 1
        while j >= 0 and array[j] > next_elem:
            # b/c the next value (index j) is greater than the element, we shift it to the right
            array[j + 1] = array[j]
            j -= 1
        # Either at the beginning of the array when j < 0 or the proper position btwn two elements when
        # array[j] < next_elem. This is where we "insert" the saved element
        array[j + 1] = next_elem
    return array


class TestInsertionSort(TestCase):
    def testA(self):
        array = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort(array), [1, 2, 3, 4, 5])

    def testB(self):
        array = [5, 4, 6, 3, 1]
        self.assertEqual(insertion_sort(array), [1, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()