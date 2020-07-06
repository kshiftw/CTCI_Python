""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. can you do this in place?
"""
import unittest
from unittest import TestCase


def rotate_matrix(matrix: list) -> list:
    """ Rotate an NxN square matrix clockwise 90 degrees.

    Idea:
    - Loop through each layer of the matrix starting from the outer towards the inside
    - For each layer, view each of the sides (top, bottom, left, right) as a list of its own and swap all cells
        - Save one side and use a loop to swap all corresponding indices

    Complexity:
    - Time: O(N*N) - must loop through all N*N elements
    - Space: O(1) - constant space to swap values

    Approach:
    - Loop through layers by using a for loop to keep track of the layer index from 0 to half of N
        - Only need to go until the middle of the length of the matrix otherwise it will do more swapping than needed
    - For each layer index, calculate the index of the start and end of the sub-lists we will be looking at
        - Have a for loop that goes from the start to end index of the sub-lists and swap all cells
        - (end - offset) gives us the index of the cell if you were to start from the end of the list
    """
    if not matrix:
        return []

    n = len(matrix)
    for layer in range(n // 2):
        start = layer
        end = n - 1 - layer
        for index in range(start, end):
            offset = index - start
            top = matrix[start][index]
            matrix[start][index] = matrix[end - offset][start]
            matrix[end - offset][start] = matrix[end][end-offset]
            matrix[end][end-offset] = matrix[index][end]
            matrix[index][end] = top
    return matrix


class TestRotateMatrix(TestCase):
    def testA(self):
        actual = rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(actual, expected)

    def testB(self):
        actual = rotate_matrix([[1, 2, 3, 4, 5],
                                [6, 7, 8, 9, 10],
                                [11, 12, 13, 14, 15],
                                [16, 17, 18, 19, 20],
                                [21, 22, 23, 24, 25]])
        expected = [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
        self.assertEqual(actual, expected)

    def testC(self):
        actual = rotate_matrix([])
        expected = []
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()