""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (Ie., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.
"""
import unittest
from unittest import TestCase


def towers_hanoi(n: int, origin: list, buffer: list, destination: list):
    """ Solves the tower of hanoi problem for N disks.

    Idea:
    - Breakdown to a sub-problem:
        1) Move n-1 disks from origin to buffer using the destination as the buffer
        2) Move the largest disk to the destination
        3) Move n-1 disks from buffer to destination using the origin as the buffer

    Complexity:
    - Time: O(2^N) - for N disks, it takes ((2^N) - 1) steps to solve
    - Space: O(N) - call stack for tower_hanoi

    Approach:
    - Base case of 0 returns None
    """
    if n == 0:
        return
    towers_hanoi(n - 1, origin, destination, buffer)
    destination.append(origin.pop())
    towers_hanoi(n - 1, buffer, origin, destination)


class TestTowersHanoi(TestCase):
    def testA(self):
        tower1 = [4, 3, 2, 1]
        tower2 = []
        tower3 = []
        towers_hanoi(4, tower1, tower2, tower3)
        self.assertEqual(tower3, [4, 3, 2, 1])

    def testB(self):
        tower1 = [8, 7, 6, 5, 4, 3, 2, 1]
        tower2 = []
        tower3 = []
        towers_hanoi(8, tower1, tower2, tower3)
        self.assertEqual(tower3,  [8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()