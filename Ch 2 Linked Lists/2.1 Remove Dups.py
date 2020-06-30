""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.1 Remove Duplicates: Write code to remove duplicates from an unsorted linked list.
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList


def remove_duplicates(llist: object) -> object:
    """ Removes all duplicates from a linked list.

    Idea:
    - We need to remove all values that appear more than once
    - A dictionary helps us with keeping track of values we have already seen

    Approach:
    - Traverse the linked list and use a dictionary to keep track of values we have already seen
        - Keep track of the previous node while traversing
        - If the current node's value is one that we have already seen, modify the previous node's next link to the
        current node's next node. This essentially "deletes" the node from our linked list
            Before: prev -> curr -> curr.next
            After: prev -> curr.next

    """
    head = llist.get_head()
    if not head:
        return
    node = head
    val_dict = {}
    while node:
        if node.value in val_dict:
            prev.next = node.next
        else:
            val_dict[node.value] = True
            prev = node
        node = node.next
    return llist


class TestRemoveDuplicates(TestCase):
    def testA(self):
        result = remove_duplicates(LinkedList([1, 2, 3, 4, 1]))
        actual = result.get_values()
        expected = LinkedList([1, 2, 3, 4]).get_values()
        self.assertEqual(actual, expected)

    def testB(self):
        result = remove_duplicates(LinkedList([1, 1, 1, 1, 1]))
        actual = result.get_values()
        expected = LinkedList([1]).get_values()
        self.assertEqual(actual, expected)

    def testC(self):
        result = remove_duplicates(LinkedList([1, 3, 3, 1, 1]))
        actual = result.get_values()
        expected = LinkedList([1, 3]).get_values()
        self.assertEqual(actual, expected)

    def testD(self):
        result = remove_duplicates(LinkedList([1]))
        actual = result.get_values()
        expected = LinkedList([1]).get_values()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()