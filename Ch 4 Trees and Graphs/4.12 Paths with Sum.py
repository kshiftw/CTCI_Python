""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to ch ild nodes).
"""
import unittest
from unittest import TestCase
from tree import TreeNode
from collections import defaultdict


def paths_with_sum(tree, target_value):
    """ Return the number of paths that have sum equal to the target value.

    Brute Force O(N^2):
    - For every node in tree, traverse through all paths and compare the sum to target value

    Idea:
    - Keep track of running_sum in a dictionary that keeps track of the count
    - For each node, calculate a running sum that a previous node would have needed in order to have a target sum from
    the path of the previous node to the current node
        - This calculated as search_sum = running_sum - target

    Complexity:
    - Time: O(N)
    - Space: O(log(N)) - call stack for binary tree

    Approach:
    - use default dictionary that sets default value as 0
        - don't need to check if key exists in dictionary
    """
    sum_table = defaultdict(int)

    def dfs(node, target, running_sum):
        if not node:
            return 0
        running_sum += node.value
        search_sum = running_sum - target
        if search_sum not in sum_table:
            total_paths = 0
        else:
            total_paths = sum_table[search_sum]

        if running_sum == target:
            total_paths += 1

        sum_table[running_sum] += 1
        total_paths += dfs(node.left, target, running_sum)
        total_paths += dfs(node.right, target, running_sum)
        sum_table[running_sum] -= 1

        return total_paths

    return dfs(tree, target_value, 0)


class TestPathsWithSum(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.left.left = TreeNode(3)
        tree.left.left.left = TreeNode(3)
        tree.left.left.right = TreeNode(-2)
        tree.left.right = TreeNode(1)
        tree.left.right.right = TreeNode(2)
        tree.right = TreeNode(-3)
        tree.right.right = TreeNode(11)

        self.assertEqual(paths_with_sum(tree, 8), 3)


if __name__ == "__main__":
    unittest.main()