""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""
import unittest
from unittest import TestCase
from tree import TreeNode


def first_common_ancestor(root: object, p: object, q: object) -> object:
    """ Returns the first common ancestor node of two nodes.

    Assumption:
    - Tree is not empty
    - p and q are nodes in the tree

    Idea:
    - There are several scenarios:
        - One of the nodes is the tree root node
            - Return the root because there is no other valid ancestor
        - The two nodes are in opposite subtrees of the root (one node in the left subtree, the other in the right)
            - The first common ancestor must be the root node
        - The two nodes are in the same subtree of the root
            - Similar idea to above, but we traverse the children of the subtree until we find a split where the two
            nodes are in different subtrees. The first common ancestor would be the parent of these two subtrees.

    Complexity:
    - Time: O(N) - if both nodes are on the bottom of the same subtree, we will have accessed all nodes through the
    covers function, likely more than once
    - Space: O(N) - requires call stack that scales linear to N

    Approach:
    - Use a helper function, covers(), to determine whether a node is contained in a subtree
    - p_left represents whether p is covered in the left subtree. It will be True if it is in the left subtree and False
    if it is in the right subtree. Similar idea for q_left
    - If the two nodes are in different subtrees, then p_left will not equal q_left. Return the root
    """
    if root == p or root == q:
        return root
    p_left = covers(root.left, p)
    q_left = covers(root.left, q)
    if p_left != q_left:
        return root
    child = root.left if p_left else root.right
    return first_common_ancestor(child, p, q)


def covers(root, node):
    if not root:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


class TestFirstCommonAncestor(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(20)
        tree.left.left = TreeNode(15)
        tree.left.right = TreeNode(3)
        tree.left.right.left = TreeNode(5)
        tree.right = TreeNode(11)
        tree.right.right = TreeNode(17)
        tree.right.right.right = TreeNode(19)
        tree.right.right.left = TreeNode(14)
        tree.right.right.left.left = TreeNode(35)

        self.assertEqual(first_common_ancestor(tree, tree.left.right.left, tree.right.right.left), tree)
        self.assertEqual(first_common_ancestor(tree, tree.left.left, tree.left.right.left), tree.left)
        self.assertEqual(first_common_ancestor(tree, tree.right, tree.right.right), tree.right)


if __name__ == "__main__":
    unittest.main()