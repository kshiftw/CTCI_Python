""" Cracking the Coding Interview, 6th Edition - Python Solutions
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
"""
import unittest
from unittest import TestCase
from linked_list import LinkedList


def palindrome(llist: object) -> bool:
    """ Checks if a linked list is a palindrome.

    Idea:
    - Use a stack to store the values of half of the linked list
    - Remove the elements from the stack and compare against the other half of the linked list
    - If there is a mismatch, then it is not a palindrome

    Complexity:
    - Time: O(N) - will traverse through all nodes of the linked list
    - Space: O(N) - need a stack that stores N/2 elements

    Approach:
    - Calculate the length by looping through the linked list until the end
    - Use the length to loop through half the of the linked list, storing the node values into a stack
    - Loop through the other half and compare against the popped values from the stack

    Alternative:
    - Instead of having the loop to calculate length first, we can utilize two pointers - slow and fast
        - Slow moves one node at a time while fast moves two nodes
        - Node values from slow pointer will be added to a stack
        - Once fast hits the end, slow will be in the middle of the linked list
        - Continue moving slow pointer until the end while comparing its values to popped values from the stack
    """
    if not llist or not llist.get_head():
        return False

    head = llist.get_head()
    node = head
    length = 0
    stack = []

    while node:
        length += 1
        node = node.next
    node = head
    for _ in range(length // 2):
        stack.append(node.value)
        node = node.next
    if length % 2 != 0:
        node = node.next
    for _ in range(length // 2):
        check = stack.pop()
        if check != node.value:
            return False
        node = node.next
    return True


class TestPalindrome(TestCase):
    def testA(self):
        actual = palindrome(LinkedList(['r', 'a', 'd', 'a', 'r']))
        expected = True
        self.assertEqual(actual, expected)

    def testB(self):
        actual = palindrome(LinkedList([1, 3, 5, 7, 5, 3, 1]))
        expected = True
        self.assertEqual(actual, expected)

    def testC(self):
        actual = palindrome(LinkedList([1, 2, 3, 5, 3, 2, 3]))
        expected = False
        self.assertEqual(actual, expected)

    def testD(self):
        actual = palindrome(LinkedList(['k', 'a', 'y', 'a', 'k']))
        expected = True
        self.assertEqual(actual, expected)

    def testE(self):
        actual = palindrome(LinkedList(['k', 'i', 't', 'e']))
        expected = False
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()