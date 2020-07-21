""" Cracking the Coding Interview, 6th Edition - Python Solutions
10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""
import unittest
from unittest import TestCase


def sorted_merge(A: list, B: list, A_length: int, B_length: int):
    """ Merge two sorted arrays given that the first array has enough space allocated for the other.

    Idea:
    - Start from largest to smallest so that we don't have to shift elements

    Complexity:
    - Time: O(N + M) where N is number of elements in A and M is number of elements in B
    - Space: O(1) - constant space to store pointers

    Approach:
    - Keep track of 3 pointers
        - index A starts from the end of elements in A
        - index B starts from the end of elements in B
        - index last starts from the end of A
    - Compare values between A and B, putting the larger value at index_last until we reach the front of both A and B
    """
    index_a = A_length - 1
    index_b = B_length - 1
    index_last = index_a + index_b + 1

    while index_b >= 0:
        if index_a >= 0 and A[index_a] > B[index_b]:
            A[index_last] = A[index_a]
            index_a -= 1
        # if there are no more elements from A or if B > A
        else:
            A[index_last] = B[index_b]
            index_b -= 1
        index_last -= 1


class TestSortedMerge(TestCase):
    def testA(self):
        arrayA = [1, 3, 4, 5, None, None, None]
        arrayB = [2, 6, 10]
        sorted_merge(arrayA, arrayB, 4, 3)
        self.assertEqual(arrayA, [1, 2, 3, 4, 5, 6, 10])

    def testB(self):
        arrayA = [1, 13, 15, 17, None, None, None, None, None]
        arrayB = [2, 6, 10, 16, 18]
        sorted_merge(arrayA, arrayB, 4, 5)
        self.assertEqual(arrayA, [1, 2, 6, 10, 13, 15, 16, 17, 18])


if __name__ == "__main__":
    unittest.main()