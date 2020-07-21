"""
Python implementation of Quick Sort.
"""
import unittest
from unittest import TestCase
from random import randint


def quick_sort(array: list) -> list:
    """ Sort an array using quick sort.

    Idea:
    - Select a random pivot element and partition the array into three arrays based on their value compared to the
    pivot: low, same, high
    - It will eventually reach the base case where there are single element arrays put into the correct order based on
    their relative values
        - quick_sort() will be called again on these single element subarrays where it will hit the base case where the
        subarray has a length of 1

    Complexity:
    - Time:
        Worst: O(N^2) - if the pivot element is either the smallest or largest element, then the partitions will be
        unequal
        Best/Average: O(N*log(N)) - partition (for loop) is in linear time and the partitioning process repeats
        recursively on average log(N) times
            - Average case is where the pivot is near or equal to the median element of the array
    - Space: O(log(N)) - call stack to store recursive calls of quick_sort() on low subarray until single element

    Approach:
    - Base case: return the array if it is a single element
    - Select a random element as the pivot element
    - Loop through the entire array and compare against pivot
        - Add the element to the appropriate subarray (low, same, high)
    - Return the combination of all three subarrays after they are sorted using the recursive call of quick_sort()
    """
    if len(array) <= 1:
        return array

    low = []
    same = []
    high = []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)


class TestQuickSort(TestCase):
    def testA(self):
        array = [5, 4, 3, 2, 1]
        self.assertEqual(quick_sort(array), [1, 2, 3, 4, 5])

    def testB(self):
        array = [5, 4, 6, 3, 1]
        self.assertEqual(quick_sort(array), [1, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()