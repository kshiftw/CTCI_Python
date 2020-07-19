""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.10 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""
import unittest
from unittest import TestCase


def paint_fill(image: list, point_x: int, point_y: int, color: int):
    """ Changes the color of all adjacent points with the same starting color.

    Assumption:
    - Color is an integer that has been converted from a hex representation of a color.

    Idea:
    - DFS through the graph from the given point
        - Keep track of the initial color as prev_color
        - Recursively travel adjacent points (up, down, left, right) if the color matches the initial color and set to
        new color

    Complexity:
    - Time: O(M*N) - M is number of rows, N is number of columns. May need to travel through all points in the image
    - Space: O(N) - call stack for traverse() function

    Approach:
    - Check that the point we are checking is valid (within the boundary) to prevent an IndexError on the image matrix
        - Check if the color matches the initial color
        - Change the color
        - For each adjacent point, call the traverse function
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows = len(image)
    cols = len(image[0])

    def traverse(row, col, prev_color):
        if 0 <= col < cols and 0 <= row < rows:
            if image[row][col] == prev_color:
                image[row][col] = color
                for direction in directions:
                    next_row, next_col = row + direction[0], col + direction[1]
                    traverse(next_row, next_col, prev_color)

    traverse(point_y, point_x, image[point_y][point_x])


class TestPaintFill(TestCase):
    def testA(self):
        image = [[1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 3, 0, 0, 0, 1],
                 [1, 3, 3, 255, 3, 0, 1],
                 [1, 0, 3, 255, 0, 0, 1],
                 [1, 0, 0, 255, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1]]
        paint_fill(image, 3, 1, 9)
        print("Test A:")
        for row in image:
            print(row)

    def testB(self):
        image = [[1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 3, 0, 0, 0, 1],
                 [1, 3, 3, 255, 3, 0, 1],
                 [1, 0, 3, 255, 0, 0, 1],
                 [1, 0, 0, 255, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1]]
        paint_fill(image, 3, 2, 9)
        print('Test B:')
        for row in image:
            print(row)

    def testC(self):
        image = [[1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 3, 0, 0, 0, 1],
                 [1, 3, 3, 255, 3, 0, 1],
                 [1, 0, 3, 255, 0, 0, 1],
                 [1, 0, 0, 255, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1]]
        paint_fill(image, 6, 3, 9)
        print('Test C:')
        for row in image:
            print(row)

    def testD(self):
        image = [[1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 3, 0, 0, 0, 1],
                 [1, 3, 3, 255, 3, 0, 1],
                 [1, 0, 3, 255, 0, 0, 1],
                 [1, 0, 0, 255, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1],
                 [1, 0, 0, 30, 0, 0, 1]]
        paint_fill(image, 4, 2, 9)
        print('Test D:')
        for row in image:
            print(row)


if __name__ == "__main__":
    unittest.main()