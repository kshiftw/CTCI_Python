""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
"""
import unittest
from unittest import TestCase


def zero_matrix(matrix: list) -> list:
    """ All rows and columns in an MxN matrix that contain a 0 have all cells set to 0.

    Idea:
    - Keep track of original vs newly set zeros with an MxN matrix, new_zero

    Complexity:
    - Time: O(M*N) - loop through M*N elements
    - Space: O(M*N) - new_zero is a matrix of size M*N

    Approach:
    - Loop through all cells of the matrix, if it is a 0 and an original zero, set all cells in that row and column to 0

    Alternatives:
    - Current solution uses O(MN) space. Can reduce it to O(M+N) space by keeping track of only the row and column
    indices that have a zero. Then loop through each of these indices to set the zeros
    """
    rows = len(matrix)
    cols = len(matrix[0])

    new_zero = [[False for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0 and not new_zero[row][col]:
                for row_index in range(rows):
                    if matrix[row_index][col] != 0:
                        matrix[row_index][col] = 0
                        new_zero[row_index][col] = True
                for col_index in range(cols):
                    if matrix[row][col_index] != 0:
                        matrix[row][col_index] = 0
                        new_zero[row][col_index] = True
    return matrix


class TestZeroMatrix(TestCase):
    def testA(self):
        actual = zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
        expected = [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
        self.assertEqual(actual, expected)

    def testB(self):
        actual = zero_matrix([[1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]])
        expected = [[0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()