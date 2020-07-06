""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList
from linked_list import Node


def partition(llist: object, x: int) -> object:
    """ Partitions a linked list so that all nodes with values greater or equal to x is on the right partition and all
    nodes with values less than x are on the left partition

    Idea:
    - Create two linked lists, one for the left partition and the other for the right partition

    Complexity:
    - Time: O(N) - loop through all nodes to determine which partition to add it to
    - Space: O(N) - need two linked lists that will store a total of N elements

    Approach:
    - Loop through the original list and add each node to the left or right partition depending on its value
    - When finished looping, merge the two partitions
    """
    greater_head = Node(-1)
    greater_node = greater_head
    lesser_head = Node(-1)
    lesser_node = lesser_head

    node = llist.get_head()
    while node:
        if node.value >= x:
            greater_node.next = node
            greater_node = greater_node.next
        else:
            lesser_node.next = node
            lesser_node = lesser_node.next
        node = node.next
    llist.set_head(lesser_head.next)
    lesser_node.next = greater_head.next
    greater_node.next = None
    return llist


class TestPartition(TestCase):
    def testA(self):
        llist = partition(LinkedList([1, 5, 7, 4, 10, 9]), 6)
        actual = llist.get_values()
        expected = [1, 5, 4, 7, 10, 9]
        self.assertEqual(actual, expected)

    def testB(self):
        llist = partition(LinkedList([8, 5, 7, 4, 6, 10, 9]), 6)
        actual = llist.get_values()
        expected = [5, 4, 8, 7, 6, 10, 9]
        self.assertEqual(actual, expected)

    def testC(self):
        llist = partition(LinkedList([23, 11, 3, 41, 57, 32, 20, 5]), 33)
        actual = llist.get_values()
        expected = [23, 11, 3, 32, 20, 5, 41, 57]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()