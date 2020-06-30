""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList


def kth_to_last(llist: object, k: int) -> object:
    """ Returns a Node object of the kth to last element of a linked list.

    Assume k is less than or equal to the size of the linked list.

    Idea:
    - Once we know the size of the linked list, we can use it to find the number of nodes from the head is required to
    get the kth to last element

    Approach:
    - Perform two loops:
        - The first loop traverses the linked list to get the size
        - The second loop traverses size - k nodes, which is when we reach the kth to last element

    Alternative:
    - Use two pointers starting at head
        - Move p2 for k steps so that p1 and p2 are k nodes apart
        - Move p1 and p2 both one node at a time until p2 hits the end
        - p1 will be k nodes from the end
    """
    size = 0
    head = llist.get_head()
    node = head
    while node:
        size += 1
        node = node.next
    node = head
    index = size - k
    for _ in range(index):
        node = node.next
    return node


class TestKthToLast(TestCase):
    def testA(self):
        node = kth_to_last(LinkedList([1, 2, 3, 4, 5]), 2)
        actual = node.value
        expected = 4
        self.assertEqual(actual, expected)

    def testB(self):
        node = kth_to_last(LinkedList([1, 2, 3, 4, 5]), 4)
        actual = node.value
        expected = 2
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()