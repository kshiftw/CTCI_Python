""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) .That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP. Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList
from linked_list import Node


def sum_lists(first_llist: object, second_llist: object) -> int:
    """ Return the sum of two linked lists representing the reverse order of digits in a number.

    Idea:
    - Since the numbers are in reversed order, it is straightforward to use simple addition to add each digit, starting
    from the ones digit. In addition, we need to keep track of the carry bit if the digit sum is greater than 10

    Complexity:
    - Time: O(M+N) - loop through all M elements of first linked list and all N elements of second linked list
    - Space: O(N) - sum_llist will be a linked list of size N

    Approach:
    - Loop through all nodes of both linked lists and calculate the sum of the corresponding digits
    - Create a new linked list, sum_llist, that appends the sum as a new node
    """
    sum_llist = LinkedList()
    sum_node = None
    carry = 0
    first_node = first_llist.get_head()
    second_node = second_llist.get_head()

    while first_node or second_node:
        if first_node and second_node:
            curr_sum = first_node.value + second_node.value
            first_node = first_node.next
            second_node = second_node.next
        elif first_node and not second_node:
            curr_sum = first_node.value
            first_node = first_node.next
        elif not first_node and second_node:
            curr_sum = second_node.value
            second_node = second_node.next

        if carry == 1:
            curr_sum += 1
        if curr_sum >= 10:
            carry = 1
            curr_sum -= 10
        else:
            carry = 0

        if not sum_node:
            sum_node = Node(curr_sum)
            sum_llist.set_head(sum_node)
        else:
            sum_node.next = Node(curr_sum)
            sum_node = sum_node.next
    return sum_llist


class TestSumLists(TestCase):
    def testA(self):
        sum_llist = sum_lists(LinkedList([7, 1, 6]), LinkedList([5, 9, 2]))
        actual = sum_llist.get_values()
        expected = [2, 1, 9]
        self.assertEqual(actual, expected)

    def testB(self):
        sum_llist = sum_lists(LinkedList([1, 1]), LinkedList([2, 2, 2]))
        actual = sum_llist.get_values()
        expected = [3, 3, 2]
        self.assertEqual(actual, expected)

    def testC(self):
        sum_llist = sum_lists(LinkedList([5, 9, 4, 6]), LinkedList([8, 5]))
        actual = sum_llist.get_values()
        expected = [3, 5, 5, 6]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()