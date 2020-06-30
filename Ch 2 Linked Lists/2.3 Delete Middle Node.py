""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e-> f
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList


def delete_middle_node(middle: object) -> object:
    """ Deletes the middle node from a linked list given the middle node.

    Idea:
    - Instead of trying to change the previous node's next link, we keep it pointing to the middle node and instead,
    change the value of the middle node to its next node

    Approach:
    - Copy the next node's value and set it as the middle node's value
    - Modify the next link so that it leapfrogs over the next node
    """
    if not middle:
        return
    middle.value = middle.next.value
    middle.next = middle.next.next


class TestDeleteMiddleNode(TestCase):
    def testA(self):
        llist = LinkedList([1, 2, 3, 4, 5])
        middle_node = llist.get_head().next.next
        delete_middle_node(middle_node)
        actual = llist.get_values()
        expected = [1, 2, 4, 5]
        self.assertEqual(actual, expected)

    def testB(self):
        llist = LinkedList([1, 2, 3, 4, 5, 6])
        middle_node = llist.get_head().next.next
        delete_middle_node(middle_node)
        actual = llist.get_values()
        expected = [1, 2, 4, 5, 6]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()