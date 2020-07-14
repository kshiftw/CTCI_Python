""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""
import unittest
from unittest import TestCase


def robot_grid(grid: list) -> str:
    """ Find a path from top left to bottom right of a grid.

    Assumption:
    - Assume grid is given where 0 represents an available cell and 1 represents an off-limit cell

    Idea:
    - Recursively call the traverse function for each cell's right and bottom adjacent neighbours
        - If it is an off-limit cell, return None
    - The 'or' statement will return the first function's return if it is not None. If the first function returns None,
    then it will return the second function's return, regardless of it's truth value.
        - That means that if any of the right or bottom adjacent neighbours lead to a valid path, it will return the
        path, else if there are no valid paths, return None

    Complexity:
    - Time: O(N*M) - N is number of rows and M is number of columns. Algorithm may access all cells of the grid
    - Space: O(N*M) - store visited cells

    Approach:
    - Make sure to check that the row and column index are within the grid
    - Use a visited dictionary to keep track of paths that already include a cell to avoid redundant function calls
    """
    rows = len(grid)
    cols = len(grid[0])
    visited = {}

    def traverse(row, col, path):
        if row < rows and col < cols:
            if (row, col) in visited:
                return None
            visited[(row, col)] = True
            if grid[row][col] == 1:
                return None
            if row == rows - 1 and col == cols - 1:
                return path
            return traverse(row + 1, col, path + "D") or traverse(row, col + 1, path + "R")
    return traverse(0, 0, "")


class TestRobotGrid(TestCase):
    def testA(self):
        grid = [[0, 0, 0],
                [0, 1, 0],
                [1, 0, 0]]
        self.assertEqual(robot_grid(grid), "RRDD")

    def testB(self):
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(robot_grid(grid), "RRRDDRRRD")

    def testC(self):
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(robot_grid(grid), None)

    def testD(self):
        grid = [[0, 0, 0, 1, 0, 0, 1],
                [0, 1, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(robot_grid(grid), "DDRRRRRRD")

    def testE(self):
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(robot_grid(grid), "RRDRDRRRD")



if __name__ == "__main__":
    unittest.main()