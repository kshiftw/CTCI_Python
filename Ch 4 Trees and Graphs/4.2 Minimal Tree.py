""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""
import unittest
from unittest import TestCase


def minimal_tree(array: list) -> object:
    """ Generates a minimal height tree given a sorted array of unique integers.

    Idea:
    - Minimal height is obtained by having the left subtree and right subtree's heights nearly equivalent
    - We can achieve this by taking the middle element of the array as the root

    Complexity:
    - Time: O(N) - need to loop through all elements of the array
    - Space: O(N) - minimal_tree will be added to the call stack N times

    Approach:
    - Calculate the index of the middle element and create a Node object with the value
    - Set the left and right subtrees being the left and right sub-arrays, respectively
    """
    if not array:
        return
    mid = len(array) // 2
    node = Node(array[mid])
    node.left = minimal_tree(array[:mid])
    node.right = minimal_tree(array[mid+1:])
    return node


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.array = []

    def get_children(self):
        def traverse(node):
            if not node:
                return
            self.array.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self)
        return self.array


class TestMinimalTree(TestCase):
    def testA(self):
        tree = minimal_tree([1, 2, 3, 4, 5])
        self.assertEqual(tree.get_children(), [3, 2, 1, 5, 4])

    def testB(self):
        tree = minimal_tree([1, 5, 7, 10, 12, 20, 50])
        self.assertEqual(tree.get_children(), [10, 5, 1, 7, 20, 12, 50])


if __name__ == "__main__":
    unittest.main()