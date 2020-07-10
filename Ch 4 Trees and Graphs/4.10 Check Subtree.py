""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.10 Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2 .
That is, if you cut off the tree at node n, the two trees would be identical.
"""
import unittest
from unittest import TestCase
from tree import TreeNode


def check_subtree(t1, t2):
    """

    Idea:
    - find_root() searches all t1 nodes for a match in value with t2's root
        - When we find a match, we then use same_subtree() to see if t1's subtree matches t2

    Complexity:
    - Time: O(N + kM) where N is the number of nodes in t1, M is the number of nodes in t2, and k is the number of
    occurrences of t2's root in t1
    - Space: O(log(N) + log(M)) - worst case, our call stack will have log(N) calls of find_root() when we start from t1
    root and aren't able to find any matches going down all left children. This is added with log(M) when we find a
    match of values, but they are not the same subtrees, meaning we have to traverse the entire t2 tree. This is log(M)
    because same_subtree() will be recursively called on the left node.

    Approach:
    - DFS through t1 to find a t2's root
        - If found, check if they are the same subtree by recursively comparing the values using another DFS function
        - If not found, continue searching t1 for t2 until we have traversed the entire t1 tree
    """
    return find_root(t1, t2)


def find_root(node, find):
    if not node:
        return False
    if node.value == find.value and same_subtree(node, find):
        return True
    return find_root(node.left, find) or find_root(node.right, find)


def same_subtree(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.value != node2.value:
        return False
    return same_subtree(node1.left, node2.left) and same_subtree(node1.right, node2.right)


class TestCheckSubtree(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(12)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(7)
        tree.right.right = TreeNode(15)

        subtree = TreeNode(5)
        subtree.left = TreeNode(3)
        subtree.right = TreeNode(7)
        self.assertEqual(check_subtree(tree, subtree), True)

        subtree2 = TreeNode(5)
        subtree2.left = TreeNode(3)
        subtree2.right = TreeNode(2)
        self.assertEqual(check_subtree(tree, subtree2), False)

        subtree3 = TreeNode(15)
        self.assertEqual(check_subtree(tree, subtree3), True)


if __name__ == "__main__":
    unittest.main()