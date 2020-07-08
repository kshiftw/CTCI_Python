""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
import unittest
from unittest import TestCase
from tree import TreeNode


def validate_bst(node: object) -> bool:
    """ Check if a binary tree is a binary search tree.

    Assumption:
    - All tree node values are unique.

    Idea:
    - Binary Search Tree iff all nodes in left subtree are less than parent and all nodes in right subtree are greater
    than parent

    Complexity:
    - Time: O(N) - must traverse through all tree nodes in order to determine BST validity
    - Space: O(N) - need to store nodes into queue

    Approach:
    - BST to traverse the tree -> use a queue
        - Returns false as soon as we see a node where left isn't less than parent or right isn't greater
    - Keep track of minimum and maximum values
        - When we traverse to a left child, we know that all of its children MUST be less than its value for the tree
        to be a valid BST
        - Similar idea with the right child, but values must all be greater than the parent value
    """
    if not node:
        return False
    queue = [(node, float('-inf'), float('inf'))]
    while queue:
        current_elem = queue.pop(0)
        current = current_elem[0]
        minimum = current_elem[1]
        maximum = current_elem[2]

        if current.left:
            if current.left.value < current.value and minimum < current.left.value < maximum:
                queue.append((current.left, minimum, current.value))
            else:
                return False
        if current.right:
            if current.right.value > current.value and minimum < current.right.value < maximum:
                queue.append((current.right, current.value, maximum))
            else:
                return False
    return True


class TestValidateBST(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(20)
        tree.right = TreeNode(25)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(5)
        tree.right.right = TreeNode(8)

        self.assertEqual(validate_bst(tree), False)

    def testB(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(12)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(7)
        tree.right.right = TreeNode(15)

        self.assertEqual(validate_bst(tree), True)

    def testC(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(12)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(2)
        tree.right.right = TreeNode(15)

        self.assertEqual(validate_bst(tree), False)

    def testD(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(4)
        tree.right = TreeNode(7)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(8)
        tree.right.right.right = TreeNode(9)

        self.assertEqual(validate_bst(tree), True)

    def testE(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(12)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(11)
        tree.right.right = TreeNode(15)

        self.assertEqual(validate_bst(tree), False)


if __name__ == "__main__":
    unittest.main()