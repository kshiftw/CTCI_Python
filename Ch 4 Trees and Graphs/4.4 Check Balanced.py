""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
import unittest
from unittest import TestCase
from tree import TreeNode


def check_balanced(tree: object) -> bool:
    """ Check if a binary tree is balanced.

    Idea:
    - For each node, if it is balanced, recursively call check_balanced to determine whether the children are balanced

    Complexity:
    - Time: O(N*log(N))
    - Space:

    Approach:
    - A subtree is balanced if the height_diff is less than or equal to 1
        - This tells us that the current tree is balanced, however we still want to determine if all of its subtrees
        are also balanced, which is why we only return True if check_balanced() of the left and right subtrees are True
    """
    if not tree:
        return True
    height_diff = abs(get_height(tree.left) - get_height(tree.right))
    if height_diff <= 1:
        return check_balanced(tree.left) and check_balanced(tree.right)
    else:
        return False


def get_height(node):
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1


class TestCheckBalanced(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(20)
        tree.right = TreeNode(25)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(5)
        tree.right.right = TreeNode(8)

        self.assertEqual(check_balanced(tree), True)

    def testB(self):
        tree = TreeNode(10)
        tree.left = TreeNode(20)
        tree.right = TreeNode(25)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(5)
        tree.right.right = TreeNode(8)
        tree.right.right.right = TreeNode(13)

        self.assertEqual(check_balanced(tree), False)


if __name__ == "__main__":
    unittest.main()