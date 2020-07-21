"""
Python implementation of Merge Sort.
"""
import unittest
from unittest import TestCase


def merge_sort(array: list) -> list:
    """ Sort an array using merge sort.

    Idea:
    - Split into two functions:
        - Recursive: base function
            - Continuously splits the array in half into left and right subarrays until they are single elements
        - Iterative: merge()
            - Merges two subarrays together into a combined sorted array

    Complexity:
    - Time:
        - Worst: O(N*log(N)) - recursion halves the array until single element (log(N)) and merge() is called for each
        half, where merge() has O(N) runtime
        - Best: Same as Worst Case
    - Space: O(N) - store subarrays when recursively splitting into halves

    Approach:
    - Merge the left and right subarrays after they have been sorted using a recursive call of merge_sort()
    """
    # base case: when subarray is a single element array
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


def merge(left: list, right: list):
    # If either one is empty, return the other array
    if not left:
        return right
    if not right:
        return left

    result = []
    index_left = 0
    index_right = 0

    # loop until result is the same length as left and right subarray combined
    while len(result) < len(left) + len(right):
        # use two pointers to find next smallest element to add to result array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # if we have reached the end of either subarray, append the rest of the other subarray to result
        if index_left == len(left):
            result += right[index_right:]
            break
        if index_right == len(right):
            result += left[index_left:]
            break

    return result


class TestMergeSort(TestCase):
    def testA(self):
        array = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(array), [1, 2, 3, 4, 5])

    def testB(self):
        array = [5, 4, 6, 3, 1]
        self.assertEqual(merge_sort(array), [1, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()