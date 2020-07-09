""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
Example:
    2
  1   3
Output: [2, 1, 3], [2, 3, 1]
"""
import unittest
from unittest import TestCase
from tree import TreeNode


def bst_sequences(root):
    """ 
    Not my own solution. Taken from: https://stackoverflow.com/questions/21211701. This one had multiple recursions that
    I would not have been able to figure out by myself.
    """
    if not root:
        return []

    answer = []
    prefix = [root.value]
    left = bst_sequences(root.left) or [[]]
    right = bst_sequences(root.right) or [[]]

    # take all sequences of the left and right subtrees and weave every combination
    for i in range(len(left)):
        for j in range(len(right)):
            weaved = []
            weave(left[i], right[j], weaved, prefix)
        answer.extend(weaved)
    return answer


def weave(first, second, results, prefix):
    if not first or not second:
        results.append(prefix + first + second)
        return

    # add element to prefix and recurse until either first or second empty
    first_head = first[0]
    first_remain = first[1:]
    weave(first_remain, second, results, prefix + [first_head])

    second_head = second[0]
    second_remain = second[1:]
    weave(first, second_remain, results, prefix + [second_head])


class TestBSTSequences(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(12)
        tree.left.left = TreeNode(3)

        self.assertEqual(bst_sequences(tree), [[10, 5, 3, 12], [10, 5, 12, 3], [10, 12, 5, 3]])


if __name__ == "__main__":
    unittest.main()