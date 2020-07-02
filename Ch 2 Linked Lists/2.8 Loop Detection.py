""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C - > D -> E -> C [the same C as earlier)
Output: C
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList


def loop_detection(llist: object) -> object:
    """ Determines the node at the beginning of the cycle in a linked list.

    Assumption:
    - The input linked list contains a cycle

    Idea:
    - Use Tortoise and Hare algorithm to identify the start of cycle
    - Have two pointers, slow (tortoise) and fast (hare) that start at the head of linked list
    - Slow traverses the linked list one node at a time while fast moves two nodes at a time
    - Since we are assuming the linked list contains a cycle, the algorithm states that the two pointers will eventually
    intersect at a node. However, this node is not necessarily the beginning node of the cycle
    - To find the beginning node, start the slow pointer from the linked list head and move both pointers one node at a
    time. Once they intersect again, we will have found the beginning node of the cycle

    Complexity:
    - Time: O(N) -> needs to loop through entire linked list
    - Space: O(1) -> constant space for three pointers (head, slow, fast)

    Approach:
    - Loop through linked list until slow and fast pointer intersect
    - Loop through linked list again until they intersect, return the node

    Alternative (Brute Force):
    - Loop through nodes in linked list and store all nodes into a dictionary
    - If we find a node that is already in the dictionary, then return it
    - Requires O(N) time to loop through elements and O(N) space to store N nodes in the linked list
    """
    head = llist.get_head()
    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


class TestLoopDetection(TestCase):
    def testA(self):
        llist = LinkedList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        node = llist.get_head()
        tail = llist.get_tail()
        tail.next = node

        node = loop_detection(llist)
        actual = node.value
        expected = 'A'
        self.assertEqual(actual, expected)

    def testB(self):
        llist = LinkedList([1, 2, 3, 4, 5])
        node = llist.get_head()
        node = node.next.next
        tail = llist.get_tail()
        tail.next = node

        node = loop_detection(llist)
        actual = node.value
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()