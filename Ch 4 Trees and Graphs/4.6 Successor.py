""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""
import unittest
from unittest import TestCase
from tree import TreeNode


def successor(node: object) -> object:
    """ Return the in-order successor (the node with the next highest value) of a given node.

    Idea:
    - There are two places to look for the successor:
        1. The right subtree of a node contains values that are larger than the node
            - We just have to find the leftmost element of the right subtree which will give us the node with the
            smallest value out of all nodes that are larger than the node
            - This element in the right subtree will always be smaller than the node's ancestors b/c of BST properties
        2. If there isn't a right subtree, then we look to the node's ancestors
            - We traverse the node's parents until we find a node where it is the left child of another node
            - The parent of this left child is the successor because it is the next largest value. We know this based on
            the property that all left subtree values are less than a node.

    Complexity:
    - Time: O(log(N)) - worst case is if we have to traverse the height of the tree for cases where our node is at the
    bottom-right of the tree
    - Space: O(1) - constant space to store node pointers

    Approach:
    - First check if right subtree exists. If so, find the leftmost element of the subtree.
    - If right subtree doesn't exist, see if the node has a parent. If not, return None
    - If node.parent exists, continue to traverse parents until we find a node which is the left child of another node
        - Return this parent (of left child) node
    - If the parent nodes are only smaller than the initial node value, then there are no successor nodes
    """
    if not node:
        return None
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    if not node.parent:
        return None
    while node.parent:
        if node == node.parent.left:
            return node.parent
        node = node.parent
    return None


class TestSuccessor(TestCase):
    def testA(self):
        tree = TreeNode(17)
        tree.left = TreeNode(6)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(12)
        tree.left.right.left = TreeNode(9)
        tree.left.right.right = TreeNode(15)

        tree.left.parent = tree
        tree.left.left.parent = tree.left
        tree.left.right.parent = tree.left
        tree.left.right.left.parent = tree.left.right
        tree.left.right.right = tree.left.right

        self.assertEqual(successor(tree.left).value, 9)

    def testB(self):
        tree = TreeNode(17)
        tree.left = TreeNode(6)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(12)
        tree.left.right.left = TreeNode(9)
        tree.left.right.right = TreeNode(15)

        tree.left.parent = tree
        tree.left.left.parent = tree.left
        tree.left.right.parent = tree.left
        tree.left.right.left.parent = tree.left.right
        tree.left.right.right.parent = tree.left.right

        self.assertEqual(successor(tree), None)

    def testC(self):
        tree = TreeNode(17)
        tree.left = TreeNode(6)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(12)
        tree.left.right.left = TreeNode(9)
        tree.left.right.right = TreeNode(15)

        tree.left.parent = tree
        tree.left.left.parent = tree.left
        tree.left.right.parent = tree.left
        tree.left.right.left.parent = tree.left.right
        tree.left.right.right.parent = tree.left.right

        self.assertEqual(successor(tree.left.right).value, 15)


if __name__ == "__main__":
    unittest.main()