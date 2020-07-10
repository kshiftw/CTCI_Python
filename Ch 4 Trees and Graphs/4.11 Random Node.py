""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.11 Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
"""
import unittest
from unittest import TestCase
import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def get_random_node(self):
        """ Returns a random node from the binary search tree.

        Idea:
        - If we are able to keep track of each subtree size (ie. the number of nodes in a subtree including the root),
        then we are able to calculate the probability of selecting a node in order to have an overall equal probability
        of 1/N for each node
            - At each node, the probability of entering the left subtree is equal to the size of the left subtree * 1/N
                This is similar for the right subtree
        Example:
             10
           /    \
          5     15
         / \   /
        3  7  12

        - each node has a probability of 1/6 to be selected
        - From the root, 1/6 chance is to select 10, 3/6 chance is to select the left subtree (5) and 2/6 chance to
        select right subtree (15)

        Complexity:
        - Time: O(log(N)) - may traverse the entire depth of the tree if it selects a leaf node
        - Space: O(log(N)) - similarly, call stack will at most have log(N) calls of get_random_node()

        Approach:
        - Generate a random integer from 0 to size - 1 (inclusive) at each step to determine whether we select the root
        or select a node from either the left or right subtree
        - Eventually, we will either generate a random number that returns the root of a non-leaf node or we will reach
        a leaf node where left_size will be 0 and index will always generate 0, meaning we return the node
        """
        left_size = 0 if not self.left else self.left.size
        index = random.randint(0, self.size - 1)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def insert(self, value):
        if value <= self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        # every time we insert a node, add 1 to size
        # size represents the number of nodes in its subtrees including the root itself
        self.size += 1


class TestRouteBetweenNodes(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.insert(5)
        tree.insert(3)
        tree.insert(15)
        tree.insert(12)
        tree.insert(7)
        print('Random node value is:', tree.get_random_node().value)


if __name__ == "__main__":
    unittest.main()