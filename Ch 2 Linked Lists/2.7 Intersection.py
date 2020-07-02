""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList


def intersection(first_llist: object, second_llist: object) -> object:
    """ Finds the node that intersects two linked lists.

    Idea:
    - If we store all node objects from one linked list into a dictionary, we can check all nodes from the other linked
    list and see if it was also in the first one

    Approach:
    - Loop through all nodes in first linked list and store the nodes as keys
    - Loop through all nodes in second linked list
        - If the node exists as a key in the dictionary, return True
        - If we loop through all nodes without finding any mathces, return False

    Alternative:
    - Instead of storing every object into a dictionary from the first linked list, we observe the pattern that if two
    linked lists intersect at a node, then all nodes from that intersecting node to the tail nodes of both linked lists
    must also be the same.
    - We can use this knowledge by first finding the lengths of both linked lists. We also check that the two linked
    lists have the same tail node. Then, we make the linked lists' lengths equal if they aren't already by moving our
    starting pointer of the longer linked list. As we traverse the two linked lists, we will find the intersecting node.
    """
    node_dict = {}
    node = first_llist.get_head()
    while node:
        node_dict[node] = True
        node = node.next

    check = second_llist.get_head()
    while check:
        if check in node_dict:
            return check
        check = check.next
    return None


class TestIntersection(TestCase):
    def testA(self):
        tail_llist = LinkedList([3, 4, 6])
        first_llist = LinkedList([1, 2])
        first_llist.append_tail(tail_llist)
        second_llist = LinkedList([5, 7, 9])
        second_llist.append_tail(tail_llist)
        actual = intersection(first_llist, second_llist).value
        expected = 3
        self.assertEqual(actual, expected)

    def testB(self):
        tail_llist = LinkedList([9, 4, 6])
        first_llist = LinkedList([1, 1, 1])
        first_llist.append_tail(tail_llist)
        second_llist = LinkedList([1, 1, 1])
        second_llist.append_tail(tail_llist)
        actual = intersection(first_llist, second_llist).value
        expected = 9
        self.assertEqual(actual, expected)

    def testC(self):
        tail_llist = LinkedList([11, 3, 1])
        first_llist = LinkedList([1, 2, 7, 10])
        first_llist.append_tail(tail_llist)
        second_llist = LinkedList([5, 7, 9])
        second_llist.append_tail(tail_llist)
        actual = intersection(first_llist, second_llist).value
        expected = 11
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()