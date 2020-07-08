""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList
from tree import TreeNode


def list_of_depths(tree: object) -> list:
    """ Creates list of linked lists containing the nodes at each tree depth/level.

    Idea:
    - BFS to traverse the tree by levels
    - Store LinkedLists associated to each level by using the level as the index of the list

    Complexity:
    - Time: O(N) - traverse through all nodes in the tree
    - Space: O(N) - list of linked lists will contain every one of N tree node elements

    Approach:
    - Utilize queue to do BFS through tree
        - Keep track of depth by appending it as a second element to the tuple added to the queue
    """
    lists = []
    queue = [(tree, 0)]
    while queue:
        current = queue.pop(0)
        node = current[0]
        depth = current[1]
        if depth == len(lists):
            lists.append(LinkedList([node.value]))
        else:
            lists[depth].append_tail(LinkedList([node.value]))

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return lists


class TestListOfDepths(TestCase):
    def testA(self):
        tree = TreeNode(10)
        tree.left = TreeNode(20)
        tree.right = TreeNode(25)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(5)
        tree.right.right = TreeNode(8)

        lists = list_of_depths(tree)
        values_list = []
        for llist in lists:
            values_list.append(llist.get_values())
        self.assertEqual(values_list, [[10], [20, 25], [3, 5, 8]])

    def testB(self):
        tree = TreeNode('Cat')
        tree.left = TreeNode('Dog')
        tree.right = TreeNode('Mouse')
        tree.left.left = TreeNode('Pig')
        tree.left.right = TreeNode('Sheep')
        tree.right.right = TreeNode('Bison')
        tree.right.right.right = TreeNode('Buffalo')
        tree.left.left.right = TreeNode('Fish')
        tree.left.left.right.left = TreeNode('Horse')

        lists = list_of_depths(tree)
        values_list = []
        for llist in lists:
            values_list.append(llist.get_values())
        self.assertEqual(values_list, [['Cat'], ['Dog', 'Mouse'], ['Pig', 'Sheep', 'Bison'], ['Fish', 'Buffalo'],
                                       ['Horse']])


if __name__ == "__main__":
    unittest.main()